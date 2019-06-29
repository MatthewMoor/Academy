from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.candidate_resume, name='reg-member'),
    path('test', views.test_main, name='test'),
]