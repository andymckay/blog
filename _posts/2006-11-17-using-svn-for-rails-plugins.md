---
layout: post
title: Using SVN for rails plugins
categories: Rails
old: 1871
blog: andy-mckay
---
One way to add functionality to Rails is to use the plugin framework. It seems pretty simple, you put your stuff in SVN and then do an install ala:

<pre>
script/plugin install http://path.to.svn.server/project
</pre>

Seemed simple enough. Problem is that the way it works is moronic. It grabs the HTML for page that you'd normally see in the browser, parses it using regex's (a XML or HTML parsing library would be too much to ask). And then tries to download every file it can find.

Only problem is that it will also include the <em>svnindex.xsl</em> file if you've set up nice SVN pages following something like <a href="http://andrewbeacock.blogspot.com/2006/10/supporting-multiple-subversion-svn.html">this</a> and for some reason blow up at that point. Looking at the code, it only follows relative links, so the answer is to change Apache to use a full path to the xsl, so from:

<pre>SVNIndexXSLT /svnindex.xsl</pre>

...to:

<pre>SVNIndexXSLT http://svn.clearwind.ca/svnindex.xsl</pre>

The script ignores it and life continues.
