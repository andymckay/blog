import os
import markdown
import yaml
import jinja2
import shutil
import datetime
import sys
from bs4 import BeautifulSoup
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from stravalib import Client as StravaClient
import json
import os
from dotenv import load_dotenv

json_path = os.path.join(".strava.json")
with open(json_path, "r") as f:
    token_refresh = json.load(f)

load_dotenv()

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

    def url(self):
        return self.filename.replace(".md", ".html")
    
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
        words = BeautifulSoup(self.html, features="html.parser").get_text().strip().split()
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
    
def double_posts(posts):
    return [posts[i : i + 2] for i in range(0, len(posts), 2)]

def sort_posts(posts):
    posts.sort(key=lambda post: post.date().strftime('%Y-%m-%d'), reverse=True)
    return posts
    
def build():
    template = jinja2.Environment(loader=jinja2.FileSystemLoader("template"))
    templates = {}
    for name in ["post", "category", "index", "page", "404"]:
        templates[name] = template.get_template(f"{name}.html")
    templates["atom"] = template.get_template("atom.xml")

    def write(target, __template, **kwargs):
        with open(os.path.join("docs", target), "w") as f:
            t = templates[__template]
            f.write(t.render(**kwargs))

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
                    md = markdown.Markdown(extensions=["toc"])
                    content.body = "\n".join(body)
                    content.html = md.convert("\n".join(body))
                    content.toc = md.toc
                except Exception as e:
                    print(f"Error processing Markdown in {filename}: {e}")
                    continue

        if content.meta.get("categories"):
            content.meta["categories"] = [
                c.strip().capitalize() for c in content.meta["categories"].split(",")
            ]
            for category in content.meta["categories"]:
                categories.setdefault(category, [])
                categories[category].append(content)

        write(filename.replace(".md", ".html"), content.template, content=content)

        if isinstance(content, Post):
            posts.append(content)
    
    posts = sort_posts(posts)

    for category in sorted(categories):
        context = {
            "category": category,
            "post_rows": double_posts(sort_posts(categories[category]))
        }
        write(category.lower() + ".html", "category", **context)

    context = {
        "first": posts[0],
        "post_rows": double_posts(posts[1:5]), 
        "gear_posts": sort_posts(categories["Gear"])
    }
    write("index.html", "index", **context)

    def filtered_posts(posts):
        earliest = datetime.datetime.strptime(
            "-".join("2025-09-04".split("-", 3)[:3]), "%Y-%m-%d"
        ).date()

        filtered = []
        for post in posts:
            if post.date() > earliest:
                print("adding post", post.meta["title"])
                filtered.append(post)

        return filtered

    context = {
        "now": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "posts": filtered_posts(posts)
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

    else:
        build()
