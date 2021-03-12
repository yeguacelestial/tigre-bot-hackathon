from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from chatbot.models import Question
from chatbot.serializers import UserSerializer, GroupSerializer, QuestionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(GenericViewSet, 
                    CreateModelMixin, 
                    RetrieveModelMixin, 
                    UpdateModelMixin, 
                    ListModelMixin):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            new_data = {
                "content": request.data['content'],
                "answer": "HE RESPONDIDO A TI PREGUNTA HIJO"
            }

            serializer.create(new_data)

            return Response(new_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)