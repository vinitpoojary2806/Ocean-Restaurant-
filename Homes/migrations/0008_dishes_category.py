# Generated by Django 4.2.4 on 2023-10-23 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homes', '0007_category_discrption'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Homes.category'),
            preserve_default=False,
        ),
    ]
