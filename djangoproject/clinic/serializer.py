from rest_framework import serializers
from .models import Clinic

class Clinic_serializer(serializers.ModelSerializer):
    class Meta:
        model=Clinic
        fields="__all__"

    def validate(self,attributes):
        name=attributes.get('name')
        contact_number=attributes.get('contact_number')
        opening_time = attributes.get('opening_time') or (self.instance.opening_time if self.instance else None)
        closing_time = attributes.get('closing_time') or (self.instance.closing_time if self.instance else None)

        if Clinic.objects.filter(name=name,contact_number=contact_number).exists():
            raise serializers.ValidationError(f'Clinic with "{name}" and "{contact_number}" already exists')
        if opening_time and closing_time and closing_time<=opening_time:
            raise serializers.ValidationError('Closing time should be after opening time')
        return(attributes)