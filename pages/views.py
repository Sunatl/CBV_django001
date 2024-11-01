from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from .models import *
from django.http import HttpResponse
from django.template import loader

class VakansiListView(ListView):
    model = Vakansi
    template_name = 'list_vakan.html'
    
class VakansiDetailView(DetailView):
    model = Vakansi
    template_name = 'detail_vakan.html'
    
class VakansiCreateView(CreateView):
    model = Vakansi
    template_name = 'create_vakan.html'
    fields = ['title','description', 'price','category','image']
    success_url = reverse_lazy('list_vakan') 
    
    
class VakansiUpdateView(UpdateView):
    model = Vakansi
    template_name = 'update_vakan.html'
    fields = ['title','description', 'price','category','image']
    success_url = reverse_lazy('list_vakan') 
    
    
class VakansiDeleteView(DeleteView):
    model = Vakansi
    template_name = 'delete_vakan.html'
    success_url = reverse_lazy('list_vakan') 
    
    
def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())



# Category
class CategoryListView(ListView):
    model = Category
    template_name = 'list_cotegoty.html'
    
class CategoryDetailView(DetailView):
    model = Category
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["vakansi"] = Vakansi.objects.filter(category = self.kwargs['pk'])
        return context
    template_name = 'detail_category.html'
    context_object_name = "category"
    
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'create_cotegory.html'
    fields = ['name']
    success_url = reverse_lazy('list_category') 
    
    
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'update_category.html'
    fields = ['name']
    success_url = reverse_lazy('list_category') 
    
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('list_category') 
    
    
    
    
# Application

class ApplicationListView(ListView):
    model = Application
    template_name = 'list_app.html'
    
class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'detail_app.html'
    
class ApplicationCreateView(CreateView):
    model = Application
    template_name = 'create_app.html'
    fields = ['vakansi','applicant_name','email','phone_number','resume']
    success_url = reverse_lazy('list_app') 
    
    
class ApplicationUpdateView(UpdateView):
    model = Application
    template_name = 'update_app.html'
    fields = ['vakansi','applicant_name','email','phone_number','resume']
    success_url = reverse_lazy('list_app') 
    
    
class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'delete_app.html'
    success_url = reverse_lazy('list_app') 