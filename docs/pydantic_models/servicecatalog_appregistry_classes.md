# Servicecatalog Appregistry Classes

# AppRegistryConfigurationTypeDef

### tagQueryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.TagQueryConfigurationTypeDef]


# ApplicationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateAttributeGroupRequestTypeDef

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


# AssociateResourceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeGroupSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeGroupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequestTypeDef

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


# CreateAttributeGroupRequestTypeDef

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


# DeleteApplicationRequestTypeDef

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


# DeleteAttributeGroupRequestTypeDef

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


# DisassociateAttributeGroupRequestTypeDef

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


# DisassociateResourceRequestTypeDef

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


# GetApplicationRequestTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssociatedResourceRequestTypeDef

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


# GetAttributeGroupRequestTypeDef

### attributeGroup
- **Type**: <class 'str'>
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


# ListApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsResponseTypeDef

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedAttributeGroupsRequestPaginateTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAssociatedAttributeGroupsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedResourcesRequestPaginateTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAssociatedResourcesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttributeGroupsForApplicationRequestPaginateTypeDef

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAttributeGroupsForApplicationRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttributeGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.PaginatorConfigTypeDef]


# ListAttributeGroupsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttributeGroupsResponseTypeDef

### attributeGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.AttributeGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutConfigurationRequestTypeDef

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


# SyncResourceRequestTypeDef

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


# UpdateAttributeGroupRequestTypeDef

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


