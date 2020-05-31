from django.urls import path, include
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from gram.views import PostLikeToggle, PostLikeAPIToggle

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('post/<id>', views.post_comment, name='comment'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    path('like', views.like_post, name='like_post'),
    path('search/', views.search_profile, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)