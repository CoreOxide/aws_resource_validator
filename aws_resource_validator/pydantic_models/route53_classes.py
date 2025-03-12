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
from aws_resource_validator.pydantic_models.route53_constants import *

class ActivateKeySigningKeyRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class ChangeInfoTypeDef(BaseValidatorModel):
    Id: str
    Status: ChangeStatusType
    SubmittedAt: datetime
    Comment: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AlarmIdentifierTypeDef(BaseValidatorModel):
    Region: CloudWatchRegionType
    Name: str


class AliasTargetTypeDef(BaseValidatorModel):
    HostedZoneId: str
    DNSName: str
    EvaluateTargetHealth: bool


class VPCTypeDef(BaseValidatorModel):
    VPCRegion: Optional[VPCRegionType] = None
    VPCId: Optional[str] = None


class CidrCollectionChangeTypeDef(BaseValidatorModel):
    LocationName: str
    Action: CidrCollectionChangeActionType
    CidrList: Sequence[str]


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class CidrBlockSummaryTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    LocationName: Optional[str] = None


class CidrCollectionTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None


class CidrRoutingConfigTypeDef(BaseValidatorModel):
    CollectionId: str
    LocationName: str


class DimensionTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class CollectionSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None


class CoordinatesTypeDef(BaseValidatorModel):
    Latitude: str
    Longitude: str


class CreateCidrCollectionRequestTypeDef(BaseValidatorModel):
    Name: str
    CallerReference: str


class HostedZoneConfigTypeDef(BaseValidatorModel):
    Comment: Optional[str] = None
    PrivateZone: Optional[bool] = None


class DelegationSetTypeDef(BaseValidatorModel):
    NameServers: List[str]
    Id: Optional[str] = None
    CallerReference: Optional[str] = None


class CreateKeySigningKeyRequestTypeDef(BaseValidatorModel):
    CallerReference: str
    HostedZoneId: str
    KeyManagementServiceArn: str
    Name: str
    Status: str


class KeySigningKeyTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    KmsArn: Optional[str] = None
    Flag: Optional[int] = None
    SigningAlgorithmMnemonic: Optional[str] = None
    SigningAlgorithmType: Optional[int] = None
    DigestAlgorithmMnemonic: Optional[str] = None
    DigestAlgorithmType: Optional[int] = None
    KeyTag: Optional[int] = None
    DigestValue: Optional[str] = None
    PublicKey: Optional[str] = None
    DSRecord: Optional[str] = None
    DNSKEYRecord: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    LastModifiedDate: Optional[datetime] = None


class CreateQueryLoggingConfigRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


class QueryLoggingConfigTypeDef(BaseValidatorModel):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


class CreateReusableDelegationSetRequestTypeDef(BaseValidatorModel):
    CallerReference: str
    HostedZoneId: Optional[str] = None


class CreateTrafficPolicyInstanceRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int


class TrafficPolicyInstanceTypeDef(BaseValidatorModel):
    Id: str
    HostedZoneId: str
    Name: str
    TTL: int
    State: str
    Message: str
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    TrafficPolicyType: RRTypeType


class CreateTrafficPolicyRequestTypeDef(BaseValidatorModel):
    Name: str
    Document: str
    Comment: Optional[str] = None


class CreateTrafficPolicyVersionRequestTypeDef(BaseValidatorModel):
    Id: str
    Document: str
    Comment: Optional[str] = None


class DNSSECStatusTypeDef(BaseValidatorModel):
    ServeSignature: Optional[str] = None
    StatusMessage: Optional[str] = None


class DeactivateKeySigningKeyRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class DeleteCidrCollectionRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteHealthCheckRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str


class DeleteHostedZoneRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteKeySigningKeyRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class DeleteQueryLoggingConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteReusableDelegationSetRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteTrafficPolicyInstanceRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteTrafficPolicyRequestTypeDef(BaseValidatorModel):
    Id: str
    Version: int


class DisableHostedZoneDNSSECRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str


class EnableHostedZoneDNSSECRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str


