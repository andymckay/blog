import xml.etree.ElementTree as etree
from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor
import re
import json
import os
import hashlib
import gpxo
from rendergpx import generate_map
from pathlib import Path
from jinja2 import Environment, BaseLoader

gpx_re = r"\[(?P<prefix>gpx#)(?P<activity_number>\w+)\]"

description_html = Environment(loader=BaseLoader).from_string("""
<div class="gpx">
    <div class="row align-items-start">
        <div class="col">
            <h5>Distance</h5>
            <p>{% if distance %}{{ distance }} km{% else %}Unknown{% endif %}</p>
        </div>
        <div class="col">
            <h5>Time</h5>
            <p>Elapsed: {{ elapsed }}{% if moving_time_seconds %}<br />
            Moving: {{moving }} {% endif %}</p>
        </div>
        <div class="col">
            {% if elevation_gain %}
                <h5>Elevation</h5>
                <p><span title="Elevation gain">📈 {{ elevation_gain }} m</span>
                {% if elevation_path %}<br>
                ℹ️ <a href="#elevation-profile-{{ uid }}" data-bs-toggle="collapse">Click for profile</a>{% endif %}</p>
            {% endif %}
        </div>
    </div>
    <div class="row collapse" id="elevation-profile-{{ uid }}">
        <img src="/files/gpx/{activity_id}/elevation.png" class="img-fluid" />
    </div>
""")

activity_html_start = """
    <div class="row">
        <iframe src="/files/gpx/{activity_id}/route.html" width="100%" frameborder="0"></iframe>
    </div>
    <div class="row">
        <div class="carousel slide col-md-12" id="carousel-id-{uid}">
            <div class="carousel-inner">
"""

activity_html_photo = """
                <div class="carousel-item {active}">
                    <img src="/files/gpx/{activity_id}/{photo}.jpg" class="img-fluid photo">
                </div>
"""

activity_html_end = """
            </div>
        </div>
    </div>
"""

gpx_end = """
</div>
<div class="carousel-controls d-flex justify-content-center my-2">
        <button type="button" class="col-auto me-auto btn btn-outline-secondary" data-bs-target="#carousel-id-{uid}" data-bs-slide="prev">Previous</button>
        <button type="button" class="col-auto btn btn-outline-secondary" data-bs-target="#carousel-id-{uid}" data-bs-slide="next">Next</button>
</div>
"""

gpx_end_no_photos = """
</div>
<div class="carousel-controls d-flex justify-content-center my-2">
</div>
"""

carousel_html_element = """
        <div>
            <h4><a id="carousel-{uid}-{k}"></a>{description}</h4>
            <img src="{url}" class="img-fluid photo">
            {caption}
            <hr>
        </div>
"""

carousel_caption = """
    <div class="img-fluid photo-caption">
        <p class="exifdata">
          {model} &bull; {lens}<br />
          ISO: {iso} &bull; Aperture: {aperture} &bull; Shutter speed: {shutter}
        </p>
    </div>
"""

class GPXExtension(Extension):
    def extendMarkdown(self, md):
        gpx_tag = GPXProcessor(gpx_re, md)
        md.inlinePatterns.register(gpx_tag, "gpx", 175)


def update_activity(activity):
    activity['elapsed'] = f"{activity['elapsed_time_seconds'] // 3600}h {(activity['elapsed_time_seconds'] % 3600) // 60}m"
    if activity['moving_time_seconds']:
        activity['moving'] = f"{activity['moving_time_seconds'] // 3600}h {(activity['moving_time_seconds'] % 3600) // 60}m"
    else:
        activity['moving'] = "Unknown"
    if activity['distance_meters']:
        activity['distance'] = f"{activity['distance_meters'] / 1000:.2f}"
    else:
        activity['distance'] = "Unknown"
    

class GPXProcessor(InlineProcessor):
    def handleMatch(
        self, match: re.Match[str], data: str
    ) -> tuple[etree.Element | str, int, int]:
        activity_number = match.group("activity_number")

        if not os.path.exists(f"docs/files/gpx/{activity_number}"):
            raise ValueError(f"GPX for activity {activity_number} not found")
        
        activity_path = f"docs/files/gpx/{activity_number}/activity.json"
        gpx_path = f"docs/files/gpx/{activity_number}/route.gpx"
        route_path = f"docs/files/gpx/{activity_number}/route.html"
        elevation_path = f"docs/files/gpx/{activity_number}/elevation.png"

        if not os.path.exists(activity_path):
            # generate activity.json if info we can figure out from the GPX file
            gpx_path = f"docs/files/gpx/{activity_number}/route.gpx"
            if not os.path.exists(gpx_path):
                raise ValueError(f"GPX file for activity {activity_number} not found")
            
            track = gpxo.Track(gpx_path)
            elapsed_time_seconds = (track.data.values[-1][2] - track.data.values[0][2]).seconds
            data = {
                "elapsed_time_seconds": elapsed_time_seconds,
                "moving_time_seconds": None,
                # Coros has GPX in the extensions.
                "distance_meters": float(track._load_points()[-1].extensions[1].text),    
                "photos": [],
                "elevation_gain": None,
                "activity_id": activity_number
            }
            with open(activity_path, "w", encoding="utf8") as f:
                json.dump(data, f, indent=4)

        
        if not os.path.exists(route_path):
            generate_map(Path(gpx_path))

        activity = json.load(open(activity_path, "r", encoding="utf8"))
        activity["elevation_path"] = os.path.exists(elevation_path)

        update_activity(activity)
        activity["uid"] = activity_number
        html = description_html.render(**activity)
        html += activity_html_start.format(**activity)
        for k, photo in enumerate(activity["photos"]):
            html += activity_html_photo.format(**activity, photo=photo, active="active" if not k else "")
        html += activity_html_end.format(**activity)
        if activity["photos"]:
            html += gpx_end.format(**activity)
        else:
            html += gpx_end_no_photos.format(**activity)

        el = etree.Element("div")
        el.text = self.md.htmlStash.store(html)
        return el, match.start(0), match.end(0)

class CarouselExtension(Extension):
    def __init__(self, *args, **kw):
        self.exifdata = kw.pop("exifdata")
        super().__init__(*args, **kw)

    def extendMarkdown(self, md):
        md.preprocessors.register(CarouselProcessor(md, exifdata=self.exifdata), "carousel", 25)

carousel_start = re.compile(r"^\[carousel\]")

class CarouselProcessor(Preprocessor):
    
    def __init__(self, *args, **kw):
        self.exifdata = kw.pop("exifdata")
        super().__init__(*args, **kw)

    def run(self, lines):
        in_carousel = False
        imgs = []
        output = []
        for line in lines:
            if in_carousel:
                imgs.append(line.strip())

                if not line.strip():
                    uid = hashlib.md5("".join(imgs).encode('utf-8')).hexdigest()
                    in_carousel = False
                    html = ""
                    for (k, img) in enumerate(imgs):
                        if (img.strip()):
                            exif = self.exifdata.get(img.strip(), {})
                            if exif:
                                caption = carousel_caption.format(uid=uid, k=k, **exif)
                            else:
                                caption = ""    
                            html += carousel_html_element.format(uid=uid, k=k, url=img, active="active" if not k else "", caption=caption, **exif)
                    placeholder = self.md.htmlStash.store(html.strip())
                    output.append(placeholder)

                continue

            if carousel_start.match(line):
                in_carousel = True

            else:
                output.append(line)
        
        return output