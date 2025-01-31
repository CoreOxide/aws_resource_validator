# servicecatalog_appregistry_classes

# AppRegistryConfigurationTypeDef

### tagQueryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.TagQueryConfigurationTypeDef]


# ApplicationSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# ApplicationTagResultTypeDef

### applicationTagStatus
- **Type**: typing.Optional[typing.Literal['FAILURE', 'IN_PROGRESS', 'SUCCESS']]

### errorMessage
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourcesListItemTypeDef]]

### nextToken
- **Type**: typing.Optional[str]


# ApplicationTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### applicationTag
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssociateAttributeGroupRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateAttributeGroupResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResourceRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Sequence[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]]


# AssociateResourceResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.List[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttributeGroupDetailsTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### createdBy
- **Type**: typing.Optional[str]


# AttributeGroupSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]


# AttributeGroupTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationResponseTypeDef

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAttributeGroupRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAttributeGroupResponseTypeDef

### attributeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AttributeGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationResponseTypeDef

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ApplicationSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAttributeGroupRequestRequestTypeDef

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttributeGroupResponseTypeDef

### attributeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AttributeGroupSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateAttributeGroupRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateAttributeGroupResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResourceRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResourceResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### associatedResourceCount
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### integrations
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.IntegrationsTypeDef'>
- **Required**: Yes

### applicationTag
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssociatedResourceRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### resourceTagStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'IN_PROGRESS', 'SKIPPED', 'SUCCESS']]]

### maxResults
- **Type**: typing.Optional[int]


# GetAssociatedResourceResponseTypeDef

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceTypeDef'>
- **Required**: Yes

### options
- **Type**: typing.List[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]
- **Required**: Yes

### applicationTagResult
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ApplicationTagResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAttributeGroupRequestRequestTypeDef

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# GetAttributeGroupResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfigurationResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AppRegistryConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IntegrationsTypeDef

### resourceGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceGroupTypeDef]

### applicationTagResourceGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceGroupTypeDef]


# ListApplicationsRequestListApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAssociatedAttributeGroupsRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedAttributeGroupsResponseTypeDef

### attributeGroups
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedResourcesRequestListAssociatedResourcesPaginateTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAssociatedResourcesRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedResourcesResponseTypeDef

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttributeGroupsForApplicationRequestRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttributeGroupsForApplicationResponseTypeDef

### attributeGroupsDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AttributeGroupDetailsTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttributeGroupsRequestListAttributeGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAttributeGroupsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttributeGroupsResponseTypeDef

### attributeGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AttributeGroupSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutConfigurationRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AppRegistryConfigurationTypeDef'>
- **Required**: Yes


# ResourceDetailsTypeDef

### tagValue
- **Type**: typing.Optional[str]


# ResourceGroupTypeDef

### state
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATING', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATING']]

### arn
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# ResourceInfoTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']]

### resourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceDetailsTypeDef]

### options
- **Type**: typing.Optional[typing.List[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]]


# ResourceIntegrationsTypeDef

### resourceGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceGroupTypeDef]


# ResourceTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### associationTime
- **Type**: typing.Optional[datetime.datetime]

### integrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResourceIntegrationsTypeDef]


# ResourcesListItemTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### resourceType
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


# SyncResourceRequestRequestTypeDef

### resourceType
- **Type**: typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# SyncResourceResponseTypeDef

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### actionTaken
- **Type**: typing.Literal['NO_ACTION', 'START_SYNC']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagQueryConfigurationTypeDef

### tagKey
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

### application
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateApplicationResponseTypeDef

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAttributeGroupRequestRequestTypeDef

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[str]


# UpdateAttributeGroupResponseTypeDef

### attributeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AttributeGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


