# Generated by Django 5.0.4 on 2024-04-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
