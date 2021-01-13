from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]

