from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View,UpdateView, CreateView, DeleteView,View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.messages.views import SuccessMessageMixin
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.shortcuts import redirect


from events.forms import *
from events.models import *
# Create your views here.

class AuthMixin(LoginRequiredMixin):
    login_url = reverse_lazy('events:login')


class Login(TemplateView):
    template_name = "login.html"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            form = LoginForm()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                return render(request, self.template_name, {
                    'form': form, 'user': username, 'error': 'Incorrect username or password'})

class Logout(AuthMixin, View):
    def get(self, request):
        logout(self.request)
        return redirect('events:login')

##Mixins
class CreateMixin(AuthMixin, CreateView):
    def form_valid(self, form):
        creater = User.objects.get(username=self.request.user)
        form.instance.created_by = creater
        obj = form.save()
        return super(CreateMixin, self).form_valid(form)


class UpdateMixin(AuthMixin, UpdateView):
    def form_valid(self, form):
        prev_obj = self.get_object()
        obj = form.save()
        return super(UpdateMixin, self).form_valid(form)


##home
class HomePageView(AuthMixin,ListView):
    template_name = 'home/index.html'
    model = Event
    paginate_by = 8


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = 'home'
        return context

##event CRUD
class EventCreate(CreateMixin,PassRequestMixin, SuccessMessageMixin,):
    template_name = 'home/event_form.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = 'event_create'
        return context


class EventUpdate(UpdateMixin):
    template_name = 'home/event_form.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_name'] = 'event_update'
        return context