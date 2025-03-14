# Billingconductor Classes

# AccountAssociationsListElementTypeDef

### AccountId
- **Type**: typing.Optional[str]

### BillingGroupArn
- **Type**: typing.Optional[str]

### AccountName
- **Type**: typing.Optional[str]

### AccountEmail
- **Type**: typing.Optional[str]


# AccountGroupingTypeDef

### LinkedAccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AutoAssociate
- **Type**: typing.Optional[bool]


# AssociateAccountsInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociateAccountsOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatePricingRulesInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRuleArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociatePricingRulesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResourceErrorTypeDef

### Message
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['ILLEGAL_CUSTOMLINEITEM', 'INTERNAL_SERVER_EXCEPTION', 'INVALID_ARN', 'INVALID_BILLING_PERIOD_RANGE', 'SERVICE_LIMIT_EXCEEDED']]


# AssociateResourceResponseElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.AssociateResourceErrorTypeDef]


# AttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateResourcesToCustomLineItemInputTypeDef

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemBillingPeriodRangeTypeDef]


# BatchAssociateResourcesToCustomLineItemOutputTypeDef

### SuccessfullyAssociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.AssociateResourceResponseElementTypeDef]
- **Required**: Yes

### FailedAssociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.AssociateResourceResponseElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateResourcesFromCustomLineItemInputTypeDef

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemBillingPeriodRangeTypeDef]


# BatchDisassociateResourcesFromCustomLineItemOutputTypeDef

### SuccessfullyDisassociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.DisassociateResourceResponseElementTypeDef]
- **Required**: Yes

### FailedDisassociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.DisassociateResourceResponseElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BillingGroupCostReportElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### AWSCost
- **Type**: typing.Optional[str]

### ProformaCost
- **Type**: typing.Optional[str]

### Margin
- **Type**: typing.Optional[str]

### MarginPercentage
- **Type**: typing.Optional[str]

### Currency
- **Type**: typing.Optional[str]


# BillingGroupCostReportResultElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### AWSCost
- **Type**: typing.Optional[str]

### ProformaCost
- **Type**: typing.Optional[str]

### Margin
- **Type**: typing.Optional[str]

### MarginPercentage
- **Type**: typing.Optional[str]

### Currency
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.AttributeTypeDef]]


# BillingGroupListElementTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PrimaryAccountId
- **Type**: typing.Optional[str]

### ComputationPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ComputationPreferenceTypeDef]

### Size
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']]

### StatusReason
- **Type**: typing.Optional[str]

### AccountGrouping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupAccountGroupingTypeDef]


# BillingPeriodRangeTypeDef

### InclusiveStartBillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ExclusiveEndBillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes


# ComputationPreferenceTypeDef

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBillingGroupInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountGrouping
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.AccountGroupingTypeDef'>
- **Required**: Yes

### ComputationPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ComputationPreferenceTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### PrimaryAccountId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateBillingGroupOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomLineItemInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### BillingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChargeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemChargeDetailsTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemBillingPeriodRangeTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AccountId
- **Type**: typing.Optional[str]


# CreateCustomLineItemOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFreeTierConfigTypeDef

### Activated
- **Type**: <class 'bool'>
- **Required**: Yes


# CreatePricingPlanInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PricingRuleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePricingPlanOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePricingRuleOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTieringInputTypeDef

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.CreateFreeTierConfigTypeDef'>
- **Required**: Yes


# CustomLineItemBillingPeriodRangeTypeDef

### InclusiveStartBillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ExclusiveEndBillingPeriod
- **Type**: typing.Optional[str]


# CustomLineItemChargeDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomLineItemFlatChargeDetailsTypeDef

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# CustomLineItemListElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemChargeDetailsTypeDef]

### CurrencyCode
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### Description
- **Type**: typing.Optional[str]

### ProductCode
- **Type**: typing.Optional[str]

### BillingGroupArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[int]

### AssociationSize
- **Type**: typing.Optional[int]

### AccountId
- **Type**: typing.Optional[str]


# CustomLineItemPercentageChargeDetailsTypeDef

### PercentageValue
- **Type**: <class 'float'>
- **Required**: Yes

### AssociatedValues
- **Type**: typing.Optional[typing.Sequence[str]]


# CustomLineItemVersionListElementTypeDef

### Name
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemChargeDetailsTypeDef]

### CurrencyCode
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### Description
- **Type**: typing.Optional[str]

### ProductCode
- **Type**: typing.Optional[str]

### BillingGroupArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[int]

### AssociationSize
- **Type**: typing.Optional[int]

### StartBillingPeriod
- **Type**: typing.Optional[str]

### EndBillingPeriod
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[int]

### AccountId
- **Type**: typing.Optional[str]


# DeleteBillingGroupInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillingGroupOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomLineItemInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemBillingPeriodRangeTypeDef]


# DeleteCustomLineItemOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePricingPlanInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePricingPlanOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePricingRuleInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePricingRuleOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateAccountsInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateAccountsOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociatePricingRulesInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRuleArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociatePricingRulesOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResourceResponseElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.AssociateResourceErrorTypeDef]


# FreeTierConfigTypeDef

### Activated
- **Type**: <class 'bool'>
- **Required**: Yes


# GetBillingGroupCostReportInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.BillingPeriodRangeTypeDef]

### GroupBy
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BILLING_PERIOD', 'PRODUCT_NAME']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetBillingGroupCostReportOutputTypeDef

### BillingGroupCostReportResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.BillingGroupCostReportResultElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LineItemFilterOutputTypeDef

### Attribute
- **Type**: typing.Literal['LINE_ITEM_TYPE']
- **Required**: Yes

### MatchOption
- **Type**: typing.Literal['NOT_EQUAL']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['SAVINGS_PLAN_NEGATION']]
- **Required**: Yes


# LineItemFilterTypeDef

### Attribute
- **Type**: typing.Literal['LINE_ITEM_TYPE']
- **Required**: Yes

### MatchOption
- **Type**: typing.Literal['NOT_EQUAL']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[typing.Literal['SAVINGS_PLAN_NEGATION']]
- **Required**: Yes


# LineItemFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccountAssociationsFilterTypeDef

### Association
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListAccountAssociationsInputPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListAccountAssociationsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListAccountAssociationsInputTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListAccountAssociationsFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssociationsOutputTypeDef

### LinkedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.AccountAssociationsListElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBillingGroupAccountGroupingTypeDef

### AutoAssociate
- **Type**: typing.Optional[bool]


# ListBillingGroupCostReportsFilterTypeDef

### BillingGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]


# ListBillingGroupCostReportsInputPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupCostReportsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListBillingGroupCostReportsInputTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupCostReportsFilterTypeDef]


# ListBillingGroupCostReportsOutputTypeDef

### BillingGroupCostReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.BillingGroupCostReportElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBillingGroupsFilterTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### PricingPlan
- **Type**: typing.Optional[str]

### Statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']]]

### AutoAssociate
- **Type**: typing.Optional[bool]


# ListBillingGroupsInputPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListBillingGroupsInputTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupsFilterTypeDef]


# ListBillingGroupsOutputTypeDef

### BillingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.BillingGroupListElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomLineItemChargeDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListCustomLineItemFlatChargeDetailsTypeDef

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# ListCustomLineItemPercentageChargeDetailsTypeDef

### PercentageValue
- **Type**: <class 'float'>
- **Required**: Yes


# ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef

### StartBillingPeriod
- **Type**: typing.Optional[str]

### EndBillingPeriod
- **Type**: typing.Optional[str]


# ListCustomLineItemVersionsFilterTypeDef

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef]


# ListCustomLineItemVersionsInputPaginateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemVersionsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListCustomLineItemVersionsInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemVersionsFilterTypeDef]


# ListCustomLineItemVersionsOutputTypeDef

### CustomLineItemVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemVersionListElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomLineItemsFilterTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### BillingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListCustomLineItemsInputPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListCustomLineItemsInputTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemsFilterTypeDef]


# ListCustomLineItemsOutputTypeDef

### CustomLineItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemListElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef

### PricingRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingPlansAssociatedWithPricingRuleInputTypeDef

### PricingRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansAssociatedWithPricingRuleOutputTypeDef

### BillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlanArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansFilterTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]


# ListPricingPlansInputPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListPricingPlansFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingPlansInputTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListPricingPlansFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansOutputTypeDef

### BillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.PricingPlanListElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingRulesAssociatedToPricingPlanInputTypeDef

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesAssociatedToPricingPlanOutputTypeDef

### BillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRuleArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesFilterTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]


# ListPricingRulesInputPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListPricingRulesFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingRulesInputTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListPricingRulesFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesOutputTypeDef

### BillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.PricingRuleListElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesAssociatedToCustomLineItemFilterTypeDef

### Relationship
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]


# ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListResourcesAssociatedToCustomLineItemFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListResourcesAssociatedToCustomLineItemInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListResourcesAssociatedToCustomLineItemFilterTypeDef]


# ListResourcesAssociatedToCustomLineItemOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.ListResourcesAssociatedToCustomLineItemResponseElementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesAssociatedToCustomLineItemResponseElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### Relationship
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]

### EndBillingPeriod
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PricingPlanListElementTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[int]


# PricingRuleListElementTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TieringTypeDef

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.FreeTierConfigTypeDef'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBillingGroupAccountGroupingTypeDef

### AutoAssociate
- **Type**: typing.Optional[bool]


# UpdateBillingGroupInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']]

### ComputationPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ComputationPreferenceTypeDef]

### Description
- **Type**: typing.Optional[str]

### AccountGrouping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.UpdateBillingGroupAccountGroupingTypeDef]


# UpdateBillingGroupOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### AccountGrouping
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.UpdateBillingGroupAccountGroupingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomLineItemChargeDetailsTypeDef

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.UpdateCustomLineItemFlatChargeDetailsTypeDef]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.UpdateCustomLineItemPercentageChargeDetailsTypeDef]

### LineItemFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.billingconductor_classes.LineItemFilterUnionTypeDef]]


# UpdateCustomLineItemFlatChargeDetailsTypeDef

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# UpdateCustomLineItemInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.UpdateCustomLineItemChargeDetailsTypeDef]

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemBillingPeriodRangeTypeDef]


# UpdateCustomLineItemOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ChargeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemChargeDetailsTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### AssociationSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCustomLineItemPercentageChargeDetailsTypeDef

### PercentageValue
- **Type**: <class 'float'>
- **Required**: Yes


# UpdateFreeTierConfigTypeDef

### Activated
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdatePricingPlanInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdatePricingPlanOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTieringInputTypeDef

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.UpdateFreeTierConfigTypeDef'>
- **Required**: Yes


