from django.test import TestCase

# Create your tests here.
from images.models import Image


class TestImageUpload(TestCase):

    def test_image_uploads(self):
        self.assertFalse(Image.objects.exists())

        with open('media/images/test_image.png', 'rb') as image:
            r = self.client.post('/upload', data={'image': image})

        self.assertTrue(Image.objects.exists())
