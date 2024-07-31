from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.redshift_data_constants import *

class BatchExecuteStatementInputRequestTypeDef(BaseModel):
    Database: str
    Sqls: Sequence[str]
    ClientToken: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    SecretArn: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    WorkgroupName: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelStatementRequestRequestTypeDef(BaseModel):
    Id: str

class ColumnMetadataTypeDef(BaseModel):
    columnDefault: Optional[str] = None
    isCaseSensitive: Optional[bool] = None
    isCurrency: Optional[bool] = None
    isSigned: Optional[bool] = None
    label: Optional[str] = None
    length: Optional[int] = None
    name: Optional[str] = None
    nullable: Optional[int] = None
    precision: Optional[int] = None
    scale: Optional[int] = None
    schemaName: Optional[str] = None
    tableName: Optional[str] = None
    typeName: Optional[str] = None

class DescribeStatementRequestRequestTypeDef(BaseModel):
    Id: str

class SqlParameterTypeDef(BaseModel):
    name: str
    value: str

class SubStatementDataTypeDef(BaseModel):
    Id: str
    CreatedAt: Optional[datetime] = None
    Duration: Optional[int] = None
    Error: Optional[str] = None
    HasResultSet: Optional[bool] = None
    QueryString: Optional[str] = None
    RedshiftQueryId: Optional[int] = None
    ResultRows: Optional[int] = None
    ResultSize: Optional[int] = None
    Status: Optional[StatementStatusStringType] = None
    UpdatedAt: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeTableRequestRequestTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Schema: Optional[str] = None
    SecretArn: Optional[str] = None
    Table: Optional[str] = None
    WorkgroupName: Optional[str] = None

class FieldTypeDef(BaseModel):
    blobValue: Optional[bytes] = None
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    isNull: Optional[bool] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None

class GetStatementResultRequestRequestTypeDef(BaseModel):
    Id: str
    NextToken: Optional[str] = None

class ListDatabasesRequestRequestTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None

class ListSchemasRequestRequestTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None

class ListStatementsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RoleLevel: Optional[bool] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None

class ListTablesRequestRequestTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    TablePattern: Optional[str] = None
    WorkgroupName: Optional[str] = None

class TableMemberTypeDef(BaseModel):
    name: Optional[str] = None
    schema: Optional[str] = None
    type: Optional[str] = None

class BatchExecuteStatementOutputTypeDef(BaseModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Id: str
    SecretArn: str
    WorkgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelStatementResponseTypeDef(BaseModel):
    Status: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteStatementOutputTypeDef(BaseModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Id: str
    SecretArn: str
    WorkgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesResponseTypeDef(BaseModel):
    Databases: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasResponseTypeDef(BaseModel):
    NextToken: str
    Schemas: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableResponseTypeDef(BaseModel):
    ColumnList: List[ColumnMetadataTypeDef]
    NextToken: str
    TableName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteStatementInputRequestTypeDef(BaseModel):
    Database: str
    Sql: str
    ClientToken: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    Parameters: Optional[Sequence[SqlParameterTypeDef]] = None
    SecretArn: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    WorkgroupName: Optional[str] = None

class StatementDataTypeDef(BaseModel):
    Id: str
    CreatedAt: Optional[datetime] = None
    IsBatchStatement: Optional[bool] = None
    QueryParameters: Optional[List[SqlParameterTypeDef]] = None
    QueryString: Optional[str] = None
    QueryStrings: Optional[List[str]] = None
    SecretArn: Optional[str] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None
    UpdatedAt: Optional[datetime] = None

class DescribeStatementResponseTypeDef(BaseModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Duration: int
    Error: str
    HasResultSet: bool
    Id: str
    QueryParameters: List[SqlParameterTypeDef]
    QueryString: str
    RedshiftPid: int
    RedshiftQueryId: int
    ResultRows: int
    ResultSize: int
    SecretArn: str
    Status: StatusStringType
    SubStatements: List[SubStatementDataTypeDef]
    UpdatedAt: datetime
    WorkgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableRequestDescribeTablePaginateTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    Schema: Optional[str] = None
    SecretArn: Optional[str] = None
    Table: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStatementResultRequestGetStatementResultPaginateTypeDef(BaseModel):
    Id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatabasesRequestListDatabasesPaginateTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasRequestListSchemasPaginateTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStatementsRequestListStatementsPaginateTypeDef(BaseModel):
    RoleLevel: Optional[bool] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesRequestListTablesPaginateTypeDef(BaseModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    TablePattern: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStatementResultResponseTypeDef(BaseModel):
    ColumnMetadata: List[ColumnMetadataTypeDef]
    NextToken: str
    Records: List[List[FieldTypeDef]]
    TotalNumRows: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesResponseTypeDef(BaseModel):
    NextToken: str
    Tables: List[TableMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStatementsResponseTypeDef(BaseModel):
    NextToken: str
    Statements: List[StatementDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

