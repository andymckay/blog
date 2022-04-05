from datetime import date

today = date.today()
name = "_posts/" + today.strftime("%Y-%m-%d-post.md")
preamble = """
---
layout: post
title:
categories: gear
blog: andy-mckay
---

"""
with open(name, "w") as handle:
    handle.write(preamble)

print(name)