from django.urls import include, path
from rest_framework import routers

from api.views import ReviewViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='Reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+/comments',
    CommentViewSet,
    basename='Comments'
)

urlpatterns = [
    path('v1/', include(router.url))
]