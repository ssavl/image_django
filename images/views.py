import random
import string

from django.http import FileResponse
from django.shortcuts import render, redirect

# Create your views here.
from images.forms import ImageUploadForm, ImageEditForm
from images.models import Image
from PIL import Image as PillowImage


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/upload')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def edit_image(request, pk):
    image_object = Image.objects.get(pk=pk)
    image_url = image_object.image.url
    if request.method == 'POST':
        image = PillowImage.open(image_object.image)
        x, y = image.size
        original_ratio = x / y

        form = ImageEditForm(request.POST, ratio=original_ratio)
        if form.is_valid():
            image = image.resize((form.cleaned_data['x_axis'], form.cleaned_data['y_axis']))
            path = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
            image.save(f'media/images/{path}.jpg')
            image_url = f'/media/images/{path}.jpg'
    else:
        form = ImageEditForm()
    return render(request, 'resize-detail.html', {'image_url': image_url, 'form': form})


def list_images(request):
    return render(request, 'list.html', {'images': Image.objects.all()})
