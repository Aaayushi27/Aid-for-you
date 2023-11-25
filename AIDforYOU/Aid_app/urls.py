from django.urls import path,include
from.import views,doctor_views
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('feedback/',views.feedback,name="feedback"),
   path('registration/',doctor_views.registration,name="registration"),
   path('login/',doctor_views.login,name="login"),
   path('doctor_home/',doctor_views.doctor_home,name="doctor_home"),
   path('dedit_profile/',doctor_views.dedit_profile,name="dedit_profile"),
   path('doctor_details/',doctor_views.doctor_details,name="doctor_details"),
   path('doctor_logout/',doctor_views.doctor_logout,name="doctor_logout"),
   path('alldoctors/',views.alldoctors,name="alldoctors"),
   path('details/<str:id>/',views.details,name="details"),
   
   
]