from django.contrib import admin

# Register your models here.
from.models import Contact,Feedback_Rating,Health_Campaign, Doctor,DoctorDetails

class Health_Campaign_Admin(admin.ModelAdmin):
    list_display=('Campaign_Name','Organizer_Name','venue','Description','Date')
    search_fields=('Date',)

admin.site.register(Contact)
admin.site.register(Feedback_Rating)
admin.site.register(Health_Campaign,Health_Campaign_Admin)
admin.site.register(Doctor)
admin.site.register(DoctorDetails)


admin.site.site_header="AIDforYOU Administration"

admin.site.site_title="Admin dashboard"

admin.site.index_title="Welcome to AIDforYOU Portal"