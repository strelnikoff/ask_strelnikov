from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars/")
    user = models.OneToOneField(User)

class QuestionManager(models.Manager):
    def best_questions(self):
        return self.filter(rating__gt=GOOD_RATING).order_by('-reting')
    

class Question(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    author = models.ForeignKey(User)
    rating = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    objects = QuestionManager()
    tegs = models.ManyToManyField('Tag')
    def nice_title(self):
        return self.title
    
    def __unicode__(self):
        return u'%d - %s'.format(self.id, self.title)

class Tag(models.Model):
    name = models.CharField(max_length=30)
