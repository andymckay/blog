import xml.etree.ElementTree as etree
from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor
import re
import json
import os

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
            <p>{elapsed}</p>
        </div>
        <div class="col">
            <h5>Elevation</h5>
            <p><span title="Elevation gain">📈 {elevation_gain} m</span></p>
        </div>
    </div>
"""

activity_html = """
    <div class="row">
        <div class="col-md-6">
            <img src="/files/gpx/{activity_id}/route.png" class="img-fluid" />
        </div>
        <div class="col-md-6">
            {photo}
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <img src="/files/gpx/{activity_id}/elevation.png" class="img-fluid" />
        </div>
    </div>
"""

gpx_end = """
</div>"""

carousel_html_start = """
<div class="carousel slide col-md-12">
    <div class="carousel-inner">
"""

carousel_html_end = """
    <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
    </div>
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
        html = description_html.format(**activity)
        if not activity["photos"]:
            print(f"No photos for activity {activity_number}")
            photo = ""
        else:
            photo = activity["photos"][0]
            photo = f'<img src="/files/gpx/{activity_number}/{photo}.jpg" class="img-fluid photo" />'
        html += activity_html.format(**activity, photo=photo)
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
                    in_carousel = False
                    html = carousel_html_start
                    for (k, img) in enumerate(imgs):
                        if (img.strip()):
                            exif = self.exifdata.get(img.strip(), {})
                            if exif:
                                caption = carousel_caption.format(**exif)
                            else:
                                caption = ""    
                            html += carousel_html_element.format(url=img, active="active" if not k else "", caption=caption)
                    html += carousel_html_end
                    placeholder = self.md.htmlStash.store(html.strip())
                    output.append(placeholder)

                continue

            if carousel_start.match(line):
                in_carousel = True

            else:
                output.append(line)
        
        return output