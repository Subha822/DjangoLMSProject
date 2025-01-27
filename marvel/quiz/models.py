from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Quiz(models.Model):
#     lesson = models.ForeignKey(on_delete=models.CASCADE, related_name='quizzes')
#     title = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
#     text = models.TextField()
#     correct_answer = models.CharField(max_length=255)
#     option1 = models.CharField(max_length=255)
#     option2 = models.CharField(max_length=255)
#     option3 = models.CharField(max_length=255)
#     option4 = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.text