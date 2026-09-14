from django.shortcuts import render, redirect
from .models import Consultation, Doctor
from .forms import ConsultationForm


# Create your views here.

def home(request):
    doctors = Doctor.objects.all()

    return render(request, 'index.html', { 'doctors': doctors })

def consults_list(request):
    consultas = Consultation.objects.all()
    return render(request, 'consults_list.html', { "consultas": consultas })

def consults_add(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('consults_list')

    else:
        form = ConsultationForm()

    return render(request, 'consults_add.html', { 'form': form })

def consults_edit(request, id):
    consulta = Consultation.objects.get(id=id)

    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consulta)

        if form.is_valid():
            form.save()
            return redirect('consults_list')

    else:
        form = ConsultationForm(instance=consulta)

    return render(request, 'consults_edit.html', {'form': form})

def consults_delete(request, id):
    consulta = Consultation.objects.get(id=id)

    if request.method == 'POST':
        consulta.delete()
        return redirect("consults_list")

    return render(request, "consults_delete.html", {"consulta": consulta})