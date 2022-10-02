from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import datetime
from polls.models import Question, Choice
from django.utils import timezone


def index(request):
    mydata = Question.objects.all().order_by('-pub_date').values()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'mymembers': mydata}, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
        print(question)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    template = loader.get_template('detail.html')
    return HttpResponse(template.render({'question': question,}, request))

def result(request, result_id):
    try:
        result = Choice.objects.get(pk = result_id)
        print(result)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    template = loader.get_template('result.html')
    return HttpResponse(template.render({'question': result,}, request))

def some_name(request):
    foo_instance = Question.objects.create(question_text='test',pub_date=timezone.now()- datetime.timedelta(days=1))
    return render(request, 'detail.html')
