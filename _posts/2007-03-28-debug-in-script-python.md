---
layout: post
title: Debug in Script (Python)
categories: Plone
old: 1949
blog: andy-mckay
---
<p>Golly completely missed this one, thanks <a href="http://danielnouri.org/blog/devel/zope/enablesettrace.html">Daniel Nouri</a>.</p>
<blockquote>It allows pdb.set_trace() inside Script (Python) objects.</blockquote>
<cite><a href="http://svn.zope.org/Products.enablesettrace/trunk">enablesettrace</a></cite>
<p>When it's only two lines of code, you have to bang your head and say, why did I think putting a <code>pdb.set_trace()</code> in a Script (Python) would be any harder.</p>