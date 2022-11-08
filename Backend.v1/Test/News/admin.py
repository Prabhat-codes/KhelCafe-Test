from django.contrib import admin

# Register your models here.
from News.models import BlogPost 

from News import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','timestamp')

admin.site.register(BlogPost,BlogPostAdmin)