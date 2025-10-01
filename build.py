import http
import os
import socketserver
import markdown
import yaml
import jinja2
import shutil
import datetime
import sys
import json
import http.server
import time
from bs4 import BeautifulSoup
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from stravalib import Client as StravaClient




json_path = os.path.join(".strava.json")
with open(json_path, "r") as f:
    token_refresh = json.load(f)

client = StravaClient(
    access_token=token_refresh["access_token"],
    refresh_token=token_refresh["refresh_token"],
    token_expires=token_refresh["expires_at"],
)

with open("images.json", "r") as f:
    images = json.load(f)


class Content:
    def __init__(self, filename="", meta=None, body="", html="", toc="", category=""):
        self.filename = filename
        self.meta = meta
        self.body = body
        self.html = html
        self.toc = toc
        self.category = category

    def target_filename(self):
        return self.filename.replace(".md", ".html")

    def url(self):
        return self.target_filename()


class Post(Content):
    def __init__(self, filename="", meta=None, body="", html="", toc="", category=""):
        super().__init__(filename, meta, body, html, toc, category)
        self.template = "post"

    def date(self):
        return datetime.datetime.strptime(
            "-".join(self.filename.split("-", 3)[:3]), "%Y-%m-%d"
        ).date()

    def nice_date(self):
        return self.date().strftime("%B %d, %Y")

    def lead_in(self):
        if self.meta.get("lead_in"):
            return self.meta["lead_in"]
        words = (
            BeautifulSoup(self.html, features="html.parser").get_text().strip().split()
        )
        return " ".join(words[:15]) + "..."

    def date_xml(self):
        return self.date().isoformat() + "T00:00:00+00:00"

    def strava_image_url(self):
        if self.meta.get("image"):
            return self.meta["image"]

        if self.filename in images:
            return images[self.filename]

        print("Fetching Strava image for", self.filename)
        soup = BeautifulSoup(self.html, features="html.parser")
        url = None
        for embed in soup.find_all("div", class_="strava-embed-placeholder"):
            if embed["data-embed-type"] == "activity":
                strava_id = embed["data-embed-id"]
                activity = client.get_activity(strava_id)
                try:
                    url = activity.photos.primary.urls["600"]
                    break
                except AttributeError as e:
                    print(f"Error fetching Strava image for {strava_id}: {e}")

        images[self.filename] = url
        with open("images.json", "w") as f:
            json.dump(images, f, indent=2)


class Page(Content):
    def __init__(self, filename="", meta=None, body="", html="", toc="", category=""):
        super().__init__(filename, meta, body, html, toc, category)
        self.template = "page"


class NotFound(Content):
    def __init__(self, filename="", meta=None, body="", html="", toc="", category=""):
        super().__init__(filename, meta, body, html, toc, category)
        self.template = "404"


def getContent(filename, meta):
    if meta["layout"] == "post":
        return Post(filename=filename, meta=meta)
    if meta["layout"] == "page":
        return Page(filename=filename, meta=meta)
    if meta["layout"] == "notfound":
        return NotFound(filename=filename, meta=meta)


def capitalize(text):
    if text:
        return text[0].upper() + text[1:]
    return text


def sort_posts(posts):
    posts.sort(key=lambda post: post.date().strftime("%Y-%m-%d"), reverse=True)
    return posts


env = jinja2.Environment(loader=jinja2.FileSystemLoader("template"))
templates = {}


def category_url(category):
    return category.lower().replace(" ", "-") + ".html"


env.filters["category_url"] = category_url


def filtered_posts(posts):
    earliest = datetime.datetime.strptime(
        "-".join("2025-09-04".split("-", 3)[:3]), "%Y-%m-%d"
    ).date()

    filtered = []
    for post in posts:
        if post.date() > earliest:
            print("Adding post", post.meta["title"], "to feed.")
            filtered.append(post)

    return filtered


def write(target, __template, **kwargs):
    with open(os.path.join("docs", target), "w") as f:
        t = templates[__template]
        f.write(t.render(**kwargs))


