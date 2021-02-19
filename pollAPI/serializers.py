from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import *


class UserSerializer(serializers.ModelSerializer):
	token = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = User
		fields = '__all__'

	def get_token(self, obj):
		token = Token.objects.get(user=obj)
		return str(token.key)


class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = '__all__'



