from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

# Read
@login_required
def task_list(request):
    taken = Task.objects.filter(gebruiker=request.user) 
    return render(request, 'tasks/task_list.html', {'taken': taken})

# Creëer
@login_required
def task_create(request):
    if request.method == "POST":
        titel = request.POST['titel']
        beschrijving = request.POST.get('beschrijving', '')
        taak = Task.objects.create(
            gebruiker=request.user,
            titel=titel,
            beschrijving=beschrijving
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

# Update: 
@login_required
def task_update(request, id):
    taak = get_object_or_404(Task, id=id, gebruiker=request.user)
    if request.method == "POST":
        taak.titel = request.POST['titel']
        taak.beschrijving = request.POST.get('beschrijving', '')
        taak.status = request.POST['status']
        taak.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'taak': taak})

# Verwijder 
@login_required
def task_delete(request, id):
    taak = get_object_or_404(Task, id=id, gebruiker=request.user)
    if request.method == "POST":
        taak.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'taak': taak})
