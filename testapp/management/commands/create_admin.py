from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create initial superuser"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "dell"
        password = "precision@123"
        email = "bhagyeshyadav@gmail.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write("Superuser already exists")
