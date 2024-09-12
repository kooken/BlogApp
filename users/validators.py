from django.core.exceptions import ValidationError
import re


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Your password should be at least 8 symbols')
    if not re.search(r'\d', value):
        raise ValidationError('You password should include at least 1 digit')


def validate_email_domain(value):
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f'Only these domains are allowed: {", ".join(allowed_domains)}.')
