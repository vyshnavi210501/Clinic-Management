from rest_framework import serializers
from .models import Clinic

class Clinic_serializer(serializers.ModelSerializer):
    class Meta:
        model=Clinic
        fields="__all__"

    def validate(self,attributes):
        name=attributes.get('name') or (self.instance.name if self.instance else None)
        contact_number=attributes.get('contact_number') or (self.instance.contact_number if self.instance else None)
        opening_time = attributes.get('opening_time') or (self.instance.opening_time if self.instance else None)
        closing_time = attributes.get('closing_time') or (self.instance.closing_time if self.instance else None)
        #here self.instance is the None for newly creating objects and for existing ones it returns whole object for ex if in api call we
        #  give put call and for id=5 then wtever object we get for that id it stores in self.instance.so its used for put/patch calls

        existing_clinics = Clinic.objects.filter(name=name, contact_number=contact_number)
        if self.instance:
            existing_clinics = existing_clinics.exclude(id=self.instance.id)

        if existing_clinics.exists():
            raise serializers.ValidationError({
                "name": f'Clinic with name "{name}" and contact "{contact_number}" already exists.'
            })
        if opening_time and closing_time and closing_time<=opening_time:
            raise serializers.ValidationError('Closing time should be after opening time')
        return(attributes)