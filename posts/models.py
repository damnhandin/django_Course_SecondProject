from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#
#     class Meta:
#         verbose_name = 'Person'
#         verbose_name_plural = 'Persons'

# class Group(models.Model):
#     title = models.CharField(max_length=200, verbose_name='Название')
#     slug  = models.SlugField(max_length=255, unique=True, verbose_name='URL имя')
#     description = models.TextField(verbose_name='Описание')
#
#
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

#
# # Create your models here.
# class Post(models.Model):
#     text = models.TextField()
#
#     def __str__(self):QQ
#         return self.text[:50]
