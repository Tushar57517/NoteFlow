from django.shortcuts import render
from pages.models import Page
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
@login_required
def dashboard_view(request):
    current_hr = datetime.now().hour
    if 5 <= current_hr < 12:
        time_of_day = "morning"
    elif 12 <= current_hr < 17:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"
    pages = Page.objects.filter(owner=request.user)
    return render(request, 'dashboard/dashboard.html', {'pages':pages, 'time_of_day':time_of_day})