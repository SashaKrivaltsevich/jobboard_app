from django.db import models


class Vacancy(models.Model):
    level = models.ForeignKey(
        to="Level", 
        on_delete=models.CASCADE, 
        related_name="vacancy"
    )
    expirience = models.CharField(max_length=30)
    min_salary = models.PositiveIntegerField(null=True)
    max_salary = models.PositiveIntegerField(null=True)
    company = models.ForeignKey(
        to="Company",
        on_delete=models.CASCADE, 
        related_name="vacancies", 
        related_query_name="vacancy"
    )
    tags = models.ManyToManyField(
        to="Tag", 
        related_name="vacancies", 
        db_table="vacancies_tags"
    )
    name = models.CharField(max_length=100)
    attachment = models.FileField(upload_to="vacancy/attachments/", null=True)

    class Meta:
        db_table = "vacancies"