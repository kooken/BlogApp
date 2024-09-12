from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@blog.com',
            username='Admin',
            phone='4267894',
            is_active=True,
        )

        user.set_password('12345')
        user.save()
