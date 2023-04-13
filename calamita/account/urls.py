from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignUpView, logout_user


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', logout_user, name='logout')
]
