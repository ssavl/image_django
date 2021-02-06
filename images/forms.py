import random
import string
from io import BytesIO
from urllib import request

import requests
from django import forms
from django.core.exceptions import ValidationError
from django.core.files import File

from images.models import Image
from PIL import Image as PillowImage


class ImageUploadForm(forms.Form):
    url = forms.CharField(required=False)
    image = forms.ImageField(required=False)

    def clean(self):
        res = super().clean()
        if res['image'] and res['url']:
            raise ValidationError("Only one field has to be specified")
        if not res['image'] and not res['url']:
            raise ValidationError("Specify at least one field")
        return res

    def save(self):
        if self.cleaned_data['url']:
            name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
            result = request.urlretrieve(self.cleaned_data['url'], f'{name}.jpg')
            image = File(open(result[0], 'rb'))
        else:
            image = self.cleaned_data['image']
        return Image.objects.create(image=image)


class ImageEditForm(forms.Form):
    x_axis = forms.IntegerField(required=False)
    y_axis = forms.IntegerField(required=False)

    def __init__(self, data=None, ratio=None):
        super().__init__(data)
        self.ratio = ratio

    def clean(self):
        res = super().clean()
        if res['x_axis'] and not res['y_axis']:
            res['y_axis'] = int(res['x_axis'] / self.ratio)
        if not res['x_axis'] and res['y_axis']:
            res['x_axis'] = int(res['y_axis'] * self.ratio)
        return res
