from rest_framework.validators import ValidationError

good_link = 'https://www.youtube.com/'


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if good_link not in tmp_val:
            raise ValidationError('Ссылка ведет на сторонний ресурс')


#def link_validate(values):
#    if good_link not in values:
#        raise ValidationError('Ссылка ведет на сторонний ресурс')


