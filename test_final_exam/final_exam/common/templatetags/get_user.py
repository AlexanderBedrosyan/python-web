from django import template
from final_exam import utils

register = template.Library()


@register.simple_tag
def get_user():
    return utils.get_user_obj()