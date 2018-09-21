from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import (CreateView)
# Create your views here.

# class SignUp(CreateView):
#
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')# when a user is successfully signup then it will reverse to the login page
#                                         # reverse_lazy dosen't create action util the user dosen't press the sign up button
#     template_name = 'accounts/signup.html'

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('test')
    else:
        form = forms.UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})



