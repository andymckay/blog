import xml.etree.ElementTree as etree
from markdown import Extension
from markdown.inlinepatterns import InlineProcessor
import re

# TODO: split this out into a seperate module

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


class StravaExtensionException(Exception):
    pass


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
