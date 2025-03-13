from django.shortcuts import*
from django.contrib import messages
from django.http import HttpResponse
from college.models import feedback,file,joining,staff,result


def home(request):
    return render(request, "home.html")


def certificate(request):
    if request.method=="POST":
        n=request.POST["student_name"]
        r=request.POST["student_rool_number"]
        z=joining.objects.filter(STUDENT_NAME=n,ROOL_NUMBER=r)
        if z:
            c=request.POST["certificate"]
            return render(request,"certificate.html",{"a":z,"z":c})
        else:
            return redirect("home")


def application_form(request):
    if request.method=="POST":
        sn=request.POST['stutdent_name']
        fn=request.POST['father_name']
        g=request.POST['gender']
        db=request.POST['data_of_birth']
        a=request.POST['age']
        r=request.POST['religion']
        bg=request.POST['blood_group']
        an=request.POST['adhar_number']
        te=request.POST['ten']
        tw=request.POST['twelve']
        d=request.POST['degree']
        c=request.POST['course']
        sp=request.POST['STUDENT_PHONE_NUMBER']
        pp=request.POST['parents_PHONE_NUMBER']
        e=request.POST['email']
        pa=request.POST['password']
        ad=request.POST['address']        
        app=file(STUDENT_NAME=sn,FATHER_NAME=fn,GENDER=g,DATE_OF_BIRTH=db,AGE=a,
                      RELIGION=r,BLOOD_GROUP=bg,ADHAR_CARD_NUMBER=an,SSLC_MARK=te,HSC_MARK=tw,
                      DEGREE=d,COURSE=c,STUDENT_PHONE_NUMBER=sp,PARENTS_PHONE_NUMBER=pp,EMAIL_ID=e,
                      PASSWORD=pa,ADDRESS=ad)
        app.save()
        messages.success(request,"YOUR APPLICATION IS RECEIVED!!!!")
    return render(request,"application_form.html")


def fees(request):
    return render(request, "fees.html")


def exam_time_table(request):
    return render(request,"exam_time_table.html")


def exam_result(request):
    if request.method=="POST":
        n=request.POST['name']
        r=request.POST['rool_number']

        r=result.objects.filter(NAME=n,ROOL_NUMBER=r)
        if r:
            return render(request,"exam_result_show.html",{'z':r})
        else:
           
            messages.success(request,"INVALID NAME (or) ROOL_NUMBER")

    return render(request,"exam_result.html")


def celebrity(request):
    return render(request,"celebrity.html")


def gallery(request):
    return render(request, "gallery.html")


def video(request):
    return render(request,"video.html")

def map(request):
    return render(request,"map.html")


def feedback_store(request):
    if request.method=="POST":
        f=request.POST['feedback']
        p=request.POST['points']
        feed=feedback(FEEDBACK=f,POINTS=p)
        feed.save()
        messages.info(request, "YOUR FEEDBACK IS SUBMITED FOR SUCCESSFULLY!!!!")
    return render(request,"feedback.html")



def admin_login(request):
    if request.method == "POST":
        n= "kiasc" 
        p= "kiasc"
        sn = request.POST.get('student_name')
        sr= request.POST.get('student_rool_number')  
        if n==sn and p==sr:
            return render(request, "admin.html")
        else:
            return redirect("home")



def admin_on(request):
    return render(request,"admin.html")


def store_data(request):
    return render(request,"store_data.html")


def view_data(request):
    return render(request,"view_data.html")


