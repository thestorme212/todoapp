from django.shortcuts import render , redirect
from . import models


# Create your views here.
def index(request):
    tasks = request.POST.get('task')

    tasksalli = models.todolists.objects.values_list('id', 'description').reverse()
    stuff_for_list = {
        'alltaski': tasksalli,
    }
    return render(request, 'index.html',stuff_for_list)


def list(request):
    tasks = request.POST.get('task')
    models.todolists.objects.create(description=tasks)
    tasksall = models.todolists.objects.values_list('id', 'description').reverse()
    stuff_for_frontend = {
        'task': tasks,
        'alltask': tasksall,
    }
    return render(request, 'todel_list.html', stuff_for_frontend)
def update_task(request, pk):
    uptask = models.todolists.objects.get(id=pk)
    if request.method == 'POST':
        uptask.save()
        models.todolists.objects.filter(id=pk).update(description=request.POST.get('task'))
        return redirect('/')
    use_frontend = {
        'todo': uptask
    }
    return render(request, 'update_task.html', use_frontend)

def delete_task(request,pk):
    uptask = models.todolists.objects.get(id=pk)
    if request.method == 'POST':
        models.todolists.objects.filter(id=pk).delete()
        print('am deleteted ')
        return redirect('/')

    use_frontend = {
        'todo': uptask
    }
    return render(request,'delete_task.html',use_frontend)