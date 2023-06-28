# tests/test_position.py

from django.test import TestCase
from salsa_app.models import Position, User

class PositionModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(email='testuser@gmail.com', password='testpass123')
        Position.objects.create(name='Test Position', user_id=1)

    def test_name_label(self):
        position = Position.objects.get(id=1)
        field_label = position._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        position = Position.objects.get(id=1)
        max_length = position._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_name(self):
        position = Position.objects.get(id=1)
        expected_object_name = f'{position.name}'
        self.assertEqual(expected_object_name, str(position))
