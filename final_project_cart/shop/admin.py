from django.contrib import admin

# Register your models here.
from shop.models import catlog,products



class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(catlog,catadmin)

class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodadmin)
