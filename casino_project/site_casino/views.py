# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from .serializers import UserProfileSerializer, UserSerializer, CasinoProfileSerializer, CasinoCommentSerializer, \
    GameProfileSerializer, GamesOfWeekSerializer
from rest_framework import status
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import UserProfile, CasinoProfile, CasinoComment, GameProfile, GamesOfWeek
from drf_yasg import openapi
User = get_user_model()

# user
@swagger_auto_schema(
    method='post',
    request_body=UserProfileSerializer,
    responses={201: UserProfileSerializer()}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Вы можете вернуть данные профиля пользователя вместо данных пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={200: 'Login successful.', 401: 'Invalid credentials.'}
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Log in a user.

    This endpoint allows users to log in by providing their email and password.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    print(f"Attempting login with email: {email}")
    # Используйте 'username' вместо 'email' для аутентификации
    try:
        # Query the default User model by email
        user = User.objects.get(Q(email__iexact=email))
    except User.DoesNotExist:
        return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


    if user.check_password(password):
        login(request, user)
        return Response({'detail': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


@swagger_auto_schema(
    method='get',
    responses={
        200: 'OK',
        404: 'Not Found',
    },
)
@api_view(['GET'])
def get_user_by_email(request, email):
    try:
        user_profile = get_object_or_404(UserProfile, email=email)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Пользователь с указанным email не найден'}, status=status.HTTP_404_NOT_FOUND)

#casino
@swagger_auto_schema(
    method='get',
    responses={
        200: 'OK - Возвращает объекты CasinoProfile',
        404: 'Not Found - Если объекты не найдены',
    },
)
@api_view(['GET'])
def get_all_casino_profiles(request):
    casino_profiles = CasinoProfile.objects.all()

    serializer = CasinoProfileSerializer(casino_profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    responses={
        200: 'OK - Возвращает комментарии казино',
        404: 'Not Found - Если комментарии не найдены',
    },
)
@api_view(['GET'])
def casino_comments(request, casino_id):
    comments = CasinoComment.objects.filter(casino_id=casino_id)
    serializer = CasinoCommentSerializer(comments, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email', 'casino_id', 'comment_text'],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
            'casino_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Casino ID'),
            'comment_text': openapi.Schema(type=openapi.TYPE_STRING, description='Comment text'),
            'rating': openapi.Schema(type=openapi.TYPE_NUMBER, description='User rating for casino (optional)'),
        }
    ),
    responses={200: CasinoCommentSerializer()}
)
@api_view(['POST'])
def add_comment_to_casino(request):
    email = request.data.get('email')
    casino_id = request.data.get('casino_id')
    comment_text = request.data.get('comment_text')
    rating = request.data.get('rating')


    user = get_object_or_404(UserProfile, email=email)

    casino = get_object_or_404(CasinoProfile, id=casino_id)

    comment = CasinoComment.objects.create(
        casino=casino,
        user=user,
        comment_text=comment_text,
        rating=rating
    )

    serializer = CasinoCommentSerializer(comment)
    return Response(serializer.data)

# Next games




@swagger_auto_schema(
    method='get',
    responses={
        200: 'OK - Возвращает объекты GameProfile',
        404: 'Not Found - Если объекты не найдены',
    },
)
@api_view(['GET'])
def get_all_game_profiles(request):
    game_profiles = GameProfile.objects.all()
    serializer = GameProfileSerializer(game_profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    responses={
        200: 'OK - Возвращает объекты GameProfile',
        404: 'Not Found - Если объекты не найдены',
    },
)
@api_view(['GET'])
def get_all_game_profiles(request):
    game_profiles = GameProfile.objects.all()
    serializer = GameProfileSerializer(game_profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='get',
    responses={
        200: 'OK - Возвращает объекты GamesOfWeek',
        404: 'Not Found - Если объекты не найдены',
    },
)
@api_view(['GET'])
def get_games_of_week(request):
    games_of_week = GamesOfWeek.objects.first()

    game_id_1 = games_of_week.game_id_1
    game_id_2 = games_of_week.game_id_2
    game_id_3 = games_of_week.game_id_3


    casino_profile_1 = GameProfile.objects.get(id=game_id_1)
    casino_profile_2 = GameProfile.objects.get(id=game_id_2)
    casino_profile_3 = GameProfile.objects.get(id=game_id_3)

    serialized_casino_1 = GameProfileSerializer(casino_profile_1).data
    serialized_casino_2 = GameProfileSerializer(casino_profile_2).data
    serialized_casino_3 = GameProfileSerializer(casino_profile_3).data

    # Combine the serialized casino profiles into a single dictionary
    result = [
        serialized_casino_1,
        serialized_casino_2,
        serialized_casino_3,
    ]

    return Response(result, status=status.HTTP_200_OK)