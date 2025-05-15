from django.db import models
from django.utils import timezone


class Author(models.Model):
    full_name=models.CharField(max_length=100)
    birthday=models.IntegerField()
    country=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13,blank=True,null=True)
    email=models.CharField(blank=True,null=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=150)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='book',blank=True,null=True)
    file=models.FileField(upload_to='file',blank=True,null=True)
    is_published=models.BooleanField(default=False)


    def __str__(self):
        return self.title


    class Meta:
        db_table="book"