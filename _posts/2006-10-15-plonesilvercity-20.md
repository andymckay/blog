---
layout: post
title: PloneSilverCity 2.0
categories: Plone
old: 1861
blog: andy-mckay
---
Almost 3 years ago I wrote that thing for the book, PloneSilverCity. I've started to rewrite that for 2006 and update it a bit.

From the readme:

<blockquote>
    This is a complete rewrite of PloneSilverCity from the 
    original version of Definitive Guide to Plone. Thats about
    three years old, so I wanted to rewrite it to ensure that
    
    - we use best practices including unit and functional tests
    
    - we use archetypes as opposed to CMF types
    
    I'm retaining the name, although we'll no longer use SilverCity, 
    instead we'll use dpSyntaxHighligher, a javascript solution. This
    allows for zero dependencies.
    
    If you have Zelenium installed, when you install this product
    it will create a set of Zelenium tests that you can run pointing
    at the tests/selenium directory.
    
    To run those tests go to http://yoursite/zelenium/silvercity, but 
    note you must have a user name and password admin/admin.
</blockquote>

Got to fix up that Zelenium stuff. When it's done I'll plonk on plone.org, for now...

SVN: <a href="http://svn.clearwind.ca/public/plone/PloneSilverCity">http://svn.clearwind.ca/public/plone/PloneSilverCity</a> (svn co http://svn.clearwind.ca/public/PloneSilverCity)