class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = ''
            if field_name == 'first_name':
                placeholder = "Enter your first name..."
            elif field_name == 'last_name':
                placeholder = "Enter your last name..."
            elif field_name == 'passcode':
                placeholder = "Enter 6 digits..."
            elif field_name == "pets_number":
                placeholder = "Enter the number of your pets..."
            field.widget.attrs['placeholder'] = placeholder
            field.label = field.label.title()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class ReadOnlyMixin:
    def make_fields_readonly(self):
        for field_name, field in self.fields.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()