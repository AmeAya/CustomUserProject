from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from .models import CustomUser


def registrationView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return False
        user = CustomUser(email=email)
        user.set_password(password1)
        user.save()
        return redirect('')

    else:
        context = {'form': CustomUserCreationForm()}
        return render(request, 'registration_page.html', context)
