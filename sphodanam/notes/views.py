from django.shortcuts import render,redirect
from . models import Notes,Subjects,Semester
# Create your views here.
def result(request,sub):
    notes=Notes.objects.filter(subject=sub)
    return render(request,'result.html',{'notes':notes})
def add_one(request):
    user=request.user
    if user.is_authenticated:
        semesters=Semester.objects.all()
        if request.method == 'POST':
            sem=request.POST.get('semester')
            return redirect('addtwo',sem=sem)
        return render(request,'add1.html',{'sem':semesters})
    return redirect('index')
from django.shortcuts import render, redirect
from .models import Notes, Subjects, Semester

def add_two(request, sem):
    subjects = Subjects.objects.filter(sem=sem)
    if request.method == 'POST':
        name = request.POST.get('file_name')
        subject = request.POST.get('subject')
        file = request.FILES.get('file')  # Use request.FILES for file uploads
        note = Notes.objects.create(name=name, subject_id=subject, file=file)
        return redirect('result', sub=subject)  # Redirect to result page after successful upload
    return render(request, 'add2.html', {'sub': subjects})
