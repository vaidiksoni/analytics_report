# Import the modules
from django.db import models
from jsonfield import JSONField



# Create your models here.
class SaleOrder(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    related_opd_master_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=18, blank=True, null=True)
    opd_number = models.CharField(max_length=255)
    opd_type = models.CharField(max_length=16, blank=True, null=True)
    discount_coupon = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    tnc = models.TextField(blank=True, null=True)
    shipping_address_id = models.PositiveIntegerField(blank=True, null=True)
    billing_address_id = models.PositiveIntegerField(blank=True, null=True)
    tnc_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.PositiveIntegerField()
    vendor_id = models.PositiveIntegerField(blank=True, null=True)
    created_by_id = models.PositiveIntegerField(blank=True, null=True)
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    redeemed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frendy_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_method = models.CharField(max_length=16, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shipping_id = models.PositiveIntegerField(blank=True, null=True)
    dispute_remark = models.TextField(blank=True, null=True)
    dispute_reason = models.CharField(max_length=255, blank=True, null=True)
    package_type_id = models.PositiveIntegerField(blank=True, null=True)
    package_weight = models.IntegerField(blank=True, null=True)
    volumetric_weight = models.IntegerField(blank=True, null=True)
    shipping_partner_id = models.PositiveIntegerField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    awb_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    used_product_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    actual_shipping_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cod_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    actual_cod_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    used_wallet_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    warehouse_id = models.PositiveIntegerField(blank=True, null=True)
    shipping_full_address = models.TextField(blank=True, null=True)
    billing_full_address = models.TextField(blank=True, null=True)
    billing_state_id = models.PositiveIntegerField(blank=True, null=True)
    billing_city_id = models.PositiveIntegerField(blank=True, null=True)
    shipping_state_id = models.PositiveIntegerField(blank=True, null=True)
    shipping_city_id = models.PositiveIntegerField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    return_available_till = models.DateTimeField(blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    igst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    round_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_info = JSONField(blank=True, null =True)  # TextField == This field type is a guess.
    status_activity = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_profile_name = models.CharField(max_length=255, blank=True, null=True)
    keep_star_order = models.IntegerField(blank=True, null=True)
    aggregator_id = models.PositiveIntegerField(blank=True, null=True)
    package_height = models.FloatField(blank=True, null=True)
    package_length = models.FloatField(blank=True, null=True)
    package_width = models.FloatField(blank=True, null=True)
    package_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'
        unique_together = (('awb_number', 'shipping_partner_id'), ('shipping_partner_id', 'awb_number'),)


class SaleOrderItem(models.Model):
    opd_master = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    product_id = models.PositiveIntegerField()
    related_opd_item_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    tax_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=17, blank=True, null=True)
    shipping_method = models.CharField(max_length=16, blank=True, null=True)
    created_by_id = models.PositiveIntegerField(blank=True, null=True)
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frendy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dispute_remark = models.TextField(blank=True, null=True)
    dispute_reason = models.CharField(max_length=255, blank=True, null=True)
    product_points = models.DecimalField(max_digits=10, decimal_places=2)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    tax_percentage = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item_quantity_points = models.DecimalField(max_digits=10, decimal_places=2)
    tax_included_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_excluded_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    product_points_fund = models.DecimalField(max_digits=10, decimal_places=2)
    total_product_points_fund = models.DecimalField(max_digits=10, decimal_places=2)
    used_product_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    return_available_till = models.DateTimeField(blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    igst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    primary_category_id = models.PositiveIntegerField(blank=True, null=True)
    root_category_id = models.PositiveIntegerField(blank=True, null=True)
    primary_category = models.CharField(max_length=255, blank=True, null=True)
    root_category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale_order_item'
    def __str__(self):
        return self.primary_category



