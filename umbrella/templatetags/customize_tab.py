from django import template
from django.db import connection

register = template.Library()


@register.simple_tag()
def get_db_info():
    return connection.vendor
