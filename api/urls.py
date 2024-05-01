from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),

    path('object-create/', views.CreateObject, name='object-create'),
]
