from django.shortcuts import render
from .models import Guest_books, status_choices
from django.http import HttpResponseRedirect
def index_view(request):
    guests = Guest_books.objects.all()
    return render(request, 'index.html', {'guests': guests})


