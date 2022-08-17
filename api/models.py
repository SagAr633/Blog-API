from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='authors')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images',null=True)
    content = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True,null=True)
    liked_by = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pro_pic = models.ImageField(upload_to='images',null=True)
    bio = models.CharField(max_length=500,null=True)
    phone = models.CharField(max_length=14,default='+91')

class Comments(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)
    user = models.ForeignKey(User,on_delete=models.CASCADE)