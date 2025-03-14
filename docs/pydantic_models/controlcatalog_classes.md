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

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.AssociatedDomainSummaryTypeDef'>
- **Required**: Yes

### Objective
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.AssociatedObjectiveSummaryTypeDef'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ControlParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ControlSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# DomainResourceFilterTypeDef

### Arn
- **Type**: typing.Optional[str]


# DomainSummaryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetControlRequestTypeDef

### ControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetControlResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Behavior
- **Type**: typing.Literal['DETECTIVE', 'PREVENTIVE', 'PROACTIVE']
- **Required**: Yes

### RegionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.RegionConfigurationTypeDef'>
- **Required**: Yes

### Implementation
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ImplementationDetailsTypeDef'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.ControlParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImplementationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListCommonControlsRequestPaginateTypeDef

### CommonControlFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.CommonControlFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListCommonControlsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### CommonControlFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.CommonControlFilterTypeDef]


# ListCommonControlsResponseTypeDef

### CommonControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.CommonControlSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListControlsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListControlsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListControlsResponseTypeDef

### Controls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.ControlSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListDomainsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsResponseTypeDef

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.DomainSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectivesRequestPaginateTypeDef

### ObjectiveFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.PaginatorConfigTypeDef]


# ListObjectivesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ObjectiveFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveFilterTypeDef]


# ListObjectivesResponseTypeDef

### Objectives
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog_classes.ObjectiveSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog_classes.AssociatedDomainSummaryTypeDef'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegionConfigurationTypeDef

### Scope
- **Type**: typing.Literal['GLOBAL', 'REGIONAL']
- **Required**: Yes

### DeployableRegions
- **Type**: typing.Optional[typing.List[str]]


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


