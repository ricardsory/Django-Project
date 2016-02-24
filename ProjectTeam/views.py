from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User

from .forms import Login

def login(request):
    users = User.objects.all()
    return render(request, 'ProjectTeam/templates/login_old.html', {'users':users})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Login(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Login()

    return render(request, 'login_old.html', {'form': form})