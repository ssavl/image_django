from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return f"/image/{self.pk}"
