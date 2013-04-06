---
layout: post
title: Multiple file drag and drop in Air
categories: Air
old: 2055
blog: andy-mckay
---
<p>If you are dragging multiple files into your Air and you need to grab them, make sure you do the following:</p>
<pre>
function dropHandler(event) {
    var files = new Array;
    files = event.dataTransfer.getData("application/x-vnd.adobe.air.file-list")
    ...
}
</pre>
<p>That mime-type is what you need to get a file list and not just the last file.</p>