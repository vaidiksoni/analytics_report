# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AclPermission(models.Model):
    role = models.ForeignKey('Profile', models.DO_NOTHING)
    acl_type = models.CharField(max_length=255)
    can_add = models.IntegerField()
    acl = models.TextField()

    class Meta:
        managed = False
        db_table = 'acl_permission'


class ActivityLog(models.Model):
    user_id = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    page_url = models.TextField(blank=True, null=True)
    primary_id = models.IntegerField()
    model_class = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    log_action = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_log'


class Address(models.Model):
    billing_city_id = models.IntegerField(blank=True, null=True)
    billing_state_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    billing_country = models.CharField(max_length=10, blank=True, null=True)
    alias = models.CharField(max_length=50, blank=True, null=True)
    billing_address_line_1 = models.TextField(blank=True, null=True)
    billing_address_line_2 = models.TextField(blank=True, null=True)
    billing_pincode = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    is_default = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    shipping_address_line_1 = models.TextField(blank=True, null=True)
    shipping_address_line_2 = models.TextField(blank=True, null=True)
    shipping_city_id = models.IntegerField(blank=True, null=True)
    shipping_country = models.CharField(max_length=10, blank=True, null=True)
    shipping_pincode = models.CharField(max_length=255, blank=True, null=True)
    shipping_state_id = models.IntegerField(blank=True, null=True)
    shipping_gstin = models.CharField(max_length=255, blank=True, null=True)
    billing_gstin = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    mobile_optional = models.CharField(max_length=10, blank=True, null=True)
    billing_landmark = models.CharField(max_length=255, blank=True, null=True)
    shipping_landmark = models.CharField(max_length=255, blank=True, null=True)
    shipping_name = models.TextField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'address'


