from django.urls import path

from instagram.views import InstaUserLoginAPIView, InstaUserLoginView

urlpatterns = [
    path("api", InstaUserLoginAPIView.as_view(), name='login_api_view'),
    path("", InstaUserLoginView.as_view(), name='login_view'),

]