def addmision_store(request):
    if request.method=="POST":
        rn=request.POST['rool_number']
        sn=request.POST['stutdent_name']
        fn=request.POST['father_name']
        g=request.POST['gender']
        db=request.POST['data_of_birth']
        a=request.POST['age']
        r=request.POST['religion']
        bg=request.POST['blood_group']
        an=request.POST['adhar_number']
        fg=request.POST['first_graduate']
        te=request.POST['ten']
        tw=request.POST['twelve']
        d=request.POST['degree']
        c=request.POST['course']
        sp=request.POST['STUDENT_PHONE_NUMBER']
        pp=request.POST['parents_PHONE_NUMBER']
        e=request.POST['email']
        pa=request.POST['password']
        ad=request.POST['address']
        
        add=joining(ROOL_NUMBER=rn,STUDENT_NAME=sn,FATHER_NAME=fn,GENDER=g,DATE_OF_BIRTH=db,AGE=a,
                      RELIGION=r,BLOOD_GROUP=bg,ADHAR_CARD_NUMBER=an,FIRST_GRADUATE=fg,SSLC_MARK=te,HSC_MARK=tw,
                      DEGREE=d,COURSE=c,STUDENT_PHONE_NUMBER=sp,PARENTS_PHONE_NUMBER=pp,EMAIL_ID=e,
                      PASSWORD=pa,ADDRESS=ad)
        add.save()
        messages.success(request,"STUDENT DETAILS SUBMITED FOR SUCCESSFULLY!!!")
    return render(request,"addmision_store.html")

    
def result_store(request):
    if request.method=="POST":
        rn=request.POST['rool_number']
        n=request.POST['name']
        dp=request.POST['department']
        p1=int(request.POST['p1'])
        p2=int(request.POST['p2'])
        p3=int(request.POST['p3'])
        p4=int(request.POST['p4'])
        p5=int(request.POST['p5'])
        to=p1+p2+p3+p4+p5
        if p1>=35 and p2>=35 and p3>=35 and p4>=35 and p5>=35:
            re="PASS"
        else:
            re="FAIL" 
        res=result(ROOL_NUMBER=rn,NAME=n,DEPARTMENT=dp,PAPER_1=p1,
                  PAPER_2=p2,PAPER_3=p3,PAPER_4=p4,PAPER_5=p5,
                      TOTAL=to,RESULT=re)
        res.save()
        messages.success(request,"STUDENT RESULT DATA SUBMITED")
    return render(request,"result_store.html")


    
def staff_store(request):
    if request.method=="POST":
        rn=request.POST['staff_rool_number']
        sn=request.POST['staff_name']
        g=request.POST['gender']
        dp=request.POST['department']
        a=request.POST['age']
        sp=request.POST['staff_phone_number']
        ex=request.POST['expernices']
        sa=request.POST['salary']        
        sta=staff(STAFF_ROOL_NUMBER=rn,STAFF_NAME=sn,
                  GENDER=g,DEPARTMENT=dp,AGE=a,
                      EXPERNICES=ex, STAFF_PHONE_NUMBER=sp,SALARY=sa)
        sta.save()
        messages.success(request,"STAFF DETAILS SUBMITED FOR SUCCESSFILLY")
    return render(request,"staff_store.html")




def application_view(request):
    a=file.objects.all()
    return render(request, "application_view.html",{"z":a})



def staff_view(request):
    a=staff.objects.all()
    return render(request, "staff_view.html",{"z":a})



def feedback_view(request):
    v=feedback.objects.all()
    return render(request,"feedback_view.html",{"z":v})



def exam_result_view(request):
    v=result.objects.all()
    return render(request,"result_view.html",{"z":v})


def addmision_view(request):
    v=joining.objects.all()
    return render(request,"addmision_view.html",{"z":v})




def delete_add(request,id):
    d=joining.objects.get(id=id)
    d.delete()
    messages.info(request,"deleted for successfully")
    return redirect("addmision_view")


def delete_feed(request,id):
    d=feedback.objects.get(id=id)
    d.delete()
    messages.info(request,"deleted for successfully")
    return redirect("feedback_view")


def delete_app(request,id):
    d=file.objects.get(id=id)
    d.delete()
    messages.info(request,"deleted for successfully")
    return redirect("application_view")


def delete_staff(request,id):
    d=staff.objects.get(id=id)
    d.delete()
    messages.info(request,"deleted for successfully")
    return redirect("staff_view")



