from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api_yamdb.settings import DEFAULT_FROM_EMAIL

from .models import User
from .serializers import UserSerializer


def conf_code_to_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='Confirmation',
        message=f'Your code is {confirmation_code}',
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=UserSerializer.data['email'],
        fail_silently=False,
    )


class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # пока не знаю, что писать
    # serializer_class = ?
    # permission_class = ?
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('username',)


class SignUp(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # создаем confirmation code и отправляем на почту
            conf_code_to_email(serializer.data['username'])
            return Response(
                {'email': serializer.data['email'],
                 'username': serializer.data['username']},
                status=status.HTTP_200_OK
            )
