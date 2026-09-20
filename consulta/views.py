from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Doctor, Patient, Consultation
from .forms import DoctorForm, PatientForm, ConsultationForm


# Create your views here.

def home(request):
    doctors = Doctor.objects.all()

    return render(request, 'index.html', {'doctors': doctors})

@login_required
@permission_required('consulta.view_doctor', raise_exception=True)
def doctors_list(request):
    doctors = Doctor.objects.all().order_by('CRM')

    return render(request, 'doctors_list.html', {'doctors': doctors})

@login_required
@permission_required('consulta.add_doctor', raise_exception=True)
def doctors_add(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Médico cadastrado com sucesso!')

            return redirect('doctors_list')

    else:
        form = DoctorForm()

    return render(request, 'doctors_add.html', {'form': form})

@login_required
@permission_required('consulta.change_doctor', raise_exception=True)
def doctors_edit(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)

        if form.is_valid():
            form.save()
            messages.success(request, 'Médico atualizado com sucesso!')

            return redirect('doctors_list')

    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'doctors_edit.html', {'form': form, 'doctor': doctor})

@login_required
@permission_required('consulta.delete_doctor', raise_exception=True)
def doctors_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Médico excluído com sucesso!')

        return redirect('doctors_list')

    return render(request, 'doctors_delete.html', {'doctor': doctor})

@login_required
@permission_required('consulta.view_patient', raise_exception=True)
def patients_list(request):
    patients = Patient.objects.all()

    return render(request, 'patients_list.html', {'patients': patients})

@login_required
@permission_required('consulta.add_patient', raise_exception=True)
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
@permission_required('consulta.change_patient', raise_exception=True)
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
@permission_required('consulta.delete_patient', raise_exception=True)
def patients_delete(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Paciente excluído com sucesso!')
        return redirect('patients_list')

    return render(request, 'patients_delete.html', {'patient': patient})

@login_required
@permission_required('consulta.view_consultation', raise_exception=True)
def consults_list(request):
    consultas = Consultation.objects.select_related('doctor','patient').order_by('date')
    
    return render(request, 'consults_list.html', { "consultas": consultas })

@login_required
@permission_required('consulta.add_consultation', raise_exception=True)
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
@permission_required('consulta.change_consultation', raise_exception=True)
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
@permission_required('consulta.delete_consultation', raise_exception=True)
def consults_delete(request, id):
    consulta = get_object_or_404(Consultation, id=id)

    if request.method == 'POST':
        consulta.delete()
        messages.success(request,'Consulta excluída com sucesso!')
        return redirect("consults_list")

    return render(request, "consults_delete.html", {"consulta": consulta})

def permission_denied(request, exception):

    return render(request, '403.html', status=403)