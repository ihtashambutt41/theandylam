from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),

    #Example URL: http://127.0.0.1:8000/search/results/harry%20potter/
    path('results/<str:search_text>/', views.results, name='results'),
]