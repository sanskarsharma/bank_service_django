from rest_framework import serializers
from . import models


class BanksSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Banks
        fields = ('id', 'name')


class BranchesSerializer(serializers.ModelSerializer):

    bank = BanksSerializer(read_only=True)

    class Meta:
        model = models.Branches
        fields = ('ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state')


