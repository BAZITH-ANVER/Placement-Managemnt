from django.db import models
from placementapp.models import *
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User,Group

# Create your models here.
class Student(models.Model):
    FullName=models.CharField(max_length=50)
    MY_GENDER = (("male","Male"), ("female","Female"), ("others","Others"))
    Gender=models.CharField(max_length=300,choices=MY_GENDER,verbose_name="Gender")
    Address=models.TextField()
    phoneNumber=models.CharField(max_length=50)
    qualification=models.ForeignKey(Qualification,on_delete=models.CASCADE)  
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch=ChainedForeignKey(Batch,
        chained_field="course",
        chained_model_field="course",
        show_all=False,
        auto_choose=True,
        sort=True) 
    trainer = ChainedForeignKey(Trainer,
        chained_field="trainer",
        chained_model_field="trainer",
        show_all=False,
        auto_choose=True,
        sort=True)
    verify = models.BooleanField(default=False)  
       
    def save(self, *args, **kwargs):
        username = f"{self.FullName}"
        password =  f"{self.FullName.replace(' ', '_')}@oneteam"
        user, created = User.objects.get_or_create(username=username)
        user.set_password(password)
        user.is_staff = True
        student_group, created = Group.objects.get_or_create(name='Student')
        user.groups.add(student_group)
        user.save()
        super().save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        user = User.objects.get(username=f"{self.FullName}")
        student_group = Group.objects.get(name='Student')
        if user.groups.filter(name='Student').exists():
            user.groups.remove(student_group)
        user.delete()
        super().delete(*args, **kwargs)    
    
    
    def __str__(self):
        return self.FullName         
class Resume(models.Model):
    FullName=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    resume=models.FileField(upload_to='upload_pdfs/', blank=True, null=True)
    
    def __str__(self):
        return self.FullName   
class JobApply(models.Model):
    FullName=models.CharField(max_length=50)
    WORK_EXPERIENCE_CHOICES = (
        ('Fresher', 'Fresher'),
        ('1-3 years', '1-3 years'),
        ('4-7 years', '4-7 years'),
        ('8+ years', '8+ years'),
    )     
    Work_Experience = models.CharField(max_length=20, choices=WORK_EXPERIENCE_CHOICES)
    resume=models.FileField(upload_to='upload_pdfs/', blank=True, null=True)
    
    def __str__(self):
        return self.FullName  
