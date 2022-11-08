from django.contrib import admin
from news.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','created_on','status','category']
    list_filter=('status','created_on','category')
    search_fields=['title','content','category']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)

