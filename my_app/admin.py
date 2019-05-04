from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_editable = ('info',) # to be able to edit in the same page
    list_per_page = 10  # for pagination
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')



admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)