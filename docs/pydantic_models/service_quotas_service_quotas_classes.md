# Service Quotas Service Quotas Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteServiceQuotaIncreaseRequestFromTemplateRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorReason

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DEPENDENCY_ACCESS_DENIED_ERROR', 'DEPENDENCY_SERVICE_ERROR', 'DEPENDENCY_THROTTLING_ERROR', 'SERVICE_QUOTA_NOT_AVAILABLE_ERROR']]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAWSDefaultServiceQuotaRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetAWSDefaultServiceQuotaResponse

### Quota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuota'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssociationForServiceQuotaTemplateResponse

### ServiceQuotaTemplateAssociationStatus
- **Type**: typing.Literal['ASSOCIATED', 'DISASSOCIATED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# GetRequestedServiceQuotaChangeRequest

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRequestedServiceQuotaChangeResponse

### RequestedQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.RequestedServiceQuotaChange'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceQuotaIncreaseRequestFromTemplateRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceQuotaIncreaseRequestFromTemplateResponse

### ServiceQuotaIncreaseRequestInTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuotaIncreaseRequestInTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceQuotaRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: <class 'str'>
- **Required**: Yes

### ContextId
- **Type**: typing.Optional[str]


# GetServiceQuotaResponse

### Quota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuota'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# ListAWSDefaultServiceQuotasRequest

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAWSDefaultServiceQuotasRequestPaginate

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.PaginatorConfig]


# ListAWSDefaultServiceQuotasResponse

### Quotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuota]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRequestedServiceQuotaChangeHistoryByQuotaRequest

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


# ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.PaginatorConfig]


# ListRequestedServiceQuotaChangeHistoryByQuotaResponse

### RequestedQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.RequestedServiceQuotaChange]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRequestedServiceQuotaChangeHistoryRequest

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


# ListRequestedServiceQuotaChangeHistoryRequestPaginate

### ServiceCode
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.PaginatorConfig]


# ListRequestedServiceQuotaChangeHistoryResponse

### RequestedQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.RequestedServiceQuotaChange]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceQuotaIncreaseRequestsInTemplateRequest

### ServiceCode
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServiceQuotaIncreaseRequestsInTemplateRequestPaginate

### ServiceCode
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.PaginatorConfig]


# ListServiceQuotaIncreaseRequestsInTemplateResponse

### ServiceQuotaIncreaseRequestInTemplateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuotaIncreaseRequestInTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceQuotasRequest

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


# ListServiceQuotasRequestPaginate

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaAppliedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.PaginatorConfig]


# ListServiceQuotasResponse

### Quotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuota]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServicesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServicesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.PaginatorConfig]


# ListServicesResponse

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# MetricInfo

### MetricNamespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### MetricDimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### MetricStatisticRecommendation
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutServiceQuotaIncreaseRequestIntoTemplateRequest

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


# PutServiceQuotaIncreaseRequestIntoTemplateResponse

### ServiceQuotaIncreaseRequestInTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ServiceQuotaIncreaseRequestInTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# QuotaContextInfo

### ContextScope
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'RESOURCE']]

### ContextScopeType
- **Type**: typing.Optional[str]

### ContextId
- **Type**: typing.Optional[str]


# QuotaPeriod

### PeriodValue
- **Type**: typing.Optional[int]

### PeriodUnit
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MICROSECOND', 'MILLISECOND', 'MINUTE', 'SECOND', 'WEEK']]


# RequestServiceQuotaIncreaseRequest

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


# RequestServiceQuotaIncreaseResponse

### RequestedQuota
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.RequestedServiceQuotaChange'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.ResponseMetadata'>
- **Required**: Yes


# RequestedServiceQuotaChange

### Id
- **Type**: typing.Optional[str]

### CaseId
- **Type**: typing.Optional[str]

### ServiceCode
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaName
- **Type**: typing.Optional[str]

### DesiredValue
- **Type**: typing.Optional[float]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### Requester
- **Type**: typing.Optional[str]

### QuotaArn
- **Type**: typing.Optional[str]

### GlobalQuota
- **Type**: typing.Optional[bool]

### Unit
- **Type**: typing.Optional[str]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### QuotaContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.QuotaContextInfo]


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


# ServiceInfo

### ServiceCode
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]


# ServiceQuota

### ServiceCode
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### QuotaArn
- **Type**: typing.Optional[str]

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[str]

### Adjustable
- **Type**: typing.Optional[bool]

### GlobalQuota
- **Type**: typing.Optional[bool]

### UsageMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.MetricInfo]

### Period
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.QuotaPeriod]

### ErrorReason
- **Type**: <class 'NoneType'>

### QuotaAppliedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### QuotaContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.QuotaContextInfo]


# ServiceQuotaIncreaseRequestInTemplate

### ServiceCode
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaName
- **Type**: typing.Optional[str]

### DesiredValue
- **Type**: typing.Optional[float]

### AwsRegion
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]

### GlobalQuota
- **Type**: typing.Optional[bool]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas.service_quotas_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


