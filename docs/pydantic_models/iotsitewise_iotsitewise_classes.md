# Iotsitewise Iotsitewise Classes

# AccessDeniedException

### message
- **Type**: typing.Optional[str]


# AccessPolicySummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### identity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Identity'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Resource'>
- **Required**: Yes

### permission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateDate
- **Type**: typing.Optional[datetime.datetime]


# ActionDefinition

### actionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### actionType
- **Type**: <class 'str'>
- **Required**: Yes


# ActionPayload

### stringValue
- **Type**: <class 'str'>
- **Required**: Yes


# ActionSummary

### actionId
- **Type**: typing.Optional[str]

### actionDefinitionId
- **Type**: typing.Optional[str]

### targetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TargetResource]


# AggregatedValue

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Aggregates'>
- **Required**: Yes

### quality
- **Type**: typing.Optional[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]


# Aggregates

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


# Alarms

### alarmRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationLambdaArn
- **Type**: typing.Optional[str]


# AssetCompositeModel

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetProperty]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetCompositeModelPathSegment

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetCompositeModelSummary

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetCompositeModelPathSegment]
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]


# AssetErrorDetails

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['INTERNAL_FAILURE']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# AssetHierarchy

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetHierarchyInfo

### parentAssetId
- **Type**: typing.Optional[str]

### childAssetId
- **Type**: typing.Optional[str]


# AssetModelCompositeModel

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelProperty, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyOutput]]]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelCompositeModelDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyDefinition]]


# AssetModelCompositeModelOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyOutput]]

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssetModelCompositeModelPathSegment

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetModelCompositeModelSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelPathSegment]]


# AssetModelHierarchy

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


# AssetModelHierarchyDefinition

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


# AssetModelProperty

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyType, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyTypeOutput]
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyPathSegment]]


# AssetModelPropertyDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyType, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyTypeOutput]
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]


# AssetModelPropertyOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyTypeOutput'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyPathSegment]]


# AssetModelPropertyPathSegment

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetModelPropertySummary

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'INTEGER', 'STRING', 'STRUCT']
- **Required**: Yes

### type
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyTypeOutput'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### assetModelCompositeModelId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyPathSegment]]


# AssetModelStatus

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PROPAGATING', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ErrorDetails]


# AssetModelSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]

### assetModelType
- **Type**: typing.Optional[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]

### version
- **Type**: typing.Optional[str]


# AssetProperty

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyNotification]

### dataTypeSpec
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyPathSegment]]

### externalId
- **Type**: typing.Optional[str]


# AssetPropertyPathSegment

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# AssetPropertySummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### unit
- **Type**: typing.Optional[str]

### notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyNotification]

### assetCompositeModelId
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyPathSegment]]

### externalId
- **Type**: typing.Optional[str]


# AssetPropertyValue

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Variant'>
- **Required**: Yes

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TimeInNanos'>
- **Required**: Yes

### quality
- **Type**: typing.Optional[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]


# AssetRelationshipSummary

### relationshipType
- **Type**: typing.Literal['HIERARCHY']
- **Required**: Yes

### hierarchyInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetHierarchyInfo]


# AssetStatus

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ErrorDetails]


# AssetSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetStatus'>
- **Required**: Yes

### hierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetHierarchy]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# AssociateAssetsRequest

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


# AssociateTimeSeriesToAssetPropertyRequest

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


# AssociatedAssetsSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetStatus'>
- **Required**: Yes

### hierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetHierarchy]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# Attribute

