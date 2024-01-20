# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    number_of_avatar = models.BigIntegerField()
    age = models.BigIntegerField()

    def __str__(self):
        return self.user.username


class CasinoProfile(models.Model):
    casino_name = models.CharField(max_length=100)
    image_link = models.URLField()
    ranking_position = models.PositiveIntegerField()
    reliability = models.FloatField()
    speed = models.FloatField()
    payout = models.FloatField()
    player_rating = models.FloatField(default=5.0)
    editor_rating = models.FloatField()
    casino_text = models.TextField()
    promo_text = models.TextField()
    promo_code = models.TextField()
    payments_images = models.TextField()
    providers_images = models.TextField()
    interface_languages_image = models.TextField()
    countries_access = models.TextField()
    sorting_criteria = models.TextField()
    casino_link = models.URLField()

class CasinoComment(models.Model):
    casino = models.ForeignKey(CasinoProfile, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment_text = models.TextField()
    rating = models.FloatField()  # Поле для оценки пользователя
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.user.user.username} на {self.casino.id}"

class GameProfile(models.Model):
    game_name = models.CharField(max_length=100)
    image_link = models.URLField()
    ranking_position = models.PositiveIntegerField()
    editor_rating = models.FloatField()
    game_text = models.TextField()

    release_date = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    min_bet = models.FloatField()
    max_bet = models.FloatField()
    max_payout = models.FloatField()
    reels = models.PositiveIntegerField()
    rows = models.PositiveIntegerField()
    pay_lines = models.PositiveIntegerField()
    rtp = models.FloatField()
    volatility = models.CharField(max_length=100)
    platforms = models.CharField(max_length=None)

    casino_id_1 = models.PositiveIntegerField()
    casino_id_2 = models.PositiveIntegerField()

    multiple_casino_ids = models.TextField()

    sorting_criteria = models.TextField()

class GamesOfWeek(models.Model):
    game_id_1 = models.PositiveIntegerField()
    game_id_2 = models.PositiveIntegerField()
    game_id_3 = models.PositiveIntegerField()