def delete_result(request,id):
    d=result.objects.get(id=id)
    d.delete()
    messages.info(request,"deleted for successfully")
    return redirect("exam_result_view")



def update_result(request,id):
    d=result.objects.filter(id=id)
    
    if request.method=="POST":
        for d in d:

            rn=request.POST['rool_number']
            n=request.POST['name']
            dp=request.POST['department']
            p1=int(request.POST['p1'])
            p2=int(request.POST['p2'])
            p3=int(request.POST['p3'])
            p4=int(request.POST['p4'])
            p5=int(request.POST['p5'])
            to=p1+p2+p3+p4+p5
            if p1>=35 and p2>=35 and p3>=35 and p4>=35 and p5>=35:
                re="PASS"
            else:
                re="FAIL" 

            d.ROOL_NUMBER=rn
            d.NAME=n
            d.DEPARTMENT=dp
            d.PAPER_1=p1
            d.PAPER_2=p2
            d.PAPER_3=p3
            d.PAPER_4=p4
            d.PAPER_5=p5
            d.TOTAL=to
            d.RESULT=re
            d.save()
            messages.success(request,"STUDENT RESULT UPDATE FOR SUCCESSFULLY")
            return redirect("exam_result_view")
    return render(request,"update_result.html",{'a':d})


def update_staff(request,id):
    d=staff.objects.filter(id=id)
    
    if request.method=="POST":
        for d in d:
            rn=request.POST['staff_rool_number']
            sn=request.POST['staff_name']
            g=request.POST['gender']
            dp=request.POST['department']
            a=request.POST['age']
            sp=request.POST['staff_phone_number']
            ex=request.POST['expernices']
            sa=request.POST['salary'] 

            d.STAFF_ROOL_NUMBER =rn
            d.STAFF_NAME=sn
            d.GENDER=g
            d.DEPARTMENT=dp
            d.AGE=a
            d.EXPERNICES=ex
            d.STAFF_PHONE_NUMBER=sp
            d.SALARY=sa
            d.save()
            messages.success(request,"STAFF DETAILS UPDATE FOR SUCCESSFILLY")
            return redirect("staff_view")

    return render(request,"staff_update.html",{'a':d})


def update_addmision(request,id):
    d=joining.objects.filter(id=id)
    if request.method=="POST":
        for d in d:
            
            rn=request.POST['rool_number']
            sn=request.POST['stutdent_name']
            fn=request.POST['father_name']
            g=request.POST['gender']
            db=request.POST['data_of_birth']
            a=request.POST['age']
            r=request.POST['religion']
            bg=request.POST['blood_group']
            an=request.POST['adhar_number']
            fg=request.POST['first_graduate']
            te=request.POST['ten']
            tw=request.POST['twelve']
            de=request.POST['degree']
            c=request.POST['course']
            sp=request.POST['STUDENT_PHONE_NUMBER']
            pp=request.POST['parents_PHONE_NUMBER']
            e=request.POST['email']
            pa=request.POST['password']
            ad=request.POST['address']

            d.ROOL_NUMBER=rn
            d.STUDENT_NAME=sn
            d.FATHER_NAME=fn
            d.GENDER=g
            d.DATE_OF_BIRTH=db
            d.AGE=a
            d.RELIGION=r
            d.BLOOD_GROUP=bg
            d.ADHAR_CARD_NUMBER=an
            d.FIRST_GRADUATE=fg
            d.SSLC_MARK=te
            d.HSC_MARK=tw
            d.DEGREE=de
            d.COURSE=c
            d.STUDENT_PHONE_NUMBER=sp
            d.PARENTS_PHONE_NUMBER=pp
            d.EMAIL_ID=e
            d.PASSWORD=pa
            d.ADDRESS=ad
            d.save()


            messages.success(request," UPDATE FOR SUCCESSFILLY")
            return redirect("addmision_view")
    
    return  render(request,"update_addmision.html",{"a":d})



            