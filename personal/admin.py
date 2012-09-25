from django.contrib import admin
from django import forms
from personal.models import Personal, NameProf, WeekendWork, PeopleToWork 

class PeopleToWorkInline(admin.TabularInline):
    model = PeopleToWork
    extra = 1

class WeekendWorkAdmin(admin.ModelAdmin):
    inlines = (PeopleToWorkInline,)

class PersonalAdmin(admin.ModelAdmin):
    inlines = (PeopleToWorkInline,)

admin.site.register(Personal,PersonalAdmin)
admin.site.register(NameProf)
admin.site.register(WeekendWork,WeekendWorkAdmin)
admin.site.register(PeopleToWork)