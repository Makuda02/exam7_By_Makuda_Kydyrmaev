from django.shortcuts import render, redirect, get_object_or_404
from .models import Guest_books
from .form import Guest_booksForm

def index_view(request):
    articles = Guest_books.objects.all()
    return render(request, 'index.html', {'articles':  articles})

def article_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Guest_books, pk=pk)
    return render(request, 'article_view.html', {'article': article})


def article_create_view(request):
    if request.method == "GET":
        form = Guest_booksForm()
        return render(request,  'article_create.html', {'form': form})
    elif request.method == "POST":
        form = Guest_booksForm(data=request.POST)

        if form.is_valid():
            article = Guest_books.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                description=form.cleaned_data.get('description'),

            )
            return redirect('index')
        else:
            return render(request, 'article_create.html', {'form': form})


def article_update_view(request, pk):
    article = get_object_or_404(Guest_books, pk=pk)
    if request.method == "GET":
        form = Guest_booksForm(initial={
            'name': article.name,
            'email': article.email,
            'description': article.description,
        })
        return render(request, 'article_update.html', {'form': form})
    elif request.method == "POST":

        form = Guest_booksForm(data=request.POST)
        if form.is_valid():
            article.name = form.cleaned_data.get('name')
            article.email = form.cleaned_data.get('email')
            article.description = form.cleaned_data.get('description')
            article.end_date = form.cleaned_data.get('end_date')
            article.save()
            return redirect('index')
        else:
            return render(request, 'article_update.html', {'form': form})


def article_delete_view(request, pk):
    article = get_object_or_404(Guest_books, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')
