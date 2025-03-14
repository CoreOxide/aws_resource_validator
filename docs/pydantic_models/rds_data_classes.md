# Rds Data Classes

# ArrayValueOutputTypeDef

### booleanValues
- **Type**: typing.Optional[typing.List[bool]]

### longValues
- **Type**: typing.Optional[typing.List[int]]

### doubleValues
- **Type**: typing.Optional[typing.List[float]]

### stringValues
- **Type**: typing.Optional[typing.List[str]]

### arrayValues
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ArrayValueTypeDef

### booleanValues
- **Type**: typing.Optional[typing.Sequence[bool]]

### longValues
- **Type**: typing.Optional[typing.Sequence[int]]

### doubleValues
- **Type**: typing.Optional[typing.Sequence[float]]

### stringValues
- **Type**: typing.Optional[typing.Sequence[str]]

### arrayValues
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ArrayValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchExecuteStatementRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### sql
- **Type**: <class 'str'>
- **Required**: Yes

### database
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### parameterSets
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.rds_data_classes.SqlParameterTypeDef]]]

### transactionId
- **Type**: typing.Optional[str]


# BatchExecuteStatementResponseTypeDef

### updateResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data_classes.UpdateResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BeginTransactionRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### database
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]


# BeginTransactionResponseTypeDef

### transactionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitTransactionRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### transactionId
- **Type**: <class 'str'>
- **Required**: Yes


# CommitTransactionResponseTypeDef

### transactionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteSqlRequestTypeDef

### dbClusterOrInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsSecretStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### sqlStatements
- **Type**: <class 'str'>
- **Required**: Yes

### database
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]


# ExecuteSqlResponseTypeDef

### sqlStatementResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data_classes.SqlStatementResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteStatementRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### sql
- **Type**: <class 'str'>
- **Required**: Yes

### database
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rds_data_classes.SqlParameterTypeDef]]

### transactionId
- **Type**: typing.Optional[str]

### includeResultMetadata
- **Type**: typing.Optional[bool]

### continueAfterTimeout
- **Type**: typing.Optional[bool]

### resultSetOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.ResultSetOptionsTypeDef]

### formatRecordsAs
- **Type**: typing.Optional[typing.Literal['JSON', 'NONE']]


# ExecuteStatementResponseTypeDef

### records
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.rds_data_classes.FieldOutputTypeDef]]
- **Required**: Yes

### columnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data_classes.ColumnMetadataTypeDef]
- **Required**: Yes

### numberOfRecordsUpdated
- **Type**: <class 'int'>
- **Required**: Yes

### generatedFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data_classes.FieldOutputTypeDef]
- **Required**: Yes

### formattedRecords
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FieldOutputTypeDef

### isNull
- **Type**: typing.Optional[bool]

### booleanValue
- **Type**: typing.Optional[bool]

### longValue
- **Type**: typing.Optional[int]

### doubleValue
- **Type**: typing.Optional[float]

### stringValue
- **Type**: typing.Optional[str]

### blobValue
- **Type**: typing.Optional[bytes]

### arrayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.ArrayValueOutputTypeDef]


# FieldTypeDef

### isNull
- **Type**: typing.Optional[bool]

### booleanValue
- **Type**: typing.Optional[bool]

### longValue
- **Type**: typing.Optional[int]

### doubleValue
- **Type**: typing.Optional[float]

### stringValue
- **Type**: typing.Optional[str]

### blobValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.BlobTypeDef]

### arrayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.ArrayValueUnionTypeDef]


# FieldUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordTypeDef

### values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data_classes.ValueTypeDef]]


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


# ResultFrameTypeDef

### resultSetMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.ResultSetMetadataTypeDef]

### records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data_classes.RecordTypeDef]]


# ResultSetMetadataTypeDef

### columnCount
- **Type**: typing.Optional[int]

### columnMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data_classes.ColumnMetadataTypeDef]]


# ResultSetOptionsTypeDef

### decimalReturnType
- **Type**: typing.Optional[typing.Literal['DOUBLE_OR_LONG', 'STRING']]

### longReturnType
- **Type**: typing.Optional[typing.Literal['LONG', 'STRING']]


# RollbackTransactionRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### transactionId
- **Type**: <class 'str'>
- **Required**: Yes


# RollbackTransactionResponseTypeDef

### transactionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SqlParameterTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.FieldUnionTypeDef]

### typeHint
- **Type**: typing.Optional[typing.Literal['DATE', 'DECIMAL', 'JSON', 'TIME', 'TIMESTAMP', 'UUID']]


# SqlStatementResultTypeDef

### resultFrame
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.ResultFrameTypeDef]

### numberOfRecordsUpdated
- **Type**: typing.Optional[int]


# StructValueTypeDef

### attributes
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# UpdateResultTypeDef

### generatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data_classes.FieldOutputTypeDef]]


# ValueTypeDef

### isNull
- **Type**: typing.Optional[bool]

### bitValue
- **Type**: typing.Optional[bool]

### bigIntValue
- **Type**: typing.Optional[int]

### intValue
- **Type**: typing.Optional[int]

### doubleValue
- **Type**: typing.Optional[float]

### realValue
- **Type**: typing.Optional[float]

### stringValue
- **Type**: typing.Optional[str]

### blobValue
- **Type**: typing.Optional[bytes]

### arrayValues
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### structValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data_classes.StructValueTypeDef]


