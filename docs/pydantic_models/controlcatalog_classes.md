# Controlcatalog Classes

# AssociatedDomainSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# AssociatedObjectiveSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommonControlFilterTypeDef

### Objectives
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveResourceFilterTypeDef]]


# CommonControlSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.AssociatedDomainSummaryTypeDef'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Objective
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.AssociatedObjectiveSummaryTypeDef'>
- **Required**: Yes


# DomainResourceFilterTypeDef

### Arn
- **Type**: typing.Optional[str]


# DomainSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ListCommonControlsRequestListCommonControlsPaginateTypeDef

### CommonControlFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.CommonControlFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListCommonControlsRequestRequestTypeDef

### CommonControlFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.CommonControlFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCommonControlsResponseTypeDef

### CommonControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.CommonControlSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsRequestListDomainsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListDomainsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsResponseTypeDef

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.DomainSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListObjectivesRequestListObjectivesPaginateTypeDef

### ObjectiveFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListObjectivesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ObjectiveFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveFilterTypeDef]


# ListObjectivesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Objectives
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ObjectiveFilterTypeDef

### Domains
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.controlcatalog_classes.DomainResourceFilterTypeDef]]


# ObjectiveResourceFilterTypeDef

### Arn
- **Type**: typing.Optional[str]


# ObjectiveSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.AssociatedDomainSummaryTypeDef'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


