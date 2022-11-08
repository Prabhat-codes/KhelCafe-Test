from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS=(
    (0,"Draft"),
    (1,"Publish")
)
CATEGORY=(
    (0,"Sports"),
    (1,"Cricket"),
    (2,"Football"),
    (3,"Tennis"),
    (4,"Basketball"),
    (5,"Hockey"),
    (6,"Baseball"),
    (7,"Volleyball"),
    (8,"Badminton"),
    (9,"Table Tennis"),
)

class Post(models.Model):
    title=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='news_posts')
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS,default=0)
    category=models.IntegerField(choices=CATEGORY,default=0)
    class Meta:
        ordering=['created_on']
    
    def __str__(self):
        return self.title