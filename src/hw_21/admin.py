from django.contrib import admin
from .models import (
    MusicBand,
    Album,
    Track,
)

admin.site.register(MusicBand)
admin.site.register(Album)
admin.site.register(Track)
