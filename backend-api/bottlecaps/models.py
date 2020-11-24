from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    pass
User._meta.get_field('email')._unique = True


def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
post_save.connect(create_token, sender=User)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'<Category "{self.name}">'


class Title(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    synopsis = models.TextField(null=False, blank=False)
    cover_image_path = models.URLField(max_length=255, null=True, blank=True)
    user_score = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    user_review_count = models.PositiveIntegerField(null=False, blank=False)
    featured = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name='titles')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return f'<Title "{self.name}">'


class Review(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(null=False, blank=False)
    user = models.ForeignKey(User, related_name='reviews', null=False, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, related_name='reviews', null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    last_updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return f'<Review {self.id}>'


