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
from aws_resource_validator.pydantic_models.cognito_sync_constants import *

class BulkPublishRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CognitoStreamsTypeDef(BaseModel):
    StreamName: Optional[str] = None
    RoleArn: Optional[str] = None
    StreamingStatus: Optional[StreamingStatusType] = None

class DatasetTypeDef(BaseModel):
    IdentityId: Optional[str] = None
    DatasetName: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    DataStorage: Optional[int] = None
    NumRecords: Optional[int] = None

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str

class DescribeIdentityPoolUsageRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str

class IdentityPoolUsageTypeDef(BaseModel):
    IdentityPoolId: Optional[str] = None
    SyncSessionsCount: Optional[int] = None
    DataStorage: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None

class DescribeIdentityUsageRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str

class IdentityUsageTypeDef(BaseModel):
    IdentityId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    DatasetCount: Optional[int] = None
    DataStorage: Optional[int] = None

class GetBulkPublishDetailsRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str

class GetCognitoEventsRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str

class GetIdentityPoolConfigurationRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str

class PushSyncTypeDef(BaseModel):
    ApplicationArns: Optional[List[str]] = None
    RoleArn: Optional[str] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentityPoolUsageRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRecordsRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    LastSyncCount: Optional[int] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SyncSessionToken: Optional[str] = None

class RecordTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    SyncCount: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    DeviceLastModifiedDate: Optional[datetime] = None

class RegisterDeviceRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    Platform: PlatformType
    Token: str

class SetCognitoEventsRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    Events: Mapping[str, str]

class SubscribeToDatasetRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str

class UnsubscribeFromDatasetRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str

class BulkPublishResponseTypeDef(BaseModel):
    IdentityPoolId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetBulkPublishDetailsResponseTypeDef(BaseModel):
    IdentityPoolId: str
    BulkPublishStartTime: datetime
    BulkPublishCompleteTime: datetime
    BulkPublishStatus: BulkPublishStatusType
    FailureMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCognitoEventsResponseTypeDef(BaseModel):
    Events: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDeviceResponseTypeDef(BaseModel):
    DeviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDatasetResponseTypeDef(BaseModel):
    Dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(BaseModel):
    Dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseModel):
    Datasets: List[DatasetTypeDef]
    Count: int
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityPoolUsageResponseTypeDef(BaseModel):
    IdentityPoolUsage: IdentityPoolUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityPoolUsageResponseTypeDef(BaseModel):
    IdentityPoolUsages: List[IdentityPoolUsageTypeDef]
    MaxResults: int
    Count: int
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityUsageResponseTypeDef(BaseModel):
    IdentityUsage: IdentityUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityPoolConfigurationResponseTypeDef(BaseModel):
    IdentityPoolId: str
    PushSync: PushSyncTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetIdentityPoolConfigurationRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    PushSync: Optional[PushSyncTypeDef] = None
    CognitoStreams: Optional[CognitoStreamsTypeDef] = None

class SetIdentityPoolConfigurationResponseTypeDef(BaseModel):
    IdentityPoolId: str
    PushSync: PushSyncTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecordsResponseTypeDef(BaseModel):
    Records: List[RecordTypeDef]
    NextToken: str
    Count: int
    DatasetSyncCount: int
    LastModifiedBy: str
    MergedDatasetNames: List[str]
    DatasetExists: bool
    DatasetDeletedAfterRequestedSyncCount: bool
    SyncSessionToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecordsResponseTypeDef(BaseModel):
    Records: List[RecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecordPatchTypeDef(BaseModel):
    Op: OperationType
    Key: str
    SyncCount: int
    Value: Optional[str] = None
    DeviceLastModifiedDate: Optional[TimestampTypeDef] = None

class UpdateRecordsRequestRequestTypeDef(BaseModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    SyncSessionToken: str
    DeviceId: Optional[str] = None
    RecordPatches: Optional[Sequence[RecordPatchTypeDef]] = None
    ClientContext: Optional[str] = None

