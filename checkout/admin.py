from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):

    model = OrderLineItem

    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdmin,)

    readonly_fields = (
        'order_id', 'order_date', 'delivery_cost',
        'order_sub_total', 'order_grand_total',
        'original_bag',
        'stripe_pid')

    fields = (
        'order_id', 'user_profile', 'order_date', 'full_name',
        'email', 'contact_number', 'street_address1',
        'street_address2', 'town_or_city', 'county',
        'country', 'postcode', 'delivery_cost',
        'order_sub_total', 'order_grand_total',
        'original_bag',
        'stripe_pid')

    list_display = (
        'order_id', 'order_date', 'full_name',
        'delivery_cost', 'order_sub_total',
        'order_grand_total', )

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)