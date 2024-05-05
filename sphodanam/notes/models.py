from django.db import models

# Create your models here.
class Semester(models.Model):
    sem=models.IntegerField()
    
    def __str__(self) -> str:
        return self.sem
    
class Subjects(models.Model):
    name=models.CharField(max_length=100)
    sem=models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='subject')
    def __str__(self) -> str:
        return self.name
    
class Notes(models.Model):
   name=models.CharField(max_length=100)
   subject=models.ForeignKey(Subjects,on_delete=models.CASCADE,related_name='notes')