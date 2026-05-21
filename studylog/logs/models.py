from django.db import models
from django.contrib.auth.models import User

class StudyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    study_date = models.DateField(verbose_name='学習日')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='タグ')

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='タグ名')
    
    def __str__(self):
        return self.name
