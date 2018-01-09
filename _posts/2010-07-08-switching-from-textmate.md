---
layout: post
title: Switching from Textmate
categories: General
old: 2274
blog: andy-mckay
---
<p>Last week, I finally gave up with Textmate, a piece of software I paid for. It's clear that <a href="http://twitter.com/wasTM2released">Textmate 2</a> is turning into vapourware. I did one search on too large a directory structure and sure enough watched my Textmate process hung, yet again.</p>
<p>No idea why I was putting up with that crap, but it was time to go.</p>
<p>So I went and grabbed <a href="http://www.activestate.com/komodo-edit/downloads">Komodo Edit</a>, because it's made by ActiveState who are a) in Vancouver and b) cool people and c) I've still fond memories of working there.</p>
<p>...And it's nice to get text completion, syntax highlighting and all those yummy things.</p>
<p>I found if I went to settings I could get a nice white text on black background theme. Then went and removed all the extraneous views, toolboxes and so on. Annoying startup page can be got rid of there too, leaving you with something that feels lighter and simpler.</p>
<p>And  a find that won't kill your editor. What a concept.</p>
<p>Things I'm not keen on:</p>
<ul>
<li>I've got .kpf files all over the place like rabbit droppings. I don't want that, I don't want to share my project files, so I'm adding .kpf to SVN and Git ignore files. I just want to be able to open a folder or a series of files in Komodo from the command line.</li>
<li>Haven't spotted how to easily be able to jump to methods in my current file like I can in TextMate. Must be there somewhere.</li>
<li>The new file dialog is overly complex, just create a new file please.</li>
<li>The fact that a find brings up the find dialog, except the replace is not selectable truly <b>baffled</b> me. You have to do "replace" which brings up the find dialog and now the replace is selectable. (see pics below). This baffled me so much, I've <a href="http://svn.openkomodo.com/openkomodo">downloaded the source</a>.</li>
</ul>
<p>But so far happy with Komodo and so glad to dump TextMate. Perhaps I'm just stalling the inevitable of just using emacs.</p>
<img src="/files/komodo-find.png" title="this is the find dialog" />
<img src="/files/komodo-replace.png" title="this is the replace dialog" />