from django.db import models

DEFAULT_CHARFIELD_LENGTH = 255
DEFAULT_DECIMAL_PLACES = 2
DEFAULT_MAX_DIGITS = 10


class DefaultCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', DEFAULT_CHARFIELD_LENGTH)
        super(DefaultCharField, self).__init__(*args, **kwargs)


class DefaultDecimalField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('decimal_places', DEFAULT_DECIMAL_PLACES)
        kwargs.setdefault('max_digits', DEFAULT_MAX_DIGITS)
        super(DefaultDecimalField, self).__init__(*args, **kwargs)


from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^shortcuts\.DefaultCharField"])
add_introspection_rules([], ["^shortcuts\.DefaultDecimalField"])
