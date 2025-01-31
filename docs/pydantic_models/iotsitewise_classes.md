# iotsitewise_classes

# AccessPolicySummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### identity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.IdentityTypeDef'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResourceTypeDef'>
- **Required**: Yes

### permission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateDate
- **Type**: typing.Optional[datetime.datetime]


# ActionDefinitionTypeDef

### actionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: <class 'str'>
- **Required**: Yes


# ActionPayloadTypeDef

### stringValue
- **Type**: <class 'str'>
- **Required**: Yes


# ActionSummaryTypeDef

### actionId
- **Type**: typing.Optional[str]

### actionDefinitionId
- **Type**: typing.Optional[str]

### targetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.TargetResourceTypeDef]


# AggregatedValueTypeDef

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AggregatesTypeDef'>
- **Required**: Yes

### quality
- **Type**: typing.Optional[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]


# AggregatesTypeDef

### average
- **Type**: typing.Optional[float]

### count
- **Type**: typing.Optional[float]

### maximum
- **Type**: typing.Optional[float]

### minimum
- **Type**: typing.Optional[float]

### sum
- **Type**: typing.Optional[float]

### standardDeviation
- **Type**: typing.Optional[float]


# AlarmsTypeDef

### alarmRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationLambdaArn
- **Type**: typing.Optional[str]


# AssetCompositeModelPathSegmentTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetCompositeModelSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### path
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetCompositeModelPathSegmentTypeDef]
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]


# AssetCompositeModelTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetErrorDetailsTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['INTERNAL_FAILURE']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# AssetHierarchyInfoTypeDef

### parentAssetId
- **Type**: typing.Optional[str]

### childAssetId
- **Type**: typing.Optional[str]


# AssetHierarchyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelCompositeModelDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyDefinitionTypeDef]]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelCompositeModelPathSegmentTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetModelCompositeModelSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelPathSegmentTypeDef]]


# AssetModelCompositeModelTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyTypeDef]]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelHierarchyDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### childAssetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelHierarchyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### childAssetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelPropertyDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypeTypeDef'>
- **Required**: Yes

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelPropertyPathSegmentTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetModelPropertySummaryPaginatorTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypePaginatorTypeDef'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### assetModelCompositeModelId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyPathSegmentTypeDef]]

### externalId
- **Type**: typing.Optional[str]


# AssetModelPropertySummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypeTypeDef'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### assetModelCompositeModelId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyPathSegmentTypeDef]]

### externalId
- **Type**: typing.Optional[str]


# AssetModelPropertyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypeTypeDef'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyPathSegmentTypeDef]]

### externalId
- **Type**: typing.Optional[str]


# AssetModelStatusTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PROPAGATING', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ErrorDetailsTypeDef]


# AssetModelSummaryTypeDef

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

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### assetModelType
- **Type**: typing.Optional[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]

### externalId
- **Type**: typing.Optional[str]


# AssetPropertyPathSegmentTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetPropertySummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyNotificationTypeDef]

### assetCompositeModelId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyPathSegmentTypeDef]]

### externalId
- **Type**: typing.Optional[str]


# AssetPropertyTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyNotificationTypeDef]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyPathSegmentTypeDef]]

### externalId
- **Type**: typing.Optional[str]


# AssetPropertyValueTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.VariantTypeDef'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.TimeInNanosTypeDef'>
- **Required**: Yes

### quality
- **Type**: typing.Optional[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]


# AssetRelationshipSummaryTypeDef

### relationshipType
- **Type**: typing.Literal['HIERARCHY']
- **Required**: Yes

### hierarchyInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetHierarchyInfoTypeDef]


# AssetStatusTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ErrorDetailsTypeDef]


# AssetSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetStatusTypeDef'>
- **Required**: Yes

### hierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetHierarchyTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssociateAssetsRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### hierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### childAssetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AssociateTimeSeriesToAssetPropertyRequestRequestTypeDef

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AssociatedAssetsSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetStatusTypeDef'>
- **Required**: Yes

### hierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetHierarchyTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AttributeTypeDef

### defaultValue
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateProjectAssetsRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### assetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchAssociateProjectAssetsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetErrorDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateProjectAssetsRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### assetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchDisassociateProjectAssetsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetErrorDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregateTypes
- **Type**: typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'MAXIMUM', 'MINIMUM', 'STANDARD_DEVIATION', 'SUM']]
- **Required**: Yes

