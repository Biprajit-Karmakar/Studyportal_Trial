from django.shortcuts import render, redirect
from .models import Notes, Homework
from . forms import NoteForm, HomeworkForm

from django.views.generic.detail import DetailView
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "dashboard/home.html")

def notes(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            notes = Notes(user= request.user, title= request.POST['title'], description= request.POST['description'])
            notes.save()
        messages.success(request,f"Notes Added from {request.user.username} SUCCESSFULLY!")
    else:
            form = NoteForm()
    
    notes = Notes.objects.filter(user = request.user)
    context = {'notes': notes,'form':form}
    return render(request, "dashboard/notes.html", context)


def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')



class NotesDetail(DetailView):
    model = Notes
    context_object_name = 'note'
    # genarally it has a default html template name but we can change it by using template_name attrebute
    template_name = 'dashboard/notes_detail.html'


def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == on:
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished

            )
            homeworks.save()
            messages.success(request, f'Homework Added from {request.user.username}!!')
    else:
            form = HomeworkForm()
    form = HomeworkForm()
    homework = Homework.objects.filter(user = request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {'homeworks':homework, 'homeworks_done':homework_done, 'form':form}
    return render(request,"dashboard/homework.html", context)


def update_homework(request, pk= None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished= False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')


def delete_homework(request, pk= None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')
