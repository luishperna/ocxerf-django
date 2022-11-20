# Generated by Django 4.1.3 on 2022-11-17 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=35)),
                ('data_de_nascimento', models.DateField()),
                ('senha', models.CharField(blank=True, max_length=8)),
            ],
        ),
    ]
