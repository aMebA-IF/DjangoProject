from django.test import TestCase
from django.test import TestCase
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from django.test.client import Client, RequestFactory

User = get_user_model()
class PlaceTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username = 'Ilya', password = '12345')
        self.place = Place.objects.create(
            name = 'Sochi',
            comment = 'Beautiful',
            latitude = 43.60617507208267,
            longitude =  39.724955299773654,
            profile = self.user.profile
        )

    def test_addplace(self):
        self.assertIn(self.place, self.user.profile.places.all())

    def test_UserForm_valid(self):
        form = PlaceForm(data={'name': "Sochi", 'comment': "Beautiful", 'latitude': "43.60617507208267", 'longitude': 39.724955299773654})
        self.assertTrue(form.is_valid())

    def test_CreateView(self):
        context = {'place':self.place}
        c = Client()
        c.post('create', context)




