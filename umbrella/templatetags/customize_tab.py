from django.db import connection
from django import template
from django import db


register = template.Library()


@register.simple_tag()
def get_db_info():
    return connection.vendor


