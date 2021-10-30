from django.contrib import admin
from products.models import Product
from category.models import Category

class ProductInline(admin.StackedInline):
    model = Product
    extra = 2


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', ]
    inlines = [ProductInline]


admin.site.register(Category, CategoryAdmin)