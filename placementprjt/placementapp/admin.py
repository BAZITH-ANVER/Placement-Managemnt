from django.contrib import admin
from .models import Course,District,State,Qualification,Trainer,Batch

# Register your models here.

class TrainerAdmin(admin.ModelAdmin):
    filter_horizontal=('trainer',)
admin.site.register(Course)
admin.site.register(District)
admin.site.register(State)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Qualification)
admin.site.register(Batch)