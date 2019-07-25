from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 在Python3中使用
    # def __unicode__(self):

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __init__(self, name, tagline):
        self.name = name
        self.age = tagline
    def __str__(self):  # __str__ on Python 3
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __init__(self, name, email):
        self.name = name
        self.age = email
    def __str__(self):  # __str__ on Python 3
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __init__(self, blog, authors):
        self.blog = blog
        self.authors = authors
    def __str__(self):  # __str__ on Python 3
        return self.headline

