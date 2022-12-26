from os import path
from django.utils import timezone
from django.core.exceptions import ValidationError


def is_image(ext):
    format_support = ['jpeg', 'jpg', 'png', 'bmp', 'webp']
    if ext.split('.')[-1] not in format_support:
        return ValidationError('unknown format')
    return True


def is_audio(ext):
    format_support = ['mp3', 'm4a']
    if ext.split('.')[-1] not in format_support:
        return ValidationError('unknown file format')
    return True


def is_rbt_audio(ext):
    format_support = ['wav', 'mp3']
    if ext.split('.')[-1] not in format_support:
        return ValidationError('unknown file format')
    return True


def is_zip(ext):
    format_support = ['rar', 'zip']
    if ext.split('.')[-1] not in format_support:
        return ValidationError('unknown file format')
    return True


def genre_image_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'genre_image', "{}{}".format(int(timezone.now().timestamps()), ext))


def playlist_cover_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'playlist_image', '{}{}'.format(int(timezone.now().timestamp()), ext))


def playlist_mobile_cover_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'mobile_playlist_image', '{}{}'.format(int(timezone.now().timestamp()), ext))


def album_cover_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'album_cover', '{}{}'.format(int(timezone.now().timestamp()), ext))


def album_mobile_head_cover_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'album_mobile_head', '{}{}'.format(int(timezone.now().timestamp()), ext))


def album_list_cover_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.', 'img', 'album_list_cover', '{}{}'.format(int(timezone.now().timestamp()), ext))


def cover_zip_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_zip(ext):
        return path.join('.', 'zip', 'cover', '{}_acz.{}'.format(int(timezone.now().timestamp()), ext))


def track_zip_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_audio(ext):
        return path.join('.', 'zip', 'track', '{}{}'.format(int(timezone.now().timestamp()), ext))



