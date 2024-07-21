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
from aws_resource_validator.pydantic_models.route53_constants import *

class AccountLimitTypeDef(BaseModel):
    Type: AccountLimitTypeType
    Value: int

class ActivateKeySigningKeyRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    Name: str

class ChangeInfoTypeDef(BaseModel):
    Id: str
    Status: ChangeStatusType
    SubmittedAt: datetime
    Comment: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AlarmIdentifierTypeDef(BaseModel):
    Region: CloudWatchRegionType
    Name: str

class AliasTargetTypeDef(BaseModel):
    HostedZoneId: str
    DNSName: str
    EvaluateTargetHealth: bool

class VPCTypeDef(BaseModel):
    VPCRegion: Optional[VPCRegionType] = None
    VPCId: Optional[str] = None

class CidrCollectionChangeTypeDef(BaseModel):
    LocationName: str
    Action: CidrCollectionChangeActionType
    CidrList: Sequence[str]

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class CidrBlockSummaryTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    LocationName: Optional[str] = None

class CidrCollectionTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None

class CidrRoutingConfigTypeDef(BaseModel):
    CollectionId: str
    LocationName: str

class DimensionTypeDef(BaseModel):
    Name: str
    Value: str

class CollectionSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None

class CoordinatesTypeDef(BaseModel):
    Latitude: str
    Longitude: str

class CreateCidrCollectionRequestRequestTypeDef(BaseModel):
    Name: str
    CallerReference: str

class HostedZoneConfigTypeDef(BaseModel):
    Comment: Optional[str] = None
    PrivateZone: Optional[bool] = None

class DelegationSetTypeDef(BaseModel):
    NameServers: List[str]
    Id: Optional[str] = None
    CallerReference: Optional[str] = None

class CreateKeySigningKeyRequestRequestTypeDef(BaseModel):
    CallerReference: str
    HostedZoneId: str
    KeyManagementServiceArn: str
    Name: str
    Status: str

class KeySigningKeyTypeDef(BaseModel):
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

class CreateQueryLoggingConfigRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str

class QueryLoggingConfigTypeDef(BaseModel):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str

class CreateReusableDelegationSetRequestRequestTypeDef(BaseModel):
    CallerReference: str
    HostedZoneId: Optional[str] = None

class CreateTrafficPolicyInstanceRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    Name: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int

class TrafficPolicyInstanceTypeDef(BaseModel):
    Id: str
    HostedZoneId: str
    Name: str
    TTL: int
    State: str
    Message: str
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    TrafficPolicyType: RRTypeType

class CreateTrafficPolicyRequestRequestTypeDef(BaseModel):
    Name: str
    Document: str
    Comment: Optional[str] = None

class TrafficPolicyTypeDef(BaseModel):
    Id: str
    Version: int
    Name: str
    Type: RRTypeType
    Document: str
    Comment: Optional[str] = None

class CreateTrafficPolicyVersionRequestRequestTypeDef(BaseModel):
    Id: str
    Document: str
    Comment: Optional[str] = None

class DNSSECStatusTypeDef(BaseModel):
    ServeSignature: Optional[str] = None
    StatusMessage: Optional[str] = None

class DeactivateKeySigningKeyRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    Name: str

class DeleteCidrCollectionRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteHealthCheckRequestRequestTypeDef(BaseModel):
    HealthCheckId: str

class DeleteHostedZoneRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteKeySigningKeyRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    Name: str

class DeleteQueryLoggingConfigRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteReusableDelegationSetRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteTrafficPolicyInstanceRequestRequestTypeDef(BaseModel):
    Id: str

class DeleteTrafficPolicyRequestRequestTypeDef(BaseModel):
    Id: str
    Version: int

class DisableHostedZoneDNSSECRequestRequestTypeDef(BaseModel):
    HostedZoneId: str

class EnableHostedZoneDNSSECRequestRequestTypeDef(BaseModel):
    HostedZoneId: str

