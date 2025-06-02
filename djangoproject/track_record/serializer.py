from rest_framework import serializers
from .models import Track_Record

class TrackRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Track_Record
        fields='__all__'

    def validate(self,data):
        date=data['date']
        followup_date=data['next_followup_date']
        if date and followup_date and followup_date<=date:
            raise serializers.ValidationError('followup date is before than visit date')
        return data