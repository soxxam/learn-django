from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('result/<int:result_id>/', views.result, name='result'),
]