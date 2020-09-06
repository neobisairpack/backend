from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *


app_name = 'users'


urlpatterns = [
    path('users/', UserRetrieveUpdateAPIView.as_view(), name='users'),
    path('users/me/', CurrentUserView.as_view(), name='me'),
    path('users/update/', UserUpdateAPIView.as_view(), name='update_user'),
    path('users/registration/', RegistrationAPIView.as_view(), name='registration'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('users/password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('users/search/', UserListAPIView.as_view(), name='user-search'),
    path('rating/search/', RatingSearchListAPIView.as_view(), name='rating-search'),

    # email verification
    url(r'activate/(?P<uid64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]

