from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('hello-viewsets', views.HelloViewSet, base_name='hello-viewset')
router.register('feed', views.UserProfileFeedViewSet)



urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]