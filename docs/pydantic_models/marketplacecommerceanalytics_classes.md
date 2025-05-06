# Marketplacecommerceanalytics Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GenerateDataSetRequest

### dataSetType
- **Type**: typing.Literal['customer_profile_by_geography', 'customer_profile_by_industry', 'customer_profile_by_revenue', 'customer_subscriber_annual_subscriptions', 'customer_subscriber_hourly_monthly_subscriptions', 'daily_business_canceled_product_subscribers', 'daily_business_fees', 'daily_business_free_trial_conversions', 'daily_business_new_instances', 'daily_business_new_product_subscribers', 'daily_business_usage_by_instance_type', 'disbursed_amount_by_age_of_disbursed_funds', 'disbursed_amount_by_age_of_past_due_funds', 'disbursed_amount_by_age_of_uncollected_funds', 'disbursed_amount_by_customer_geo', 'disbursed_amount_by_instance_hours', 'disbursed_amount_by_product', 'disbursed_amount_by_product_with_uncollected_funds', 'disbursed_amount_by_uncollected_funds_breakdown', 'monthly_revenue_annual_subscriptions', 'monthly_revenue_billing_and_revenue_data', 'monthly_revenue_field_demonstration_usage', 'monthly_revenue_flexible_payment_schedule', 'sales_compensation_billed_revenue', 'us_sales_and_use_tax_records']
- **Required**: Yes

### dataSetPublicationDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### roleNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationS3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### snsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationS3Prefix
- **Type**: typing.Optional[str]

### customerDefinedValues
- **Type**: typing.Optional[typing.Dict[str, str]]


# GenerateDataSetResult

### dataSetRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplacecommerceanalytics.marketplacecommerceanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# StartSupportDataExportRequest

### dataSetType
- **Type**: typing.Literal['customer_support_contacts_data', 'test_customer_support_contacts_data']
- **Required**: Yes

### fromDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### roleNameArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationS3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### snsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationS3Prefix
- **Type**: typing.Optional[str]

### customerDefinedValues
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartSupportDataExportResult

### dataSetRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplacecommerceanalytics.marketplacecommerceanalytics_classes.ResponseMetadata'>
- **Required**: Yes


