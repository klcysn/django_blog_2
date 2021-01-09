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
    profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance = request.user.profile)
    
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect(request.path)
    
    context = {
        "u_form": user_form,
        "p_form": profile_form
    }
    return render(request, "users/profile.html", context)