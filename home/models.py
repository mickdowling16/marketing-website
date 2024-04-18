from django.db import models

class PortfolioItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_images/')
    testimonial = models.TextField()

    def __str__(self):
        return self.name
