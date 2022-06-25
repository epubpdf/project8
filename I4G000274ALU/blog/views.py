from audioop import reverse
from dataclasses import field
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpRequest
 
from . models import Post

# Create your views here.
def PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    success_url = "post_list.html"

def PostCreateView(CreateView):
    model = Post
    field = "__all__"
    template_name = "post_detail.html"
    success_url = "post_detail.html"

def PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    success_url = "post_detail.html"

def PostUpdateView(UpdateView):
    model = Post
    field = "__all__"
    template_name = "post_form.html"
    success_url = "post_form.html"

def PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "post_confirm.html"
    success_url = "post_confirm.html"