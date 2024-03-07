from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Dweet, Profile
import csv 
from django.http import HttpResponse
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
    list_display = ("username", "first_name", "last_name", "email")
    list_filter = ["is_staff" ]

    actions = ['generate_csv_report']

    def generate_csv_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users_report.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['id','username', 'First Name','Last Name'])
        
        for user in queryset:
            writer.writerow([f'USR-00{user.id}', user.username, user.first_name, user.last_name])  # Replace with your model fields
        
        return response

    generate_csv_report.short_description = "Generate CSV Report"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

admin.site.register(Dweet)