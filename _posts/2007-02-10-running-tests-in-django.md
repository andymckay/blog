---
layout: post
title: Running tests in Django
categories: Django
old: 1908
blog: andy-mckay
---
Found I was getting this error in Django running tests:  <pre>Got an error recreating the test database: must be owner of database test_clearwind </pre><p>Did a bit of googling and took a while, so in case I get it again the answer is to run the following in psql:</p><pre>alter user django createdb;</pre>Where django is the name of my user.