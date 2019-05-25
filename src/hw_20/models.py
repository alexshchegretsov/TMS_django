from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    weight = models.IntegerField(null=False)
    owner_full_name = models.CharField(max_length=50)
    year_issue = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.brand.title()} {self.model}'
