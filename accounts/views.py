from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import (CreateView)
# Create your views here.

class SignUp(CreateView):

    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')# when a user is successfully signup then it will reverse to the login page
                                        # reverse_lazy dosen't create action util the user dosen't press the sign up button
    template_name = 'accounts/signup.html'



