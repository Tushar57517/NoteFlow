from django.shortcuts import render
from pages.models import Page

# Create your views here.
def dashboard_view(request):
    pages = Page.objects.all()
    return render(request, 'dashboard/dashboard.html', {'pages':pages})