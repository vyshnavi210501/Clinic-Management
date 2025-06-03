from rest_framework import serializers
from .models import Therapist

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Therapist
        fields='__all__'

    def validate(self, attrs):
        start = attrs.get('start_time') or (self.instance.start_time if self.instance else None)
        end = attrs.get('end_time') or (self.instance.end_time if self.instance else None)
        if start and end and end < start:
            raise serializers.ValidationError("End time must be greater than start time")
        return attrs


