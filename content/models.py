from django.db import models
from common.basemodels import BaseModel
from django.contrib.sites.models import Site
from django.contrib.contenttypes.fields import GenericRelation
from social.models import Rate, Like, Comment
from django.db.models import F, Avg, Sum, Count
from .utils import genre_image_path, playlist_cover_path, playlist_mobile_cover_path, album_mobile_head_cover_path,\
    album_cover_path, album_list_cover_path, cover_zip_path, album_demo_path
from django_minio_backend import MinioBackend
from reusable.utils import create_slug_fa, get_client_ip_address
from utility.models import Channels


class ItunesPages:
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


class GenreCategory(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    genre_category = models.ManyToManyField(GenreCategory, blank=True, related_name='genres',
                                            related_query_name='genre')
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to=genre_image_path, blank=True, storage=MinioBackend(bucket_name='itunes-public'))
    color_1 = models.CharField(max_length=10, blank=True)
    color_2 = models.CharField(max_length=10, blank=True)

    @property
    def slug_fa(self) -> str:
        return create_slug_fa(self.name)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class GiftAlbumRelation(BaseModel):
    PHYSICAL = 'phy'
    SIGNED = 'sig'
    DIGITAL = 'dig'
    TYPE_CHOICES = (
        (PHYSICAL, 'فیزیکی'),
        (SIGNED, 'امضا شده'),
        (DIGITAL, 'دیجیتال'),
    )

    album_type = models.CharField(choices=TYPE_CHOICES, max_length=3)
    from_album = models.ForeignKey('Album',
                                   on_delete=models.CASCADE, null=True, related_name='from_album')
    to_album = models.ForeignKey('Album', on_delete=models.CASCADE, null=True, related_name='to_album')

    def album_type_to_persian(self):
        if self.album_type == GiftAlbumRelation.PHYSICAL:
            return 'فیزیکی'
        elif self.album_type == GiftAlbumRelation.SIGNED:
            return 'امضا شده'
        else:
            return 'دیجیتال'


class Album(BaseModel):
    title = models.CharField(max_length=150, unique=True)
    short_title = models.CharField(max_length=60, blank=True, null=True)
    title_en = models.CharField(max_length=150, blank=True)
    cover = models.ImageField(upload_to=album_cover_path, blank=True, null=True,
                              storage=MinioBackend(bucket_name='itunes-public'))
    mobile_head_cover = models.ImageField(upload_to=album_mobile_head_cover_path, blank=True, null=True,
                                          storage=MinioBackend(bucket_name='itunes-public'))
    list_cover = models.ImageField(upload_to=album_list_cover_path,blank=True, null=True,
                                   storage=MinioBackend(bucket_name='itunes-'))
    cover_thumb = models.ImageField(blank=True, storage=MinioBackend('itunes_public'))
    auto_sample_generate = models.BooleanField(default=False, blank=True,
                                               help_text='Do you want to generate sample version?')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    description = models.TextField()
    release_date = models.DateTimeField(blank=True, null=True)
    # publisher = models.ForeignKey()
    is_banner = models.BooleanField(default=False)
    cost_share = models.PositiveIntegerField(default=0)
    cover_zip = models.FileField(upload_to=cover_zip_path, storage=MinioBackend(bucket_name='itunes-sales'))
    available_virtual = models.BooleanField(default=False)
    physical_price = models.DecimalField(decimal_places=2, max_digits=6)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField()
    signed_physical_price = models.DecimalField(decimal_places=2, max_digits=6)
    signed_discount = models.FloatField()
    physical_discount = models.FloatField()
    genres = models.ManyToManyField(Genre, related_name='albums', related_query_name='album', blank=True)
    channels = models.ManyToManyField(Channels, related_name='albums', related_query_name='album')
    rate = GenericRelation(Rate, related_name='content_album')
    like = GenericRelation(Like, related_name='content_album')
    comment = GenericRelation(Comment, related_name='content_album')
    enable = models.BooleanField(default=True)
    pre_sale = models.BooleanField(default=False)
    demo = models.FileField(upload_to=album_demo_path, blank=True, storage=MinioBackend(bucket_name='itunes-public'))

    def __str__(self):
        return '{}{}'.format(self.title, self.id)

    @property
    def slug(self):
        if self.title_en == '':
            return str(self.id)
        data = []
        data.extend([item for item in self.title_en.split(' ') if item != ''])
        return '-'.join(data)

    @property
    def slug_fa(self):
        if self.title == '':
            return str(self.id)
        data = []
        data.extend([item for item in self.title.split(' ') if item != ''])
        return '-'.join(data)


class AlbumFeedCategory(BaseModel):
    title = models.CharField(max_length=60, unique=True)
    albums = models.ManyToManyField(Album,
                                    related_name='album_categories',
                                    related_query_name='album_category',
                                    through='AlbumFeedCategoryAlbumRelation')
    sites = models.ManyToManyField(Site)
    order = models.PositiveIntegerField(default=0)
    enable = models.BooleanField(default=True)

    @property
    def slug_fa(self):
        return create_slug_fa(self.title)


class AlbumFeedCategoryAlbumRelation(BaseModel):
    album_feed_category = models.ForeignKey(AlbumFeedCategory, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order',)


class AlbumVideo(BaseModel):
    album = models.ForeignKey(Album,
                              on_delete=models.CASCADE,
                              related_name='album_videos',
                              related_query_name='album_video',
                              )
    tags = models.ManyToManyField(Tag, related_name='album_tags', related_query_name='album_tag', blank=True)
    comments = GenericRelation(Comment, related_query_name='album_video_comment')
    likes = GenericRelation(Like, related_query_name='album_video_like')
    rates = GenericRelation(Rate, related_query_name='album_video_rate')

    @property
    def title(self):
        return self.album.title

    def __str__(self):
        return self.title

    @property
    def slug_fa(self):
        return create_slug_fa(self.title)

    @property
    def rate_score(self):
        return self.rates.all().aggregate(Avg('score'))['score_avg']

    @property
    def like_no(self):
        return self.likes.count()
    
