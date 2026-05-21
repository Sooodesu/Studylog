from django import forms
from .models import StudyLog, Tag

class StudyLogForm(forms.ModelForm):
    class Meta:
        model = StudyLog
        fields = [
                    'title',
                    'content',
                    'study_date',
                    'tags'
        ]
        labels = {
            'title': 'タイトル',
            'content': '内容',
            'study_date': '学習日',
            'tags': 'タグ'
        }
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            'name': 'タグ名'
        }