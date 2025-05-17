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


# This class is the input for the 'delete_record' function.
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


# This class is the input for the 'get_record' function.
class GetRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    FeatureNames: Optional[List[str]] = None
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


class TtlDuration(BaseValidatorModel):
    Unit: TtlDurationUnitType
    Value: int

BatchGetRecordIdentifierUnion = Union[BatchGetRecordIdentifier, BatchGetRecordIdentifierOutput]


# This class is the output for the 'put_record' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class BatchGetRecordResultDetail(BaseValidatorModel):
    FeatureGroupName: str
    RecordIdentifierValueAsString: str
    Record: List[FeatureValueOutput]
    ExpiresAt: Optional[str] = None


# This class is the output for the 'get_record' function.
class GetRecordResponse(BaseValidatorModel):
    Record: List[FeatureValueOutput]
    ExpiresAt: str
    ResponseMetadata: ResponseMetadata

FeatureValueUnion = Union[FeatureValue, FeatureValueOutput]


# This class is the input for the 'batch_get_record' function.
class BatchGetRecordRequest(BaseValidatorModel):
    Identifiers: List[BatchGetRecordIdentifierUnion]
    ExpirationTimeResponse: Optional[ExpirationTimeResponseType] = None


# This class is the output for the 'batch_get_record' function.
class BatchGetRecordResponse(BaseValidatorModel):
    Records: List[BatchGetRecordResultDetail]
    Errors: List[BatchGetRecordError]
    UnprocessedIdentifiers: List[BatchGetRecordIdentifierOutput]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_record' function.
class PutRecordRequest(BaseValidatorModel):
    FeatureGroupName: str
    Record: List[FeatureValueUnion]
    TargetStores: Optional[List[TargetStoreType]] = None
    TtlDuration: Optional[TtlDuration] = None