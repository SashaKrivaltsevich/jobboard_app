from django.db import models


class Company(models.Model):
    name = models.CharField(unique=True, max_length=100)
    employees_number = models.PositiveIntegerField()


class Vacancy(models.Model):
    LEVELS = (
    ("JR","Junior"),
    ("Middle", "Middle")
    )

    level = models.CharField(choices=LEVELS, max_length=30)
    expirience = models.CharField(max_length=30)
    min_salary = models.PositiveIntegerField(null=True)
    max_salary = models.PositiveIntegerField(null=True)
    company = models.ForeignKey(
        to="Company",
        on_delete=models.CASCADE, 
        related_name="vacancies", 
        related_query_name="vacancy"
    )
    