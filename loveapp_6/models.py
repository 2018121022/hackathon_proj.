from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# Create your models here.

class Love(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = "loveapp/", blank = True, null = True)
    author_name = models.CharField(null = True, max_length=100)
    gender = models.CharField(null = True, max_length=100)
    age = models.IntegerField(null = True)
    job = models.CharField(null = True, max_length=100)
    number = models.IntegerField(null = True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Love, related_name = 'comments', on_delete = models.CASCADE, null = True)
    작성자 = models.CharField(null = True, max_length=20)
    내용 = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    성별 = models.CharField(null = True, max_length=100)
    나이 = models.IntegerField(null = True)
    직업 = models.CharField(null = True, max_length=100)
    연애_횟수 = models.IntegerField(null = True)

    def approve(self):
        self.save()

    def __str__(self):
        return self.작성자

class Question(models.Model):
    post = models.ForeignKey(Love, related_name = 'questions', on_delete = models.CASCADE, null = True)
    question_text = models.CharField(max_length=200)
    gender = models.CharField(null = True, max_length=100)
    age = models.IntegerField(null = True)
    job = models.CharField(null = True, max_length=100)
    number = models.IntegerField(null = True)
    author_name = models.CharField(null = True, max_length=100)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.question_text

class Choice(models.Model): 
    #post = models.ForeignKey(Question, related_name = 'choices', on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Question, on_delete=models.CASCADE, null = True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def approve(self):
        self.save()

    def __str__(self):
        return self.choice_text

class Post(models.Model):
    post=models.ForeignKey(Love, related_name = 'posts', on_delete = models.CASCADE, null = True)
    title = models.CharField(null = True, max_length=200)
    content = models.TextField()
    video = EmbedVideoField()
    gender = models.CharField(null = True, max_length=100)
    age = models.IntegerField(null = True)
    job = models.CharField(null = True, max_length=100)
    number = models.IntegerField(null = True)
    author_name = models.CharField(null = True, max_length=100)