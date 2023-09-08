from django.contrib import admin
from django.urls import path, include

from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('movie_app.urls')),
    # path('api/v1/directors/', views.director_detail_api_view),

    path('api/v1/', include('movie_app.urls')),
    # path('api/v1/movies/<int:movie_id>/', views.movie_detail_api_view),

    path('api/v1/', include('movie_app.urls')),
    # path('api/v1/reviews/<int:review_id>/', views.review_detail_api_view),

    path('api/v1/users/', include('users.urls'))
]
