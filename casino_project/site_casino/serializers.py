# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, CasinoProfile, CasinoComment, GameProfile, GamesOfWeek


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Добавляем поле для пароля

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = UserProfile
        fields = ['id','email',     'password', 'username',  'number_of_avatar', 'age']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password, email=validated_data['email'])
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile

class GameProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameProfile
        fields = ('id', 'game_name', 'image_link', 'ranking_position', 'editor_rating', 'game_text',
                  'release_date', 'genre', 'min_bet', 'max_bet', 'max_payout', 'reels', 'rows',
                  'pay_lines', 'rtp', 'volatility', 'platforms', 'casino_id_1', 'casino_id_2',
                  'multiple_casino_ids','sorting_criteria')

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Разделение текста на два языка по трем слешам
        game_name_parts = data['game_name'].split("///")
        game_text_parts = data['game_text'].split("///")
        genre_parts = data['genre'].split("///")
        volatility_parts = data['volatility'].split("///")
        platforms_parts = data['platforms'].split("///")

        # Задание текста для английского и бразильского языков
        name_eng = game_name_parts[0].strip() if len(game_name_parts) > 0 else ''
        name_braz = game_name_parts[1].strip() if len(game_name_parts) > 1 else ''

        text_eng = game_text_parts[0].strip() if len(game_text_parts) > 0 else ''
        text_braz = game_text_parts[1].strip() if len(game_text_parts) > 1 else ''

        genre_eng = genre_parts[0].strip() if len(genre_parts) > 0 else ''
        genre_braz = genre_parts[1].strip() if len(genre_parts) > 1 else ''

        volatility_eng = volatility_parts[0].strip() if len(volatility_parts) > 0 else ''
        volatility_braz = volatility_parts[1].strip() if len(volatility_parts) > 1 else ''

        platforms_eng = platforms_parts[0].strip() if len(platforms_parts) > 0 else ''
        platforms_braz = platforms_parts[1].strip() if len(platforms_parts) > 1 else ''

        # Добавление языковых полей
        data['game_name'] = {'english': name_eng, 'brazilian': name_braz}
        data['game_text'] = {'english': text_eng, 'brazilian': text_braz}
        data['genre'] = {'english': genre_eng, 'brazilian': genre_braz}
        data['volatility'] = {'english': volatility_eng, 'brazilian': volatility_braz}
        data['platforms'] = {'english': platforms_eng, 'brazilian': platforms_braz}

        data['multiple_casino_ids'] = data['multiple_casino_ids'].split(',') if data['multiple_casino_ids'] else []
        data['sorting_criteria'] = data['sorting_criteria'].split(',') if data['sorting_criteria'] else []

        return data
class GamesOfWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesOfWeek
        fields = ('game_id_1', 'game_id_2', 'game_id_3')


class CasinoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasinoProfile
        fields = ('id', 'casino_name', 'image_link', 'ranking_position', 'reliability', 'speed', 'payout',
                  'player_rating', 'editor_rating', 'casino_text', 'promo_text', 'promo_code',
                  'payments_images', 'providers_images', 'interface_languages_image', 'countries_access',
                  'sorting_criteria', 'casino_link')

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Разделение текста на два языка по трем слешам
        casino_text_parts = data['casino_text'].split("///")
        promo_text_parts = data['promo_text'].split("///")
        name_text_parts = data['casino_name'].split("///")
        # Задание текста для английского и бразильского языков

        a=casino_text_parts[0].strip() if len(casino_text_parts) > 0 else '',
        b =  promo_text_parts[0].strip() if len(promo_text_parts) > 0 else '',



        c = casino_text_parts[1].strip() if len(casino_text_parts) > 1 else '',
        d = promo_text_parts[1].strip() if len(promo_text_parts) > 1 else '',

        name_eng = name_text_parts[0].strip() if len(name_text_parts) > 0 else '',
        name_braz = name_text_parts[1].strip() if len(name_text_parts) > 1 else '',
        # Добавление старых полей
        data['casino_name'] = {'english': name_eng, 'brazilian': name_braz}
        data['promo_text'] = data['promo_text'].split(',') if data['promo_text'] else []
        data['promo_code'] = data['promo_code'].split(',') if data['promo_code'] else []
        data['sorting_criteria'] = data['sorting_criteria'].split(',') if data['sorting_criteria'] else []
        data['payments_images'] = data['payments_images'].split(',') if data['payments_images'] else []
        data['providers_images'] = data['providers_images'].split(',') if data['providers_images'] else []
        data['interface_languages_image'] = data['interface_languages_image'].split(',') if data[
            'interface_languages_image'] else []
        data['countries_access'] = data['countries_access'].split(',') if data['countries_access'] else []
        data['casino_text'] = {'english': a, 'brazilian': c}
        data['promo_text'] = {'english': b, 'brazilian': d}
        return data
class CasinoCommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = CasinoComment
        fields = ('id', 'casino', 'user', 'comment_text', 'rating', 'created_at')