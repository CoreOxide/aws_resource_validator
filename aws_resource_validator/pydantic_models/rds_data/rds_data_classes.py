from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.rds_data.rds_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ArrayValueOutput(BaseValidatorModel):
    booleanValues: Optional[List[bool]] = None
    longValues: Optional[List[int]] = None
    doubleValues: Optional[List[float]] = None
    stringValues: Optional[List[str]] = None
    arrayValues: Optional[List[Dict[str, Any]]] = None


class ArrayValue(BaseValidatorModel):
    booleanValues: Optional[List[bool]] = None
    longValues: Optional[List[int]] = None
    doubleValues: Optional[List[float]] = None
    stringValues: Optional[List[str]] = None
    arrayValues: Optional[List[Dict[str, Any]]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BeginTransactionRequest(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    database: Optional[str] = None
    schema: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ColumnMetadata(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[int] = None
    typeName: Optional[str] = None
    label: Optional[str] = None
    schemaName: Optional[str] = None
    tableName: Optional[str] = None
    isAutoIncrement: Optional[bool] = None
    isSigned: Optional[bool] = None
    isCurrency: Optional[bool] = None
    isCaseSensitive: Optional[bool] = None
    nullable: Optional[int] = None
    precision: Optional[int] = None
    scale: Optional[int] = None
    arrayBaseColumnType: Optional[int] = None


class CommitTransactionRequest(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    transactionId: str


class ExecuteSqlRequest(BaseValidatorModel):
    dbClusterOrInstanceArn: str
    awsSecretStoreArn: str
    sqlStatements: str
    database: Optional[str] = None
    schema: Optional[str] = None


class ResultSetOptions(BaseValidatorModel):
    decimalReturnType: Optional[DecimalReturnTypeType] = None
    longReturnType: Optional[LongReturnTypeType] = None


class RollbackTransactionRequest(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    transactionId: str


class StructValue(BaseValidatorModel):
    attributes: Optional[List[Dict[str, Any]]] = None


class FieldOutput(BaseValidatorModel):
    isNull: Optional[bool] = None
    booleanValue: Optional[bool] = None
    longValue: Optional[int] = None
    doubleValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[bytes] = None
    arrayValue: Optional[ArrayValueOutput] = None

ArrayValueUnion = Union[ArrayValue, ArrayValueOutput]


class BeginTransactionResponse(BaseValidatorModel):
    transactionId: str
    ResponseMetadata: ResponseMetadata


class CommitTransactionResponse(BaseValidatorModel):
    transactionStatus: str
    ResponseMetadata: ResponseMetadata


class RollbackTransactionResponse(BaseValidatorModel):
    transactionStatus: str
    ResponseMetadata: ResponseMetadata


class ResultSetMetadata(BaseValidatorModel):
    columnCount: Optional[int] = None
    columnMetadata: Optional[List[ColumnMetadata]] = None


class Value(BaseValidatorModel):
    isNull: Optional[bool] = None
    bitValue: Optional[bool] = None
    bigIntValue: Optional[int] = None
    intValue: Optional[int] = None
    doubleValue: Optional[float] = None
    realValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[bytes] = None
    arrayValues: Optional[List[Dict[str, Any]]] = None
    structValue: Optional[StructValue] = None


class ExecuteStatementResponse(BaseValidatorModel):
    records: List[List[FieldOutput]]
    columnMetadata: List[ColumnMetadata]
    numberOfRecordsUpdated: int
    generatedFields: List[FieldOutput]
    formattedRecords: str
    ResponseMetadata: ResponseMetadata


class UpdateResult(BaseValidatorModel):
    generatedFields: Optional[List[FieldOutput]] = None


class Field(BaseValidatorModel):
    isNull: Optional[bool] = None
    booleanValue: Optional[bool] = None
    longValue: Optional[int] = None
    doubleValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[Blob] = None
    arrayValue: Optional[ArrayValueUnion] = None


class Record(BaseValidatorModel):
    values: Optional[List[Value]] = None


class BatchExecuteStatementResponse(BaseValidatorModel):
    updateResults: List[UpdateResult]
    ResponseMetadata: ResponseMetadata

FieldUnion = Union[Field, FieldOutput]


class ResultFrame(BaseValidatorModel):
    resultSetMetadata: Optional[ResultSetMetadata] = None
    records: Optional[List[Record]] = None


class SqlParameter(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[FieldUnion] = None
    typeHint: Optional[TypeHintType] = None


class SqlStatementResult(BaseValidatorModel):
    resultFrame: Optional[ResultFrame] = None
    numberOfRecordsUpdated: Optional[int] = None


class BatchExecuteStatementRequest(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    sql: str
    database: Optional[str] = None
    schema: Optional[str] = None
    parameterSets: Optional[List[List[SqlParameter]]] = None
    transactionId: Optional[str] = None


class ExecuteStatementRequest(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    sql: str
    database: Optional[str] = None
    schema: Optional[str] = None
    parameters: Optional[List[SqlParameter]] = None
    transactionId: Optional[str] = None
    includeResultMetadata: Optional[bool] = None
    continueAfterTimeout: Optional[bool] = None
    resultSetOptions: Optional[ResultSetOptions] = None
    formatRecordsAs: Optional[RecordsFormatTypeType] = None


class ExecuteSqlResponse(BaseValidatorModel):
    sqlStatementResults: List[SqlStatementResult]
    ResponseMetadata: ResponseMetadata