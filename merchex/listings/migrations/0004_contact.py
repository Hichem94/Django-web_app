# Generated by Django 5.1 on 2024-08-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_rename_linsting_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=100)),
            ],
        ),
    ]
