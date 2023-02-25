from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # Put the login account in question.author
            question.create_date = timezone.now()
            question.save()
            return redirect('mysitev1:index')
    else: #GET request 처리
        form=QuestionForm() #/forms.py
    context = {'form': form}
    return render(request, 'mysitev1/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "You do not have permission to modify.")
        return redirect('mysitev1:detail', question_id=question.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question) #instance 변경될 대상 model 지정
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('mysitev1:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'mysitev1/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '"You do not have permission to delete."')
        return redirect('mysitev1:detail', question_id=question.id)
    question.delete()
    return redirect('mysitev1:index')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '"You do not have permission to vote."')
    else:
        question.voter.add(request.user)
    return redirect('mysitev1:detail', question_id=question.id)