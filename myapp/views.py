from django.shortcuts import render, get_object_or_404, redirect
from .models import MonitoringStation, EquipmentType
from django import forms


# Create your views here.
def myapp(request):
    return render(request, 'myapp.html')


def monitoring_stations_view(request):
    monitoring_stations = MonitoringStation.objects.all()
    return render(request, 'stations/monitoring_stations.html', {'object_list': monitoring_stations})


def add_monitoring_station(request):
    if request.method == 'POST':
        form = MonitoringStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_stations')
    else:
        form = MonitoringStationForm()
    return render(request, 'stations/add_monitoring_station.html', {'form': form})


def edit_monitoring_station(request, pk):
    station = get_object_or_404(MonitoringStation, pk=pk)
    if request.method == 'POST':
        form = MonitoringStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('monitoring_stations')
    else:
        form = MonitoringStationForm(instance=station)
    return render(request, 'stations/edit_monitoring_station.html', {'form': form})


def delete_monitoring_station(request, pk):
    station = get_object_or_404(MonitoringStation, pk=pk)
    if request.method == 'POST':
        station.delete()
        return redirect('monitoring_stations')
    return render(request, 'stations/delete_monitoring_station.html', {'station': station})


# forms
class MonitoringStationForm(forms.ModelForm):
    class Meta:
        model = MonitoringStation
        fields = '__all__'


class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = EquipmentType
        exclude = ['last_update']


def equipment_type_view(request):
    equipment_type = EquipmentType.objects.all()
    return render(request, 'equipment/equipment_type.html',  {'object_list': equipment_type})


def edit_equipment_type(request, pk):
    equipment = get_object_or_404(EquipmentType, pk=pk)
    if request.method == 'POST':
        form = EquipmentTypeForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_type')
    else:
        form = EquipmentTypeForm(instance=equipment)
    return render(request, 'equipment/edit_equipment_type.html', {'form': form})


def delete_equipment_type(request, pk):
    station = get_object_or_404(EquipmentType, pk=pk)
    if request.method == 'POST':
        station.delete()
        return redirect('equipment_type')
    return render(request, 'equipment/delete_equipment_type.html', {'station': station})


def add_equipment_type(request):
    if request.method == 'POST':
        form = EquipmentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_type')
    else:
        form = EquipmentTypeForm()
    return render(request, 'equipment/add_equipment_type.html', {'form': form})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)
