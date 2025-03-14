# Iottwinmaker Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchPutPropertyErrorEntryTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.BatchPutPropertyErrorTypeDef]
- **Required**: Yes


# BatchPutPropertyErrorTypeDef

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entry
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueEntryOutputTypeDef'>
- **Required**: Yes


# BatchPutPropertyValuesRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueEntryUnionTypeDef]
- **Required**: Yes


# BatchPutPropertyValuesResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.BatchPutPropertyErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BundleInformationTypeDef

### bundleNames
- **Type**: typing.List[str]
- **Required**: Yes

### pricingTier
- **Type**: typing.Optional[typing.Literal['TIER_1', 'TIER_2', 'TIER_3', 'TIER_4']]


# CancelMetadataTransferJobRequestTypeDef

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMetadataTransferJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatusTypeDef'>
- **Required**: Yes

### progress
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobProgressTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ColumnDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyGroupRequestTypeDef

### groupType
- **Type**: typing.Optional[typing.Literal['TABULAR']]

### propertyNames
- **Type**: typing.Optional[typing.Sequence[str]]

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]


# ComponentPropertyGroupResponseTypeDef

### groupType
- **Type**: typing.Literal['TABULAR']
- **Required**: Yes

### propertyNames
- **Type**: typing.List[str]
- **Required**: Yes

### isInherited
- **Type**: <class 'bool'>
- **Required**: Yes


# ComponentRequestTypeDef

### description
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequestTypeDef]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequestTypeDef]]


# ComponentResponseTypeDef

### componentName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.StatusTypeDef]

### definedIn
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyResponseTypeDef]]

### propertyGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupResponseTypeDef]]

### syncSource
- **Type**: typing.Optional[str]

### areAllPropertiesReturned
- **Type**: typing.Optional[bool]

### compositeComponents
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentSummaryTypeDef]]

### areAllCompositeComponentsReturned
- **Type**: typing.Optional[bool]


# ComponentSummaryTypeDef

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.StatusTypeDef'>
- **Required**: Yes

### definedIn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### propertyGroups
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupResponseTypeDef]]

### syncSource
- **Type**: typing.Optional[str]

### componentPath
- **Type**: typing.Optional[str]


# ComponentTypeSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.StatusTypeDef]

### componentTypeName
- **Type**: typing.Optional[str]


# ComponentUpdateRequestTypeDef

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### description
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### propertyUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequestTypeDef]]

### propertyGroupUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequestTypeDef]]


# CompositeComponentRequestTypeDef

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequestTypeDef]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequestTypeDef]]


# CompositeComponentTypeRequestTypeDef

### componentTypeId
- **Type**: typing.Optional[str]


# CompositeComponentTypeResponseTypeDef

### componentTypeId
- **Type**: typing.Optional[str]

### isInherited
- **Type**: typing.Optional[bool]


# CompositeComponentUpdateRequestTypeDef

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'UPDATE']]

### description
- **Type**: typing.Optional[str]

### propertyUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyRequestTypeDef]]

### propertyGroupUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentPropertyGroupRequestTypeDef]]


# CreateComponentTypeRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionRequestTypeDef]]

### extendsFrom
- **Type**: typing.Optional[typing.Sequence[str]]

### functions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.FunctionRequestTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyGroupRequestTypeDef]]

### componentTypeName
- **Type**: typing.Optional[str]

### compositeComponentTypes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentTypeRequestTypeDef]]


# CreateComponentTypeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEntityRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentRequestTypeDef]]

### compositeComponents
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentRequestTypeDef]]

### parentEntityId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEntityResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMetadataTransferJobRequestTypeDef

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.SourceConfigurationUnionTypeDef]
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### metadataTransferJobId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateMetadataTransferJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSceneRequestTypeDef

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


# CreateSceneResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSyncJobRequestTypeDef

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


# CreateSyncJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceRequestTypeDef

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


# CreateWorkspaceResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataConnectorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataTypeOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataValueOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.RelationshipValueTypeDef]

### expression
- **Type**: typing.Optional[str]


# DataValueTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.RelationshipValueTypeDef]

### expression
- **Type**: typing.Optional[str]


# DataValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteComponentTypeRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentTypeResponseTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEntityRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### isRecursive
- **Type**: typing.Optional[bool]


# DeleteEntityResponseTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSceneRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSyncJobRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSyncJobResponseTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'INITIALIZING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceResponseTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityPropertyReferenceOutputTypeDef

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


