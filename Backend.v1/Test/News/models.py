from django.db import models
from django import forms
from django.forms import forms
from django.forms import ModelForm
# Create your models here.
from django.forms import forms 
class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    timestamp=models.DateTimeField()
    class Meta:
        ordering = ['-timestamp']

class BlogPostForm(ModelForm):
    class Meta:
        model=BlogPost
        exclude = ['timestamp']
