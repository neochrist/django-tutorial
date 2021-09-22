from django.db import models
import datetime 

from django.utils import timezone


# Create your models here.


'''
In pool there are two models
Question and Choice.

Question has a question texd and a published date.

Choice has text fo the choice, votes
and it is associated with a Question
'''
#> q.was_published_recently() doesnt work on my text editor.
# it works in documentation, part two###


class Question(models.Model):
	#....



	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self)


class Choice(models.Model):
	#..

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)





