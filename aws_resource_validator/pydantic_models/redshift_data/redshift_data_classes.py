from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.redshift_data.redshift_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BatchExecuteStatementInput(BaseValidatorModel):
    Sqls: List[str]
    ClientToken: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    Database: Optional[str] = None
    DbUser: Optional[str] = None
    ResultFormat: Optional[ResultFormatStringType] = None
    SecretArn: Optional[str] = None
    SessionId: Optional[str] = None
    SessionKeepAliveSeconds: Optional[int] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    WorkgroupName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelStatementRequest(BaseValidatorModel):
    Id: str


class ColumnMetadata(BaseValidatorModel):
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


class DescribeStatementRequest(BaseValidatorModel):
    Id: str


class SqlParameter(BaseValidatorModel):
    name: str
    value: str


class SubStatementData(BaseValidatorModel):
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


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeTableRequest(BaseValidatorModel):
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


class Field(BaseValidatorModel):
    blobValue: Optional[bytes] = None
    booleanValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    isNull: Optional[bool] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None


class GetStatementResultRequest(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None


class GetStatementResultV2Request(BaseValidatorModel):
    Id: str
    NextToken: Optional[str] = None


class QueryRecords(BaseValidatorModel):
    CSVRecords: Optional[str] = None


class ListDatabasesRequest(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None


class ListSchemasRequest(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None


class ListStatementsRequest(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Database: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RoleLevel: Optional[bool] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None
    WorkgroupName: Optional[str] = None


class ListTablesRequest(BaseValidatorModel):
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


class TableMember(BaseValidatorModel):
    name: Optional[str] = None
    schema: Optional[str] = None
    type: Optional[str] = None


class BatchExecuteStatementOutput(BaseValidatorModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbGroups: List[str]
    DbUser: str
    Id: str
    SecretArn: str
    SessionId: str
    WorkgroupName: str
    ResponseMetadata: ResponseMetadata


class CancelStatementResponse(BaseValidatorModel):
    Status: bool
    ResponseMetadata: ResponseMetadata


class ExecuteStatementOutput(BaseValidatorModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbGroups: List[str]
    DbUser: str
    Id: str
    SecretArn: str
    SessionId: str
    WorkgroupName: str
    ResponseMetadata: ResponseMetadata


class ListDatabasesResponse(BaseValidatorModel):
    Databases: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchemasResponse(BaseValidatorModel):
    Schemas: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeTableResponse(BaseValidatorModel):
    ColumnList: List[ColumnMetadata]
    TableName: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExecuteStatementInput(BaseValidatorModel):
    Sql: str
    ClientToken: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    Database: Optional[str] = None
    DbUser: Optional[str] = None
    Parameters: Optional[List[SqlParameter]] = None
    ResultFormat: Optional[ResultFormatStringType] = None
    SecretArn: Optional[str] = None
    SessionId: Optional[str] = None
    SessionKeepAliveSeconds: Optional[int] = None
    StatementName: Optional[str] = None
    WithEvent: Optional[bool] = None
    WorkgroupName: Optional[str] = None


class StatementData(BaseValidatorModel):
    Id: str
    CreatedAt: Optional[datetime] = None
    IsBatchStatement: Optional[bool] = None
    QueryParameters: Optional[List[SqlParameter]] = None
    QueryString: Optional[str] = None
    QueryStrings: Optional[List[str]] = None
    ResultFormat: Optional[ResultFormatStringType] = None
    SecretArn: Optional[str] = None
    SessionId: Optional[str] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None
    UpdatedAt: Optional[datetime] = None


class DescribeStatementResponse(BaseValidatorModel):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Duration: int
    Error: str
    HasResultSet: bool
    Id: str
    QueryParameters: List[SqlParameter]
    QueryString: str
    RedshiftPid: int
    RedshiftQueryId: int
    ResultFormat: ResultFormatStringType
    ResultRows: int
    ResultSize: int
    SecretArn: str
    SessionId: str
    Status: StatusStringType
    SubStatements: List[SubStatementData]
    UpdatedAt: datetime
    WorkgroupName: str
    ResponseMetadata: ResponseMetadata


class DescribeTableRequestPaginate(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    Schema: Optional[str] = None
    SecretArn: Optional[str] = None
    Table: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetStatementResultRequestPaginate(BaseValidatorModel):
    Id: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetStatementResultV2RequestPaginate(BaseValidatorModel):
    Id: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatabasesRequestPaginate(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    DbUser: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemasRequestPaginate(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStatementsRequestPaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Database: Optional[str] = None
    RoleLevel: Optional[bool] = None
    StatementName: Optional[str] = None
    Status: Optional[StatusStringType] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTablesRequestPaginate(BaseValidatorModel):
    Database: str
    ClusterIdentifier: Optional[str] = None
    ConnectedDatabase: Optional[str] = None
    DbUser: Optional[str] = None
    SchemaPattern: Optional[str] = None
    SecretArn: Optional[str] = None
    TablePattern: Optional[str] = None
    WorkgroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetStatementResultResponse(BaseValidatorModel):
    ColumnMetadata: List[ColumnMetadata]
    Records: List[List[Field]]
    TotalNumRows: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetStatementResultV2Response(BaseValidatorModel):
    ColumnMetadata: List[ColumnMetadata]
    Records: List[QueryRecords]
    ResultFormat: ResultFormatStringType
    TotalNumRows: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTablesResponse(BaseValidatorModel):
    Tables: List[TableMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStatementsResponse(BaseValidatorModel):
    Statements: List[StatementData]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None