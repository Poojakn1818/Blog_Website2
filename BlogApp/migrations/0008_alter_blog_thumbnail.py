# Generated by Django 4.2.4 on 2024-07-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='b_img'),
        ),
    ]
