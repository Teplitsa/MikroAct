from django.db import models

DEFAULT_CHARFIELD_LENGTH = 255


class DefaultCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', DEFAULT_CHARFIELD_LENGTH)
        super(DefaultCharField, self).__init__(*args, **kwargs)
