# Redshift Data Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchExecuteStatementInputTypeDef

### Sqls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### ResultFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON']]

### SecretArn
- **Type**: typing.Optional[str]

### SessionId
- **Type**: typing.Optional[str]

### SessionKeepAliveSeconds
- **Type**: typing.Optional[int]

### StatementName
- **Type**: typing.Optional[str]

### WithEvent
- **Type**: typing.Optional[bool]

### WorkgroupName
- **Type**: typing.Optional[str]


# BatchExecuteStatementOutputTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### DbGroups
- **Type**: typing.List[str]
- **Required**: Yes

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelStatementRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CancelStatementResponseTypeDef

### Status
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ColumnMetadataTypeDef

### columnDefault
- **Type**: typing.Optional[str]

### isCaseSensitive
- **Type**: typing.Optional[bool]

### isCurrency
- **Type**: typing.Optional[bool]

### isSigned
- **Type**: typing.Optional[bool]

### label
- **Type**: typing.Optional[str]

### length
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nullable
- **Type**: typing.Optional[int]

### precision
- **Type**: typing.Optional[int]

### scale
- **Type**: typing.Optional[int]

### schemaName
- **Type**: typing.Optional[str]

### tableName
- **Type**: typing.Optional[str]

### typeName
- **Type**: typing.Optional[str]


# DescribeStatementRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStatementResponseTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### HasResultSet
- **Type**: <class 'bool'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### QueryParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.SqlParameterTypeDef]
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### RedshiftPid
- **Type**: <class 'int'>
- **Required**: Yes

### RedshiftQueryId
- **Type**: <class 'int'>
- **Required**: Yes

### ResultFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### ResultRows
- **Type**: <class 'int'>
- **Required**: Yes

### ResultSize
- **Type**: <class 'int'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ABORTED', 'ALL', 'FAILED', 'FINISHED', 'PICKED', 'STARTED', 'SUBMITTED']
- **Required**: Yes

### SubStatements
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.SubStatementDataTypeDef]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### WorkgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTableRequestPaginateTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ConnectedDatabase
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# DescribeTableRequestTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ConnectedDatabase
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]


# DescribeTableResponseTypeDef

### ColumnList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.ColumnMetadataTypeDef]
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExecuteStatementInputTypeDef

### Sql
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_data_classes.SqlParameterTypeDef]]

### ResultFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON']]

### SecretArn
- **Type**: typing.Optional[str]

### SessionId
- **Type**: typing.Optional[str]

### SessionKeepAliveSeconds
- **Type**: typing.Optional[int]

### StatementName
- **Type**: typing.Optional[str]

### WithEvent
- **Type**: typing.Optional[bool]

### WorkgroupName
- **Type**: typing.Optional[str]


# ExecuteStatementOutputTypeDef

### ClusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### DbGroups
- **Type**: typing.List[str]
- **Required**: Yes

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FieldTypeDef

### blobValue
- **Type**: typing.Optional[bytes]

### booleanValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### isNull
- **Type**: typing.Optional[bool]

### longValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]


# GetStatementResultRequestPaginateTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# GetStatementResultRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultResponseTypeDef

### ColumnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.ColumnMetadataTypeDef]
- **Required**: Yes

### Records
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.FieldTypeDef]]
- **Required**: Yes

### TotalNumRows
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultV2RequestPaginateTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# GetStatementResultV2RequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultV2ResponseTypeDef

### ColumnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.ColumnMetadataTypeDef]
- **Required**: Yes

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.QueryRecordsTypeDef]
- **Required**: Yes

### ResultFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### TotalNumRows
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesRequestPaginateTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# ListDatabasesRequestTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]


# ListDatabasesResponseTypeDef

### Databases
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasRequestPaginateTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ConnectedDatabase
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### SchemaPattern
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# ListSchemasRequestTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ConnectedDatabase
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SchemaPattern
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]


# ListSchemasResponseTypeDef

### Schemas
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStatementsRequestPaginateTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### RoleLevel
- **Type**: typing.Optional[bool]

### StatementName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ALL', 'FAILED', 'FINISHED', 'PICKED', 'STARTED', 'SUBMITTED']]

### WorkgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# ListStatementsRequestTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### Database
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RoleLevel
- **Type**: typing.Optional[bool]

### StatementName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ALL', 'FAILED', 'FINISHED', 'PICKED', 'STARTED', 'SUBMITTED']]

### WorkgroupName
- **Type**: typing.Optional[str]


# ListStatementsResponseTypeDef

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.StatementDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTablesRequestPaginateTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ConnectedDatabase
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### SchemaPattern
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### TablePattern
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# ListTablesRequestTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterIdentifier
- **Type**: typing.Optional[str]

### ConnectedDatabase
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SchemaPattern
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### TablePattern
- **Type**: typing.Optional[str]

### WorkgroupName
- **Type**: typing.Optional[str]


# ListTablesResponseTypeDef

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.TableMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QueryRecordsTypeDef

### CSVRecords
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


# SqlParameterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# StatementDataTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### IsBatchStatement
- **Type**: typing.Optional[bool]

### QueryParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.SqlParameterTypeDef]]

### QueryString
- **Type**: typing.Optional[str]

### QueryStrings
- **Type**: typing.Optional[typing.List[str]]

### ResultFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON']]

### SecretArn
- **Type**: typing.Optional[str]

### SessionId
- **Type**: typing.Optional[str]

### StatementName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ALL', 'FAILED', 'FINISHED', 'PICKED', 'STARTED', 'SUBMITTED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# SubStatementDataTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[int]

### Error
- **Type**: typing.Optional[str]

### HasResultSet
- **Type**: typing.Optional[bool]

### QueryString
- **Type**: typing.Optional[str]

### RedshiftQueryId
- **Type**: typing.Optional[int]

### ResultRows
- **Type**: typing.Optional[int]

### ResultSize
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'FINISHED', 'PICKED', 'STARTED', 'SUBMITTED']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TableMemberTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

