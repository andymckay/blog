---
layout: post
title: Scary code
categories: Rails
old: 1968
blog: andy-mckay
---
<p>Just saw this code and it instantly sent shivers down my spine.</p>
<pre>
namespace :rubaidh do
  task :tag_layout_with_release_info, :roles => :app do
    [snipped by me]
    run "perl -p -i -e 's?</body>?</body>#{release_info}?' #{layout}"
  end
end
</pre>
<p>A rake task for rails that contains a shell out to perl which then outputs HTML. Could as well be done in Make file, ugh.</p>
<p>Sorry for the delay on posting, been a busy few weeks and sat down at the browser with complete writers block. Odd consider the normal quality of my posting.</p>