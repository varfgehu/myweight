# Generated by Django 2.0.3 on 2020-06-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0017_auto_20200626_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='intake',
            name='user',
            field=models.CharField(default='default', max_length=16),
        ),
        migrations.AlterField(
            model_name='intake',
            name='meal_type',
            field=models.CharField(choices=[('BREAKFAST', 'breakfast'), ('LUNCH', 'lunch'), ('DINNER', 'dinner'), ('SNACK SIZE', 'snack1'), ('SNACK SIZE', 'snack2'), ('EXTRA', 'extra')], default='1', max_length=16),
        ),
    ]
