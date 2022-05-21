from django.urls import path

from quiz import views

urlpatterns = [
    path('hello/', views.helloAPI ),
    path('<int:id>/', views.randomQuiz ),
]
