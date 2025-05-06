from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssetShallow(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[str] = None
    Id: Optional[str] = None
    PackagingGroupId: Optional[str] = None
    ResourceId: Optional[str] = None
    SourceArn: Optional[str] = None
    SourceRoleArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class Authorization(BaseValidatorModel):
    CdnIdentifierSecret: str
    SecretsRoleArn: str


class EgressAccessLogs(BaseValidatorModel):
    LogGroupName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateAssetRequest(BaseValidatorModel):
    Id: str
    PackagingGroupId: str
    SourceArn: str
    SourceRoleArn: str
    ResourceId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class EgressEndpoint(BaseValidatorModel):
    PackagingConfigurationId: Optional[str] = None
    Status: Optional[str] = None
    Url: Optional[str] = None


class StreamSelection(BaseValidatorModel):
    MaxVideoBitsPerSecond: Optional[int] = None
    MinVideoBitsPerSecond: Optional[int] = None
    StreamOrder: Optional[StreamOrderType] = None


class DeleteAssetRequest(BaseValidatorModel):
    Id: str


class DeletePackagingConfigurationRequest(BaseValidatorModel):
    Id: str


class DeletePackagingGroupRequest(BaseValidatorModel):
    Id: str


class DescribeAssetRequest(BaseValidatorModel):
    Id: str


class DescribePackagingConfigurationRequest(BaseValidatorModel):
    Id: str


class DescribePackagingGroupRequest(BaseValidatorModel):
    Id: str


class EncryptionContractConfiguration(BaseValidatorModel):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssetsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None


class ListPackagingConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PackagingGroupId: Optional[str] = None


class ListPackagingGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdatePackagingGroupRequest(BaseValidatorModel):
    Id: str
    Authorization: Optional[Authorization] = None


class ConfigureLogsRequest(BaseValidatorModel):
    Id: str
    EgressAccessLogs: Optional[EgressAccessLogs] = None


class CreatePackagingGroupRequest(BaseValidatorModel):
    Id: str
    Authorization: Optional[Authorization] = None
    EgressAccessLogs: Optional[EgressAccessLogs] = None
    Tags: Optional[Dict[str, str]] = None


class PackagingGroup(BaseValidatorModel):
    ApproximateAssetCount: Optional[int] = None
    Arn: Optional[str] = None
    Authorization: Optional[Authorization] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    EgressAccessLogs: Optional[EgressAccessLogs] = None
    Id: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ConfigureLogsResponse(BaseValidatorModel):
    Arn: str
    Authorization: Authorization
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogs
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreatePackagingGroupResponse(BaseValidatorModel):
    Arn: str
    Authorization: Authorization
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogs
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribePackagingGroupResponse(BaseValidatorModel):
    ApproximateAssetCount: int
    Arn: str
    Authorization: Authorization
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogs
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListAssetsResponse(BaseValidatorModel):
    Assets: List[AssetShallow]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdatePackagingGroupResponse(BaseValidatorModel):
    ApproximateAssetCount: int
    Arn: str
    Authorization: Authorization
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogs
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateAssetResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List[EgressEndpoint]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeAssetResponse(BaseValidatorModel):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List[EgressEndpoint]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DashManifest(BaseValidatorModel):
    ManifestLayout: Optional[ManifestLayoutType] = None
    ManifestName: Optional[str] = None
    MinBufferTimeSeconds: Optional[int] = None
    Profile: Optional[ProfileType] = None
    ScteMarkersSource: Optional[ScteMarkersSourceType] = None
    StreamSelection: Optional[StreamSelection] = None


class HlsManifest(BaseValidatorModel):
    AdMarkers: Optional[AdMarkersType] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    ManifestName: Optional[str] = None
    ProgramDateTimeIntervalSeconds: Optional[int] = None
    RepeatExtXKey: Optional[bool] = None
    StreamSelection: Optional[StreamSelection] = None


class MssManifest(BaseValidatorModel):
    ManifestName: Optional[str] = None
    StreamSelection: Optional[StreamSelection] = None


class SpekeKeyProviderOutput(BaseValidatorModel):
    RoleArn: str
    SystemIds: List[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None


class SpekeKeyProvider(BaseValidatorModel):
    RoleArn: str
    SystemIds: List[str]
    Url: str
    EncryptionContractConfiguration: Optional[EncryptionContractConfiguration] = None


class ListAssetsRequestPaginate(BaseValidatorModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackagingConfigurationsRequestPaginate(BaseValidatorModel):
    PackagingGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackagingGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackagingGroupsResponse(BaseValidatorModel):
    PackagingGroups: List[PackagingGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CmafEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput
    ConstantInitializationVector: Optional[str] = None


class DashEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput


class HlsEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None


class MssEncryptionOutput(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProviderOutput


class CmafEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider
    ConstantInitializationVector: Optional[str] = None


class DashEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider


class HlsEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider
    ConstantInitializationVector: Optional[str] = None
    EncryptionMethod: Optional[EncryptionMethodType] = None


class MssEncryption(BaseValidatorModel):
    SpekeKeyProvider: SpekeKeyProvider


class CmafPackageOutput(BaseValidatorModel):
    HlsManifests: List[HlsManifest]
    Encryption: Optional[CmafEncryptionOutput] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None


class DashPackageOutput(BaseValidatorModel):
    DashManifests: List[DashManifest]
    Encryption: Optional[DashEncryptionOutput] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[List[Literal['ADS']]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None


class HlsPackageOutput(BaseValidatorModel):
    HlsManifests: List[HlsManifest]
    Encryption: Optional[HlsEncryptionOutput] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None


class MssPackageOutput(BaseValidatorModel):
    MssManifests: List[MssManifest]
    Encryption: Optional[MssEncryptionOutput] = None
    SegmentDurationSeconds: Optional[int] = None


class CmafPackage(BaseValidatorModel):
    HlsManifests: List[HlsManifest]
    Encryption: Optional[CmafEncryption] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None


class DashPackage(BaseValidatorModel):
    DashManifests: List[DashManifest]
    Encryption: Optional[DashEncryption] = None
    IncludeEncoderConfigurationInSegments: Optional[bool] = None
    IncludeIframeOnlyStream: Optional[bool] = None
    PeriodTriggers: Optional[List[Literal['ADS']]] = None
    SegmentDurationSeconds: Optional[int] = None
    SegmentTemplateFormat: Optional[SegmentTemplateFormatType] = None


class HlsPackage(BaseValidatorModel):
    HlsManifests: List[HlsManifest]
    Encryption: Optional[HlsEncryption] = None
    IncludeDvbSubtitles: Optional[bool] = None
    SegmentDurationSeconds: Optional[int] = None
    UseAudioRenditionGroup: Optional[bool] = None


class MssPackage(BaseValidatorModel):
    MssManifests: List[MssManifest]
    Encryption: Optional[MssEncryption] = None
    SegmentDurationSeconds: Optional[int] = None


class CreatePackagingConfigurationResponse(BaseValidatorModel):
    Arn: str
    CmafPackage: CmafPackageOutput
    CreatedAt: str
    DashPackage: DashPackageOutput
    HlsPackage: HlsPackageOutput
    Id: str
    MssPackage: MssPackageOutput
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribePackagingConfigurationResponse(BaseValidatorModel):
    Arn: str
    CmafPackage: CmafPackageOutput
    CreatedAt: str
    DashPackage: DashPackageOutput
    HlsPackage: HlsPackageOutput
    Id: str
    MssPackage: MssPackageOutput
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PackagingConfiguration(BaseValidatorModel):
    Arn: Optional[str] = None
    CmafPackage: Optional[CmafPackageOutput] = None
    CreatedAt: Optional[str] = None
    DashPackage: Optional[DashPackageOutput] = None
    HlsPackage: Optional[HlsPackageOutput] = None
    Id: Optional[str] = None
    MssPackage: Optional[MssPackageOutput] = None
    PackagingGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

CmafPackageUnion = Union[CmafPackage, CmafPackageOutput]

DashPackageUnion = Union[DashPackage, DashPackageOutput]

HlsPackageUnion = Union[HlsPackage, HlsPackageOutput]

MssPackageUnion = Union[MssPackage, MssPackageOutput]


class ListPackagingConfigurationsResponse(BaseValidatorModel):
    PackagingConfigurations: List[PackagingConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreatePackagingConfigurationRequest(BaseValidatorModel):
    Id: str
    PackagingGroupId: str
    CmafPackage: Optional[CmafPackageUnion] = None
    DashPackage: Optional[DashPackageUnion] = None
    HlsPackage: Optional[HlsPackageUnion] = None
    MssPackage: Optional[MssPackageUnion] = None
    Tags: Optional[Dict[str, str]] = None