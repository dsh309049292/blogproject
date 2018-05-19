# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# 创建一张分类表，含有name字段，类型是字符型，长度是100字节。
class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

# 创建一张标签表，含有name字段，类型是字符型，长度是100字节。
class Tag(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

# 创建一张文章表，含有标题、正文、作者、创建时间、最后一次修改时间、文章摘要、作者。
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 200, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tag, blank = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs = {'pk': self.pk})

#创建一个存储图片的模型。
class Img(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'img')