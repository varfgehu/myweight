# Generated by Django 2.0.3 on 2020-06-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0013_nutrition_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intake',
            name='foods',
            field=models.ManyToManyField(blank=True, related_name='intakes', to='nutrition.Nutrition'),
        ),
    ]
