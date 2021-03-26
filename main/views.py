from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import ToDO
from .forms import TodoForms


# Create your views here.

def index(request):
    todo_list = ToDO.objects.order_by('id')
    form = TodoForms()
    
    return render(request, 'main/index.html', {
        'todo_list': todo_list,
        'form': form})


@require_POST
def addTodo(request):
    form = TodoForms(request.POST)

    if form.is_valid():
        new_todo = ToDO(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    todo = ToDO.objects.get(id=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    ToDO.objects.filter(complete__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    ToDO.objects.all().delete()

    return redirect('index')