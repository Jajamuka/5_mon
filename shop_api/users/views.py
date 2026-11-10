from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serialiizers import UserRegistrationSerializer, UserAuthSerializer, UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmationCode
import random
import string

@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False,
    )
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    ConfirmationCode.objects.create(user=user, code=code)

    return Response(data={'user_id': user.id, 'code': code},
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    code = serializer.validated_data['code']

    try:
        confirmation = ConfirmationCode.objects.get(code=code)
    except ConfirmationCode.DoesNotExist:
        return Response(data={'error': 'Неверный код'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = confirmation.user
    user.is_active = True
    user.save()
    confirmation.delete()

    return Response(data={'message': 'Пользователь подтверждён'})