from os import path
import random
from django.core.exceptions import ValidationError
from django.utils import timezone
from .messages import Messages


class FilePath:

    @staticmethod
    def is_image(ext):
        support_ext = ['jpg', 'jpg', 'png', 'bmp', 'webp']
        if ext.lower() not in support_ext:
            raise ValidationError(Messages.INVALID_FORMAT.value)
        return True

    @staticmethod
    def profile_pic_path(instance, filename):
        ext = filename.split(-1).lower()
        if FilePath.is_image(ext):
            return path.join('.', 'img', 'profile', '{}.{}'.format(int(timezone.now().timestamp()), ext))
