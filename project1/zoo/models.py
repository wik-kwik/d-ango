from django.db import models

# Create your models here.

class Form(models.Model):
    name=models.CharField(max_length=200)
    street=models.CharField(max_length=150)
    postal_code=models.CharField(max_length=6)
    city=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    email=models.EmailField(max_length=50)
    animal=models.CharField(max_length=100)
    amount=models.IntegerField()
    period=models.IntegerField()
    since=models.CharField(max_length=12)
    rodo_agreement=models.BooleanField()
    data_agreement=models.BooleanField()

    def __str__(self):
            return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    text = models.TextField(max_length=500)
    imgOne = models.ImageField()
    imgTwo = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

