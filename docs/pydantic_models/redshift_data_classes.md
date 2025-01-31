# redshift_data_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchExecuteStatementInputRequestTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Sqls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

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

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### WorkgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelStatementRequestRequestTypeDef

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


# DescribeStatementRequestRequestTypeDef

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

### ResultRows
- **Type**: <class 'int'>
- **Required**: Yes

### ResultSize
- **Type**: <class 'int'>
- **Required**: Yes

### SecretArn
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


# DescribeTableRequestDescribeTablePaginateTypeDef

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


# DescribeTableRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecuteStatementInputRequestTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Sql
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.redshift_data_classes.SqlParameterTypeDef]]

### SecretArn
- **Type**: typing.Optional[str]

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

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
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


# GetStatementResultRequestGetStatementResultPaginateTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# GetStatementResultRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultResponseTypeDef

### ColumnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.ColumnMetadataTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
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


# ListDatabasesRequestListDatabasesPaginateTypeDef

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


# ListDatabasesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchemasRequestListSchemasPaginateTypeDef

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


# ListSchemasRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Schemas
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStatementsRequestListStatementsPaginateTypeDef

### RoleLevel
- **Type**: typing.Optional[bool]

### StatementName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ALL', 'FAILED', 'FINISHED', 'PICKED', 'STARTED', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data_classes.PaginatorConfigTypeDef]


# ListStatementsRequestRequestTypeDef

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


# ListStatementsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.StatementDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTablesRequestListTablesPaginateTypeDef

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


# ListTablesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data_classes.TableMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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

### SecretArn
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

### name
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


