from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import *

router = DefaultRouter()
router.register("author", AuthorModelViewSet)
router.register("socialmedia", SocialmediaModelViewSet)
router.register("category", CategoryModelViewSet)
router.register("tags", TagModelViewSet)
router.register("posts", PostModelViewSet)
router.register("contact", ContactViewSet)
router.register("advertising", AdvertisingModelViewSet)
router.register("partners", PartnerModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
