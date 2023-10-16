from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Author, Contact, Comment


# admin.site.register(Post)
# admin.site.register(Author)
# admin.site.register(Contact)
# admin.site.register(Comment)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'author_image', 'preview')
    list_filter = ('name',)

    # """ admin panel uchun rasm chiqarish preview """

    def preview(self, obj):
        html_code = f"""<img src={obj.author_image.url} alt="No image" width="50" height="60">"""

        return format_html(html_code)


admin.site.register(Author, AuthorAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    list_filter = ('subject',)


# Register the AuthorAdmin class with the Author model
admin.site.register(Contact, ContactAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'image')
    list_filter = ('author', 'title')


# Register the AuthorAdmin class with the Author model
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post')
    list_filter = ('created_at',)


admin.site.register(Comment, CommentAdmin)