### defaultValue
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateProjectAssetsRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### assetIds
- **Type**: typing.List[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchAssociateProjectAssetsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetErrorDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateProjectAssetsRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### assetIds
- **Type**: typing.List[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# BatchDisassociateProjectAssetsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetErrorDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregateTypes
- **Type**: typing.List[typing.Literal['AVERAGE', 'COUNT', 'MAXIMUM', 'MINIMUM', 'STANDARD_DEVIATION', 'SUM']]
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
- **Type**: typing.Optional[typing.List[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# BatchGetAssetPropertyAggregatesErrorEntry

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entryId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesErrorInfo

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchGetAssetPropertyAggregatesRequest

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyAggregatesEntry]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# BatchGetAssetPropertyAggregatesResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyAggregatesErrorEntry]
- **Required**: Yes

### successEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyAggregatesSuccessEntry]
- **Required**: Yes

### skippedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyAggregatesSkippedEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyAggregatesSkippedEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### completionStatus
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyAggregatesErrorInfo]


# BatchGetAssetPropertyAggregatesSuccessEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregatedValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AggregatedValue]
- **Required**: Yes


# BatchGetAssetPropertyValueEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyValueErrorEntry

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entryId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAssetPropertyValueErrorInfo

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistoryEntry

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
- **Type**: typing.Optional[typing.List[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# BatchGetAssetPropertyValueHistoryErrorEntry

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### entryId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistoryErrorInfo

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'InvalidRequestException', 'ResourceNotFoundException']
- **Required**: Yes

### errorTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchGetAssetPropertyValueHistoryRequest

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueHistoryEntry]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# BatchGetAssetPropertyValueHistoryResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueHistoryErrorEntry]
- **Required**: Yes

### successEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueHistorySuccessEntry]
- **Required**: Yes

### skippedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueHistorySkippedEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyValueHistorySkippedEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### completionStatus
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueHistoryErrorInfo]


# BatchGetAssetPropertyValueHistorySuccessEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetPropertyValueHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyValue]
- **Required**: Yes


# BatchGetAssetPropertyValueRequest

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueEntry]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyValueResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueErrorEntry]
- **Required**: Yes

### successEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueSuccessEntry]
- **Required**: Yes

### skippedEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueSkippedEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# BatchGetAssetPropertyValueSkippedEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### completionStatus
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchGetAssetPropertyValueErrorInfo]


# BatchGetAssetPropertyValueSuccessEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### assetPropertyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyValue]


# BatchPutAssetPropertyError

### errorCode
- **Type**: typing.Literal['AccessDeniedException', 'ConflictingOperationException', 'InternalFailureException', 'InvalidRequestException', 'LimitExceededException', 'ResourceNotFoundException', 'ServiceUnavailableException', 'ThrottlingException', 'TimestampOutOfRangeException']
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### timestamps
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TimeInNanos]
- **Required**: Yes


# BatchPutAssetPropertyErrorEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchPutAssetPropertyError]
- **Required**: Yes


# BatchPutAssetPropertyValueRequest

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PutAssetPropertyValueEntry]
- **Required**: Yes

### enablePartialEntryProcessing
- **Type**: typing.Optional[bool]


# BatchPutAssetPropertyValueResponse

### errorEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.BatchPutAssetPropertyErrorEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# Citation

### reference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Reference]

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Content]


# ColumnInfo

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ColumnType]


# ColumnType

### scalarType
- **Type**: typing.Optional[typing.Literal['BOOLEAN', 'DOUBLE', 'INT', 'STRING', 'TIMESTAMP']]


# CompositeModelProperty

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### assetProperty
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Property'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]


# CompositionDetails

### compositionRelationship
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.CompositionRelationshipItem]]


# CompositionRelationshipItem

### id
- **Type**: typing.Optional[str]


# CompositionRelationshipSummary

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelType
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationErrorDetails

### code
- **Type**: typing.Literal['INTERNAL_FAILURE', 'VALIDATION_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationStatus

### state
- **Type**: typing.Literal['ACTIVE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ConfigurationErrorDetails]


# ConflictingOperationException

### message
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# Content

### text
- **Type**: typing.Optional[str]


# CreateAccessPolicyRequest

### accessPolicyIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Identity'>
- **Required**: Yes

### accessPolicyResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Resource'>
- **Required**: Yes

### accessPolicyPermission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAccessPolicyResponse

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetModelCompositeModelRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelType
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelExternalId
- **Type**: typing.Optional[str]

### parentAssetModelCompositeModelId
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyDefinition]]

### ifMatch
- **Type**: typing.Optional[str]

### ifNoneMatch
- **Type**: typing.Optional[str]

### matchForVersionType
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'LATEST']]


# CreateAssetModelCompositeModelResponse

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelPathSegment]
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetModelRequest

### assetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelType
- **Type**: typing.Optional[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]

### assetModelId
- **Type**: typing.Optional[str]

### assetModelExternalId
- **Type**: typing.Optional[str]

### assetModelDescription
- **Type**: typing.Optional[str]

### assetModelProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyDefinition]]

### assetModelHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelHierarchyDefinition]]

### assetModelCompositeModels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelDefinition]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAssetModelResponse

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetRequest

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### assetDescription
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### assetExternalId
- **Type**: typing.Optional[str]


# CreateAssetResponse

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBulkImportJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.File]
- **Required**: Yes

### errorReportLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ErrorReportLocation'>
- **Required**: Yes

### jobConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.JobConfiguration, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.JobConfigurationOutput]
- **Required**: Yes

### adaptiveIngestion
- **Type**: typing.Optional[bool]

### deleteFilesAfterImport
- **Type**: typing.Optional[bool]


# CreateBulkImportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDashboardRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDashboardResponse

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetSource'>
- **Required**: Yes

### datasetId
- **Type**: typing.Optional[str]

### datasetDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDatasetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGatewayRequest

### gatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayPlatform
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GatewayPlatform'>
- **Required**: Yes

### gatewayVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateGatewayResponse

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePortalRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ImageFile]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### portalAuthMode
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]

### notificationSenderEmail
- **Type**: typing.Optional[str]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Alarms]

### portalType
- **Type**: typing.Optional[typing.Literal['SITEWISE_PORTAL_V1', 'SITEWISE_PORTAL_V2']]

### portalTypeConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalTypeEntry, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalTypeEntryOutput]]]


# CreatePortalResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalStatus'>
- **Required**: Yes

### ssoApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProjectResponse

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# Csv

### columnNames
- **Type**: typing.List[typing.Literal['ALIAS', 'ASSET_ID', 'DATA_TYPE', 'PROPERTY_ID', 'QUALITY', 'TIMESTAMP_NANO_OFFSET', 'TIMESTAMP_SECONDS', 'VALUE']]
- **Required**: Yes


# CsvOutput

### columnNames
- **Type**: typing.List[typing.Literal['ALIAS', 'ASSET_ID', 'DATA_TYPE', 'PROPERTY_ID', 'QUALITY', 'TIMESTAMP_NANO_OFFSET', 'TIMESTAMP_SECONDS', 'VALUE']]
- **Required**: Yes


# CustomerManagedS3Storage

### s3ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DashboardSummary

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


# DataSetReference

### datasetArn
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Source]


# DatasetSource

### sourceType
- **Type**: typing.Literal['KENDRA']
- **Required**: Yes

### sourceFormat
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### sourceDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.SourceDetail]


# DatasetStatus

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ErrorDetails]


# DatasetSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetStatus'>
- **Required**: Yes


# Datum

### scalarValue
- **Type**: typing.Optional[str]

### arrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### rowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### nullValue
- **Type**: typing.Optional[bool]


# DatumPaginator

### scalarValue
- **Type**: typing.Optional[str]

### arrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### rowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### nullValue
- **Type**: typing.Optional[bool]


# DatumWaiter

### scalarValue
- **Type**: typing.Optional[str]

### arrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### rowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### nullValue
- **Type**: typing.Optional[bool]


# DeleteAccessPolicyRequest

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAssetModelCompositeModelRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### ifMatch
- **Type**: typing.Optional[str]

### ifNoneMatch
- **Type**: typing.Optional[str]

### matchForVersionType
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'LATEST']]


# DeleteAssetModelCompositeModelResponse

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAssetModelRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### ifMatch
- **Type**: typing.Optional[str]

### ifNoneMatch
- **Type**: typing.Optional[str]

### matchForVersionType
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'LATEST']]


# DeleteAssetModelResponse

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAssetRequest

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteAssetResponse

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDashboardRequest

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteDatasetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteDatasetResponse

### datasetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGatewayRequest

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePortalRequest

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePortalResponse

### portalStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteTimeSeriesRequest

### alias
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# DescribeAccessPolicyRequest

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessPolicyResponse

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Identity'>
- **Required**: Yes

### accessPolicyResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Resource'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeActionRequest

### actionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActionResponse

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TargetResource'>
- **Required**: Yes

### actionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ActionPayload'>
- **Required**: Yes

### executionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetCompositeModelRequest

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetCompositeModelResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetCompositeModelPathSegment]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetProperty]
- **Required**: Yes

### assetCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetCompositeModelSummary]
- **Required**: Yes

### actionDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ActionDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetModelCompositeModelRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelCompositeModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelVersion
- **Type**: typing.Optional[str]


# DescribeAssetModelCompositeModelResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelPathSegment]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyOutput]
- **Required**: Yes

### compositionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.CompositionDetails'>
- **Required**: Yes

### assetModelCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelSummary]
- **Required**: Yes

### actionDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ActionDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetModelRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### assetModelVersion
- **Type**: typing.Optional[str]


