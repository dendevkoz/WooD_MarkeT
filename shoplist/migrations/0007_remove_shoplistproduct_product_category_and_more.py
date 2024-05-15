# Generated by Django 4.2.2 on 2023-08-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0006_remove_shoplistproduct_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoplistproduct',
            name='product_category',
        ),
        migrations.AddField(
            model_name='shoplistproduct',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shoplist.category'),
        ),
    ]
