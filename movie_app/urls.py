from movie_app import views
from django.urls import path

urlpatterns = [
    # path('', views.director_list_api_view),
    # path('<int:director_id>/', views.director_detail_api_view),
    #
    # path('', views.movie_list_api_view),
    # path('<int:movie_id>/', views.movie_detail_api_view),
    #
    # path('', views.review_list_api_view),
    # path('<int:review_id>/', views.review_detail_api_view),

    path('directors/', views.DirectorViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('directors/<int:id>/', views.DirectorViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),

    path('movies/', views.MovieViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('movies/<int:id>/', views.MovieViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),

    path('reviews/', views.ReviewViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('reviews/<int:id>/', views.ReviewViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
]



