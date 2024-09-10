from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from author.models import Author
from .forms import BookForm, GenreForm
from .models import Book, Genre


@login_required
def show_all_books(request):
    author_id = request.GET.get('author')
    genre_id = request.GET.get('genre')

    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()

    if author_id:
        books = books.filter(authors__id=author_id)
        genres = Genre.objects.filter(books__authors__id=author_id).distinct()

    if genre_id:
        books = books.filter(genres__id=genre_id)
        authors = Author.objects.filter(books__genres__id=genre_id).distinct()

    selected_author = author_id if author_id else None
    selected_genre = genre_id if genre_id else None

    return render(request, 'book/all_books.html', context={
        'title': 'All books',
        'books': books,
        'authors': authors,
        'genres': genres,
        'selected_author': selected_author,
        'selected_genre': selected_genre,
    })


@login_required
def show_one_book(request, id_book):
    book = Book.get_by_id(id_book)
    title = 'Description'
    return render(request=request, template_name='book/book.html', context={
        'title': title,
        'book': book,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def create_or_update_book(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, id=book_id)
        title = 'Edit book'
    else:
        book = None
        title = 'Add book'

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            authors = form.cleaned_data['authors']
            book.authors.set(authors)

            form.save_m2m()
            return redirect('books:single_book', book.id)
    else:
        form = BookForm(instance=book)
        if book:
            form.fields['authors'].initial = book.authors.all()

    return render(request, 'book/add_book.html', {
        'form': form,
        'title': title,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_book(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('books:all_books')


@login_required
@user_passes_test(lambda u: u.is_staff)
def show_all_genres(request):
    genres = Genre.get_all()
    title = 'All Genres'
    return render(request, 'book/all_genre.html', {
        'title': title,
        'genres': genres,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_genre(request, genre_id):
    if genre_id:
        genre = get_object_or_404(Genre, id=genre_id)
        genre.delete_by_id(genre_id)
        return redirect('books:all_genres')


@login_required
@user_passes_test(lambda u: u.is_staff)
def create_or_update_genre(request, genre_id=None):
    if genre_id:
        genre = get_object_or_404(Genre, id=genre_id)
        title = "Edit Genre"
    else:
        genre = None
        title = "Add Genre"

    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('book:all_genres')
    else:
        form = GenreForm(instance=genre)

    return render(request, 'book/genre_form.html', {'form': form, 'title': title})
