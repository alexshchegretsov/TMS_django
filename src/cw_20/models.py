from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=200,null=False)
    last_name = models.CharField(max_length=200, null=False)
    profession = models.CharField(max_length=200, null=True)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


