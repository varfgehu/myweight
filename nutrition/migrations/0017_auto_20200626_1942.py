# Generated by Django 2.0.3 on 2020-06-26 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0016_auto_20200626_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portion',
            old_name='nutritions',
            new_name='foods',
        ),
    ]
