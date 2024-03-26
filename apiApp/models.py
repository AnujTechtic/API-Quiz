from django.db import models
import uuid
# Create your models here.
class Department(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    name = models.CharField(max_length = 50 ,unique=True)
    def __str__(self):
        return self.name
    
class Exam(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    name = models.CharField(max_length = 256 , null=True , blank = True,unique=False)
    code = models.CharField(max_length=10,unique=True ,null=False , blank = False)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    name = models.CharField(max_length=100 , editable = True)
    email = models.EmailField(max_length = 50 , editable = True)
    code = models.ForeignKey(Exam , on_delete = models.CASCADE)
    def __str__(self):
        return self.name
    
class Question(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    exam = models.ForeignKey(Exam , on_delete= models.CASCADE, null = True)
    question = models.TextField(editable = True)
    options = models.JSONField(default={"1":"", "2": "", "3": "", "4": ""})
    true_option = models.IntegerField()
    def __str__(self):
        return self.question
    
class Log(models.Model):
    question = models.ForeignKey(Question , on_delete = models.CASCADE)
    student = models.ForeignKey(Student , on_delete = models.CASCADE)
    ans = models.IntegerField(editable= True)
    validity = models.BooleanField(default = False , editable = True , null = True)
    attempt = models.BooleanField(default = False)    
    class Meta:
        unique_together = ('question', 'student')
    def __int__(self):
        return self.student