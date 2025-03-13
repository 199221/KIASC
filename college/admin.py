from django.contrib import admin
from college.models import feedback,file,joining,staff,result

# Register your models here.

class project1(admin.ModelAdmin):
    feed=["FEEDBACK","POINTS"]

admin.site.register(feedback,project1)


class project2(admin.ModelAdmin):
    app=["STUDENT_NAME","FATHER_NAME","GENDER","DATE_OF_BIRTH","AGE","RELIGION","BLOOD_GROUP","ADHAR_CARD_NUMBER","SSLC_MARK","HSC_MARK","DEGREE","COURSE","STUDENT_PHONE_NUMBER","PARENTS_PHONE_NUMBER","EMAIL_ID","PASSWORD","ADDRESS"]

admin.site.register(file,project2)



class project3(admin.ModelAdmin):
    add=["ROOL_NUMBER","STUDENT_NAME","FATHER_NAME","GENDER","DATE_OF_BIRTH","AGE","RELIGION","BLOOD_GROUP","ADHAR_CARD_NUMBER","FIRST_GRADUATE","SSLC_MARK","HSC_MARK","DEGREE","COURSE","STUDENT_PHONE_NUMBER","PARENTS_PHONE_NUMBER","EMAIL_ID","PASSWORD","ADDRESS"]

admin.site.register(joining,project3)



class project4(admin.ModelAdmin):
    sta=["STAFF_ROOL_NUMBER","STAFF_NAME","GENDER","AGE","DEPARTMENT","STAFF_PHONE_NUMBER","EXPERNICES","SALARY"]

admin.site.register(staff,project4)



class project5(admin.ModelAdmin):
    res=["ROOL_NUMBER","NAME","DEPARTMENT","PAPER_1","PAPER_2","PAPER_3","PAPER_4","PAPER_5","TOTAL","RESULT"]

admin.site.register(result,project5)
