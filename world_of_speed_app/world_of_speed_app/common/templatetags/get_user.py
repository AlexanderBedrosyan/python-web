from django import template
from world_of_speed_app import utils

register = template.Library()


@register.simple_tag
def get_user():
    return utils.get_user_obj()