def get_content():
    for name in ["post", "category", "index", "page", "404"]:
        templates[name] = env.get_template(f"{name}.html")
    templates["atom"] = env.get_template("atom.xml")

    print("Building site...")
    categories = {}
    posts = []

    # Sort based on date in filename.
    files = os.listdir("content")

    for filename in files:
        if filename.endswith(".md"):
            with open(os.path.join("content", filename), "r") as f:
                content = f.read()
                isHeader = False
                foundHeader = False

                header, body = [], []
                for line in content.splitlines():
                    if line.startswith("---") and not foundHeader:
                        if isHeader and not foundHeader:
                            foundHeader = True
                        isHeader = not isHeader
                        continue

                    if isHeader:
                        header.append(line)
                    else:
                        body.append(line)

                try:
                    meta = yaml.safe_load("\n".join(header))
                except Exception as e:
                    print(f"Error processing YAML in {filename}: {e}")
                    continue

                content = getContent(filename=filename, meta=meta)

                try:
                    md = markdown.Markdown(extensions=["toc", "tables"])
                    content.body = "\n".join(body)
                    content.html = md.convert("\n".join(body))
                    content.toc = md.toc
                except Exception as e:
                    print(f"Error processing Markdown in {filename}: {e}")
                    continue

        if content.meta.get("categories"):
            content.meta["categories"] = [
                capitalize(c.strip()) for c in content.meta["categories"].split(",")
            ]
            for category in content.meta["categories"]:
                categories.setdefault(category, [])
                categories[category].append(content)

        if isinstance(content, Post):
            posts.append(content)

    posts = sort_posts(posts)
    return posts, categories


def build():
    posts, categories = get_content()
    for content in posts:
        write(content.target_filename(), content.template, content=content)

    posts = sort_posts(posts)

    for category in sorted(categories):
        context = {"category": category, "posts": sort_posts(categories[category])}
        write(category_url(category), "category", **context)

    context = {
        "posts": posts[:3],
        "hike_posts": sort_posts(categories["Hiking"][:10]),
        "gear_posts": sort_posts(categories["Gear"][:10]),
    }
    write("index.html", "index", **context)

    context = {
        "now": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "posts": filtered_posts(posts),
    }
    write("atom.xml", "atom", **context)

    os.makedirs("docs/static", exist_ok=True)
    for filename in os.listdir("template/static"):
        if os.path.isdir(os.path.join("template/static", filename)):
            continue
        shutil.copy(
            os.path.join("template/static", filename),
            os.path.join("docs/static", filename),
        )

    print("Build complete.")


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.src_path.find("blog/docs") > -1:
            return
        elif event.is_directory:
            return
        else:
            print("Event detected:", event.event_type, "on file:", event.src_path)
            build()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        build()
        path = os.curdir
        observer = Observer()
        observer.schedule(Handler(), path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    if len(sys.argv) > 1 and sys.argv[1] == "--clean":
        for filename in os.listdir("docs"):
            if filename.endswith(".html"):
                os.remove(os.path.join("docs", filename))
        print("Cleaned docs directory.")

    if len(sys.argv) > 1 and sys.argv[1] == "--list-categories":
        posts, categories = get_content()
        for category in sorted(categories.keys()):
            print(category)
            for post in sort_posts(categories[category]):
                print("  ", post.filename)

    if len(sys.argv) > 1 and sys.argv[1] == "--new-post":
        today = datetime.datetime.today()
        filename = today.strftime("%Y-%m-%d") + "-post.md"
        with open("content/" + filename, "w") as f:
            f.write(
                """
---
layout: post
title:
categories:
---

Text goes here.
"""
            )
        print("New post: content/" + filename, "created.")

    if len(sys.argv) > 1 and sys.argv[1] == "--serve":
        Handler = http.server.SimpleHTTPRequestHandler
        os.chdir("docs")
        with socketserver.TCPServer(("", 8000), Handler) as httpd:
            httpd.serve_forever()
        os.chdir("..")

    else:
        print("Arguments: --watch, --clean, --list-categories, --new-post, --serve")
        build()
