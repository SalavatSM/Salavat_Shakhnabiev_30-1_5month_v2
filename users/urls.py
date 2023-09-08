from users import views
from django.urls import path
# from .views import confirm_user

urlpatterns = [
    path('authorization/', views.authorization_api_view),
    path('registration/', views.registration_api_view),
    path('confirm/', views.confirm_user)
]
