from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Consultation, Doctor, Patient
from .forms import ConsultationForm, PatientForm


# Create your views here.

def home(request):
    doctors = Doctor.objects.all()

    return render(request, 'index.html', { 'doctors': doctors })

@login_required
def consults_list(request):
    consultas = Consultation.objects.select_related('doctor','patient').order_by('date')
    
    return render(request, 'consults_list.html', { "consultas": consultas })

@login_required
def consults_add(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Consulta agendada com sucesso!')
            return redirect('consults_list')

    else:
        form = ConsultationForm()

    return render(request, 'consults_add.html', { 'form': form })

@login_required
def consults_edit(request, id):
    consulta = get_object_or_404(Consultation, id=id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consulta)

        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta atualizada com sucesso!')
            return redirect('consults_list')

    else:
        form = ConsultationForm(instance=consulta)

    return render(request, 'consults_edit.html', {'form': form})

@login_required
def consults_delete(request, id):
    consulta = get_object_or_404(Consultation, id=id)

    if request.method == 'POST':
        consulta.delete()
        messages.success(request,'Consulta excluída com sucesso!')
        return redirect("consults_list")

    return render(request, "consults_delete.html", {"consulta": consulta})

@login_required
def patients_list(request):
    patients = Patient.objects.all()

    return render(request, 'patients_list.html', {'patients': patients})

@login_required
def patients_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm()

    return render(request, 'patients_add.html', {'form': form})

@login_required
def patients_edit(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente atualizado com sucesso!')
            return redirect('patients_list')

    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients_edit.html', {'form': form})

@login_required
def patients_delete(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Paciente excluído com sucesso!')
        return redirect('patients_list')

    return render(request, 'patients_delete.html', {'patient': patient})