from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create your models here.


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # for idenetifying the type of the object that user likes. # eg If user likes video, image, boutique
    object_id = models.PositiveIntegerField()
    # for referencing that particular object. # eg video
    content_object = GenericForeignKey()
    # for reading that actual object.
