from django.views.generic import ListView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from home.models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import DogForm, UpdateForm
from django.template import loader
from django.shortcuts import get_object_or_404

class HomePageView(ListView):
    model = Dog

def detail(request, dog_id):
    dog = Dog.objects.get(pk=dog_id)
    template = loader.get_template('home/dog_detail.html')
    context = {
        'dog': dog,
        'father': dog.father,
        'mother': dog.mother
    }
    return HttpResponse(template.render(context, request))


def like(request, dog_id):
    dog = Dog.objects.get(pk=dog_id)
    dog.like = dog.like + 1
    dog.save()
    return detail(request, dog_id)


class AddDogView(CreateView):
    form_class = DogForm
    template_name = "home/dog_form.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()

        return HttpResponseRedirect('/')






class EidtDogView(UpdateView):
    template_name = "home/dog_edit_form.html"
    form_class = UpdateForm
    model = Dog

    def get_object(self):
        obj = self.model.objects.get(pk=self.kwargs['pk'])
        return obj

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()

        return HttpResponseRedirect('/' + str(self.kwargs['pk']))

    



class DeleteDogView(DeleteView):
    model = Dog
    success_url = "/"


