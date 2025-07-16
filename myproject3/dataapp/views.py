# from django.shortcuts import get_object_or_404, render, redirect
# from .models import Patient
# from .forms import PatientForm



# def data(request):
#     return render(request,"dataapp/mainpage.html")

# def mainpage(request):
#     return render(request,"dataapp/mainpage.html")

# def about(request):
#     return render(request,"dataapp/aboutus.html")

# def register(request):
#     return render(request,"dataapp/register.html")

# def login(request):
#     return render(request,"dataapp/login.html")

# def services(request):
#     return render(request,"dataapp/services.html")


# def appointment(request):
#     return render(request,"dataapp/appointment.html")

# def consultation(request):
#     return render(request,"dataapp/onlineconsult.html")


# from django.shortcuts import render
# from .models import Patient
# # Create your views here.

# def person_list(request):
#     people = Patient.objects.all()
#     return render(request,"dataapp/person_list.html",{'people':people})

# def add_person(request):
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person_list')
#     else:
#         form = PatientForm()
#     return render(request,'dataapp/add_person.html',{'form':form})

# def delete_person(request, pk):
#     person = get_object_or_404(Patient, pk=pk)
#     if request.method == 'POST':
#         person.delete()
#         return redirect('person_list')
#     return render(request, 'dataapp/delete_person.html', {'person': person}),


# def update_person(request, pk):
#     person = get_object_or_404(Patient, pk=pk)
#     if request.method == 'POST':
#         form = PatientForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_list')
#     else:
#         form = PatientForm(instance=person)
#     return render(request, 'dataapp/update_person.html', {'form': form, 'person': person})


from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointSerializer

class TaskViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointSerializer

