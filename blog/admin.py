from django.contrib import admin

from .models import CategoryArticles, BlogArticles


admin.site.register(CategoryArticles)
admin.site.register(BlogArticles)

