from rest_framework.validators import ValidationError

good_link = 'https://www.youtube.com/'


class SomeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pass



def link_validate(values):
    if good_link not in values:
        raise ValidationError('Ссылка ведет на сторонний ресурс')


