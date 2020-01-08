from django.shortcuts import render, HttpResponse
from .models import EmpDetails
from .forms import EmpDetailsForm

def home_page(request):
    return HttpResponse("Welcome to my Home Page ...!")

def hello_world(request):
    return render(request, template_name='hello_world.html')

def about_page(request):
    return render(request, template_name='about_page.html')

def welcome_page(request):
    dict = {'user' : 'Vasi'}
    return render(request, template_name='welcome_page.html', context=dict)

def emp_details(request):
    # example {'nandha' : 1, 'gopal' :123}
    queryset = EmpDetails.objects.all()
    Dict = {}
    for emp_detail in queryset:
        Dict[emp_detail.emp_name] = emp_detail.emp_id
    return render(request, template_name='emp_details.html', context={'Dict' :Dict})

def register_emp(request):
    if request.method == 'POST':
        print(request.POST)
        form = EmpDetailsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            err = "Form validation is failed..."
            print(err)
    form = EmpDetailsForm()
    return render(request, template_name='emp_register.html', context={'form' :form})
