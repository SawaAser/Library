# Generated by Django 4.1 on 2024-08-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_publication_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_of_issue',
            field=models.DateField(blank=True, null=True),
        ),
    ]
