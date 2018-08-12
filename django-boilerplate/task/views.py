from commons.utils.response import OK,NoContent,Created
from django.core import serializers
from .models import Referrals,Appointments,Provider,Patient
from pymodm.queryset import QuerySet
from django.views.decorators.http import require_http_methods
from datetime import datetime
from bson.objectid import ObjectId

@require_http_methods(["GET"])
def show_appointments(request,provider_id):
    appointment=list(Appointments.objects.raw({'providerId':provider_id}).values())
    response={
        'data':appointment
    }
    return OK(response)
    
# @require_http_methods(["GET"])
# def show_providers(request):
#     provider=list(Provider.objects.all().values())
#     response={
#         'data':provider
#     }
#     return OK(response)

@require_http_methods(["POST"])
def search_providers(request):
    query=request._json_body
    # print(type(query))
    filters=[]
    for k,v in query.items():
        filters.append({k:v})
    query = {
        '$and': filters
    }
    # print(query)
    resources = list(Provider.objects.raw(query).values())
    res={'data':resources}
    # print(res)
    return OK(res)
    
@require_http_methods(["PATCH"])
def decline_referral(request,provider_id,referral_id):
    query={
        'referredToId':provider_id,
        '_id':ObjectId(referral_id)
    }
    filters=[]
    for k,v in query.items():
        filters.append({k:v})
    finalquery={
        '$and':filters
    }
    res=Referrals.objects.raw(finalquery).update({"$set":{"status":"DECLINE"}})
    # res=Referrals.objects.raw({'referral_id':referral_id}).update({"$set":{"status":"DECLINE"}})
    return NoContent()

@require_http_methods(["PATCH"])
def accept_referral(request,provider_id,referral_id):
    query={
        'referredToId':provider_id,
        '_id':ObjectId(referral_id)
    }
    filters=[]
    for k,v in query.items():
        filters.append({k:v})
    finalquery={
        '$and':filters
    }
    res=Referrals.objects.raw(finalquery).update({"$set":{"status":"ACCEPT"}})
    response=Referrals.objects.raw(finalquery)
    # print(type(response))
    for r in response:
        Appointments(r.referredToId,r.patientId,datetime.now(),"SCHEDULED").save()
    return NoContent()

@require_http_methods(["GET"])
def sent_referrals(request,provider_id):
    referral = list(Referrals.objects.raw({'referredById': provider_id}).values())
    response={'data':referral}
    return OK(response) 

@require_http_methods(["GET"]) 
def receive_referrals(request,provider_id):
    referral=list(Referrals.objects.raw({'referredToId':provider_id}).values())
    response={'data':referral}
    return OK(response)

@require_http_methods(["POST"])
def create_referral(request,patient_id):
    query=request._json_body
    # print(type(query))
    referred_by_id=query.get('referredById',None)
    # print(type(patient_id))
    referred_to_id=query.get('referredToId',None)
    remarks=query.get('remarks',"No remarks")
    created_on=query.get('createdOn',datetime.now())
    updated_on=query.get('updatedOn',datetime.now())
    status=query.get('status',"PENDING")
    res=Referrals(patientId=patient_id,referredById=referred_by_id,
    referredToId=referred_to_id,createdOn=created_on,updatedOn=updated_on,
    status=status,remarks=remarks).save()
    # print(type(res))
    return Created(res.to_son()) 
    










