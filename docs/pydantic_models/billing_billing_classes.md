# Billing Billing Classes

# ActiveTimeRange

### activeAfterInclusive
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### activeBeforeInclusive
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingViewElement

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### billingViewType
- **Type**: typing.Optional[typing.Literal['BILLING_GROUP', 'CUSTOM', 'PRIMARY']]

### ownerAccountId
- **Type**: typing.Optional[str]

### dataFilterExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.ExpressionOutput]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# BillingViewListElement

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ownerAccountId
- **Type**: typing.Optional[str]

### billingViewType
- **Type**: typing.Optional[typing.Literal['BILLING_GROUP', 'CUSTOM', 'PRIMARY']]


# CreateBillingViewRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sourceViews
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### dataFilterExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.billing.billing_classes.Expression, aws_resource_validator.pydantic_models.billing.billing_classes.ExpressionOutput, NoneType]

### clientToken
- **Type**: typing.Optional[str]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.billing.billing_classes.ResourceTag]]


# CreateBillingViewResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBillingViewRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBillingViewResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes


# DimensionValues

### key
- **Type**: typing.Literal['LINKED_ACCOUNT']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# DimensionValuesOutput

### key
- **Type**: typing.Literal['LINKED_ACCOUNT']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# Expression

### dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.DimensionValues]

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.TagValues]


# ExpressionOutput

### dimensions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.DimensionValuesOutput]

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.TagValuesOutput]


# GetBillingViewRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBillingViewResponse

### billingView
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.BillingViewElement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes


# ListBillingViewsRequest

### activeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.ActiveTimeRange]

### arns
- **Type**: typing.Optional[typing.List[str]]

### billingViewTypes
- **Type**: typing.Optional[typing.List[typing.Literal['BILLING_GROUP', 'CUSTOM', 'PRIMARY']]]

### ownerAccountId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBillingViewsRequestPaginate

### activeTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.ActiveTimeRange]

### arns
- **Type**: typing.Optional[typing.List[str]]

### billingViewTypes
- **Type**: typing.Optional[typing.List[typing.Literal['BILLING_GROUP', 'CUSTOM', 'PRIMARY']]]

### ownerAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.PaginatorConfig]


# ListBillingViewsResponse

### billingViews
- **Type**: typing.List[aws_resource_validator.pydantic_models.billing.billing_classes.BillingViewListElement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceViewsForBillingViewRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSourceViewsForBillingViewRequestPaginate

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.billing.billing_classes.PaginatorConfig]


# ListSourceViewsForBillingViewResponse

### sourceViews
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### resourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.billing.billing_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
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

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.billing.billing_classes.ResourceTag]
- **Required**: Yes


# TagValues

### key
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# TagValuesOutput

### key
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceTagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBillingViewRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### dataFilterExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.billing.billing_classes.Expression, aws_resource_validator.pydantic_models.billing.billing_classes.ExpressionOutput, NoneType]


# UpdateBillingViewResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.billing.billing_classes.ResponseMetadata'>
- **Required**: Yes


