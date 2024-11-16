from django.contrib import admin
from .models import GD,StdGD
from .forms import MarksForm

# Register your models here.

@admin.register(GD)
class GDAdmin(admin.ModelAdmin):
    list_display = ('gd_id', 'date', 'time', 'link')

@admin.register(StdGD)
class StdGDAdmin(admin.ModelAdmin):
    list_display = ('gd_id', 'student_id', 'marks')
    form = MarksForm
    exclude = ['marks']

