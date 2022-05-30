from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, TariffsViewSet, CoworkingViewSet, GetTariffsView, GetCoworkingView
router = DefaultRouter()
router.register('tarrifs', TariffsViewSet, )
router.register('coworking', CoworkingViewSet, )
router.register('ticket', TicketViewSet, )




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tarrifs/filter', GetTariffsView.as_view()),
    path('api/coworking/filter', GetCoworkingView.as_view()),
]
