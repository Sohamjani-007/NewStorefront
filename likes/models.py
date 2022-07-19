from django.db import models
import uuid
from model_utils.models import TimeStampedModel
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

class ShowExcel(models.Model):
    USER_REVIEW = "USER_REVIEW"          
    EXPERT_REVIEW = "EXPERT_REVIEW"
    OVERVIEW = "OVERVIEW"

    SPLIT_CHOICES = [
        (USER_REVIEW, 'user_review'),
        (EXPERT_REVIEW, 'expert_review'),
        (OVERVIEW, 'overview'),
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    video = models.CharField(max_length=100)
    audio = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    language_id = models.CharField(max_length=100)
    type =  models.CharField(max_length=30, choices=SPLIT_CHOICES)
    variant_id = models.CharField(max_length=100)

class OutletQuoteCategory(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    l0 = models.JSONField(null=True)
    l1 = models.JSONField(null=True)
    l2 = models.JSONField(null=True)
    l3 = models.JSONField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'outlet_quote_category'

