from django.db import models
from common.basemodels import BaseModel
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()


class Like(BaseModel):
    profile = models.ForeignKey(User.profile,
                                on_delete=models.CASCADE,
                                related_name='social-likes',
                                related_query_name='social-like'
                                )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        unique_together = ('content_type', 'profile', 'object_id')

    def __str__(self):
        return '{}{}'.format(self.content_type, self.profile.name)


class Comment(BaseModel):
    profile = models.ForeignKey(User.profile,
                                on_delete=models.CASCADE,
                                related_name='social_comments',
                                related_query_name='social_comment'
                                )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    text = models.TextField()

    class Meta:
        unique_together = ('object_id', 'content_type', 'profile')

    def __str__(self):
        return '{}{}'.format(self.content_type, self.profile.name)


class Rate(BaseModel):
    profile = models.ForeignKey(User.profile,
                                on_delete=models.CASCADE,
                                related_name='social_rates',
                                related_query_name='social_rate'
                                )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        unique_together = ('profile', 'object_id', 'content_type')

    def __str__(self):
        return '{}{}'.format(self.content_type, self.profile.name)




