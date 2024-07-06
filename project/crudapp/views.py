# crudapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
from .forms import AppointmentForm

def index(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_form.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('index')
    return render(request, 'appointment_form.html', {'appointment': appointment})
