from rest_framework import serializers

from phones.models import Phone


class PhoneSerializer(serializers.ModelSerializer):
        class Meta:
            model = Phone
            fields = ['id','name','price','release_date']