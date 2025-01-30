# appintegrations_classes

# ApplicationAssociationSummaryTypeDef

### ApplicationAssociationArn
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]


# ApplicationSourceConfigTypeDef

### ExternalUrlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ExternalUrlConfigTypeDef]


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

# CreateApplicationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigTypeDef'>
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


# CreateDataIntegrationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: <class 'str'>
- **Required**: Yes

### SourceURI
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ScheduleConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientToken
- **Type**: typing.Optional[str]

### FileConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationTypeDef'>
- **Required**: Yes

### ObjectConfiguration
- **Type**: typing.Dict[str, typing.Dict[str, typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventIntegrationRequestRequestTypeDef

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


# DataIntegrationSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SourceURI
- **Type**: typing.Optional[str]


# DeleteApplicationRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataIntegrationRequestRequestTypeDef

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventIntegrationRequestRequestTypeDef

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


# ExternalUrlConfigTypeDef

### AccessUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ApprovedOrigins
- **Type**: typing.Optional[typing.Sequence[str]]


# FileConfigurationTypeDef

### Folders
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# GetApplicationRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigTypeDef'>
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


# GetDataIntegrationRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.FileConfigurationTypeDef'>
- **Required**: Yes

### ObjectConfiguration
- **Type**: typing.Dict[str, typing.Dict[str, typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventIntegrationRequestRequestTypeDef

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


# ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListApplicationAssociationsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationsRequestListApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef

### DataIntegrationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListDataIntegrationAssociationsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListDataIntegrationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataIntegrationsResponseTypeDef

### DataIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.DataIntegrationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef

### EventIntegrationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListEventIntegrationAssociationsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.PaginatorConfigTypeDef]


# ListEventIntegrationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventIntegrationsResponseTypeDef

### EventIntegrations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appintegrations_classes.EventIntegrationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appintegrations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ApplicationSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appintegrations_classes.ApplicationSourceConfigTypeDef]

### Subscriptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.SubscriptionTypeDef]]

### Publications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appintegrations_classes.PublicationTypeDef]]

### Permissions
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateDataIntegrationRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateEventIntegrationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


