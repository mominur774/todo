from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Todo
from .forms import TodoForm

# Create your views here.


class AddTodo(View):
    def get(self, request):
        form = TodoForm()
        items = Todo.objects.all()
        return render(request, 'item/todo.html', {'form': form, 'items': items})

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


def deleteTodo(request, pk):
    item = Todo.objects.get(pk=pk)
    item.delete()
    return redirect('/')
