from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),

    path('poll/create/', views.createPoll, name='create-poll'),
    path('poll/update/<str:pk>/', views.updatePoll, name='update-poll'),
    path('poll/delete/<str:pk>/', views.deletePoll, name='delete-poll'),

    path('polls/active/', views.getActivePolls, name='polls-active'),

    path('question/create/<str:id_poll>/', views.createQuestion, name='create-question'),
    path('question/update/<str:pk>/', views.updateQuestion, name='update-question'),
    path('question/delete/<str:pk>/', views.deleteQuestion, name='delete-question'),

    path('choice/create/<str:question_id>/', views.createChoice, name='create-choice'),
    path('choice/update/<str:pk>/', views.updateChoice, name='update-choice'),
    path('choice/delete/<str:pk>/', views.deleteChoice, name='delete-choice'),

    path('answer/create/<str:poll_id>/', views.voteUser, name='vote-user'),

    path('user/votes/', views.getDetails, name='details'),
]
