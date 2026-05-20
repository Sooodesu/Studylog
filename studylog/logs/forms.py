from django import forms
from .models import StudyLog

class StudyLogForm(forms.ModelForm):
    class Meta:
        model = StudyLog
        fields = [
                    'title',
                    'content',
                    'study_date',
        ]
        labels = {
            'title': 'タイトル',
            'content': '内容',
            'study_date': '学習日',
        }