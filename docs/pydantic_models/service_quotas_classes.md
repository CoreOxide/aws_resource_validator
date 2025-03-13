# Service Quotas Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteServiceQuotaIncreaseRequestFromTemplateRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorReasonTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DEPENDENCY_ACCESS_DENIED_ERROR', 'DEPENDENCY_SERVICE_ERROR', 'DEPENDENCY_THROTTLING_ERROR', 'SERVICE_QUOTA_NOT_AVAILABLE_ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAWSDefaultServiceQuotaRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetAWSDefaultServiceQuotaResponseTypeDef

### Quota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssociationForServiceQuotaTemplateResponseTypeDef

### ServiceQuotaTemplateAssociationStatus
- **Type**: typing.Literal['ASSOCIATED', 'DISASSOCIATED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRequestedServiceQuotaChangeRequestTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRequestedServiceQuotaChangeResponseTypeDef

### RequestedQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.RequestedServiceQuotaChangeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceQuotaIncreaseRequestFromTemplateRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef

### ServiceQuotaIncreaseRequestInTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaIncreaseRequestInTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceQuotaRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ContextId
- **Type**: typing.Optional[str]


# GetServiceQuotaResponseTypeDef

### Quota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAWSDefaultServiceQuotasRequestPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListAWSDefaultServiceQuotasRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAWSDefaultServiceQuotasResponseTypeDef

### Quotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListRequestedServiceQuotaChangeHistoryByQuotaRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]


# ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef

### RequestedQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.RequestedServiceQuotaChangeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListRequestedServiceQuotaChangeHistoryRequestTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]


# ListRequestedServiceQuotaChangeHistoryResponseTypeDef

### RequestedQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.RequestedServiceQuotaChangeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListServiceQuotaIncreaseRequestsInTemplateRequestTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef

### ServiceQuotaIncreaseRequestInTemplateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaIncreaseRequestInTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceQuotasRequestPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaAppliedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListServiceQuotasRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaAppliedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]


# ListServiceQuotasResponseTypeDef

### Quotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListServicesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServicesResponseTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricInfoTypeDef

### MetricNamespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### MetricDimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetricStatisticRecommendation
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutServiceQuotaIncreaseRequestIntoTemplateRequestTypeDef

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredValue
- **Type**: <class 'float'>
- **Required**: Yes


# PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef

### ServiceQuotaIncreaseRequestInTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaIncreaseRequestInTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QuotaContextInfoTypeDef

### ContextScope
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'RESOURCE']]

### ContextScopeType
- **Type**: typing.Optional[str]

### ContextId
- **Type**: typing.Optional[str]


# QuotaPeriodTypeDef

### PeriodValue
- **Type**: typing.Optional[int]

### PeriodUnit
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MICROSECOND', 'MILLISECOND', 'MINUTE', 'SECOND', 'WEEK']]


# RequestServiceQuotaIncreaseRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredValue
- **Type**: <class 'float'>
- **Required**: Yes

### ContextId
- **Type**: typing.Optional[str]


# RequestServiceQuotaIncreaseResponseTypeDef

### RequestedQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.RequestedServiceQuotaChangeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestedServiceQuotaChangeTypeDef

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


# ServiceInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceQuotaIncreaseRequestInTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceQuotaTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.service_quotas_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


