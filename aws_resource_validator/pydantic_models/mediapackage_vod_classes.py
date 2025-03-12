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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateAssetRequestTypeDef(BaseValidatorModel):
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


class DeleteAssetRequestTypeDef(BaseValidatorModel):
    Id: str


class DeletePackagingConfigurationRequestTypeDef(BaseValidatorModel):
    Id: str


class DeletePackagingGroupRequestTypeDef(BaseValidatorModel):
    Id: str


class DescribeAssetRequestTypeDef(BaseValidatorModel):
    Id: str


class DescribePackagingConfigurationRequestTypeDef(BaseValidatorModel):
    Id: str


class DescribePackagingGroupRequestTypeDef(BaseValidatorModel):
    Id: str


class EncryptionContractConfigurationTypeDef(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssetsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None


class ListPackagingConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None


class ListPackagingGroupsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdatePackagingGroupRequestTypeDef(BaseValidatorModel):
    Id: str
    Authorization: Optional[AuthorizationTypeDef] = None


class ConfigureLogsRequestTypeDef(BaseValidatorModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogsTypeDef] = None


class CreatePackagingGroupRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class SpekeKeyProviderOutputTypeDef(BaseValidatorModel):
    RoleArn: str
    SystemIds: List[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None


class SpekeKeyProviderTypeDef(BaseValidatorModel):
    RoleArn: str
    SystemIds: Sequence[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfigurationTypeDef] = None


class ListAssetsRequestPaginateTypeDef(BaseValidatorModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPackagingConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPackagingGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPackagingGroupsResponseTypeDef(BaseValidatorModel):
    PackagingGroups: List[PackagingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CmafEncryptionOutputTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: Optional[str] = None


class DashEncryptionOutputTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef


class HlsEncryptionOutputTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None


class MssEncryptionOutputTypeDef(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef


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


class CmafPackageOutputTypeDef(BaseValidatorModel):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: Optional[CmafEncryptionOutputTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None


class DashPackageOutputTypeDef(BaseValidatorModel):
    DashManifests: List[DashManifestTypeDef]
    Encryption: Optional[DashEncryptionOutputTypeDef] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[List[Literal["ADS"]]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None


class HlsPackageOutputTypeDef(BaseValidatorModel):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: Optional[HlsEncryptionOutputTypeDef] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None


class MssPackageOutputTypeDef(BaseValidatorModel):
    MssManifests: List[MssManifestTypeDef]
    Encryption: Optional[MssEncryptionOutputTypeDef] = None
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


class CreatePackagingConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    CmafPackage: CmafPackageOutputTypeDef
    CreatedAt: str
    DashPackage: DashPackageOutputTypeDef
    HlsPackage: HlsPackageOutputTypeDef
    Id: str
    MssPackage: MssPackageOutputTypeDef
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePackagingConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    CmafPackage: CmafPackageOutputTypeDef
    CreatedAt: str
    DashPackage: DashPackageOutputTypeDef
    HlsPackage: HlsPackageOutputTypeDef
    Id: str
    MssPackage: MssPackageOutputTypeDef
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PackagingConfigurationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CmafPackage: Optional[CmafPackageOutputTypeDef] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackageOutputTypeDef] = None
    HlsPackage: Optional[HlsPackageOutputTypeDef] = None
    Id: Optional[str] = None
    MssPackage: Optional[MssPackageOutputTypeDef] = None
    PackagingGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListPackagingConfigurationsResponseTypeDef(BaseValidatorModel):
    PackagingConfigurations: List[PackagingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MssPackageUnionTypeDef(BaseValidatorModel):
    pass


class DashPackageUnionTypeDef(BaseValidatorModel):
    pass


class CmafPackageUnionTypeDef(BaseValidatorModel):
    pass


class HlsPackageUnionTypeDef(BaseValidatorModel):
    pass


class CreatePackagingConfigurationRequestTypeDef(BaseValidatorModel):
    Id: str
    PackagingGroupId: str
    CmafPackage: Optional[CmafPackageUnionTypeDef] = None
    DashPackage: Optional[DashPackageUnionTypeDef] = None
    HlsPackage: Optional[HlsPackageUnionTypeDef] = None
    MssPackage: Optional[MssPackageUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


