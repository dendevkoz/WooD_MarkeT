from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ShoplistProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(default='Описание товара')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title_img = models.ImageField(upload_to='uploads/', null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
     




    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(ShoplistProduct, on_delete=models.CASCADE, related_name='images')


class Color(models.Model):
    new_color = models.CharField(max_length=30)
    add_color = models.ForeignKey(ShoplistProduct, on_delete=models.CASCADE, related_name='add_color')


class Size(models.Model):
    new_size = models.CharField(max_length=30)
    add_size = models.ForeignKey(ShoplistProduct, on_delete=models.CASCADE, related_name='add_size')





