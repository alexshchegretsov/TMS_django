from django.db import models


class MusicBand(models.Model):
    name = models.CharField(max_length=50)
    foundation_year = models.IntegerField()
    genre = models.CharField(max_length=30)


    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=50)
    year_issue = models.IntegerField()
    band = models.ForeignKey(MusicBand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    duration = models.DurationField()
    band = models.ForeignKey(MusicBand, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name