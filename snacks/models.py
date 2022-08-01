from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='files/images', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'My Snack'
        verbose_name_plural = 'Our Snacks'

    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])