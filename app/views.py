from django.shortcuts import render
from .models import Phonebook
from django.views.generic import ListView,CreateView

# Create your views here.

class MemberListview(ListView):
    model = Phonebook
    template_name = 'app/index.html'
    context_object_name = 'profiles'
    ordering = {'name'}

def get_queryset(self):
    query = self.request.GET.get('q')
    if query:
        return Phonebook.objects.filter(name__icontains=query)| Phonebook.objects.filter(male__icontains=query)
    else:
        return Phonebook.objects.all()

class MemberCreateView(CreateView):
    model = Phonebook
    fields = '__all__'