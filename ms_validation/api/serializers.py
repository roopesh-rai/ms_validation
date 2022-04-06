from rest_framework import serializers
from .models import Student

def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError("Name Must Be Start With R")

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'roopesh' and ct.lower() != 'veraval':
            raise serializers.ValidationError("City Must Be Veraval")
        return data
