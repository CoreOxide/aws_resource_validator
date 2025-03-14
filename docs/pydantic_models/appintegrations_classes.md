# Appintegrations Classes

# ApplicationAssociationSummaryTypeDef

### ApplicationAssociationArn
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]


# ApplicationSourceConfigOutputTypeDef

### ExternalUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ExternalUrlConfigOutputTypeDef]


# ApplicationSourceConfigTypeDef

### ExternalUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ExternalUrlConfigTypeDef]


# ApplicationSourceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplicationSummaryTypeDef

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

# CreateApplicationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.SubscriptionTypeDef]]

### Publications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.PublicationTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateApplicationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataIntegrationAssociationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ExecutionConfigurationTypeDef]


# CreateDataIntegrationAssociationResponseTypeDef

### DataIntegrationAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### DataIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataIntegrationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]

### FileConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationUnionTypeDef]

### ObjectConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Sequence[str]]]]


# CreateDataIntegrationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationOutputTypeDef'>
- **Required**: Yes

### ObjectConfiguration
- **Type**: typing.Dict[str, typing.Dict[str, typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventIntegrationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.EventFilterTypeDef'>
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


# CreateEventIntegrationResponseTypeDef

### EventIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataIntegrationAssociationSummaryTypeDef

### DataIntegrationAssociationArn
- **Type**: typing.Optional[str]

### DataIntegrationArn
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### DestinationURI
- **Type**: typing.Optional[str]

### LastExecutionStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.LastExecutionStatusTypeDef]

### ExecutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ExecutionConfigurationTypeDef]


# DataIntegrationSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SourceURI
- **Type**: typing.Optional[str]


# DeleteApplicationRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataIntegrationRequestTypeDef

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventIntegrationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# EventFilterTypeDef

### Source
- **Type**: <class 'str'>
- **Required**: Yes


# EventIntegrationAssociationTypeDef

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


# EventIntegrationTypeDef

### EventIntegrationArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EventFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.EventFilterTypeDef]

### EventBridgeBus
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExecutionConfigurationTypeDef

### ExecutionMode
- **Type**: typing.Literal['ON_DEMAND', 'SCHEDULED']
- **Required**: Yes

### OnDemandConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.OnDemandConfigurationTypeDef]

### ScheduleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfigurationTypeDef]


# ExternalUrlConfigOutputTypeDef

### AccessUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovedOrigins
- **Type**: typing.Optional[typing.List[str]]


# ExternalUrlConfigTypeDef

### AccessUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovedOrigins
- **Type**: typing.Optional[typing.Sequence[str]]


# FileConfigurationOutputTypeDef

### Folders
- **Type**: typing.List[str]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# FileConfigurationTypeDef

### Folders
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# FileConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetApplicationRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigOutputTypeDef'>
- **Required**: Yes

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.SubscriptionTypeDef]
- **Required**: Yes

### Publications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.PublicationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataIntegrationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataIntegrationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### FileConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationOutputTypeDef'>
- **Required**: Yes

### ObjectConfiguration
- **Type**: typing.Dict[str, typing.Dict[str, typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventIntegrationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventIntegrationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.EventFilterTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LastExecutionStatusTypeDef

### ExecutionStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]


# ListApplicationAssociationsRequestPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListApplicationAssociationsRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationAssociationsResponseTypeDef

### ApplicationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataIntegrationAssociationsRequestPaginateTypeDef

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListDataIntegrationAssociationsRequestTypeDef

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationAssociationsResponseTypeDef

### DataIntegrationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.DataIntegrationAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataIntegrationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListDataIntegrationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationsResponseTypeDef

### DataIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.DataIntegrationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventIntegrationAssociationsRequestPaginateTypeDef

### EventIntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListEventIntegrationAssociationsRequestTypeDef

### EventIntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventIntegrationAssociationsResponseTypeDef

### EventIntegrationAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.EventIntegrationAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventIntegrationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListEventIntegrationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventIntegrationsResponseTypeDef

### EventIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.EventIntegrationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OnDemandConfigurationTypeDef

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublicationTypeDef

### Event
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### Description
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


# ScheduleConfigurationTypeDef

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### FirstExecutionFrom
- **Type**: typing.Optional[str]

### Object
- **Type**: typing.Optional[str]


# SubscriptionTypeDef

### Event
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ApplicationSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigUnionTypeDef]

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.SubscriptionTypeDef]]

### Publications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.PublicationTypeDef]]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDataIntegrationAssociationRequestTypeDef

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DataIntegrationAssociationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ExecutionConfigurationTypeDef'>
- **Required**: Yes


# UpdateDataIntegrationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateEventIntegrationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


