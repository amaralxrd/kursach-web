from urllib.request import Request
from rest_framework.viewsets import ModelViewSet
from .serializers import TicketSerializer, TariffsSerializer, CoworkingSerializer
from .models import Ticket, Tariffs, Coworking
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response


class CoworkingViewSet(ModelViewSet):
    queryset = Coworking.objects.all()
    serializer_class = CoworkingSerializer
    
class TariffsViewSet(ModelViewSet):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer

class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delTicket(self,request, pk=None):
        ticket=self.queryset.get(id=pk)
        ticket.delete()
        return Response('Успешно')

class GetTariffsView(ListAPIView):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['hours']


class GetCoworkingView(ListAPIView):
    queryset = Coworking.objects.filter( Q(work='да') | Q(work='Да') | Q(work='yes') | Q(work='Yes') )
    serializer_class = CoworkingSerializer

