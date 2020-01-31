from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.db.models import Sum

from .models import Widget
from .forms import WidgetForm

def index(request):
  widgets = Widget.objects.all()
  widget_form = WidgetForm()
  total = Widget.objects.aggregate(Sum('quantity')) 
  return render(request, 'index.html', {
    'widgets': widgets,
    'widget_form': widget_form,
    'total': total
  })

def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('index')

def delete_widget(request, widget_id):
  widget = Widget.objects.get(id=widget_id)
  widget.delete()
  return redirect('index')
