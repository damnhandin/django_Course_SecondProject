# Generated by Django 5.0.2 on 2024-03-03 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_person_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person1', 'verbose_name_plural': 'Persons'},
        ),
    ]