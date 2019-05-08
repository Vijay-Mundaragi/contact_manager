from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('detail/<int:pk>/', views.ContactDetailView.as_view(), name="detail"),
    path('search', views.search, name='search'),
]