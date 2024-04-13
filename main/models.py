from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Категория ', max_length=150)
    url = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('Язык ', max_length=50)
    url = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.name

class Kyrs(models.Model):
    name = models.CharField('name ', max_length=150)
    img = models.ImageField('фото', upload_to="kyrs/",blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    money = models.CharField('Цена ', max_length=150)
    content = models.TextField()
    url = models.SlugField('url', max_length=100, unique=True)
    lan =  models.ForeignKey(Language, verbose_name="Язык", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ползывитель", blank=True, null=True)

    def _str_(self):
        return self.name


class Lesson(models.Model):
    kyrs = models.ForeignKey(Kyrs, on_delete=models.CASCADE)
    name = models.CharField('name ', max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='video/')


class Test(models.Model):
    task = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tests')
    question = models.CharField('question ',max_length=200)
    correct_answer = models.CharField('correct_answer', max_length=100)


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя ', max_length=100)
    text = models.TextField('Сообщениие')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Родитель", blank=True, null=True),
    kyrs = models.ForeignKey(Kyrs, on_delete=models.CASCADE, verbose_name="курс")

    def __str__(self):
        return f"{self.name}-{self.kyrs}"
