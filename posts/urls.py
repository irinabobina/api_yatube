from django.urls import path, include
#from django.contrib import admin
#from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostsViewSet, PostViewSet

router = DefaultRouter()
router.register('api/v1/posts', PostsViewSet)
router.register('api/v1/posts/{post_id}', PostViewSet)
#router.register('api/v1/api-token-auth/')

urlpatterns = [

    router.urls

]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]

