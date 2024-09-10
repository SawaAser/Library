from django import forms
from .models import Author
from book.models import Book


class AuthorForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        label='Books',
        required=False,
    )
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic', 'books']

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic',
            'books': 'Books'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()
        self.fields['books'].widget.choices = [(book.id, book.name) for book in
                                                 Book.objects.all()]


class EditAuthorForm(forms.ModelForm):
    books = forms.ModelMultipleChoiceField(
        queryset=Book.objects.all(),
        label='Books',
        required= False,
    )

    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic', 'books']

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic',
            'books': 'Books'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()
        self.fields['books'].widget.choices = [(book.id, book.name) for book in
                                               Book.objects.all()]
