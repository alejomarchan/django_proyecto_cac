from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def registro(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Tu cuenta ha sido creada!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'formulario': form}
    return render(request, 'registro.html', context)