from django.contrib import admin
from guestbooks.models import Guest_books

@admin.register(Guest_books)
class Guest_booksAdmin(admin.ModelAdmin):
    pass