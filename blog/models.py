from django.db import models

# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/')
    status = models.BooleanField(default=False)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline