from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name
