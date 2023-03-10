from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #Get the each data('username') from form
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #user authentication
            login(request, user) #login
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})