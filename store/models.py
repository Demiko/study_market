from django.db import models as m
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
def file_save_path(instance, filename):
    return '{0}/{1}'.format(instance.slug, filename)

class Product(m.Model):
    name = m.CharField(max_length=200)
    slug = m.SlugField(max_length=200)
    description = m.TextField()
    price = m.FloatField()
    in_stock = m.IntegerField()
    image = m.ImageField(upload_to=file_save_path, default='')
    tags = m.ManyToManyField('Tag',symmetrical=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class User(m.Model):
    login = m.CharField(max_length=50)
    password = m.CharField(max_length=64)  # encrypted
    email = m.EmailField()
    name = m.CharField(max_length=50)

    def __str__(self):
        return self.login

    class Meta:
        ordering = ['login']


class Cart(m.Model):
    user_id = m.ForeignKey(User)
    date = m.DateField()

class Tag(m.Model):
    name = m.CharField(max_length=50)
    slug = m.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
