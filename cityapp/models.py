from django.db import models

# Create your models here.
class Population(models.Model):
    name_of_city = models.CharField(max_length = 100)
    state_code = models.IntegerField(default = 0)
    state_name = models.CharField(max_length = 100)
    dist_code = models.IntegerField()
    population_total = models.IntegerField()
    population_male = models.IntegerField()
    population_female = models.IntegerField()
    population_total_0_6 = models.IntegerField()
    population_male_0_6 = models.IntegerField()
    population_female_0_6 = models.IntegerField()
    literates_total = models.IntegerField()
    literates_male = models.IntegerField()
    literates_female = models.IntegerField()
    sex_ratio = models.IntegerField()
    child_sex_ratio = models.IntegerField()
    effective_literacy_rate_total = models.IntegerField()
    effective_literacy_rate_male = models.IntegerField()
    effective_literacy_rate_female = models.IntegerField()
    location = models.CharField(max_length=100)
    total_graduates = models.IntegerField()
    male_graduates = models.IntegerField()
    female_graduates = models.IntegerField()

class PatientTreatment(models.Model):
    eventname = models.CharField(max_length=100)
    physicianid = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.eventname, self.physicianid)

class EventCategory(models.Model):
    eventname = models.ForeignKey(PatientTreatment, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.eventname)

class PhysicianSpeciality(models.Model):
    physicianid = models.ForeignKey(PatientTreatment, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.physicianid)






