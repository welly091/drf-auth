from rest_framework import serializers
from .models import Preorder


class PreorderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('client', 'item', 'prime', 'price', 'created_at')
        model = Preorder