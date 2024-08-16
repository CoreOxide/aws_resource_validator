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
from aws_resource_validator.pydantic_models.mediapackage_constants import *

class AuthorizationTypeDef(BaseValidatorModel):
    CdnIdentifierSecret: str
    SecretsRoleArn: str

class EgressAccessLogsTypeDef(BaseValidatorModel):
    LogGroupName: Optional[str] = None

class IngressAccessLogsTypeDef(BaseValidatorModel):
    LogGroupName: Optional[str] = None

class HlsManifestCreateOrUpdateParametersTypeDef(BaseValidatorModel):
    Id: str
    AdMarkers: Optional[AdMarkersType] = None
    AdTriggers: Optional[Sequence[AdTriggersElementType]] = None
    AdsOnDeliveryRestrictions: Optional[AdsOnDeliveryRestrictionsType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    PlaylistType: Optional[PlaylistTypeType] = None
    PlaylistWindowSeconds: Optional[int] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None

class StreamSelectionTypeDef(BaseValidatorModel):
    MaxVideoBitsPerSecond: Optional[int] = None
    MinVideoBitsPerSecond: Optional[int] = None
    StreamOrder: Optional[StreamOrderType] = None

class HlsManifestTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class S3DestinationTypeDef(BaseValidatorModel):
    BucketName: str
    ManifestKey: str
    RoleArn: str

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribeChannelRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribeHarvestJobRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribeOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class EncryptionContractConfigurationTypeDef(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class IngestEndpointTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Password: Optional[str] = None
    Url: Optional[str] = None
    Username: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHarvestJobsRequestRequestTypeDef(BaseValidatorModel):
    IncludeChannelId: Optional[str] = None
    IncludeStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOriginEndpointsRequestRequestTypeDef(BaseValidatorModel):
    ChannelId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class RotateChannelCredentialsRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class RotateIngestEndpointCredentialsRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    IngestEndpointId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Description: Optional[str] = None

class ConfigureLogsRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    IngressAccessLogs: Optional[IngressAccessLogsTypeDef] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHarvestJobRequestRequestTypeDef(BaseValidatorModel):
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: S3DestinationTypeDef
    StartTime: str

class CreateHarvestJobResponseTypeDef(BaseValidatorModel):
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

class DescribeHarvestJobResponseTypeDef(BaseValidatorModel):
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

class HarvestJobTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ChannelId: Optional[str] = None
    CreatedAt: Optional[str] = None
    EndTime: Optional[str] = None
    Id: Optional[str] = None
    OriginEndpointId: Optional[str] = None
    S3Destination: Optional[S3DestinationTypeDef] = None
    StartTime: Optional[str] = None
    Status: Optional[StatusType] = None

class SpekeKeyProviderPaginatorTypeDef(BaseValidatorModel):
    ResourceId: str
    RoleArn: str
    SystemIds: List[str]
    Url: str
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class SpekeKeyProviderTypeDef(BaseValidatorModel):
    ResourceId: str
    RoleArn: str
    SystemIds: Sequence[str]
    Url: str
    CertificateArn: Optional[str] = None
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class HlsIngestTypeDef(BaseValidatorModel):
    IngestEndpoints: Optional[List[IngestEndpointTypeDef]] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHarvestJobsRequestListHarvestJobsPaginateTypeDef(BaseValidatorModel):
    IncludeChannelId: Optional[str] = None
    IncludeStatus: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef(BaseValidatorModel):
    ChannelId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHarvestJobsResponseTypeDef(BaseValidatorModel):
    HarvestJobs: List[HarvestJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CmafEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class DashEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    KeyRotationIntervalSeconds: Optional[int] = None

class HlsEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None

class MssEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef

class CmafEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[CmafEncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None

class DashEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    KeyRotationIntervalSeconds: Optional[int] = None

class HlsEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None
    KeyRotationIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None

class MssEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class ChannelTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[str] = None
    Description: Optional[str] = None
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    HlsIngest: Optional[HlsIngestTypeDef] = None
    Id: Optional[str] = None
    IngressAccessLogs: Optional[IngressAccessLogsTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class ConfigureLogsResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RotateChannelCredentialsResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RotateIngestEndpointCredentialsResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    Description: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    HlsIngest: HlsIngestTypeDef
    Id: str
    IngressAccessLogs: IngressAccessLogsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CmafPackagePaginatorTypeDef(BaseValidatorModel):
    Encryption: Optional[CmafEncryptionPaginatorTypeDef] = None
    HlsManifests: Optional[List[HlsManifestTypeDef]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class DashPackagePaginatorTypeDef(BaseValidatorModel):
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

class HlsPackagePaginatorTypeDef(BaseValidatorModel):
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

class MssPackagePaginatorTypeDef(BaseValidatorModel):
    Encryption: Optional[MssEncryptionPaginatorTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class CmafPackageCreateOrUpdateParametersTypeDef(BaseValidatorModel):
    Encryption: Optional[CmafEncryptionTypeDef] = None
    HlsManifests: Optional[Sequence[HlsManifestCreateOrUpdateParametersTypeDef]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class CmafPackageTypeDef(BaseValidatorModel):
    Encryption: Optional[CmafEncryptionTypeDef] = None
    HlsManifests: Optional[List[HlsManifestTypeDef]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentPrefix: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class DashPackageTypeDef(BaseValidatorModel):
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

class HlsPackageTypeDef(BaseValidatorModel):
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

class MssPackageTypeDef(BaseValidatorModel):
    Encryption: Optional[MssEncryptionTypeDef] = None
    ManifestWindowSeconds: Optional[int] = None
    SegmentDurationSeconds: Optional[int] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OriginEndpointPaginatorTypeDef(BaseValidatorModel):
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

class CreateOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
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

class CreateOriginEndpointResponseTypeDef(BaseValidatorModel):
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

class DescribeOriginEndpointResponseTypeDef(BaseValidatorModel):
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

class OriginEndpointTypeDef(BaseValidatorModel):
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

class UpdateOriginEndpointRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateOriginEndpointResponseTypeDef(BaseValidatorModel):
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

class ListOriginEndpointsResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    OriginEndpoints: List[OriginEndpointPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOriginEndpointsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    OriginEndpoints: List[OriginEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

