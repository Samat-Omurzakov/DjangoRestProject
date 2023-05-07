from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from users.serializers import UserCreateSerializer, UserAuthorizeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# Create your views here.


@api_view(['POST'])
def authorization_aip_view(request):
    """ Validate Data """
    serializer = UserAuthorizeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    """ Read Data """
    # username = serializer.validated_data.get('username')
    # password = serializer.validated_data.get('password')
    """ Authenticate (Search) User"""
    # user = authenticate(username=username, password=password)
    user = authenticate(**serializer.validated_data)
    if user:
        """ Authorize User """
        # Token.objects.filter(user=user).delete()
        # token = Token.objects.create(user=user)
        token, creted = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    """ Error on Unauthorizing"""
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    user = User.objects.create(username=username, password=password)
    return Response(data={'user_id': user.id})


# @api_view(['Post'])
# def confirm_api_view(request):
#     serializer = UserAuthorizeSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response()
