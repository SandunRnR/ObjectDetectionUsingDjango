from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),

    path('object-create/', views.CreateObject, name='object-create'),
    path('get-all-objects/', views.GetAllObjects, name='get-all-objects'),
    path('get-object-by-id/<int:id>/', views.GetObjectById, name='get-object-by-id'),


]
