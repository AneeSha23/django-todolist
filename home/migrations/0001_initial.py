# Generated by Django 4.1.2 on 2022-12-17 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]