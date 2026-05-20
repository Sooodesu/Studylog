from django.db import models

class StudyLog(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    study_date = models.DateField(verbose_name='学習日')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
