from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import StudentProfile


class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'stud_list'

    def get_queryset(self):
        return StudentProfile.objects.all()

class DetailView(generic.DetailView):
    pass

class saveData(CreateView):
    model = StudentProfile
    fields = ['fname','lname','email','address','password','mobile']

class editData(UpdateView):
    model = StudentProfile
    fields = ['fname','lname','email','address','password','mobile']

class deleteData(DeleteView):
    model = StudentProfile
    success_url = reverse_lazy('students:index')


