### resolution
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### qualities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# BatchGetAssetPropertyAggregatesErrorEntryTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entryId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesErrorInfoTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesRequestRequestTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyAggregatesEntryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# BatchGetAssetPropertyAggregatesResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyAggregatesErrorEntryTypeDef]
- **Required**: Yes

### successEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyAggregatesSuccessEntryTypeDef]
- **Required**: Yes

### skippedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyAggregatesSkippedEntryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesSkippedEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### completionStatus
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyAggregatesErrorInfoTypeDef]


# BatchGetAssetPropertyAggregatesSuccessEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregatedValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AggregatedValueTypeDef]
- **Required**: Yes


# BatchGetAssetPropertyValueEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyValueErrorEntryTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entryId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAssetPropertyValueErrorInfoTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistoryEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### startDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### qualities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# BatchGetAssetPropertyValueHistoryErrorEntryTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entryId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistoryErrorInfoTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistoryRequestRequestTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueHistoryEntryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# BatchGetAssetPropertyValueHistoryResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueHistoryErrorEntryTypeDef]
- **Required**: Yes

### successEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueHistorySuccessEntryTypeDef]
- **Required**: Yes

### skippedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueHistorySkippedEntryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistorySkippedEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### completionStatus
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueHistoryErrorInfoTypeDef]


# BatchGetAssetPropertyValueHistorySuccessEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetPropertyValueHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyValueTypeDef]
- **Required**: Yes


# BatchGetAssetPropertyValueRequestRequestTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueEntryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyValueResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueErrorEntryTypeDef]
- **Required**: Yes

### successEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueSuccessEntryTypeDef]
- **Required**: Yes

### skippedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueSkippedEntryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetAssetPropertyValueSkippedEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### completionStatus
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchGetAssetPropertyValueErrorInfoTypeDef]


# BatchGetAssetPropertyValueSuccessEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetPropertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyValueTypeDef]


# BatchPutAssetPropertyErrorEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchPutAssetPropertyErrorTypeDef]
- **Required**: Yes


# BatchPutAssetPropertyErrorTypeDef

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'ConflictingOperationException', 'InternalFailureException', 'InvalidRequestException', 'LimitExceededException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException', 'TimestampOutOfRangeException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### timestamps
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.TimeInNanosTypeDef]
- **Required**: Yes


# BatchPutAssetPropertyValueRequestRequestTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.PutAssetPropertyValueEntryTypeDef]
- **Required**: Yes


# BatchPutAssetPropertyValueResponseTypeDef

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.BatchPutAssetPropertyErrorEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ColumnInfoTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ColumnTypeTypeDef]


# ColumnTypeTypeDef

### scalarType
- **Type**: typing.Optional[typing.Literal['BOOLEAN', 'DOUBLE', 'INT', 'STRING', 'TIMESTAMP']]


# CompositeModelPropertyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### assetProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypeDef'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# CompositionDetailsTypeDef

### compositionRelationship
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.CompositionRelationshipItemTypeDef]]


# CompositionRelationshipItemTypeDef

### id
- **Type**: typing.Optional[str]


# CompositionRelationshipSummaryTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelType
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationErrorDetailsTypeDef

### code
- **Type**: typing.Literal['INTERNAL_FAILURE', 'VALIDATION_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationStatusTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ConfigurationErrorDetailsTypeDef]


# CreateAccessPolicyRequestRequestTypeDef

### accessPolicyIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.IdentityTypeDef'>
- **Required**: Yes

### accessPolicyResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResourceTypeDef'>
- **Required**: Yes

### accessPolicyPermission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAccessPolicyResponseTypeDef

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetModelCompositeModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelType
- **Type**: <class 'str'>
- **Required**: Yes

### parentAssetModelCompositeModelId
- **Type**: typing.Optional[str]

### assetModelCompositeModelExternalId
- **Type**: typing.Optional[str]

### assetModelCompositeModelId
- **Type**: typing.Optional[str]

### assetModelCompositeModelDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### composedAssetModelId
- **Type**: typing.Optional[str]

### assetModelCompositeModelProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyDefinitionTypeDef]]


# CreateAssetModelCompositeModelResponseTypeDef

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelPathSegmentTypeDef]
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetModelRequestRequestTypeDef

### assetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelDescription
- **Type**: typing.Optional[str]

### assetModelProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyDefinitionTypeDef]]

### assetModelHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelHierarchyDefinitionTypeDef]]

### assetModelCompositeModels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelDefinitionTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### assetModelId
- **Type**: typing.Optional[str]

### assetModelExternalId
- **Type**: typing.Optional[str]

### assetModelType
- **Type**: typing.Optional[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]


# CreateAssetModelResponseTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetRequestRequestTypeDef

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### assetDescription
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### assetExternalId
- **Type**: typing.Optional[str]


# CreateAssetResponseTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBulkImportJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.FileTypeDef]
- **Required**: Yes

### errorReportLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ErrorReportLocationTypeDef'>
- **Required**: Yes

### jobConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.JobConfigurationTypeDef'>
- **Required**: Yes

### adaptiveIngestion
- **Type**: typing.Optional[bool]

### deleteFilesAfterImport
- **Type**: typing.Optional[bool]


# CreateBulkImportJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDashboardRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardName
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDashboardResponseTypeDef

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGatewayRequestRequestTypeDef

### gatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayPlatform
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.GatewayPlatformTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateGatewayResponseTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePortalRequestRequestTypeDef

### portalName
- **Type**: <class 'str'>
- **Required**: Yes

### portalContactEmail
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### portalLogoImageFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ImageFileTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### portalAuthMode
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]

### notificationSenderEmail
- **Type**: typing.Optional[str]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.AlarmsTypeDef]


# CreatePortalResponseTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalStartUrl
- **Type**: <class 'str'>
- **Required**: Yes

### portalStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PortalStatusTypeDef'>
- **Required**: Yes

### ssoApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### projectDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResponseTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CsvTypeDef

### columnNames
- **Type**: typing.Sequence[typing.Literal['ALIAS', 'ASSET_ID', 'DATA_TYPE', 'PROPERTY_ID', 'QUALITY', 'TIMESTAMP_NANO_OFFSET', 'TIMESTAMP_SECONDS', 'VALUE']]
- **Required**: Yes


# CustomerManagedS3StorageTypeDef

### s3ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DashboardSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateDate
- **Type**: typing.Optional[datetime.datetime]


# DatumTypeDef

### scalarValue
- **Type**: typing.Optional[str]

### arrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### rowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### nullValue
- **Type**: typing.Optional[bool]


# DeleteAccessPolicyRequestRequestTypeDef

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAssetModelCompositeModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAssetModelCompositeModelResponseTypeDef

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAssetModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAssetModelResponseTypeDef

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAssetRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAssetResponseTypeDef

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDashboardRequestRequestTypeDef

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteGatewayRequestRequestTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePortalRequestRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePortalResponseTypeDef

### portalStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PortalStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteTimeSeriesRequestRequestTypeDef

### alias
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# DescribeAccessPolicyRequestRequestTypeDef

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessPolicyResponseTypeDef

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.IdentityTypeDef'>
- **Required**: Yes

### accessPolicyResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResourceTypeDef'>
- **Required**: Yes

### accessPolicyPermission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### accessPolicyCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### accessPolicyLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeActionRequestRequestTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActionResponseTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.TargetResourceTypeDef'>
- **Required**: Yes

### actionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ActionPayloadTypeDef'>
- **Required**: Yes

### executionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetCompositeModelRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetCompositeModelResponseTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetCompositeModelPathSegmentTypeDef]
- **Required**: Yes

### assetCompositeModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelType
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyTypeDef]
- **Required**: Yes

### assetCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetCompositeModelSummaryTypeDef]
- **Required**: Yes

### actionDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ActionDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetModelCompositeModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetModelCompositeModelResponseTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelPathSegmentTypeDef]
- **Required**: Yes

### assetModelCompositeModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelType
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyTypeDef]
- **Required**: Yes

### compositionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.CompositionDetailsTypeDef'>
- **Required**: Yes

### assetModelCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelSummaryTypeDef]
- **Required**: Yes

### actionDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ActionDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetModelRequestAssetModelActiveWaitTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WaiterConfigTypeDef]


# DescribeAssetModelRequestAssetModelNotExistsWaitTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WaiterConfigTypeDef]


# DescribeAssetModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]


# DescribeAssetModelResponseTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyTypeDef]
- **Required**: Yes

### assetModelHierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelHierarchyTypeDef]
- **Required**: Yes

### assetModelCompositeModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelTypeDef]
- **Required**: Yes

### assetModelCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetModelLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### assetModelType
- **Type**: typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']
- **Required**: Yes

### assetModelCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelSummaryTypeDef]
- **Required**: Yes

### assetModelExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetPropertyRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetPropertyResponseTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypeDef'>
- **Required**: Yes

### compositeModel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.CompositeModelPropertyTypeDef'>
- **Required**: Yes

### assetExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAssetRequestAssetActiveWaitTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WaiterConfigTypeDef]


# DescribeAssetRequestAssetNotExistsWaitTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WaiterConfigTypeDef]


# DescribeAssetRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]


# DescribeAssetResponseTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyTypeDef]
- **Required**: Yes

### assetHierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetHierarchyTypeDef]
- **Required**: Yes

### assetCompositeModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetCompositeModelTypeDef]
- **Required**: Yes

### assetCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetStatusTypeDef'>
- **Required**: Yes

### assetDescription
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetCompositeModelSummaryTypeDef]
- **Required**: Yes

### assetExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBulkImportJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBulkImportJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']
- **Required**: Yes

### jobRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.FileTypeDef]
- **Required**: Yes

### errorReportLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ErrorReportLocationTypeDef'>
- **Required**: Yes

### jobConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.JobConfigurationTypeDef'>
- **Required**: Yes

### jobCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### jobLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### adaptiveIngestion
- **Type**: <class 'bool'>
- **Required**: Yes

### deleteFilesAfterImport
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDashboardRequestRequestTypeDef

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardResponseTypeDef

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardName
- **Type**: <class 'str'>
- **Required**: Yes

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardDescription
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dashboardLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDefaultEncryptionConfigurationResponseTypeDef

### encryptionType
- **Type**: typing.Literal['KMS_BASED_ENCRYPTION', 'SITEWISE_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ConfigurationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGatewayCapabilityConfigurationRequestRequestTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayCapabilityConfigurationResponseTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### capabilitySyncStatus
- **Type**: typing.Literal['IN_SYNC', 'OUT_OF_SYNC', 'SYNC_FAILED', 'UNKNOWN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGatewayRequestRequestTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayResponseTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayPlatform
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.GatewayPlatformTypeDef'>
- **Required**: Yes

### gatewayCapabilitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.GatewayCapabilitySummaryTypeDef]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoggingOptionsResponseTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.LoggingOptionsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePortalRequestPortalActiveWaitTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WaiterConfigTypeDef]


# DescribePortalRequestPortalNotExistsWaitTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WaiterConfigTypeDef]


# DescribePortalRequestRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePortalResponseTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalName
- **Type**: <class 'str'>
- **Required**: Yes

### portalDescription
- **Type**: <class 'str'>
- **Required**: Yes

### portalClientId
- **Type**: <class 'str'>
- **Required**: Yes

### portalStartUrl
- **Type**: <class 'str'>
- **Required**: Yes

### portalContactEmail
- **Type**: <class 'str'>
- **Required**: Yes

### portalStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PortalStatusTypeDef'>
- **Required**: Yes

### portalCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### portalLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### portalLogoImageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ImageLocationTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalAuthMode
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### notificationSenderEmail
- **Type**: <class 'str'>
- **Required**: Yes

### alarms
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AlarmsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponseTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### projectDescription
- **Type**: <class 'str'>
- **Required**: Yes

### projectCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### projectLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStorageConfigurationResponseTypeDef

### storageType
- **Type**: typing.Literal['MULTI_LAYER_STORAGE', 'SITEWISE_DEFAULT_STORAGE']
- **Required**: Yes

### multiLayerStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.MultiLayerStorageTypeDef'>
- **Required**: Yes

### disassociatedDataStorage
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ConfigurationStatusTypeDef'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### warmTier
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### warmTierRetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.WarmTierRetentionPeriodTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTimeSeriesRequestRequestTypeDef

### alias
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]


# DescribeTimeSeriesResponseTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### timeSeriesId
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### dataTypeSpec
- **Type**: <class 'str'>
- **Required**: Yes

### timeSeriesCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeSeriesLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeSeriesArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetailedErrorTypeDef

### code
- **Type**: typing.Literal['INCOMPATIBLE_COMPUTE_LOCATION', 'INCOMPATIBLE_FORWARDING_CONFIGURATION']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateAssetsRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### hierarchyId
- **Type**: <class 'str'>
- **Required**: Yes

### childAssetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisassociateTimeSeriesFromAssetPropertyRequestRequestTypeDef

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorDetailsTypeDef

### code
- **Type**: typing.Literal['INTERNAL_FAILURE', 'VALIDATION_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.DetailedErrorTypeDef]]


# ErrorReportLocationTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes


# ExecuteActionRequestRequestTypeDef

### targetResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.TargetResourceTypeDef'>
- **Required**: Yes

### actionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ActionPayloadTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ExecuteActionResponseTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteQueryRequestExecuteQueryPaginateTypeDef

### queryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ExecuteQueryRequestRequestTypeDef

### queryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ExecuteQueryResponseTypeDef

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ColumnInfoTypeDef]
- **Required**: Yes

### rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.RowTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExpressionVariablePaginatorTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.VariableValuePaginatorTypeDef'>
- **Required**: Yes


# ExpressionVariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.VariableValueTypeDef'>
- **Required**: Yes


# FileFormatTypeDef

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.CsvTypeDef]

