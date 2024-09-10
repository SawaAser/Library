from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import AuthorForm, EditAuthorForm
from .models import Author


class AuthorCreateView(UserPassesTestMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create_author.html'
    success_url = reverse_lazy('author:list_authors')

    def test_func(self):
        return self.request.user.is_staff


class AuthorEditView(UserPassesTestMixin, UpdateView):
    model = Author
    form_class = EditAuthorForm
    template_name = 'author/edit_author.html'
    success_url = reverse_lazy('author:list_authors')

    def test_func(self):
        return self.request.user.is_staff

    def get_object(self, queryset=None):
        author_id = self.kwargs['id_author']
        return get_object_or_404(self.model, id=author_id)


@login_required
@user_passes_test(lambda u: u.is_staff)
def all_authors(request):
    authors = Author.objects.all()
    title = 'All Authors'
    return render(request=request, template_name='author/all_authors.html', context={
        'title': title,
        'authors': authors,
    })


@login_required
@user_passes_test(lambda u: u.is_staff)
def dell_authors(request, id_author):
    authors = Author.objects.all()
    title = 'All Authors'

    author = Author.get_by_id(id_author)
    if author.books.count() == 0:
        Author.delete_by_id(id_author)
        return render(request=request, template_name='author/all_authors.html', context={
            'title': title,
            'authors': authors,
        })
    else:
        return render(request=request, template_name='author/all_authors.html', context={
            'title': title,
            'authors': authors,
        })
