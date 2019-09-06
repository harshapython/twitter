from __future__ import absolute_import, unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models 
# tweets
class Tweets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', default='None')
    text = models.CharField(max_length=160,default=None)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    profile_image = models.ImageField(upload_to='static/img', null=True, blank=True)    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.text
#followers and following list
class Follow(models.Model):
    followers = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE,)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE,)    
    class Meta:
        unique_together = ('followers', 'following',)
#profiles
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilename = models.TextField(max_length=50,blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='static/images', blank=True, null=True)
    header_image = models.ImageField(upload_to='static/images', blank=True, null=True)    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return str(self.user)
#comments
class comment(models.Model):
    twtid = models.ForeignKey(Tweets, on_delete=models.CASCADE, related_name='twtid', default='None')
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True,blank=True)
    text = models.CharField(max_length=160,default=None)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
#reply comments
class Replycomment(models.Model):
    replyid = models.ForeignKey(comment, on_delete=models.CASCADE, related_name='cmtid', default='None')
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True,blank=True)
    text = models.CharField(max_length=160,default=None)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    image = models.ImageField(upload_to='static/img', null=True, blank=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.text
