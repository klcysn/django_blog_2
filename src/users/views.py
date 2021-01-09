from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    form = RegistrationForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        # return redirect("login")
    context = {
        "form": form
    }
    return render(request, "users/register.html")

def profile(request):
    user_form = UserUpdateForm(request.POST or None, instance=request.user)