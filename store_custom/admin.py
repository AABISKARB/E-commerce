from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from store.admin import ProductAdmin
from tags.models import TaggedItem
from store.models import Product

class TagInline(GenericStackedInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)