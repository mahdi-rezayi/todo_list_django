from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from main.models import *


# Create your views here.

def categoryList(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/category/index.html', context)


def categoryCreate(request):
    return render(request, 'main/category/create.html')


def categoryStore(request):
    if request.method == 'POST':
        category_name = request.POST.get('name')
        Category.objects.create(name=category_name)
        return redirect('category_list')

    raise Http404("the method is not correct")


def categoryEdit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {'category': category}
    return render(request, 'main/category/edit.html', context)


def categoryUpdate(request, pk):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=pk)
        category.name = request.POST.get('name')
        category.save()
        return redirect('category_list')

    raise Http404("The method is not correct")


def categoryDelete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


def todoList(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'main/todo/index.html', context)


def todoCreate(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'main/todo/create.html', context)


def todoStore(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        is_completed = request.POST.get('is_completed') == 'on'

        category = None
        if category_id:
            category = get_object_or_404(Category, pk=category_id)

        Todo.objects.create(
            title=title,
            description=description,
            category=category,
            is_completed=is_completed
        )
        return redirect('todo_list')

    raise Http404("The method is not correct")


def todoEdit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    categories = Category.objects.all()
    context = {'todo': todo, 'categories': categories}
    return render(request, 'main/todo/edit.html', context)


def todoUpdate(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=pk)
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        category_id = request.POST.get('category')
        is_completed = request.POST.get('is_completed') == 'on'

        if category_id:
            todo.category = get_object_or_404(Category, pk=category_id)
        else:
            todo.category = None

        todo.is_completed = is_completed
        todo.save()
        return redirect('todo_list')

    raise Http404("The method is not correct")


def todoDelete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')


def todoComplete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect('todo_list')
