# Generated by Django 4.0.3 on 2022-03-25 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='dete_of_death',
            new_name='date_of_death',
        ),
    ]
