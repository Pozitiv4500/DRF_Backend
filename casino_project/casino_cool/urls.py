

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from site_casino.views import registration_view, login_view,get_user_by_email,get_all_casino_profiles,casino_comments,add_comment_to_casino,get_all_game_profiles,get_games_of_week


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('get_user_by_email/<str:email>/', get_user_by_email, name='get_user_by_email'),
    path('games-of-week/', get_games_of_week, name='games_of_week'),

    path('all-casino-profiles/', get_all_casino_profiles, name='all_casino_profiles'),
    path('all-game-profiles/', get_all_game_profiles, name='all_game_profiles'),

    path('casinos/<int:casino_id>/comments/', casino_comments, name='casino_comments'),
    path('add_comment/', add_comment_to_casino, name='add_comment'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
