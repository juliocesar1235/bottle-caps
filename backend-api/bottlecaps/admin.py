from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.contrib.auth.models import User

from bottlecaps.models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'rating', 'user', 'created_at', 'last_updated_at',)

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_score', 'user_review_count', 'created_at', 'last_updated_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'last_updated_at',)

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
