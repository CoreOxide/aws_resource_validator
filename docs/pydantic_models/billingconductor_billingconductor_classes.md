# Billingconductor Billingconductor Classes

# AccountAssociationsListElement

### AccountId
- **Type**: typing.Optional[str]

### BillingGroupArn
- **Type**: typing.Optional[str]

### AccountName
- **Type**: typing.Optional[str]

### AccountEmail
- **Type**: typing.Optional[str]


# AccountGrouping

### LinkedAccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### AutoAssociate
- **Type**: typing.Optional[bool]


# AssociateAccountsInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# AssociateAccountsOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatePricingRulesInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRuleArns
- **Type**: typing.List[str]
- **Required**: Yes


# AssociatePricingRulesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResourceError

### Message
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[typing.Literal['ILLEGAL_CUSTOMLINEITEM', 'INTERNAL_SERVER_EXCEPTION', 'INVALID_ARN', 'INVALID_BILLING_PERIOD_RANGE', 'SERVICE_LIMIT_EXCEEDED']]


# AssociateResourceResponseElement

### Arn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.AssociateResourceError]


# Attribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateResourcesToCustomLineItemInput

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemBillingPeriodRange]


# BatchAssociateResourcesToCustomLineItemOutput

### SuccessfullyAssociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.AssociateResourceResponseElement]
- **Required**: Yes

### FailedAssociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.AssociateResourceResponseElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateResourcesFromCustomLineItemInput

### TargetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemBillingPeriodRange]


# BatchDisassociateResourcesFromCustomLineItemOutput

### SuccessfullyDisassociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.DisassociateResourceResponseElement]
- **Required**: Yes

### FailedDisassociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.DisassociateResourceResponseElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# BillingGroupCostReportElement

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


# BillingGroupCostReportResultElement

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.Attribute]]


# BillingGroupListElement

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PrimaryAccountId
- **Type**: typing.Optional[str]

### ComputationPreference
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListBillingGroupAccountGrouping]


# BillingPeriodRange

### InclusiveStartBillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ExclusiveEndBillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes


# ComputationPreference

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBillingGroupInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountGrouping
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.AccountGrouping'>
- **Required**: Yes

### ComputationPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ComputationPreference'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### PrimaryAccountId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateBillingGroupOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomLineItemInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemChargeDetails'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemBillingPeriodRange]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AccountId
- **Type**: typing.Optional[str]


# CreateCustomLineItemOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFreeTierConfig

### Activated
- **Type**: <class 'bool'>
- **Required**: Yes


# CreatePricingPlanInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PricingRuleArns
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePricingPlanOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePricingRuleInput

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### BillingEntity
- **Type**: typing.Optional[str]

### Tiering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CreateTieringInput]

### UsageType
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]


# CreatePricingRuleOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTieringInput

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CreateFreeTierConfig'>
- **Required**: Yes


# CustomLineItemBillingPeriodRange

### InclusiveStartBillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ExclusiveEndBillingPeriod
- **Type**: typing.Optional[str]


# CustomLineItemChargeDetails

### Type
- **Type**: typing.Literal['CREDIT', 'FEE']
- **Required**: Yes

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemFlatChargeDetails]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemPercentageChargeDetails]

### LineItemFilters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.LineItemFilter, aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.LineItemFilterOutput]]]


# CustomLineItemFlatChargeDetails

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# CustomLineItemListElement

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemChargeDetails]

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


# CustomLineItemPercentageChargeDetails

### PercentageValue
- **Type**: <class 'float'>
- **Required**: Yes

### AssociatedValues
- **Type**: typing.Optional[typing.List[str]]


# CustomLineItemVersionListElement

### Name
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemChargeDetails]

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


# DeleteBillingGroupInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillingGroupOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomLineItemInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemBillingPeriodRange]


# DeleteCustomLineItemOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePricingPlanInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePricingPlanOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePricingRuleInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePricingRuleOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateAccountsInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociateAccountsOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociatePricingRulesInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRuleArns
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociatePricingRulesOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResourceResponseElement

### Arn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.AssociateResourceError]


# FreeTierConfig

### Activated
- **Type**: <class 'bool'>
- **Required**: Yes


# GetBillingGroupCostReportInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriodRange
- **Type**: <class 'NoneType'>

### GroupBy
- **Type**: typing.Optional[typing.List[typing.Literal['BILLING_PERIOD', 'PRODUCT_NAME']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetBillingGroupCostReportOutput

### BillingGroupCostReportResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.BillingGroupCostReportResultElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LineItemFilter

### Attribute
- **Type**: typing.Literal['LINE_ITEM_TYPE']
- **Required**: Yes

### MatchOption
- **Type**: typing.Literal['NOT_EQUAL']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['SAVINGS_PLAN_NEGATION']]
- **Required**: Yes


# LineItemFilterOutput

### Attribute
- **Type**: typing.Literal['LINE_ITEM_TYPE']
- **Required**: Yes

### MatchOption
- **Type**: typing.Literal['NOT_EQUAL']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['SAVINGS_PLAN_NEGATION']]
- **Required**: Yes


# ListAccountAssociationsFilter

### Association
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]


# ListAccountAssociationsInput

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListAccountAssociationsFilter]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssociationsInputPaginate

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListAccountAssociationsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListAccountAssociationsOutput

### LinkedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.AccountAssociationsListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBillingGroupAccountGrouping

### AutoAssociate
- **Type**: typing.Optional[bool]


