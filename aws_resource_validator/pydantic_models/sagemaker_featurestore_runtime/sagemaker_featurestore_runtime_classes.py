from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sagemaker_featurestore_runtime.sagemaker_featurestore_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    RecordIdentifiersValueAsString: List[str]
    FeatureNames: Optional[List[str]] = None


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
    TargetStores: Optional[List[TargetStoreType]] = None
    DeletionMode: Optional[DeletionModeType] = None


class FeatureValue(BaseValidatorModel):
    FeatureName: str
    ValueAsString: Optional[str] = None
    ValueAsStringList: Optional[List[str]] = None


class GetRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: Optional[List[str]] = None
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class TtlDuration(BaseValidatorModel):
    Unit: TtlDurationUnitType
    Value: int

BatchGetRecordIdentifierUnion = Union[BatchGetRecordIdentifier, BatchGetRecordIdentifierOutput]


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

FeatureValueUnion = Union[FeatureValue, FeatureValueOutput]


class BatchGetRecordRequest(BaseValidatorModel):
    Identifiers: List[BatchGetRecordIdentifierUnion]
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class BatchGetRecordResponse(BaseValidatorModel):
    Records: List[BatchGetRecordResultDetail]
    Errors: List[BatchGetRecordError]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierOutput]
    ResponseMetadata: ResponseMetadata


class PutRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    Record: List[FeatureValueUnion]
    TargetStores: Optional[List[TargetStoreType]] = None
    TtlDuration: Optional[TtlDuration] = None