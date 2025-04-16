# Appintegrations Classes

# ApplicationAssociationSummary

### ApplicationAssociationArn
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]


# ApplicationSourceConfig

### ExternalUrlConfig
- **Type**: <class 'NoneType'>


# ApplicationSourceConfigOutput

### ExternalUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ExternalUrlConfigOutput]


# ApplicationSourceConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplicationSummary

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigUnion'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.Subscription]]

### Publications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.Publication]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateApplicationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataIntegrationAssociationRequest

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### ObjectConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Sequence[str]]]]

### DestinationURI
- **Type**: typing.Optional[str]

### ClientAssociationMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]

### ExecutionConfiguration
- **Type**: <class 'NoneType'>


# CreateDataIntegrationAssociationResponse

### DataIntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### DataIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataIntegrationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SourceURI
- **Type**: typing.Optional[str]

### ScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfiguration]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]

### FileConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationUnion]

### ObjectConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Sequence[str]]]]


# CreateDataIntegrationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes

### SourceURI
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfiguration'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationOutput'>
- **Required**: Yes

### ObjectConfiguration
- **Type**: typing.Dict[str, typing.Dict[str, typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventIntegrationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.EventFilter'>
- **Required**: Yes

### EventBridgeBus
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEventIntegrationResponse

### EventIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# DataIntegrationAssociationSummary

### DataIntegrationAssociationArn
- **Type**: typing.Optional[str]

### DataIntegrationArn
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### DestinationURI
- **Type**: typing.Optional[str]

### LastExecutionStatus
- **Type**: <class 'NoneType'>

### ExecutionConfiguration
- **Type**: <class 'NoneType'>


# DataIntegrationSummary

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SourceURI
- **Type**: typing.Optional[str]


# DeleteApplicationRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataIntegrationRequest

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventIntegrationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# EventFilter

### Source
- **Type**: <class 'str'>
- **Required**: Yes


# EventIntegration

### EventIntegrationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: <class 'NoneType'>

### EventBridgeBus
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventIntegrationAssociation

### EventIntegrationAssociationArn
- **Type**: typing.Optional[str]

### EventIntegrationAssociationId
- **Type**: typing.Optional[str]

### EventIntegrationName
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### EventBridgeRuleName
- **Type**: typing.Optional[str]

### ClientAssociationMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExecutionConfiguration

### ExecutionMode
- **Type**: typing.Literal['ON_DEMAND', 'SCHEDULED']
- **Required**: Yes

### OnDemandConfiguration
- **Type**: <class 'NoneType'>

### ScheduleConfiguration
- **Type**: <class 'NoneType'>


# ExternalUrlConfig

### AccessUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovedOrigins
- **Type**: typing.Optional[typing.Sequence[str]]


# ExternalUrlConfigOutput

### AccessUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovedOrigins
- **Type**: typing.Optional[typing.List[str]]


# FileConfiguration

### Folders
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# FileConfigurationOutput

### Folders
- **Type**: typing.List[str]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# FileConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetApplicationRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigOutput'>
- **Required**: Yes

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.Subscription]
- **Required**: Yes

### Publications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.Publication]
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Permissions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataIntegrationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataIntegrationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes

### SourceURI
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfiguration'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### FileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationOutput'>
- **Required**: Yes

### ObjectConfiguration
- **Type**: typing.Dict[str, typing.Dict[str, typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventIntegrationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventIntegrationResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventBridgeBus
- **Type**: <class 'str'>
- **Required**: Yes

### EventFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.EventFilter'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# LastExecutionStatus

### ExecutionStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]


# ListApplicationAssociationsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationAssociationsRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfig]


# ListApplicationAssociationsResponse

### ApplicationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfig]


# ListApplicationsResponse

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataIntegrationAssociationsRequest

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationAssociationsRequestPaginate

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfig]


# ListDataIntegrationAssociationsResponse

### DataIntegrationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.DataIntegrationAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataIntegrationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfig]


# ListDataIntegrationsResponse

### DataIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.DataIntegrationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventIntegrationAssociationsRequest

### EventIntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventIntegrationAssociationsRequestPaginate

### EventIntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfig]


# ListEventIntegrationAssociationsResponse

### EventIntegrationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.EventIntegrationAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventIntegrationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventIntegrationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfig]


# ListEventIntegrationsResponse

### EventIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.EventIntegration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadata'>
- **Required**: Yes


# OnDemandConfiguration

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Publication

### Event
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### Description
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


# ScheduleConfiguration

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### FirstExecutionFrom
- **Type**: typing.Optional[str]

### Object
- **Type**: typing.Optional[str]


# Subscription

### Event
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ApplicationSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigUnion]

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.Subscription]]

### Publications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.Publication]]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDataIntegrationAssociationRequest

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataIntegrationAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ExecutionConfiguration'>
- **Required**: Yes


# UpdateDataIntegrationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateEventIntegrationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


