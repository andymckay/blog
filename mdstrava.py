import xml.etree.ElementTree as etree
from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor
import re

strava_re = r"\[(?P<prefix>strava#)(?P<activity_number>\d+)\]"

strava_html = """
<div class="strava-embed-placeholder" 
       data-embed-type="activity" 
       data-embed-id="{activity_number}" 
       data-style="standard" 
       data-from-embed="false">
   </div>
<script src="https://strava-embeds.com/embed.js"></script>
<p class="strava-explanation"><a href="https://www.strava.com/activities/{activity_number}">View on Strava here.</a></p>
"""

carousel_html_start = """
<div id="carousel" class="carousel slide col-md-12">
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

class StravaExtension(Extension):
    def extendMarkdown(self, md):
        strava_tag = StravaProcessor(strava_re, md)
        md.inlinePatterns.register(strava_tag, "strava", 175)


class StravaProcessor(InlineProcessor):
    def handleMatch(
        self, match: re.Match[str], data: str
    ) -> tuple[etree.Element | str, int, int]:
        activity_number = match.group("activity_number")

        html = strava_html.format(activity_number=activity_number)
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
                            caption = carousel_caption.format(**exif)
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