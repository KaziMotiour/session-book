import datetime
import imp

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

import datetime

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        
        self.assertIs(future_question.was_published_recently(), True)

def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    print(old_question)
    print(old_question.was_published_recently())
    self.assertIs(old_question.was_published_recently(), True)



class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
   
        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = Question.objects.create(question_text="Past question.", pub_date= datetime.date.today() - datetime.timedelta(30))
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )
    
    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        # question = Question.objects.create(question_text="Past question.", pub_date= datetime.date.today() - datetime.timedelta(30))
        question = Question.objects.create(question_text="Future question.", pub_date= datetime.date.today() + datetime.timedelta(30))
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )
    
    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question1 = Question.objects.create(question_text="Past question1.", pub_date= datetime.date.today() - datetime.timedelta(30))
        question2 = Question.objects.create(question_text="Past question2", pub_date= datetime.date.today() - datetime.timedelta(5))
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )