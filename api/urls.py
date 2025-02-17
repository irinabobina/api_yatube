from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import APIPostViewSet, APICommentViewSet


router = DefaultRouter()
router.register('posts', APIPostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', APICommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
