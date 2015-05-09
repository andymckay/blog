---
layout: post
title: Building Python packages from Travis
categories: General
blog: andy-mckay
---

If you've got a Python package that you push to <a href="http://pypi.python.org/">pypi</a> and you run your tests on <a href="http://travis-ci.org/">Travis</a> then I *strongly* recommend that you set up uploading your Python packages to pypi using Travis. There's a few reasons for this:

* builds are clean and do not contain any artifacts that might be present on your local system
* anyone with commit access to the repository can do a release by tagging and not just the owner on pypi (really useful at Mozilla)
* the step is automated and that's a win

Follow <a href="http://docs.travis-ci.com/user/deployment/pypi/">this documentation</a>. Basically, alter <code>travis.yml</code>:

<pre>
deploy:
  provider: pypi
  user: marketplacedevsinternal
  on:
    all_branches: true
    tags: true
</pre>

Then run:

<code>travis encrypt --add deploy.password</code>.

Job done. This also works for <a href="http://docs.travis-ci.com/user/deployment/npm">npm</a> and a <a href="http://docs.travis-ci.com/user/deployment/">pile of other stuff</a>.
