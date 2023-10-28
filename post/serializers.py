from rest_framework import serializers
from post.models import *


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "image", "role"]


class SocialmediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Socialmedia
        fields = ["title", "logo", "url"]


class CategorymediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "logo"]


class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ["title"]


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ["title", "image", "content", "viewers", "created_at", "updated_at"]


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "image", "subject", "message"]


class PartnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ["name", "logo", "url"]


class AdvertisingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = ["title", "content", "url"]
