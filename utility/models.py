from django.db import models
from common.basemodels import BaseModel


class Channels(BaseModel):
    ITUNES = 'i'
    DINGTUNES = 'd'
    CHANNELS_CHOICES = (
        (ITUNES, 'itunes'),
        (DINGTUNES, 'dingtunes')
    )

    name = models.CharField(max_length=1, choices=CHANNELS_CHOICES)

    def __str__(self):
        return self.name


class ContactUs(BaseModel):
    origin = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.origin


class Faq(BaseModel):
    MUSIC = 'm'
    CHARGOOSH = 'c'
    AUDIO_BOOK = 'a'
    TYPE_CHOICES = (
        (MUSIC, 'موزیک'),
        (CHARGOOSH, 'چارگوش'),
        (AUDIO_BOOK, 'کتاب صوتی'),
    )

    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    tip = models.BooleanField(default=False)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return '{}{}'.format(self.id, self.question)

