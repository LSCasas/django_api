from django.db import models

# Create your models here.
class Owner(models.Model):
    """Owner object"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()


class Species(models.Model):
    """Pet species"""
    name = models.CharField(max_length=20)


class Pet(models.Model):
    """Pet object"""
    

    class Species(models.IntegerChoices):
        OTHERS = 0
        CAT = 1
        DOG = 2
        BIRD = 3

    name = models.CharField(max_length=256)
    owner = models.ForeignKey(Owner, related_name="pets", on_delete=models.CASCADE)
    age = models.IntegerField()
    spacies = models.CharField(Species, on_delete=models.PROTECT)
    record = models.ForeignKey('Record', related_name='pets', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

pet = Pet(species=Pet.Species.DOG)

class Record(modes.Model):
    """Medical Record object"""
    class Category(models.IntegerChoices):
        """Medical record category"""
        OTHER = 1
        BLOOD_PRESSURE = 2
        BLOOD_SUGGAR = 3
        BLOOD_GLUCOSE = 4
        BLOOD_OXYGEN = 5
        VACCINATION = 6

    category = models.IntegerField(choices=Category.choices)
    procedure = models.CharField(max_length=255)
    pet = models.ForeignKey(Pet, related_name="records", on_delete=models.CASCADE)
    date = models.DateField()