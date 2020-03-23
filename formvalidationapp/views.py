from django.shortcuts import render
from django.http.response import HttpResponse


from .forms import registrationform
from .models import registrationdata


def reg_form(request):
    form = registrationform(request.POST)
    context = {'form': form}
    if form.is_valid():
        print(form.cleaned_data)
        firstname = form.cleaned_data.get('firstname')
        lastname = form.cleaned_data.get('lastname')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        mobile = form.cleaned_data.get('mobile')
        data = registrationdata(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email,
            password1=password1,
            password2=password2,
            mobile=mobile
        )
        data.save()
    return render(request, 'feedback.html', context)
