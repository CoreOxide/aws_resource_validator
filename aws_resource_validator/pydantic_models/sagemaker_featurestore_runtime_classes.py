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
from aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime_constants import *

class BatchGetRecordErrorTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    ErrorCode: str
    ErrorMessage: str


class BatchGetRecordIdentifierOutputTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: List[str]
    FeatureNames: Optional[List[str]] = None


class BatchGetRecordIdentifierTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: Sequence[str]
    FeatureNames: Optional[Sequence[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FeatureValueOutputTypeDef(BaseValidatorModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[List[str]] = None


class DeleteRecordRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    EventTime: str
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    DeletionMode: Optional[DeletionModeType] = None


class FeatureValueTypeDef(BaseValidatorModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[Sequence[str]] = None


class GetRecordRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: Optional[Sequence[str]] = None
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class TtlDurationTypeDef(BaseValidatorModel):
    Unit: TtlDurationUnitType
    Value: int


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetRecordResultDetailTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: List[FeatureValueOutputTypeDef]
    ExpiresAt: Optional[str] = None


class GetRecordResponseTypeDef(BaseValidatorModel):
    Record: List[FeatureValueOutputTypeDef]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetRecordIdentifierUnionTypeDef(BaseValidatorModel):
    pass


class BatchGetRecordRequestTypeDef(BaseValidatorModel):
    Identifiers: Sequence[BatchGetRecordIdentifierUnionTypeDef]
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class BatchGetRecordResponseTypeDef(BaseValidatorModel):
    Records: List[BatchGetRecordResultDetailTypeDef]
    Errors: List[BatchGetRecordErrorTypeDef]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FeatureValueUnionTypeDef(BaseValidatorModel):
    pass


class PutRecordRequestTypeDef(BaseValidatorModel):
    FeatureGroupName: str
    Record: Sequence[FeatureValueUnionTypeDef]
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    TtlDuration: Optional[TtlDurationTypeDef] = None


