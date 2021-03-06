# Generated by Django 2.0.3 on 2020-06-26 18:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0011_auto_20200626_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.date.today, help_text='date of the meal')),
                ('meal_type', models.CharField(max_length=16)),
                ('foods', models.ManyToManyField(blank=True, related_name='intakes', to='nutrition.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carb', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calorie', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='nutritions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrition', to='nutrition.Nutrition'),
        ),
    ]
