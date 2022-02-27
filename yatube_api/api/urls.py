from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentsViewSet

router = DefaultRouter()

router.register(r"groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentsViewSet, basename="comments"
)
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
]
