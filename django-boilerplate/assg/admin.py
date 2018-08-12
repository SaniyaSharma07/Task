from django.contrib import admin
from .models import Appointments,Referrals,Patient,Provider 

# Register your models here.
admin.site.Register(Appointments)
admin.site.Register(Referrals)
admin.site.Register(Patient)
admin.site.Register(Provider)
