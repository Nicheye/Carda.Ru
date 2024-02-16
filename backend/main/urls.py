from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',MainView.as_view()),
	path('<int:id>',MainView.as_view()),
	path('search',SearchView.as_view()),
	path('ai',AiBot.as_view()),
]