### parquet
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# FileTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# ForwardingConfigTypeDef

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# GatewayCapabilitySummaryTypeDef

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilitySyncStatus
- **Type**: typing.Literal['IN_SYNC', 'OUT_OF_SYNC', 'SYNC_FAILED', 'UNKNOWN']
- **Required**: Yes


# GatewayPlatformTypeDef

### greengrass
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.GreengrassTypeDef]

### greengrassV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.GreengrassV2TypeDef]


# GatewaySummaryTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### gatewayPlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.GatewayPlatformTypeDef]

### gatewayCapabilitySummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.GatewayCapabilitySummaryTypeDef]]


# GetAssetPropertyAggregatesRequestGetAssetPropertyAggregatesPaginateTypeDef

### aggregateTypes
- **Type**: typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'MAXIMUM', 'MINIMUM', 'STANDARD_DEVIATION', 'SUM']]
- **Required**: Yes

### resolution
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### qualities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# GetAssetPropertyAggregatesRequestRequestTypeDef

### aggregateTypes
- **Type**: typing.Sequence[typing.Literal['AVERAGE', 'COUNT', 'MAXIMUM', 'MINIMUM', 'STANDARD_DEVIATION', 'SUM']]
- **Required**: Yes

### resolution
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### qualities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetAssetPropertyAggregatesResponseTypeDef

### aggregatedValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AggregatedValueTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssetPropertyValueHistoryRequestGetAssetPropertyValueHistoryPaginateTypeDef

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### startDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### qualities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# GetAssetPropertyValueHistoryRequestRequestTypeDef

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### startDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### qualities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetAssetPropertyValueHistoryResponseTypeDef

### assetPropertyValueHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyValueTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssetPropertyValueRequestRequestTypeDef

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# GetAssetPropertyValueResponseTypeDef

### propertyValue
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyValueTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInterpolatedAssetPropertyValuesRequestGetInterpolatedAssetPropertyValuesPaginateTypeDef

### startTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### endTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### quality
- **Type**: typing.Literal['BAD', 'GOOD', 'UNCERTAIN']
- **Required**: Yes

### intervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### startTimeOffsetInNanos
- **Type**: typing.Optional[int]

### endTimeOffsetInNanos
- **Type**: typing.Optional[int]

### intervalWindowInSeconds
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# GetInterpolatedAssetPropertyValuesRequestRequestTypeDef

### startTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### endTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### quality
- **Type**: typing.Literal['BAD', 'GOOD', 'UNCERTAIN']
- **Required**: Yes

### intervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]

### startTimeOffsetInNanos
- **Type**: typing.Optional[int]

### endTimeOffsetInNanos
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### intervalWindowInSeconds
- **Type**: typing.Optional[int]


# GetInterpolatedAssetPropertyValuesResponseTypeDef

### interpolatedAssetPropertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.InterpolatedAssetPropertyValueTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GreengrassTypeDef