# EntityPropertyReferenceTypeDef

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


# EntityPropertyReferenceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntitySummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.StatusTypeDef'>
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


# ErrorDetailsTypeDef

### code
- **Type**: typing.Optional[typing.Literal['COMPOSITE_COMPONENT_FAILURE', 'INTERNAL_FAILURE', 'PROCESSING_ERROR', 'SYNC_CREATING_ERROR', 'SYNC_DELETING_ERROR', 'SYNC_INITIALIZING_ERROR', 'SYNC_PROCESSING_ERROR', 'VALIDATION_ERROR']]

### message
- **Type**: typing.Optional[str]


# ExecuteQueryRequestTypeDef

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


# ExecuteQueryResponseTypeDef

### columnDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.ColumnDescriptionTypeDef]
- **Required**: Yes

### rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.RowTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# FilterByAssetModelTypeDef

### assetModelId
- **Type**: typing.Optional[str]

### assetModelExternalId
- **Type**: typing.Optional[str]

### includeOffspring
- **Type**: typing.Optional[bool]

### includeAssets
- **Type**: typing.Optional[bool]


# FilterByAssetTypeDef

### assetId
- **Type**: typing.Optional[str]

### assetExternalId
- **Type**: typing.Optional[str]

### includeOffspring
- **Type**: typing.Optional[bool]

### includeAssetModel
- **Type**: typing.Optional[bool]


# FilterByComponentTypeTypeDef

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# FilterByEntityTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# FunctionRequestTypeDef

### requiredProperties
- **Type**: typing.Optional[typing.Sequence[str]]

### scope
- **Type**: typing.Optional[typing.Literal['ENTITY', 'WORKSPACE']]

### implementedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataConnectorTypeDef]


# FunctionResponseTypeDef

### requiredProperties
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['ENTITY', 'WORKSPACE']]

### implementedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataConnectorTypeDef]

### isInherited
- **Type**: typing.Optional[bool]


# GetComponentTypeRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentTypeResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionResponseTypeDef]
- **Required**: Yes

### extendsFrom
- **Type**: typing.List[str]
- **Required**: Yes

### functions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.FunctionResponseTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.StatusTypeDef'>
- **Required**: Yes

### propertyGroups
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyGroupResponseTypeDef]
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### compositeComponentTypes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentTypeResponseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEntityRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEntityResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.StatusTypeDef'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### components
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentResponseTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMetadataTransferJobRequestTypeDef

### metadataTransferJobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetadataTransferJobResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SourceConfigurationOutputTypeDef]
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DestinationConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatusTypeDef'>
- **Required**: Yes

### progress
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobProgressTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPricingPlanResponseTypeDef

### currentPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlanTypeDef'>
- **Required**: Yes

### pendingPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPropertyValueHistoryRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyFilterTypeDef]]

### startDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.TimestampTypeDef]

### endDateTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.TimestampTypeDef]

### interpolation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.InterpolationParametersTypeDef]

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


# GetPropertyValueHistoryResponseTypeDef

### propertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetPropertyValueRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.TabularConditionsTypeDef]


# GetPropertyValueResponseTypeDef

### propertyValues
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyLatestValueTypeDef]
- **Required**: Yes

### tabularPropertyValues
- **Type**: typing.List[typing.List[typing.Dict[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutputTypeDef]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSceneRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### sceneId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSceneResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.SceneErrorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSyncJobRequestTypeDef

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: typing.Optional[str]


# GetSyncJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncJobStatusTypeDef'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkspaceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InterpolationParametersTypeDef

### interpolationType
- **Type**: typing.Optional[typing.Literal['LINEAR']]

### intervalInSeconds
- **Type**: typing.Optional[int]


# IotSiteWiseSourceConfigurationFilterTypeDef

### filterByAssetModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByAssetModelTypeDef]

### filterByAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByAssetTypeDef]


# IotSiteWiseSourceConfigurationOutputTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotSiteWiseSourceConfigurationFilterTypeDef]]


# IotSiteWiseSourceConfigurationTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotSiteWiseSourceConfigurationFilterTypeDef]]


# IotTwinMakerDestinationConfigurationTypeDef

### workspace
- **Type**: <class 'str'>
- **Required**: Yes


# IotTwinMakerSourceConfigurationFilterTypeDef

### filterByComponentType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByComponentTypeTypeDef]

### filterByEntity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.FilterByEntityTypeDef]


# IotTwinMakerSourceConfigurationOutputTypeDef

### workspace
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotTwinMakerSourceConfigurationFilterTypeDef]]


