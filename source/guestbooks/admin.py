from django.contrib import admin
from guestbooks.models import Guest_books

@admin.register(Guest_books)
class Guest_booksAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'email', 'description', 'start_date', 'end_date']
    list_display_links = ['id', 'status', 'name', 'email']
    list_filter = ['name']
    search_fields = ['id', 'status', 'name']
    fields = ['status', 'name', 'email', 'description', 'start_date', 'end_date']
    readonly_fields = ['start_date', 'end_date']