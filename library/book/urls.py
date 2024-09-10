from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('all-books/', views.show_all_books, name='all_books'),
    path('book/<int:id_book>/', views.show_one_book, name='single_book'),
    path('add_book', views.create_or_update_book, name='add_book'),
    path('edit/<int:book_id>/', views.create_or_update_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('all-genres/', views.show_all_genres, name='all_genres'),
    path('add_genre/', views.create_or_update_genre, name='add_genre'),
    path('edit_genre/<int:genre_id>/', views.create_or_update_genre, name='edit_genre'),
    path('delete_genre/<int:genre_id>/', views.delete_genre, name='delete_genre'),
]
