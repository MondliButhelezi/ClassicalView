from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('monitoring_stations/', views.monitoring_stations_view, name='monitoring_stations'),
    path('monitoring_stations/add/', views.add_monitoring_station, name='add_monitoring_station'),
    path('monitoring_stations/<int:pk>/edit/', views.edit_monitoring_station, name='edit_monitoring_station'),
    path('monitoring_stations/<int:pk>/delete/', views.delete_monitoring_station, name='delete_monitoring_station'),

    path('equipment_type/', views.equipment_type_view, name='equipment_type'),
    path('equipment_type/add/', views.add_equipment_type, name='add_equipment_type'),
    path('equipment_type/<int:pk>/edit/', views.edit_equipment_type, name='edit_equipment_type'),
    path('equipment_type/<int:pk>/delete/', views.delete_equipment_type, name='delete_equipment_type'),


]

handler404 = 'myapp.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