class AttrSpecDetailInLang(models.Model):
    lang = models.ForeignKey('Lang', models.DO_NOTHING)
    attribute_specification = models.ForeignKey('AttributeSpecification', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attr_spec_detail_in_lang'
        unique_together = (('lang', 'attribute_specification'),)


class AttributeGroup(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_group'


class AttributeSpecification(models.Model):
    group_type = models.CharField(max_length=9, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=13)
    value = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_visible = models.IntegerField(blank=True, null=True)
    is_filterable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_specification'


class Barcode(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    barcode = models.CharField(unique=True, max_length=255, blank=True, null=True)
    is_available = models.IntegerField()
    to_bin = models.ForeignKey('Container', models.DO_NOTHING, blank=True, null=True)
    to_warehouse = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    is_qcfail = models.IntegerField()
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode'


class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True)
    meta_description = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by_id = models.PositiveIntegerField()
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Carrier(models.Model):
    is_free = models.IntegerField(blank=True, null=True)
    max_length = models.FloatField()
    max_width = models.FloatField()
    max_depth = models.FloatField()
    volumetric_factor = models.IntegerField(blank=True, null=True)
    tracking_url = models.CharField(max_length=255, blank=True, null=True)
    enable_api = models.IntegerField()
    is_reverse_shipment = models.IntegerField()
    registered_user_name = models.CharField(max_length=255, blank=True, null=True)
    aggregator_carrier_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier'


class CarrierAggregator(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier_aggregator'


class CarrierAwbnumber(models.Model):
    awb_number = models.CharField(max_length=255)
    is_used = models.IntegerField()
    status = models.CharField(max_length=8)
    package = models.ForeignKey('Package', models.DO_NOTHING, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrier_awbnumber'
        unique_together = (('awb_number', 'carrier'),)


class Cart(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    attributes = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantity = models.IntegerField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frendy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_points = models.DecimalField(max_digits=10, decimal_places=2)
    combo_dataset_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class CashWithdrawal(models.Model):
    wallet_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawal_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tds_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tds_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transferred_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bank_id = models.IntegerField(blank=True, null=True)
    transfer_id = models.CharField(max_length=255, blank=True, null=True)
    transfer_to_bank = models.CharField(max_length=255, blank=True, null=True)
    transfer_date = models.DateTimeField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    inprogress_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    canceled_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    completed_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    inprogress_at = models.DateTimeField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    bank_info = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cash_withdrawal'


class Category(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    attribute_group_id = models.PositiveIntegerField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    children = models.TextField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    sizechart_variable = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    is_root = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    cover_image_url = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_image_url = models.CharField(max_length=255, blank=True, null=True)
    sequence_order = models.TextField(blank=True, null=True)
    is_popular = models.IntegerField()
    is_app_root_category = models.IntegerField()
    app_layout = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    include_subcategory_specification_in_filter = models.IntegerField(blank=True, null=True)
    include_subcategory_attribute_in_filter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryDetailInLanguage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    meta_name = models.CharField(max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    lang_id = models.PositiveIntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name_with_parent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_detail_in_language'
        unique_together = (('lang_id', 'category'),)


class City(models.Model):
    name = models.CharField(max_length=50)
    state_id = models.PositiveIntegerField()
    status = models.CharField(max_length=8)
    created_by_id = models.PositiveIntegerField()
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('id', 'state_id'), ('state_id', 'name'),)


class CmsBanner(models.Model):
    name = models.CharField(max_length=255)
    heading = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    lang = models.ForeignKey('Lang', models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_banner'


class CmsBannerImages(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    alt_tags = models.CharField(max_length=255, blank=True, null=True)
    cms_banner = models.ForeignKey(CmsBanner, models.DO_NOTHING, blank=True, null=True)
    analytics_title = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sequence_no = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_banner_images'


class ColorHexcode(models.Model):
    id = models.BigAutoField(primary_key=True)
    attribute_id = models.PositiveIntegerField(blank=True, null=True)
    color_identifier = models.CharField(max_length=255)
    hexcode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'color_hexcode'


class Communication(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sub_type_1 = models.CharField(max_length=255, blank=True, null=True)
    sub_type_2 = models.CharField(max_length=255, blank=True, null=True)
    sub_type_3 = models.CharField(max_length=255, blank=True, null=True)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    from_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    to_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication'


class CommunicationRead(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING, blank=True, null=True)
    communication = models.ForeignKey(Communication, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communication_read'


class CommunityLeaderSlab(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    self_monthly_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    community_monthly_min_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    community_monthly_max_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    group_commision = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_leader_slab'


class Container(models.Model):
    rack_id = models.IntegerField(blank=True, null=True)
    shelf_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    type = models.CharField(max_length=5)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    container_type = models.CharField(max_length=255, blank=True, null=True)
    sync_inventory = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'container'


class CustomerEvent(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    event_class = models.CharField(max_length=255)
    method_name = models.CharField(max_length=255)
    arguments = models.TextField()
    remark = models.TextField()
    priority = models.IntegerField()
    event_distribute = models.CharField(max_length=24, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_event'


class DataSet(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    analytics_title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    based_on = models.CharField(max_length=9, blank=True, null=True)
    display_title = models.CharField(max_length=255, blank=True, null=True)
    is_combo = models.IntegerField()
    sorting = models.CharField(max_length=21)

    class Meta:
        managed = False
        db_table = 'data_set'


class DataSetBrands(models.Model):
    order = models.IntegerField()
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    data_set = models.ForeignKey(DataSet, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    redirect_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_set_brands'


class DataSetCategories(models.Model):
    order = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    data_set = models.ForeignKey(DataSet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_set_categories'


class DataSetFilterConditions(models.Model):
    field = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    attribute = models.TextField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    condition_type = models.CharField(max_length=3, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    data_set = models.ForeignKey(DataSet, models.DO_NOTHING, blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_set_filter_conditions'


class DataSetGroup(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    data_set_ids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_set_group'


class DataSetProducts(models.Model):
    order = models.IntegerField()
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    data_set = models.ForeignKey(DataSet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_set_products'


class EmployeeCategoryAssociation(models.Model):
    employee = models.ForeignKey('User', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    include_sub_category = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_category_association'


class EmployeeWarehouseAssociation(models.Model):
    employee = models.ForeignKey('User', models.DO_NOTHING)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_warehouse_association'


class EventCountTracker(models.Model):
    event = models.ForeignKey(CustomerEvent, models.DO_NOTHING, blank=True, null=True)
    event_effecting_game_level = models.ForeignKey('GameLevel', models.DO_NOTHING, blank=True, null=True)
    event_effecting_game_stage = models.ForeignKey('GameStage', models.DO_NOTHING, blank=True, null=True)
    event_effecting_membership = models.ForeignKey('Membership', models.DO_NOTHING, blank=True, null=True)
    event_effecting_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    event_source_user_id = models.PositiveIntegerField(blank=True, null=True)
    event_source_game_level_id = models.PositiveIntegerField(blank=True, null=True)
    event_source_game_stage_id = models.PositiveIntegerField(blank=True, null=True)
    event_source_membership_id = models.PositiveIntegerField(blank=True, null=True)
    event_count = models.IntegerField(blank=True, null=True)
    is_unique_to_each_user = models.IntegerField(blank=True, null=True)
    tag_1 = models.CharField(max_length=255, blank=True, null=True)
    group_event_name = models.CharField(max_length=255, blank=True, null=True)
    is_bonus = models.IntegerField()
    status = models.CharField(max_length=8)
    happened_at_level = models.CharField(max_length=2)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    arguments_1 = models.CharField(max_length=255, blank=True, null=True)
    arguments_1_condition = models.CharField(max_length=7, blank=True, null=True)
    arguments_1_value_1 = models.CharField(max_length=255, blank=True, null=True)
    arguments_1_value_2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_count_tracker'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Faq(models.Model):
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    faq_topics = models.ForeignKey('FaqTopics', models.DO_NOTHING, blank=True, null=True)
    lang = models.ForeignKey('Lang', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faq'


class FaqTopics(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    lang = models.ForeignKey('Lang', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)
    display_in_general = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_topics'


class FrendyCeConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frendy_ce_config'


class FundDistribution(models.Model):
    event_id = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    arguments_1 = models.TextField(blank=True, null=True)
    arguments_1_condition = models.CharField(max_length=7, blank=True, null=True)
    arguments_1_value_1 = models.TextField(blank=True, null=True)
    arguments_1_value_2 = models.TextField(blank=True, null=True)
    completes_stage_on_count = models.IntegerField(blank=True, null=True)
    conditional_tag_1_value_from = models.CharField(max_length=8, blank=True, null=True)
    conditional_tag_1_argument_param = models.TextField(blank=True, null=True)
    conditional_tag_1_value = models.TextField(blank=True, null=True)
    run_at = models.TextField(blank=True, null=True)
    is_unique_to_each_user = models.IntegerField(blank=True, null=True)
    manage_new_group_event_count = models.IntegerField(blank=True, null=True)
    for_group_event_set_tag_1_from = models.CharField(max_length=8, blank=True, null=True)
    for_group_event_tag_1_argument_param = models.TextField(blank=True, null=True)
    for_group_event_set_tag_1_value = models.TextField(blank=True, null=True)
    skip_fields_to_set_for_group = models.TextField(blank=True, null=True)
    initial_value = models.IntegerField(blank=True, null=True)
    is_bonus = models.IntegerField(blank=True, null=True)
    cash_type = models.CharField(max_length=10, blank=True, null=True)
    cash = models.IntegerField(blank=True, null=True)
    cash_percentage_of_argument = models.TextField(blank=True, null=True)
    points_type = models.CharField(max_length=10, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    points_percentage_of_argument = models.TextField(blank=True, null=True)
    invites = models.IntegerField(blank=True, null=True)
    fire_sub_event = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    source_membership_id = models.IntegerField(blank=True, null=True)
    source_game_level_id = models.IntegerField(blank=True, null=True)
    source_game_stage_id = models.IntegerField(blank=True, null=True)
    effecting_membership_id = models.IntegerField(blank=True, null=True)
    effecting_game_level_id = models.IntegerField(blank=True, null=True)
    effecting_game_stage_id = models.IntegerField(blank=True, null=True)
    effecting_level = models.CharField(max_length=2)
    completes_stage_id = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    start_datetime = models.CharField(max_length=255, blank=True, null=True)
    end_datetime = models.CharField(max_length=255, blank=True, null=True)
    increase_group_event_counter = models.CharField(max_length=255, blank=True, null=True)
    group_condition_name_from = models.CharField(max_length=255, blank=True, null=True)
    group_condition_name_value = models.CharField(max_length=255, blank=True, null=True)
    group_condition_skip_fields = models.TextField(blank=True, null=True)
    for_group_event_set_name_from = models.CharField(max_length=255, blank=True, null=True)
    for_group_event_name_argument_param = models.CharField(max_length=255, blank=True, null=True)
    for_group_event_set_name_value = models.CharField(max_length=255, blank=True, null=True)
    group_event_name = models.CharField(max_length=255, blank=True, null=True)
    group_condition_name_argument_param = models.CharField(max_length=255, blank=True, null=True)
    group_run_at = models.CharField(max_length=255, blank=True, null=True)
    increase_group_count_if_event_runs = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    wallet_log_status = models.CharField(max_length=8, blank=True, null=True)
    pre_action_sub_event = models.CharField(max_length=255, blank=True, null=True)
    post_action_sub_event = models.CharField(max_length=255, blank=True, null=True)
    action_based_on = models.CharField(max_length=23, blank=True, null=True)
    increase_event_counter = models.IntegerField(blank=True, null=True)
    display_message = models.TextField(blank=True, null=True)
    notification_run = models.IntegerField(blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    send_email = models.IntegerField(blank=True, null=True)
    send_push_notication = models.IntegerField(blank=True, null=True)
    sms_template_id = models.PositiveIntegerField(blank=True, null=True)
    email_template_id = models.PositiveIntegerField(blank=True, null=True)
    push_notification_template_id = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fund_distribution'


class GameLevel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    badge = models.CharField(max_length=7, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    days_to_complete = models.IntegerField(blank=True, null=True)
    days_based_on = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_reward_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_level'


class GameStage(models.Model):
    game_level = models.ForeignKey(GameLevel, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    stage_display_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_stage'


class GroupAttributes(models.Model):
    status = models.CharField(max_length=8)
    value = models.TextField(blank=True, null=True)
    attribute = models.ForeignKey(AttributeSpecification, models.DO_NOTHING, blank=True, null=True)
    attribute_group = models.ForeignKey(AttributeGroup, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_attributes'


class GroupOrder(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2)
    actual_order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_order'


class InternalComment(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING, blank=True, null=True)
    comment_type = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_comment'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Lang(models.Model):
    name = models.CharField(unique=True, max_length=50)
    status = models.CharField(max_length=8)
    iso_code = models.CharField(max_length=10)
    lang_code = models.CharField(max_length=10)
    locale = models.CharField(max_length=10)
    is_rtl = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    icon_url = models.CharField(max_length=255, blank=True, null=True)
    lang_color = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang'


class LayoutRule(models.Model):
    pincode = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    request_banner = models.ForeignKey(CmsBanner, models.DO_NOTHING, blank=True, null=True)
    response_banner = models.ForeignKey(CmsBanner, models.DO_NOTHING, blank=True, null=True)
    request_dataset_group = models.ForeignKey(DataSetGroup, models.DO_NOTHING, blank=True, null=True)
    response_dataset_group = models.ForeignKey(DataSetGroup, models.DO_NOTHING, blank=True, null=True)
    zone_id = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_rule'


class LogisticPincodeAssociation(models.Model):
    pincode = models.ForeignKey('Pincode', models.DO_NOTHING, blank=True, null=True)
    carrier = models.ForeignKey(Carrier, models.DO_NOTHING, blank=True, null=True)
    is_cod_available = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_reverse_available = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'logistic_pincode_association'


class Manifest(models.Model):
    name = models.CharField(max_length=255)
    scanned_copy_of_manifest = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=14)
    shipping_partner = models.ForeignKey(Carrier, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    vendor = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    status_activity = models.TextField(blank=True, null=True)  # This field type is a guess.
    aggregator = models.ForeignKey(CarrierAggregator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifest'
        unique_together = (('aggregator', 'shipping_partner', 'name'),)


class ManifestPackage(models.Model):
    package = models.ForeignKey('Package', models.DO_NOTHING)
    manifest = models.ForeignKey(Manifest, models.DO_NOTHING)
    aggregator_order_id = models.CharField(max_length=255, blank=True, null=True)
    aggregator_shipment_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manifest_package'


class Media(models.Model):
    file_uri = models.CharField(max_length=1000)
    mime_type = models.CharField(max_length=50)
    status = models.CharField(max_length=8)
    meta = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    product_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sequence_no = models.PositiveIntegerField(blank=True, null=True)
    product_definition_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'


class MediaDescription(models.Model):
    description = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    lang = models.ForeignKey(Lang, models.DO_NOTHING)
    media = models.ForeignKey(Media, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_description'


class MediaLibrary(models.Model):
    file_uri = models.CharField(max_length=1000)
    mime_type = models.CharField(max_length=50)
    status = models.CharField(max_length=8)
    meta = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_library'


class Membership(models.Model):
    name = models.CharField(max_length=190)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class NotificationEvents(models.Model):
    name = models.CharField(max_length=255)
    send_email = models.IntegerField()
    email_template = models.ForeignKey('NotificationTemplate', models.DO_NOTHING, blank=True, null=True)
    send_sms = models.IntegerField()
    sms_template = models.ForeignKey('NotificationTemplate', models.DO_NOTHING, blank=True, null=True)
    send_push_notification = models.IntegerField()
    push_notification_template = models.ForeignKey('NotificationTemplate', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    identifier = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_events'


class NotificationLog(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    template = models.ForeignKey('NotificationTemplate', models.DO_NOTHING)
    remark = models.TextField(blank=True, null=True)
    notification_type = models.CharField(max_length=17)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_log'


class NotificationTemplate(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    template_type = models.CharField(max_length=17)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_template'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField(blank=True, null=True)
    client_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField()
    client_id = models.PositiveIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class OpdItemsTodelete(models.Model):
    opd_master = models.ForeignKey('OpdMasterTodelete', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    related_opd_item_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    tax_id = models.PositiveIntegerField(blank=True, null=True)
    status = models.CharField(max_length=17, blank=True, null=True)
    shipping_method = models.CharField(max_length=16, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'opd_items_todelete'


class OpdMasterTodelete(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    related_opd_master_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=18, blank=True, null=True)
    opd_number = models.CharField(max_length=255)
    opd_type = models.CharField(max_length=16, blank=True, null=True)
    discount_coupon = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    tnc = models.TextField(blank=True, null=True)
    shipping_address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    billing_address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    tnc_id = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    vendor = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
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
    package_type = models.ForeignKey('PackageType', models.DO_NOTHING, blank=True, null=True)
    package_weight = models.IntegerField(blank=True, null=True)
    volumetric_weight = models.IntegerField(blank=True, null=True)
    shipping_partner = models.ForeignKey(Carrier, models.DO_NOTHING, blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    awb_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    used_product_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    actual_shipping_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cod_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    actual_cod_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    used_wallet_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    shipping_full_address = models.TextField(blank=True, null=True)
    billing_full_address = models.TextField(blank=True, null=True)
    billing_state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    billing_city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    shipping_state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    shipping_city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    return_available_till = models.DateTimeField(blank=True, null=True)
    sgst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    igst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    round_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    status_activity = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_profile_name = models.CharField(max_length=255, blank=True, null=True)
    keep_star_order = models.IntegerField(blank=True, null=True)
    aggregator = models.ForeignKey(CarrierAggregator, models.DO_NOTHING, blank=True, null=True)
    package_height = models.FloatField(blank=True, null=True)
    package_length = models.FloatField(blank=True, null=True)
    package_width = models.FloatField(blank=True, null=True)
    package_depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opd_master_todelete'
        unique_together = (('awb_number', 'shipping_partner'), ('shipping_partner', 'awb_number'),)


class OrderReturn(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    opd_master = models.ForeignKey('SaleOrder', models.DO_NOTHING)
    opd_item = models.ForeignKey('SaleOrderItem', models.DO_NOTHING)
    return_reason = models.CharField(max_length=255, blank=True, null=True)
    return_remark = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    attachment_1 = models.CharField(max_length=255, blank=True, null=True)
    attachment_2 = models.CharField(max_length=255, blank=True, null=True)
    attachment_3 = models.CharField(max_length=255, blank=True, null=True)
    attachment_4 = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    awb_number = models.CharField(max_length=255, blank=True, null=True)
    shipping_partner = models.ForeignKey(Carrier, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('Package', models.DO_NOTHING, blank=True, null=True)
    tracking_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    return_number = models.CharField(max_length=255, blank=True, null=True)
    is_self_shipment = models.IntegerField(blank=True, null=True)
    pickup_date = models.DateTimeField(blank=True, null=True)
    qc_passed_qty = models.IntegerField(blank=True, null=True)
    qc_failed_qty = models.IntegerField(blank=True, null=True)
    qc_failed_reason = models.TextField(blank=True, null=True)
    cancel_reason = models.TextField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    warehouse_full_address = models.TextField(blank=True, null=True)
    pickup_full_address = models.TextField(blank=True, null=True)
    warehouse = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    payment_quantity = models.IntegerField(blank=True, null=True)
    payment_mode = models.TextField(blank=True, null=True)
    is_rto = models.IntegerField(blank=True, null=True)
    shipment_charge = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    actual_shipment_charge = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    received_other_item = models.IntegerField(blank=True, null=True)
    actual_return_product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    status_activity = models.TextField(blank=True, null=True)
    aggregator = models.ForeignKey(CarrierAggregator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_return'


class OrderReturnBarcodeDetail(models.Model):
    barcode = models.TextField(blank=True, null=True)
    is_qc_failed = models.IntegerField(blank=True, null=True)
    qc_failed_reason = models.CharField(max_length=255, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    attachment_1 = models.CharField(max_length=255, blank=True, null=True)
    attachment_2 = models.CharField(max_length=255, blank=True, null=True)
    attachment_3 = models.CharField(max_length=255, blank=True, null=True)
    is_saleable = models.IntegerField(blank=True, null=True)
    item_not_received = models.IntegerField(blank=True, null=True)
    order_return = models.ForeignKey(OrderReturn, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_return_barcode_detail'


class Package(models.Model):
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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'package'
        unique_together = (('awb_number', 'shipping_partner_id'), ('shipping_partner_id', 'awb_number'),)


class PackageItem(models.Model):
    package = models.ForeignKey(Package, models.DO_NOTHING, blank=True, null=True)
    sub_order = models.ForeignKey('SubOrder', models.DO_NOTHING, blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    sub_order_item = models.ForeignKey('SuborderItem', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=9)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    picklist_id = models.IntegerField(blank=True, null=True)
    picklist_item_id = models.IntegerField(blank=True, null=True)
    dispute_reason = models.CharField(max_length=255, blank=True, null=True)
    dispute_remark = models.TextField(blank=True, null=True)
    sale_order_item = models.ForeignKey('SaleOrderItem', models.DO_NOTHING, blank=True, null=True)
    barcodes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_item'


class PackageType(models.Model):
    name = models.CharField(max_length=255)
    length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_type'


class PageAcl(models.Model):
    employee = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    url = models.CharField(max_length=255)
    allow_access = models.IntegerField()
    redirect_url = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page_acl'


class PasswordResets(models.Model):
    email = models.CharField(max_length=190)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PaymentTransaction(models.Model):
    order_transaction_id = models.IntegerField(blank=True, null=True)
    sale_order_id = models.IntegerField(blank=True, null=True)
    purchase_order_id = models.IntegerField(blank=True, null=True)
    purchase_invoice_id = models.IntegerField(blank=True, null=True)
    payment_transaction_info = models.TextField(blank=True, null=True)
    payment_mode = models.CharField(max_length=255)
    status = models.CharField(max_length=9)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    payment_gateway_order_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    payment_gateway_transcation_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    payment_correction_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class Picklist(models.Model):
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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'picklist'
        unique_together = (('awb_number', 'shipping_partner_id'), ('shipping_partner_id', 'awb_number'),)


class PicklistItem(models.Model):
    picklist = models.ForeignKey(Picklist, models.DO_NOTHING, blank=True, null=True)
    sub_order = models.ForeignKey('SubOrder', models.DO_NOTHING, blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    sub_order_item = models.ForeignKey('SuborderItem', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=9)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    dispute_reason = models.CharField(max_length=255, blank=True, null=True)
    dispute_remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picklist_item'


class Pincode(models.Model):
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    pincode = models.IntegerField()
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pincode'


class Product(models.Model):
    identifier = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    hsn = models.CharField(max_length=255, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    package_weight = models.FloatField(blank=True, null=True)
    package_height = models.FloatField(blank=True, null=True)
    package_length = models.FloatField(blank=True, null=True)
    package_width = models.FloatField(blank=True, null=True)
    package_depth = models.FloatField(blank=True, null=True)
    condition = models.CharField(max_length=11, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    shipping_method = models.CharField(max_length=16, blank=True, null=True)
    label_in_stock = models.CharField(max_length=255, blank=True, null=True)
    label_out_stock = models.CharField(max_length=255, blank=True, null=True)
    low_stock_limit = models.IntegerField(blank=True, null=True)
    back_order = models.IntegerField()
    availability_days = models.IntegerField(blank=True, null=True)
    delivery_time_in_stock = models.IntegerField(blank=True, null=True)
    delivery_time_out_stock = models.IntegerField(blank=True, null=True)
    floating_days = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    cod_available = models.IntegerField()
    expiry_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=8)
    size_chart = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    product_definition_id = models.PositiveIntegerField(blank=True, null=True)
    attribute_group = models.ForeignKey(AttributeGroup, models.DO_NOTHING, blank=True, null=True)
    tax_rule = models.ForeignKey('TaxationRule', models.DO_NOTHING)
    return_policy = models.ForeignKey('ReturnPolicy', models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_definition = models.IntegerField()
    expected_logistic_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reserved_quantity = models.IntegerField(blank=True, null=True)
    back_order_limit = models.IntegerField()
    net_stock = models.IntegerField(blank=True, null=True)
    badge = models.TextField(blank=True, null=True)  # This field type is a guess.
    status_activity = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_visible = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('sku', 'is_definition'),)


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    is_primary = models.IntegerField()
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductDetailInLanguage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    short_desc = models.TextField(blank=True, null=True)
    meta_title = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    lang = models.ForeignKey(Lang, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    search_string = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_detail_in_language'
        unique_together = (('lang', 'product'),)


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    membership = models.ForeignKey(Membership, models.DO_NOTHING, blank=True, null=True)
    vendor_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    frendy_price = models.DecimalField(max_digits=10, decimal_places=2)
    self_frendy_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    self_frendy_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frendy_cash_fund = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frendy_points_fund = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discovery_frendy_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discovery_frendy_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    min_qty = models.IntegerField(blank=True, null=True)
    max_qty = models.IntegerField(blank=True, null=True)
    effective_start_date = models.DateField(blank=True, null=True)
    effective_end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    dataset = models.ForeignKey(DataSet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_price'


class ProductRelevance(models.Model):
    dataset_id = models.PositiveIntegerField(blank=True, null=True)
    product_id = models.PositiveIntegerField(blank=True, null=True)
    product_definition_id = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_relevance'
        unique_together = (('dataset_id', 'product_id'),)


class ProductReview(models.Model):
    rating = models.CharField(max_length=10)
    review = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    lang = models.ForeignKey(Lang, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    approver = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    rejected_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_review'


class ProductReviewMedia(models.Model):
    file_uri = models.CharField(max_length=1000)
    mime_type = models.CharField(max_length=50)
    status = models.CharField(max_length=8)
    meta = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    review = models.ForeignKey(ProductReview, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_review_media'


class ProductRule(models.Model):
    pincode = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    data_set = models.TextField(blank=True, null=True)
    fullfilment_center = models.TextField(blank=True, null=True)
    include_physical_stock = models.IntegerField()
    include_virtual_stock = models.IntegerField()
    is_rule_include = models.IntegerField()
    shipping_value = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=8)
    shipping_based_on = models.CharField(max_length=9, blank=True, null=True)
    zone_id = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_rule'


class ProductSpecification(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    specification = models.ForeignKey(AttributeSpecification, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_specification'


class ProductVariation(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    condition = models.CharField(max_length=11, blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=50, blank=True, null=True)
    isbn = models.CharField(unique=True, max_length=50, blank=True, null=True)
    impact_on_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_method = models.CharField(max_length=16, blank=True, null=True)
    has_variants = models.IntegerField(blank=True, null=True)
    is_virtual = models.IntegerField()
    status = models.CharField(max_length=8)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_variation'


class ProductVariationAttributeValue(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    attribute = models.ForeignKey(AttributeSpecification, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_variation_attribute_value'


class ProductVendor(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    vendor = models.ForeignKey('User', models.DO_NOTHING)
    is_primary = models.IntegerField()
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    vendor_sku = models.CharField(max_length=255, blank=True, null=True)
    vendor_price = models.CharField(max_length=255, blank=True, null=True)
    vendor_stock = models.CharField(max_length=255)
    product_definition_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_vendor'


class ProductWarehouse(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_warehouse'


class Profile(models.Model):
    name = models.CharField(max_length=190)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'


class PurchaseInvoice(models.Model):
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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'purchase_invoice'
        unique_together = (('awb_number', 'shipping_partner_id'), ('shipping_partner_id', 'awb_number'),)


class PurchaseInvoiceItem(models.Model):
    opd_master = models.ForeignKey(PurchaseInvoice, models.DO_NOTHING)
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

    class Meta:
        managed = False
        db_table = 'purchase_invoice_item'


class PurchaseOrder(models.Model):
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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'purchase_order'
        unique_together = (('awb_number', 'shipping_partner_id'), ('shipping_partner_id', 'awb_number'),)


class PurchaseOrderItem(models.Model):
    opd_master = models.ForeignKey(PurchaseOrder, models.DO_NOTHING)
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

    class Meta:
        managed = False
        db_table = 'purchase_order_item'


class ReferralStructure(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    parent_level_1 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_2 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_3 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_4 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_5 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_6 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_7 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_8 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_9 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    parent_level_10 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    distribute_level_0 = models.IntegerField()
    distribute_level_1 = models.IntegerField()
    distribute_level_2 = models.IntegerField()
    distribute_level_3 = models.IntegerField()
    distribute_level_4 = models.IntegerField()
    distribute_level_5 = models.IntegerField()
    distribute_level_6 = models.IntegerField()
    distribute_level_7 = models.IntegerField()
    distribute_level_8 = models.IntegerField()
    distribute_level_9 = models.IntegerField()
    distribute_level_10 = models.IntegerField()
    user_referral_code = models.ForeignKey('UserReferralCode', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by_id = models.PositiveIntegerField(blank=True, null=True)
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    community_leader_slab_id = models.IntegerField(blank=True, null=True)
    temp1 = models.BigIntegerField(blank=True, null=True)
    temp2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral_structure'


class RefundPaymentCorrection(models.Model):
    id = models.BigAutoField(primary_key=True)
    opd_master = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_date = models.DateTimeField(blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=255, blank=True, null=True)
    action_to_be_taken_on_razorpay = models.CharField(max_length=255, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    order_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund_payment_correction'


class RefundRequest(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    opd_master = models.ForeignKey('SaleOrder', models.DO_NOTHING)
    opd_items = models.ForeignKey('SaleOrderItem', models.DO_NOTHING, blank=True, null=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=9)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    refund_number = models.CharField(max_length=255, blank=True, null=True)
    payment_transaction_id = models.TextField(blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
    order_return = models.ForeignKey(OrderReturn, models.DO_NOTHING, blank=True, null=True)
    refund_for = models.CharField(max_length=7, blank=True, null=True)
    refund_mode = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund_request'


class RelevanceDataset(models.Model):
    dataset_id = models.PositiveIntegerField()
    category_id = models.PositiveIntegerField()
    specifications = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    brands = models.TextField(blank=True, null=True)
    product_fields = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    category_weightage = models.CharField(max_length=255, blank=True, null=True)
    key_weightage = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'relevance_dataset'


class ReportUser(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=190, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    age_group = models.CharField(max_length=5, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    invite_code = models.CharField(max_length=255, blank=True, null=True)
    default_address_pincode = models.CharField(max_length=255, blank=True, null=True)
    invite_code_active = models.IntegerField(blank=True, null=True)
    user_frendy_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_frendy_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_redeemable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_pending = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_lifetime_earned = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_lifetime_spent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    point_pending = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    point_lifetime_earned = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    point_lifetime_spent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_withdrawable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_parent_id = models.PositiveIntegerField(blank=True, null=True)
    user_parent_first_name = models.CharField(max_length=255, blank=True, null=True)
    user_total_community_size = models.IntegerField(blank=True, null=True)
    user_total_active_community_size = models.IntegerField(blank=True, null=True)
    user_earning = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inner_circle_size = models.IntegerField(blank=True, null=True)
    inner_circle_active_size = models.IntegerField(blank=True, null=True)
    inner_circle_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    inner_circle_earning = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outer_circle_size = models.IntegerField(blank=True, null=True)
    outer_circle_active_size = models.IntegerField(blank=True, null=True)
    outer_circle_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outer_circle_earning = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extended_circle_size = models.IntegerField(blank=True, null=True)
    extended_circle_active_size = models.IntegerField(blank=True, null=True)
    extended_circle_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    extended_circle_earning = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_count = models.IntegerField(blank=True, null=True)
    order_delivered_count = models.IntegerField(blank=True, null=True)
    order_cancelled_count = models.IntegerField(blank=True, null=True)
    order_returned_count = models.IntegerField(blank=True, null=True)
    order_rto_count = models.IntegerField(blank=True, null=True)
    order_total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    point_bonus_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    point_order_returned = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_item_count = models.IntegerField(blank=True, null=True)
    average_point_per_item = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    average_point_per_order = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    average_point_per_returned_item = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    average_point_per_cancelled_item = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_part_of_inner_circle_id = models.IntegerField(blank=True, null=True)
    is_part_of_inner_circle_name = models.CharField(max_length=255, blank=True, null=True)
    is_part_of_inner_circle = models.IntegerField(blank=True, null=True)
    is_part_of_outer_circle_id = models.IntegerField(blank=True, null=True)
    is_part_of_outer_circle_name = models.CharField(max_length=255, blank=True, null=True)
    is_part_of_outer_circle = models.IntegerField(blank=True, null=True)
    is_part_of_extended_circle_id = models.IntegerField(blank=True, null=True)
    is_part_of_extended_circle_name = models.CharField(max_length=255, blank=True, null=True)
    is_part_of_extended_circle = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    kyc_status = models.CharField(max_length=255, blank=True, null=True)
    items_in_cart = models.IntegerField(blank=True, null=True)
    items_in_wishlist = models.IntegerField(blank=True, null=True)
    is_user_select = models.IntegerField(blank=True, null=True)
    is_kyc_rejected = models.IntegerField(blank=True, null=True)
    total_cash_withdrawed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    badges_won_count = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    is_sent = models.IntegerField()
    dateofbirth = models.DateField(blank=True, null=True)
    point_order_item_cancelled = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_order_item_cancelled = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash_order_item_returned = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_community_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_referred_date = models.DateTimeField(blank=True, null=True)
    point_order_item_returned = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_user'


class ReturnPolicy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    no_of_days = models.IntegerField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'return_policy'


class ReviewDetail(models.Model):
    is_liked = models.CharField(max_length=2)
    status = models.CharField(max_length=8)
    user = models.ForeignKey('User', models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    review = models.ForeignKey(ProductReview, models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_detail'


class Role(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'role'


class SaleInvoice(models.Model):
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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'sale_invoice'
        unique_together = (('awb_number', 'shipping_partner_id'), ('shipping_partner_id', 'awb_number'),)


class SaleInvoiceItem(models.Model):
    opd_master = models.ForeignKey(SaleInvoice, models.DO_NOTHING)
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

    class Meta:
        managed = False
        db_table = 'sale_invoice_item'


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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        managed = False
        db_table = 'sale_order_item'


class ShippingRule(models.Model):
    shipping_charge = models.DecimalField(max_digits=8, decimal_places=2)
    pincode = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    fullfilment_center = models.TextField(blank=True, null=True)
    min_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    min_qty = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_qty = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_points = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    membership_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    zone_id = models.IntegerField(blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    min_value = models.IntegerField(blank=True, null=True)
    max_value = models.IntegerField(blank=True, null=True)
    shipping_based_on = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_rule'


class State(models.Model):
    name = models.CharField(unique=True, max_length=50)
    status = models.CharField(max_length=8)
    gst_code = models.PositiveIntegerField(blank=True, null=True)
    created_by_id = models.PositiveIntegerField(blank=True, null=True)
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class StaticContent(models.Model):
    key = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'static_content'


class Stock(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    product_variation = models.ForeignKey(ProductVariation, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    bin = models.ForeignKey(Container, models.DO_NOTHING, blank=True, null=True)
    vendor = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock'


class StockCycleCountsLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING)
    rack = models.ForeignKey(Container, models.DO_NOTHING)
    bin = models.ForeignKey(Container, models.DO_NOTHING)
    success_barcodes = models.TextField(blank=True, null=True)
    failed_barcodes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_cycle_counts_log'


class StockProductDetails(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    opd_master = models.ForeignKey(OpdMasterTodelete, models.DO_NOTHING, blank=True, null=True)
    stock_transaction = models.ForeignKey('StockTransaction', models.DO_NOTHING, blank=True, null=True)
    is_available = models.IntegerField()
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    stock_transaction_rows = models.ForeignKey('StockTransactionRows', models.DO_NOTHING, blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    is_qcfail = models.IntegerField()
    barcode = models.ForeignKey(Barcode, models.DO_NOTHING, blank=True, null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(Package, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_product_details'


class StockTransaction(models.Model):
    from_warehouse = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    from_vendor = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    from_bin = models.ForeignKey(Container, models.DO_NOTHING, blank=True, null=True)
    to_warehouse = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    to_vendor = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    to_bin = models.ForeignKey(Container, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=26, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    opd_master = models.ForeignKey(OpdMasterTodelete, models.DO_NOTHING, blank=True, null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(Package, models.DO_NOTHING, blank=True, null=True)
    sub_order = models.ForeignKey('SubOrder', models.DO_NOTHING, blank=True, null=True)
    manifest = models.ForeignKey(Manifest, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_transaction'


class StockTransactionRows(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    stock_transaction = models.ForeignKey(StockTransaction, models.DO_NOTHING, blank=True, null=True)
    from_bin_id = models.IntegerField(blank=True, null=True)
    to_bin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_transaction_rows'


class SubOrder(models.Model):
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
    extra_info = models.TextField(blank=True, null=True)  # This field type is a guess.
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
        db_table = 'sub_order'
        unique_together = (('shipping_partner_id', 'awb_number'), ('awb_number', 'shipping_partner_id'),)


class SuborderItem(models.Model):
    sub_order = models.ForeignKey(SubOrder, models.DO_NOTHING, blank=True, null=True)
    sale_order = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', models.DO_NOTHING, blank=True, null=True)
    vendor = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    order_item = models.ForeignKey(SaleOrderItem, models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    shipping_method = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(max_length=16)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    dispute_reason = models.CharField(max_length=255, blank=True, null=True)
    dispute_remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suborder_item'


class Taxation(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.CharField(max_length=255, blank=True, null=True)
    sub_tax = models.CharField(max_length=255, blank=True, null=True)
    is_sub_tax = models.IntegerField()
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxation'


class TaxationRule(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    state = models.ForeignKey(State, models.DO_NOTHING, blank=True, null=True)
    tax = models.ForeignKey(Taxation, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxation_rule'


class Temp(models.Model):
    date_1 = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp'


class TicketAttachment(models.Model):
    image_url = models.TextField()
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_attachment'


class Tickets(models.Model):
    ticket_no = models.CharField(max_length=36)
    status = models.CharField(max_length=19, blank=True, null=True)
    issue_sub_type = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    cancel_reason = models.TextField(blank=True, null=True)
    cancel_narration = models.TextField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    created_by = models.ForeignKey('User', models.DO_NOTHING)
    assigned_to = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    issue_type = models.CharField(max_length=255, blank=True, null=True)
    order = models.ForeignKey(OpdMasterTodelete, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class UploadedSheets(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    is_uploaded = models.IntegerField()
    status = models.CharField(max_length=8)
    created_by_0 = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by_id', blank=True, null=True)  # Field renamed because of name conflict.
    updated_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploaded_sheets'


class User(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    wallet = models.ForeignKey('Wallet', models.DO_NOTHING, blank=True, null=True)
    profile = models.ForeignKey(Profile, models.DO_NOTHING, blank=True, null=True)
    membership = models.ForeignKey(Membership, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    gstin = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    otp = models.CharField(max_length=255, blank=True, null=True)
    otp_validity = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=10)
    dateofbirth = models.DateField(blank=True, null=True)
    is_invited = models.IntegerField()
    email = models.CharField(max_length=190, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    token_validity = models.BigIntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    is_email_verified = models.IntegerField(blank=True, null=True)
    is_mobile_verified = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10)
    applied_refferal_code = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    bank_account_number = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_type = models.CharField(max_length=7, blank=True, null=True)
    pan_number = models.CharField(max_length=255, blank=True, null=True)
    adhar_number = models.CharField(max_length=255, blank=True, null=True)
    age_group = models.CharField(max_length=5, blank=True, null=True)
    is_referral_code_allow = models.IntegerField(blank=True, null=True)
    is_internal = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(State, models.DO_NOTHING, blank=True, null=True)
    device_type = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.TextField(blank=True, null=True)
    device_token = models.TextField(blank=True, null=True)
    field_device_info = models.TextField(db_column='_device_info', blank=True, null=True)  # Field renamed because it started with '_'.
    device_info = models.TextField(blank=True, null=True)
    bank_ifsc = models.CharField(max_length=255, blank=True, null=True)
    bank_branch = models.CharField(max_length=255, blank=True, null=True)
    apply_referral_date = models.DateTimeField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    force_referral_code_allow = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    membership_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('mobile', 'user_type'), ('email', 'user_type'),)


class UserBankDetail(models.Model):
    account_number = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    ifsc_code = models.CharField(max_length=255)
    branch = models.CharField(max_length=255, blank=True, null=True)
    account_type = models.CharField(max_length=255, blank=True, null=True)
    is_verifed = models.IntegerField()
    user = models.ForeignKey(User, models.DO_NOTHING)
    verified_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    cancel_check = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    is_reject = models.IntegerField()
    cancel_by_id = models.IntegerField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bank_detail'


class UserCompletedGameLevelStage(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    game_level = models.ForeignKey(GameLevel, models.DO_NOTHING, blank=True, null=True)
    game_stage = models.ForeignKey(GameStage, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    earned_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_completed_game_level_stage'


class UserFriendContact(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    is_sms = models.IntegerField()
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_friend_contact'


class UserKycDetails(models.Model):
    address_proof = models.CharField(max_length=15)
    front_image = models.CharField(max_length=255, blank=True, null=True)
    back_image = models.CharField(max_length=255, blank=True, null=True)
    name_on_pancard = models.CharField(max_length=255, blank=True, null=True)
    pancard_number = models.CharField(max_length=255, blank=True, null=True)
    pancard_front_image = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_remark = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    verified_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    cancel_by_id = models.IntegerField(blank=True, null=True)
    canceled_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_kyc_details'


class UserReferralCode(models.Model):
    referral_code = models.CharField(max_length=255)
    used = models.IntegerField(blank=True, null=True)
    allowed = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8)
    user = models.ForeignKey(User, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_referral_code'


class UserRemovedReferralCode(models.Model):
    level = models.CharField(max_length=2)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    removed_from_parent = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_removed_referral_code'


class UserTags(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    tag = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    created_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tags'
        unique_together = (('user', 'tag'),)


class VendorBrand(models.Model):
    brand = models.CharField(max_length=255)
    auth_doc = models.CharField(max_length=255)
    expiry = models.DateTimeField()
    gender = models.CharField(max_length=255, blank=True, null=True)
    margin = models.IntegerField()
    margin_type = models.CharField(max_length=255, blank=True, null=True)
    disapproved_reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=11)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    vendor = models.ForeignKey(User, models.DO_NOTHING)
    approved_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    disapproved_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    disapproved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_brand'
        unique_together = (('category', 'vendor', 'brand'),)


class VendorCarrier(models.Model):
    carrier = models.ForeignKey(Carrier, models.DO_NOTHING)
    vendor = models.ForeignKey(User, models.DO_NOTHING)
    is_default = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_carrier'


class VendorDetails(models.Model):
    company_type = models.CharField(max_length=255, blank=True, null=True)
    registration_certificate_code = models.CharField(max_length=255, blank=True, null=True)
    upload_registration_certificate = models.CharField(max_length=255, blank=True, null=True)
    cin = models.CharField(max_length=255, blank=True, null=True)
    nature_of_business = models.CharField(max_length=255, blank=True, null=True)
    is_msme = models.IntegerField(blank=True, null=True)
    msme_number = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    tan_number = models.CharField(max_length=255, blank=True, null=True)
    upload_gst_certificate = models.CharField(max_length=255, blank=True, null=True)
    upload_pan_card = models.CharField(max_length=255, blank=True, null=True)
    upload_tan_card = models.CharField(max_length=255, blank=True, null=True)
    upload_cancel_cheque = models.CharField(max_length=255, blank=True, null=True)
    type_of_invoice = models.CharField(max_length=255, blank=True, null=True)
    finanace_phone_no = models.CharField(max_length=255, blank=True, null=True)
    finanace_email_id = models.CharField(max_length=255, blank=True, null=True)
    operations_phone_no = models.CharField(max_length=255, blank=True, null=True)
    operations_email_id = models.CharField(max_length=255, blank=True, null=True)
    mon_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    tue_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    wed_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    thu_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    fri_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    sat_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    sun_time_from_to = models.CharField(max_length=255, blank=True, null=True)
    brand_details = models.TextField(blank=True, null=True)  # This field type is a guess.
    reject_reason = models.TextField(blank=True, null=True)
    vendor = models.OneToOneField(User, models.DO_NOTHING)
    approved_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    rejected_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)
    accept_agreement = models.IntegerField(blank=True, null=True)
    poc = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    payment_cycle = models.IntegerField(blank=True, null=True)
    vrf_submitted_at = models.DateTimeField(blank=True, null=True)
    vrf_status = models.CharField(max_length=11)
    vrf_agreement = models.TextField(blank=True, null=True)
    i_agree = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_details'


class VideoTutorials(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    video_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_by = models.ForeignKey(User, models.DO_NOTHING)
    updated_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    deleted_by = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    lang = models.ForeignKey(Lang, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    video_thumbnail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_tutorials'


class Wallet(models.Model):
    total_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    redeemed_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    redeemed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    refund_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_added_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_added_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_removed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_removed_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reimbursement_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reimbursement_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawal_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawal_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_added_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_added_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_removed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_removed_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet'


class WalletLog(models.Model):
    wallet_id = models.PositiveIntegerField(blank=True, null=True)
    level = models.CharField(max_length=2, blank=True, null=True)
    event_id = models.PositiveIntegerField(blank=True, null=True)
    source_user_id = models.PositiveIntegerField(blank=True, null=True)
    fund_distribution_id = models.PositiveIntegerField(blank=True, null=True)
    event_count_tracker_id = models.PositiveIntegerField(blank=True, null=True)
    opd_master_id = models.PositiveIntegerField(blank=True, null=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    invites = models.IntegerField(blank=True, null=True)
    is_bonus = models.IntegerField(blank=True, null=True)
    floating_date = models.DateField(blank=True, null=True)
    floating_reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=19)
    updated_by_id = models.PositiveIntegerField(blank=True, null=True)
    deleted_by_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by_id = models.PositiveIntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    fund_percentage = models.CharField(max_length=255, blank=True, null=True)
    fund_argument = models.CharField(max_length=255, blank=True, null=True)
    extra_info = models.TextField(blank=True, null=True)
    is_visible = models.IntegerField(blank=True, null=True)
    wallet_type = models.CharField(max_length=255, blank=True, null=True)
    effected_at = models.DateTimeField(blank=True, null=True)
    is_update_wallet = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_log'


class WalletLogMonthly(models.Model):
    wallet_id = models.PositiveIntegerField(blank=True, null=True)
    cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    redeemed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    redeemed_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_bonus_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_0_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_1_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_2_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_3_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_4_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_5_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_6_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_7_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_8_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_9_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_level_10_bonus_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    community_leader_slab_id = models.IntegerField(blank=True, null=True)
    downline_points = models.BigIntegerField(blank=True, null=True)
    slab_group_commision = models.BigIntegerField(blank=True, null=True)
    slab_bonus_value = models.BigIntegerField(blank=True, null=True)
    inner_circle_temp1 = models.BigIntegerField(blank=True, null=True)
    difference = models.BigIntegerField(blank=True, null=True)
    refund_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refund_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_added_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_added_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_removed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adujustment_removed_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reimbursement_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reimbursement_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawal_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    withdrawal_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_added_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_added_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_removed_cash = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    incentive_removed_points = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_log_monthly'
        unique_together = (('wallet_id', 'month', 'year'),)


class Warehouse(models.Model):
    vendor = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'warehouse'


class WishList(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    product_variation = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wish_list'
