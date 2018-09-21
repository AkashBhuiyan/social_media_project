from django.db import models
from django.utils.text import slugify # slugify allows us to remove any character's alpha numeric _ -
import misaka # allows markdown inside of a post text (redis commenting system)
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils import timezone


# Create your models here.

User = get_user_model() # it allows me to do call thing of a current user session
from django import template

#register = template.library() #this is how we can use custom template tags in future


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False,default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):

    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')


    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')