# DescribeAssetModelRequestWait

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### assetModelVersion
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAssetModelRequestWaitExtra

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### assetModelVersion
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAssetModelResponse

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelType
- **Type**: typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']
- **Required**: Yes

### assetModelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyOutput]
- **Required**: Yes

### assetModelHierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelHierarchy]
- **Required**: Yes

### assetModelCompositeModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelOutput]
- **Required**: Yes

### assetModelCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelSummary]
- **Required**: Yes

### assetModelCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetModelLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### assetModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### eTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetPropertyRequest

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetPropertyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Property'>
- **Required**: Yes

### compositeModel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.CompositeModelProperty'>
- **Required**: Yes

### assetExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAssetRequest

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]


# DescribeAssetRequestWait

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAssetRequestWaitExtra

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### excludeProperties
- **Type**: typing.Optional[bool]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAssetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetProperty]
- **Required**: Yes

### assetHierarchies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetHierarchy]
- **Required**: Yes

### assetCompositeModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetCompositeModel]
- **Required**: Yes

### assetCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetStatus'>
- **Required**: Yes

### assetDescription
- **Type**: <class 'str'>
- **Required**: Yes

### assetCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetCompositeModelSummary]
- **Required**: Yes

### assetExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBulkImportJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBulkImportJobResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.File]
- **Required**: Yes

### errorReportLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ErrorReportLocation'>
- **Required**: Yes

### jobConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.JobConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDashboardRequest

### dashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDashboardResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetDescription
- **Type**: <class 'str'>
- **Required**: Yes

### datasetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetSource'>
- **Required**: Yes

### datasetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetStatus'>
- **Required**: Yes

### datasetCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### datasetLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### datasetVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDefaultEncryptionConfigurationResponse

### encryptionType
- **Type**: typing.Literal['KMS_BASED_ENCRYPTION', 'SITEWISE_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ConfigurationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGatewayCapabilityConfigurationRequest

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayCapabilityConfigurationResponse

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
- **Type**: typing.Literal['IN_SYNC', 'NOT_APPLICABLE', 'OUT_OF_SYNC', 'SYNC_FAILED', 'UNKNOWN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGatewayRequest

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GatewayPlatform'>
- **Required**: Yes

### gatewayVersion
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayCapabilitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GatewayCapabilitySummary]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoggingOptionsResponse

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.LoggingOptions'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePortalRequest

### portalId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePortalRequestWait

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribePortalRequestWaitExtra

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribePortalResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalStatus'>
- **Required**: Yes

### portalCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### portalLastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### portalLogoImageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ImageLocation'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Alarms'>
- **Required**: Yes

### portalType
- **Type**: typing.Literal['SITEWISE_PORTAL_V1', 'SITEWISE_PORTAL_V2']
- **Required**: Yes

### portalTypeConfiguration
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalTypeEntryOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProjectRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStorageConfigurationResponse

### storageType
- **Type**: typing.Literal['MULTI_LAYER_STORAGE', 'SITEWISE_DEFAULT_STORAGE']
- **Required**: Yes

### multiLayerStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MultiLayerStorage'>
- **Required**: Yes

### disassociatedDataStorage
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.RetentionPeriod'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ConfigurationStatus'>
- **Required**: Yes

### lastUpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### warmTier
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### warmTierRetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.WarmTierRetentionPeriod'>
- **Required**: Yes

### disallowIngestNullNaN
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTimeSeriesRequest

### alias
- **Type**: typing.Optional[str]

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]


# DescribeTimeSeriesResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# DetailedError

### code
- **Type**: typing.Literal['INCOMPATIBLE_COMPUTE_LOCATION', 'INCOMPATIBLE_FORWARDING_CONFIGURATION']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateAssetsRequest

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


# DisassociateTimeSeriesFromAssetPropertyRequest

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorDetails

### code
- **Type**: typing.Literal['INTERNAL_FAILURE', 'VALIDATION_ERROR']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DetailedError]]


# ErrorReportLocation

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: <class 'str'>
- **Required**: Yes


# ExecuteActionRequest

### targetResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TargetResource'>
- **Required**: Yes

### actionDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ActionPayload'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ExecuteActionResponse

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteQueryRequest

### queryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]


# ExecuteQueryRequestPaginate

### queryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ExecuteQueryResponse

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ColumnInfo]
- **Required**: Yes

### rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Row]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExecuteQueryResponsePaginator

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ColumnInfo]
- **Required**: Yes

### rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.RowPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExecuteQueryResponseWaiter

### columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ColumnInfo]
- **Required**: Yes

### rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.RowWaiter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExpressionVariable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.VariableValue, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.VariableValueOutput]
- **Required**: Yes


# ExpressionVariableOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.VariableValueOutput'>
- **Required**: Yes


# File

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### versionId
- **Type**: typing.Optional[str]


# FileFormat

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Csv]

### parquet
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FileFormatOutput

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.CsvOutput]

### parquet
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ForwardingConfig

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# GatewayCapabilitySummary

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilitySyncStatus
- **Type**: typing.Literal['IN_SYNC', 'NOT_APPLICABLE', 'OUT_OF_SYNC', 'SYNC_FAILED', 'UNKNOWN']
- **Required**: Yes


# GatewayPlatform

### greengrass
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Greengrass]

### greengrassV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GreengrassV2]

### siemensIE
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.SiemensIE]


# GatewaySummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GatewayPlatform]

### gatewayVersion
- **Type**: typing.Optional[str]

### gatewayCapabilitySummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GatewayCapabilitySummary]]


# GetAssetPropertyAggregatesRequest

### aggregateTypes
- **Type**: typing.List[typing.Literal['AVERAGE', 'COUNT', 'MAXIMUM', 'MINIMUM', 'STANDARD_DEVIATION', 'SUM']]
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
- **Type**: typing.Optional[typing.List[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetAssetPropertyAggregatesRequestPaginate

### aggregateTypes
- **Type**: typing.List[typing.Literal['AVERAGE', 'COUNT', 'MAXIMUM', 'MINIMUM', 'STANDARD_DEVIATION', 'SUM']]
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
- **Type**: typing.Optional[typing.List[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# GetAssetPropertyAggregatesResponse

### aggregatedValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AggregatedValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetAssetPropertyValueHistoryRequest

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
- **Type**: typing.Optional[typing.List[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetAssetPropertyValueHistoryRequestPaginate

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
- **Type**: typing.Optional[typing.List[typing.Literal['BAD', 'GOOD', 'UNCERTAIN']]]

### timeOrdering
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# GetAssetPropertyValueHistoryResponse

### assetPropertyValueHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetAssetPropertyValueRequest

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# GetAssetPropertyValueResponse

### propertyValue
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyValue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# GetInterpolatedAssetPropertyValuesRequest

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


# GetInterpolatedAssetPropertyValuesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# GetInterpolatedAssetPropertyValuesResponse

### interpolatedAssetPropertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.InterpolatedAssetPropertyValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Greengrass

### groupArn
- **Type**: <class 'str'>
- **Required**: Yes


# GreengrassV2

### coreDeviceThingName
- **Type**: <class 'str'>
- **Required**: Yes

### coreDeviceOperatingSystem
- **Type**: typing.Optional[typing.Literal['LINUX_AARCH64', 'LINUX_AMD64', 'WINDOWS_AMD64']]


# GroupIdentity

### id
- **Type**: <class 'str'>
- **Required**: Yes


# IAMRoleIdentity

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# IAMUserIdentity

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# Identity

### user
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.UserIdentity]

### group
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GroupIdentity]

### iamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.IAMUserIdentity]

### iamRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.IAMRoleIdentity]


# Image

### id
- **Type**: typing.Optional[str]

### file
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ImageFile]


# ImageFile

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### type
- **Type**: typing.Literal['PNG']
- **Required**: Yes


# ImageLocation

### id
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes


# InternalFailureException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# InterpolatedAssetPropertyValue

### timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TimeInNanos'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Variant'>
- **Required**: Yes


# InvalidRequestException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# InvocationOutput

### message
- **Type**: typing.Optional[str]

### citations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Citation]]


# InvokeAssistantRequest

### message
- **Type**: <class 'str'>
- **Required**: Yes

### conversationId
- **Type**: typing.Optional[str]

### enableTrace
- **Type**: typing.Optional[bool]


# InvokeAssistantResponse

### body
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseStream]
- **Required**: Yes

### conversationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# JobConfiguration

### fileFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.FileFormat'>
- **Required**: Yes


# JobConfigurationOutput

### fileFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.FileFormatOutput'>
- **Required**: Yes


# JobSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']
- **Required**: Yes


# KendraSourceDetail

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# LimitExceededException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessPoliciesRequest

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


# ListAccessPoliciesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAccessPoliciesResponse

### accessPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AccessPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListActionsRequest

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


# ListActionsRequestPaginate

### targetResourceType
- **Type**: typing.Literal['ASSET']
- **Required**: Yes

### targetResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListActionsResponse

### actionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ActionSummary]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# ListAssetModelCompositeModelsRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### assetModelVersion
- **Type**: typing.Optional[str]


# ListAssetModelCompositeModelsRequestPaginate

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssetModelCompositeModelsResponse

### assetModelCompositeModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetModelPropertiesRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]

### assetModelVersion
- **Type**: typing.Optional[str]


# ListAssetModelPropertiesRequestPaginate

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]

### assetModelVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssetModelPropertiesResponse

### assetModelPropertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetModelsRequest

### assetModelTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### assetModelVersion
- **Type**: typing.Optional[str]


# ListAssetModelsRequestPaginate

### assetModelTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ASSET_MODEL', 'COMPONENT_MODEL']]]

### assetModelVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssetModelsResponse

### assetModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetPropertiesRequest

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]


