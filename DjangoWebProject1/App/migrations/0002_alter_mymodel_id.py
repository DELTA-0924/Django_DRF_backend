# Generated by Django 4.2.7 on 2023-11-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
