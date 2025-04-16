# Iottwinmaker Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPutPropertyError

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entry
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueEntryOutput'>
- **Required**: Yes


# BatchPutPropertyErrorEntry

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.BatchPutPropertyError]
- **Required**: Yes


# BatchPutPropertyValuesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueEntryUnion]
- **Required**: Yes


# BatchPutPropertyValuesResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.BatchPutPropertyErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# BundleInformation

### bundleNames
- **Type**: typing.List[str]
- **Required**: Yes

### pricingTier
- **Type**: typing.Optional[typing.Literal['TIER_1', 'TIER_2', 'TIER_3', 'TIER_4']]


# CancelMetadataTransferJobRequest

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMetadataTransferJobResponse

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatus'>
- **Required**: Yes

### progress
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobProgress'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# ColumnDescription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyGroupRequest

### groupType
- **Type**: typing.Optional[typing.Literal['TABULAR']]

### propertyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]


# ComponentPropertyGroupResponse

### groupType
- **Type**: typing.Literal['TABULAR']
- **Required**: Yes

### propertyNames
- **Type**: typing.List[str]
- **Required**: Yes

### isInherited
- **Type**: <class 'bool'>
- **Required**: Yes


# ComponentRequest

### description
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequest]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequest]]


# ComponentResponse

### componentName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.Status]

### definedIn
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyResponse]]

### propertyGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupResponse]]

### syncSource
- **Type**: typing.Optional[str]

### areAllPropertiesReturned
- **Type**: typing.Optional[bool]

### compositeComponents
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentSummary]]

### areAllCompositeComponentsReturned
- **Type**: typing.Optional[bool]


# ComponentSummary

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.Status'>
- **Required**: Yes

### definedIn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### propertyGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupResponse]]

### syncSource
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]


# ComponentTypeSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.Status]

### componentTypeName
- **Type**: typing.Optional[str]


# ComponentUpdateRequest

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### description
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### propertyUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequest]]

### propertyGroupUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequest]]


# CompositeComponentRequest

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequest]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequest]]


# CompositeComponentTypeRequest

### componentTypeId
- **Type**: typing.Optional[str]


# CompositeComponentTypeResponse

### componentTypeId
- **Type**: typing.Optional[str]

### isInherited
- **Type**: typing.Optional[bool]


# CompositeComponentUpdateRequest

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### description
- **Type**: typing.Optional[str]

### propertyUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequest]]

### propertyGroupUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequest]]


# CreateComponentTypeRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### isSingleton
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### propertyDefinitions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionRequest]]

### extendsFrom
- **Type**: typing.Optional[typing.Sequence[str]]

### functions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.FunctionRequest]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyGroupRequest]]

### componentTypeName
- **Type**: typing.Optional[str]

### compositeComponentTypes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentTypeRequest]]


# CreateComponentTypeResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEntityRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### components
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentRequest]]

### compositeComponents
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentRequest]]

### parentEntityId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEntityResponse

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMetadataTransferJobRequest

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.SourceConfigurationUnion]
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DestinationConfiguration'>
- **Required**: Yes

### metadataTransferJobId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateMetadataTransferJobResponse

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSceneRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes

### contentLocation
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### capabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### sceneMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSceneResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSyncJobRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### syncRole
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSyncJobResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'INITIALIZING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### s3Location
- **Type**: typing.Optional[str]

### role
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorkspaceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# DataConnector

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataTypeOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataValue

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### integerValue
- **Type**: typing.Optional[int]

### longValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listValue
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### mapValue
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### relationshipValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.RelationshipValue]

### expression
- **Type**: typing.Optional[str]


# DataValueOutput

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### integerValue
- **Type**: typing.Optional[int]

### longValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### mapValue
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### relationshipValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.RelationshipValue]

### expression
- **Type**: typing.Optional[str]


# DataValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteComponentTypeRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentTypeResponse

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEntityRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### isRecursive
- **Type**: typing.Optional[bool]


# DeleteEntityResponse

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSceneRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSyncJobRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSyncJobResponse

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'INITIALIZING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceResponse

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityPropertyReference

### propertyName
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]

### externalIdProperty
- **Type**: typing.Optional[typing.Mapping[str, str]]

### entityId
- **Type**: typing.Optional[str]


# EntityPropertyReferenceOutput

### propertyName
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]

### externalIdProperty
- **Type**: typing.Optional[typing.Dict[str, str]]

### entityId
- **Type**: typing.Optional[str]


# EntityPropertyReferenceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntitySummary

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.Status'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### parentEntityId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### hasChildEntities
- **Type**: typing.Optional[bool]


# ErrorDetails

### code
- **Type**: typing.Optional[typing.Literal['COMPOSITE_COMPONENT_FAILURE', 'INTERNAL_FAILURE', 'PROCESSING_ERROR', 'SYNC_CREATING_ERROR', 'SYNC_DELETING_ERROR', 'SYNC_INITIALIZING_ERROR', 'SYNC_PROCESSING_ERROR', 'VALIDATION_ERROR']]

### message
- **Type**: typing.Optional[str]


# ExecuteQueryRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### queryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ExecuteQueryResponse

### columnDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.ColumnDescription]
- **Required**: Yes

### rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.Row]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# FilterByAsset

### assetId
- **Type**: typing.Optional[str]

### assetExternalId
- **Type**: typing.Optional[str]

### includeOffspring
- **Type**: typing.Optional[bool]

### includeAssetModel
- **Type**: typing.Optional[bool]


# FilterByAssetModel

### assetModelId
- **Type**: typing.Optional[str]

### assetModelExternalId
- **Type**: typing.Optional[str]

### includeOffspring
- **Type**: typing.Optional[bool]

### includeAssets
- **Type**: typing.Optional[bool]


# FilterByComponentType

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# FilterByEntity

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# FunctionRequest

### requiredProperties
- **Type**: typing.Optional[typing.Sequence[str]]

### scope
- **Type**: typing.Optional[typing.Literal['ENTITY', 'WORKSPACE']]

### implementedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataConnector]


# FunctionResponse

### requiredProperties
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['ENTITY', 'WORKSPACE']]

### implementedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataConnector]

### isInherited
- **Type**: typing.Optional[bool]


# GetComponentTypeRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentTypeResponse

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### isSingleton
- **Type**: <class 'bool'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### propertyDefinitions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionResponse]
- **Required**: Yes

### extendsFrom
- **Type**: typing.List[str]
- **Required**: Yes

### functions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.FunctionResponse]
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### isAbstract
- **Type**: <class 'bool'>
- **Required**: Yes

### isSchemaInitialized
- **Type**: <class 'bool'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.Status'>
- **Required**: Yes

### propertyGroups
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyGroupResponse]
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### compositeComponentTypes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentTypeResponse]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetEntityRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEntityResponse

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.Status'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentResponse]
- **Required**: Yes

### parentEntityId
- **Type**: <class 'str'>
- **Required**: Yes

### hasChildEntities
- **Type**: <class 'bool'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### areAllComponentsReturned
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetadataTransferJobRequest

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetadataTransferJobResponse

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SourceConfigurationOutput]
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DestinationConfiguration'>
- **Required**: Yes

### metadataTransferJobRole
- **Type**: <class 'str'>
- **Required**: Yes

### reportUrl
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatus'>
- **Required**: Yes

### progress
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobProgress'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetPricingPlanResponse

### currentPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlan'>
- **Required**: Yes

### pendingPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlan'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetPropertyValueHistoryRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### selectedProperties
- **Type**: typing.Sequence[str]
- **Required**: Yes

### entityId
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### propertyFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyFilter]]

### startDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.Timestamp]

### endDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.Timestamp]

### interpolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.InterpolationParameters]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### orderByTime
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### startTime
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]


# GetPropertyValueHistoryResponse

### propertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetPropertyValueRequest

### selectedProperties
- **Type**: typing.Sequence[str]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### entityId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### propertyGroupName
- **Type**: typing.Optional[str]

### tabularConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.TabularConditions]


# GetPropertyValueResponse

### propertyValues
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyLatestValue]
- **Required**: Yes

### tabularPropertyValues
- **Type**: typing.List[typing.List[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutput]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSceneRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSceneResponse

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes

### contentLocation
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.List[str]
- **Required**: Yes

### sceneMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### generatedSceneMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### error
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.SceneError'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetSyncJobRequest

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: typing.Optional[str]


# GetSyncJobResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### syncRole
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncJobStatus'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkspaceResponse

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### linkedServices
- **Type**: typing.List[str]
- **Required**: Yes

### s3Location
- **Type**: <class 'str'>
- **Required**: Yes

### role
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# InterpolationParameters

### interpolationType
- **Type**: typing.Optional[typing.Literal['LINEAR']]

### intervalInSeconds
- **Type**: typing.Optional[int]


# IotSiteWiseSourceConfiguration

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotSiteWiseSourceConfigurationFilter]]


