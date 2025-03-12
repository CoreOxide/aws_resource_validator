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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateStreamInputTypeDef(BaseValidatorModel):
    StreamName: str
    DeviceName: Optional[str] = None
    MediaType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    DataRetentionInHours: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteEdgeConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DeleteSignalingChannelInputTypeDef(BaseValidatorModel):
    ChannelARN: str
    CurrentVersion: Optional[str] = None


class DeleteStreamInputTypeDef(BaseValidatorModel):
    StreamARN: str
    CurrentVersion: Optional[str] = None


class LocalSizeConfigTypeDef(BaseValidatorModel):
    MaxLocalMediaSizeInMB: Optional[int] = None
    StrategyOnFullSize: Optional[StrategyOnFullSizeType] = None


class DescribeEdgeConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DescribeImageGenerationConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeMappedResourceConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMediaStorageConfigurationInputTypeDef(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None


class MediaStorageConfigurationTypeDef(BaseValidatorModel):
    Status: MediaStorageConfigurationStatusType
    StreamARN: Optional[str] = None


class DescribeNotificationConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class DescribeSignalingChannelInputTypeDef(BaseValidatorModel):
    ChannelName: Optional[str] = None
    ChannelARN: Optional[str] = None


class DescribeStreamInputTypeDef(BaseValidatorModel):
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


class GetDataEndpointInputTypeDef(BaseValidatorModel):
    APIName: APINameType
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class SingleMasterChannelEndpointConfigurationTypeDef(BaseValidatorModel):
    Protocols: Optional[Sequence[ChannelProtocolType]] = None
    Role: Optional[ChannelRoleType] = None


class ImageGenerationDestinationConfigTypeDef(BaseValidatorModel):
    Uri: str
    DestinationRegion: str


class ListEdgeAgentConfigurationsInputTypeDef(BaseValidatorModel):
    HubDeviceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StreamNameConditionTypeDef(BaseValidatorModel):
    ComparisonOperator: Optional[Literal["BEGINS_WITH"]] = None
    ComparisonValue: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    NextToken: Optional[str] = None


class ListTagsForStreamInputTypeDef(BaseValidatorModel):
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


class TagStreamInputTypeDef(BaseValidatorModel):
    Tags: Mapping[str, str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeyList: Sequence[str]


class UntagStreamInputTypeDef(BaseValidatorModel):
    TagKeyList: Sequence[str]
    StreamARN: Optional[str] = None
    StreamName: Optional[str] = None


class UpdateDataRetentionInputTypeDef(BaseValidatorModel):
    CurrentVersion: str
    Operation: UpdateDataRetentionOperationType
    DataRetentionChangeInHours: int
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None


class UpdateStreamInputTypeDef(BaseValidatorModel):
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


class UpdateSignalingChannelInputTypeDef(BaseValidatorModel):
    ChannelARN: str
    CurrentVersion: str
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None


class ListSignalingChannelsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChannelNameCondition: Optional[ChannelNameConditionTypeDef] = None


class CreateSignalingChannelInputTypeDef(BaseValidatorModel):
    ChannelName: str
    ChannelType: Optional[ChannelTypeType] = None
    SingleMasterConfiguration: Optional[SingleMasterConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
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
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForStreamOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DeletionConfigTypeDef(BaseValidatorModel):
    EdgeRetentionInHours: Optional[int] = None
    LocalSizeConfig: Optional[LocalSizeConfigTypeDef] = None
    DeleteAfterUpload: Optional[bool] = None


class DescribeMappedResourceConfigurationInputPaginateTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEdgeAgentConfigurationsInputPaginateTypeDef(BaseValidatorModel):
    HubDeviceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSignalingChannelsInputPaginateTypeDef(BaseValidatorModel):
    ChannelNameCondition: Optional[ChannelNameConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MappedResourceConfigurationListItemTypeDef(BaseValidatorModel):
    pass


class DescribeMappedResourceConfigurationOutputTypeDef(BaseValidatorModel):
    MappedResourceConfigurationList: List[MappedResourceConfigurationListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMediaStorageConfigurationOutputTypeDef(BaseValidatorModel):
    MediaStorageConfiguration: MediaStorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMediaStorageConfigurationInputTypeDef(BaseValidatorModel):
    ChannelARN: str
    MediaStorageConfiguration: MediaStorageConfigurationTypeDef


class DescribeStreamOutputTypeDef(BaseValidatorModel):
    StreamInfo: StreamInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListStreamsOutputTypeDef(BaseValidatorModel):
    StreamInfoList: List[StreamInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EdgeAgentStatusTypeDef(BaseValidatorModel):
    LastRecorderStatus: Optional[LastRecorderStatusTypeDef] = None
    LastUploaderStatus: Optional[LastUploaderStatusTypeDef] = None


class GetSignalingChannelEndpointInputTypeDef(BaseValidatorModel):
    ChannelARN: str
    SingleMasterChannelEndpointConfiguration: Optional[ SingleMasterChannelEndpointConfigurationTypeDef ] = None


class ResourceEndpointListItemTypeDef(BaseValidatorModel):
    pass


class GetSignalingChannelEndpointOutputTypeDef(BaseValidatorModel):
    ResourceEndpointList: List[ResourceEndpointListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ImageGenerationConfigurationOutputTypeDef(BaseValidatorModel):
    Status: ConfigurationStatusType
    ImageSelectorType: ImageSelectorTypeType
    DestinationConfig: ImageGenerationDestinationConfigTypeDef
    SamplingInterval: int
    Format: FormatType
    FormatConfig: Optional[Dict[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None


class ImageGenerationConfigurationTypeDef(BaseValidatorModel):
    Status: ConfigurationStatusType
    ImageSelectorType: ImageSelectorTypeType
    DestinationConfig: ImageGenerationDestinationConfigTypeDef
    SamplingInterval: int
    Format: FormatType
    FormatConfig: Optional[Mapping[Literal["JPEGQuality"], str]] = None
    WidthPixels: Optional[int] = None
    HeightPixels: Optional[int] = None


class ListStreamsInputPaginateTypeDef(BaseValidatorModel):
    StreamNameCondition: Optional[StreamNameConditionTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamsInputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeImageGenerationConfigurationOutputTypeDef(BaseValidatorModel):
    ImageGenerationConfiguration: ImageGenerationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeNotificationConfigurationOutputTypeDef(BaseValidatorModel):
    NotificationConfiguration: NotificationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNotificationConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None


class EdgeConfigTypeDef(BaseValidatorModel):
    HubDeviceArn: str
    RecorderConfig: RecorderConfigTypeDef
    UploaderConfig: Optional[UploaderConfigTypeDef] = None
    DeletionConfig: Optional[DeletionConfigTypeDef] = None


class ImageGenerationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateImageGenerationConfigurationInputTypeDef(BaseValidatorModel):
    StreamName: Optional[str] = None
    StreamARN: Optional[str] = None
    ImageGenerationConfiguration: Optional[ImageGenerationConfigurationUnionTypeDef] = None


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


class StartEdgeConfigurationUpdateInputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


