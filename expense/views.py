from django.shortcuts import render

from django.views.generic.list import ListView
from expense.models import Reports

class ReportsList(ListView):
    model = Reports
    context_object_name = 'reports'
