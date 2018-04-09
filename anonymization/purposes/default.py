from collections import OrderedDict
from django.core.exceptions import ImproperlyConfigured
from datetime import timedelta, datetime
import six

purposes_map = OrderedDict()


class PurposeMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        new_class = super(PurposeMetaclass, mcs).__new__(mcs, name, bases, attrs)
        if hasattr(new_class, 'slug') and new_class.slug:
            if new_class.slug in purposes_map:
                raise ImproperlyConfigured('More anonymization purposes with slug {}'.format(new_class.slug))

            purposes_map[new_class.slug] = new_class
        return new_class


class AbstractPurpose(six.with_metaclass(PurposeMetaclass, object)):
    name = None
    slug = None
    fields = {}
    expires_in = timedelta()
