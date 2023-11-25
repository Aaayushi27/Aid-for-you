from django.shortcuts import render
from.models import Doctor,DoctorDetails
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def registration(request):
    if request.method=='GET':
        return render(request,'Aid_app/Doctor/doctor.html')
    if request.method=='POST':
        doctor_id=request.POST["Doctorid"]

        doc_list=Doctor.objects.filter(Doctorid=doctor_id)
        # doclen=len(doc_list)
        # if(doc_len>0):
        #       messages.success(request,"This Id already exists!!👍😝")
        # # print("doctor saved")
        # return render(request,'Aid_app/Doctor/doctor.html')

        password=request.POST["password"]
        name=request.POST["name"]
        address=request.POST["address"]
        email=request.POST["email"]
        gender=request.POST["gender"]
        phone=request.POST["phone"]
        age=request.POST["age"]
        cityname=request.POST["cityName"]
        fieldSpecialist=request.POST["fieldSpecialist"]
        experience=request.POST["experience"]
        print(doctor_id,password,name,address,email,gender,phone,age,cityname,fieldSpecialist,experience)
        doctor=Doctor(Doctorid=doctor_id,password=password,name=name,address=address,email=email,gender=gender,phone=phone,age=age,cityName=cityname,fieldSpecialist=fieldSpecialist,experience=experience)
        doctor.save()#ORM framework
        messages.success(request,"Registration done successfully you can do login now!!👍😝")
        # print("doctor saved")
        return render(request,'Aid_app/Doctor/doctor.html')

def login(request):
    if request.method =='GET':
       return render(request,'Aid_app/Doctor/login.html')
    if request.method=='POST':
        doctor_id=request.POST["Doctorid"]
        password=request.POST["password"]
        doctor_list=Doctor.objects.filter(Doctorid=doctor_id,password=password)
        x=len(doctor_list)
        print("length is",x)
        if x>0:
            doctor_object=Doctor.objects.get(Doctorid=doctor_id)
            request.session["session_key"]=doctor_id
            context={"doctor_data":doctor_object}
            return render(request,'Aid_app/Doctor/doctor_home.html',context)
        else:
            messages.error(request,"Invalid Credentials😢☹️")
        return render(request,'Aid_app/Doctor/login.html')

def doctor_home(request):
    loggedin_userid=request.session["session_key"] #fething values from session
    doctor_object=Doctor.objects.get(Doctorid=loggedin_userid)
    context={"doctor_data":doctor_object}
    return render(request,'Aid_app/Doctor/doctor_home.html',context )

def dedit_profile(request):
    if request.method =='GET':
        loggedin_userid=request.session["session_key"] #fething values from session
        doctor_object=Doctor.objects.get(Doctorid=loggedin_userid)
        context={"doctor_data":doctor_object}
        return render(request,'Aid_app/Doctor/doctorprofile.html',context)
    if request.method=='POST':
        print("in post method")
        user_email=request.POST["email"]
        user_phone=request.POST["phone"]
        user_cityname=request.POST["city"]
        user_address=request.POST["address"]
        loggedin_userid=request.session["session_key"] #fething values from #session
        print(loggedin_userid)
        doctor_object=Doctor.objects.get(Doctorid=loggedin_userid)
        doctor_object.email=user_email
        doctor_object.phone=user_phone
        doctor_object.cityname=user_cityname
        doctor_object.address=user_address
        doctor_object.save()
        print("profile updated😍")
        context={"doctor_data":doctor_object}
        return render(request,'Aid_app/Doctor/doctor_home.html',context)


def doctor_details(request):
    if request.method =='GET':
       return render(request,'Aid_app/Doctor/doctor_details.html')
    if request.method =='POST':
        Doctorid= request.session["session_key"]
        print(Doctorid)
        fieldname_list=request.POST.getlist("fieldname")
        print(fieldname_list)
        fieldname=""
        
        for f in fieldname_list:
            fieldname=fieldname+f+","

        # specialization_list=request.POST.getlist("specialization")
        # print(specialization_list)
        # specialization=""
        # for s in specialization_list:
        #     specialization=specialization+s+","
        # print(specialization)
        specialization=request.POST["specialization"]
        visiting_hours=request.POST["visiting_hours"]
        other_details=request.POST["details"]
        print(specialization,visiting_hours,other_details)

        upload_pic=request.FILES["profile_pic"]
        fs=FileSystemStorage()
        file_obj=fs.save(upload_pic.name,upload_pic)
        uploadfile_url=fs.url(file_obj)
        doctor_object=Doctor.objects.get(Doctorid=Doctorid)
        dd=DoctorDetails(doctor=doctor_object,fieldname=fieldname,doctor_pic=upload_pic,specialization=specialization,visiting_hours=visiting_hours,description=other_details)
        dd.save()
        # messages.success(request,"your details are saved now!!👍🙂")
        return render(request,'Aid_app/Doctor/doctor_details.html')

def doctor_logout(request):
    del request.session["session_key"]
    messages.success(request,"successfully logout😁😊")
    return render(request,'Aid_app/Doctor/login.html')


