from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bottlecaps.models import *

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'rating', 'user', 'created_at', 'last_updated_at',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_score', 'user_review_count', 'created_at', 'last_updated_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'last_updated_at',)

# Re-register UserAdmin
admin.site.register(User, UserAdmin)