# IotSiteWiseSourceConfigurationFilter

### filterByAssetModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByAssetModel]

### filterByAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByAsset]


# IotSiteWiseSourceConfigurationOutput

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotSiteWiseSourceConfigurationFilter]]


# IotTwinMakerDestinationConfiguration

### workspace
- **Type**: <class 'str'>
- **Required**: Yes


# IotTwinMakerSourceConfiguration

### workspace
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotTwinMakerSourceConfigurationFilter]]


# IotTwinMakerSourceConfigurationFilter

### filterByComponentType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByComponentType]

### filterByEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByEntity]


# IotTwinMakerSourceConfigurationOutput

### workspace
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotTwinMakerSourceConfigurationFilter]]


# LambdaFunction

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListComponentTypesFilter

### extendsFrom
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### isAbstract
- **Type**: typing.Optional[bool]


# ListComponentTypesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.ListComponentTypesFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListComponentTypesResponse

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentTypeSummary]
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### componentPath
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsResponse

### componentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEntitiesFilter

### parentEntityId
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# ListEntitiesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.ListEntitiesFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEntitiesResponse

### entitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.EntitySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetadataTransferJobsFilter

### workspaceId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'ERROR', 'PENDING', 'RUNNING', 'VALIDATING']]


# ListMetadataTransferJobsRequest

### sourceType
- **Type**: typing.Literal['iotsitewise', 'iottwinmaker', 's3']
- **Required**: Yes

### destinationType
- **Type**: typing.Literal['iotsitewise', 'iottwinmaker', 's3']
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.ListMetadataTransferJobsFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMetadataTransferJobsResponse

### metadataTransferJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPropertiesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### componentName
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPropertiesResponse

### propertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScenesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScenesResponse

### sceneSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SceneSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSyncJobsRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSyncJobsResponse

### syncJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSyncResourcesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncResourceFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSyncResourcesResponse

### syncResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesResponse

### workspaceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.WorkspaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MetadataTransferJobProgress

### totalCount
- **Type**: typing.Optional[int]

### succeededCount
- **Type**: typing.Optional[int]

### skippedCount
- **Type**: typing.Optional[int]

### failedCount
- **Type**: typing.Optional[int]


# MetadataTransferJobStatus

### state
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'ERROR', 'PENDING', 'RUNNING', 'VALIDATING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetails]

### queuedPosition
- **Type**: typing.Optional[int]


# MetadataTransferJobSummary

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatus'>
- **Required**: Yes

### progress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobProgress]


# OrderBy

### propertyName
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ParentEntityUpdateRequest

### updateType
- **Type**: typing.Literal['DELETE', 'UPDATE']
- **Required**: Yes

### parentEntityId
- **Type**: typing.Optional[str]


# PricingPlan

### effectiveDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### pricingMode
- **Type**: typing.Literal['BASIC', 'STANDARD', 'TIERED_BUNDLE']
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateReason
- **Type**: typing.Literal['DEFAULT', 'ENTITY_COUNT_UPDATE', 'OVERWRITTEN', 'PRICING_MODE_UPDATE', 'PRICING_TIER_UPDATE']
- **Required**: Yes

### billableEntityCount
- **Type**: typing.Optional[int]

### bundleInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.BundleInformation]


# PropertyDefinitionRequest

### dataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataTypeUnion]

### isRequiredInEntity
- **Type**: typing.Optional[bool]

### isExternalId
- **Type**: typing.Optional[bool]

### isStoredExternally
- **Type**: typing.Optional[bool]

### isTimeSeries
- **Type**: typing.Optional[bool]

### defaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueUnion]

### configuration
- **Type**: typing.Optional[typing.Mapping[str, str]]

### displayName
- **Type**: typing.Optional[str]


# PropertyDefinitionResponse

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DataTypeOutput'>
- **Required**: Yes

### isTimeSeries
- **Type**: <class 'bool'>
- **Required**: Yes

### isRequiredInEntity
- **Type**: <class 'bool'>
- **Required**: Yes

### isExternalId
- **Type**: <class 'bool'>
- **Required**: Yes

### isStoredExternally
- **Type**: <class 'bool'>
- **Required**: Yes

### isImported
- **Type**: <class 'bool'>
- **Required**: Yes

### isFinal
- **Type**: <class 'bool'>
- **Required**: Yes

### isInherited
- **Type**: <class 'bool'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutput]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### displayName
- **Type**: typing.Optional[str]


# PropertyFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertyGroupRequest

