# Generated by Django 4.2.7 on 2023-12-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_apartaments_managers_delete_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartaments',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='managers',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
