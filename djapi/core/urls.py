from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, FeedBackView, RegisterView, ProfileView, CommentView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path("feedback/", FeedBackView.as_view()),
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("comments/", CommentView.as_view()),
    path("comments/<slug:post_slug>/", CommentView.as_view())
]
