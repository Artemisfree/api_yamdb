from django.urls import include, path
from rest_framework import routers

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet, \
    ReviewViewSet, CommentViewSet
from users.views import AdminViewSet


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='Reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='Comments'
)
router.register(r'titles', TitleViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('users.urls')),
    path('v1/users/', AdminViewSet),
]
