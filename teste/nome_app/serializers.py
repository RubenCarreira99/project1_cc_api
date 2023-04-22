from rest_framework import serializers
 
# import the todo data model
from .models import Member

# create a serializer class
class MemberSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Member
        fields = ('id', 'firstname','lastname','phone', 'joined_date')