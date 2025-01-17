from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from api.models import User, Contact

class Command(BaseCommand):
   help = 'Popluate the database with sample data'

   def handle(self, *args, **kwargs):
      for _ in range(10):
         username = get_random_string(5)
         phone_number = get_random_string(10, '0123456789')
         email = f'{username}@example.com'
         password = 'password123'

         user = User.objects.create_user(
            username=username,
            phone_number=phone_number,
            email=email,
            password=password
         )

         for _ in range(5):
            contact_name = get_random_string(5)
            contact_phone = get_random_string(10, '0123456789')
            contact_email = f'{contact_name}@example.com'

            Contact.objects.create(
               owner=user,
               name=contact_name,
               phone_number=contact_phone,
               email=contact_email
            )

      self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))