# Generated by Django 4.2.11 on 2024-05-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('consulting_section', models.CharField(max_length=20)),
                ('appoinment_fees', models.IntegerField()),
                ('persons', models.IntegerField()),
            ],
        ),
    ]
