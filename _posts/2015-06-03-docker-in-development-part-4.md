---
layout: post
title: Docker in development (part 4)
categories: General
blog: andy-mckay
---

Tips for developing with Docker.

Keep your container small
-------------------------

Each layer in your Dockerfile is cached. This means that if you have the same layer repeated in multiple images, it will cache and reuse that layer.

So its easy not too worry about how big a layer is. Until you start pulling your containers on to servers, test runners, QA servers, developers laptops and so on. Then you start to wonder how your container blew up to 2 gigs [<a href="#footnote-1">1</a>].

After you add a layer, do yourself a favour and see how much it adds. To find out how much a layer adds, use the <code>docker history [image id]</code> command. The results can be suprising, especially when it comes to <a href="http://en.wikipedia.org/wiki/Yellowdog_Updater,_Modified">yum</a>.

Installing <a href="http://supervisor.readthedocs.org/en/latest/">supervisor</a> using <a href="https://pypi.python.org/pypi/pip">pip</a>:

<pre>
540868cb5bab        35 seconds ago      /bin/sh -c pip install supervisor               2.429 MB
</pre>

Installing supervisor using yum:

<pre>
16bb922e5ff5        6 hours ago         /bin/sh -c yum install -y supervisor            224.5 MB
</pre>

That's a 222.071 MB difference.

You can do a <code>yum clean</code> and that's when it gets interesting. Three seperate lines, no clean:

<pre>
392cecc77eae        12 hours ago         /bin/sh -c yum install -y cronie                34.72 MB
91154ebe69d8        12 hours ago         /bin/sh -c yum install -y bash-completion       18.67 MB
760d1b735093        12 hours ago         /bin/sh -c yum install -y supervisor            224.5 MB
</pre>

Install and clean in three lines:

<pre>
832fe193df7d        About a minute ago   /bin/sh -c yum install -y cronie && yum clean   34.69 MB
331bc45fc42a        About a minute ago   /bin/sh -c yum install -y bash-completion &&    18.64 MB
f74a8b922149        2 minutes ago        /bin/sh -c yum install -y supervisor && yum c   21.54 MB
</pre>

Install and clean in one line:

<pre>
23d486d7bc04        2 minutes ago        /bin/sh -c yum install -y supervisor bash-com   38.7 MB
</pre>

The last one saves you 239.19 MB.

It's a pretty simple and quick check to see how big the layer in your Dockerfile. Next time you add a layer, give it a try.

See also <a href="/2015-06-01-docker-in-development-part-3/">part 3</a>.

<ol>
<li><a id="footnote-1"></a>Yes, one of our containers has grown to this size.</li>
</ol>
