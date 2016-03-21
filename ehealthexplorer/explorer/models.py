from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.dispatch.dispatcher import receiver

class Searcher(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    name = models.CharField(max_length=128,default="")
    surname = models.CharField(max_length=128,default="")
    username = models.CharField(max_length=128,default="")
    email = models.CharField(max_length=128,default="")
    picture = models.ImageField(upload_to='profile_images',default='/static/prof-img/user.png')

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    slug = models.SlugField(default="")
    id = models.AutoField(primary_key=True)
    shared = models.BooleanField(default=False)
    time_shared = models.DateTimeField(default=None,null=True,blank=True)

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
    id = models.AutoField(primary_key=True)

    flesch_score = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    polarity_score=models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    subjectivity_score=models.DecimalField(max_digits=3,decimal_places=2,default=0.00)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

@receiver(user_registered)
def callback(sender, **kwargs):
    user = kwargs.pop('user')
    searcher = Searcher.objects.get_or_create(user=user)[0]
    searcher.save()