from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediapackage.mediapackage_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Authorization(BaseValidatorModel):
    CdnIdentifierSecret: str
    SecretsRoleArn: str


class EgressAccessLogs(BaseValidatorModel):
    LogGroupName: Optional[str] = None


class IngressAccessLogs(BaseValidatorModel):
    LogGroupName: Optional[str] = None


class HlsManifestCreateOrUpdateParameters(BaseValidatorModel):
    Id: str
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None


class StreamSelection(BaseValidatorModel):
    MaxVideoBitsPerSecond: Optional[int] = None
    MinVideoBitsPerSecond: Optional[int] = None
    StreamOrder: Optional[StreamOrderType] = None


class HlsManifest(BaseValidatorModel):
    Id: str
    AdMarkers: Optional[AdMarkersType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    Url: Optional[str] = None
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_channel' function.
class CreateChannelRequest(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class S3Destination(BaseValidatorModel):
    BucketName: str
    ManifestKey: str
    RoleArn: str


class DeleteChannelRequest(BaseValidatorModel):
    Id: str


class DeleteOriginEndpointRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'describe_channel' function.
class DescribeChannelRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'describe_harvest_job' function.
class DescribeHarvestJobRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'describe_origin_endpoint' function.
class DescribeOriginEndpointRequest(BaseValidatorModel):
    Id: str


class EncryptionContractConfiguration(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType


class IngestEndpoint(BaseValidatorModel):
    Id: Optional[str] = None
    Password: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_channels' function.
class ListChannelsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_harvest_jobs' function.
class ListHarvestJobsRequest(BaseValidatorModel):
    IncludeChannelId: Optional[str] = None
    IncludeStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_origin_endpoints' function.
class ListOriginEndpointsRequest(BaseValidatorModel):
    ChannelId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'rotate_channel_credentials' function.
class RotateChannelCredentialsRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'rotate_ingest_endpoint_credentials' function.
class RotateIngestEndpointCredentialsRequest(BaseValidatorModel):
    Id: str
    IngestEndpointId: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_channel' function.
class UpdateChannelRequest(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None


# This class is the input for the 'configure_logs' function.
class ConfigureLogsRequest(BaseValidatorModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogs] = None
    IngressAccessLogs: Optional[IngressAccessLogs] = None


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_harvest_job' function.
class CreateHarvestJobRequest(BaseValidatorModel):
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3Destination
    StartTime: str


# This class is the output for the 'create_harvest_job' function.
class CreateHarvestJobResponse(BaseValidatorModel):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3Destination
    StartTime: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_harvest_job' function.
class DescribeHarvestJobResponse(BaseValidatorModel):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3Destination
    StartTime: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


class HarvestJob(BaseValidatorModel):
    Arn: Optional[str] = None
    ChannelId: Optional[str] = None
    CreatedAt: Optional[str] = None
    EndTime: Optional[str] = None
    Id: Optional[str] = None
    OriginEndpointId: Optional[str] = None
    S3Destination: Optional[S3Destination] = None
    StartTime: Optional[str] = None
    Status: Optional[StatusType] = None


class SpekeKeyProviderOutput(BaseValidatorModel):
    ResourceId: str
    RoleArn: str
    SystemIds: List[str]
    Url: str
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None


class SpekeKeyProvider(BaseValidatorModel):
    ResourceId: str
    RoleArn: str
    SystemIds: List[str]
    Url: str
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None


class HlsIngest(BaseValidatorModel):
    IngestEndpoints: Optional[List[IngestEndpoint]] = None


class ListChannelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHarvestJobsRequestPaginate(BaseValidatorModel):
    IncludeChannelId: Optional[str] = None
    IncludeStatus: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOriginEndpointsRequestPaginate(BaseValidatorModel):
    ChannelId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_harvest_jobs' function.
class ListHarvestJobsResponse(BaseValidatorModel):
    HarvestJobs: List[HarvestJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CmafEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None


class DashEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput
    KeyRotationIntervalSeconds: Optional[int] = None


class HlsEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None


class MssEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput


class DashEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider
    KeyRotationIntervalSeconds: Optional[int] = None


class HlsEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None


class MssEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider

SpekeKeyProviderUnion = Union[SpekeKeyProvider, SpekeKeyProviderOutput]


class Channel(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[str] = None
    Description: Optional[str] = None
    EgressAccessLogs: Optional[EgressAccessLogs] = None
    HlsIngest: Optional[HlsIngest] = None
    Id: Optional[str] = None
    IngressAccessLogs: Optional[IngressAccessLogs] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'configure_logs' function.
class ConfigureLogsResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogs
    HlsIngest: HlsIngest
    Id: str
    IngressAccessLogs: IngressAccessLogs
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel' function.
class CreateChannelResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogs
    HlsIngest: HlsIngest
    Id: str
    IngressAccessLogs: IngressAccessLogs
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_channel' function.
class DescribeChannelResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogs
    HlsIngest: HlsIngest
    Id: str
    IngressAccessLogs: IngressAccessLogs
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rotate_channel_credentials' function.
class RotateChannelCredentialsResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogs
    HlsIngest: HlsIngest
    Id: str
    IngressAccessLogs: IngressAccessLogs
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rotate_ingest_endpoint_credentials' function.
class RotateIngestEndpointCredentialsResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogs
    HlsIngest: HlsIngest
    Id: str
    IngressAccessLogs: IngressAccessLogs
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_channel' function.
class UpdateChannelResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogs
    HlsIngest: HlsIngest
    Id: str
    IngressAccessLogs: IngressAccessLogs
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CmafPackage(BaseValidatorModel):
    Encryption: Optional[CmafEncryptionOutput] = None
    HlsManifests: Optional[List[HlsManifest]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelection] = None


class DashPackageOutput(BaseValidatorModel):
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[DashEncryptionOutput] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    PeriodTriggers: Optional[List[Literal['ADS']]] = None
    Profile: Optional[ProfileType] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None
    StreamSelection: Optional[StreamSelection] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    UtcTiming: Optional[UtcTimingType] = None
    UtcTimingUri: Optional[str] = None


class HlsPackageOutput(BaseValidatorModel):
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[HlsEncryptionOutput] = None
    IncludeDvbSubtitles: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelection] = None
    UseAudioRenditionGroup: Optional[bool] = None


class MssPackageOutput(BaseValidatorModel):
    Encryption: Optional[MssEncryptionOutput] = None
    ManifestWindowSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelection] = None


class DashPackage(BaseValidatorModel):
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[DashEncryption] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    PeriodTriggers: Optional[List[Literal['ADS']]] = None
    Profile: Optional[ProfileType] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None
    StreamSelection: Optional[StreamSelection] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    UtcTiming: Optional[UtcTimingType] = None
    UtcTimingUri: Optional[str] = None


class HlsPackage(BaseValidatorModel):
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[HlsEncryption] = None
    IncludeDvbSubtitles: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelection] = None
    UseAudioRenditionGroup: Optional[bool] = None


class MssPackage(BaseValidatorModel):
    Encryption: Optional[MssEncryption] = None
    ManifestWindowSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelection] = None


class CmafEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderUnion
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None


# This class is the output for the 'list_channels' function.
class ListChannelsResponse(BaseValidatorModel):
    Channels: List[Channel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_origin_endpoint' function.
class CreateOriginEndpointResponse(BaseValidatorModel):
    Arn: str
    Authorization: Authorization
    ChannelId: str
    CmafPackage: CmafPackage
    CreatedAt: str
    DashPackage: DashPackageOutput
    Description: str
    HlsPackage: HlsPackageOutput
    Id: str
    ManifestName: str
    MssPackage: MssPackageOutput
    Origination: OriginationType
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_origin_endpoint' function.
class DescribeOriginEndpointResponse(BaseValidatorModel):
    Arn: str
    Authorization: Authorization
    ChannelId: str
    CmafPackage: CmafPackage
    CreatedAt: str
    DashPackage: DashPackageOutput
    Description: str
    HlsPackage: HlsPackageOutput
    Id: str
    ManifestName: str
    MssPackage: MssPackageOutput
    Origination: OriginationType
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
    ResponseMetadata: ResponseMetadata


class OriginEndpoint(BaseValidatorModel):
    Arn: Optional[str] = None
    Authorization: Optional[Authorization] = None
    ChannelId: Optional[str] = None
    CmafPackage: Optional[CmafPackage] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackageOutput] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackageOutput] = None
    Id: Optional[str] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackageOutput] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    TimeDelaySeconds: Optional[int] = None
    Url: Optional[str] = None
    Whitelist: Optional[List[str]] = None


