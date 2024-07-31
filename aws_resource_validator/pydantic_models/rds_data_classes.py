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
from aws_resource_validator.pydantic_models.rds_data_constants import *

class ArrayValueTypeDef(BaseModel):
    booleanValues: Optional[Sequence[bool]] = None
    longValues: Optional[Sequence[int]] = None
    doubleValues: Optional[Sequence[float]] = None
    stringValues: Optional[Sequence[str]] = None
    arrayValues: Optional[Sequence[Dict[str, Any]]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BeginTransactionRequestRequestTypeDef(BaseModel):
    resourceArn: str
    secretArn: str
    database: Optional[str] = None
    schema: Optional[str] = None

class ColumnMetadataTypeDef(BaseModel):
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

class CommitTransactionRequestRequestTypeDef(BaseModel):
    resourceArn: str
    secretArn: str
    transactionId: str

class ExecuteSqlRequestRequestTypeDef(BaseModel):
    dbClusterOrInstanceArn: str
    awsSecretStoreArn: str
    sqlStatements: str
    database: Optional[str] = None
    schema: Optional[str] = None

class ResultSetOptionsTypeDef(BaseModel):
    decimalReturnType: Optional[DecimalReturnTypeType] = None
    longReturnType: Optional[LongReturnTypeType] = None

class RecordTypeDef(BaseModel):
    values: Optional[List["ValueTypeDef"]] = None

class RollbackTransactionRequestRequestTypeDef(BaseModel):
    resourceArn: str
    secretArn: str
    transactionId: str

class StructValueTypeDef(BaseModel):
    attributes: Optional[List["ValueTypeDef"]] = None

class ValueTypeDef(BaseModel):
    isNull: Optional[bool] = None
    bitValue: Optional[bool] = None
    bigIntValue: Optional[int] = None
    intValue: Optional[int] = None
    doubleValue: Optional[float] = None
    realValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[bytes] = None
    arrayValues: Optional[List[Dict[str, Any]]] = None
    structValue: Optional[Dict[str, Any]] = None

class BeginTransactionResponseTypeDef(BaseModel):
    transactionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CommitTransactionResponseTypeDef(BaseModel):
    transactionStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackTransactionResponseTypeDef(BaseModel):
    transactionStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class FieldTypeDef(BaseModel):
    isNull: Optional[bool] = None
    booleanValue: Optional[bool] = None
    longValue: Optional[int] = None
    doubleValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[BlobTypeDef] = None
    arrayValue: Optional["ArrayValueTypeDef"] = None

class ResultSetMetadataTypeDef(BaseModel):
    columnCount: Optional[int] = None
    columnMetadata: Optional[List[ColumnMetadataTypeDef]] = None

class ExecuteStatementResponseTypeDef(BaseModel):
    records: List[List[FieldTypeDef]]
    columnMetadata: List[ColumnMetadataTypeDef]
    numberOfRecordsUpdated: int
    generatedFields: List[FieldTypeDef]
    formattedRecords: str
    ResponseMetadata: ResponseMetadataTypeDef

class SqlParameterTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[FieldTypeDef] = None
    typeHint: Optional[TypeHintType] = None

class UpdateResultTypeDef(BaseModel):
    generatedFields: Optional[List[FieldTypeDef]] = None

class ResultFrameTypeDef(BaseModel):
    resultSetMetadata: Optional[ResultSetMetadataTypeDef] = None
    records: Optional[List[RecordTypeDef]] = None

class BatchExecuteStatementRequestRequestTypeDef(BaseModel):
    resourceArn: str
    secretArn: str
    sql: str
    database: Optional[str] = None
    schema: Optional[str] = None
    parameterSets: Optional[Sequence[Sequence[SqlParameterTypeDef]]] = None
    transactionId: Optional[str] = None

class ExecuteStatementRequestRequestTypeDef(BaseModel):
    resourceArn: str
    secretArn: str
    sql: str
    database: Optional[str] = None
    schema: Optional[str] = None
    parameters: Optional[Sequence[SqlParameterTypeDef]] = None
    transactionId: Optional[str] = None
    includeResultMetadata: Optional[bool] = None
    continueAfterTimeout: Optional[bool] = None
    resultSetOptions: Optional[ResultSetOptionsTypeDef] = None
    formatRecordsAs: Optional[RecordsFormatTypeType] = None

class BatchExecuteStatementResponseTypeDef(BaseModel):
    updateResults: List[UpdateResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SqlStatementResultTypeDef(BaseModel):
    resultFrame: Optional[ResultFrameTypeDef] = None
    numberOfRecordsUpdated: Optional[int] = None

class ExecuteSqlResponseTypeDef(BaseModel):
    sqlStatementResults: List[SqlStatementResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

