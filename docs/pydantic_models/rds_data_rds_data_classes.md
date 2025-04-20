# Rds Data Rds Data Classes

# ArrayValue

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


# ArrayValueOutput

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchExecuteStatementRequest

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
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.SqlParameter]]]

### transactionId
- **Type**: typing.Optional[str]


# BatchExecuteStatementResponse

### updateResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.UpdateResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResponseMetadata'>
- **Required**: Yes


# BeginTransactionRequest

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


# BeginTransactionResponse

### transactionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResponseMetadata'>
- **Required**: Yes


# ColumnMetadata

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[int]

### typeName
- **Type**: typing.Optional[str]

### label
- **Type**: typing.Optional[str]

### schemaName
- **Type**: typing.Optional[str]

### tableName
- **Type**: typing.Optional[str]

### isAutoIncrement
- **Type**: typing.Optional[bool]

### isSigned
- **Type**: typing.Optional[bool]

### isCurrency
- **Type**: typing.Optional[bool]

### isCaseSensitive
- **Type**: typing.Optional[bool]

### nullable
- **Type**: typing.Optional[int]

### precision
- **Type**: typing.Optional[int]

### scale
- **Type**: typing.Optional[int]

### arrayBaseColumnType
- **Type**: typing.Optional[int]


# CommitTransactionRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### transactionId
- **Type**: <class 'str'>
- **Required**: Yes


# CommitTransactionResponse

### transactionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteSqlRequest

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


# ExecuteSqlResponse

### sqlStatementResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.SqlStatementResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResponseMetadata'>
- **Required**: Yes


# ExecuteStatementRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.SqlParameter]]

### transactionId
- **Type**: typing.Optional[str]

### includeResultMetadata
- **Type**: typing.Optional[bool]

### continueAfterTimeout
- **Type**: typing.Optional[bool]

### resultSetOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResultSetOptions]

### formatRecordsAs
- **Type**: typing.Optional[typing.Literal['JSON', 'NONE']]


# ExecuteStatementResponse

### records
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.FieldOutput]]
- **Required**: Yes

### columnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ColumnMetadata]
- **Required**: Yes

### numberOfRecordsUpdated
- **Type**: <class 'int'>
- **Required**: Yes

### generatedFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.FieldOutput]
- **Required**: Yes

### formattedRecords
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResponseMetadata'>
- **Required**: Yes


# Field

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### arrayValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ArrayValue, aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ArrayValueOutput, NoneType]


# FieldOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ArrayValueOutput]


# Record

### values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.Value]]


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


# ResultFrame

### resultSetMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResultSetMetadata]

### records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.Record]]


# ResultSetMetadata

### columnCount
- **Type**: typing.Optional[int]

### columnMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ColumnMetadata]]


# ResultSetOptions

### decimalReturnType
- **Type**: typing.Optional[typing.Literal['DOUBLE_OR_LONG', 'STRING']]

### longReturnType
- **Type**: typing.Optional[typing.Literal['LONG', 'STRING']]


# RollbackTransactionRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### transactionId
- **Type**: <class 'str'>
- **Required**: Yes


# RollbackTransactionResponse

### transactionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResponseMetadata'>
- **Required**: Yes


# SqlParameter

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.Field, aws_resource_validator.pydantic_models.rds_data.rds_data_classes.FieldOutput, NoneType]

### typeHint
- **Type**: typing.Optional[typing.Literal['DATE', 'DECIMAL', 'JSON', 'TIME', 'TIMESTAMP', 'UUID']]


# SqlStatementResult

### resultFrame
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.ResultFrame]

### numberOfRecordsUpdated
- **Type**: typing.Optional[int]


# StructValue

### attributes
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# UpdateResult

### generatedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.FieldOutput]]


# Value

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rds_data.rds_data_classes.StructValue]


