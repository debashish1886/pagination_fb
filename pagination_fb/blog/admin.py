from django.contrib import admin

from .models import Post

admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','tittle','desc','publish_date']

