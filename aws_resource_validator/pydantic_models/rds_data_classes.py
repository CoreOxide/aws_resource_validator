from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class ArrayValueOutputTypeDef(BaseValidatorModel):
    booleanValues: Optional[List[bool]] = None
    longValues: Optional[List[int]] = None
    doubleValues: Optional[List[float]] = None
    stringValues: Optional[List[str]] = None
    arrayValues: Optional[List[Dict[str, Any]]] = None


class ArrayValueTypeDef(BaseValidatorModel):
    booleanValues: Optional[Sequence[bool]] = None
    longValues: Optional[Sequence[int]] = None
    doubleValues: Optional[Sequence[float]] = None
    stringValues: Optional[Sequence[str]] = None
    arrayValues: Optional[Sequence[Mapping[str, Any]]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BeginTransactionRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    database: Optional[str] = None
    schema: Optional[str] = None


class CommitTransactionRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    transactionId: str


class ExecuteSqlRequestTypeDef(BaseValidatorModel):
    dbClusterOrInstanceArn: str
    awsSecretStoreArn: str
    sqlStatements: str
    database: Optional[str] = None
    schema: Optional[str] = None


class ResultSetOptionsTypeDef(BaseValidatorModel):
    decimalReturnType: Optional[DecimalReturnTypeType] = None
    longReturnType: Optional[LongReturnTypeType] = None


class RollbackTransactionRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    transactionId: str


class StructValueTypeDef(BaseValidatorModel):
    attributes: Optional[List[Dict[str, Any]]] = None


class FieldOutputTypeDef(BaseValidatorModel):
    isNull: Optional[bool] = None
    booleanValue: Optional[bool] = None
    longValue: Optional[int] = None
    doubleValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[bytes] = None
    arrayValue: Optional[ArrayValueOutputTypeDef] = None


class BeginTransactionResponseTypeDef(BaseValidatorModel):
    transactionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CommitTransactionResponseTypeDef(BaseValidatorModel):
    transactionStatus: str
    ResponseMetadata: ResponseMetadataTypeDef


class RollbackTransactionResponseTypeDef(BaseValidatorModel):
    transactionStatus: str
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnMetadataTypeDef(BaseValidatorModel):
    pass


class ResultSetMetadataTypeDef(BaseValidatorModel):
    columnCount: Optional[int] = None
    columnMetadata: Optional[List[ColumnMetadataTypeDef]] = None


class ValueTypeDef(BaseValidatorModel):
    isNull: Optional[bool] = None
    bitValue: Optional[bool] = None
    bigIntValue: Optional[int] = None
    intValue: Optional[int] = None
    doubleValue: Optional[float] = None
    realValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[bytes] = None
    arrayValues: Optional[List[Dict[str, Any]]] = None
    structValue: Optional[StructValueTypeDef] = None


class ExecuteStatementResponseTypeDef(BaseValidatorModel):
    records: List[List[FieldOutputTypeDef]]
    columnMetadata: List[ColumnMetadataTypeDef]
    numberOfRecordsUpdated: int
    generatedFields: List[FieldOutputTypeDef]
    formattedRecords: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateResultTypeDef(BaseValidatorModel):
    generatedFields: Optional[List[FieldOutputTypeDef]] = None


class ArrayValueUnionTypeDef(BaseValidatorModel):
    pass


class BlobTypeDef(BaseValidatorModel):
    pass


class FieldTypeDef(BaseValidatorModel):
    isNull: Optional[bool] = None
    booleanValue: Optional[bool] = None
    longValue: Optional[int] = None
    doubleValue: Optional[float] = None
    stringValue: Optional[str] = None
    blobValue: Optional[BlobTypeDef] = None
    arrayValue: Optional[ArrayValueUnionTypeDef] = None


class RecordTypeDef(BaseValidatorModel):
    values: Optional[List[ValueTypeDef]] = None


class BatchExecuteStatementResponseTypeDef(BaseValidatorModel):
    updateResults: List[UpdateResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ResultFrameTypeDef(BaseValidatorModel):
    resultSetMetadata: Optional[ResultSetMetadataTypeDef] = None
    records: Optional[List[RecordTypeDef]] = None


class FieldUnionTypeDef(BaseValidatorModel):
    pass


class SqlParameterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[FieldUnionTypeDef] = None
    typeHint: Optional[TypeHintType] = None


class SqlStatementResultTypeDef(BaseValidatorModel):
    resultFrame: Optional[ResultFrameTypeDef] = None
    numberOfRecordsUpdated: Optional[int] = None


class BatchExecuteStatementRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    secretArn: str
    sql: str
    database: Optional[str] = None
    schema: Optional[str] = None
    parameterSets: Optional[Sequence[Sequence[SqlParameterTypeDef]]] = None
    transactionId: Optional[str] = None


class ExecuteStatementRequestTypeDef(BaseValidatorModel):
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


class ExecuteSqlResponseTypeDef(BaseValidatorModel):
    sqlStatementResults: List[SqlStatementResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


