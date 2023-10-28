from django.contrib import admin

# Register your models here.
from post.models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    search_fields = ["name", "role"]


@admin.register(Socialmedia)
class SocialmediaAdmin(admin.ModelAdmin):
    list_display = ("title", "url")
    search_fields = ["title"]
    list_filter = ["author"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]
    # list_filter = ["author"]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]
    # list_filter = ["author"]


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "author",
        "viewers",
        "created_at",
        "updated_at",
    )
    search_fields = ["title"]
    list_filter = ["author"]

    def save_model(self, request, obj, form, change):
        obj.viewers += 1
        obj.save()


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    search_fields = ["name", "email", "subject", "message"]
    list_filter = ["subscribe_at"]


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "url")
    search_fields = ["title"]
    list_filter = ["title"]
