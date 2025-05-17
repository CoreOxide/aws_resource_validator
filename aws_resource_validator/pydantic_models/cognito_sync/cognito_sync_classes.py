from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cognito_sync.cognito_sync_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'bulk_publish' function.
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


# This class is the input for the 'delete_dataset' function.
class DeleteDatasetRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str


# This class is the input for the 'describe_dataset' function.
class DescribeDatasetRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str


# This class is the input for the 'describe_identity_pool_usage' function.
class DescribeIdentityPoolUsageRequest(BaseValidatorModel):
    IdentityPoolId: str


class IdentityPoolUsage(BaseValidatorModel):
    IdentityPoolId: Optional[str] = None
    SyncSessionsCount: Optional[int] = None
    DataStorage: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None


# This class is the input for the 'describe_identity_usage' function.
class DescribeIdentityUsageRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str


class IdentityUsage(BaseValidatorModel):
    IdentityId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    DatasetCount: Optional[int] = None
    DataStorage: Optional[int] = None


# This class is the input for the 'get_bulk_publish_details' function.
class GetBulkPublishDetailsRequest(BaseValidatorModel):
    IdentityPoolId: str


# This class is the input for the 'get_cognito_events' function.
class GetCognitoEventsRequest(BaseValidatorModel):
    IdentityPoolId: str


# This class is the input for the 'get_identity_pool_configuration' function.
class GetIdentityPoolConfigurationRequest(BaseValidatorModel):
    IdentityPoolId: str


class PushSyncOutput(BaseValidatorModel):
    ApplicationArns: Optional[List[str]] = None
    RoleArn: Optional[str] = None


# This class is the input for the 'list_datasets' function.
class ListDatasetsRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_identity_pool_usage' function.
class ListIdentityPoolUsageRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_records' function.
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


# This class is the input for the 'register_device' function.
class RegisterDeviceRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    Platform: PlatformType
    Token: str


# This class is the input for the 'set_cognito_events' function.
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


# This class is the output for the 'bulk_publish' function.
class BulkPublishResponse(BaseValidatorModel):
    IdentityPoolId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_cognito_events' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bulk_publish_details' function.
class GetBulkPublishDetailsResponse(BaseValidatorModel):
    IdentityPoolId: str
    BulkPublishStartTime: datetime
    BulkPublishCompleteTime: datetime
    BulkPublishStatus: BulkPublishStatusType
    FailureMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cognito_events' function.
class GetCognitoEventsResponse(BaseValidatorModel):
    Events: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_device' function.
class RegisterDeviceResponse(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_dataset' function.
class DeleteDatasetResponse(BaseValidatorModel):
    Dataset: Dataset
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_dataset' function.
class DescribeDatasetResponse(BaseValidatorModel):
    Dataset: Dataset
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_datasets' function.
class ListDatasetsResponse(BaseValidatorModel):
    Datasets: List[Dataset]
    Count: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_identity_pool_usage' function.
class DescribeIdentityPoolUsageResponse(BaseValidatorModel):
    IdentityPoolUsage: IdentityPoolUsage
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_identity_pool_usage' function.
class ListIdentityPoolUsageResponse(BaseValidatorModel):
    IdentityPoolUsages: List[IdentityPoolUsage]
    MaxResults: int
    Count: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_identity_usage' function.
class DescribeIdentityUsageResponse(BaseValidatorModel):
    IdentityUsage: IdentityUsage
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_identity_pool_configuration' function.
class GetIdentityPoolConfigurationResponse(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncOutput
    CognitoStreams: CognitoStreams
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_identity_pool_configuration' function.
class SetIdentityPoolConfigurationResponse(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncOutput
    CognitoStreams: CognitoStreams
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_records' function.
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


# This class is the output for the 'update_records' function.
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


# This class is the input for the 'set_identity_pool_configuration' function.
class SetIdentityPoolConfigurationRequest(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: Optional[PushSyncUnion] = None
    CognitoStreams: Optional[CognitoStreams] = None


# This class is the input for the 'update_records' function.
class UpdateRecordsRequest(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    SyncSessionToken: str
    DeviceId: Optional[str] = None
    RecordPatches: Optional[List[RecordPatch]] = None
    ClientContext: Optional[str] = None