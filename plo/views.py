from django.views.generic import ListView,CreateView, View
from .models import customer
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .forms import UserForm

class IndexView(ListView):
    template_name= 'plo/index.html'
    context_object_name = 'dep_list'

    def get_queryset(self):
        return  customer.objects.all()


class SaveData(CreateView):
    model = customer
    fields = ['user_name','password','email']
    success_url = reverse_lazy('plo:index')

class LoginData(CreateView):
    model = customer
    fields = ['user_name','password',]
    success_url = reverse_lazy('plo:logined')

class UserFormView(View):
    form_class = UserForm
    template_name = 'plo/customer_login.html'

class About(View):
    form_class = UserForm
    template_name = 'plo/about1.html'

class LoginDone(View):
    form_class = UserForm
    template_name = 'plo/logined.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('plo:logined')


            return render(request, self.template_name, {'form': form})

