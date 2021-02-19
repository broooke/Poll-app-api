from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import *
from .models import *


# Create your views here.

'''Auth'''
@api_view(['GET'])
def loginUser(request):
	data = request.data
	username = data.get('username')
	password = data.get('password')

	if username is None or password is None:
		message = {'detail':'Fill in both fields'}
		return Response(message, status=status.HTTP_400_BAD_REQUEST)

	user = authenticate(username=username, password=password)

	if user is None:
		message = {'detail':'User does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)

	token, _ = Token.objects.get_or_create(user=user)

	serializer = UserSerializer(user, many=False)
	return Response(serializer.data)


'''CRUD Polls'''
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createPoll(request):
	data = request.data

	poll = Poll.objects.create(
		name=data.get('name'),
		date_end=data.get('date_end'),
		description=data.get('description')
	)

	serializer = PollSerializer(poll, many=False)
	return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updatePoll(request, pk):
	data = request.data
	try:
		poll = Poll.objects.get(id=pk)
		poll.name = data.get('name')
		poll.date_end = data.get('date_end')
		poll.description = data.get('description')

		poll.save()

		serializer = PollSerializer(poll, many=False)
		return Response(serializer.data)
	except:
		message = {'detail':'Poll does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePoll(request, pk):
	try:
		poll = Poll.objects.get(id=pk)
		poll.delete()
		return Response('Poll was deleted')
	except:
		message = {'detail':'Poll does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


'''CRUD Questions'''
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createQuestion(request, id_poll):
	data = request.data
	try:
		poll = Poll.objects.get(id=id_poll)

		question = Question.objects.create(
			name=data.get('name'),
			type_question=data.get('type_question'),
			poll=poll
		)

		serializer = QuestionSerializer(question, many=False)
		return Response(serializer.data)
	except:
		message = {'detail':'Poll does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateQuestion(request, pk):
	data = request.data
	try:
		question = Question.objects.get(id=pk)
		question.name = data.get('name')
		question.type_question = data.get('type_question')

		question.save()

		serializer = QuestionSerializer(question, many=False)
		return Response(serializer.data)
	except:
		message = {'detail':'Question does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteQuestion(request, pk):
	try:
		question = Question.objects.get(id=pk)
		question.delete()
		return Response('Question was deleted')
	except:
		message = {'detail':'Question does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


'''CRUD Choices'''
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createChoice(request, question_id):
	data = request.data
	try:
		question = Question.objects.get(id=question_id)

		choice = Choice.objects.create(
			question = question,
			text = data.get('text')
		)

		serializer = ChoiceSerializer(choice, many=False)
		return Response(serializer.data)
	except:
		message = {'detail':'Question does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateChoice(request, pk):
	data = request.data
	try:
		choice = Choice.objects.get(id=pk)
		choice.text = data.get('text')

		choice.save()

		serializer = ChoiceSerializer(choice, many=False)
		return Response(serializer.data)
	except:
		message = {'detail':'Choice does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteChoice(request, pk):
	try:
		choice = Choice.objects.get(id=pk)
		choice.delete()
		return Response('Choice was deleted')
	except:
		message = {'detail':'Choice does not exist'}
		return Response(message, status=status.HTTP_404_NOT_FOUND)

'''Get active polls'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getActivePolls(request):
	polls = Poll.objects.filter(date_end__gte=timezone.now()).filter(date_start__lte=timezone.now())
	serializer = PollSerializer(polls, many=True)
	return Response(serializer.data)


'''Vote'''
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def voteUser(request, poll_id):
	user = request.user
	data = request.data

	poll = Poll.objects.get(id=poll_id)
	questions = Question.objects.filter(poll=poll)
	i = 0
	for question in questions:
		type_question = question.type_question
		if type_question == 'Text Answer':
			Answer.objects.create(
				user = user.id,
				poll = poll,
				question = question,
				text = data.get('text'+str(i))
			)
			i+=1
		elif type_question == 'One Choice':
			Answer.objects.create(
				user = user.id,
				poll = poll,
				question = question,
				choice_one = Choice.objects.get(text=data.get('name'))
			)
		elif type_question == 'Many Choice':
			answer = Answer.objects.create(
				user = user.id,
				poll = poll,
				question = question
			)
			choice_num = 0
			for choice in question.choice_set.all():
				if choice.text == data.get('choice'+str(choice_num)):
					answer.choice_many.add(choice)
					choice_num+=1

	return Response("Answers saved!")


'''Get Details Result'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDetails(request):
	answers = Answer.objects.filter(user=request.user.id)
	serializer = AnswerSerializer(answers, many=True)
	return Response(serializer.data)
	
		