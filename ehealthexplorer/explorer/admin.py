from django.contrib import admin
from models import Searcher,Category, Page
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Searcher)
admin.site.register(Category)
admin.site.register(Page)