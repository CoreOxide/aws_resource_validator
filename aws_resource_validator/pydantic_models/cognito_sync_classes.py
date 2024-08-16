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
from aws_resource_validator.pydantic_models.cognito_sync_constants import *

class BulkPublishRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class DeleteDatasetRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str

class DescribeDatasetRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str

class DescribeIdentityPoolUsageRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class IdentityPoolUsageTypeDef(BaseValidatorModel):
    IdentityPoolId: Optional[str] = None
    SyncSessionsCount: Optional[int] = None
    DataStorage: Optional[int] = None
    LastModifiedDate: Optional[datetime] = None

class DescribeIdentityUsageRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str

class IdentityUsageTypeDef(BaseValidatorModel):
    IdentityId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    DatasetCount: Optional[int] = None
    DataStorage: Optional[int] = None

class GetBulkPublishDetailsRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class GetCognitoEventsRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class GetIdentityPoolConfigurationRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str

class PushSyncTypeDef(BaseValidatorModel):
    ApplicationArns: Optional[List[str]] = None
    RoleArn: Optional[str] = None

class ListDatasetsRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentityPoolUsageRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRecordsRequestRequestTypeDef(BaseValidatorModel):
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

class RegisterDeviceRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    Platform: PlatformType
    Token: str

class SetCognitoEventsRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    Events: Mapping[str, str]

class SubscribeToDatasetRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    DeviceId: str

class UnsubscribeFromDatasetRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityPoolUsageResponseTypeDef(BaseValidatorModel):
    IdentityPoolUsage: IdentityPoolUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdentityPoolUsageResponseTypeDef(BaseValidatorModel):
    IdentityPoolUsages: List[IdentityPoolUsageTypeDef]
    MaxResults: int
    Count: int
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityUsageResponseTypeDef(BaseValidatorModel):
    IdentityUsage: IdentityUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityPoolConfigurationResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SetIdentityPoolConfigurationRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: Optional[PushSyncTypeDef] = None
    CognitoStreams: Optional[CognitoStreamsTypeDef] = None

class SetIdentityPoolConfigurationResponseTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    PushSync: PushSyncTypeDef
    CognitoStreams: CognitoStreamsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecordsResponseTypeDef(BaseValidatorModel):
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

class UpdateRecordsResponseTypeDef(BaseValidatorModel):
    Records: List[RecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RecordPatchTypeDef(BaseValidatorModel):
    Op: OperationType
    Key: str
    SyncCount: int
    Value: Optional[str] = None
    DeviceLastModifiedDate: Optional[TimestampTypeDef] = None

class UpdateRecordsRequestRequestTypeDef(BaseValidatorModel):
    IdentityPoolId: str
    IdentityId: str
    DatasetName: str
    SyncSessionToken: str
    DeviceId: Optional[str] = None
    RecordPatches: Optional[Sequence[RecordPatchTypeDef]] = None
    ClientContext: Optional[str] = None

