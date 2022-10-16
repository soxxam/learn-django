from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Question
from django.shortcuts import render
import pyrebase
 
# config={
#    // apiKey: "AIzaSyBc10ugt9naJF8inUrXolzyIqYwRetmXjg",
#     authDomain: "eng-ver-2.firebaseapp.com",
#     databaseURL: "https://eng-ver-2-default-rtdb.asia-southeast1.firebasedatabase.app",
#     projectId: "eng-ver-2",
#     storageBucket: "eng-ver-2.appspot.com",
#     messagingSenderId: "11804727838",
#     appId: "1:11804727838:web:e6dfa01e1a7a2d2bdaec0f"
# }
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()

def home(request):
    day = database.child('Category_Dang_Kien_Thuc').child('Day').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })
def question(request):
    return render(request, 'cauhoi.html')

def user(request):
    return render(request, 'user.html')

def category(request):
    return render(request, 'danhmuc.html')

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    #cách 1
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    # cách 2 
    # question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'templates/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))