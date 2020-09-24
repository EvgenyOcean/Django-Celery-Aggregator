from django.db import models
from django.contrib.auth.models import User

class PostsManager(models.Manager):
    def featured(self, sources):
        return super().get_queryset().filter(featured=True).filter(source__in=sources)

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=250, blank=False, null=False)
    content = models.TextField()
    link = models.CharField(max_length=250, blank=False, null=False, unique=True)
    source = models.CharField(max_length=25)
    featured = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='posts', null=True, blank=True)
    objects = PostsManager()

    def __str__(self):
        return self.title
