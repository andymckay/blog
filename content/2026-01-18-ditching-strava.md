
---
layout: post
title: Ditching Strava
categories: apps
image: /files/elbows-up.jpg
---

As part of the slow, but ongoing, effort to remove US companies out of my life, I've decided to remove Strava out of my life. This was not an easy decision, I've used Strava for 8 years and used it *a lot*. I'll miss seeing what my friends do on Strava and many other things. However *uploading so much personal data about my activities to a US company with data on US servers at this point in 2026 is no longer acceptable*.

Strava served a few functions for me, so I'll go through what I've done to get off of Strava and what I'm missing below 👇

### Recording

I rarely use Strava for recording insted it comes from my watch or my cycling computer. I don't use my cycling computer much anymore but unfortunately its a <a href="https://en.wikipedia.org/wiki/Wahoo_Fitness">Wahoo</a> and they are a US company. The main device I use multiple times a day is my watch and that's from <a href="https://en.wikipedia.org/wiki/COROS_Wearables_Inc">Coros</a>.

Coros parent company is Chinese with its head office in California. So at this point I've got no guarantees that my data is going to either China or the US. Also having a legal entity in the US is a problem. At this point, I trust China more than I do the US. I guess that's because China hasn't threatened Canada's sovereignty repeatedly or threatened us with "taking us over". Coros being under the influence of the US is a problem, but one step at a time.

### Analysis

I used Strava to look at my activities and analyse the data. So I'm using <a href="https://intervals.icu">intervals.icu</a> for that (hat tip to <a href="https://pnw.zone/@felix/115833363579937530">@felix</a>). Intervals.icu is a London company, and their servers are in Germany. Germany has probably some of the highest data protection and privacy laws around (at least that I know about). It's supported by donation of 10 EUR every 3 months 👍. 

It imported all my data directly from Strava and I can now go and compare my new runs with my old runs. Activities import straight from Coros, so there's nothing for me to do there:

<img src="/files/intervals-icu.png" class="img-fluid">

### Blog

In the past after uploading an activity to Strava, if I wrote a blog post about it I'd share it here so that it appears nicely in the post. I tried checking out other services but I couldn't find one I really liked - but honourable mentions to <a href="https://www.komoot.com/">Komoot</a> (in the EU) and <a href="https://outdooractive.com">Outdoor Active</a> (in the EU).

Strava provided a great download of my data, with all 3,457 activities along with photos, routes and so on. More detail on <a href="https://support.strava.com/hc/en-us/articles/216918437-Exporting-your-Data-and-Bulk-Export">that is here</a>. 

Armed with the <code>.gpx</code> files, I tried to figure out how to convert 117 Strava embeds into a new site embed. Only to find many problems around correlating all the data and the IDs. The Strava export is the raw data, then you have to call it's API to match up other bits of data. Then the other services have patchy APIs that don't really the job either. I spent way too long on this part and instead just decided to build it all.

So instead I:

* parsed the markdown files looking for Strava IDs
* grabbed some key data from the Strava API and put into a <code>.json</code>
* grabbed the <code>.gpx</code> file from Strava (that's not in the export or the API, instead the original upload file is present)
* grab the photos out of the export (it's not in the API)
* generate open street map image of the route using Mapbox
* generate an elevation image of the route
* convert the Markdown file to use a new Markdown extension

So given a <code>.gpx</code> I can generate a similar amount of information that any of these services can generate. You can see an example here: <a href="/2025-10-06-skyline.html">Skyline</a>.

It's rather janky at this moment, making it look good is going to take some time and cleaning, but it's a start. All the data and generation is now under my control, with all the advantages and disadvantages that brings, but I'm going to keep those <code>.gpx</code> files backed up locally from now on, so I can easily move between services. It also means that readers of this blog aren't making web requests to Strava, so helping their privacy a teeny tiny bit.

**Note:** I'm making the decision to be open about *some* activities and show them on the blog. But I'm not sharing widely the activities I do *every day*. There's an important difference between *sharing everything* and having the *autonomy to share an activity of my choice* on the blog.

### What's lost

Connections with friends and seeing what they do. Spying with envy on pro athletes. Segments and easy comparisons of old runs. But credit to Strava for providing an excellent download. I haven't found a great substitute for these yet and I'm not sure I want to look for an alternative at this point.

---

I realise this is all seems rather futile, there's lots more places where my data goes to the US or US companies. But one step at a time and I'll get there.