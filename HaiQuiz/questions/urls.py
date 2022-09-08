from django.urls import path
from . import views
urlpatterns=[
    path('',views.ApiOverview,name='home'),
    path('add/',views.add_question,name='add_question'),
    path('all/',views.view_questions,name='all_question'),
    path('update/<int:pk>/', views.update_questions,name='update_questions'),
    path('delete/<int:pk>/', views.delete_questions,name='delete_questions'),
]