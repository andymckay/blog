---
layout: post
title: Doing a PUT in Adobe Air
categories: Air
old: 2056
blog: andy-mckay
---
<p>This one had me confused for quite a while, simply I wanted to do a PUT in Adobe Air to my Plone site. Something that you think would be quite easy but somehow all I got were errors. The problem turned out to be I was doing an upload, when it should have been <code>uploadUnencoded</code> which has a slightly different signature.</p>
<pre>
function uploadFile(file) {
    // an internal function to get our upload url
    var url = getPref("url");
    // an internal function to get the file name for the PUT
    var urlRequest = new air.URLRequest(url + "/" + fileFromPath(file.url));

    var headers = new Array()
    // an internal function to get the Plone security cookie
    headers.push(new air.URLRequestHeader("Cookie", "__ac=" + getPref("cookie")));
    // an internal function to get the file extension
    headers.push(new air.URLRequestHeader("Content-Type", extensionFromFile(file)));    
    
    urlRequest.requestHeaders = headers; 
    urlRequest.method = air.URLRequestMethod.PUT;
    
    file.addEventListener(air.ProgressEvent.PROGRESS, uploadProgress);
    file.addEventListener(air.Event.COMPLETE, uploadComplete);
    file.addEventListener(air.SecurityErrorEvent.SECURITY_ERROR, uploadError);
    file.addEventListener(air.HTTPStatusEvent.HTTP_STATUS, uploadError);	
    file.addEventListener(air.IOErrorEvent.IO_ERROR, uploadError);
    
    file.uploadUnencoded(urlRequest);
} 
</pre>