# IotTwinMakerSourceConfigurationTypeDef

### workspace
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.IotTwinMakerSourceConfigurationFilterTypeDef]]


# LambdaFunctionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListComponentTypesFilterTypeDef

### extendsFrom
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### isAbstract
- **Type**: typing.Optional[bool]


# ListComponentTypesRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.ListComponentTypesFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListComponentTypesResponseTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### componentTypeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentTypeSummaryTypeDef]
- **Required**: Yes

### maxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequestTypeDef

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


# ListComponentsResponseTypeDef

### componentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEntitiesFilterTypeDef

### parentEntityId
- **Type**: typing.Optional[str]

### componentTypeId
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# ListEntitiesRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.ListEntitiesFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEntitiesResponseTypeDef

### entitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.EntitySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetadataTransferJobsFilterTypeDef

### workspaceId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'ERROR', 'PENDING', 'RUNNING', 'VALIDATING']]


# ListMetadataTransferJobsRequestTypeDef

### sourceType
- **Type**: typing.Literal['iotsitewise', 'iottwinmaker', 's3']
- **Required**: Yes

### destinationType
- **Type**: typing.Literal['iotsitewise', 'iottwinmaker', 's3']
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.ListMetadataTransferJobsFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMetadataTransferJobsResponseTypeDef

### metadataTransferJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPropertiesRequestTypeDef

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


# ListPropertiesResponseTypeDef

### propertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScenesRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScenesResponseTypeDef

### sceneSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SceneSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSyncJobsRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSyncJobsResponseTypeDef

### syncJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSyncResourcesRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### syncSource
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncResourceFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSyncResourcesResponseTypeDef

### syncResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesResponseTypeDef

### workspaceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.WorkspaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MetadataTransferJobProgressTypeDef

### totalCount
- **Type**: typing.Optional[int]

### succeededCount
- **Type**: typing.Optional[int]

### skippedCount
- **Type**: typing.Optional[int]

### failedCount
- **Type**: typing.Optional[int]


# MetadataTransferJobStatusTypeDef

### state
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'ERROR', 'PENDING', 'RUNNING', 'VALIDATING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetailsTypeDef]

### queuedPosition
- **Type**: typing.Optional[int]


# MetadataTransferJobSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobStatusTypeDef'>
- **Required**: Yes

### progress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.MetadataTransferJobProgressTypeDef]


# OrderByTypeDef

### propertyName
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ParentEntityUpdateRequestTypeDef

### updateType
- **Type**: typing.Literal['DELETE', 'UPDATE']
- **Required**: Yes

### parentEntityId
- **Type**: typing.Optional[str]


# PricingPlanTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.BundleInformationTypeDef]


# PropertyDefinitionRequestTypeDef

### dataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataTypeUnionTypeDef]

### isRequiredInEntity
- **Type**: typing.Optional[bool]

### isExternalId
- **Type**: typing.Optional[bool]

### isStoredExternally
- **Type**: typing.Optional[bool]

### isTimeSeries
- **Type**: typing.Optional[bool]

### defaultValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueUnionTypeDef]

### configuration
- **Type**: typing.Optional[typing.Mapping[str, str]]

### displayName
- **Type**: typing.Optional[str]


# PropertyDefinitionResponseTypeDef

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DataTypeOutputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutputTypeDef]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### displayName
- **Type**: typing.Optional[str]


# PropertyFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertyGroupRequestTypeDef

### groupType
- **Type**: typing.Optional[typing.Literal['TABULAR']]

### propertyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# PropertyGroupResponseTypeDef

### groupType
- **Type**: typing.Literal['TABULAR']
- **Required**: Yes

### propertyNames
- **Type**: typing.List[str]
- **Required**: Yes

### isInherited
- **Type**: <class 'bool'>
- **Required**: Yes


# PropertyLatestValueTypeDef

### propertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceOutputTypeDef'>
- **Required**: Yes

### propertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutputTypeDef]


# PropertyRequestTypeDef

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionRequestTypeDef]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueUnionTypeDef]

### updateType
- **Type**: typing.Optional[typing.Literal['CREATE', 'DELETE', 'RESET_VALUE', 'UPDATE']]


# PropertyResponseTypeDef

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionResponseTypeDef]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutputTypeDef]

### areAllPropertyValuesReturned
- **Type**: typing.Optional[bool]


