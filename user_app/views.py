from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect


def registrationView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        context = {'form': CustomUserCreationForm()}
        return render(request, 'registration_page.html', context)
