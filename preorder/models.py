from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Preorder(models.Model):
    client = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
    PRIME_CHOICES = ((True, "Yes"), (False, "No"))
    prime = models.BooleanField(choices=PRIME_CHOICES)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
