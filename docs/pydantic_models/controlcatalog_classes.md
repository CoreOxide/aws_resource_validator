# Controlcatalog Classes

# AssociatedDomainSummary

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# AssociatedObjectiveSummary

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommonControlFilter

### Objectives
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ObjectiveResourceFilter]]


# CommonControlSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.AssociatedDomainSummary'>
- **Required**: Yes

### Objective
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.AssociatedObjectiveSummary'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ControlParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ControlSummary

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# DomainResourceFilter

### Arn
- **Type**: typing.Optional[str]


# DomainSummary

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


# GetControlRequest

### ControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetControlResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.RegionConfiguration'>
- **Required**: Yes

### Implementation
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ImplementationDetails'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ControlParameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ResponseMetadata'>
- **Required**: Yes


# ImplementationDetails

### Type
- **Type**: <class 'str'>
- **Required**: Yes


# ListCommonControlsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### CommonControlFilter
- **Type**: <class 'NoneType'>


# ListCommonControlsRequestPaginate

### CommonControlFilter
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.PaginatorConfig]


# ListCommonControlsResponse

### CommonControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.CommonControlSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListControlsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListControlsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.PaginatorConfig]


# ListControlsResponse

### Controls
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ControlSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.PaginatorConfig]


# ListDomainsResponse

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.DomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectivesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ObjectiveFilter
- **Type**: <class 'NoneType'>


# ListObjectivesRequestPaginate

### ObjectiveFilter
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.PaginatorConfig]


# ListObjectivesResponse

### Objectives
- **Type**: typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ObjectiveSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ObjectiveFilter

### Domains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.DomainResourceFilter]]


# ObjectiveResourceFilter

### Arn
- **Type**: typing.Optional[str]


# ObjectiveSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_classes.AssociatedDomainSummary'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegionConfiguration

### Scope
- **Type**: typing.Literal['GLOBAL', 'REGIONAL']
- **Required**: Yes

### DeployableRegions
- **Type**: typing.Optional[typing.List[str]]


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


