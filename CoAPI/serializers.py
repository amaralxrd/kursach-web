from rest_framework.serializers import ModelSerializer
from .models import Tariffs, Ticket, Coworking


class TariffsSerializer(ModelSerializer):
    class Meta:
        model = Tariffs
        fields = '__all__'

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class CoworkingSerializer(ModelSerializer):
    class Meta:
        model = Coworking
        fields = '__all__'