# image_django
test task - image redactor and uploader,
author Stepura Savelii

###Setting up a virtual environment for a project

> pip install -r requirement.txt

###Run the project on the test server

> python manage.py makemigrations
> 
> python manage.py migrate
> 
> python manage.py runserver

###Project description:

The project takes the image, saves the image to the database, and allows you to resize the image in the editor.


The project accepts both images as a file and as an image link.

There are restrictions on receiving images. The application only accepts a certain image format .jpg .png, it is possible to throw an exception in this process


PS: some tests were done in the test.py file