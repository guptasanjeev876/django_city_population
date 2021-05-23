from django.contrib import admin
from .models import Population, PatientTreatment, EventCategory, PhysicianSpeciality
from import_export.admin import ImportExportModelAdmin

@admin.register(Population)
class PopulationAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name_of_city', 'state_name']

@admin.register(PatientTreatment)
class PateintTreatAdmin(admin.ModelAdmin):
    list_display = ["id", "eventname", "physicianid"]

@admin.register(EventCategory)
class EventCatAdmin(admin.ModelAdmin):
    list_display = ["id", "eventname","category"]

@admin.register(PhysicianSpeciality)
class PhysicianAdmin(admin.ModelAdmin):
    list_display = ["id","physicianid", "speciality"]
