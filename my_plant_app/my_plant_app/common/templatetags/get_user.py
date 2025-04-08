from django import template
from my_plant_app import utils

register = template.Library()


@register.simple_tag
def get_user():
    return utils.get_user_obj()
