# Generated by Django 5.1.1 on 2024-09-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_reader_books_in_bag'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='books_in_bag',
            field=models.ManyToManyField(blank=True, through='api.RentalRecord', to='api.book'),
        ),
    ]
