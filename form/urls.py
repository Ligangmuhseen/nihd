# urls.py

from django.urls import path
from . import views
from .views import CsrfTokenView
from .views import UsersView, UsersDetailView


urlpatterns = [
    path('api/submit-form/', views.submit_form, name='submit-form'),
    path('api/superuser/', views.superuser_login, name='superuser_login'),
    path('api/get_csrf_token/', CsrfTokenView.as_view(), name='get_csrf_token'),
    path('user/upload/', UsersView.as_view(), name='user-list'),
    path('user/upload/<int:pk>/', UsersDetailView.as_view(), name='user-detail'),
]





