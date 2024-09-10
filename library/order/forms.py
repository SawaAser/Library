from django import forms

from authentication.models import CustomUser
from book.models import Book
from .models import Order


class OrderCreateForm(forms.Form):
    plated_end_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Plated End Date')


class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'end_at': forms.DateInput(attrs={'type': 'date'}),
            'plated_end_at': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderEditForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['book'].widget.choices = [
                (book.id, book.name) for book in Book.objects.all()
            ]
            self.fields['book'].initial = self.instance.book.id
            self.fields['user'].widget.choices = [
                (user.id, f"{user.first_name} {user.last_name}") for user in CustomUser.objects.all()
            ]
            self.fields['user'].initial = self.instance.user.id
