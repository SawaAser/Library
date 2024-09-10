from django import forms
from author.models import Author
from .models import Book, Genre


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        required=False,
    )

    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'image', 'authors', 'genres', 'publication_year', 'date_of_issue']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 80}),
            'publication_year': forms.NumberInput(attrs={'type': 'number'}),
            'date_of_issue': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
        labels = {
            'name': 'Book Title',
            'description': 'Description',
            'count': 'Count',
            'image': 'Cover Image',
            'authors': 'Authors',
            'genres': 'Genres',
            'publication_year': 'Publication Year',
            'date_of_issue': 'Date of Issue',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['authors'].queryset = Author.objects.all()
        self.fields['authors'].widget.choices = [(author.id, author.surname + " " + author.name) for author in
                                                 Author.objects.all()]


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
