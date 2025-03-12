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
from aws_resource_validator.pydantic_models.cognito_sync_constants import *

class BulkPublishRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CognitoStreamsTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    RoleArn: Optional[str] = None
    StreamingStatus: Optional[StreamingStatusType] = None


class DatasetTypeDef(BaseValidatorModel):
    IdentityId: Optional[str] = None
    DatasetName: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    DataStorage: Optional[int] = None
    NumRecords: Optional[int] = None


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str


class DescribeIdentityPoolUsageRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class IdentityPoolUsageTypeDef(BaseValidatorModel):
    IdentityPoolId: Optional[str] = None
    SyncSessionsCount: Optional[int] = None
    DataStorage: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None


class DescribeIdentityUsageRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str


class IdentityUsageTypeDef(BaseValidatorModel):
    IdentityId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    DatasetCount: Optional[int] = None
    DataStorage: Optional[int] = None


class GetBulkPublishDetailsRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class GetCognitoEventsRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class GetIdentityPoolConfigurationRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str


class PushSyncOutputTypeDef(BaseValidatorModel):
    ApplicationArns: Optional[List[str]] = None
    RoleArn: Optional[str] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIdentityPoolUsageRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRecordsRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    LastSyncCount: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SyncSessionToken: Optional[str] = None


class RecordTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    SyncCount: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    DeviceLastModifiedDate: Optional[datetime] = None


class PushSyncTypeDef(BaseValidatorModel):
    ApplicationArns: Optional[Sequence[str]] = None
    RoleArn: Optional[str] = None


class RegisterDeviceRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    Platform: PlatformType
    Token: str


class SetCognitoEventsRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Events: Mapping[str, str]


class SubscribeToDatasetRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str


class UnsubscribeFromDatasetRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str


class BulkPublishResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetBulkPublishDetailsResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    BulkPublishStartTime: datetime
    BulkPublishCompleteTime: datetime
    BulkPublishStatus: BulkPublishStatusType
    FailureMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCognitoEventsResponseTypeDef(BaseValidatorModel):
    Events: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterDeviceResponseTypeDef(BaseValidatorModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDatasetResponseTypeDef(BaseValidatorModel):
    Dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    Dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    Datasets: List[DatasetTypeDef]
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeIdentityPoolUsageResponseTypeDef(BaseValidatorModel):
    IdentityPoolUsage: IdentityPoolUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListIdentityPoolUsageResponseTypeDef(BaseValidatorModel):
    IdentityPoolUsages: List[IdentityPoolUsageTypeDef]
    MaxResults: int
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeIdentityUsageResponseTypeDef(BaseValidatorModel):
    IdentityUsage: IdentityUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdentityPoolConfigurationResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncOutputTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SetIdentityPoolConfigurationResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncOutputTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRecordsResponseTypeDef(BaseValidatorModel):
    Records: List[RecordTypeDef]
    Count: int
    DatasetSyncCount: int
    LastModifiedBy: str
    MergedDatasetNames: List[str]
    DatasetExists: bool
    DatasetDeletedAfterRequestedSyncCount: bool
    SyncSessionToken: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateRecordsResponseTypeDef(BaseValidatorModel):
    Records: List[RecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class RecordPatchTypeDef(BaseValidatorModel):
    Op: OperationType
    Key: str
    SyncCount: int
    Value: Optional[str] = None
    DeviceLastModifiedDate: Optional[TimestampTypeDef] = None


class PushSyncUnionTypeDef(BaseValidatorModel):
    pass


class SetIdentityPoolConfigurationRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: Optional[PushSyncUnionTypeDef] = None
    CognitoStreams: Optional[CognitoStreamsTypeDef] = None


class UpdateRecordsRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    SyncSessionToken: str
    DeviceId: Optional[str] = None
    RecordPatches: Optional[Sequence[RecordPatchTypeDef]] = None
    ClientContext: Optional[str] = None


