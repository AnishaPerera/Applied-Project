from django import forms
from .models import Thread, Comment, Reply

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']