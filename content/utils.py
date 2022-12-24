from os import path
from django.core.exceptions import ValidationError


def is_image(ext):
    format_support = ['jpeg', 'jpg', 'png', 'bmp', 'webp']
    if ext.split('.')[1] not in format_support:
        return ValidationError('unknown format')
    return True


def is_audio(ext):
    format_support = ['mp3', 'm4a']
    if ext.split('.')[1] not in format_support:
        return ValidationError('unknown file format')
    return True


def is_rbt_audio(ext):
    format_support = ['wav', 'mp3']
    if ext.split('.')[1] not in format_support:
        return ValidationError('unknown file format')
    return True


def is_zip(ext):
    format_support = ['rar', 'zip']
    if ext.split('.')[1] not in format_support:
        return ValidationError('unknown file format')
    return True


