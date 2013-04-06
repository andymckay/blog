---
layout: post
title: Deprecation warnings under control - almost
categories: Plone
old: 1851
blog: andy-mckay
---
Thanks to a <a href="http://awkly.org/archive/ignoring-deprecation-warnings/">helpful post from Sidnei</a>, I'm almost there. 

I've got two zope.conf files now, a zope.conf and a zope-full.conf. The former has logging minimised, and deprecation warnings blocked.

<pre>
&lt;warnfilter>
    action ignore
    category exceptions.DeprecationWarning
&lt;/warnfilter>
&lt;warnfilter>
    action ignore
    category exceptions.Warning
&lt;/warnfilter>

&lt;eventlog>
  level error
  &lt;logfile>
    path $INSTANCE/log/event.log
    level error
  &lt;/logfile>
&lt;/eventlog>
</pre>

The latter is the default zope configuration file. I then copied runzope to runzope-full and pointed it to the new config file.

<pre>
CONFIG_FILE="/opt/Plone-2.5/Instance/etc/zope-full.conf"
...
exec "$PYTHON" "$ZOPE_RUN" --configure=$CONFIG_FILE "$@"
</pre>

So now I can:

<ul>
	<li>Do runzope and get only errors when the occur, here's a sample:
<pre>/opt/Plone-2.5/zope/etc $ ~/plone-bin/runzope
2006-09-14 10:33:54 ERROR Zope.SiteErrorLog http://localhost:8080/test/sampleError
Traceback (innermost last):
  Module ZPublisher.Publish, line 115, in publish
  Module ZPublisher.mapply, line 88, in mapply
  Module ZPublisher.Publish, line 41, in call_object
  Module Shared.DC.Scripts.Bindings, line 311, in __call__
  Module Shared.DC.Scripts.Bindings, line 348, in _bindAndExec
  Module Products.PythonScripts.PythonScript, line 323, in _exec
  Module None, line 1, in sampleError
   - <PythonScript at /test/sampleError>
   - Line 1
ZeroDivisionError: integer division or modulo by zero</pre>

</li>
	<li>Do runzope-full and get all the errors, useful for testing before a release or debugging.</li>
</ul>

However one left on the plate: zopectl debug does the latter:

<pre>
~/plone-bin/zopectl debug
Starting debugger (the name "app" is bound to the top-level Zope object)
2006-09-14 10:52:07 WARNING Init Class Products.ATContentTypes.content.base.ATCTFolderMixin has a security declaration for nonexistent method 'manage_copyObjects'
2006-09-14 10:52:08 WARNING Plone Deprecation Warning 
The CMFPlone.MemberData class will be removed in Plone 3.0
2006-09-14 10:52:08 WARNING Plone Deprecation Warning 
CustomizationPolicies are deprecated and will be removed in Plone 3.0. Please use GenericSetup extension profiles instead.
2006-09-14 10:52:08 WARNING Plone Deprecation Warning 
registerSetupWidget is deprecated and will be removed in Plone 3.0.
2006-09-14 10:52:08 WARNING Plone Deprecation Warning 
registerSetupWidget is deprecated and will be removed in Plone 3.0.
2006-09-14 10:52:09 WARNING Init Class Products.PloneMultisite.MultisiteTool.MultisiteTool has a security declaration for nonexistent method 'inheritDefaultSubscriptions'
2006-09-14 10:52:09 WARNING Init Class Products.PloneMultisite.MultisiteTool.MultisiteTool has a security declaration for nonexistent method 'inheritDefaultSubscriptions'
2006-09-14 10:52:10 WARNING Plone Deprecation Warning 
CustomizationPolicies are deprecated and will be removed in Plone 3.0. Please use GenericSetup extension profiles instead.
2006-09-14 10:52:10 WARNING Plone Deprecation Warning 
registerSetupWidget is deprecated and will be removed in Plone 3.0.
>>> 
</pre>

...and the same with zopectl run. Still needs a bit more work.