from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    닉네임 = models.CharField(max_length=16)
    나이 = models.CharField(max_length=10)
    성별 = models.CharField(max_length=16)
    직업 = models.CharField(max_length=16)
    연애횟수 = models.CharField(max_length=16)