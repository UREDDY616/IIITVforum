from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.db import models
from django.db.models import F
from django.utils.text import slugify
from django_markdown.models import MarkdownField
from hitcount.models import HitCountMixin
from taggit.managers import TaggableManager
from django.db.models.signals import post_save
from django.contrib.auth.models import User



class QaQuestion(models.Model, HitCountMixin):
    """Model class to contain every question in the forum"""
    slug = models.SlugField(max_length=200)
    title = models.CharField(max_length=200, blank=False)
    description = MarkdownField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    tags = TaggableManager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    closed = models.BooleanField(default=False)



    def __str__(self):
        return self.title


class QaAnswer(models.Model):
    """Model class to contain every answer in the forum and to link it
    to the proper question."""
    question = models.ForeignKey(QaQuestion)
    answer_text = MarkdownField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    answer = models.BooleanField(default=False)


    def __str__(self):  # pragma: no cover
        return self.answer_text

    class Meta:
        ordering = ['-answer', '-pub_date']




class QaBaseComment(models.Model):
    """Abstract model to define the basic elements to every single comment."""
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True

    def __str__(self):  # pragma: no cover
        return self.comment_text


class QaAnswerComment(QaBaseComment):
    """Model class to contain the comments for the answers."""
    comment_text = MarkdownField()
    answer = models.ForeignKey(QaAnswer)



class QaQuestionComment(QaBaseComment):
    """Model class to contain the comments for the questions."""
    comment_text = models.CharField(max_length=250)
    question = models.ForeignKey(QaQuestion)
