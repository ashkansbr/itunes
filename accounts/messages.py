from enum import Enum
from django.utils.translation import gettext_lazy as _


class Messages(Enum):
    INVALID_FORMAT = _('unknown file format')
    IMAGE_SIZE = _("image size shouldn't be greater than 4MB")
    DATABASE_ERROR = _('database is not available')