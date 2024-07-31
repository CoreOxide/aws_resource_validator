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
from aws_resource_validator.pydantic_models.mediapackage_constants import *

class AuthorizationTypeDef(BaseModel):
    CdnIdentifierSecret: str
    SecretsRoleArn: str

class EgressAccessLogsTypeDef(BaseModel):
    LogGroupName: Optional[str] = None

class IngressAccessLogsTypeDef(BaseModel):
    LogGroupName: Optional[str] = None

class HlsManifestCreateOrUpdateParametersTypeDef(BaseModel):
    Id: str
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[Sequence[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None

class StreamSelectionTypeDef(BaseModel):
    MaxVideoBitsPerSecond: Optional[int] = None
    MinVideoBitsPerSecond: Optional[int] = None
    StreamOrder: Optional[StreamOrderType] = None

class HlsManifestTypeDef(BaseModel):
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateChannelRequestRequestTypeDef(BaseModel):
    Id: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class S3DestinationTypeDef(BaseModel):
    BucketName: str
    ManifestKey: str
    RoleArn: str

class DeleteChannelRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteOriginEndpointRequestRequestTypeDef(BaseModel):
    Id: str

class DescribeChannelRequestRequestTypeDef(BaseModel):
    Id: str

class DescribeHarvestJobRequestRequestTypeDef(BaseModel):
    Id: str

class DescribeOriginEndpointRequestRequestTypeDef(BaseModel):
    Id: str

class EncryptionContractConfigurationTypeDef(BaseModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class IngestEndpointTypeDef(BaseModel):
    Id: Optional[str] = None
    Password: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHarvestJobsRequestRequestTypeDef(BaseModel):
    IncludeChannelId: Optional[str] = None
    IncludeStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOriginEndpointsRequestRequestTypeDef(BaseModel):
    ChannelId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class RotateChannelCredentialsRequestRequestTypeDef(BaseModel):
    Id: str

class RotateIngestEndpointCredentialsRequestRequestTypeDef(BaseModel):
    Id: str
    IngestEndpointId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateChannelRequestRequestTypeDef(BaseModel):
    Id: str
    Description: Optional[str] = None

class ConfigureLogsRequestRequestTypeDef(BaseModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    IngressAccessLogs: Optional[IngressAccessLogsTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHarvestJobRequestRequestTypeDef(BaseModel):
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3DestinationTypeDef
    StartTime: str

class CreateHarvestJobResponseTypeDef(BaseModel):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3DestinationTypeDef
    StartTime: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHarvestJobResponseTypeDef(BaseModel):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3DestinationTypeDef
    StartTime: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class HarvestJobTypeDef(BaseModel):
    Arn: Optional[str] = None
    ChannelId: Optional[str] = None
    CreatedAt: Optional[str] = None
    EndTime: Optional[str] = None
    Id: Optional[str] = None
    OriginEndpointId: Optional[str] = None
    S3Destination: Optional[S3DestinationTypeDef] = None
    StartTime: Optional[str] = None
    Status: Optional[StatusType] = None

class SpekeKeyProviderPaginatorTypeDef(BaseModel):
    ResourceId: str
    RoleArn: str
    SystemIds: List[str]
    Url: str
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class SpekeKeyProviderTypeDef(BaseModel):
    ResourceId: str
    RoleArn: str
    SystemIds: Sequence[str]
    Url: str
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class HlsIngestTypeDef(BaseModel):
    IngestEndpoints: Optional[List[IngestEndpointTypeDef]] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHarvestJobsRequestListHarvestJobsPaginateTypeDef(BaseModel):
    IncludeChannelId: Optional[str] = None
    IncludeStatus: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef(BaseModel):
    ChannelId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHarvestJobsResponseTypeDef(BaseModel):
    HarvestJobs: List[HarvestJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CmafEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class DashEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    KeyRotationIntervalSeconds: Optional[int] = None

class HlsEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None

class MssEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef

class CmafEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class DashEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    KeyRotationIntervalSeconds: Optional[int] = None

class HlsEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None

class MssEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class ChannelTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[str] = None
    Description: Optional[str] = None
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    HlsIngest: Optional[HlsIngestTypeDef] = None
    Id: Optional[str] = None
    IngressAccessLogs: Optional[IngressAccessLogsTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class ConfigureLogsResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RotateChannelCredentialsResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RotateIngestEndpointCredentialsResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CmafPackagePaginatorTypeDef(BaseModel):
    Encryption: Optional[CmafEncryptionPaginatorTypeDef] = None
    HlsManifests: Optional[List[HlsManifestTypeDef]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class DashPackagePaginatorTypeDef(BaseModel):
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[DashEncryptionPaginatorTypeDef] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    PeriodTriggers: Optional[List[Literal["ADS"]]] = None
    Profile: Optional[ProfileType] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    UtcTiming: Optional[UtcTimingType] = None
    UtcTimingUri: Optional[str] = None

class HlsPackagePaginatorTypeDef(BaseModel):
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[List[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[HlsEncryptionPaginatorTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None
    UseAudioRenditionGroup: Optional[bool] = None

class MssPackagePaginatorTypeDef(BaseModel):
    Encryption: Optional[MssEncryptionPaginatorTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class CmafPackageCreateOrUpdateParametersTypeDef(BaseModel):
    Encryption: Optional[CmafEncryptionTypeDef] = None
    HlsManifests: Optional[Sequence[HlsManifestCreateOrUpdateParametersTypeDef]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class CmafPackageTypeDef(BaseModel):
    Encryption: Optional[CmafEncryptionTypeDef] = None
    HlsManifests: Optional[List[HlsManifestTypeDef]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class DashPackageTypeDef(BaseModel):
    AdTriggers: Optional[Sequence[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[DashEncryptionTypeDef] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestWindowSeconds: Optional[int] = None
    MinBufferTimeSeconds: Optional[int] = None
    MinUpdatePeriodSeconds: Optional[int] = None
    PeriodTriggers: Optional[Sequence[Literal["ADS"]]] = None
    Profile: Optional[ProfileType] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None
    SuggestedPresentationDelaySeconds: Optional[int] = None
    UtcTiming: Optional[UtcTimingType] = None
    UtcTimingUri: Optional[str] = None

class HlsPackageTypeDef(BaseModel):
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[Sequence[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    Encryption: Optional[HlsEncryptionTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None
    UseAudioRenditionGroup: Optional[bool] = None

class MssPackageTypeDef(BaseModel):
    Encryption: Optional[MssEncryptionTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class ListChannelsResponseTypeDef(BaseModel):
    Channels: List[ChannelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginEndpointPaginatorTypeDef(BaseModel):
    Arn: Optional[str] = None
    Authorization: Optional[AuthorizationTypeDef] = None
    ChannelId: Optional[str] = None
    CmafPackage: Optional[CmafPackagePaginatorTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackagePaginatorTypeDef] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackagePaginatorTypeDef] = None
    Id: Optional[str] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackagePaginatorTypeDef] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    TimeDelaySeconds: Optional[int] = None
    Url: Optional[str] = None
    Whitelist: Optional[List[str]] = None

class CreateOriginEndpointRequestRequestTypeDef(BaseModel):
    ChannelId: str
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None
    CmafPackage: Optional[CmafPackageCreateOrUpdateParametersTypeDef] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    TimeDelaySeconds: Optional[int] = None
    Whitelist: Optional[Sequence[str]] = None

class CreateOriginEndpointResponseTypeDef(BaseModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    ChannelId: str
    CmafPackage: CmafPackageTypeDef
    CreatedAt: str
    DashPackage: DashPackageTypeDef
    Description: str
    HlsPackage: HlsPackageTypeDef
    Id: str
    ManifestName: str
    MssPackage: MssPackageTypeDef
    Origination: OriginationType
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOriginEndpointResponseTypeDef(BaseModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    ChannelId: str
    CmafPackage: CmafPackageTypeDef
    CreatedAt: str
    DashPackage: DashPackageTypeDef
    Description: str
    HlsPackage: HlsPackageTypeDef
    Id: str
    ManifestName: str
    MssPackage: MssPackageTypeDef
    Origination: OriginationType
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class OriginEndpointTypeDef(BaseModel):
    Arn: Optional[str] = None
    Authorization: Optional[AuthorizationTypeDef] = None
    ChannelId: Optional[str] = None
    CmafPackage: Optional[CmafPackageTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    Id: Optional[str] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    TimeDelaySeconds: Optional[int] = None
    Url: Optional[str] = None
    Whitelist: Optional[List[str]] = None

class UpdateOriginEndpointRequestRequestTypeDef(BaseModel):
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None
    CmafPackage: Optional[CmafPackageCreateOrUpdateParametersTypeDef] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    Description: Optional[str] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    ManifestName: Optional[str] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    Origination: Optional[OriginationType] = None
    StartoverWindowSeconds: Optional[int] = None
    TimeDelaySeconds: Optional[int] = None
    Whitelist: Optional[Sequence[str]] = None

class UpdateOriginEndpointResponseTypeDef(BaseModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    ChannelId: str
    CmafPackage: CmafPackageTypeDef
    CreatedAt: str
    DashPackage: DashPackageTypeDef
    Description: str
    HlsPackage: HlsPackageTypeDef
    Id: str
    ManifestName: str
    MssPackage: MssPackageTypeDef
    Origination: OriginationType
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOriginEndpointsResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    OriginEndpoints: List[OriginEndpointPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOriginEndpointsResponseTypeDef(BaseModel):
    NextToken: str
    OriginEndpoints: List[OriginEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

