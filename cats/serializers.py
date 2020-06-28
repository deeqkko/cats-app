from .models import Cats
from rest_framework import serializers


class CatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cats
        fields = [
            'cat_name',
            'cat_nicknames',
            'cat_dob',
            'cat_image'
        ]
