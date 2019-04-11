from django.contrib import admin

# Register your models here.
from Entity.models import Entity,WorkOrder,OrderLot


class EntityDisplay(admin.ModelAdmin):
	search_fields  = ('date1','entity',)
	ordering = ['-date1','entity']
	list_display =  ('date1','entity','lot_no','current_status')


class WorkOrderDisplay(admin.ModelAdmin):
	search_fields  = ('order_no',)
	ordering = ['-date1',]
	list_display =  ('date1','order_no')
	
class OrderLotDisplay(admin.ModelAdmin):
	search_fields  = ('entity','lot_no')
	ordering = ['-order_no',]
	list_display =  ('order_no','lot_no','entity','current_status','finish'	)	



admin.site.register(Entity,EntityDisplay)
admin.site.register(WorkOrder,WorkOrderDisplay)
admin.site.register(OrderLot,OrderLotDisplay)