### groupArn
- **Type**: <class 'str'>
- **Required**: Yes


# GreengrassV2TypeDef

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes


# GroupIdentityTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# IAMRoleIdentityTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# IAMUserIdentityTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# IdentityTypeDef

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.UserIdentityTypeDef]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.GroupIdentityTypeDef]

### iamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.IAMUserIdentityTypeDef]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.IAMRoleIdentityTypeDef]


# ImageFileTypeDef

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### type
- **Type**: typing.Literal['PNG']
- **Required**: Yes


# ImageLocationTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes


# ImageTypeDef

### id
- **Type**: typing.Optional[str]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ImageFileTypeDef]


# InterpolatedAssetPropertyValueTypeDef

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.TimeInNanosTypeDef'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.VariantTypeDef'>
- **Required**: Yes


# JobConfigurationTypeDef

### fileFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.FileFormatTypeDef'>
- **Required**: Yes


# JobSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']
- **Required**: Yes


# ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef

### identityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'IAM', 'USER']]

### identityId
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['PORTAL', 'PROJECT']]

### resourceId
- **Type**: typing.Optional[str]

### iamArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAccessPoliciesRequestRequestTypeDef

### identityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'IAM', 'USER']]

### identityId
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['PORTAL', 'PROJECT']]

### resourceId
- **Type**: typing.Optional[str]

### iamArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccessPoliciesResponseTypeDef

### accessPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AccessPolicySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListActionsRequestListActionsPaginateTypeDef

### targetResourceType
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### targetResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListActionsRequestRequestTypeDef

### targetResourceType
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### targetResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListActionsResponseTypeDef

### actionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ActionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetModelCompositeModelsRequestListAssetModelCompositeModelsPaginateTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssetModelCompositeModelsRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssetModelCompositeModelsResponseTypeDef

### assetModelCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetModelPropertiesRequestListAssetModelPropertiesPaginateTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssetModelPropertiesRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]


# ListAssetModelPropertiesResponsePaginatorTypeDef

### assetModelPropertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertySummaryPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetModelPropertiesResponseTypeDef

### assetModelPropertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetModelsRequestListAssetModelsPaginateTypeDef

### assetModelTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssetModelsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### assetModelTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]]


# ListAssetModelsResponseTypeDef

### assetModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetPropertiesRequestListAssetPropertiesPaginateTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssetPropertiesRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]


# ListAssetPropertiesResponseTypeDef

### assetPropertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetRelationshipsRequestListAssetRelationshipsPaginateTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### traversalType
- **Type**: typing.Literal['PATH_TO_ROOT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssetRelationshipsRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### traversalType
- **Type**: typing.Literal['PATH_TO_ROOT']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssetRelationshipsResponseTypeDef

### assetRelationshipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetRelationshipSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssetsRequestListAssetsPaginateTypeDef

### assetModelId
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'TOP_LEVEL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssetsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### assetModelId
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'TOP_LEVEL']]


# ListAssetsResponseTypeDef

### assetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedAssetsRequestListAssociatedAssetsPaginateTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### hierarchyId
- **Type**: typing.Optional[str]

### traversalDirection
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListAssociatedAssetsRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### hierarchyId
- **Type**: typing.Optional[str]

### traversalDirection
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAssociatedAssetsResponseTypeDef

### assetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssociatedAssetsSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBulkImportJobsRequestListBulkImportJobsPaginateTypeDef

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListBulkImportJobsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']]


# ListBulkImportJobsResponseTypeDef

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.JobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCompositionRelationshipsRequestListCompositionRelationshipsPaginateTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListCompositionRelationshipsRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCompositionRelationshipsResponseTypeDef

### compositionRelationshipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.CompositionRelationshipSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDashboardsRequestListDashboardsPaginateTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListDashboardsRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDashboardsResponseTypeDef

### dashboardSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.DashboardSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGatewaysRequestListGatewaysPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListGatewaysRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGatewaysResponseTypeDef

### gatewaySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.GatewaySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPortalsRequestListPortalsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListPortalsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPortalsResponseTypeDef

### portalSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.PortalSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectAssetsRequestListProjectAssetsPaginateTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListProjectAssetsRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectAssetsResponseTypeDef

### assetIds
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectsResponseTypeDef

### projectSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTimeSeriesRequestListTimeSeriesPaginateTypeDef

### assetId
- **Type**: typing.Optional[str]

### aliasPrefix
- **Type**: typing.Optional[str]

### timeSeriesType
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'DISASSOCIATED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PaginatorConfigTypeDef]


# ListTimeSeriesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### assetId
- **Type**: typing.Optional[str]

### aliasPrefix
- **Type**: typing.Optional[str]

### timeSeriesType
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'DISASSOCIATED']]


# ListTimeSeriesResponseTypeDef

### TimeSeriesSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.TimeSeriesSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingOptionsTypeDef

### level
- **Type**: typing.Literal['ERROR', 'INFO', 'OFF']
- **Required**: Yes


# MeasurementProcessingConfigTypeDef

### forwardingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ForwardingConfigTypeDef'>
- **Required**: Yes


# MeasurementTypeDef

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MeasurementProcessingConfigTypeDef]


# MetricPaginatorTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ExpressionVariablePaginatorTypeDef]
- **Required**: Yes

### window
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.MetricWindowTypeDef'>
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MetricProcessingConfigTypeDef]


# MetricProcessingConfigTypeDef

### computeLocation
- **Type**: typing.Literal['CLOUD', 'EDGE']
- **Required**: Yes


# MetricTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.ExpressionVariableTypeDef]
- **Required**: Yes

### window
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.MetricWindowTypeDef'>
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MetricProcessingConfigTypeDef]


# MetricWindowTypeDef

### tumbling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.TumblingWindowTypeDef]


# MonitorErrorDetailsTypeDef

### code
- **Type**: typing.Optional[typing.Literal['INTERNAL_FAILURE', 'LIMIT_EXCEEDED', 'VALIDATION_ERROR']]

### message
- **Type**: typing.Optional[str]


# MultiLayerStorageTypeDef

### customerManagedS3Storage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.CustomerManagedS3StorageTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortalResourceTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# PortalStatusTypeDef

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MonitorErrorDetailsTypeDef]


# PortalSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### startUrl
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PortalStatusTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateDate
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]


# ProjectResourceTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectSummaryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateDate
- **Type**: typing.Optional[datetime.datetime]


# PropertyNotificationTypeDef

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# PropertyTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyNotificationTypeDef]

### unit
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PropertyTypeTypeDef]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyPathSegmentTypeDef]]

### externalId
- **Type**: typing.Optional[str]


# PropertyTypePaginatorTypeDef

### attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.AttributeTypeDef]

### measurement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MeasurementTypeDef]

### transform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.TransformPaginatorTypeDef]

### metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MetricPaginatorTypeDef]


# PropertyTypeTypeDef

### attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.AttributeTypeDef]

### measurement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MeasurementTypeDef]

### transform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.TransformTypeDef]

### metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MetricTypeDef]


# PutAssetPropertyValueEntryTypeDef

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyValues
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetPropertyValueTypeDef]
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# PutDefaultEncryptionConfigurationRequestRequestTypeDef

### encryptionType
- **Type**: typing.Literal['KMS_BASED_ENCRYPTION', 'SITEWISE_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# PutDefaultEncryptionConfigurationResponseTypeDef

### encryptionType
- **Type**: typing.Literal['KMS_BASED_ENCRYPTION', 'SITEWISE_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ConfigurationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutLoggingOptionsRequestRequestTypeDef

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.LoggingOptionsTypeDef'>
- **Required**: Yes


# PutStorageConfigurationRequestRequestTypeDef

### storageType
- **Type**: typing.Literal['MULTI_LAYER_STORAGE', 'SITEWISE_DEFAULT_STORAGE']
- **Required**: Yes

### multiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.MultiLayerStorageTypeDef]

### disassociatedDataStorage
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.RetentionPeriodTypeDef]

### warmTier
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### warmTierRetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.WarmTierRetentionPeriodTypeDef]


# PutStorageConfigurationResponseTypeDef

### storageType
- **Type**: typing.Literal['MULTI_LAYER_STORAGE', 'SITEWISE_DEFAULT_STORAGE']
- **Required**: Yes

### multiLayerStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.MultiLayerStorageTypeDef'>
- **Required**: Yes

### disassociatedDataStorage
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ConfigurationStatusTypeDef'>
- **Required**: Yes

### warmTier
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### warmTierRetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.WarmTierRetentionPeriodTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceTypeDef

### portal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.PortalResourceTypeDef]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ProjectResourceTypeDef]


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


# RetentionPeriodTypeDef

### numberOfDays
- **Type**: typing.Optional[int]

### unlimited
- **Type**: typing.Optional[bool]


# RowTypeDef

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.DatumTypeDef]
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetResourceTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes


