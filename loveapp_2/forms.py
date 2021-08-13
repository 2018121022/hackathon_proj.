from django import forms
from .models import Comment, Post, Question, Choice

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('작성자', '성별', '나이', '직업', '연애_횟수', '내용')
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'video')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text', )