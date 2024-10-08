# Pydantic Models in sagemaker_featurestore_runtime_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetRecordErrorTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierValueAsString
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetRecordIdentifierTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifiersValueAsString
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FeatureNames
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetRecordRequestRequestTypeDef

### Identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordIdentifierTypeDef]
- **Required**: Yes

### ExpirationTimeResponse
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# BatchGetRecordResponseTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordResultDetailTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordErrorTypeDef]
- **Required**: Yes

### UnprocessedIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetRecordResultDetailTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierValueAsString
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.FeatureValueTypeDef]
- **Required**: Yes

### ExpiresAt
- **Type**: typing.Optional[str]


# DeleteRecordRequestRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierValueAsString
- **Type**: <class 'str'>
- **Required**: Yes

### EventTime
- **Type**: <class 'str'>
- **Required**: Yes

### TargetStores
- **Type**: typing.Optional[typing.Sequence[typing.Literal['OfflineStore', 'OnlineStore']]]

### DeletionMode
- **Type**: typing.Optional[typing.Literal['HardDelete', 'SoftDelete']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FeatureValueTypeDef

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### ValueAsString
- **Type**: typing.Optional[str]

### ValueAsStringList
- **Type**: typing.Optional[typing.List[str]]


# GetRecordRequestRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierValueAsString
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ExpirationTimeResponse
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# GetRecordResponseTypeDef

### Record
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.FeatureValueTypeDef]
- **Required**: Yes

### ExpiresAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRecordRequestRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.FeatureValueTypeDef]
- **Required**: Yes

### TargetStores
- **Type**: typing.Optional[typing.Sequence[typing.Literal['OfflineStore', 'OnlineStore']]]

### TtlDuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.TtlDurationTypeDef]


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


# TtlDurationTypeDef

### Unit
- **Type**: typing.Literal['Days', 'Hours', 'Minutes', 'Seconds', 'Weeks']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes

