# savingsplans_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateSavingsPlanRequestRequestTypeDef

### savingsPlanOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### commitment
- **Type**: <class 'str'>
- **Required**: Yes

### upfrontPaymentAmount
- **Type**: typing.Optional[str]

### purchaseTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSavingsPlanResponseTypeDef

### savingsPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteQueuedSavingsPlanRequestRequestTypeDef

### savingsPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSavingsPlanRatesRequestRequestTypeDef

### savingsPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanRateFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeSavingsPlanRatesResponseTypeDef

### savingsPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### searchResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanRateTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSavingsPlansOfferingRatesRequestRequestTypeDef

### savingsPlanOfferingIds
- **Type**: typing.Optional[typing.Sequence[str]]

### savingsPlanPaymentOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All Upfront', 'No Upfront', 'Partial Upfront']]]

### savingsPlanTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Compute', 'EC2Instance', 'SageMaker']]]

### products
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC2', 'Fargate', 'Lambda', 'SageMaker']]]

### serviceCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSLambda', 'AmazonEC2', 'AmazonECS', 'AmazonEKS', 'AmazonSageMaker']]]

### usageTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### operations
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanOfferingRateFilterElementTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeSavingsPlansOfferingRatesResponseTypeDef

### searchResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanOfferingRateTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSavingsPlansOfferingsRequestRequestTypeDef

### offeringIds
- **Type**: typing.Optional[typing.Sequence[str]]

### paymentOptions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All Upfront', 'No Upfront', 'Partial Upfront']]]

### productType
- **Type**: typing.Optional[typing.Literal['EC2', 'Fargate', 'Lambda', 'SageMaker']]

### planTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Compute', 'EC2Instance', 'SageMaker']]]

### durations
- **Type**: typing.Optional[typing.Sequence[int]]

### currencies
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CNY', 'USD']]]

### descriptions
- **Type**: typing.Optional[typing.Sequence[str]]

### serviceCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### usageTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### operations
- **Type**: typing.Optional[typing.Sequence[str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanOfferingFilterElementTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeSavingsPlansOfferingsResponseTypeDef

### searchResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanOfferingTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSavingsPlansRequestRequestTypeDef

### savingsPlanArns
- **Type**: typing.Optional[typing.Sequence[str]]

### savingsPlanIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['active', 'payment-failed', 'payment-pending', 'pending-return', 'queued', 'queued-deleted', 'retired', 'returned']]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanFilterTypeDef]]


# DescribeSavingsPlansResponseTypeDef

### savingsPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ParentSavingsPlanOfferingTypeDef

### offeringId
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[typing.Literal['All Upfront', 'No Upfront', 'Partial Upfront']]

### planType
- **Type**: typing.Optional[typing.Literal['Compute', 'EC2Instance', 'SageMaker']]

### durationSeconds
- **Type**: typing.Optional[int]

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### planDescription
- **Type**: typing.Optional[str]


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


# ReturnSavingsPlanRequestRequestTypeDef

### savingsPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ReturnSavingsPlanResponseTypeDef

### savingsPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.savingsplans_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SavingsPlanFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['commitment', 'ec2-instance-family', 'end', 'payment-option', 'region', 'savings-plan-type', 'start', 'term', 'upfront']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SavingsPlanOfferingFilterElementTypeDef

### name
- **Type**: typing.Optional[typing.Literal['instanceFamily', 'region']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SavingsPlanOfferingPropertyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['instanceFamily', 'region']]

### value
- **Type**: typing.Optional[str]


# SavingsPlanOfferingRateFilterElementTypeDef

### name
- **Type**: typing.Optional[typing.Literal['instanceFamily', 'instanceType', 'productDescription', 'productId', 'region', 'tenancy']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SavingsPlanOfferingRatePropertyTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# SavingsPlanOfferingRateTypeDef

### savingsPlanOffering
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.savingsplans_classes.ParentSavingsPlanOfferingTypeDef]

### rate
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[typing.Literal['Hrs', 'Lambda-GB-Second', 'Request']]

### productType
- **Type**: typing.Optional[typing.Literal['EC2', 'Fargate', 'Lambda', 'SageMaker']]

### serviceCode
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'AmazonEC2', 'AmazonECS', 'AmazonEKS', 'AmazonSageMaker']]

### usageType
- **Type**: typing.Optional[str]

### operation
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanOfferingRatePropertyTypeDef]]


# SavingsPlanOfferingTypeDef

### offeringId
- **Type**: typing.Optional[str]

### productTypes
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'Fargate', 'Lambda', 'SageMaker']]]

### planType
- **Type**: typing.Optional[typing.Literal['Compute', 'EC2Instance', 'SageMaker']]

### description
- **Type**: typing.Optional[str]

### paymentOption
- **Type**: typing.Optional[typing.Literal['All Upfront', 'No Upfront', 'Partial Upfront']]

### durationSeconds
- **Type**: typing.Optional[int]

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### serviceCode
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[str]

### operation
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanOfferingPropertyTypeDef]]


# SavingsPlanRateFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['instanceType', 'operation', 'productDescription', 'productType', 'region', 'serviceCode', 'tenancy', 'usageType']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SavingsPlanRatePropertyTypeDef

### name
- **Type**: typing.Optional[typing.Literal['instanceFamily', 'instanceType', 'productDescription', 'region', 'tenancy']]

### value
- **Type**: typing.Optional[str]


# SavingsPlanRateTypeDef

### rate
- **Type**: typing.Optional[str]

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### unit
- **Type**: typing.Optional[typing.Literal['Hrs', 'Lambda-GB-Second', 'Request']]

### productType
- **Type**: typing.Optional[typing.Literal['EC2', 'Fargate', 'Lambda', 'SageMaker']]

### serviceCode
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'AmazonEC2', 'AmazonECS', 'AmazonEKS', 'AmazonSageMaker']]

### usageType
- **Type**: typing.Optional[str]

### operation
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.savingsplans_classes.SavingsPlanRatePropertyTypeDef]]


# SavingsPlanTypeDef

### offeringId
- **Type**: typing.Optional[str]

### savingsPlanId
- **Type**: typing.Optional[str]

### savingsPlanArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### start
- **Type**: typing.Optional[str]

### end
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['active', 'payment-failed', 'payment-pending', 'pending-return', 'queued', 'queued-deleted', 'retired', 'returned']]

### region
- **Type**: typing.Optional[str]

### ec2InstanceFamily
- **Type**: typing.Optional[str]

### savingsPlanType
- **Type**: typing.Optional[typing.Literal['Compute', 'EC2Instance', 'SageMaker']]

### paymentOption
- **Type**: typing.Optional[typing.Literal['All Upfront', 'No Upfront', 'Partial Upfront']]

### productTypes
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'Fargate', 'Lambda', 'SageMaker']]]

### currency
- **Type**: typing.Optional[typing.Literal['CNY', 'USD']]

### commitment
- **Type**: typing.Optional[str]

### upfrontPaymentAmount
- **Type**: typing.Optional[str]

### recurringPaymentAmount
- **Type**: typing.Optional[str]

### termDurationInSeconds
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### returnableUntil
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


