---
layout: post
title: Mail filters
categories: Mozilla
blog: andy-mckay
---

Wil posted on <a href="http://micropipes.com/blog//2017/07/07/some-gmail-filters-to-make-sorting-through-mozilla-mail-easier/">his blog some mail filters</a> he uses to cope with all the incoming mail. Here's a few of mine:

Highlight mentions on mentored bugs:

<pre>
Matches: from:bugzilla-daemon@mozilla.org "X-Bugzilla-Mentors"
Do this: Skip Inbox, Apply label "Bugzilla/Mentored"
</pre>

Filter out intermittents:

<pre>
Matches: from:bugzilla-daemon@mozilla.org "X-Bugzilla-Keywords: intermittent-failure"
Do this: Skip Inbox, Apply label "Bugzilla/Intermittents"
</pre>

Filter down by a specific product and component:

<pre>
Matches: from:bugzilla-daemon@mozilla.org "X-Bugzilla-Product: Firefox" "X-Bugzilla-Component: Extension Compatibility"
Do this: Skip Inbox, Apply label "Bugzilla/Extension Compat"
</pre>
