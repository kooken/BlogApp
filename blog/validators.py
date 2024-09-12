from django.core.exceptions import ValidationError
from datetime import date


def validate_age(user):
    if user.date_of_birth:
        age = date.today().year - user.date_of_birth.year
        if date.today() < date(user.date_of_birth.year, date.today().month, date.today().day):
            age -= 1
        if age < 18:
            raise ValidationError('Post author should be at least 18 years old!')
    else:
        raise ValidationError("Date of birth isn't in the users profile")


def validate_title(value):
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    if any(word in value.lower() for word in forbidden_words):
        raise ValidationError('Title contains forbidden words')
