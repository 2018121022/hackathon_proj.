from django.shortcuts import render, get_object_or_404, redirect
from loveapp_4.models import Love, Question, Choice, Comment
from .forms import CommentForm, PostForm, QuestionForm, ChoiceForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/account/login/')
def index_4(request):
    love_index = Love.objects.all()
    return render(request, 'index_4.html', {'love_index' : love_index})

def detail_4(request, love_id):
    love = get_object_or_404(Love, pk = love_id)
    return render(request, 'detail_4.html', {'love' : love})

def write_4(request):
    if request.method == "GET":
        return render(request, "write_4.html")
    love = Love.objects.create()
    love.title = request.POST['title']
    love.content = request.POST['content']
    love.image = request.FILES.get('image')
    love.author_name = request.POST['author_name']
    love.gender = request.POST['gender']
    love.age = request.POST['age']
    love.job = request.POST['job']
    love.number = request.POST['number']
    love.save()
    return redirect('detail_4', love.id)

def update_4(request, love_id):
    if request.method == "GET":
        love = get_object_or_404(Love, pk = love_id)
        return render(request, "update_4.html", {"love":love})
        
    love = get_object_or_404(Love, pk = love_id)
    love.title = request.POST['title']
    love.content = request.POST['content']
    love.image = request.FILES.get('image')
    love.save()
    return redirect('detail_4', love.id)
    
def delete_4(request, love_id):
    love = get_object_or_404(Love, pk = love_id)
    love.delete()
    return redirect('index_4')

def add_comment_to_post_4(request, love_id):
    love = get_object_or_404(Love, pk = love_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = love
            comment.save()
        return redirect('detail_4', love_id)
    else:
        form = CommentForm()
        return render(request, 'add_comment_to_post_4.html', {'form':form})

def add_music_to_post_4(request, love_id):
    love = get_object_or_404(Love, pk = love_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.post = love
            post.save()
        return redirect('detail_4', love_id)
    else:
        form = PostForm()
        return render(request, 'add_music_to_post_4.html', {'form':form})

def add_poll_to_post_4(request, love_id):
    love = get_object_or_404(Love, pk = love_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = False)
            question.post = love
            question.save()
        return redirect('detail_4', love_id)
    else:
        form = QuestionForm()
        return render(request, 'add_poll_to_post_4.html', {'form':form})

def detail_poll_4(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request,'detail_poll_4.html', {'question':question})

def result_4(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'result_4.html', {'question':question})

def vote_4(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail_poll_4.html', {'question':question, 
        'error_message':'선택한 항목이 없습니다.'})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result_4', args = (question.id,)))

def add_choices_to_post_4(request, love_id):
    love = get_object_or_404(Question, pk = love_id)
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit = False)
            choice.post = love
            choice.save()
        return redirect('detail_poll_4', love_id)
    else:
        form = ChoiceForm()
        return render(request, 'add_choices_to_post_4.html', {'form':form})

def comment_delete_4(request, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Love, pk = comment.post.id)
    
    comment.delete()
   
    return redirect('detail_4', post.id)