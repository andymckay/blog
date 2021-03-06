---
layout: post
title: Putting weather onto a site
categories: Plone
old: 2193
blog: andy-mckay
---
<p>Just following on from the last post about Cleartrain, someone asked in irc which product to use to put the weather onto their Plone site. There's a bunch of old ones out there. The simple answer is, don't. Just do it in Javascript, for example:</p>
<pre>    &lt;div id="weather-feed" /&gt;
    &lt;script type="text/javascript" src="https://www.google.com/jsapi"&gt;&lt;/script&gt;
    &lt;script type="text/javascript"&gt;
    
    google.load("feeds", "1");

    var rss = new Object();

    rss.url = "http://weather.yahooapis.com/forecastrss?p=";
    rss.node = "CAXX0518";  // vancouver

    function initialize() {
        var feed = new google.feeds.Feed(rss.url + rss.node);
        feed.load(function(result) {
          if (!result.error) {
            var msg = document.getElementById("weather-feed");
            msg.innerHTML = msg.innerHTML + '&lt;div&gt;' + result.feed.title + '&lt;/div&gt;';
            for (var i = 0; i &lt; result.feed.entries.length; i++) {
              var entry = result.feed.entries[i];
              var link = '&lt;a href="' + entry.link + '"&gt;' + entry.title + '&lt;/a&gt;';
              var para = '&lt;p&gt;' + entry.content + '&lt;/p&gt;';
              msg.innerHTML = msg.innerHTML + '&lt;di &gt;' + link + para + '&lt;/div&gt;';
            };
          }
        });
    };

    google.setOnLoadCallback(initialize);
    
    &lt;/script&gt;</pre> 
<p>This pulls in the weather from Yahoo, via Google. See <a href="http://developer.yahoo.com/weather/#request">http://developer.yahoo.com/weather/#request</a> for more.</p>
<p>Example:</p>
    <div id="weather-feed" />
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
    
    google.load("feeds", "1");

    var rss = new Object();

    rss.url = "http://weather.yahooapis.com/forecastrss?p=";
    rss.node = "CAXX0518";  // vancouver

    function initialize() {
        var feed = new google.feeds.Feed(rss.url + rss.node);
        feed.load(function(result) {
          if (!result.error) {
            var msg = document.getElementById("weather-feed");
            msg.innerHTML = msg.innerHTML + '<div>' + result.feed.title + '</div>';
            for (var i = 0; i < result.feed.entries.length; i++) {
              var entry = result.feed.entries[i];
              var link = '<a href="' + entry.link + '">' + entry.title + '</a>';
              var para = '<p>' + entry.content + '</p>';
              msg.innerHTML = msg.innerHTML + '<di >' + link + para + '</div>';
            };
          }
        });
    };

    google.setOnLoadCallback(initialize);
    
    </script>