from django.shortcuts import render, HttpResponseRedirect
from .forms import employeeRegistration
from .models import employee
# Create your views here.

# this function for adding new name and showing


def addandshow(request):
    if request.method == 'POST':
        fm = employeeRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            dm = fm.cleaned_data['department']
            reg = employee(name=nm, department=dm)
            reg.save()
            fm = employeeRegistration()
    else:
        fm = employeeRegistration()
    empd = employee.objects.all()

    return render(request, 'addandshow.html', {'form': fm, 'emp': empd})


#  this function will delete
def deletedata(request, id):
    if request.method == 'POST':
        pi = employee.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
