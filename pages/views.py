from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Page

# Create your views here.
def page_view(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, "pages/page.html", {"page":page})