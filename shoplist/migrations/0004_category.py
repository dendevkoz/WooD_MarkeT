# Generated by Django 4.2.2 on 2023-08-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0003_alter_shoplistproduct_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
            },
        ),
    ]
