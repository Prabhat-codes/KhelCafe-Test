from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponseRedirect
from News.models import *
def archive(request):
    posts=BlogPost.objects.all()[:10]
    return render(request, 'archive.html',{'posts':posts,'form':BlogPostForm()})

def create_blogpost(request):
    if request.method=='POST':
        form=BlogPostForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            body=form.cleaned_data['body']
            timestamp=datetime.now()
            post=BlogPost(title=title,body=body,timestamp=timestamp)
            post.save()
            return HttpResponseRedirect('/')
    else:
        form=BlogPostForm()
    return HttpResponseRedirect('/News')