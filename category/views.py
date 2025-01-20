from django.shortcuts import render, redirect
from .form import CategoryForm

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})
