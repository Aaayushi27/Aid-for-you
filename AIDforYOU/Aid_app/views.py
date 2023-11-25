from django.shortcuts import render
from.models import Contact,Feedback_Rating,Health_Campaign,DoctorDetails,Doctor
from django.contrib import messages


# Create your views here.
def home(request):
   Health_Campaign_List=Health_Campaign.objects.all() 
   print(Health_Campaign_List)     #equivalent to select*from Health_Campaign 
   #list(dynamic data) to template
   context={
      "Health_Campaign_key":Health_Campaign_List
       
    }
   return render(request, 'Aid_app/html/home.html',context)
def about(request):
    return render(request, 'Aid_app/html/about.html')
def contact(request):
    if request.method=='GET':
      return render(request,'Aid_app/html/contact.html')
      
    if  request.method=='POST':
         # code for data insertion and then send back on the same page with message
         user_name=request.POST["name"] #fetching the values from controls using name
         user_email=request.POST["email"] #request post is built-in dictionary
         user_phone=request.POST["phone"]
         user_query=request.POST["query"]
         # print(user_name,user_email,user_phone,user_query)
         contact=Contact(name=user_name,email=user_email,phone=user_phone,question=user_query)
         contact.save() #ORM Framework
         messages.success(request, "Thank You for Contacting Us We will Reach You Soon!!!  ")
         print("contact saved")
         return render(request, 'Aid_app/html/contact.html')
def feedback(request):
     if request.method=='GET':
        return render(request, 'Aid_app/html/feedback.html')
     if request.method=='POST':
        user_name=request.POST["name"]
        user_email=request.POST["email"]
        user_feedback=request.POST["feedback"]
        user_ratings=request.POST["ratings"]
      
      # print(user_name,user_email,user_ratings,user_feedback)
        feedback=Feedback_Rating(name=user_name,email=user_email,feedback_text=user_feedback,ratings=user_ratings)
        feedback.save()
        messages.success(request, "Thank You for  Your Valuable feedback We will Reach You Soon!!!  ")
        print("feedback saved")
        return render(request, 'Aid_app/html/feedback.html')

def alldoctors(request):
   doctor_list=Doctor.objects.all()
   context={
      "doctor_data":doctor_list
   }
   return render(request,'Aid_app/html/alldoctors.html',context)



def details(request,id):
  print("doctor id is,id")
  doctor_object=Doctor.objects.get(Doctorid=id)
  dd=DoctorDetails.objects.get(doctor=doctor_object)
  context={"dd":dd}
  return render(request,'Aid_app/html/details.html',context)
