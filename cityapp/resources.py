from django.db.models.base import ModelState
from import_export import resources
from .models import Population

class Population(resources.ModelResource):
    class Meta:
        model = Population
        