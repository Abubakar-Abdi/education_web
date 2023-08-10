from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class contact1(models.Model):
    
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=350)
    email=models.EmailField(default=None)
    Username=models.CharField(max_length=150,default=True)
   # password=models.DO_NOTHING
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.Username
STATUS = ((0,"draft"),
          (1, "publish"))
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title







