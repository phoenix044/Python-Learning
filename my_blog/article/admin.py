from django.contrib import admin

from .models import ArticlePost
from .models import ArticleColumn
# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)
