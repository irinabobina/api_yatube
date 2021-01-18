from django.urls import path 
from django.urls import include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


from .views import APIPostViewSet, APICommentViewSet


router = DefaultRouter()
router.register('posts', APIPostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', APICommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls))
]

urlpatterns = [
    #path('v1/', include(router.urls)),
    #path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),  
]