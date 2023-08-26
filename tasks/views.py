from django.shortcuts import render, redirect

tasks_list = []  # Lista para almacenar las tareas


def task_list(request):
    return render(request, 'tasks/task_list.html', {'tasks': tasks_list})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        tasks_list.append(title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')
