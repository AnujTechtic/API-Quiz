from rest_framework import serializers
from .models import Department, Exam, Student, Question, Log

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Department
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Exam
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Question
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Log
        fields = '__all__'