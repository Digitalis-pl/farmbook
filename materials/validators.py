from rest_framework.validators import ValidationError

good_link = 'https://www.youtube.com/'


def link_validate(values):
    if good_link not in values:
        raise ValidationError('Ссылка ведет на сторонний ресурс')
