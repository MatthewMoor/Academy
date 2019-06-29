from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.candidate_resume, name='reg-member'),
    path('test', views.test_save, name='test'),
    path('Jedis/', views.jedis_list, name='JedisList'),
    path('JediDetail/', views.jedi_from, name='Djedi'),
    path('SeeTest/<int:candidate_id>/', views.see_test, name='supervise'),
]