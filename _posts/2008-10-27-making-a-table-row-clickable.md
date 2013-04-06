---
layout: post
title: Making a table row clickable
categories: clearwind
old: 2144
blog: andy-mckay
---
<p>This one is quite old, but I just spent a bit of time fiddling with the listings page on Arecibo. I really hate that when I've got a table, I have just one link to view the item in the whole row, that's just unfriendly. So I did some googling and spent some doing exactly what I shouldn't of: fiddling with CSS and making it all into spans.</p>
<p>Today I remembered that tables in HTML are damn good at displaying tables and threw that out. Instead a quick jQuery can grab all the rows and make them link to the first link in the row:</p>
<pre>
            $('table.listing tbody tr').bind("click", function() {
                window.location = $(this).find("a").attr("href");
                return false;
            });
</pre>
<p>And remember to turn the cursor into a pointer so it looks more like a link:</p>
<pre>
   cursor: pointer;
</pre>
<p>Elementary stuff, but i'll be able to find this code next time and the Arecibo user interface is just that bit nicer.</p>