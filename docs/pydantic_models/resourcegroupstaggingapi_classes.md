# resourcegroupstaggingapi_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComplianceDetailsTypeDef

### NoncompliantKeys
- **Type**: typing.Optional[typing.List[str]]

### KeysWithNoncompliantValues
- **Type**: typing.Optional[typing.List[str]]

### ComplianceStatus
- **Type**: typing.Optional[bool]


# DescribeReportCreationOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailureInfoTypeDef

### StatusCode
- **Type**: typing.Optional[int]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalServiceException', 'InvalidParameterException']]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetComplianceSummaryInputGetComplianceSummaryPaginateTypeDef

### TargetIdFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### RegionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### TagKeyFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### GroupBy
- **Type**: typing.Optional[typing.Sequence[typing.Literal['REGION', 'RESOURCE_TYPE', 'TARGET_ID']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.PaginatorConfigTypeDef]


# GetComplianceSummaryInputRequestTypeDef

### TargetIdFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### RegionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### TagKeyFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### GroupBy
- **Type**: typing.Optional[typing.Sequence[typing.Literal['REGION', 'RESOURCE_TYPE', 'TARGET_ID']]]

### MaxResults
- **Type**: typing.Optional[int]

### PaginationToken
- **Type**: typing.Optional[str]


# GetComplianceSummaryOutputTypeDef

### SummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.SummaryTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcesInputGetResourcesPaginateTypeDef

### TagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.TagFilterTypeDef]]

### TagsPerPage
- **Type**: typing.Optional[int]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeComplianceDetails
- **Type**: typing.Optional[bool]

### ExcludeCompliantResources
- **Type**: typing.Optional[bool]

### ResourceARNList
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.PaginatorConfigTypeDef]


# GetResourcesInputRequestTypeDef

### PaginationToken
- **Type**: typing.Optional[str]

### TagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.TagFilterTypeDef]]

### ResourcesPerPage
- **Type**: typing.Optional[int]

### TagsPerPage
- **Type**: typing.Optional[int]

### ResourceTypeFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeComplianceDetails
- **Type**: typing.Optional[bool]

### ExcludeCompliantResources
- **Type**: typing.Optional[bool]

### ResourceARNList
- **Type**: typing.Optional[typing.Sequence[str]]


# GetResourcesOutputTypeDef

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTagMappingList
- **Type**: typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResourceTagMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTagKeysInputGetTagKeysPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.PaginatorConfigTypeDef]


# GetTagKeysInputRequestTypeDef

### PaginationToken
- **Type**: typing.Optional[str]


# GetTagKeysOutputTypeDef

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTagValuesInputGetTagValuesPaginateTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.PaginatorConfigTypeDef]


# GetTagValuesInputRequestTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationToken
- **Type**: typing.Optional[str]


# GetTagValuesOutputTypeDef

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResourceTagMappingTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.TagTypeDef]]

### ComplianceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ComplianceDetailsTypeDef]


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


# StartReportCreationInputRequestTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# SummaryTypeDef

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


# TagFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# TagResourcesInputRequestTypeDef

### ResourceARNList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagResourcesOutputTypeDef

### FailedResourcesMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.FailureInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourcesInputRequestTypeDef

### ResourceARNList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourcesOutputTypeDef

### FailedResourcesMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.FailureInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.resourcegroupstaggingapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


