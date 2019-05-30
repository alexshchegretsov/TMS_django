from django.contrib import admin
from .models import ContactInfo, Person, Group

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(ContactInfo)
# Register your models here.
