from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_page, name="create-page"),
    path('<str:pk>/', views.page_view, name="page-view"),
]
