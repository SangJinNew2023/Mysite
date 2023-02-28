from ..forms import CommentForm
from ..models import Question, Answer, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_at = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('mysitev1:detail', question_id = answer.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'mysitev1/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, "You do not have permission to modify.")
        return redirect('mysitev1:detail', question_id=comment.answer.question.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment) #instance 변경될 대상 model 지정
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('mysitev1:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'mysitev1/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '"You do not have permission to delete."')
    else:
        comment.delete()
    return redirect('mysitev1:detail', question_id=comment.answer.question.id)