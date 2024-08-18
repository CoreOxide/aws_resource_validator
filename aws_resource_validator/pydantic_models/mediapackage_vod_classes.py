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
from aws_resource_validator.pydantic_models.mediapackage_vod_constants import *

class AssetShallowTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[str] = None
    Id: Optional[str] = None
    PackagingGroupId: Optional[str] = None
    ResourceId: Optional[str] = None
    SourceArn: Optional[str] = None
    SourceRoleArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class AuthorizationTypeDef(BaseValidatorModel):
    CdnIdentifierSecret: str
    SecretsRoleArn: str

class EgressAccessLogsTypeDef(BaseValidatorModel):
    LogGroupName: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateAssetRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    PackagingGroupId: str
    SourceArn: str
    SourceRoleArn: str
    ResourceId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class EgressEndpointTypeDef(BaseValidatorModel):
    PackagingConfigurationId: Optional[str] = None
    Status: Optional[str] = None
    Url: Optional[str] = None

class StreamSelectionTypeDef(BaseValidatorModel):
    MaxVideoBitsPerSecond: Optional[int] = None
    MinVideoBitsPerSecond: Optional[int] = None
    StreamOrder: Optional[StreamOrderType] = None

class DeleteAssetRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeletePackagingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeletePackagingGroupRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribeAssetRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribePackagingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DescribePackagingGroupRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class EncryptionContractConfigurationTypeDef(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssetsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None

class ListPackagingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None

class ListPackagingGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdatePackagingGroupRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None

class ConfigureLogsRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None

class CreatePackagingGroupRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class PackagingGroupTypeDef(BaseValidatorModel):
    ApproximateAssetCount: Optional[int] = None
    Arn: Optional[str] = None
    Authorization: Optional[AuthorizationTypeDef] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None
    Id: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ConfigureLogsResponseTypeDef(BaseValidatorModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackagingGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagingGroupResponseTypeDef(BaseValidatorModel):
    ApproximateAssetCount: int
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsResponseTypeDef(BaseValidatorModel):
    Assets: List[AssetShallowTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackagingGroupResponseTypeDef(BaseValidatorModel):
    ApproximateAssetCount: int
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssetResponseTypeDef(BaseValidatorModel):
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

class DescribeAssetResponseTypeDef(BaseValidatorModel):
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

class DashManifestTypeDef(BaseValidatorModel):
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestName: Optional[str] = None
    MinBufferTimeSeconds: Optional[int] = None
    Profile: Optional[ProfileType] = None
    ScteMarkersSource: Optional[ScteMarkersSourceType] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class HlsManifestTypeDef(BaseValidatorModel):
    AdMarkers: Optional[AdMarkersType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class MssManifestTypeDef(BaseValidatorModel):
    ManifestName: Optional[str] = None
    StreamSelection: Optional[StreamSelectionTypeDef] = None

class SpekeKeyProviderPaginatorTypeDef(BaseValidatorModel):
    RoleArn: str
    SystemIds: List[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class SpekeKeyProviderTypeDef(BaseValidatorModel):
    RoleArn: str
    SystemIds: Sequence[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None

class ListAssetsRequestListAssetsPaginateTypeDef(BaseValidatorModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef(BaseValidatorModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagingGroupsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PackagingGroups: List[PackagingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CmafEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None

class DashEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef

class HlsEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None

class MssEncryptionPaginatorTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderPaginatorTypeDef

class CmafEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None

class DashEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class HlsEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None

class MssEncryptionTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class CmafPackagePaginatorTypeDef(BaseValidatorModel):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: Optional[CmafEncryptionPaginatorTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None

class DashPackagePaginatorTypeDef(BaseValidatorModel):
    DashManifests: List[DashManifestTypeDef]
    Encryption: Optional[DashEncryptionPaginatorTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[List[Literal["ADS"]]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None

class HlsPackagePaginatorTypeDef(BaseValidatorModel):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: Optional[HlsEncryptionPaginatorTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None

class MssPackagePaginatorTypeDef(BaseValidatorModel):
    MssManifests: List[MssManifestTypeDef]
    Encryption: Optional[MssEncryptionPaginatorTypeDef] = None
    SegmentDurationSeconds: Optional[int] = None

class CmafPackageTypeDef(BaseValidatorModel):
    HlsManifests: Sequence[HlsManifestTypeDef]
    Encryption: Optional[CmafEncryptionTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None

class DashPackageTypeDef(BaseValidatorModel):
    DashManifests: Sequence[DashManifestTypeDef]
    Encryption: Optional[DashEncryptionTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[Sequence[Literal["ADS"]]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None

class HlsPackageTypeDef(BaseValidatorModel):
    HlsManifests: Sequence[HlsManifestTypeDef]
    Encryption: Optional[HlsEncryptionTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None

class MssPackageTypeDef(BaseValidatorModel):
    MssManifests: Sequence[MssManifestTypeDef]
    Encryption: Optional[MssEncryptionTypeDef] = None
    SegmentDurationSeconds: Optional[int] = None

class PackagingConfigurationPaginatorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CmafPackage: Optional[CmafPackagePaginatorTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackagePaginatorTypeDef] = None
    HlsPackage: Optional[HlsPackagePaginatorTypeDef] = None
    Id: Optional[str] = None
    MssPackage: Optional[MssPackagePaginatorTypeDef] = None
    PackagingGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class CreatePackagingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    PackagingGroupId: str
    CmafPackage: Optional[CmafPackageTypeDef] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreatePackagingConfigurationResponseTypeDef(BaseValidatorModel):
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

class DescribePackagingConfigurationResponseTypeDef(BaseValidatorModel):
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

class PackagingConfigurationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CmafPackage: Optional[CmafPackageTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackageTypeDef] = None
    HlsPackage: Optional[HlsPackageTypeDef] = None
    Id: Optional[str] = None
    MssPackage: Optional[MssPackageTypeDef] = None
    PackagingGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListPackagingConfigurationsResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    PackagingConfigurations: List[PackagingConfigurationPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagingConfigurationsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PackagingConfigurations: List[PackagingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

