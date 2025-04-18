from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class StartsWithValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must start with a letter!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if value[0].isalpha() is False:
            raise ValidationError(self.message)