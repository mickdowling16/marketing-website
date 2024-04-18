from django.db import models

class PortfolioItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/portfolio/')
    testimonial = models.TextField()

    def __str__(self):
        return self.name

class Partner(models.Model):
    image = models.ImageField(upload_to='media/partners/')