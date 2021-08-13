from django.db import models

# Create your models here.
class Love(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "loveapp/", blank = True, null = True)

    def __str__(self):
        return self.title