# ListAssetPropertiesRequestPaginate

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'BASE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssetPropertiesResponse

### assetPropertySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetRelationshipsRequest

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


# ListAssetRelationshipsRequestPaginate

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### traversalType
- **Type**: typing.Literal['PATH_TO_ROOT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssetRelationshipsResponse

### assetRelationshipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetRelationshipSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### assetModelId
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'TOP_LEVEL']]


# ListAssetsRequestPaginate

### assetModelId
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'TOP_LEVEL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssetsResponse

### assetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedAssetsRequest

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


# ListAssociatedAssetsRequestPaginate

### assetId
- **Type**: <class 'str'>
- **Required**: Yes

### hierarchyId
- **Type**: typing.Optional[str]

### traversalDirection
- **Type**: typing.Optional[typing.Literal['CHILD', 'PARENT']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListAssociatedAssetsResponse

### assetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssociatedAssetsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBulkImportJobsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']]


# ListBulkImportJobsRequestPaginate

### filter
- **Type**: typing.Optional[typing.Literal['ALL', 'CANCELLED', 'COMPLETED', 'COMPLETED_WITH_FAILURES', 'FAILED', 'PENDING', 'RUNNING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListBulkImportJobsResponse

### jobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCompositionRelationshipsRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCompositionRelationshipsRequestPaginate

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListCompositionRelationshipsResponse

### compositionRelationshipSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.CompositionRelationshipSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDashboardsRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDashboardsRequestPaginate

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListDashboardsResponse

### dashboardSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DashboardSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequest

### sourceType
- **Type**: typing.Literal['KENDRA']
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsRequestPaginate

### sourceType
- **Type**: typing.Literal['KENDRA']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListDatasetsResponse

### datasetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGatewaysRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListGatewaysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListGatewaysResponse

### gatewaySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.GatewaySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPortalsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPortalsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListPortalsResponse

### portalSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectAssetsRequest

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectAssetsRequestPaginate

### projectId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListProjectAssetsResponse

### assetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequest

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListProjectsRequestPaginate

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListProjectsResponse

### projectSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# ListTimeSeriesRequest

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


# ListTimeSeriesRequestPaginate

### assetId
- **Type**: typing.Optional[str]

### aliasPrefix
- **Type**: typing.Optional[str]

### timeSeriesType
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'DISASSOCIATED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PaginatorConfig]


# ListTimeSeriesResponse

### TimeSeriesSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TimeSeriesSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Location

### uri
- **Type**: typing.Optional[str]


# LoggingOptions

### level
- **Type**: typing.Literal['ERROR', 'INFO', 'OFF']
- **Required**: Yes


# Measurement

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MeasurementProcessingConfig]


# MeasurementProcessingConfig

### forwardingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ForwardingConfig'>
- **Required**: Yes


# Metric

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ExpressionVariable, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ExpressionVariableOutput]]
- **Required**: Yes

### window
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MetricWindow'>
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MetricProcessingConfig]


# MetricOutput

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ExpressionVariableOutput]
- **Required**: Yes

### window
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MetricWindow'>
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MetricProcessingConfig]


# MetricProcessingConfig

### computeLocation
- **Type**: typing.Literal['CLOUD', 'EDGE']
- **Required**: Yes


# MetricWindow

### tumbling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TumblingWindow]


# MonitorErrorDetails

