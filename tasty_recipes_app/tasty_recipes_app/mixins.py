class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            if field_name == 'ingredients':
                field.help_text = "Ingredients must be separated by a comma and space."
                field.widget.attrs['placeholder'] = "ingredient1, ingredient2, ..."
            if field_name == 'instructions':
                field.widget.attrs['placeholder'] = "Enter detailed instructions here..."
            if 'image' == field_name:
                field.widget.attrs['placeholder'] = "Optional image URL here..."
                field.label = 'Image URL:'
            field.label = f"{field_name.replace('_', ' ').capitalize()}:"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class ReadOnlyMixin:

    def make_fields_readonly(self):
        for field_name, field in self.fields.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()