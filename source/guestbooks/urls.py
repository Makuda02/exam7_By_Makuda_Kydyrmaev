from django.urls import path
from guestbooks.views import index_view

urlpatterns = [
    path('', index_view)
]