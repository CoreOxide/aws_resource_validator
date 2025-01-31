# Service Quotas Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef

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


# GetAWSDefaultServiceQuotaRequestRequestTypeDef

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


# GetRequestedServiceQuotaChangeRequestRequestTypeDef

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


# GetServiceQuotaIncreaseRequestFromTemplateRequestRequestTypeDef

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


# GetServiceQuotaRequestRequestTypeDef

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


# ListAWSDefaultServiceQuotasRequestListAWSDefaultServiceQuotasPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListAWSDefaultServiceQuotasRequestRequestTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAWSDefaultServiceQuotasResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Quotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRequestedServiceQuotaChangeHistoryByQuotaRequestListRequestedServiceQuotaChangeHistoryByQuotaPaginateTypeDef

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


# ListRequestedServiceQuotaChangeHistoryByQuotaRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.RequestedServiceQuotaChangeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRequestedServiceQuotaChangeHistoryRequestListRequestedServiceQuotaChangeHistoryPaginateTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'CASE_CLOSED', 'CASE_OPENED', 'DENIED', 'INVALID_REQUEST', 'NOT_APPROVED', 'PENDING']]

### QuotaRequestedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListRequestedServiceQuotaChangeHistoryRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedQuotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.RequestedServiceQuotaChangeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceQuotaIncreaseRequestsInTemplateRequestListServiceQuotaIncreaseRequestsInTemplatePaginateTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListServiceQuotaIncreaseRequestsInTemplateRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceQuotasRequestListServiceQuotasPaginateTypeDef

### ServiceCode
- **Type**: <class 'str'>
- **Required**: Yes

### QuotaCode
- **Type**: typing.Optional[str]

### QuotaAppliedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListServiceQuotasRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Quotas
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceQuotaTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesRequestListServicesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.PaginatorConfigTypeDef]


# ListServicesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListServicesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.service_quotas_classes.ServiceInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.service_quotas_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# PutServiceQuotaIncreaseRequestIntoTemplateRequestRequestTypeDef

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


# RequestServiceQuotaIncreaseRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.QuotaContextInfoTypeDef]


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


# ServiceInfoTypeDef

### ServiceCode
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]


# ServiceQuotaIncreaseRequestInTemplateTypeDef

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


# ServiceQuotaTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.MetricInfoTypeDef]

### Period
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.QuotaPeriodTypeDef]

### ErrorReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.ErrorReasonTypeDef]

### QuotaAppliedAtLevel
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ALL', 'RESOURCE']]

### QuotaContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.service_quotas_classes.QuotaContextInfoTypeDef]


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