# PropertySummaryTypeDef

### propertyName
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionResponseTypeDef]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutputTypeDef]

### areAllPropertyValuesReturned
- **Type**: typing.Optional[bool]


# PropertyValueEntryOutputTypeDef

### entityPropertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceOutputTypeDef'>
- **Required**: Yes

### propertyValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueOutputTypeDef]]


# PropertyValueEntryTypeDef

### entityPropertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceUnionTypeDef'>
- **Required**: Yes

### propertyValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueUnionTypeDef]]


# PropertyValueEntryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertyValueHistoryTypeDef

### entityPropertyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.EntityPropertyReferenceOutputTypeDef'>
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyValueOutputTypeDef]]


# PropertyValueOutputTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueOutputTypeDef'>
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### time
- **Type**: typing.Optional[str]


# PropertyValueTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.DataValueUnionTypeDef'>
- **Required**: Yes

### timestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.TimestampTypeDef]

### time
- **Type**: typing.Optional[str]


# PropertyValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RelationshipTypeDef

### targetComponentTypeId
- **Type**: typing.Optional[str]

### relationshipType
- **Type**: typing.Optional[str]


# RelationshipValueTypeDef

### targetEntityId
- **Type**: typing.Optional[str]

### targetComponentName
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


# RowTypeDef

### rowData
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# S3DestinationConfigurationTypeDef

### location
- **Type**: <class 'str'>
- **Required**: Yes


# S3SourceConfigurationTypeDef

### location
- **Type**: <class 'str'>
- **Required**: Yes


# SceneErrorTypeDef

### code
- **Type**: typing.Optional[typing.Literal['MATTERPORT_ERROR']]

### message
- **Type**: typing.Optional[str]


# SceneSummaryTypeDef

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


# SourceConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatusTypeDef

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetailsTypeDef]


# SyncJobStatusTypeDef

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'INITIALIZING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetailsTypeDef]


# SyncJobSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### workspaceId
- **Type**: typing.Optional[str]

### syncSource
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncJobStatusTypeDef]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### updateDateTime
- **Type**: typing.Optional[datetime.datetime]


# SyncResourceFilterTypeDef

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'ERROR', 'INITIALIZING', 'IN_SYNC', 'PROCESSING']]

### resourceType
- **Type**: typing.Optional[typing.Literal['COMPONENT_TYPE', 'ENTITY']]

### resourceId
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# SyncResourceStatusTypeDef

### state
- **Type**: typing.Optional[typing.Literal['DELETED', 'ERROR', 'INITIALIZING', 'IN_SYNC', 'PROCESSING']]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ErrorDetailsTypeDef]


# SyncResourceSummaryTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['COMPONENT_TYPE', 'ENTITY']]

### externalId
- **Type**: typing.Optional[str]

### resourceId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.SyncResourceStatusTypeDef]

### updateDateTime
- **Type**: typing.Optional[datetime.datetime]


# TabularConditionsTypeDef

### orderBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.OrderByTypeDef]]

### propertyFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyFilterTypeDef]]


# TagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateComponentTypeRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyDefinitionRequestTypeDef]]

### extendsFrom
- **Type**: typing.Optional[typing.Sequence[str]]

### functions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.FunctionRequestTypeDef]]

### propertyGroups
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.PropertyGroupRequestTypeDef]]

### componentTypeName
- **Type**: typing.Optional[str]

### compositeComponentTypes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentTypeRequestTypeDef]]


# UpdateComponentTypeResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEntityRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.ComponentUpdateRequestTypeDef]]

### compositeComponentUpdates
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.iottwinmaker_classes.CompositeComponentUpdateRequestTypeDef]]

### parentEntityUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iottwinmaker_classes.ParentEntityUpdateRequestTypeDef]


# UpdateEntityResponseTypeDef

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'ERROR', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePricingPlanRequestTypeDef

### pricingMode
- **Type**: typing.Literal['BASIC', 'STANDARD', 'TIERED_BUNDLE']
- **Required**: Yes

### bundleNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdatePricingPlanResponseTypeDef

### currentPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlanTypeDef'>
- **Required**: Yes

### pendingPricingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.PricingPlanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSceneRequestTypeDef

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


# UpdateSceneResponseTypeDef

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### role
- **Type**: typing.Optional[str]

### s3Location
- **Type**: typing.Optional[str]


# UpdateWorkspaceResponseTypeDef

### updateDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iottwinmaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkspaceSummaryTypeDef

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


