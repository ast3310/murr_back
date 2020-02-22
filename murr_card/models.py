from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

Murren = get_user_model()


class MurrCard(models.Model):
    title = models.CharField(max_length=128)
    cover = models.ImageField(blank=True, upload_to='murren_pics')
    description = models.CharField(max_length=256)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Murren, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EditorImageForMurrCard(models.Model):

    # name = models.CharField(max_length=255)
    murr_editor_image = models.ImageField(upload_to='editor_image_for_murr_card/%Y/%m/%d/', null=True, max_length=255)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.murr_editor_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.murr_editor_image.path)


class EditorDataForMurrCard(models.Model):

    data_for_murr = models.TextField()


# class EditorImageForMurrCard(models.Model):
#
#     # editor_image = models.ImageField(upload_to='editor_image_for_murr_card/%Y/%m/%d/', null=True, blank=True)
#     editor_image = models.FileField(upload_to='editor_image_for_murr_card', null=True, blank=True)
#

