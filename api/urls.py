from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),

    path('object-create/', views.create_object, name='object-create'),
    path('get-all-objects/', views.GetAllObjects, name='get-all-objects'),
    path('get-object-by-id/<int:id>/', views.GetObjectById, name='get-object-by-id'),
    path('delete-object-by-id/<int:object_id>/', views.delete_object_by_id, name='delete-object-by-id'),
    path('update-object-by-id/<int:object_id>/', views.update_object_by_id, name='update-object-by-id'),
]