# ListBillingGroupCostReportsFilter

### BillingGroupArns
- **Type**: typing.Optional[typing.List[str]]


# ListBillingGroupCostReportsInput

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListBillingGroupCostReportsFilter]


# ListBillingGroupCostReportsInputPaginate

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListBillingGroupCostReportsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListBillingGroupCostReportsOutput

### BillingGroupCostReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.BillingGroupCostReportElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBillingGroupsFilter

### Arns
- **Type**: typing.Optional[typing.List[str]]

### PricingPlan
- **Type**: typing.Optional[str]

### Statuses
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']]]

### AutoAssociate
- **Type**: typing.Optional[bool]


# ListBillingGroupsInput

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListBillingGroupsFilter]


# ListBillingGroupsInputPaginate

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListBillingGroupsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListBillingGroupsOutput

### BillingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.BillingGroupListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomLineItemChargeDetails

### Type
- **Type**: typing.Literal['CREDIT', 'FEE']
- **Required**: Yes

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemFlatChargeDetails]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemPercentageChargeDetails]

### LineItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.LineItemFilterOutput]]


# ListCustomLineItemFlatChargeDetails

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# ListCustomLineItemPercentageChargeDetails

### PercentageValue
- **Type**: <class 'float'>
- **Required**: Yes


# ListCustomLineItemVersionsBillingPeriodRangeFilter

### StartBillingPeriod
- **Type**: typing.Optional[str]

### EndBillingPeriod
- **Type**: typing.Optional[str]


# ListCustomLineItemVersionsFilter

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemVersionsBillingPeriodRangeFilter]


# ListCustomLineItemVersionsInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemVersionsFilter]


# ListCustomLineItemVersionsInputPaginate

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemVersionsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListCustomLineItemVersionsOutput

### CustomLineItemVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemVersionListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomLineItemsFilter

### Names
- **Type**: typing.Optional[typing.List[str]]

### BillingGroups
- **Type**: typing.Optional[typing.List[str]]

### Arns
- **Type**: typing.Optional[typing.List[str]]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]


# ListCustomLineItemsInput

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemsFilter]


# ListCustomLineItemsInputPaginate

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListCustomLineItemsOutput

### CustomLineItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansAssociatedWithPricingRuleInput

### PricingRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansAssociatedWithPricingRuleInputPaginate

### PricingRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListPricingPlansAssociatedWithPricingRuleOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansFilter

### Arns
- **Type**: typing.Optional[typing.List[str]]


# ListPricingPlansInput

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListPricingPlansFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingPlansInputPaginate

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListPricingPlansFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListPricingPlansOutput

### BillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### PricingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PricingPlanListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesAssociatedToPricingPlanInput

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesAssociatedToPricingPlanInputPaginate

### PricingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListPricingRulesAssociatedToPricingPlanOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesFilter

### Arns
- **Type**: typing.Optional[typing.List[str]]


# ListPricingRulesInput

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListPricingRulesFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPricingRulesInputPaginate

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListPricingRulesFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListPricingRulesOutput

### BillingPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### PricingRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PricingRuleListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesAssociatedToCustomLineItemFilter

### Relationship
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]


# ListResourcesAssociatedToCustomLineItemInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListResourcesAssociatedToCustomLineItemFilter]


# ListResourcesAssociatedToCustomLineItemInputPaginate

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### BillingPeriod
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListResourcesAssociatedToCustomLineItemFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.PaginatorConfig]


# ListResourcesAssociatedToCustomLineItemOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListResourcesAssociatedToCustomLineItemResponseElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesAssociatedToCustomLineItemResponseElement

### Arn
- **Type**: typing.Optional[str]

### Relationship
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]

### EndBillingPeriod
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PricingPlanListElement

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


# PricingRuleListElement

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
- **Type**: <class 'NoneType'>

### UsageType
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]


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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Tiering

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.FreeTierConfig'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBillingGroupAccountGrouping

### AutoAssociate
- **Type**: typing.Optional[bool]


# UpdateBillingGroupInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PRIMARY_ACCOUNT_MISSING']]

### ComputationPreference
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### AccountGrouping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateBillingGroupAccountGrouping]


# UpdateBillingGroupOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateBillingGroupAccountGrouping'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomLineItemChargeDetails

### Flat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateCustomLineItemFlatChargeDetails]

### Percentage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateCustomLineItemPercentageChargeDetails]

### LineItemFilters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.LineItemFilter, aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.LineItemFilterOutput]]]


# UpdateCustomLineItemFlatChargeDetails

### ChargeValue
- **Type**: <class 'float'>
- **Required**: Yes


# UpdateCustomLineItemInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ChargeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateCustomLineItemChargeDetails]

### BillingPeriodRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.CustomLineItemBillingPeriodRange]


# UpdateCustomLineItemOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ListCustomLineItemChargeDetails'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### AssociationSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCustomLineItemPercentageChargeDetails

### PercentageValue
- **Type**: <class 'float'>
- **Required**: Yes


# UpdateFreeTierConfig

### Activated
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdatePricingPlanInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdatePricingPlanOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePricingRuleInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateTieringInput]


# UpdatePricingRuleOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateTieringInput'>
- **Required**: Yes

### UsageType
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTieringInput

### FreeTier
- **Type**: <class 'aws_resource_validator.pydantic_models.billingconductor.billingconductor_classes.UpdateFreeTierConfig'>
- **Required**: Yes


