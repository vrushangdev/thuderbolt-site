from django.contrib import admin
from .models import  Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','number')
    list_display_links = ('name', 'email','number',)
    list_filter = ('name', 'email',)
    search_fields = ('name', 'email', 'number','message',)
    list_per_page = 25

admin.site.register(Contact,ContactAdmin)