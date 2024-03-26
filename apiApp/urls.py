from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path('dept', views.departmentList, name='dept-list'),
    path('exam', views.examList, name='exam-list'),
    path('question', views.questionList, name='question-list'),
    path('dept/<str:pk>', views.departmentDetail, name='dept'),
    path('exam/<str:pk>', views.examDetail, name='exam'),
    path('question/<str:pk>', views.questionDetail, name='question'),
    path('dept/create-exam/<str:pk>', views.createExam, name='create-exam'),

]