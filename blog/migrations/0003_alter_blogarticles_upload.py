# Generated by Django 4.2.2 on 2023-07-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogarticles_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]