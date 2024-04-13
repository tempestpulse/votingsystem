from django.urls import path

from .views import ElectionList, ElectionDetail, ElectionResult
from . import views

app_name = 'election'

urlpatterns = [
    path('', ElectionList.as_view(), name='election-list'),
    path('<int:pk>/', ElectionDetail.as_view(), name='election-detail'),
    path('<int:pk>/vote', views.vote, name='vote'),
    path('<int:pk>/result', ElectionResult.as_view(), name='election-result'),
    path('contact/', views.contact_view, name='contact'),
    path('about_us/', views.about_us_view, name='about_us_view'),
    path('profile/', views.profile_view, name="profile")
]
