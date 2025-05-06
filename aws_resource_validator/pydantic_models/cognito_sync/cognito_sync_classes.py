from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BulkPublishRequest(BaseValidatorModel):
    IdentityPoolId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CognitoStreams(BaseValidatorModel):
    StreamName: Optional[str] = None
    RoleArn: Optional[str] = None
    StreamingStatus: Optional[StreamingStatusType] = None


class Dataset(BaseValidatorModel):
    IdentityId: Optional[str] = None
    DatasetName: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    DataStorage: Optional[int] = None
    NumRecords: Optional[int] = None


class DeleteDatasetRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str


class DescribeDatasetRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str


class DescribeIdentityPoolUsageRequest(BaseValidatorModel):
    IdentityPoolId: str


class IdentityPoolUsage(BaseValidatorModel):
    IdentityPoolId: Optional[str] = None
    SyncSessionsCount: Optional[int] = None
    DataStorage: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None


class DescribeIdentityUsageRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str


class IdentityUsage(BaseValidatorModel):
    IdentityId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    DatasetCount: Optional[int] = None
    DataStorage: Optional[int] = None


class GetBulkPublishDetailsRequest(BaseValidatorModel):
    IdentityPoolId: str


class GetCognitoEventsRequest(BaseValidatorModel):
    IdentityPoolId: str


class GetIdentityPoolConfigurationRequest(BaseValidatorModel):
    IdentityPoolId: str


class PushSyncOutput(BaseValidatorModel):
    ApplicationArns: Optional[List[str]] = None
    RoleArn: Optional[str] = None


class ListDatasetsRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIdentityPoolUsageRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRecordsRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    LastSyncCount: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SyncSessionToken: Optional[str] = None


class Record(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    SyncCount: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    DeviceLastModifiedDate: Optional[datetime] = None


class PushSync(BaseValidatorModel):
    ApplicationArns: Optional[List[str]] = None
    RoleArn: Optional[str] = None

Timestamp = Union[datetime, str]


class RegisterDeviceRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    Platform: PlatformType
    Token: str


class SetCognitoEventsRequest(BaseValidatorModel):
    IdentityPoolId: str
    Events: Dict[str, str]


class SubscribeToDatasetRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str


class UnsubscribeFromDatasetRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str


class BulkPublishResponse(BaseValidatorModel):
    IdentityPoolId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetBulkPublishDetailsResponse(BaseValidatorModel):
    IdentityPoolId: str
    BulkPublishStartTime: datetime
    BulkPublishCompleteTime: datetime
    BulkPublishStatus: BulkPublishStatusType
    FailureMessage: str
    ResponseMetadata: ResponseMetadata


class GetCognitoEventsResponse(BaseValidatorModel):
    Events: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RegisterDeviceResponse(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadata


class DeleteDatasetResponse(BaseValidatorModel):
    Dataset: Dataset
    ResponseMetadata: ResponseMetadata


class DescribeDatasetResponse(BaseValidatorModel):
    Dataset: Dataset
    ResponseMetadata: ResponseMetadata


class ListDatasetsResponse(BaseValidatorModel):
    Datasets: List[Dataset]
    Count: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeIdentityPoolUsageResponse(BaseValidatorModel):
    IdentityPoolUsage: IdentityPoolUsage
    ResponseMetadata: ResponseMetadata


class ListIdentityPoolUsageResponse(BaseValidatorModel):
    IdentityPoolUsages: List[IdentityPoolUsage]
    MaxResults: int
    Count: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeIdentityUsageResponse(BaseValidatorModel):
    IdentityUsage: IdentityUsage
    ResponseMetadata: ResponseMetadata


class GetIdentityPoolConfigurationResponse(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncOutput
    CognitoStreams: CognitoStreams
    ResponseMetadata: ResponseMetadata


class SetIdentityPoolConfigurationResponse(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncOutput
    CognitoStreams: CognitoStreams
    ResponseMetadata: ResponseMetadata


class ListRecordsResponse(BaseValidatorModel):
    Records: List[Record]
    Count: int
    DatasetSyncCount: int
    LastModifiedBy: str
    MergedDatasetNames: List[str]
    DatasetExists: bool
    DatasetDeletedAfterRequestedSyncCount: bool
    SyncSessionToken: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateRecordsResponse(BaseValidatorModel):
    Records: List[Record]
    ResponseMetadata: ResponseMetadata

PushSyncUnion = Union[PushSync, PushSyncOutput]


class RecordPatch(BaseValidatorModel):
    Op: OperationType
    Key: str
    SyncCount: int
    Value: Optional[str] = None
    DeviceLastModifiedDate: Optional[Timestamp] = None


class SetIdentityPoolConfigurationRequest(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: Optional[PushSyncUnion] = None
    CognitoStreams: Optional[CognitoStreams] = None


class UpdateRecordsRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    SyncSessionToken: str
    DeviceId: Optional[str] = None
    RecordPatches: Optional[List[RecordPatch]] = None
    ClientContext: Optional[str] = None