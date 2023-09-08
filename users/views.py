from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from .models import CustomUser


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.create_user(username=username, password=password)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})


@api_view(['POST'])
def authorization_api_view(request):
    # 1. Get credential data from client
    username = request.data.get('username')
    password = request.data.get('password')

    # 2. Authentication of user
    user = authenticate(username=username, password=password)
    if user is not None:
        # 3. Return Key
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        return Response(data={'key': token.key})
    else:
        # 4. Return error
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'User credentials not correct!'})


@api_view(['POST'])
def confirm_user(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    confirmation_code = serializer.validated_data['confirmation_code']
    is_active = serializer.validated_data['is_active']

    try:
        user = CustomUser.objects.get(username=username, confirmation_code=confirmation_code)
    except CustomUser.DoesNotExist:
        return Response({'detail': 'Invalid username or confirmation code.'}, status=status.HTTP_400_BAD_REQUEST)

    if user.is_active:
        return Response({'detail': 'User is already active.'}, status=status.HTTP_400_BAD_REQUEST)

    user.is_active = is_active
    user.confirmation_code = None
    user.save()

    return Response({'detail': 'User has been confirmed.'}, status=status.HTTP_200_OK)

