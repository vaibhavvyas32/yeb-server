from django.contrib import admin

from yebapp.forms import MarksForm
from .model import UserDetail
# Register your models here.


@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('u_key', 'p_name', 'p_email', 'p_phone', 'school')
    exclude = ['marks']
    form = MarksForm
    search_fields = ('p_name', 'p_email')


