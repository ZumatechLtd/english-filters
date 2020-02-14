# -*- coding: utf-8 -*-
# (c) 2015 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com
from django import template
from django.utils.encoding import force_text
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True, needs_autoescape=True)
def join_or(value, autoescape=True):
    """
    Outputs a list as a fragment of English that has "or" in it if the list
    contains more than one item. For example, for [1, 2, 3, 4] will be output
    as "1, 2, 3 or 4".
    """
    return _join_english('or', value, autoescape)


@register.filter(is_safe=True, needs_autoescape=True)
def join_and(value, autoescape=True):
    return _join_english('and', value, autoescape)


def _join_english(word, value, autoescape=True):
    value = list(map(force_text, value))
    if autoescape:
        value = [conditional_escape(v) for v in value]

    if len(value) == 0:
        data = ''
    elif len(value) == 1:
        data = value[0]
    else:
        comma_separated = ', '.join(value[:-1])
        last = value[-1]
        data = (' %s ' % word).join([comma_separated, last])

    return mark_safe(data)
