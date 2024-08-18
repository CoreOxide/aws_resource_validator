from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class BatchExecuteStatementInputRequestTypeDef(BaseValidatorModel):
    Database: str
    Sqls: Sequence[str]
    ClientToken: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    SecretArn: Optional[str] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    WorkgroupName: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelStatementRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class ColumnMetadataTypeDef(BaseValidatorModel):
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

class DescribeStatementRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class SqlParameterTypeDef(BaseValidatorModel):
    name: str
    value: str

class SubStatementDataTypeDef(BaseValidatorModel):
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

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeTableRequestRequestTypeDef(BaseValidatorModel):
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

class FieldTypeDef(BaseValidatorModel):
    blobValue: Optional[bytes] = None
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    isNull: Optional[bool] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None

class GetStatementResultRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None

class ListDatabasesRequestRequestTypeDef(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None

class ListSchemasRequestRequestTypeDef(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None

class ListStatementsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RoleLevel: Optional[bool] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None

class ListTablesRequestRequestTypeDef(BaseValidatorModel):
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

class TableMemberTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    schema: Optional[str] = None
    type: Optional[str] = None

class BatchExecuteStatementOutputTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Id: str
    SecretArn: str
    WorkgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelStatementResponseTypeDef(BaseValidatorModel):
    Status: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteStatementOutputTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Id: str
    SecretArn: str
    WorkgroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatabasesResponseTypeDef(BaseValidatorModel):
    Databases: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Schemas: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableResponseTypeDef(BaseValidatorModel):
    ColumnList: List[ColumnMetadataTypeDef]
    NextToken: str
    TableName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteStatementInputRequestTypeDef(BaseValidatorModel):
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

class StatementDataTypeDef(BaseValidatorModel):
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

class DescribeStatementResponseTypeDef(BaseValidatorModel):
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

class DescribeTableRequestDescribeTablePaginateTypeDef(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    Schema: Optional[str] = None
    SecretArn: Optional[str] = None
    Table: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStatementResultRequestGetStatementResultPaginateTypeDef(BaseValidatorModel):
    Id: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatabasesRequestListDatabasesPaginateTypeDef(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasRequestListSchemasPaginateTypeDef(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStatementsRequestListStatementsPaginateTypeDef(BaseValidatorModel):
    RoleLevel: Optional[bool] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesRequestListTablesPaginateTypeDef(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    TablePattern: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStatementResultResponseTypeDef(BaseValidatorModel):
    ColumnMetadata: List[ColumnMetadataTypeDef]
    NextToken: str
    Records: List[List[FieldTypeDef]]
    TotalNumRows: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Tables: List[TableMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStatementsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Statements: List[StatementDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