class GeoLocationDetailsTypeDef(BaseModel):
    ContinentCode: Optional[str] = None
    ContinentName: Optional[str] = None
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None
    SubdivisionCode: Optional[str] = None
    SubdivisionName: Optional[str] = None

class GeoLocationTypeDef(BaseModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None

class GetAccountLimitRequestRequestTypeDef(BaseModel):
    Type: AccountLimitTypeType

class GetChangeRequestRequestTypeDef(BaseModel):
    Id: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetDNSSECRequestRequestTypeDef(BaseModel):
    HostedZoneId: str

class GetGeoLocationRequestRequestTypeDef(BaseModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None

class GetHealthCheckLastFailureReasonRequestRequestTypeDef(BaseModel):
    HealthCheckId: str

class GetHealthCheckRequestRequestTypeDef(BaseModel):
    HealthCheckId: str

class GetHealthCheckStatusRequestRequestTypeDef(BaseModel):
    HealthCheckId: str

class GetHostedZoneLimitRequestRequestTypeDef(BaseModel):
    Type: HostedZoneLimitTypeType
    HostedZoneId: str

class HostedZoneLimitTypeDef(BaseModel):
    Type: HostedZoneLimitTypeType
    Value: int

class GetHostedZoneRequestRequestTypeDef(BaseModel):
    Id: str

class GetQueryLoggingConfigRequestRequestTypeDef(BaseModel):
    Id: str

class GetReusableDelegationSetLimitRequestRequestTypeDef(BaseModel):
    Type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"]
    DelegationSetId: str

class ReusableDelegationSetLimitTypeDef(BaseModel):
    Type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"]
    Value: int

class GetReusableDelegationSetRequestRequestTypeDef(BaseModel):
    Id: str

class GetTrafficPolicyInstanceRequestRequestTypeDef(BaseModel):
    Id: str

class GetTrafficPolicyRequestRequestTypeDef(BaseModel):
    Id: str
    Version: int

class StatusReportTypeDef(BaseModel):
    Status: Optional[str] = None
    CheckedTime: Optional[datetime] = None

class LinkedServiceTypeDef(BaseModel):
    ServicePrincipal: Optional[str] = None
    Description: Optional[str] = None

class HostedZoneOwnerTypeDef(BaseModel):
    OwningAccount: Optional[str] = None
    OwningService: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCidrBlocksRequestRequestTypeDef(BaseModel):
    CollectionId: str
    LocationName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ListCidrCollectionsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ListCidrLocationsRequestRequestTypeDef(BaseModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class LocationSummaryTypeDef(BaseModel):
    LocationName: Optional[str] = None

class ListGeoLocationsRequestRequestTypeDef(BaseModel):
    StartContinentCode: Optional[str] = None
    StartCountryCode: Optional[str] = None
    StartSubdivisionCode: Optional[str] = None
    MaxItems: Optional[str] = None

class ListHealthChecksRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListHostedZonesByNameRequestRequestTypeDef(BaseModel):
    DNSName: Optional[str] = None
    HostedZoneId: Optional[str] = None
    MaxItems: Optional[str] = None

class ListHostedZonesByVPCRequestRequestTypeDef(BaseModel):
    VPCId: str
    VPCRegion: VPCRegionType
    MaxItems: Optional[str] = None
    NextToken: Optional[str] = None

class ListHostedZonesRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal["PrivateHostedZone"]] = None

class ListQueryLoggingConfigsRequestRequestTypeDef(BaseModel):
    HostedZoneId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ListResourceRecordSetsRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    StartRecordName: Optional[str] = None
    StartRecordType: Optional[RRTypeType] = None
    StartRecordIdentifier: Optional[str] = None
    MaxItems: Optional[str] = None

class ListReusableDelegationSetsRequestRequestTypeDef(BaseModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceType: TagResourceTypeType
    ResourceId: str

class ListTagsForResourcesRequestRequestTypeDef(BaseModel):
    ResourceType: TagResourceTypeType
    ResourceIds: Sequence[str]

class ListTrafficPoliciesRequestRequestTypeDef(BaseModel):
    TrafficPolicyIdMarker: Optional[str] = None
    MaxItems: Optional[str] = None

class TrafficPolicySummaryTypeDef(BaseModel):
    Id: str
    Name: str
    Type: RRTypeType
    LatestVersion: int
    TrafficPolicyCount: int

class ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None

class ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef(BaseModel):
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None

class ListTrafficPolicyInstancesRequestRequestTypeDef(BaseModel):
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None

class ListTrafficPolicyVersionsRequestRequestTypeDef(BaseModel):
    Id: str
    TrafficPolicyVersionMarker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListVPCAssociationAuthorizationsRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ResourceRecordTypeDef(BaseModel):
    Value: str

class TestDNSAnswerRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    RecordName: str
    RecordType: RRTypeType
    ResolverIP: Optional[str] = None
    EDNS0ClientSubnetIP: Optional[str] = None
    EDNS0ClientSubnetMask: Optional[str] = None

class UpdateHostedZoneCommentRequestRequestTypeDef(BaseModel):
    Id: str
    Comment: Optional[str] = None

class UpdateTrafficPolicyCommentRequestRequestTypeDef(BaseModel):
    Id: str
    Version: int
    Comment: str

class UpdateTrafficPolicyInstanceRequestRequestTypeDef(BaseModel):
    Id: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int

class ActivateKeySigningKeyResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateVPCWithHostedZoneResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeCidrCollectionResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeResourceRecordSetsResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateKeySigningKeyResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHostedZoneResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeySigningKeyResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableHostedZoneDNSSECResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateVPCFromHostedZoneResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableHostedZoneDNSSECResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountLimitResponseTypeDef(BaseModel):
    Limit: AccountLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCheckerIpRangesResponseTypeDef(BaseModel):
    CheckerIpRanges: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetHealthCheckCountResponseTypeDef(BaseModel):
    HealthCheckCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostedZoneCountResponseTypeDef(BaseModel):
    HostedZoneCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyInstanceCountResponseTypeDef(BaseModel):
    TrafficPolicyInstanceCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class TestDNSAnswerResponseTypeDef(BaseModel):
    Nameserver: str
    RecordName: str
    RecordType: RRTypeType
    RecordData: List[str]
    ResponseCode: str
    Protocol: str
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckConfigPaginatorTypeDef(BaseModel):
    Type: HealthCheckTypeType
    IPAddress: Optional[str] = None
    Port: Optional[int] = None
    ResourcePath: Optional[str] = None
    FullyQualifiedDomainName: Optional[str] = None
    SearchString: Optional[str] = None
    RequestInterval: Optional[int] = None
    FailureThreshold: Optional[int] = None
    MeasureLatency: Optional[bool] = None
    Inverted: Optional[bool] = None
    Disabled: Optional[bool] = None
    HealthThreshold: Optional[int] = None
    ChildHealthChecks: Optional[List[str]] = None
    EnableSNI: Optional[bool] = None
    Regions: Optional[List[HealthCheckRegionType]] = None
    AlarmIdentifier: Optional[AlarmIdentifierTypeDef] = None
    InsufficientDataHealthStatus: Optional[InsufficientDataHealthStatusType] = None
    RoutingControlArn: Optional[str] = None

class HealthCheckConfigTypeDef(BaseModel):
    Type: HealthCheckTypeType
    IPAddress: Optional[str] = None
    Port: Optional[int] = None
    ResourcePath: Optional[str] = None
    FullyQualifiedDomainName: Optional[str] = None
    SearchString: Optional[str] = None
    RequestInterval: Optional[int] = None
    FailureThreshold: Optional[int] = None
    MeasureLatency: Optional[bool] = None
    Inverted: Optional[bool] = None
    Disabled: Optional[bool] = None
    HealthThreshold: Optional[int] = None
    ChildHealthChecks: Optional[Sequence[str]] = None
    EnableSNI: Optional[bool] = None
    Regions: Optional[Sequence[HealthCheckRegionType]] = None
    AlarmIdentifier: Optional[AlarmIdentifierTypeDef] = None
    InsufficientDataHealthStatus: Optional[InsufficientDataHealthStatusType] = None
    RoutingControlArn: Optional[str] = None

class UpdateHealthCheckRequestRequestTypeDef(BaseModel):
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

class AssociateVPCWithHostedZoneRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: Optional[str] = None

class CreateVPCAssociationAuthorizationRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    VPC: VPCTypeDef

class CreateVPCAssociationAuthorizationResponseTypeDef(BaseModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVPCAssociationAuthorizationRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    VPC: VPCTypeDef

class DisassociateVPCFromHostedZoneRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: Optional[str] = None

class ListVPCAssociationAuthorizationsResponseTypeDef(BaseModel):
    HostedZoneId: str
    NextToken: str
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeCidrCollectionRequestRequestTypeDef(BaseModel):
    Id: str
    Changes: Sequence[CidrCollectionChangeTypeDef]
    CollectionVersion: Optional[int] = None

class ChangeTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceType: TagResourceTypeType
    ResourceId: str
    AddTags: Optional[Sequence[TagTypeDef]] = None
    RemoveTagKeys: Optional[Sequence[str]] = None

class ResourceTagSetTypeDef(BaseModel):
    ResourceType: Optional[TagResourceTypeType] = None
    ResourceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ListCidrBlocksResponseTypeDef(BaseModel):
    NextToken: str
    CidrBlocks: List[CidrBlockSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCidrCollectionResponseTypeDef(BaseModel):
    Collection: CidrCollectionTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloudWatchAlarmConfigurationTypeDef(BaseModel):
    EvaluationPeriods: int
    Threshold: float
    ComparisonOperator: ComparisonOperatorType
    Period: int
    MetricName: str
    Namespace: str
    Statistic: StatisticType
    Dimensions: Optional[List[DimensionTypeDef]] = None

class ListCidrCollectionsResponseTypeDef(BaseModel):
    NextToken: str
    CidrCollections: List[CollectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GeoProximityLocationTypeDef(BaseModel):
    AWSRegion: Optional[str] = None
    LocalZoneGroup: Optional[str] = None
    Coordinates: Optional[CoordinatesTypeDef] = None
    Bias: Optional[int] = None

class CreateHostedZoneRequestRequestTypeDef(BaseModel):
    Name: str
    CallerReference: str
    VPC: Optional[VPCTypeDef] = None
    HostedZoneConfig: Optional[HostedZoneConfigTypeDef] = None
    DelegationSetId: Optional[str] = None

class CreateReusableDelegationSetResponseTypeDef(BaseModel):
    DelegationSet: DelegationSetTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReusableDelegationSetResponseTypeDef(BaseModel):
    DelegationSet: DelegationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReusableDelegationSetsResponseTypeDef(BaseModel):
    DelegationSets: List[DelegationSetTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKeySigningKeyResponseTypeDef(BaseModel):
    ChangeInfo: ChangeInfoTypeDef
    KeySigningKey: KeySigningKeyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueryLoggingConfigResponseTypeDef(BaseModel):
    QueryLoggingConfig: QueryLoggingConfigTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryLoggingConfigResponseTypeDef(BaseModel):
    QueryLoggingConfig: QueryLoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueryLoggingConfigsResponseTypeDef(BaseModel):
    QueryLoggingConfigs: List[QueryLoggingConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyInstanceResponseTypeDef(BaseModel):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyInstanceResponseTypeDef(BaseModel):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyInstancesByHostedZoneResponseTypeDef(BaseModel):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyInstancesByPolicyResponseTypeDef(BaseModel):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyInstancesResponseTypeDef(BaseModel):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrafficPolicyInstanceResponseTypeDef(BaseModel):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyResponseTypeDef(BaseModel):
    TrafficPolicy: TrafficPolicyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyVersionResponseTypeDef(BaseModel):
    TrafficPolicy: TrafficPolicyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyResponseTypeDef(BaseModel):
    TrafficPolicy: TrafficPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyVersionsResponseTypeDef(BaseModel):
    TrafficPolicies: List[TrafficPolicyTypeDef]
    IsTruncated: bool
    TrafficPolicyVersionMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrafficPolicyCommentResponseTypeDef(BaseModel):
    TrafficPolicy: TrafficPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDNSSECResponseTypeDef(BaseModel):
    Status: DNSSECStatusTypeDef
    KeySigningKeys: List[KeySigningKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeoLocationResponseTypeDef(BaseModel):
    GeoLocationDetails: GeoLocationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGeoLocationsResponseTypeDef(BaseModel):
    GeoLocationDetailsList: List[GeoLocationDetailsTypeDef]
    IsTruncated: bool
    NextContinentCode: str
    NextCountryCode: str
    NextSubdivisionCode: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeRequestResourceRecordSetsChangedWaitTypeDef(BaseModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetHostedZoneLimitResponseTypeDef(BaseModel):
    Limit: HostedZoneLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetReusableDelegationSetLimitResponseTypeDef(BaseModel):
    Limit: ReusableDelegationSetLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckObservationTypeDef(BaseModel):
    Region: Optional[HealthCheckRegionType] = None
    IPAddress: Optional[str] = None
    StatusReport: Optional[StatusReportTypeDef] = None

class HostedZoneTypeDef(BaseModel):
    Id: str
    Name: str
    CallerReference: str
    Config: Optional[HostedZoneConfigTypeDef] = None
    ResourceRecordSetCount: Optional[int] = None
    LinkedService: Optional[LinkedServiceTypeDef] = None

class HostedZoneSummaryTypeDef(BaseModel):
    HostedZoneId: str
    Name: str
    Owner: HostedZoneOwnerTypeDef

class ListCidrBlocksRequestListCidrBlocksPaginateTypeDef(BaseModel):
    CollectionId: str
    LocationName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCidrCollectionsRequestListCidrCollectionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCidrLocationsRequestListCidrLocationsPaginateTypeDef(BaseModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHealthChecksRequestListHealthChecksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHostedZonesRequestListHostedZonesPaginateTypeDef(BaseModel):
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal["PrivateHostedZone"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateTypeDef(BaseModel):
    HostedZoneId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceRecordSetsRequestListResourceRecordSetsPaginateTypeDef(BaseModel):
    HostedZoneId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateTypeDef(BaseModel):
    HostedZoneId: str
    MaxResults: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCidrLocationsResponseTypeDef(BaseModel):
    NextToken: str
    CidrLocations: List[LocationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPoliciesResponseTypeDef(BaseModel):
    TrafficPolicySummaries: List[TrafficPolicySummaryTypeDef]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHealthCheckRequestRequestTypeDef(BaseModel):
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceTagSet: ResourceTagSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourcesResponseTypeDef(BaseModel):
    ResourceTagSets: List[ResourceTagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckPaginatorTypeDef(BaseModel):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigPaginatorTypeDef
    HealthCheckVersion: int
    LinkedService: Optional[LinkedServiceTypeDef] = None
    CloudWatchAlarmConfiguration: Optional[CloudWatchAlarmConfigurationTypeDef] = None

class HealthCheckTypeDef(BaseModel):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigTypeDef
    HealthCheckVersion: int
    LinkedService: Optional[LinkedServiceTypeDef] = None
    CloudWatchAlarmConfiguration: Optional[CloudWatchAlarmConfigurationTypeDef] = None

class ResourceRecordSetPaginatorTypeDef(BaseModel):
    Name: str
    Type: RRTypeType
    SetIdentifier: Optional[str] = None
    Weight: Optional[int] = None
    Region: Optional[ResourceRecordSetRegionType] = None
    GeoLocation: Optional[GeoLocationTypeDef] = None
    Failover: Optional[ResourceRecordSetFailoverType] = None
    MultiValueAnswer: Optional[bool] = None
    TTL: Optional[int] = None
    ResourceRecords: Optional[List[ResourceRecordTypeDef]] = None
    AliasTarget: Optional[AliasTargetTypeDef] = None
    HealthCheckId: Optional[str] = None
    TrafficPolicyInstanceId: Optional[str] = None
    CidrRoutingConfig: Optional[CidrRoutingConfigTypeDef] = None
    GeoProximityLocation: Optional[GeoProximityLocationTypeDef] = None

class ResourceRecordSetTypeDef(BaseModel):
    Name: str
    Type: RRTypeType
    SetIdentifier: Optional[str] = None
    Weight: Optional[int] = None
    Region: Optional[ResourceRecordSetRegionType] = None
    GeoLocation: Optional[GeoLocationTypeDef] = None
    Failover: Optional[ResourceRecordSetFailoverType] = None
    MultiValueAnswer: Optional[bool] = None
    TTL: Optional[int] = None
    ResourceRecords: Optional[Sequence[ResourceRecordTypeDef]] = None
    AliasTarget: Optional[AliasTargetTypeDef] = None
    HealthCheckId: Optional[str] = None
    TrafficPolicyInstanceId: Optional[str] = None
    CidrRoutingConfig: Optional[CidrRoutingConfigTypeDef] = None
    GeoProximityLocation: Optional[GeoProximityLocationTypeDef] = None

class GetHealthCheckLastFailureReasonResponseTypeDef(BaseModel):
    HealthCheckObservations: List[HealthCheckObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetHealthCheckStatusResponseTypeDef(BaseModel):
    HealthCheckObservations: List[HealthCheckObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostedZoneResponseTypeDef(BaseModel):
    HostedZone: HostedZoneTypeDef
    ChangeInfo: ChangeInfoTypeDef
    DelegationSet: DelegationSetTypeDef
    VPC: VPCTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostedZoneResponseTypeDef(BaseModel):
    HostedZone: HostedZoneTypeDef
    DelegationSet: DelegationSetTypeDef
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHostedZonesByNameResponseTypeDef(BaseModel):
    HostedZones: List[HostedZoneTypeDef]
    DNSName: str
    HostedZoneId: str
    IsTruncated: bool
    NextDNSName: str
    NextHostedZoneId: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHostedZonesResponseTypeDef(BaseModel):
    HostedZones: List[HostedZoneTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHostedZoneCommentResponseTypeDef(BaseModel):
    HostedZone: HostedZoneTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHostedZonesByVPCResponseTypeDef(BaseModel):
    HostedZoneSummaries: List[HostedZoneSummaryTypeDef]
    MaxItems: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHealthChecksResponsePaginatorTypeDef(BaseModel):
    HealthChecks: List[HealthCheckPaginatorTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHealthCheckResponseTypeDef(BaseModel):
    HealthCheck: HealthCheckTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHealthCheckResponseTypeDef(BaseModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHealthChecksResponseTypeDef(BaseModel):
    HealthChecks: List[HealthCheckTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHealthCheckResponseTypeDef(BaseModel):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceRecordSetsResponsePaginatorTypeDef(BaseModel):
    ResourceRecordSets: List[ResourceRecordSetPaginatorTypeDef]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeTypeDef(BaseModel):
    Action: ChangeActionType
    ResourceRecordSet: ResourceRecordSetTypeDef

class ListResourceRecordSetsResponseTypeDef(BaseModel):
    ResourceRecordSets: List[ResourceRecordSetTypeDef]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeBatchTypeDef(BaseModel):
    Changes: Sequence[ChangeTypeDef]
    Comment: Optional[str] = None

class ChangeResourceRecordSetsRequestRequestTypeDef(BaseModel):
    HostedZoneId: str
    ChangeBatch: ChangeBatchTypeDef