### groupType
- **Type**: typing.Optional[typing.Literal['TABULAR']]

### propertyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# PropertyGroupResponse

### groupType
- **Type**: typing.Literal['TABULAR']
- **Required**: Yes

### propertyNames
- **Type**: typing.List[str]
- **Required**: Yes

### isInherited
- **Type**: <class 'bool'>
- **Required**: Yes


# PropertyLatestValue

### propertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceOutput'>
- **Required**: Yes

### propertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutput]


# PropertyRequest

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionRequest]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueUnion]

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'RESET_VALUE', 'UPDATE']]


# PropertyResponse

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionResponse]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutput]

### areAllPropertyValuesReturned
- **Type**: typing.Optional[bool]


# PropertySummary

### propertyName
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionResponse]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutput]

### areAllPropertyValuesReturned
- **Type**: typing.Optional[bool]


# PropertyValue

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueUnion'>
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.Timestamp]

### time
- **Type**: typing.Optional[str]


# PropertyValueEntry

### entityPropertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceUnion'>
- **Required**: Yes

### propertyValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueUnion]]


# PropertyValueEntryOutput

### entityPropertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceOutput'>
- **Required**: Yes

### propertyValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueOutput]]


# PropertyValueEntryUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertyValueHistory

### entityPropertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceOutput'>
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueOutput]]


# PropertyValueOutput

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutput'>
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### time
- **Type**: typing.Optional[str]


# PropertyValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Relationship

### targetComponentTypeId
- **Type**: typing.Optional[str]

### relationshipType
- **Type**: typing.Optional[str]


# RelationshipValue

### targetEntityId
- **Type**: typing.Optional[str]

### targetComponentName
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


# Row

### rowData
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# S3DestinationConfiguration

### location
- **Type**: <class 'str'>
- **Required**: Yes


# S3SourceConfiguration

### location
- **Type**: <class 'str'>
- **Required**: Yes


# SceneError

### code
- **Type**: typing.Optional[typing.Literal['MATTERPORT_ERROR']]

### message
- **Type**: typing.Optional[str]


# SceneSummary

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes

### contentLocation
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# SourceConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Status

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetails]


# SyncJobStatus

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'INITIALIZING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetails]


# SyncJobSummary

### arn
- **Type**: typing.Optional[str]

### workspaceId
- **Type**: typing.Optional[str]

### syncSource
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncJobStatus]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### updateDateTime
- **Type**: typing.Optional[datetime.datetime]


# SyncResourceFilter

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'ERROR', 'INITIALIZING', 'IN_SYNC', 'PROCESSING']]

### resourceType
- **Type**: typing.Optional[typing.Literal['COMPONENT_TYPE', 'ENTITY']]

### resourceId
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# SyncResourceStatus

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'ERROR', 'INITIALIZING', 'IN_SYNC', 'PROCESSING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetails]


# SyncResourceSummary

### resourceType
- **Type**: typing.Optional[typing.Literal['COMPONENT_TYPE', 'ENTITY']]

### externalId
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncResourceStatus]

### updateDateTime
- **Type**: typing.Optional[datetime.datetime]


# TabularConditions

### orderBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.OrderBy]]

### propertyFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyFilter]]


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateComponentTypeRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### isSingleton
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### propertyDefinitions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionRequest]]

### extendsFrom
- **Type**: typing.Optional[typing.Sequence[str]]

### functions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.FunctionRequest]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyGroupRequest]]

### componentTypeName
- **Type**: typing.Optional[str]

### compositeComponentTypes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentTypeRequest]]


# UpdateComponentTypeResponse

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEntityRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### entityName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### componentUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentUpdateRequest]]

### compositeComponentUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentUpdateRequest]]

### parentEntityUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ParentEntityUpdateRequest]


# UpdateEntityResponse

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePricingPlanRequest

### pricingMode
- **Type**: typing.Literal['BASIC', 'STANDARD', 'TIERED_BUNDLE']
- **Required**: Yes

### bundleNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdatePricingPlanResponse

### currentPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlan'>
- **Required**: Yes

### pendingPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlan'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSceneRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes

### contentLocation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### capabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### sceneMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateSceneResponse

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### role
- **Type**: typing.Optional[str]

### s3Location
- **Type**: typing.Optional[str]


# UpdateWorkspaceResponse

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadata'>
- **Required**: Yes


# WorkspaceSummary

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### linkedServices
- **Type**: typing.Optional[typing.List[str]]


