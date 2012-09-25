from django.contrib import admin
from django import forms
from finances.personal import Personal, NameProf, WeekendWork, PeopleToWork 

admin.site.register(Personal)
admin.site.register(NameProf)
admin.site.register(WeekendWork)
admin.site.register(PeopleToWork)