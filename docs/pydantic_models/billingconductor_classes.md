# billingconductor_classes

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


# AssociateAccountsInputRequestTypeDef

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


# AssociatePricingRulesInputRequestTypeDef

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

# BatchAssociateResourcesToCustomLineItemInputRequestTypeDef

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


# BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef

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


# CreateBillingGroupInputRequestTypeDef

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


# CreateCustomLineItemInputRequestTypeDef

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


# CreatePricingPlanInputRequestTypeDef

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


# CreatePricingRuleInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['BILLING_ENTITY', 'GLOBAL', 'SERVICE', 'SKU']
- **Required**: Yes

### Type
- **Type**: typing.Literal['DISCOUNT', 'MARKUP', 'TIERING']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ModifierPercentage
- **Type**: typing.Optional[float]

### Service
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### BillingEntity
- **Type**: typing.Optional[str]

### Tiering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CreateTieringInputTypeDef]

### UsageType
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]


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

### Type
- **Type**: typing.Literal['CREDIT', 'FEE']
- **Required**: Yes

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemFlatChargeDetailsTypeDef]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemPercentageChargeDetailsTypeDef]

### LineItemFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.billingconductor_classes.LineItemFilterTypeDef]]


# CustomLineItemFlatChargeDetailsTypeDef

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# CustomLineItemListElementPaginatorTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemChargeDetailsPaginatorTypeDef]

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


# CustomLineItemVersionListElementPaginatorTypeDef

### Name
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemChargeDetailsPaginatorTypeDef]

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


# DeleteBillingGroupInputRequestTypeDef

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


# DeleteCustomLineItemInputRequestTypeDef

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


# DeletePricingPlanInputRequestTypeDef

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


# DeletePricingRuleInputRequestTypeDef

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


# DisassociateAccountsInputRequestTypeDef

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


# DisassociatePricingRulesInputRequestTypeDef

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


# GetBillingGroupCostReportInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LineItemFilterPaginatorTypeDef

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


# ListAccountAssociationsFilterTypeDef

### Association
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListAccountAssociationsInputListAccountAssociationsPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListAccountAssociationsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListAccountAssociationsInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBillingGroupAccountGroupingTypeDef

### AutoAssociate
- **Type**: typing.Optional[bool]


# ListBillingGroupCostReportsFilterTypeDef

### BillingGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]


# ListBillingGroupCostReportsInputListBillingGroupCostReportsPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupCostReportsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListBillingGroupCostReportsInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBillingGroupsFilterTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### PricingPlan
- **Type**: typing.Optional[str]

### Statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']]]

### AutoAssociate
- **Type**: typing.Optional[bool]


# ListBillingGroupsInputListBillingGroupsPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListBillingGroupsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListBillingGroupsInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomLineItemChargeDetailsPaginatorTypeDef

### Type
- **Type**: typing.Literal['CREDIT', 'FEE']
- **Required**: Yes

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemFlatChargeDetailsTypeDef]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemPercentageChargeDetailsTypeDef]

### LineItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.LineItemFilterPaginatorTypeDef]]


# ListCustomLineItemChargeDetailsTypeDef

### Type
- **Type**: typing.Literal['CREDIT', 'FEE']
- **Required**: Yes

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemFlatChargeDetailsTypeDef]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemPercentageChargeDetailsTypeDef]

### LineItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.LineItemFilterTypeDef]]


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


# ListCustomLineItemVersionsInputListCustomLineItemVersionsPaginateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemVersionsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListCustomLineItemVersionsInputRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemVersionsFilterTypeDef]


# ListCustomLineItemVersionsOutputPaginatorTypeDef

### CustomLineItemVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemVersionListElementPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomLineItemVersionsOutputTypeDef

### CustomLineItemVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemVersionListElementTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomLineItemsFilterTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### BillingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListCustomLineItemsInputListCustomLineItemsPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListCustomLineItemsInputRequestTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListCustomLineItemsFilterTypeDef]


# ListCustomLineItemsOutputPaginatorTypeDef

### CustomLineItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemListElementPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomLineItemsOutputTypeDef

### CustomLineItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor_classes.CustomLineItemListElementTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPricingPlansAssociatedWithPricingRuleInputListPricingPlansAssociatedWithPricingRulePaginateTypeDef

### PricingRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPricingPlansFilterTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]


# ListPricingPlansInputListPricingPlansPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListPricingPlansFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingPlansInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPricingRulesAssociatedToPricingPlanInputListPricingRulesAssociatedToPricingPlanPaginateTypeDef

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPricingRulesFilterTypeDef

### Arns
- **Type**: typing.Optional[typing.Sequence[str]]


# ListPricingRulesInputListPricingRulesPaginateTypeDef

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListPricingRulesFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListPricingRulesInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourcesAssociatedToCustomLineItemFilterTypeDef

### Relationship
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]


# ListResourcesAssociatedToCustomLineItemInputListResourcesAssociatedToCustomLineItemPaginateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.ListResourcesAssociatedToCustomLineItemFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.PaginatorConfigTypeDef]


# ListResourcesAssociatedToCustomLineItemInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourcesAssociatedToCustomLineItemResponseElementTypeDef

### Arn
- **Type**: typing.Optional[str]

### Relationship
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]

### EndBillingPeriod
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

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

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[typing.Literal['BILLING_ENTITY', 'GLOBAL', 'SERVICE', 'SKU']]

### Type
- **Type**: typing.Optional[typing.Literal['DISCOUNT', 'MARKUP', 'TIERING']]

### ModifierPercentage
- **Type**: typing.Optional[float]

### Service
- **Type**: typing.Optional[str]

### AssociatedPricingPlanCount
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[int]

### BillingEntity
- **Type**: typing.Optional[str]

### Tiering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.TieringTypeDef]

### UsageType
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBillingGroupAccountGroupingTypeDef

### AutoAssociate
- **Type**: typing.Optional[bool]


# UpdateBillingGroupInputRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.billingconductor_classes.LineItemFilterTypeDef]]


# UpdateCustomLineItemFlatChargeDetailsTypeDef

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# UpdateCustomLineItemInputRequestTypeDef

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


# UpdatePricingPlanInputRequestTypeDef

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


# UpdatePricingRuleInputRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DISCOUNT', 'MARKUP', 'TIERING']]

### ModifierPercentage
- **Type**: typing.Optional[float]

### Tiering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor_classes.UpdateTieringInputTypeDef]


# UpdatePricingRuleOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['BILLING_ENTITY', 'GLOBAL', 'SERVICE', 'SKU']
- **Required**: Yes

### Type
- **Type**: typing.Literal['DISCOUNT', 'MARKUP', 'TIERING']
- **Required**: Yes

### ModifierPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### Service
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedPricingPlanCount
- **Type**: <class 'int'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### BillingEntity
- **Type**: <class 'str'>
- **Required**: Yes

### Tiering
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.UpdateTieringInputTypeDef'>
- **Required**: Yes

### UsageType
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTieringInputTypeDef

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor_classes.UpdateFreeTierConfigTypeDef'>
- **Required**: Yes


