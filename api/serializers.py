from rest_framework import serializers
from .models import Object
from datetime import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


class ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = '__all__'    
    
    @classmethod
    def create_object(cls, class_name, confidence):
        try:
            entity = cls.Meta.model.objects.create(
                class_name=class_name,
                confidence=confidence,
                timestamp=timezone.now()
            )

            return {
                "id": entity.id,
                "class_name": entity.class_name,
                "confidence": entity.confidence,
                "timestamp": entity.timestamp
            }
        
        except Exception as e:
            return {"error": f"Could not save data: {str(e)}"}

