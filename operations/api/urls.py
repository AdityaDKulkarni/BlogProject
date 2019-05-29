from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from operations.views import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, base_name='post')
router.register(r'category', CategoryViewSet, base_name='category')
urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
