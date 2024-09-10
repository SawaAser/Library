from django.urls import path
from . import views


app_name = 'author'

urlpatterns = [
    path('all_authors/', views.all_authors, name='list_authors'),
    path('dell_authors/<int:id_author>/', views.dell_authors, name='dell_authors'),
    path('edit_author/<int:id_author>/', views.AuthorEditView.as_view(), name='edit_author'),
    path('create/', views.AuthorCreateView.as_view(), name='create_author'),
]

