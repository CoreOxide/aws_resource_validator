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
from aws_resource_validator.pydantic_models.kinesisvideo_constants import *

class SingleMasterConfigurationTypeDef(BaseModel):
    MessageTtlSeconds: Optional[int] = None

class ChannelNameConditionTypeDef(BaseModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateStreamInputRequestTypeDef(BaseModel):
    StreamName: str
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    DataRetentionInHours: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteEdgeConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DeleteSignalingChannelInputRequestTypeDef(BaseModel):
    ChannelARN: str
    CurrentVersion: Optional[str] = None

class DeleteStreamInputRequestTypeDef(BaseModel):
    StreamARN: str
    CurrentVersion: Optional[str] = None

class LocalSizeConfigTypeDef(BaseModel):
    MaxLocalMediaSizeInMB: Optional[int] = None
    StrategyOnFullSize: Optional[StrategyOnFullSizeType] = None

class DescribeEdgeConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DescribeImageGenerationConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeMappedResourceConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MappedResourceConfigurationListItemTypeDef(BaseModel):
    Type: Optional[str] = None
    ARN: Optional[str] = None

class DescribeMediaStorageConfigurationInputRequestTypeDef(BaseModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None

class MediaStorageConfigurationTypeDef(BaseModel):
    Status: MediaStorageConfigurationStatusType
    StreamARN: Optional[str] = None

class DescribeNotificationConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DescribeSignalingChannelInputRequestTypeDef(BaseModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None

class DescribeStreamInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StreamInfoTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[StatusType] = None
    CreationTime: Optional[datetime] = None
    DataRetentionInHours: Optional[int] = None

class LastRecorderStatusTypeDef(BaseModel):
    JobStatusDetails: Optional[str] = None
    LastCollectedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    RecorderStatus: Optional[RecorderStatusType] = None

class LastUploaderStatusTypeDef(BaseModel):
    JobStatusDetails: Optional[str] = None
    LastCollectedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    UploaderStatus: Optional[UploaderStatusType] = None

class GetDataEndpointInputRequestTypeDef(BaseModel):
    APIName: APINameType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class SingleMasterChannelEndpointConfigurationTypeDef(BaseModel):
    Protocols: Optional[Sequence[ChannelProtocolType]] = None
    Role: Optional[ChannelRoleType] = None

class ResourceEndpointListItemTypeDef(BaseModel):
    Protocol: Optional[ChannelProtocolType] = None
    ResourceEndpoint: Optional[str] = None

class ImageGenerationDestinationConfigTypeDef(BaseModel):
    Uri: str
    DestinationRegion: str

class ListEdgeAgentConfigurationsInputRequestTypeDef(BaseModel):
    HubDeviceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StreamNameConditionTypeDef(BaseModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    NextToken: Optional[str] = None

class ListTagsForStreamInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None

class MediaSourceConfigTypeDef(BaseModel):
    MediaUriSecretArn: str
    MediaUriType: MediaUriTypeType

class NotificationDestinationConfigTypeDef(BaseModel):
    Uri: str

class ScheduleConfigTypeDef(BaseModel):
    ScheduleExpression: str
    DurationInSeconds: int

class TagStreamInputRequestTypeDef(BaseModel):
    Tags: Mapping[str, str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeyList: Sequence[str]

class UntagStreamInputRequestTypeDef(BaseModel):
    TagKeyList: Sequence[str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None

class UpdateDataRetentionInputRequestTypeDef(BaseModel):
    CurrentVersion: str
    Operation: UpdateDataRetentionOperationType
    DataRetentionChangeInHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class UpdateStreamInputRequestTypeDef(BaseModel):
    CurrentVersion: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None

class ChannelInfoTypeDef(BaseModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None
    ChannelType: Optional[ChannelTypeType] = None
    ChannelStatus: Optional[StatusType] = None
    CreationTime: Optional[datetime] = None
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None
    Version: Optional[str] = None

class UpdateSignalingChannelInputRequestTypeDef(BaseModel):
    ChannelARN: str
    CurrentVersion: str
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None

class ListSignalingChannelsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChannelNameCondition: Optional[ChannelNameConditionTypeDef] = None

class CreateSignalingChannelInputRequestTypeDef(BaseModel):
    ChannelName: str
    ChannelType: Optional[ChannelTypeType] = None
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSignalingChannelOutputTypeDef(BaseModel):
    ChannelARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamOutputTypeDef(BaseModel):
    StreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataEndpointOutputTypeDef(BaseModel):
    DataEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForStreamOutputTypeDef(BaseModel):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletionConfigTypeDef(BaseModel):
    EdgeRetentionInHours: Optional[int] = None
    LocalSizeConfig: Optional[LocalSizeConfigTypeDef] = None
    DeleteAfterUpload: Optional[bool] = None

class DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef(BaseModel):
    HubDeviceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef(BaseModel):
    ChannelNameCondition: Optional[ChannelNameConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMappedResourceConfigurationOutputTypeDef(BaseModel):
    MappedResourceConfigurationList: List[MappedResourceConfigurationListItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMediaStorageConfigurationOutputTypeDef(BaseModel):
    MediaStorageConfiguration: MediaStorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMediaStorageConfigurationInputRequestTypeDef(BaseModel):
    ChannelARN: str
    MediaStorageConfiguration: MediaStorageConfigurationTypeDef

class DescribeStreamOutputTypeDef(BaseModel):
    StreamInfo: StreamInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsOutputTypeDef(BaseModel):
    StreamInfoList: List[StreamInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EdgeAgentStatusTypeDef(BaseModel):
    LastRecorderStatus: Optional[LastRecorderStatusTypeDef] = None
    LastUploaderStatus: Optional[LastUploaderStatusTypeDef] = None

class GetSignalingChannelEndpointInputRequestTypeDef(BaseModel):
    ChannelARN: str
    SingleMasterChannelEndpointConfiguration: Optional[       SingleMasterChannelEndpointConfigurationTypeDef     ] = None

class GetSignalingChannelEndpointOutputTypeDef(BaseModel):
    ResourceEndpointList: List[ResourceEndpointListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImageGenerationConfigurationTypeDef(BaseModel):
    Status: ConfigurationStatusType
    ImageSelectorType: ImageSelectorTypeType
    DestinationConfig: ImageGenerationDestinationConfigTypeDef
    SamplingInterval: int
    Format: FormatType
    FormatConfig: Optional[Dict[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None

class ListStreamsInputListStreamsPaginateTypeDef(BaseModel):
    StreamNameCondition: Optional[StreamNameConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamNameCondition: Optional[StreamNameConditionTypeDef] = None

class NotificationConfigurationTypeDef(BaseModel):
    Status: ConfigurationStatusType
    DestinationConfig: NotificationDestinationConfigTypeDef

class RecorderConfigTypeDef(BaseModel):
    MediaSourceConfig: MediaSourceConfigTypeDef
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None

class UploaderConfigTypeDef(BaseModel):
    ScheduleConfig: ScheduleConfigTypeDef

class DescribeSignalingChannelOutputTypeDef(BaseModel):
    ChannelInfo: ChannelInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSignalingChannelsOutputTypeDef(BaseModel):
    ChannelInfoList: List[ChannelInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageGenerationConfigurationOutputTypeDef(BaseModel):
    ImageGenerationConfiguration: ImageGenerationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageGenerationConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    ImageGenerationConfiguration: Optional[ImageGenerationConfigurationTypeDef] = None

class DescribeNotificationConfigurationOutputTypeDef(BaseModel):
    NotificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNotificationConfigurationInputRequestTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None

class EdgeConfigTypeDef(BaseModel):
    HubDeviceArn: str
    RecorderConfig: RecorderConfigTypeDef
    UploaderConfig: Optional[UploaderConfigTypeDef] = None
    DeletionConfig: Optional[DeletionConfigTypeDef] = None

class DescribeEdgeConfigurationOutputTypeDef(BaseModel):
    StreamName: str
    StreamARN: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    SyncStatus: SyncStatusType
    FailedStatusDetails: str
    EdgeConfig: EdgeConfigTypeDef
    EdgeAgentStatus: EdgeAgentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEdgeAgentConfigurationsEdgeConfigTypeDef(BaseModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SyncStatus: Optional[SyncStatusType] = None
    FailedStatusDetails: Optional[str] = None
    EdgeConfig: Optional[EdgeConfigTypeDef] = None

class StartEdgeConfigurationUpdateInputRequestTypeDef(BaseModel):
    EdgeConfig: EdgeConfigTypeDef
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StartEdgeConfigurationUpdateOutputTypeDef(BaseModel):
    StreamName: str
    StreamARN: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    SyncStatus: SyncStatusType
    FailedStatusDetails: str
    EdgeConfig: EdgeConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEdgeAgentConfigurationsOutputTypeDef(BaseModel):
    EdgeConfigs: List[ListEdgeAgentConfigurationsEdgeConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

