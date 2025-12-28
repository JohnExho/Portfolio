from django.urls import path
from . import views
from .views import (
    HomeView,
    MoreInfoView, 
)
app_name = "main"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('more/', views.MoreInfoView.as_view(), name='more'),
]
 