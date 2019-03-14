from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tags_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)