# TimeInNanosTypeDef

### timeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### offsetInNanos
- **Type**: typing.Optional[int]


# TimeSeriesSummaryTypeDef

### timeSeriesId
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### timeSeriesCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeSeriesLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### timeSeriesArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### alias
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]


# TransformPaginatorTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.ExpressionVariablePaginatorTypeDef]
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.TransformProcessingConfigTypeDef]


# TransformProcessingConfigTypeDef

### computeLocation
- **Type**: typing.Literal['CLOUD', 'EDGE']
- **Required**: Yes

### forwardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ForwardingConfigTypeDef]


# TransformTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.ExpressionVariableTypeDef]
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.TransformProcessingConfigTypeDef]


# TumblingWindowTypeDef

### interval
- **Type**: <class 'str'>
- **Required**: Yes

### offset
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessPolicyRequestRequestTypeDef

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.IdentityTypeDef'>
- **Required**: Yes

### accessPolicyResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResourceTypeDef'>
- **Required**: Yes

### accessPolicyPermission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateAssetModelCompositeModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelExternalId
- **Type**: typing.Optional[str]

### assetModelCompositeModelDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### assetModelCompositeModelProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyTypeDef]]


# UpdateAssetModelCompositeModelResponseTypeDef

### assetModelCompositeModelPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelPathSegmentTypeDef]
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssetModelRequestRequestTypeDef

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelDescription
- **Type**: typing.Optional[str]

### assetModelProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyTypeDef]]

### assetModelHierarchies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelHierarchyTypeDef]]

### assetModelCompositeModels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelCompositeModelTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### assetModelExternalId
- **Type**: typing.Optional[str]


# UpdateAssetModelResponseTypeDef

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssetPropertyRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyAlias
- **Type**: typing.Optional[str]

### propertyNotificationState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### clientToken
- **Type**: typing.Optional[str]

### propertyUnit
- **Type**: typing.Optional[str]


# UpdateAssetRequestRequestTypeDef

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### assetDescription
- **Type**: typing.Optional[str]

### assetExternalId
- **Type**: typing.Optional[str]


# UpdateAssetResponseTypeDef

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.AssetStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardRequestRequestTypeDef

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardName
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateGatewayCapabilityConfigurationRequestRequestTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGatewayCapabilityConfigurationResponseTypeDef

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilitySyncStatus
- **Type**: typing.Literal['IN_SYNC', 'OUT_OF_SYNC', 'SYNC_FAILED', 'UNKNOWN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGatewayRequestRequestTypeDef

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePortalRequestRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### portalName
- **Type**: <class 'str'>
- **Required**: Yes

### portalContactEmail
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalDescription
- **Type**: typing.Optional[str]

### portalLogoImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.ImageTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### notificationSenderEmail
- **Type**: typing.Optional[str]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise_classes.AlarmsTypeDef]


# UpdatePortalResponseTypeDef

### portalStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.PortalStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectRequestRequestTypeDef

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### projectDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UserIdentityTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# VariableValuePaginatorTypeDef

### propertyId
- **Type**: typing.Optional[str]

### hierarchyId
- **Type**: typing.Optional[str]

### propertyPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyPathSegmentTypeDef]]


# VariableValueTypeDef

### propertyId
- **Type**: typing.Optional[str]

### hierarchyId
- **Type**: typing.Optional[str]

### propertyPath
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsitewise_classes.AssetModelPropertyPathSegmentTypeDef]]


# VariantTypeDef

### stringValue
- **Type**: typing.Optional[str]

### integerValue
- **Type**: typing.Optional[int]

### doubleValue
- **Type**: typing.Optional[float]

### booleanValue
- **Type**: typing.Optional[bool]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarmTierRetentionPeriodTypeDef

### numberOfDays
- **Type**: typing.Optional[int]

### unlimited
- **Type**: typing.Optional[bool]


