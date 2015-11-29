---
layout: post
title: Documentation debt
categories: General
blog: andy-mckay
---

There's lots of talk about technical debt, but documentation debt is just as real and similar. Every line of documentation you write needs maintaining and keeping up to date... and the chances are that over time it will slowly become more and more outdated and useless.

This does harm when the documentation actively misleads people, making them make wrong decisions and costs them time. You've probably all seen a person come onto a mailing list or group chat wondering why something doesn't work and getting frustrated. Followed by the answer "oh that documentation is out of date".

That frustration is real and can be harmful to your project.

* Avoid documenting stuff that doesn't need to be documented, especially if it is documented elsewhere. For example: if your project is on GitHub and follows standard practices, you shouldn't really need to document that commit process much.

* Avoid the trap of "it might be useful to someone". It just might, but that argument means you can document anything. In code terms this is similar to "let's make this an Adpater/Factory/Engine/Class of boggling complexity because in the future someone might want to..." problem.

* Review your documentation and be merciless about cutting things.

* Apply a review process to your documentation, Wiki's are fine for collaboration and spontaneity but that might not be suitable for your projects documentation. One example is to use source control tools to store your documentation and provide a review process.

* Finally, if a document needs critical information, putting it at the top of the page is pointless if the page runs for more than one screen length. For example <a href="https://docs.djangoproject.com/en/1.6/ref/unicode/#translated-strings">consider this page</a> vs <a href="https://developer.mozilla.org/en-US/docs/Mercurial/Using_Mercurial#How_can_I_generate_a_patch_for_somebody_else_to_check-in_for_me.3F">this page</a>, both are deprecated.

Just as you spend time reviewing technical debt, I recommend reviewing and cleaning documentation debt too.
