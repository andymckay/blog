---
layout: post
title: Creating a ModelForm dynamically
categories: Django
old: 2249
blog: andy-mckay
---
<p>A simple short snippet for creating a ModelForm for an object dynamically. This is a useful library function to validate data and save changes to a model without having to declare a form:</p>
<pre>
from django import forms

def model_to_modelform(model):
    meta = type('Meta', (), { "model":model, })
    modelform_class = type('modelform', (forms.ModelForm,), {"Meta": meta})
    return modelform_class
</pre>
<p>Based on "<a href="http://www.b-list.org/weblog/2008/nov/09/dynamic-forms/">So you want a dynamic form</a>".</p>