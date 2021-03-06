---
layout: post
title: State Workflow for Django, initial release
categories: Django
old: 2152
blog: andy-mckay
---
<p>This is a simple rip off of the DCWorkflow that Plone uses, DCWorkflow originally coming from Digital Creations many moons ago. Anyway I always liked it because its very simple and abstracts quite a few things away from the object, letting admin's decide how things happen. The goal of this state workflow is to:</p>
<ul>
<li>put any number of workflows on a model</li>
<li>the workflow can contain mulitple states</li>
<li>there can be multiple transitions between the workflows</li>
<li>conditions (well scripts) are checked before a transition is run</li>
<li>scripts are run in the transition</li>
</ul>

<p>Workflows can be constructed through the admin interface, or through scripts. The admin interface is a little rough and you <b>can't actually workflow things in it</b>. Since it doesn't check which scripts can be assigned to which workflow, or look for changes, but since I don't want to use the admin interface, I'm not too worried about that.</p>

<p>Users don't actually get to write any scripts. Scripts are created by the admin and given descriptions, the admins can then decide which script to assign to which transition and when. There are two kinds of (optional) scripts:</p>
<ul>
<li>permission: this is to check the object can be transitioned and gets passed the object and the transition. If you want other things like request or user, you might have to use threadlocals or other hacks to get them. If any of the assigned permission scripts does not return True (or anything evaluating as True), then it fails.</li>
<li>do: this is what happens when the script is run and involves changing things, logging, emailing that sort of thing. Script gets passed the object and the transition. Returns ignored, if there's a problem raise an error.</li>
</ul>

<p>The unit tests explain this better than some text, but here's a brief synopsis. Supposing a news item workflow, three states: private, pending, published. Someone in the office needs to review it before it goes live. Also all the fields have to be filled out.</p>
<p>Here' an example permission script assigned to the review transition, ie you can't workflow to review until you fill these out:</p>
<pre>
def check_complete(obj, transition):
    for field in ["title", "description"]:
        if not getattr(obj, field):
            return False
    return True 
</pre>
<p>So here's our news item:</p>
<pre>                                       
from stateworkflow.models.state import State

class NewsItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    state = models.ForeignKey(State)   
</pre>
<p>You can do all this manually (see unit tests) or try the following WorkflowManager a nice wrapper around it all:</p>
<pre>
from stateworkflow.workflowmanager import WorkflowManager

self.one = NewsItem()
self.one.state = Workflow.objects.get(id=2).default_state 
# at the moment we can't transition
self.one.title = "Hello"
self.one.description = "This is a description"
self.one.save()

# we should now be to able transition
wf = WorkflowManager(self.one)
wf.do_transition("Request review")
# we are now pending
assert wf.get_state() == self.one.state
assert wf.get_state().name == "Pending"
</pre> 
<p>For more its in SVN at:</p>
<pre>svn co http://svn.clearwind.ca/public/django/stateworkflow</pre>
<p>Hope its helpful.</p>