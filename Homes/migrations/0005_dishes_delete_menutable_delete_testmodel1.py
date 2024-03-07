# Generated by Django 4.2.4 on 2023-10-22 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homes', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('price', models.IntegerField(default=150)),
            ],
        ),
        migrations.DeleteModel(
            name='MenuTable',
        ),
        migrations.DeleteModel(
            name='TestModel1',
        ),
    ]