# Redshift Data Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchExecuteStatementInput

### Sqls
- **Type**: typing.List[str]
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


# BatchExecuteStatementOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes


# CancelStatementRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CancelStatementResponse

### Status
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes


# ColumnMetadata

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


# DescribeStatementRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStatementResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.SqlParameter]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.SubStatementData]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### WorkgroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTableRequest

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


# DescribeTableRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# DescribeTableResponse

### ColumnList
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ColumnMetadata]
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExecuteStatementInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.SqlParameter]]

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


# ExecuteStatementOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes


# Field

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


# GetStatementResultRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultRequestPaginate

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# GetStatementResultResponse

### ColumnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ColumnMetadata]
- **Required**: Yes

### Records
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.Field]]
- **Required**: Yes

### TotalNumRows
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultV2Request

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetStatementResultV2RequestPaginate

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# GetStatementResultV2Response

### ColumnMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ColumnMetadata]
- **Required**: Yes

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.QueryRecords]
- **Required**: Yes

### ResultFormat
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### TotalNumRows
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesRequest

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


# ListDatabasesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# ListDatabasesResponse

### Databases
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemasRequest

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


# ListSchemasRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# ListSchemasResponse

### Schemas
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStatementsRequest

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


# ListStatementsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# ListStatementsResponse

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.StatementData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTablesRequest

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


# ListTablesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.PaginatorConfig]


# ListTablesResponse

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.TableMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QueryRecords

### CSVRecords
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


# SqlParameter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# StatementData

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### IsBatchStatement
- **Type**: typing.Optional[bool]

### QueryParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.redshift_data.redshift_data_classes.SqlParameter]]

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


# SubStatementData

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


# TableMember

### name
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


