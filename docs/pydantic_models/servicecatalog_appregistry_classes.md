# Servicecatalog Appregistry Classes

# AppRegistryConfiguration

### tagQueryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.TagQueryConfiguration]


# Application

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


# ApplicationSummary

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


# ApplicationTagResult

### applicationTagStatus
- **Type**: typing.Optional[typing.Literal['FAILURE', 'IN_PROGRESS', 'SUCCESS']]

### errorMessage
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourcesListItem]]

### nextToken
- **Type**: typing.Optional[str]


# AssociateAttributeGroupRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateAttributeGroupResponse

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResourceRequest

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
- **Type**: typing.Optional[typing.List[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]]


# AssociateResourceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# AttributeGroup

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


# AttributeGroupDetails

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### createdBy
- **Type**: typing.Optional[str]


# AttributeGroupSummary

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateApplicationResponse

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.Application'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAttributeGroupRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAttributeGroupResponse

### attributeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AttributeGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationResponse

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ApplicationSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAttributeGroupRequest

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttributeGroupResponse

### attributeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AttributeGroupSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateAttributeGroupRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateAttributeGroupResponse

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### attributeGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResourceRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResourceResponse

### applicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.Integrations'>
- **Required**: Yes

### applicationTag
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssociatedResourceRequest

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
- **Type**: typing.Optional[typing.List[typing.Literal['FAILED', 'IN_PROGRESS', 'SKIPPED', 'SUCCESS']]]

### maxResults
- **Type**: typing.Optional[int]


# GetAssociatedResourceResponse

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.Resource'>
- **Required**: Yes

### options
- **Type**: typing.List[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]
- **Required**: Yes

### applicationTagResult
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ApplicationTagResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# GetAttributeGroupRequest

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes


# GetAttributeGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AppRegistryConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# Integrations

### resourceGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourceGroup]

### applicationTagResourceGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourceGroup]


# ListApplicationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.PaginatorConfig]


# ListApplicationsResponse

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedAttributeGroupsRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedAttributeGroupsRequestPaginate

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.PaginatorConfig]


# ListAssociatedAttributeGroupsResponse

### attributeGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedResourcesRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedResourcesRequestPaginate

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.PaginatorConfig]


# ListAssociatedResourcesResponse

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttributeGroupsForApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttributeGroupsForApplicationRequestPaginate

### application
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.PaginatorConfig]


# ListAttributeGroupsForApplicationResponse

### attributeGroupsDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AttributeGroupDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttributeGroupsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttributeGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.PaginatorConfig]


# ListAttributeGroupsResponse

### attributeGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AttributeGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutConfigurationRequest

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AppRegistryConfiguration'>
- **Required**: Yes


# Resource

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### associationTime
- **Type**: typing.Optional[datetime.datetime]

### integrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourceIntegrations]


# ResourceDetails

### tagValue
- **Type**: typing.Optional[str]


# ResourceGroup

### state
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATING', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATING']]

### arn
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# ResourceInfo

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']]

### resourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourceDetails]

### options
- **Type**: typing.Optional[typing.List[typing.Literal['APPLY_APPLICATION_TAG', 'SKIP_APPLICATION_TAG']]]


# ResourceIntegrations

### resourceGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResourceGroup]


# ResourcesListItem

### resourceArn
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### resourceType
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


# SyncResourceRequest

### resourceType
- **Type**: typing.Literal['CFN_STACK', 'RESOURCE_TAG_VALUE']
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# SyncResourceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# TagQueryConfiguration

### tagKey
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationRequest

### application
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateApplicationResponse

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.Application'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAttributeGroupRequest

### attributeGroup
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[str]


# UpdateAttributeGroupResponse

### attributeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.AttributeGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_classes.ResponseMetadata'>
- **Required**: Yes


