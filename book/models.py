from django.db import models


class DeleteModel(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    objects = DeleteModel()
    new = models.Manager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save(*args, **kwargs)


class Author(BaseModel):
    full_name = models.CharField(max_length=100)
    birthday = models.IntegerField()
    country = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Book(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='book', blank=True, null=True)
    file = models.FileField(upload_to='file', blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"


# models.py
class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name
