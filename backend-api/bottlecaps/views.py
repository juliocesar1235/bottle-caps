from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *


class TitleList(APIView):
    """
    Get all titles, or create a new one
    """
    def get(self, request):
        titles = Title.objects.all()
        serialized_titles = TitleSerializer(titles, many=True)
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
            raise Http404

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
            raise Http404

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
