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
from aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_constants import *

class BatchGetRecordErrorTypeDef(BaseModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    ErrorCode: str
    ErrorMessage: str

class BatchGetRecordIdentifierTypeDef(BaseModel):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: Sequence[str]
    FeatureNames: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FeatureValueTypeDef(BaseModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[List[str]] = None

class DeleteRecordRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    EventTime: str
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    DeletionMode: Optional[DeletionModeType] = None

class GetRecordRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: Optional[Sequence[str]] = None
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None

class TtlDurationTypeDef(BaseModel):
    Unit: TtlDurationUnitType
    Value: int

class BatchGetRecordRequestRequestTypeDef(BaseModel):
    Identifiers: Sequence[BatchGetRecordIdentifierTypeDef]
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRecordResultDetailTypeDef(BaseModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: List[FeatureValueTypeDef]
    ExpiresAt: Optional[str] = None

class GetRecordResponseTypeDef(BaseModel):
    Record: List[FeatureValueTypeDef]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordRequestRequestTypeDef(BaseModel):
    FeatureGroupName: str
    Record: Sequence[FeatureValueTypeDef]
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    TtlDuration: Optional[TtlDurationTypeDef] = None

class BatchGetRecordResponseTypeDef(BaseModel):
    Records: List[BatchGetRecordResultDetailTypeDef]
    Errors: List[BatchGetRecordErrorTypeDef]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

