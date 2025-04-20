# Resourcegroupstaggingapi Resourcegroupstaggingapi Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComplianceDetails

### NoncompliantKeys
- **Type**: typing.Optional[typing.List[str]]

### KeysWithNoncompliantValues
- **Type**: typing.Optional[typing.List[str]]

### ComplianceStatus
- **Type**: typing.Optional[bool]


# DescribeReportCreationOutput

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### S3Location
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


# FailureInfo

### StatusCode
- **Type**: typing.Optional[int]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalServiceException', 'InvalidParameterException']]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetComplianceSummaryInput

### TargetIdFilters
- **Type**: typing.Optional[typing.List[str]]

### RegionFilters
- **Type**: typing.Optional[typing.List[str]]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.List[str]]

### TagKeyFilters
- **Type**: typing.Optional[typing.List[str]]

### GroupBy
- **Type**: typing.Optional[typing.List[typing.Literal['REGION', 'RESOURCE_TYPE', 'TARGET_ID']]]

### MaxResults
- **Type**: typing.Optional[int]

### PaginationToken
- **Type**: typing.Optional[str]


# GetComplianceSummaryInputPaginate

### TargetIdFilters
- **Type**: typing.Optional[typing.List[str]]

### RegionFilters
- **Type**: typing.Optional[typing.List[str]]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.List[str]]

### TagKeyFilters
- **Type**: typing.Optional[typing.List[str]]

### GroupBy
- **Type**: typing.Optional[typing.List[typing.Literal['REGION', 'RESOURCE_TYPE', 'TARGET_ID']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.PaginatorConfig]


# GetComplianceSummaryOutput

### SummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.Summary]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcesInput

### PaginationToken
- **Type**: typing.Optional[str]

### TagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.TagFilter]]

### ResourcesPerPage
- **Type**: typing.Optional[int]

### TagsPerPage
- **Type**: typing.Optional[int]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.List[str]]

### IncludeComplianceDetails
- **Type**: typing.Optional[bool]

### ExcludeCompliantResources
- **Type**: typing.Optional[bool]

### ResourceARNList
- **Type**: typing.Optional[typing.List[str]]


# GetResourcesInputPaginate

### TagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.TagFilter]]

### TagsPerPage
- **Type**: typing.Optional[int]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.List[str]]

### IncludeComplianceDetails
- **Type**: typing.Optional[bool]

### ExcludeCompliantResources
- **Type**: typing.Optional[bool]

### ResourceARNList
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.PaginatorConfig]


# GetResourcesOutput

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagMappingList
- **Type**: typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResourceTagMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


# GetTagKeysInput

### PaginationToken
- **Type**: typing.Optional[str]


# GetTagKeysInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.PaginatorConfig]


# GetTagKeysOutput

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


# GetTagValuesInput

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationToken
- **Type**: typing.Optional[str]


# GetTagValuesInputPaginate

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.PaginatorConfig]


# GetTagValuesOutput

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTagMapping

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.Tag]]

### ComplianceDetails
- **Type**: <class 'NoneType'>


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


# StartReportCreationInput

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# Summary

### LastUpdated
- **Type**: typing.Optional[str]

### TargetId
- **Type**: typing.Optional[str]

### TargetIdType
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'OU', 'ROOT']]

### Region
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### NonCompliantResources
- **Type**: typing.Optional[int]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagFilter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TagResourcesInput

### ResourceARNList
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagResourcesOutput

### FailedResourcesMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.FailureInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourcesInput

### ResourceARNList
- **Type**: typing.List[str]
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourcesOutput

### FailedResourcesMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.FailureInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_classes.ResponseMetadata'>
- **Required**: Yes


