# Generated by Django 4.2.4 on 2023-10-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homes', '0006_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='discrption',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]