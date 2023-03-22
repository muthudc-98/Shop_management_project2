from django.contrib import admin

from shopapp.models import Shopview 

class Shopadmin(admin.ModelAdmin):
	list_display=['name','quantity','price']

admin.site.register(Shopview,Shopadmin)
