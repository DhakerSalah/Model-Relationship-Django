from pyexpat import model
from django.db import models

# Create your models here.

class Paradigm(models.Model):
    paradigm_name = models.CharField(max_length=20)

    def __str__(self):
        return self.paradigm_name

        

class Language(models.Model):
    language_name = models.CharField(max_length=20)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.language_name

        

class Programmer(models.Model):
    programmer_name = models.CharField(max_length=30)
    langages = models.ManyToManyField(Language)

    def __str__(self):
        return self.programmer_name
