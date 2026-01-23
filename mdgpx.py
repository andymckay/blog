import xml.etree.ElementTree as etree
from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor
import re
import json
import os
import hashlib

gpx_re = r"\[(?P<prefix>gpx#)(?P<activity_number>\d+)\]"

description_html = """
<div class="gpx">
    <div class="row align-items-start">
        <div class="col">
            <h5>Distance</h5>
            <p>{distance} km</p>
        </div>
        <div class="col">
            <h5>Time</h5>
            <p>Elapsed: {elapsed}<br />
            Moving: {moving}</p>
        </div>
        <div class="col">
            <h5>Elevation</h5>
            <p><span title="Elevation gain">📈 {elevation_gain} m</span><br>
            ℹ️ <a href="#elevation-profile-{uid}" data-bs-toggle="collapse">Click for profile</a></p>
        </div>
    </div>
    <div class="row collapse" id="elevation-profile-{uid}">
        <img src="/files/gpx/{activity_id}/elevation.png" class="img-fluid" />
    </div>
"""

activity_html_start = """
    <div class="row">
        <div class="carousel slide col-md-12" id="carousel-id-{uid}">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="/files/gpx/{activity_id}/route.png" class="img-fluid photo">
                </div>
"""

activity_html_photo = """
                <div class="carousel-item">
                    <img src="/files/gpx/{activity_id}/{photo}.jpg" class="img-fluid photo">
                </div>
"""

activity_html_end = """
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carousel-id-{uid}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carousel-id-{uid}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </div>
"""

gpx_end = """
</div>"""

carousel_html_start = """
<div class="carousel slide col-md-12" id="carousel-id-{uid}">
    <div class="carousel-inner">
"""

carousel_html_end = """
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carousel-id-{uid}" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carousel-id-{uid}" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
"""

carousel_html_element = """
        <div class="carousel-item {active}">
            <img src="{url}" class="d-block w-100">
            {caption}
        </div>
"""

carousel_caption = """
    <div class="carousel-caption d-none d-md-block fs-6">
        <p>
          <b>{description}</b><br />
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
    activity['moving'] = f"{activity['moving_time_seconds'] // 3600}h {(activity['moving_time_seconds'] % 3600) // 60}m"
    activity['distance'] = f"{activity['distance_meters'] / 1000:.2f}"

class GPXProcessor(InlineProcessor):
    def handleMatch(
        self, match: re.Match[str], data: str
    ) -> tuple[etree.Element | str, int, int]:
        activity_number = match.group("activity_number")

        if not os.path.exists(f"docs/files/gpx/{activity_number}"):
            raise ValueError(f"GPX for activity {activity_number} not found")
        
        activity = json.load(open(f"docs/files/gpx/{activity_number}/activity.json", "r", encoding="utf8"))
        update_activity(activity)
        html = description_html.format(**activity, uid=activity_number)
        html += activity_html_start.format(**activity, uid=activity_number)
        for photo in activity["photos"]:
            html += activity_html_photo.format(**activity, photo=photo, uid=activity_number)
        html += activity_html_end.format(**activity, uid=activity_number)
        html += gpx_end

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
                    html = carousel_html_start.format(uid=uid)
                    for (k, img) in enumerate(imgs):
                        if (img.strip()):
                            exif = self.exifdata.get(img.strip(), {})
                            if exif:
                                caption = carousel_caption.format(**exif)
                            else:
                                caption = ""    
                            html += carousel_html_element.format(url=img, active="active" if not k else "", caption=caption)
                    html += carousel_html_end.format(uid=uid)
                    placeholder = self.md.htmlStash.store(html.strip())
                    output.append(placeholder)

                continue

            if carousel_start.match(line):
                in_carousel = True

            else:
                output.append(line)
        
        return output