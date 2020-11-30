from rest_framework import serializers
from .models import User, Category, Title, Review 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='user.username', read_only=True, required=False)
    class Meta:
        model = Review
        fields = ['heading', 'comment', 'rating', 'author', 'title', 'created_at', 'last_updated_at']
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TitleSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, required=False, read_only=True)
    categories = CategorySerializer(source='category', many=True, required=False, read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'name', 'synopsis', 'cover_image_path', 'featured', 'user_score', 'user_review_count', 'reviews', 'categories','created_at', 'last_updated_at']


class TitleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id', 'name', 'cover_image_path', 'featured']



