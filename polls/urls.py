from polls import views
from django.urls import path
from django.shortcuts import reverse


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_polls'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
