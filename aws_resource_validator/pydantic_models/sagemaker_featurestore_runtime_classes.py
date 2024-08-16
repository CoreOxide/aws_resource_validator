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
from aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_constants import *

class BatchGetRecordErrorTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    ErrorCode: str
    ErrorMessage: str

class BatchGetRecordIdentifierTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: Sequence[str]
    FeatureNames: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FeatureValueTypeDef(BaseValidatorModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[List[str]] = None

class DeleteRecordRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    EventTime: str
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    DeletionMode: Optional[DeletionModeType] = None

class GetRecordRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: Optional[Sequence[str]] = None
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None

class TtlDurationTypeDef(BaseValidatorModel):
    Unit: TtlDurationUnitType
    Value: int

class BatchGetRecordRequestRequestTypeDef(BaseValidatorModel):
    Identifiers: Sequence[BatchGetRecordIdentifierTypeDef]
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetRecordResultDetailTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: List[FeatureValueTypeDef]
    ExpiresAt: Optional[str] = None

class GetRecordResponseTypeDef(BaseValidatorModel):
    Record: List[FeatureValueTypeDef]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRecordRequestRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    Record: Sequence[FeatureValueTypeDef]
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    TtlDuration: Optional[TtlDurationTypeDef] = None

class BatchGetRecordResponseTypeDef(BaseValidatorModel):
    Records: List[BatchGetRecordResultDetailTypeDef]
    Errors: List[BatchGetRecordErrorTypeDef]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

