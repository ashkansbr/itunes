from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from common.basemodels import BaseModel
from .utils import FilePath


class User(AbstractUser):
    ...


class Profile(BaseModel):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='profile',
                                related_query_name='profile',
                                verbose_name=_('user')
                                )
    phone = models.CharField(max_length=11,
                             validators=[RegexValidator(regex=r"09\d{9}")],
                             verbose_name=_('phone'),
                             )
    name = models.CharField(max_length=80,
                            blank=True
                            )
    family_name = models.CharField(max_length=80,
                                   blank=True,
                                   verbose_name=_('family name')
                                   )
    referrer = models.ForeignKey('self',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 default=None,
                                 )
    referral_code = models.CharField(max_length=10,
                                     blank=True,
                                     verbose_name=_('referral code'))

    image = models.ImageField(blank=True,
                              upload_to=FilePath.profile_pic_path,
                              )
    score = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(help_text=_('مقدار کیف پول به تومان'))
    email = models.EmailField(blank=True)
    birth_date = models.DateTimeField(blank=True)
