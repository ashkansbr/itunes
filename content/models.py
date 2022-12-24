from django.db import models
from common.basemodels import BaseModel
from django.contrib.sites.models import Site
from reusable.utils import create_slug_fa, get_client_ip_address


class ItunesPages():
    START_PAGE = 'start_page'
    MUSIC_PAGE = 'music_page'
    BOOK_PAGE = 'book_page'
    PAGE_CHOICES = (
        (START_PAGE, 'صفحه شروع'),
        (MUSIC_PAGE, 'صفحه نخست موزیک'),
        (BOOK_PAGE, 'صفحه نخست کتاب'),
    )


class BaseVidaneh(BaseModel):
    vidaneh_url = models.URLField(blank=True)
    video = models.URLField(blank=True)
    thumb = models.URLField(blank=True)

    class Meta:
        abstract = True


class Video(BaseVidaneh):
    title = models.CharField(max_length=50)
    sites = models.ManyToManyField(Site)

    def __str__(self):
        return "<{}>".format(self.title)

    @property
    def slug_fa(self) -> str:
        return create_slug_fa(self.title)
    # def related(self):
    #     return Video.objects.exclude(id=self.id).filter(sites__id__in)

    def video_link_generator(self):
        qualities = ['480', '720', '1080']
        name = self.video.split('_')[0]
        return [{'quality': quality, 'link': '{}{}.mp4'.format(name, quality)} for quality in qualities]

    # def save(self, *args, **kwargs):
