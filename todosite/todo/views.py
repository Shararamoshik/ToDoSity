from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# Create your views here.
def main_view(request):
    return render(request, 'main/main.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        # Создаем новую задачу
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            user=request.user  # Привязываем к текущему пользователю
        )
        return redirect('task_list')

    return render(request, 'todo/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        # Берем данные из формы
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed') == 'on'
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')

        # Проверяем, что заголовок есть
        if title:
            # Создаем задачу с привязкой к пользователю
            task = Task.objects.create(
                user=request.user,  # ВАЖНО: привязываем к текущему пользователю
                title=title,
                description=description,
                completed=completed,
            )

            # Обрабатываем дату и время, если они есть
            if due_date:
                task.due_date = due_date
            if due_time:
                task.due_time = due_time
            task.save()

            return redirect('task_list')

        # Если GET запрос или ошибка - возвращаем на список
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return redirect('task_list')

