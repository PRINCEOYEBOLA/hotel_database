from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Record

# Create your views here.

def staff(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect("management:loginview")
        else:
            pass
    context = {
        "form": UserCreationForm()
        }
    return render(request, "management/staff.html", context)

def AddUser(request):
    if request.method == "POST":
        occupant_name = request.POST.get('occupant_name')
        occupant_email= request.POST.get('occupant_email')
        occupant_work = request.POST.get('occupant_work')
        amount_paid   = request.POST.get('amount_paid')
        room_number   = request.POST.get('room_number')
        duration      = request.POST.get('duration')
        checkin       = request.POST.get('checkin')
        checkout      = request.POST.get('checkout')
        
        new_customer = Record(Occupant_Name=occupant_name, 
                              Occupant_Email=occupant_email, 
                              Occupant_Occupation=occupant_work, 
                              Amount_Paid=amount_paid, 
                              Room_Number=room_number, 
                              No_of_Night=duration,
                              Start_date=checkin,
                              End_date=checkout,
                              )
        new_customer.save()
        return redirect('management:portalview')
        
    return render(request, "management/AddUser.html")

def login(request):
    return redirect("management:adduserview")

def portal(request):
    return render(request, "management/portal.html")

