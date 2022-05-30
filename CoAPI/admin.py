from django.contrib import admin
from .models import Coworking, Tariffs, Ticket
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Coworking)
class cowork(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Tariffs)
class tariff(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Ticket)
class ticket(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

