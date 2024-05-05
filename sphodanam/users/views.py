from django.shortcuts import render, redirect
from notes.models import Semester, Subjects
from django.contrib.auth import authenticate,login,logout
def index_page(request):
    sem = Semester.objects.all()

    if request.method == 'POST':
        semester = request.POST.get('semester')
        return redirect('index2',pk=semester)  # Redirect to 'index2' URL pattern if the request method is POST

    return render(request, 'index.html', {'sem': sem})

def index_two(request,pk):
    subject=Subjects.objects.filter(sem=pk)
    if request.method == 'POST':
        subject_selected=request.POST.get('subject')
        return redirect('result',sub=subject_selected)
    return render(request, '2.html',{'sub':subject})

def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request,'login.html')
