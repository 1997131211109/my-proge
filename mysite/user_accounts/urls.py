
from .views import SignUpView
from django.urls import path
from .views import profile
from . import views



urlpatterns = [
    path('profile/', profile, name='profile'),
    path('create-post/', views.create_post, name='create_post'),
    path('<slug:slug>/create-comment/', views.create_comment, name='create_comment'),
    path('signup/', SignUpView.as_view(), name='signup'),
]