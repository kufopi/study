from django.shortcuts import render, redirect
from .forms import ConasRegForm, CourseRegForm
from .models import ConasReg, CourseReg
from django.contrib import messages


# Create your views here.
def camas(request):
    word = 'CAMAS'
    form = CourseRegForm()
    if request.method == 'POST':
        form = CourseRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yay!! registration complete')
            return redirect('home')
        else:
            messages.error(request, 'Opps! Something smells fishy!!! during registration')
    context ={'form':form,'word':word}
    return render(request, 'course/camasform.html', context)



def conas(request):
    form = ConasRegForm()
    word = 'CONAS'
    if request.method == 'POST':
        form = ConasRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Yay!! registration complete')
            return redirect('home')
        else:
            messages.error(request, 'Opps! Something smells fishy!!! during registration')
    context ={'form':form, 'word':word}
    return render(request, 'course/camasform.html', context)