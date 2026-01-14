from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Page
from .forms import PageForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def page_view(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, "pages/page.html", {"page":page})

@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.owner = request.user
            page.save()
            return redirect('page-view', pk=page.id)
    else:
        form = PageForm()
    return render(request, 'pages/create_page.html', {'form':form})