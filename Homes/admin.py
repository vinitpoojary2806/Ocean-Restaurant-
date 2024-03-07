from django.contrib import admin
from Homes.models import *
import csv 
from django.http import HttpResponse



# Register your models here.


#admin.site.register(ContactTable)

admin.site.register(Category)
# admin.site.register()

admin.site.register(Dishes)




class BookReport(admin.ModelAdmin):
    list_display = ("user", "name", "email", "date", "numberofpeople")
      
    actions = ['generate_csv_report']

       
    def generate_csv_report(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users_report.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['id','user', 'Name','Email', 'Date', 'Number Of People'])
        
        for user in queryset:
            writer.writerow([f'USR-00{user.id}', user.user, user.name, user.email, user.date, user.numberofpeople])  # Replace with your model fields
        
        return response

    generate_csv_report.short_description = "Generate CSV Report"

admin.site.register(BookTable, BookReport)