from django.db import models

# Create your models here.

class feedback(models.Model):
    FEEDBACK=models.CharField(max_length=200)
    POINTS=models.IntegerField()




class file(models.Model):
    STUDENT_NAME=models.CharField(max_length=100)
    FATHER_NAME=models.CharField(max_length=100)
    GENDER=models.CharField(max_length=100)
    DATE_OF_BIRTH=models.CharField(max_length=100)
    AGE=models.IntegerField()
    RELIGION=models.CharField(max_length=100)
    BLOOD_GROUP=models.CharField(max_length=100)
    ADHAR_CARD_NUMBER=models.CharField(max_length=20)
    SSLC_MARK=models.IntegerField()
    HSC_MARK=models.IntegerField()
    DEGREE=models.CharField(max_length=100)
    COURSE=models.CharField(max_length=100)
    STUDENT_PHONE_NUMBER=models.CharField(max_length=20)
    PARENTS_PHONE_NUMBER=models.CharField(max_length=20)
    EMAIL_ID=models.EmailField()
    PASSWORD=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=100)



class joining(models.Model):
    ROOL_NUMBER=models.CharField(max_length=100)
    STUDENT_NAME=models.CharField(max_length=100)
    FATHER_NAME=models.CharField(max_length=100)
    GENDER=models.CharField(max_length=100)
    DATE_OF_BIRTH=models.CharField(max_length=100)
    AGE=models.IntegerField()
    RELIGION=models.CharField(max_length=100)
    BLOOD_GROUP=models.CharField(max_length=100)
    ADHAR_CARD_NUMBER=models.CharField(max_length=20)
    FIRST_GRADUATE=models.CharField(max_length=100)
    SSLC_MARK=models.IntegerField()
    HSC_MARK=models.IntegerField()
    DEGREE=models.CharField(max_length=100)
    COURSE=models.CharField(max_length=100)
    STUDENT_PHONE_NUMBER=models.CharField(max_length=20)
    PARENTS_PHONE_NUMBER=models.CharField(max_length=20)
    EMAIL_ID=models.EmailField()
    PASSWORD=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=100)



class staff(models.Model):
    STAFF_ROOL_NUMBER=models.CharField(max_length=100)
    STAFF_NAME=models.CharField(max_length=100)
    GENDER=models.CharField(max_length=100)
    DEPARTMENT=models.CharField(max_length=100)
    AGE=models.IntegerField()
    STAFF_PHONE_NUMBER=models.IntegerField()
    EXPERNICES=models.CharField(max_length=100)
    SALARY=models.CharField(max_length=100)



class result(models.Model):
    ROOL_NUMBER=models.CharField(max_length=100)
    NAME=models.CharField(max_length=100)
    DEPARTMENT=models.CharField(max_length=100)
    PAPER_1=models.IntegerField()
    PAPER_2=models.IntegerField()
    PAPER_3=models.IntegerField()
    PAPER_4=models.IntegerField()
    PAPER_5=models.IntegerField()
    TOTAL=models.IntegerField()
    RESULT=models.CharField(max_length=10)

class kamal(models.Model):
    name=models.CharField(max_length=10)
    number=models.IntegerField()
    
