from django.db import models
from django.utils import timezone

# Create your models here.

class EntityManager (models.Manager):
	def create_post(self,date1,entity,lot_no,current_status,status_history):
		post = self.create(date1=date1,entity=entity,lot_no = lot_no,current_status = current_status,status_history=status_history)
		return post


class Entity(models.Model):
	id =  models.AutoField(primary_key=True)
	date1 = models.DateField(default= timezone.now,verbose_name ='日期') 
	entity = models.CharField(max_length=200,verbose_name ='機台')
	lot_no = models.CharField(max_length=20,verbose_name='批號',blank = True,null = True)
	current_status = models.TextField(blank = True,null = True,verbose_name='機況' )
	status_history = models.TextField(blank = True,null = True,verbose_name='歷史機況' )
	obj = EntityManager()
	
	class Meta:
		ordering = ('-date1',)
	
	def __str__(self):
		return self.entity
	
	def decade_date(self):
		datestr =  self.date1.strftime('%Y/%m/%d')
		return datestr
		

class WorkOrder(models.Model):
	id =  models.AutoField(primary_key=True)
	date1 = models.DateField(default= timezone.now) 
	order_no = models.CharField(max_length=200)
	class Meta:
		ordering = ('-date1',)

	def __str__(self):
		return self.order_no


class OrderLot(models.Model):
	id = models.AutoField(primary_key=True)
	order_no = models.ForeignKey('WorkOrder',on_delete = models.CASCADE) 
	lot_no = models.CharField(max_length=20,verbose_name='批號',blank = True,null = True)
	entity = models.CharField(max_length=20,verbose_name='機台',blank = True,null = True)
	current_status = models.ForeignKey('Entity',on_delete = models.CASCADE,verbose_name='機況',blank = True,null = True)
	product_status = models.CharField(max_length=200,verbose_name='現況',blank = True,null = True)
	finish = models.BooleanField (default = False,verbose_name='採收')
	
	class Meta:
		ordering = ('-order_no',)

	def __str__(self):
		return self.lot_no
	