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
from aws_resource_validator.pydantic_models.kinesisvideo_constants import *

class SingleMasterConfiguration(BaseValidatorModel):
    MessageTtlSeconds: Optional[int] = None


class ChannelNameCondition(BaseValidatorModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateStreamInput(BaseValidatorModel):
    StreamName: str
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    DataRetentionInHours: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteEdgeConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DeleteSignalingChannelInput(BaseValidatorModel):
    ChannelARN: str
    CurrentVersion: Optional[str] = None


class DeleteStreamInput(BaseValidatorModel):
    StreamARN: str
    CurrentVersion: Optional[str] = None


class LocalSizeConfig(BaseValidatorModel):
    MaxLocalMediaSizeInMB: Optional[int] = None
    StrategyOnFullSize: Optional[StrategyOnFullSizeType] = None


class DescribeEdgeConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DescribeImageGenerationConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeMappedResourceConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMediaStorageConfigurationInput(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None


class MediaStorageConfiguration(BaseValidatorModel):
    Status: MediaStorageConfigurationStatusType
    StreamARN: Optional[str] = None


class DescribeNotificationConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DescribeSignalingChannelInput(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None


class DescribeStreamInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class StreamInfo(BaseValidatorModel):
    DeviceName: Optional[str] = None
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Version: Optional[str] = None
    Status: Optional[StatusType] = None
    CreationTime: Optional[datetime] = None
    DataRetentionInHours: Optional[int] = None


class LastRecorderStatus(BaseValidatorModel):
    JobStatusDetails: Optional[str] = None
    LastCollectedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    RecorderStatus: Optional[RecorderStatusType] = None


class LastUploaderStatus(BaseValidatorModel):
    JobStatusDetails: Optional[str] = None
    LastCollectedTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    UploaderStatus: Optional[UploaderStatusType] = None


class GetDataEndpointInput(BaseValidatorModel):
    APIName: APINameType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class SingleMasterChannelEndpointConfiguration(BaseValidatorModel):
    Protocols: Optional[Sequence[ChannelProtocolType]] = None
    Role: Optional[ChannelRoleType] = None


class ImageGenerationDestinationConfig(BaseValidatorModel):
    Uri: str
    DestinationRegion: str


class ListEdgeAgentConfigurationsInput(BaseValidatorModel):
    HubDeviceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StreamNameCondition(BaseValidatorModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None


class ListTagsForStreamInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None


class MediaSourceConfig(BaseValidatorModel):
    MediaUriSecretArn: str
    MediaUriType: MediaUriTypeType


class NotificationDestinationConfig(BaseValidatorModel):
    Uri: str


class ScheduleConfig(BaseValidatorModel):
    ScheduleExpression: str
    DurationInSeconds: int


class TagStreamInput(BaseValidatorModel):
    Tags: Mapping[str, str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    ResourceARN: str
    TagKeyList: Sequence[str]


class UntagStreamInput(BaseValidatorModel):
    TagKeyList: Sequence[str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None


class UpdateDataRetentionInput(BaseValidatorModel):
    CurrentVersion: str
    Operation: UpdateDataRetentionOperationType
    DataRetentionChangeInHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class UpdateStreamInput(BaseValidatorModel):
    CurrentVersion: str
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None


class ChannelInfo(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None
    ChannelType: Optional[ChannelTypeType] = None
    ChannelStatus: Optional[StatusType] = None
    CreationTime: Optional[datetime] = None
    SingleMasterConfiguration: Optional[SingleMasterConfiguration] = None
    Version: Optional[str] = None


class UpdateSignalingChannelInput(BaseValidatorModel):
    ChannelARN: str
    CurrentVersion: str
    SingleMasterConfiguration: Optional[SingleMasterConfiguration] = None


class ListSignalingChannelsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChannelNameCondition: Optional[ChannelNameCondition] = None


class CreateSignalingChannelInput(BaseValidatorModel):
    ChannelName: str
    ChannelType: Optional[ChannelTypeType] = None
    SingleMasterConfiguration: Optional[SingleMasterConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None


class TagResourceInput(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateSignalingChannelOutput(BaseValidatorModel):
    ChannelARN: str
    ResponseMetadata: ResponseMetadata


class CreateStreamOutput(BaseValidatorModel):
    StreamARN: str
    ResponseMetadata: ResponseMetadata


class GetDataEndpointOutput(BaseValidatorModel):
    DataEndpoint: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForStreamOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeletionConfig(BaseValidatorModel):
    EdgeRetentionInHours: Optional[int] = None
    LocalSizeConfig: Optional[LocalSizeConfig] = None
    DeleteAfterUpload: Optional[bool] = None


class DescribeMappedResourceConfigurationInputPaginate(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEdgeAgentConfigurationsInputPaginate(BaseValidatorModel):
    HubDeviceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSignalingChannelsInputPaginate(BaseValidatorModel):
    ChannelNameCondition: Optional[ChannelNameCondition] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class MappedResourceConfigurationListItem(BaseValidatorModel):
    pass


class DescribeMappedResourceConfigurationOutput(BaseValidatorModel):
    MappedResourceConfigurationList: List[MappedResourceConfigurationListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMediaStorageConfigurationOutput(BaseValidatorModel):
    MediaStorageConfiguration: MediaStorageConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateMediaStorageConfigurationInput(BaseValidatorModel):
    ChannelARN: str
    MediaStorageConfiguration: MediaStorageConfiguration


class DescribeStreamOutput(BaseValidatorModel):
    StreamInfo: StreamInfo
    ResponseMetadata: ResponseMetadata


class ListStreamsOutput(BaseValidatorModel):
    StreamInfoList: List[StreamInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EdgeAgentStatus(BaseValidatorModel):
    LastRecorderStatus: Optional[LastRecorderStatus] = None
    LastUploaderStatus: Optional[LastUploaderStatus] = None


class GetSignalingChannelEndpointInput(BaseValidatorModel):
    ChannelARN: str
    SingleMasterChannelEndpointConfiguration: Optional[ SingleMasterChannelEndpointConfiguration ] = None


class ResourceEndpointListItem(BaseValidatorModel):
    pass


class GetSignalingChannelEndpointOutput(BaseValidatorModel):
    ResourceEndpointList: List[ResourceEndpointListItem]
    ResponseMetadata: ResponseMetadata


class ImageGenerationConfigurationOutput(BaseValidatorModel):
    Status: ConfigurationStatusType
    ImageSelectorType: ImageSelectorTypeType
    DestinationConfig: ImageGenerationDestinationConfig
    SamplingInterval: int
    Format: FormatType
    FormatConfig: Optional[Dict[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None


class ImageGenerationConfiguration(BaseValidatorModel):
    Status: ConfigurationStatusType
    ImageSelectorType: ImageSelectorTypeType
    DestinationConfig: ImageGenerationDestinationConfig
    SamplingInterval: int
    Format: FormatType
    FormatConfig: Optional[Mapping[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None


class ListStreamsInputPaginate(BaseValidatorModel):
    StreamNameCondition: Optional[StreamNameCondition] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StreamNameCondition: Optional[StreamNameCondition] = None


class NotificationConfiguration(BaseValidatorModel):
    Status: ConfigurationStatusType
    DestinationConfig: NotificationDestinationConfig


class RecorderConfig(BaseValidatorModel):
    MediaSourceConfig: MediaSourceConfig
    ScheduleConfig: Optional[ScheduleConfig] = None


class UploaderConfig(BaseValidatorModel):
    ScheduleConfig: ScheduleConfig


class DescribeSignalingChannelOutput(BaseValidatorModel):
    ChannelInfo: ChannelInfo
    ResponseMetadata: ResponseMetadata


class ListSignalingChannelsOutput(BaseValidatorModel):
    ChannelInfoList: List[ChannelInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeImageGenerationConfigurationOutput(BaseValidatorModel):
    ImageGenerationConfiguration: ImageGenerationConfigurationOutput
    ResponseMetadata: ResponseMetadata


class DescribeNotificationConfigurationOutput(BaseValidatorModel):
    NotificationConfiguration: NotificationConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateNotificationConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None


class EdgeConfig(BaseValidatorModel):
    HubDeviceArn: str
    RecorderConfig: RecorderConfig
    UploaderConfig: Optional[UploaderConfig] = None
    DeletionConfig: Optional[DeletionConfig] = None


class ImageGenerationConfigurationUnion(BaseValidatorModel):
    pass


class UpdateImageGenerationConfigurationInput(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    ImageGenerationConfiguration: Optional[ImageGenerationConfigurationUnion] = None


class DescribeEdgeConfigurationOutput(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    SyncStatus: SyncStatusType
    FailedStatusDetails: str
    EdgeConfig: EdgeConfig
    EdgeAgentStatus: EdgeAgentStatus
    ResponseMetadata: ResponseMetadata


class ListEdgeAgentConfigurationsEdgeConfig(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    SyncStatus: Optional[SyncStatusType] = None
    FailedStatusDetails: Optional[str] = None
    EdgeConfig: Optional[EdgeConfig] = None


class StartEdgeConfigurationUpdateInput(BaseValidatorModel):
    EdgeConfig: EdgeConfig
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class StartEdgeConfigurationUpdateOutput(BaseValidatorModel):
    StreamName: str
    StreamARN: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    SyncStatus: SyncStatusType
    FailedStatusDetails: str
    EdgeConfig: EdgeConfig
    ResponseMetadata: ResponseMetadata


class ListEdgeAgentConfigurationsOutput(BaseValidatorModel):
    EdgeConfigs: List[ListEdgeAgentConfigurationsEdgeConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