# This class is the output for the 'update_origin_endpoint' function.
class UpdateOriginEndpointResponse(BaseValidatorModel):
    Arn: str
    Authorization: Authorization
    ChannelId: str
    CmafPackage: CmafPackage
    CreatedAt: str
    DashPackage: DashPackageOutput
    Description: str
    HlsPackage: HlsPackageOutput
    Id: str
    ManifestName: str
    MssPackage: MssPackageOutput
    Origination: OriginationType
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
    ResponseMetadata: ResponseMetadata

DashPackageUnion = Union[DashPackage, DashPackageOutput]

HlsPackageUnion = Union[HlsPackage, HlsPackageOutput]

MssPackageUnion = Union[MssPackage, MssPackageOutput]

CmafEncryptionUnion = Union[CmafEncryption, CmafEncryptionOutput]


# This class is the output for the 'list_origin_endpoints' function.
class ListOriginEndpointsResponse(BaseValidatorModel):
    OriginEndpoints: List[OriginEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CmafPackageCreateOrUpdateParameters(BaseValidatorModel):
    Encryption: Optional[CmafEncryptionUnion] = None
    HlsManifests: Optional[List[HlsManifestCreateOrUpdateParameters]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelection] = None


# This class is the input for the 'create_origin_endpoint' function.
class CreateOriginEndpointRequest(BaseValidatorModel):
    ChannelId: str
    Id: str
    Authorization: Optional[Authorization] = None
    CmafPackage: Optional[CmafPackageCreateOrUpdateParameters] = None
    DashPackage: Optional[DashPackageUnion] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackageUnion] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackageUnion] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    TimeDelaySeconds: Optional[int] = None
    Whitelist: Optional[List[str]] = None


# This class is the input for the 'update_origin_endpoint' function.
class UpdateOriginEndpointRequest(BaseValidatorModel):
    Id: str
    Authorization: Optional[Authorization] = None
    CmafPackage: Optional[CmafPackageCreateOrUpdateParameters] = None
    DashPackage: Optional[DashPackageUnion] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackageUnion] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackageUnion] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    TimeDelaySeconds: Optional[int] = None
    Whitelist: Optional[List[str]] = None