class GeoLocationDetailsTypeDef(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    ContinentName: Optional[str] = None
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None
    SubdivisionCode: Optional[str] = None
    SubdivisionName: Optional[str] = None


class GeoLocationTypeDef(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None


class GetChangeRequestTypeDef(BaseValidatorModel):
    Id: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetDNSSECRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str


class GetGeoLocationRequestTypeDef(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None


class GetHealthCheckLastFailureReasonRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str


class GetHealthCheckRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str


class GetHealthCheckStatusRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str


class GetHostedZoneRequestTypeDef(BaseValidatorModel):
    Id: str


class GetQueryLoggingConfigRequestTypeDef(BaseValidatorModel):
    Id: str


class GetReusableDelegationSetRequestTypeDef(BaseValidatorModel):
    Id: str


class GetTrafficPolicyInstanceRequestTypeDef(BaseValidatorModel):
    Id: str


class GetTrafficPolicyRequestTypeDef(BaseValidatorModel):
    Id: str
    Version: int


class StatusReportTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    CheckedTime: Optional[datetime] = None


class LinkedServiceTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    Description: Optional[str] = None


class HostedZoneOwnerTypeDef(BaseValidatorModel):
    OwningAccount: Optional[str] = None
    OwningService: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCidrBlocksRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ListCidrCollectionsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ListCidrLocationsRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class LocationSummaryTypeDef(BaseValidatorModel):
    LocationName: Optional[str] = None


class ListGeoLocationsRequestTypeDef(BaseValidatorModel):
    StartContinentCode: Optional[str] = None
    StartCountryCode: Optional[str] = None
    StartSubdivisionCode: Optional[str] = None
    MaxItems: Optional[str] = None


class ListHealthChecksRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListHostedZonesByNameRequestTypeDef(BaseValidatorModel):
    DNSName: Optional[str] = None
    HostedZoneId: Optional[str] = None
    MaxItems: Optional[str] = None


class ListHostedZonesByVPCRequestTypeDef(BaseValidatorModel):
    VPCId: str
    VPCRegion: VPCRegionType
    MaxItems: Optional[str] = None
    NextToken: Optional[str] = None


class ListHostedZonesRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal["PrivateHostedZone"]] = None


class ListQueryLoggingConfigsRequestTypeDef(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ListResourceRecordSetsRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    StartRecordName: Optional[str] = None
    StartRecordType: Optional[RRTypeType] = None
    StartRecordIdentifier: Optional[str] = None
    MaxItems: Optional[str] = None


class ListReusableDelegationSetsRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str


class ListTagsForResourcesRequestTypeDef(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceIds: Sequence[str]


class ListTrafficPoliciesRequestTypeDef(BaseValidatorModel):
    TrafficPolicyIdMarker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyInstancesByHostedZoneRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyInstancesByPolicyRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyInstancesRequestTypeDef(BaseValidatorModel):
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyVersionsRequestTypeDef(BaseValidatorModel):
    Id: str
    TrafficPolicyVersionMarker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListVPCAssociationAuthorizationsRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ResourceRecordTypeDef(BaseValidatorModel):
    Value: str


class TestDNSAnswerRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    RecordName: str
    RecordType: RRTypeType
    ResolverIP: Optional[str] = None
    EDNS0ClientSubnetIP: Optional[str] = None
    EDNS0ClientSubnetMask: Optional[str] = None


class UpdateHostedZoneCommentRequestTypeDef(BaseValidatorModel):
    Id: str
    Comment: Optional[str] = None


class UpdateTrafficPolicyCommentRequestTypeDef(BaseValidatorModel):
    Id: str
    Version: int
    Comment: str


class UpdateTrafficPolicyInstanceRequestTypeDef(BaseValidatorModel):
    Id: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int


class ActivateKeySigningKeyResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateVPCWithHostedZoneResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChangeCidrCollectionResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class ChangeResourceRecordSetsResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeactivateKeySigningKeyResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteHostedZoneResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteKeySigningKeyResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisableHostedZoneDNSSECResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateVPCFromHostedZoneResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnableHostedZoneDNSSECResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AccountLimitTypeDef(BaseValidatorModel):
    pass


class GetAccountLimitResponseTypeDef(BaseValidatorModel):
    Limit: AccountLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetChangeResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCheckerIpRangesResponseTypeDef(BaseValidatorModel):
    CheckerIpRanges: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetHealthCheckCountResponseTypeDef(BaseValidatorModel):
    HealthCheckCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetHostedZoneCountResponseTypeDef(BaseValidatorModel):
    HostedZoneCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrafficPolicyInstanceCountResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstanceCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateHealthCheckRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str
    HealthCheckVersion: Optional[int] = None
    IPAddress: Optional[str] = None
    Port: Optional[int] = None
    ResourcePath: Optional[str] = None
    FullyQualifiedDomainName: Optional[str] = None
    SearchString: Optional[str] = None
    FailureThreshold: Optional[int] = None
    Inverted: Optional[bool] = None
    Disabled: Optional[bool] = None
    HealthThreshold: Optional[int] = None
    ChildHealthChecks: Optional[Sequence[str]] = None
    EnableSNI: Optional[bool] = None
    Regions: Optional[Sequence[HealthCheckRegionType]] = None
    AlarmIdentifier: Optional[AlarmIdentifierTypeDef] = None
    InsufficientDataHealthStatus: Optional[InsufficientDataHealthStatusType] = None
    ResetElements: Optional[Sequence[ResettableElementNameType]] = None


class AssociateVPCWithHostedZoneRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: Optional[str] = None


class CreateVPCAssociationAuthorizationRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef


class CreateVPCAssociationAuthorizationResponseTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVPCAssociationAuthorizationRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef


class DisassociateVPCFromHostedZoneRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: Optional[str] = None


class ListVPCAssociationAuthorizationsResponseTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ChangeCidrCollectionRequestTypeDef(BaseValidatorModel):
    Id: str
    Changes: Sequence[CidrCollectionChangeTypeDef]
    CollectionVersion: Optional[int] = None


class ChangeTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str
    AddTags: Optional[Sequence[TagTypeDef]] = None
    RemoveTagKeys: Optional[Sequence[str]] = None


class ResourceTagSetTypeDef(BaseValidatorModel):
    ResourceType: Optional[TagResourceTypeType] = None
    ResourceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None


class ListCidrBlocksResponseTypeDef(BaseValidatorModel):
    CidrBlocks: List[CidrBlockSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CloudWatchAlarmConfigurationTypeDef(BaseValidatorModel):
    EvaluationPeriods: int
    Threshold: float
    ComparisonOperator: ComparisonOperatorType
    Period: int
    MetricName: str
    Namespace: str
    Statistic: StatisticType
    Dimensions: Optional[List[DimensionTypeDef]] = None


class ListCidrCollectionsResponseTypeDef(BaseValidatorModel):
    CidrCollections: List[CollectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GeoProximityLocationTypeDef(BaseValidatorModel):
    AWSRegion: Optional[str] = None
    LocalZoneGroup: Optional[str] = None
    Coordinates: Optional[CoordinatesTypeDef] = None
    Bias: Optional[int] = None


class CreateHostedZoneRequestTypeDef(BaseValidatorModel):
    Name: str
    CallerReference: str
    VPC: Optional[VPCTypeDef] = None
    HostedZoneConfig: Optional[HostedZoneConfigTypeDef] = None
    DelegationSetId: Optional[str] = None


class CreateReusableDelegationSetResponseTypeDef(BaseValidatorModel):
    DelegationSet: DelegationSetTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetReusableDelegationSetResponseTypeDef(BaseValidatorModel):
    DelegationSet: DelegationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListReusableDelegationSetsResponseTypeDef(BaseValidatorModel):
    DelegationSets: List[DelegationSetTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateKeySigningKeyResponseTypeDef(BaseValidatorModel):
    ChangeInfo: ChangeInfoTypeDef
    KeySigningKey: KeySigningKeyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateQueryLoggingConfigResponseTypeDef(BaseValidatorModel):
    QueryLoggingConfig: QueryLoggingConfigTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryLoggingConfigResponseTypeDef(BaseValidatorModel):
    QueryLoggingConfig: QueryLoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListQueryLoggingConfigsResponseTypeDef(BaseValidatorModel):
    QueryLoggingConfigs: List[QueryLoggingConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateTrafficPolicyInstanceResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrafficPolicyInstanceResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTrafficPolicyInstancesByHostedZoneResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTrafficPolicyInstancesByPolicyResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTrafficPolicyInstancesResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTrafficPolicyInstanceResponseTypeDef(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TrafficPolicyTypeDef(BaseValidatorModel):
    pass


class CreateTrafficPolicyResponseTypeDef(BaseValidatorModel):
    TrafficPolicy: TrafficPolicyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrafficPolicyVersionResponseTypeDef(BaseValidatorModel):
    TrafficPolicy: TrafficPolicyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrafficPolicyResponseTypeDef(BaseValidatorModel):
    TrafficPolicy: TrafficPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTrafficPolicyVersionsResponseTypeDef(BaseValidatorModel):
    TrafficPolicies: List[TrafficPolicyTypeDef]
    IsTruncated: bool
    TrafficPolicyVersionMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTrafficPolicyCommentResponseTypeDef(BaseValidatorModel):
    TrafficPolicy: TrafficPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDNSSECResponseTypeDef(BaseValidatorModel):
    Status: DNSSECStatusTypeDef
    KeySigningKeys: List[KeySigningKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetGeoLocationResponseTypeDef(BaseValidatorModel):
    GeoLocationDetails: GeoLocationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListGeoLocationsResponseTypeDef(BaseValidatorModel):
    GeoLocationDetailsList: List[GeoLocationDetailsTypeDef]
    IsTruncated: bool
    NextContinentCode: str
    NextCountryCode: str
    NextSubdivisionCode: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetChangeRequestWaitTypeDef(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class HostedZoneLimitTypeDef(BaseValidatorModel):
    pass


class GetHostedZoneLimitResponseTypeDef(BaseValidatorModel):
    Limit: HostedZoneLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef


class ReusableDelegationSetLimitTypeDef(BaseValidatorModel):
    pass


class GetReusableDelegationSetLimitResponseTypeDef(BaseValidatorModel):
    Limit: ReusableDelegationSetLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef


class HealthCheckObservationTypeDef(BaseValidatorModel):
    Region: Optional[HealthCheckRegionType] = None
    IPAddress: Optional[str] = None
    StatusReport: Optional[StatusReportTypeDef] = None


class HostedZoneTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    CallerReference: str
    Config: Optional[HostedZoneConfigTypeDef] = None
    ResourceRecordSetCount: Optional[int] = None
    LinkedService: Optional[LinkedServiceTypeDef] = None


class HostedZoneSummaryTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str
    Owner: HostedZoneOwnerTypeDef


class ListCidrBlocksRequestPaginateTypeDef(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCidrCollectionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCidrLocationsRequestPaginateTypeDef(BaseValidatorModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHealthChecksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHostedZonesRequestPaginateTypeDef(BaseValidatorModel):
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal["PrivateHostedZone"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueryLoggingConfigsRequestPaginateTypeDef(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceRecordSetsRequestPaginateTypeDef(BaseValidatorModel):
    HostedZoneId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVPCAssociationAuthorizationsRequestPaginateTypeDef(BaseValidatorModel):
    HostedZoneId: str
    MaxResults: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCidrLocationsResponseTypeDef(BaseValidatorModel):
    CidrLocations: List[LocationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TrafficPolicySummaryTypeDef(BaseValidatorModel):
    pass


class ListTrafficPoliciesResponseTypeDef(BaseValidatorModel):
    TrafficPolicySummaries: List[TrafficPolicySummaryTypeDef]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTagSet: ResourceTagSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourcesResponseTypeDef(BaseValidatorModel):
    ResourceTagSets: List[ResourceTagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class HealthCheckConfigOutputTypeDef(BaseValidatorModel):
    pass


class HealthCheckTypeDef(BaseValidatorModel):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigOutputTypeDef
    HealthCheckVersion: int
    LinkedService: Optional[LinkedServiceTypeDef] = None
    CloudWatchAlarmConfiguration: Optional[CloudWatchAlarmConfigurationTypeDef] = None


class GetHealthCheckLastFailureReasonResponseTypeDef(BaseValidatorModel):
    HealthCheckObservations: List[HealthCheckObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetHealthCheckStatusResponseTypeDef(BaseValidatorModel):
    HealthCheckObservations: List[HealthCheckObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHostedZoneResponseTypeDef(BaseValidatorModel):
    HostedZone: HostedZoneTypeDef
    ChangeInfo: ChangeInfoTypeDef
    DelegationSet: DelegationSetTypeDef
    VPC: VPCTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetHostedZoneResponseTypeDef(BaseValidatorModel):
    HostedZone: HostedZoneTypeDef
    DelegationSet: DelegationSetTypeDef
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListHostedZonesByNameResponseTypeDef(BaseValidatorModel):
    HostedZones: List[HostedZoneTypeDef]
    DNSName: str
    HostedZoneId: str
    IsTruncated: bool
    NextDNSName: str
    NextHostedZoneId: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListHostedZonesResponseTypeDef(BaseValidatorModel):
    HostedZones: List[HostedZoneTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateHostedZoneCommentResponseTypeDef(BaseValidatorModel):
    HostedZone: HostedZoneTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListHostedZonesByVPCResponseTypeDef(BaseValidatorModel):
    HostedZoneSummaries: List[HostedZoneSummaryTypeDef]
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class HealthCheckConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateHealthCheckRequestTypeDef(BaseValidatorModel):
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigUnionTypeDef


class CreateHealthCheckResponseTypeDef(BaseValidatorModel):
    HealthCheck: HealthCheckTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetHealthCheckResponseTypeDef(BaseValidatorModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListHealthChecksResponseTypeDef(BaseValidatorModel):
    HealthChecks: List[HealthCheckTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateHealthCheckResponseTypeDef(BaseValidatorModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceRecordSetOutputTypeDef(BaseValidatorModel):
    pass


class ListResourceRecordSetsResponseTypeDef(BaseValidatorModel):
    ResourceRecordSets: List[ResourceRecordSetOutputTypeDef]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceRecordSetUnionTypeDef(BaseValidatorModel):
    pass


class ChangeTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ResourceRecordSet: ResourceRecordSetUnionTypeDef


class ChangeBatchTypeDef(BaseValidatorModel):
    Changes: Sequence[ChangeTypeDef]
    Comment: Optional[str] = None


class ChangeResourceRecordSetsRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    ChangeBatch: ChangeBatchTypeDef


