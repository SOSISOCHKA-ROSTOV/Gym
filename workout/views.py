from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .utils import*

# Create your views here.
def index(request):

    d = datetime.datetime.now()
    w = Lite.objects.all()
    day_user = d.day
    buy=0

    if(request.user.is_authenticated):
      if (request.user.last_name == 'workout_litework'):
        w = Lite.objects.all()
      if (request.user.last_name == 'workout_medium'):
        w = Medium.objects.all()
      for i in w:
          if (i.id == day_user):
              buy = i
      if (request.user.last_name == ''):
        request.user.last_name = 'none'
        buy=''


    return render(request, "workout/index.html", {'buy': buy})

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'workout/register.html'
    success_url = reverse_lazy('login')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')



class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'workout/login.html'
    #success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')



def logout_user(request):
    logout(request)
    return redirect('login')

def person_account(request):
    request.user.last_name = request.POST.get("title","Undefined")
    request.user.save()
    return render(request, "workout/personal account.html")
