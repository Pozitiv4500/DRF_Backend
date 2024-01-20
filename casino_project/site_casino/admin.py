from django.contrib import admin
from .models import UserProfile, CasinoProfile, CasinoComment, GameProfile, GamesOfWeek

admin.site.register(UserProfile)
admin.site.register(CasinoProfile)

admin.site.register(CasinoComment)
admin.site.register(GameProfile)
admin.site.register(GamesOfWeek)