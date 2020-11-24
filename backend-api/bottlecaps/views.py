from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny # Let anonymous users register
    ]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, _ = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class TitleList(APIView):
    """
    Get all titles, or create a new one
    """
    def get(self, request):
        titles = Title.objects.all()
        serialized_titles = TitleShortSerializer(titles, many=True)
        return Response(serialized_titles.data)

    def post(self, request):
        serialized_title = TitleSerializer(data=request.data)
        if serialized_title.is_valid():
            serialized_title.save()
            return Response(serialized_title.data, status=status.HTTP_201_CREATED)


class TitleView(APIView):
    """
    Retrieve, update or delete existing title instance
    """
    def get_object(self, key):
        try:
            return Title.objects.get(id=key)
        except Title.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, key):
        title = self.get_object(key)
        serialized_title = TitleSerializer(title)
        return Response(serialized_title.data)

    def put(self, request, key):
        title = self.get_object(key)
        serialized_title = TitleSerializer(title, data=request.data)
        if serialized_title.is_valid():
            serialized_title.save()
            return Response(serialized_title.data)
        return Response(serialized_title.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, key):
        title = self.get_object(key)
        title.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(APIView):
    """
    Get all reviews, or create a new one
    """
    def get(self, request):
        reviews = Review.objects.all()
        serialized_reviews = ReviewSerializer(reviews, many=True)
        return Response(serialized_reviews.data)

    def post(self, request):
        serialized_review = ReviewSerializer(data=request.data)
        title = Title.objects.get(id=request.data['title'])
        if serialized_review.is_valid():
            serialized_review.save(user=request.user, title=title)
            return Response(serialized_review.data, status=status.HTTP_201_CREATED)
        return Response(serialized_review.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewView(APIView):
    """
    Retrieve, update or delete existing review instance
    """
    def get_object(self, key):
        try:
            return Review.objects.get(id=key)
        except Review.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, key):
        review = self.get_object(key)
        serialized_review = ReviewSerializer(review)
        return Response(serialized_review.data)

    def put(self, request, key):
        review = self.get_object(key)
        serialized_review = ReviewSerializer(review, data=request.data)
        if serialized_review.is_valid():
            serialized_review.save()
            return Response(serialized_review.data)
        return Response(serialized_review.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, key):
        review = self.get_object(key)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
