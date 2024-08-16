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
from aws_resource_validator.pydantic_models.kinesisvideo_constants import *

class SingleMasterConfigurationTypeDef(BaseValidatorModel):
    MessageTtlSeconds: Optional[int] = None

class ChannelNameConditionTypeDef(BaseValidatorModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateStreamInputRequestTypeDef(BaseValidatorModel):
    StreamName: str
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    DataRetentionInHours: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteEdgeConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DeleteSignalingChannelInputRequestTypeDef(BaseValidatorModel):
    ChannelARN: str
    CurrentVersion: Optional[str] = None

class DeleteStreamInputRequestTypeDef(BaseValidatorModel):
    StreamARN: str
    CurrentVersion: Optional[str] = None

class LocalSizeConfigTypeDef(BaseValidatorModel):
    MaxLocalMediaSizeInMB: Optional[int] = None
    StrategyOnFullSize: Optional[StrategyOnFullSizeType] = None

class DescribeEdgeConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DescribeImageGenerationConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeMappedResourceConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MappedResourceConfigurationListItemTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    ARN: Optional[str] = None

class DescribeMediaStorageConfigurationInputRequestTypeDef(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None

class MediaStorageConfigurationTypeDef(BaseValidatorModel):
    Status: MediaStorageConfigurationStatusType
    StreamARN: Optional[str] = None

class DescribeNotificationConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class DescribeSignalingChannelInputRequestTypeDef(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None

class DescribeStreamInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StreamInfoTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[StatusType] = None
    CreationTime: Optional[datetime] = None
    DataRetentionInHours: Optional[int] = None

class LastRecorderStatusTypeDef(BaseValidatorModel):
    JobStatusDetails: Optional[str] = None
    LastCollectedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    RecorderStatus: Optional[RecorderStatusType] = None

class LastUploaderStatusTypeDef(BaseValidatorModel):
    JobStatusDetails: Optional[str] = None
    LastCollectedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    UploaderStatus: Optional[UploaderStatusType] = None

class GetDataEndpointInputRequestTypeDef(BaseValidatorModel):
    APIName: APINameType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class SingleMasterChannelEndpointConfigurationTypeDef(BaseValidatorModel):
    Protocols: Optional[Sequence[ChannelProtocolType]] = None
    Role: Optional[ChannelRoleType] = None

class ResourceEndpointListItemTypeDef(BaseValidatorModel):
    Protocol: Optional[ChannelProtocolType] = None
    ResourceEndpoint: Optional[str] = None

class ImageGenerationDestinationConfigTypeDef(BaseValidatorModel):
    Uri: str
    DestinationRegion: str

class ListEdgeAgentConfigurationsInputRequestTypeDef(BaseValidatorModel):
    HubDeviceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StreamNameConditionTypeDef(BaseValidatorModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None

class ListTagsForStreamInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None

class MediaSourceConfigTypeDef(BaseValidatorModel):
    MediaUriSecretArn: str
    MediaUriType: MediaUriTypeType

class NotificationDestinationConfigTypeDef(BaseValidatorModel):
    Uri: str

class ScheduleConfigTypeDef(BaseValidatorModel):
    ScheduleExpression: str
    DurationInSeconds: int

class TagStreamInputRequestTypeDef(BaseValidatorModel):
    Tags: Mapping[str, str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeyList: Sequence[str]

class UntagStreamInputRequestTypeDef(BaseValidatorModel):
    TagKeyList: Sequence[str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None

class UpdateDataRetentionInputRequestTypeDef(BaseValidatorModel):
    CurrentVersion: str
    Operation: UpdateDataRetentionOperationType
    DataRetentionChangeInHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class UpdateStreamInputRequestTypeDef(BaseValidatorModel):
    CurrentVersion: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None

class ChannelInfoTypeDef(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None
    ChannelType: Optional[ChannelTypeType] = None
    ChannelStatus: Optional[StatusType] = None
    CreationTime: Optional[datetime] = None
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None
    Version: Optional[str] = None

class UpdateSignalingChannelInputRequestTypeDef(BaseValidatorModel):
    ChannelARN: str
    CurrentVersion: str
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None

class ListSignalingChannelsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChannelNameCondition: Optional[ChannelNameConditionTypeDef] = None

class CreateSignalingChannelInputRequestTypeDef(BaseValidatorModel):
    ChannelName: str
    ChannelType: Optional[ChannelTypeType] = None
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateSignalingChannelOutputTypeDef(BaseValidatorModel):
    ChannelARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamOutputTypeDef(BaseValidatorModel):
    StreamARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataEndpointOutputTypeDef(BaseValidatorModel):
    DataEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForStreamOutputTypeDef(BaseValidatorModel):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletionConfigTypeDef(BaseValidatorModel):
    EdgeRetentionInHours: Optional[int] = None
    LocalSizeConfig: Optional[LocalSizeConfigTypeDef] = None
    DeleteAfterUpload: Optional[bool] = None

class DescribeMappedResourceConfigurationInputDescribeMappedResourceConfigurationPaginateTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEdgeAgentConfigurationsInputListEdgeAgentConfigurationsPaginateTypeDef(BaseValidatorModel):
    HubDeviceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef(BaseValidatorModel):
    ChannelNameCondition: Optional[ChannelNameConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMappedResourceConfigurationOutputTypeDef(BaseValidatorModel):
    MappedResourceConfigurationList: List[MappedResourceConfigurationListItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMediaStorageConfigurationOutputTypeDef(BaseValidatorModel):
    MediaStorageConfiguration: MediaStorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMediaStorageConfigurationInputRequestTypeDef(BaseValidatorModel):
    ChannelARN: str
    MediaStorageConfiguration: MediaStorageConfigurationTypeDef

class DescribeStreamOutputTypeDef(BaseValidatorModel):
    StreamInfo: StreamInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsOutputTypeDef(BaseValidatorModel):
    StreamInfoList: List[StreamInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EdgeAgentStatusTypeDef(BaseValidatorModel):
    LastRecorderStatus: Optional[LastRecorderStatusTypeDef] = None
    LastUploaderStatus: Optional[LastUploaderStatusTypeDef] = None

class GetSignalingChannelEndpointInputRequestTypeDef(BaseValidatorModel):
    ChannelARN: str
    SingleMasterChannelEndpointConfiguration: Optional[       SingleMasterChannelEndpointConfigurationTypeDef     ] = None

class GetSignalingChannelEndpointOutputTypeDef(BaseValidatorModel):
    ResourceEndpointList: List[ResourceEndpointListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImageGenerationConfigurationTypeDef(BaseValidatorModel):
    Status: ConfigurationStatusType
    ImageSelectorType: ImageSelectorTypeType
    DestinationConfig: ImageGenerationDestinationConfigTypeDef
    SamplingInterval: int
    Format: FormatType
    FormatConfig: Optional[Dict[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None

class ListStreamsInputListStreamsPaginateTypeDef(BaseValidatorModel):
    StreamNameCondition: Optional[StreamNameConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamNameCondition: Optional[StreamNameConditionTypeDef] = None

class NotificationConfigurationTypeDef(BaseValidatorModel):
    Status: ConfigurationStatusType
    DestinationConfig: NotificationDestinationConfigTypeDef

class RecorderConfigTypeDef(BaseValidatorModel):
    MediaSourceConfig: MediaSourceConfigTypeDef
    ScheduleConfig: Optional[ScheduleConfigTypeDef] = None

class UploaderConfigTypeDef(BaseValidatorModel):
    ScheduleConfig: ScheduleConfigTypeDef

class DescribeSignalingChannelOutputTypeDef(BaseValidatorModel):
    ChannelInfo: ChannelInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSignalingChannelsOutputTypeDef(BaseValidatorModel):
    ChannelInfoList: List[ChannelInfoTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageGenerationConfigurationOutputTypeDef(BaseValidatorModel):
    ImageGenerationConfiguration: ImageGenerationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImageGenerationConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    ImageGenerationConfiguration: Optional[ImageGenerationConfigurationTypeDef] = None

class DescribeNotificationConfigurationOutputTypeDef(BaseValidatorModel):
    NotificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNotificationConfigurationInputRequestTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None

class EdgeConfigTypeDef(BaseValidatorModel):
    HubDeviceArn: str
    RecorderConfig: RecorderConfigTypeDef
    UploaderConfig: Optional[UploaderConfigTypeDef] = None
    DeletionConfig: Optional[DeletionConfigTypeDef] = None

class DescribeEdgeConfigurationOutputTypeDef(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    SyncStatus: SyncStatusType
    FailedStatusDetails: str
    EdgeConfig: EdgeConfigTypeDef
    EdgeAgentStatus: EdgeAgentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEdgeAgentConfigurationsEdgeConfigTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SyncStatus: Optional[SyncStatusType] = None
    FailedStatusDetails: Optional[str] = None
    EdgeConfig: Optional[EdgeConfigTypeDef] = None

class StartEdgeConfigurationUpdateInputRequestTypeDef(BaseValidatorModel):
    EdgeConfig: EdgeConfigTypeDef
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None

class StartEdgeConfigurationUpdateOutputTypeDef(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    SyncStatus: SyncStatusType
    FailedStatusDetails: str
    EdgeConfig: EdgeConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEdgeAgentConfigurationsOutputTypeDef(BaseValidatorModel):
    EdgeConfigs: List[ListEdgeAgentConfigurationsEdgeConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

