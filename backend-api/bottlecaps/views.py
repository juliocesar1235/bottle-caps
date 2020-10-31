from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import *

class HomeView(APIView):
    def get(self, request):
        user = request.user
        serialized_user = ProfileSerializer(Profile.objects.get(user=user)).data
        return Response(serialized_user)
