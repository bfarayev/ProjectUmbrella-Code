from django.contrib import admin
from posts.models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('subject', 'is_public', 'data_posted')
    list_editable = ('is_public',)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

