from django.contrib import admin

from book.models import  Author, Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
