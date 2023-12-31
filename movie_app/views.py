from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorValidateSerializer,
                          MovieValidateSerializer, ReviewValidateSerializer)
from .models import Director, Movie, Review

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class DirectorViewSet(ModelViewSet):
    pagination_class = PageNumberPagination  # pagination
    queryset = Director.objects.all()    # List of data from DB
    serializer_class = DirectorSerializer  # class of serializer inherited by model serializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        # 1. Get data from validated data
        name = serializer.validated_data.get('name')

        # 2. Create object
        director = Director.objects.create(name=name)

        # 3. Return created object
        return Response(data=DirectorSerializer(director).data)


# class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer
#     lookup_field = 'id'


class MovieViewSet(ModelViewSet):
    pagination_class = PageNumberPagination  # pagination
    queryset = Movie.objects.all()    # List of data from DB
    serializer_class = MovieSerializer  # class of serializer inherited by model serializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        # 1. Get data from validated data
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        # rating = request.data.get('rating')

        # 2. Create object
        movie = Movie.objects.create(title=title, description=description, duration=duration,
                                     director_id=director_id)
        # movie.rating.set(rating)
        # movie.save()

        # 3. Return created object
        return Response(data=MovieSerializer(movie).data)


# class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     lookup_field = 'id'


class ReviewViewSet(ModelViewSet):
    pagination_class = PageNumberPagination  # pagination
    queryset = Review.objects.all()    # List of data from DB
    serializer_class = ReviewSerializer  # class of serializer inherited by model serializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})
        # 1. Get data from validated data
        movie_id = serializer.validated_data.get('movie_id')
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')

        # 2. Create object
        review = Review.objects.create(movie_id=movie_id, text=text)

        # 3. Return created object
        return Response(data=ReviewSerializer(review).data)


# class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     lookup_field = 'id'

#
# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         data = DirectorSerializer(instance=directors, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         # 0. Validation
#         serializer = DirectorValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         # 1. Get data from validated data
#         name = serializer.validated_data.get('name')
#
#         # 2. Create object
#         director = Director.objects.create(name=name)
#
#         # 3. Return created object
#         return Response(data=DirectorSerializer(director).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, director_id):
#     try:
#         director = Director.objects.get(id=director_id)
#     except Director.DoesNotExist:
#         return Response(data={'Error': 'Director not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = DirectorSerializer(instance=director, many=False).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data=DirectorSerializer(director).data)
#
#
# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         data = MovieSerializer(instance=movies, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         # 0. Validation
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         # 1. Get data from validated data
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         duration = serializer.validated_data.get('duration')
#         director_id = serializer.validated_data.get('director_id')
#         # rating = request.data.get('rating')
#
#         # 2. Create object
#         movie = Movie.objects.create(title=title, description=description, duration=duration,
#                                      director_id=director_id)
#         # movie.rating.set(rating)
#         # movie.save()
#
#         # 3. Return created object
#         return Response(data=MovieSerializer(movie).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, movie_id):
#     try:
#         movie = Movie.objects.get(id=movie_id)
#     except Movie.DoesNotExist:
#         return Response(data={'Error': 'Movie not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = MovieSerializer(instance=movie, many=False).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director_id')
#         movie.save()
#         return Response(data=MovieSerializer(movie).data)
#
#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     print(request.user)
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewSerializer(instance=reviews, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         # 0. Validation
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST,
#                             data={'errors': serializer.errors})
#         # 1. Get data from validated data
#         movie_id = serializer.validated_data.get('movie_id')
#         text = serializer.validated_data.get('text')
#         stars = serializer.validated_data.get('stars')
#
#         # 2. Create object
#         review = Review.objects.create(movie_id=movie_id, text=text)
#
#         # 3. Return created object
#         return Response(data=ReviewSerializer(review).data)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, review_id):
#     try:
#         review = Review.objects.get(id=review_id)
#     except Review.DoesNotExist:
#         return Response(data={'Error': 'Review not Found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = ReviewSerializer(instance=review, many=False).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         review.movie_id = request.data.get('movie_id')
#         review.text = request.data.get('text')
#         # review.stars = request.data.get('stars')
#         review.save()
#         return Response(data=ReviewSerializer(review).data)



