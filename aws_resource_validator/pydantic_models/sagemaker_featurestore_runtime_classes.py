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

class BatchGetRecordError(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    ErrorCode: str
    ErrorMessage: str


class BatchGetRecordIdentifierOutput(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: List[str]
    FeatureNames: Optional[List[str]] = None


class BatchGetRecordIdentifier(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifiersValueAsString: Sequence[str]
    FeatureNames: Optional[Sequence[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FeatureValueOutput(BaseValidatorModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[List[str]] = None


class DeleteRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    EventTime: str
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    DeletionMode: Optional[DeletionModeType] = None


class FeatureValue(BaseValidatorModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[Sequence[str]] = None


class GetRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: Optional[Sequence[str]] = None
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class TtlDuration(BaseValidatorModel):
    Unit: TtlDurationUnitType
    Value: int


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class BatchGetRecordResultDetail(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: List[FeatureValueOutput]
    ExpiresAt: Optional[str] = None


class GetRecordResponse(BaseValidatorModel):
    Record: List[FeatureValueOutput]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadata


class BatchGetRecordIdentifierUnion(BaseValidatorModel):
    pass


class BatchGetRecordRequest(BaseValidatorModel):
    Identifiers: Sequence[BatchGetRecordIdentifierUnion]
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class BatchGetRecordResponse(BaseValidatorModel):
    Records: List[BatchGetRecordResultDetail]
    Errors: List[BatchGetRecordError]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierOutput]
    ResponseMetadata: ResponseMetadata


class FeatureValueUnion(BaseValidatorModel):
    pass


class PutRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    Record: Sequence[FeatureValueUnion]
    TargetStores: Optional[Sequence[TargetStoreType]] = None
    TtlDuration: Optional[TtlDuration] = None


