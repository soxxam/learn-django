from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    #cách 1
    try:
        question = Question.objects.get(pk=question_id)
        list_choice = question.taichoices.all()
        

    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    # cách 2 
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question, "tailistchoice" :list_choice})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
