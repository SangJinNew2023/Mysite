from django import forms
from .models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
