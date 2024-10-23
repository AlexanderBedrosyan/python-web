from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class UpperValueValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Name must start with a capital letter!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if value[0] != value[0].upper():
            raise ValidationError(self.message)