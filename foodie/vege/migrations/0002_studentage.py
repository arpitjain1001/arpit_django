# Generated by Django 4.2.1 on 2023-07-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_age', models.IntegerField(max_length=100)),
            ],
        ),
    ]
