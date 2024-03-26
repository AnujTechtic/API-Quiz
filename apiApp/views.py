from .models import *
from .serializer import *
from rest_framework.response import Response 
from rest_framework.decorators import api_view
import json

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'POST':'api/create-dept'},
        {'GET':'api/view-dept'},
        {'GET':'api/read-dept/id'},
        {'POST':'api/create-exam/dept-id'},
        {'GET':'api/view-exam'},
        {'GET':'api/read-exam/id'},
        {'GET':'api/view-question'},
        {'GET':'api/read-question/id'},
        {'POST':'api/create-question/exam-id'},

    ]
    return Response(routes)

@api_view(['GET'])
def departmentList(request):
    allDept = Department.objects.all()
    serializer = DepartmentSerializer(allDept, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def examList(request):
    allExam = Exam.objects.all()
    serializer = ExamSerializer(allExam, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def questionList(request):
    allQuestion = Question.objects.all()
    serializer = QuestionSerializer(allQuestion, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def departmentDetail(request,pk):
    Dept = Department.objects.get(id = pk)
    serializer = DepartmentSerializer(Dept, many= False)
    return Response(serializer.data)
    
@api_view(['GET'])
def examDetail(request,pk):
        Exm = Exam.objects.filter(id = pk)
        serializer = ExamSerializer(Exm, many= True)
        return Response(serializer.data)
    
@api_view(['GET'])
def questionDetail(request,pk):
        Ques = Question.objects.filter(id = pk)
        serializer = QuestionSerializer(Ques, many= False)
        return Response(serializer.data)

@api_view(['POST'])
def createDepartment(request):
     print(request.method)
     data = request.data
     newDept = Department.objects.create(
          name = data['name']
     )
     newDept.save()
     Dept = Department.objects.all()
     serializer = DepartmentSerializer(Dept, many = True)
     return Response(serializer.data)

    
@api_view(['POST'])
def createExam(request, pk):
    Dept = Department.objects.get(id = pk)
    data = request.data
    newExam = Exam.objects.create(
         dept = Dept,
         name = data['name'],
         code = data['code'])
    newExam.save()
    Eam = Exam.objects.all()
    serializer = ExamSerializer(Eam, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createQuestion(request, pk):
    Eam = Exam.objects.get(id = pk)
    data = request.data
    newQuestion = Question.objects.create(
         exam = Eam,
         question = data['question'],
         options =  data['options'],
         true_option = data['true_option']
         )
    newQuestion.save()
    Ques = Question.objects.all()
    serializer = QuestionSerializer(Ques, many = True)
    return Response(serializer.data)

