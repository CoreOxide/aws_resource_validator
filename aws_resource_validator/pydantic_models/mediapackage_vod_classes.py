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
from aws_resource_validator.pydantic_models.mediapackage_vod_constants import *

class AssetShallowTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[str] = None
    Id: Optional[str] = None
    PackagingGroupId: Optional[str] = None
    ResourceId: Optional[str] = None
    SourceArn: Optional[str] = None
    SourceRoleArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class AuthorizationTypeDef(BaseModel):
    CdnIdentifierSecret: str
    SecretsRoleArn: str

class EgressAccessLogsTypeDef(BaseModel):
    LogGroupName: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateAssetRequestRequestTypeDef(BaseModel):
    Id: str
    PackagingGroupId: str
    SourceArn: str
    SourceRoleArn: str
    ResourceId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class EgressEndpointTypeDef(BaseModel):
    PackagingConfigurationId: Optional[str] = None
    Status: Optional[str] = None
    Url: Optional[str] = None

class StreamSelectionTypeDef(BaseModel):
    MaxVideoBitsPerSecond: Optional[int] = None
    MinVideoBitsPerSecond: Optional[int] = None
    StreamOrder: Optional[StreamOrderType] = None

class DeleteAssetRequestRequestTypeDef(BaseModel):
    Id: str

class DeletePackagingConfigurationRequestRequestTypeDef(BaseModel):
    Id: str

class DeletePackagingGroupRequestRequestTypeDef(BaseModel):
    Id: str

class DescribeAssetRequestRequestTypeDef(BaseModel):
    Id: str

class DescribePackagingConfigurationRequestRequestTypeDef(BaseModel):
    Id: str

class DescribePackagingGroupRequestRequestTypeDef(BaseModel):
    Id: str

class EncryptionContractConfigurationTypeDef(BaseModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssetsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None

class ListPackagingConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None

class ListPackagingGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdatePackagingGroupRequestRequestTypeDef(BaseModel):
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None

class ConfigureLogsRequestRequestTypeDef(BaseModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None

class CreatePackagingGroupRequestRequestTypeDef(BaseModel):
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class PackagingGroupTypeDef(BaseModel):
    ApproximateAssetCount: Optional[int] = None
    Arn: Optional[str] = None
    Authorization: Optional[AuthorizationTypeDef] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    Id: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ConfigureLogsResponseTypeDef(BaseModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackagingGroupResponseTypeDef(BaseModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagingGroupResponseTypeDef(BaseModel):
    ApproximateAssetCount: int
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsResponseTypeDef(BaseModel):
    Assets: List[AssetShallowTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackagingGroupResponseTypeDef(BaseModel):
    ApproximateAssetCount: int
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssetResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List[EgressEndpointTypeDef]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAssetResponseTypeDef(BaseModel):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List[EgressEndpointTypeDef]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DashManifestTypeDef(BaseModel):
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestName: Optional[str] = None
    MinBufferTimeSeconds: Optional[int] = None
    Profile: Optional[ProfileType] = None
    ScteMarkersSource: Optional[ScteMarkersSourceType] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class HlsManifestTypeDef(BaseModel):
    AdMarkers: Optional[AdMarkersType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class MssManifestTypeDef(BaseModel):
    ManifestName: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class SpekeKeyProviderPaginatorTypeDef(BaseModel):
    RoleArn: str
    SystemIds: List[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class SpekeKeyProviderTypeDef(BaseModel):
    RoleArn: str
    SystemIds: Sequence[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class ListAssetsRequestListAssetsPaginateTypeDef(BaseModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef(BaseModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagingGroupsResponseTypeDef(BaseModel):
    NextToken: str
    PackagingGroups: List[PackagingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CmafEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None

class DashEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef

class HlsEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None

class MssEncryptionPaginatorTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef

class CmafEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None

class DashEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class HlsEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None

class MssEncryptionTypeDef(BaseModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class CmafPackagePaginatorTypeDef(BaseModel):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: Optional[CmafEncryptionPaginatorTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None

class DashPackagePaginatorTypeDef(BaseModel):
    DashManifests: List[DashManifestTypeDef]
    Encryption: Optional[DashEncryptionPaginatorTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[List[Literal["ADS"]]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None

class HlsPackagePaginatorTypeDef(BaseModel):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: Optional[HlsEncryptionPaginatorTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None

class MssPackagePaginatorTypeDef(BaseModel):
    MssManifests: List[MssManifestTypeDef]
    Encryption: Optional[MssEncryptionPaginatorTypeDef] = None
    SegmentDurationSeconds: Optional[int] = None

class CmafPackageTypeDef(BaseModel):
    HlsManifests: Sequence[HlsManifestTypeDef]
    Encryption: Optional[CmafEncryptionTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None

class DashPackageTypeDef(BaseModel):
    DashManifests: Sequence[DashManifestTypeDef]
    Encryption: Optional[DashEncryptionTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[Sequence[Literal["ADS"]]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None

class HlsPackageTypeDef(BaseModel):
    HlsManifests: Sequence[HlsManifestTypeDef]
    Encryption: Optional[HlsEncryptionTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None

class MssPackageTypeDef(BaseModel):
    MssManifests: Sequence[MssManifestTypeDef]
    Encryption: Optional[MssEncryptionTypeDef] = None
    SegmentDurationSeconds: Optional[int] = None

class PackagingConfigurationPaginatorTypeDef(BaseModel):
    Arn: Optional[str] = None
    CmafPackage: Optional[CmafPackagePaginatorTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackagePaginatorTypeDef] = None
    HlsPackage: Optional[HlsPackagePaginatorTypeDef] = None
    Id: Optional[str] = None
    MssPackage: Optional[MssPackagePaginatorTypeDef] = None
    PackagingGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class CreatePackagingConfigurationRequestRequestTypeDef(BaseModel):
    Id: str
    PackagingGroupId: str
    CmafPackage: Optional[CmafPackageTypeDef] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreatePackagingConfigurationResponseTypeDef(BaseModel):
    Arn: str
    CmafPackage: CmafPackageTypeDef
    CreatedAt: str
    DashPackage: DashPackageTypeDef
    HlsPackage: HlsPackageTypeDef
    Id: str
    MssPackage: MssPackageTypeDef
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagingConfigurationResponseTypeDef(BaseModel):
    Arn: str
    CmafPackage: CmafPackageTypeDef
    CreatedAt: str
    DashPackage: DashPackageTypeDef
    HlsPackage: HlsPackageTypeDef
    Id: str
    MssPackage: MssPackageTypeDef
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PackagingConfigurationTypeDef(BaseModel):
    Arn: Optional[str] = None
    CmafPackage: Optional[CmafPackageTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    Id: Optional[str] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    PackagingGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListPackagingConfigurationsResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    PackagingConfigurations: List[PackagingConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagingConfigurationsResponseTypeDef(BaseModel):
    NextToken: str
    PackagingConfigurations: List[PackagingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

