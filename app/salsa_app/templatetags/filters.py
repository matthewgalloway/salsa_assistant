from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def get_description(value, dictionary):
    return dictionary.get(value, '')


@register.filter
def get_attribute(obj, attr):
    return getattr(obj, attr, '')