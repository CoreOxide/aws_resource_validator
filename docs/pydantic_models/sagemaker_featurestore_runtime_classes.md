# Sagemaker Featurestore Runtime Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetRecordError

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


# BatchGetRecordIdentifier

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifiersValueAsString
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FeatureNames
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetRecordIdentifierOutput

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifiersValueAsString
- **Type**: typing.List[str]
- **Required**: Yes

### FeatureNames
- **Type**: typing.Optional[typing.List[str]]


# BatchGetRecordIdentifierUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetRecordRequest

### Identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordIdentifierUnion]
- **Required**: Yes

### ExpirationTimeResponse
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# BatchGetRecordResponse

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordResultDetail]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordError]
- **Required**: Yes

### UnprocessedIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.BatchGetRecordIdentifierOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetRecordResultDetail

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierValueAsString
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.FeatureValueOutput]
- **Required**: Yes

### ExpiresAt
- **Type**: typing.Optional[str]


# DeleteRecordRequest

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# FeatureValue

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### ValueAsString
- **Type**: typing.Optional[str]

### ValueAsStringList
- **Type**: typing.Optional[typing.Sequence[str]]


# FeatureValueOutput

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### ValueAsString
- **Type**: typing.Optional[str]

### ValueAsStringList
- **Type**: typing.Optional[typing.List[str]]


# FeatureValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetRecordRequest

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


# GetRecordResponse

### Record
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.FeatureValueOutput]
- **Required**: Yes

### ExpiresAt
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# PutRecordRequest

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Record
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_classes.FeatureValueUnion]
- **Required**: Yes

### TargetStores
- **Type**: typing.Optional[typing.Sequence[typing.Literal['OfflineStore', 'OnlineStore']]]

### TtlDuration
- **Type**: <class 'NoneType'>


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


# TtlDuration

### Unit
- **Type**: typing.Literal['Days', 'Hours', 'Minutes', 'Seconds', 'Weeks']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


