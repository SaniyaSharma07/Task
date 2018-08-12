from django.urls import path
from . import views

urlpatterns=[
	path('providers/<int:provider_id>/appointments',views.show_appointments),
	# path('providers',views.show_providers),
	path('providers/<int:provider_id>/referrals/<referral_id>/_decline',views.decline_referral),
	path('providers/<int:provider_id>/referrals/<referral_id>/_accept',views.accept_referral),
	path('providers/<int:provider_id>/sent_referrals',views.sent_referrals),
	path('providers/<int:provider_id>/receive_referrals',views.receive_referrals),
	path('providers/_search',views.search_providers),
	# path('referrals/<int:referredById>/referredto/<int:referredToId>/patient/<int:patientId>/_create_referral',
	# views.create_referral)
	path('patients/<int:patient_id>/referrals',views.create_referral)
	# path('providers/<int:provider_id>/patients/<int:patient_id>/_create_referral',views.create_referral)
]



