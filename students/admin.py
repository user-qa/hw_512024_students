from django.contrib import admin
from students.models import StudentModel

@admin.register(StudentModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'dob', 'gender','created_at']
    search_fields = ['first_name', 'last_name', 'dob', 'gender','created_at']
    list_filter = ['first_name']