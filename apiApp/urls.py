from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path('create-dept', views.createDepartment, name='create-dept'),
    path('view-dept', views.departmentList, name='view-dept'),
    path('read-dept/<str:pk>', views.departmentDetail, name='read-dept'),
    path('create-exam/<str:pk>', views.createExam, name='create-exam'),
    path('read-exam/<str:pk>', views.examDetail, name='read-exam'),
    path('view-exam', views.examList, name='view-exam'),
    path('create-question/<str:pk>', views.createQuestion, name='create-question'),
    path('view-question', views.questionList, name='view-question'),
    path('read-question/<str:pk>', views.questionDetail, name='read-question'),
]