from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
    # for the ImageField we must install the pillow package (pip install Pillow)
    # This accepts only images.

    # image = models.FileField(upload_to="images")
    # "FileField" will NOT store the file in the database, instead it will store the file on the hard-disk and in the database it will store the path of that file
    # Based on the MEDIA_ROOT setting from the settings.py it will store the file in the indicated folder