from django.shortcuts import render

# Create your views here.
from post.models import *
from post.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    filter_backends = (SearchFilter,)
    search_fields = ("name", "role")


class SocialmediaModelViewSet(ModelViewSet):
    queryset = Socialmedia.objects.all()
    serializer_class = SocialmediaSerializers
    filter_backends = (SearchFilter,)
    search_fields = ("title", "url")


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorymediaSerializers
    filter_backends = (SearchFilter,)


class TagModelViewSet(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers
    filter_backends = (SearchFilter,)


class PostModelViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    filter_backends = (SearchFilter,)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    filter_backends = (SearchFilter,)


class PartnerModelViewSet(ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnerSerializers
    filter_backends = (SearchFilter,)


class AdvertisingModelViewSet(ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializers
    filter_backends = (SearchFilter,)
