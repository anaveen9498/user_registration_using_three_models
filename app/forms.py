from django import forms
from app.models import *


class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        exclude=['topic_name']


class AccessRecordsForm(forms.ModelForm):
    class Meta():
        model=AccessRecords
        exclude=['player_name']