from django.db import models

# Create your models here.


class Poll(models.Model):
	name = models.CharField(max_length=256, null=True, unique=True)
	date_start = models.DateTimeField(auto_now_add=True)
	date_end = models.DateTimeField()
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Question(models.Model):
	STATUS = (
				('Text Answer','Text Answer'),
				('One Choice','One Choice'),
				('Many Choice','Many Choice'),
			)
	name = models.CharField(max_length=256, null=True)
	type_question = models.CharField(max_length=200, null=True, choices=STATUS)
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=180,null=True)
	
	def __str__(self):
		return self.text

class Answer(models.Model):
	user = models.IntegerField()
	poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
	choice_one = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True, blank=True)
	choice_many = models.ManyToManyField(Choice, related_name='choices', null=True, blank=True)
	text = models.CharField(max_length=180,null=True, blank=True)

	def __str__(self):
		return str(self.user)
