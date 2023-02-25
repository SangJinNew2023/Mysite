from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Question, Answer

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | #Title search
            Q(content__icontains=kw) | #Content search
            Q(answer__content__icontains=kw) | #Answer content search
            Q(author__username__icontains=kw) | #Question author search
            Q(answer__author__username__icontains=kw) #Answer author search
        ).distinct()
    paginator = Paginator(question_list, 10) # 페이지당 10개
    page_obj = paginator.get_page(page)
    context = {'question_list':page_obj, 'page':page, 'kw': kw}
    return render(request, 'mysitev1/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    page=request.GET.get('page', '1')
    answer_list=Answer.objects.filter(question=question).order_by('-voter')
    paginator = Paginator(answer_list, 5)
    page_obj = paginator.get_page(page)
    context = {'answer_list': page_obj, 'question': question}
    return render(request, 'mysitev1/question_detail.html', context)