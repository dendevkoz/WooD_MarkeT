from django.db import models

class CategoryArticles(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class BlogArticles(models.Model):
    articles_name = models.CharField(max_length=100)
    articles_text = models.TextField()
    articles_author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    product_category = models.ForeignKey(CategoryArticles, on_delete=models.SET_NULL, null=True, blank=True)
    upload = models.ImageField(upload_to='uploads/', null=True, blank=True)
    def __str__(self):
        return self.articles_name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

