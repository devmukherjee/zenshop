from django.contrib import admin
from .models import Product,Order
# Register your models here.




admin.site.site_header= "Zenshop Admin"
admin.site.site_title= "Zenshop"
admin.site.index_title= "Manage Zenshop"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="Default")

    change_category_to_default.short_description="Default Category"
    list_display= ('title','price','discount_price','category','description')
    search_fields= ('title','description','category')
    actions= ('change_category_to_default',)
    list_editable=('price','category')

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)