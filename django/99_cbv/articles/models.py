from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 디테일뷰...
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.pk})

