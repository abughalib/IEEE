from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib import messages
from django.contrib.messages import get_messages
# Create your views here.


def home(request):
    message = get_messages(request)
    message.used = True
    return render(request, 'Home/index.html', {'message': message})


def reg_form(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Form Submitted successfully")
            return redirect(home)
        else:
            print(request.POST)
            error = "Verify your input"
            if len(form.WNumber) < 10 or form.WNumber.isnumeric():
                error = "Check Your mobile Number"
            registration_form = RegForm()
            return render(request, 'Home/RegistrationForm.html',
                          {'form': registration_form, 'error': error})
    registration_form = RegForm()
    return render(request, 'Home/RegistrationForm.html', {'form': registration_form})
