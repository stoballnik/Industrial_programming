from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('index')
    else:
        return render(request, 'add.html')

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deleteComplete(request):
    Todo.objects.filter(completed__exact=True).delete()

    return render('index.html')

def deleteAll(request):
    Todo.objects.all().delete()

    return render('index.html')