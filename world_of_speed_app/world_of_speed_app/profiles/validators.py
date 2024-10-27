from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class CharactersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Username must contain only letters, digits, and underscores!"
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        for ch in value:
            if not ch.lower().isalnum() and ch.lower() != '_':
                raise ValidationError(self.message)