### code
- **Type**: typing.Optional[typing.Literal['INTERNAL_FAILURE', 'LIMIT_EXCEEDED', 'VALIDATION_ERROR']]

### message
- **Type**: typing.Optional[str]


# MultiLayerStorage

### customerManagedS3Storage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.CustomerManagedS3Storage'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortalResource

### id
- **Type**: <class 'str'>
- **Required**: Yes


# PortalStatus

### state
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'PENDING', 'UPDATING']
- **Required**: Yes

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MonitorErrorDetails]


# PortalSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalStatus'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateDate
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]

### portalType
- **Type**: typing.Optional[typing.Literal['SITEWISE_PORTAL_V1', 'SITEWISE_PORTAL_V2']]


# PortalTypeEntry

### portalTools
- **Type**: typing.Optional[typing.List[str]]


# PortalTypeEntryOutput

### portalTools
- **Type**: typing.Optional[typing.List[str]]


# ProjectResource

### id
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectSummary

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


# Property

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyNotification]

### unit
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyTypeOutput]

### path
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyPathSegment]]

### externalId
- **Type**: typing.Optional[str]


# PropertyNotification

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# PropertyType

### attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Attribute]

### measurement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Measurement]

### transform
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Transform, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TransformOutput, NoneType]

### metric
- **Type**: typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Metric, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MetricOutput, NoneType]


# PropertyTypeOutput

### attribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Attribute]

### measurement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Measurement]

### transform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TransformOutput]

### metric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MetricOutput]


# PropertyValueNullValue

### valueType
- **Type**: typing.Literal['B', 'D', 'I', 'S', 'U']
- **Required**: Yes


# PutAssetPropertyValueEntry

### entryId
- **Type**: <class 'str'>
- **Required**: Yes

### propertyValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetPropertyValue]
- **Required**: Yes

### assetId
- **Type**: typing.Optional[str]

### propertyId
- **Type**: typing.Optional[str]

### propertyAlias
- **Type**: typing.Optional[str]


# PutDefaultEncryptionConfigurationRequest

### encryptionType
- **Type**: typing.Literal['KMS_BASED_ENCRYPTION', 'SITEWISE_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# PutDefaultEncryptionConfigurationResponse

### encryptionType
- **Type**: typing.Literal['KMS_BASED_ENCRYPTION', 'SITEWISE_DEFAULT_ENCRYPTION']
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ConfigurationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# PutLoggingOptionsRequest

### loggingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.LoggingOptions'>
- **Required**: Yes


# PutStorageConfigurationRequest

### storageType
- **Type**: typing.Literal['MULTI_LAYER_STORAGE', 'SITEWISE_DEFAULT_STORAGE']
- **Required**: Yes

### multiLayerStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MultiLayerStorage]

### disassociatedDataStorage
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### retentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.RetentionPeriod]

### warmTier
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### warmTierRetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.WarmTierRetentionPeriod]

### disallowIngestNullNaN
- **Type**: typing.Optional[bool]


# PutStorageConfigurationResponse

### storageType
- **Type**: typing.Literal['MULTI_LAYER_STORAGE', 'SITEWISE_DEFAULT_STORAGE']
- **Required**: Yes

### multiLayerStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.MultiLayerStorage'>
- **Required**: Yes

### disassociatedDataStorage
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### retentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.RetentionPeriod'>
- **Required**: Yes

### configurationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ConfigurationStatus'>
- **Required**: Yes

### warmTier
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### warmTierRetentionPeriod
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.WarmTierRetentionPeriod'>
- **Required**: Yes

### disallowIngestNullNaN
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# Reference

### dataset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DataSetReference]


# Resource

### portal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalResource]

### project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ProjectResource]


# ResourceNotFoundException

### message
- **Type**: <class 'str'>
- **Required**: Yes


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


# ResponseStream

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Trace]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.InvocationOutput]

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AccessDeniedException]

### conflictingOperationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ConflictingOperationException]

### internalFailureException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.InternalFailureException]

### invalidRequestException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.InvalidRequestException]

### limitExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.LimitExceededException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResourceNotFoundException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ThrottlingException]


# RetentionPeriod

### numberOfDays
- **Type**: typing.Optional[int]

### unlimited
- **Type**: typing.Optional[bool]


# Row

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Datum]
- **Required**: Yes


# RowPaginator

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatumPaginator]
- **Required**: Yes


# RowWaiter

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatumWaiter]
- **Required**: Yes


# SiemensIE

