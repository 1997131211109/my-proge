
from .views import SignUpView
from django.urls import path
from .views import profile

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
]