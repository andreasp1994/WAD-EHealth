from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Searcher(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    # The additional attributes we wish to include.

    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    slug = models.SlugField(default="")
    id = models.AutoField(primary_key=True)
    shared = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
        #        self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=300)
    url = models.URLField(default="")

    flesch_score = models.IntegerField(default =0)
    polarity_score=models.IntegerField(default=0)
    subjectivity_score=models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
