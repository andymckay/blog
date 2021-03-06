---
layout: post
title: Using VMWare
categories: General
old: 2172
blog: andy-mckay
---
<p>Just got a new MacPro at home and that's given me the development setup I've wanted for quite a while.</p>
<p>I've been becoming more and more impressed with VMWare and we started using it in quite a big way at Blue Fountain for development. There are so many advantages for me that I've switched to making all my sandboxes VMWare installs.</p>
<p>This morning I discovered an issue with running the python twitter module on mod_wsgi - namely it blows up with "[Errno 25] Inappropriate ioctl for device" since mod_wsgi tries to use <a href="http://docs.python.org/library/os.html#os.getlogin">os.getlogin()</a>. Fixing this would mean simulating mod_wsgi and the Arecibo setup.</p>
<p>This took a few minutes, just ran a script to copy my base VM over to a new vm:</p>
<pre>#!/usr/bin/python
import shutil
import os
import sys
source = "/Users/andy/Documents/Virtual Machines.localized/base.vmwarevm"
dest = "/Users/andy/Documents/Virtual Machines.localized"
assert os.path.exists(source)
if len(sys.argv) > 1:
	name = sys.argv[1]
else:
	print "No name specified"
	sys.exit(1)
dest = os.path.join(dest, "%s.vmwarevm" % name)
print "Starting copy of base virtual machine to: %s" % name
shutil.copytree(source, dest)
chunk = source.split('/')[-1].split('.')[0]
for filename in os.listdir(dest):
	if filename.startswith(chunk):
		oldfile = os.path.join(dest, filename)
		newfile = filename.replace(chunk, name)
		print "Renaming virtual machine file from: %s to %s" % (oldfile, newfile)
		newfile = os.path.join(dest, newfile)
		shutil.move(oldfile, newfile)
print "Fixing config file"
for ext in [".vmx", ".vmdk"]:
	config = os.path.join(dest, "%s%s" % (name, ext))
	data = open(config, "rb").read()
	data = data.replace(chunk, name)
	open(config, "wb").write(data)
</pre>
<p>Pointers to more detailed code or tools for doing that appreciated. After starting the VM, I just ssh in (since its got my ssh keys on) and start apt-getting the couple of things I need to run Arecibo (mostly openid related. Editing the files is easy, I just use <a href="http://www.macfusionapp.org/">MacFusion</a> to do an SSHFS mount of the files on the server.</p>
<p>After that the combination of the browser, a terminal window and Textmate and I could be editing locally. Except, of course, I'm not. Everything it's own little sandbox and they can't pollute each other.</p>
<p>There are tools like virtualenv for Python which are great. But let's face it as a consultant in the past I've done Java, PHP, VB and all sorts of icky stuff.</p>
<p>For a consultant, this is a crucial tool that used to be satisfied by having a room full of naff old boxes - no more. Oh and best of all I don't have to mess around with building on OS X which can be it's own barrel of fun.</p>