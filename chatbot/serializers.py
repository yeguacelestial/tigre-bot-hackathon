from django.contrib.auth.models import User, Group

from chatbot.models import Question

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    """
    This is the question serializer. Receives a question as string.
    """
    class Meta:
        model = Question
        fields = ['id', 'content']