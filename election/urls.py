from django.urls import path

from .views import ElectionList, ElectionDetail
from . import views

app_name = 'election'

urlpatterns = [
    path('', ElectionList.as_view(), name='election-list'),
    path('<int:pk>/', ElectionDetail.as_view(), name='election-detail'),
    path('<int:pk>/vote', views.vote, name='vote'),
    path('contact/', views.contact_view, name='contact'),
    path('about_us/', views.about_us_view, name='about_us_view')
]
