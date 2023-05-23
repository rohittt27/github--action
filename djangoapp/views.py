from django.shortcuts import render, HttpResponse
from .forms import EmployeeForm
from .models import Employee

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Created Successfully')
    else:
        form = EmployeeForm()
    return render(request, 'employee.html', {'form': form})