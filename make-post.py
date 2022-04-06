from datetime import date
import sys
import os

today = date.today()
print(sys.argv)
if len(sys.argv) < 2:
    print("Provide post name")
    sys.exit(1)

name = "_posts/" + today.strftime("%Y-%m-%d") + "-%s.md" % sys.argv[1]
preamble = """---
layout: post
title:
categories: gear
blog: andy-mckay
---

"""
with open(name, "w") as handle:
    handle.write(preamble)

print(name)
os.system("code %s" % name)