### iotCoreThingName
- **Type**: <class 'str'>
- **Required**: Yes


# Source

### arn
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Location]


# SourceDetail

### kendra
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.KendraSourceDetail]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetResource

### assetId
- **Type**: <class 'str'>
- **Required**: Yes


# ThrottlingException

### message
- **Type**: <class 'str'>
- **Required**: Yes


# TimeInNanos

### timeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### offsetInNanos
- **Type**: typing.Optional[int]


# TimeSeriesSummary

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


# Trace

### text
- **Type**: typing.Optional[str]


# Transform

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ExpressionVariable, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ExpressionVariableOutput]]
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TransformProcessingConfig]


# TransformOutput

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ExpressionVariableOutput]
- **Required**: Yes

### processingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.TransformProcessingConfig]


# TransformProcessingConfig

### computeLocation
- **Type**: typing.Literal['CLOUD', 'EDGE']
- **Required**: Yes

### forwardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ForwardingConfig]


# TumblingWindow

### interval
- **Type**: <class 'str'>
- **Required**: Yes

### offset
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccessPolicyRequest

### accessPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicyIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Identity'>
- **Required**: Yes

### accessPolicyResource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Resource'>
- **Required**: Yes

### accessPolicyPermission
- **Type**: typing.Literal['ADMINISTRATOR', 'VIEWER']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateAssetModelCompositeModelRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelProperty, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyOutput]]]

### ifMatch
- **Type**: typing.Optional[str]

### ifNoneMatch
- **Type**: typing.Optional[str]

### matchForVersionType
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'LATEST']]


# UpdateAssetModelCompositeModelResponse

### assetModelCompositeModelPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelPathSegment]
- **Required**: Yes

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssetModelRequest

### assetModelId
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelName
- **Type**: <class 'str'>
- **Required**: Yes

### assetModelExternalId
- **Type**: typing.Optional[str]

### assetModelDescription
- **Type**: typing.Optional[str]

### assetModelProperties
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelProperty, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyOutput]]]

### assetModelHierarchies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelHierarchy]]

### assetModelCompositeModels
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModel, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelCompositeModelOutput]]]

### clientToken
- **Type**: typing.Optional[str]

### ifMatch
- **Type**: typing.Optional[str]

### ifNoneMatch
- **Type**: typing.Optional[str]

### matchForVersionType
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'LATEST']]


# UpdateAssetModelResponse

### assetModelStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssetPropertyRequest

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


# UpdateAssetRequest

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


# UpdateAssetResponse

### assetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardRequest

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


# UpdateDatasetRequest

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetSource'>
- **Required**: Yes

### datasetDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateDatasetResponse

### datasetId
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.DatasetStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewayCapabilityConfigurationRequest

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGatewayCapabilityConfigurationResponse

### capabilityNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### capabilitySyncStatus
- **Type**: typing.Literal['IN_SYNC', 'NOT_APPLICABLE', 'OUT_OF_SYNC', 'SYNC_FAILED', 'UNKNOWN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewayRequest

### gatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### gatewayName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePortalRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Image]

### clientToken
- **Type**: typing.Optional[str]

### notificationSenderEmail
- **Type**: typing.Optional[str]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.Alarms]

### portalType
- **Type**: typing.Optional[typing.Literal['SITEWISE_PORTAL_V1', 'SITEWISE_PORTAL_V2']]

### portalTypeConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalTypeEntry, aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalTypeEntryOutput]]]


# UpdatePortalResponse

### portalStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PortalStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectRequest

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


# UserIdentity

### id
- **Type**: <class 'str'>
- **Required**: Yes


# VariableValue

### propertyId
- **Type**: typing.Optional[str]

### hierarchyId
- **Type**: typing.Optional[str]

### propertyPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyPathSegment]]


# VariableValueOutput

### propertyId
- **Type**: typing.Optional[str]

### hierarchyId
- **Type**: typing.Optional[str]

### propertyPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.AssetModelPropertyPathSegment]]


# Variant

### stringValue
- **Type**: typing.Optional[str]

### integerValue
- **Type**: typing.Optional[int]

### doubleValue
- **Type**: typing.Optional[float]

### booleanValue
- **Type**: typing.Optional[bool]

### nullValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsitewise.iotsitewise_classes.PropertyValueNullValue]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarmTierRetentionPeriod

### numberOfDays
- **Type**: typing.Optional[int]

### unlimited
- **Type**: typing.Optional[bool]


