from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53.route53_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountLimit(BaseValidatorModel):
    Type: AccountLimitTypeType
    Value: int


class ActivateKeySigningKeyRequest(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class ChangeInfo(BaseValidatorModel):
    Id: str
    Status: ChangeStatusType
    SubmittedAt: datetime
    Comment: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AlarmIdentifier(BaseValidatorModel):
    Region: CloudWatchRegionType
    Name: str


class AliasTarget(BaseValidatorModel):
    HostedZoneId: str
    DNSName: str
    EvaluateTargetHealth: bool


class VPC(BaseValidatorModel):
    VPCRegion: Optional[VPCRegionType] = None
    VPCId: Optional[str] = None


class CidrCollectionChange(BaseValidatorModel):
    LocationName: str
    Action: CidrCollectionChangeActionType
    CidrList: List[str]


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class CidrBlockSummary(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    LocationName: Optional[str] = None


class CidrCollection(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None


class CidrRoutingConfig(BaseValidatorModel):
    CollectionId: str
    LocationName: str


class Dimension(BaseValidatorModel):
    Name: str
    Value: str


class CollectionSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Version: Optional[int] = None


class Coordinates(BaseValidatorModel):
    Latitude: str
    Longitude: str


class CreateCidrCollectionRequest(BaseValidatorModel):
    Name: str
    CallerReference: str


class HostedZoneConfig(BaseValidatorModel):
    Comment: Optional[str] = None
    PrivateZone: Optional[bool] = None


class DelegationSet(BaseValidatorModel):
    NameServers: List[str]
    Id: Optional[str] = None
    CallerReference: Optional[str] = None


class CreateKeySigningKeyRequest(BaseValidatorModel):
    CallerReference: str
    HostedZoneId: str
    KeyManagementServiceArn: str
    Name: str
    Status: str


class KeySigningKey(BaseValidatorModel):
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


class CreateQueryLoggingConfigRequest(BaseValidatorModel):
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


class QueryLoggingConfig(BaseValidatorModel):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


class CreateReusableDelegationSetRequest(BaseValidatorModel):
    CallerReference: str
    HostedZoneId: Optional[str] = None


class CreateTrafficPolicyInstanceRequest(BaseValidatorModel):
    HostedZoneId: str
    Name: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int


class TrafficPolicyInstance(BaseValidatorModel):
    Id: str
    HostedZoneId: str
    Name: str
    TTL: int
    State: str
    Message: str
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    TrafficPolicyType: RRTypeType


class CreateTrafficPolicyRequest(BaseValidatorModel):
    Name: str
    Document: str
    Comment: Optional[str] = None


class TrafficPolicy(BaseValidatorModel):
    Id: str
    Version: int
    Name: str
    Type: RRTypeType
    Document: str
    Comment: Optional[str] = None


class CreateTrafficPolicyVersionRequest(BaseValidatorModel):
    Id: str
    Document: str
    Comment: Optional[str] = None


class DNSSECStatus(BaseValidatorModel):
    ServeSignature: Optional[str] = None
    StatusMessage: Optional[str] = None


class DeactivateKeySigningKeyRequest(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class DeleteCidrCollectionRequest(BaseValidatorModel):
    Id: str


class DeleteHealthCheckRequest(BaseValidatorModel):
    HealthCheckId: str


class DeleteHostedZoneRequest(BaseValidatorModel):
    Id: str


class DeleteKeySigningKeyRequest(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class DeleteQueryLoggingConfigRequest(BaseValidatorModel):
    Id: str


class DeleteReusableDelegationSetRequest(BaseValidatorModel):
    Id: str


class DeleteTrafficPolicyInstanceRequest(BaseValidatorModel):
    Id: str


class DeleteTrafficPolicyRequest(BaseValidatorModel):
    Id: str
    Version: int


class DisableHostedZoneDNSSECRequest(BaseValidatorModel):
    HostedZoneId: str


class EnableHostedZoneDNSSECRequest(BaseValidatorModel):
    HostedZoneId: str


class GeoLocationDetails(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    ContinentName: Optional[str] = None
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None
    SubdivisionCode: Optional[str] = None
    SubdivisionName: Optional[str] = None


class GeoLocation(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None


class GetAccountLimitRequest(BaseValidatorModel):
    Type: AccountLimitTypeType


class GetChangeRequest(BaseValidatorModel):
    Id: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetDNSSECRequest(BaseValidatorModel):
    HostedZoneId: str


class GetGeoLocationRequest(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None


class GetHealthCheckLastFailureReasonRequest(BaseValidatorModel):
    HealthCheckId: str


class GetHealthCheckRequest(BaseValidatorModel):
    HealthCheckId: str


class GetHealthCheckStatusRequest(BaseValidatorModel):
    HealthCheckId: str


class GetHostedZoneLimitRequest(BaseValidatorModel):
    Type: HostedZoneLimitTypeType
    HostedZoneId: str


class HostedZoneLimit(BaseValidatorModel):
    Type: HostedZoneLimitTypeType
    Value: int


class GetHostedZoneRequest(BaseValidatorModel):
    Id: str


class GetQueryLoggingConfigRequest(BaseValidatorModel):
    Id: str


class GetReusableDelegationSetLimitRequest(BaseValidatorModel):
    Type: Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
    DelegationSetId: str


class ReusableDelegationSetLimit(BaseValidatorModel):
    Type: Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
    Value: int


class GetReusableDelegationSetRequest(BaseValidatorModel):
    Id: str


class GetTrafficPolicyInstanceRequest(BaseValidatorModel):
    Id: str


class GetTrafficPolicyRequest(BaseValidatorModel):
    Id: str
    Version: int


class StatusReport(BaseValidatorModel):
    Status: Optional[str] = None
    CheckedTime: Optional[datetime] = None


class LinkedService(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    Description: Optional[str] = None


class HostedZoneOwner(BaseValidatorModel):
    OwningAccount: Optional[str] = None
    OwningService: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCidrBlocksRequest(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ListCidrCollectionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ListCidrLocationsRequest(BaseValidatorModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class LocationSummary(BaseValidatorModel):
    LocationName: Optional[str] = None


class ListGeoLocationsRequest(BaseValidatorModel):
    StartContinentCode: Optional[str] = None
    StartCountryCode: Optional[str] = None
    StartSubdivisionCode: Optional[str] = None
    MaxItems: Optional[str] = None


class ListHealthChecksRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListHostedZonesByNameRequest(BaseValidatorModel):
    DNSName: Optional[str] = None
    HostedZoneId: Optional[str] = None
    MaxItems: Optional[str] = None


class ListHostedZonesByVPCRequest(BaseValidatorModel):
    VPCId: str
    VPCRegion: VPCRegionType
    MaxItems: Optional[str] = None
    NextToken: Optional[str] = None


class ListHostedZonesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal['PrivateHostedZone']] = None


class ListQueryLoggingConfigsRequest(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ListResourceRecordSetsRequest(BaseValidatorModel):
    HostedZoneId: str
    StartRecordName: Optional[str] = None
    StartRecordType: Optional[RRTypeType] = None
    StartRecordIdentifier: Optional[str] = None
    MaxItems: Optional[str] = None


class ListReusableDelegationSetsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str


class ListTagsForResourcesRequest(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceIds: List[str]


class ListTrafficPoliciesRequest(BaseValidatorModel):
    TrafficPolicyIdMarker: Optional[str] = None
    MaxItems: Optional[str] = None


class TrafficPolicySummary(BaseValidatorModel):
    Id: str
    Name: str
    Type: RRTypeType
    LatestVersion: int
    TrafficPolicyCount: int


class ListTrafficPolicyInstancesByHostedZoneRequest(BaseValidatorModel):
    HostedZoneId: str
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyInstancesByPolicyRequest(BaseValidatorModel):
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyInstancesRequest(BaseValidatorModel):
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


class ListTrafficPolicyVersionsRequest(BaseValidatorModel):
    Id: str
    TrafficPolicyVersionMarker: Optional[str] = None
    MaxItems: Optional[str] = None


class ListVPCAssociationAuthorizationsRequest(BaseValidatorModel):
    HostedZoneId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ResourceRecord(BaseValidatorModel):
    Value: str


class TestDNSAnswerRequest(BaseValidatorModel):
    HostedZoneId: str
    RecordName: str
    RecordType: RRTypeType
    ResolverIP: Optional[str] = None
    EDNS0ClientSubnetIP: Optional[str] = None
    EDNS0ClientSubnetMask: Optional[str] = None


class UpdateHostedZoneCommentRequest(BaseValidatorModel):
    Id: str
    Comment: Optional[str] = None


class UpdateTrafficPolicyCommentRequest(BaseValidatorModel):
    Id: str
    Version: int
    Comment: str


class UpdateTrafficPolicyInstanceRequest(BaseValidatorModel):
    Id: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int


class ActivateKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class AssociateVPCWithHostedZoneResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class ChangeCidrCollectionResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class ChangeResourceRecordSetsResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class DeactivateKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class DeleteHostedZoneResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class DeleteKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class DisableHostedZoneDNSSECResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class DisassociateVPCFromHostedZoneResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class EnableHostedZoneDNSSECResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class GetAccountLimitResponse(BaseValidatorModel):
    Limit: AccountLimit
    Count: int
    ResponseMetadata: ResponseMetadata


class GetChangeResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


class GetCheckerIpRangesResponse(BaseValidatorModel):
    CheckerIpRanges: List[str]
    ResponseMetadata: ResponseMetadata


class GetHealthCheckCountResponse(BaseValidatorModel):
    HealthCheckCount: int
    ResponseMetadata: ResponseMetadata


class GetHostedZoneCountResponse(BaseValidatorModel):
    HostedZoneCount: int
    ResponseMetadata: ResponseMetadata


class GetTrafficPolicyInstanceCountResponse(BaseValidatorModel):
    TrafficPolicyInstanceCount: int
    ResponseMetadata: ResponseMetadata


class TestDNSAnswerResponse(BaseValidatorModel):
    Nameserver: str
    RecordName: str
    RecordType: RRTypeType
    RecordData: List[str]
    ResponseCode: str
    Protocol: str
    ResponseMetadata: ResponseMetadata


class HealthCheckConfigOutput(BaseValidatorModel):
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
    AlarmIdentifier: Optional[AlarmIdentifier] = None
    InsufficientDataHealthStatus: Optional[InsufficientDataHealthStatusType] = None
    RoutingControlArn: Optional[str] = None


class HealthCheckConfig(BaseValidatorModel):
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
    AlarmIdentifier: Optional[AlarmIdentifier] = None
    InsufficientDataHealthStatus: Optional[InsufficientDataHealthStatusType] = None
    RoutingControlArn: Optional[str] = None


class UpdateHealthCheckRequest(BaseValidatorModel):
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
    ChildHealthChecks: Optional[List[str]] = None
    EnableSNI: Optional[bool] = None
    Regions: Optional[List[HealthCheckRegionType]] = None
    AlarmIdentifier: Optional[AlarmIdentifier] = None
    InsufficientDataHealthStatus: Optional[InsufficientDataHealthStatusType] = None
    ResetElements: Optional[List[ResettableElementNameType]] = None


class AssociateVPCWithHostedZoneRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC
    Comment: Optional[str] = None


class CreateVPCAssociationAuthorizationRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC


class CreateVPCAssociationAuthorizationResponse(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC
    ResponseMetadata: ResponseMetadata


class DeleteVPCAssociationAuthorizationRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC


class DisassociateVPCFromHostedZoneRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC
    Comment: Optional[str] = None


class ListVPCAssociationAuthorizationsResponse(BaseValidatorModel):
    HostedZoneId: str
    VPCs: List[VPC]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ChangeCidrCollectionRequest(BaseValidatorModel):
    Id: str
    Changes: List[CidrCollectionChange]
    CollectionVersion: Optional[int] = None


class ChangeTagsForResourceRequest(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str
    AddTags: Optional[List[Tag]] = None
    RemoveTagKeys: Optional[List[str]] = None


class ResourceTagSet(BaseValidatorModel):
    ResourceType: Optional[TagResourceTypeType] = None
    ResourceId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ListCidrBlocksResponse(BaseValidatorModel):
    CidrBlocks: List[CidrBlockSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateCidrCollectionResponse(BaseValidatorModel):
    Collection: CidrCollection
    Location: str
    ResponseMetadata: ResponseMetadata


class CloudWatchAlarmConfiguration(BaseValidatorModel):
    EvaluationPeriods: int
    Threshold: float
    ComparisonOperator: ComparisonOperatorType
    Period: int
    MetricName: str
    Namespace: str
    Statistic: StatisticType
    Dimensions: Optional[List[Dimension]] = None


class ListCidrCollectionsResponse(BaseValidatorModel):
    CidrCollections: List[CollectionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GeoProximityLocation(BaseValidatorModel):
    AWSRegion: Optional[str] = None
    LocalZoneGroup: Optional[str] = None
    Coordinates: Optional[Coordinates] = None
    Bias: Optional[int] = None


class CreateHostedZoneRequest(BaseValidatorModel):
    Name: str
    CallerReference: str
    VPC: Optional[VPC] = None
    HostedZoneConfig: Optional[HostedZoneConfig] = None
    DelegationSetId: Optional[str] = None


class CreateReusableDelegationSetResponse(BaseValidatorModel):
    DelegationSet: DelegationSet
    Location: str
    ResponseMetadata: ResponseMetadata


class GetReusableDelegationSetResponse(BaseValidatorModel):
    DelegationSet: DelegationSet
    ResponseMetadata: ResponseMetadata


class ListReusableDelegationSetsResponse(BaseValidatorModel):
    DelegationSets: List[DelegationSet]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class CreateKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    KeySigningKey: KeySigningKey
    Location: str
    ResponseMetadata: ResponseMetadata


class CreateQueryLoggingConfigResponse(BaseValidatorModel):
    QueryLoggingConfig: QueryLoggingConfig
    Location: str
    ResponseMetadata: ResponseMetadata


class GetQueryLoggingConfigResponse(BaseValidatorModel):
    QueryLoggingConfig: QueryLoggingConfig
    ResponseMetadata: ResponseMetadata


class ListQueryLoggingConfigsResponse(BaseValidatorModel):
    QueryLoggingConfigs: List[QueryLoggingConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateTrafficPolicyInstanceResponse(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstance
    Location: str
    ResponseMetadata: ResponseMetadata


class GetTrafficPolicyInstanceResponse(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstance
    ResponseMetadata: ResponseMetadata


class ListTrafficPolicyInstancesByHostedZoneResponse(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstance]
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class ListTrafficPolicyInstancesByPolicyResponse(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstance]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class ListTrafficPolicyInstancesResponse(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstance]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class UpdateTrafficPolicyInstanceResponse(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstance
    ResponseMetadata: ResponseMetadata


class CreateTrafficPolicyResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    Location: str
    ResponseMetadata: ResponseMetadata


class CreateTrafficPolicyVersionResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    Location: str
    ResponseMetadata: ResponseMetadata


class GetTrafficPolicyResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    ResponseMetadata: ResponseMetadata


class ListTrafficPolicyVersionsResponse(BaseValidatorModel):
    TrafficPolicies: List[TrafficPolicy]
    IsTruncated: bool
    TrafficPolicyVersionMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class UpdateTrafficPolicyCommentResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    ResponseMetadata: ResponseMetadata


class GetDNSSECResponse(BaseValidatorModel):
    Status: DNSSECStatus
    KeySigningKeys: List[KeySigningKey]
    ResponseMetadata: ResponseMetadata


class GetGeoLocationResponse(BaseValidatorModel):
    GeoLocationDetails: GeoLocationDetails
    ResponseMetadata: ResponseMetadata


class ListGeoLocationsResponse(BaseValidatorModel):
    GeoLocationDetailsList: List[GeoLocationDetails]
    IsTruncated: bool
    NextContinentCode: str
    NextCountryCode: str
    NextSubdivisionCode: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class GetChangeRequestWait(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetHostedZoneLimitResponse(BaseValidatorModel):
    Limit: HostedZoneLimit
    Count: int
    ResponseMetadata: ResponseMetadata


class GetReusableDelegationSetLimitResponse(BaseValidatorModel):
    Limit: ReusableDelegationSetLimit
    Count: int
    ResponseMetadata: ResponseMetadata


class HealthCheckObservation(BaseValidatorModel):
    Region: Optional[HealthCheckRegionType] = None
    IPAddress: Optional[str] = None
    StatusReport: Optional[StatusReport] = None


class HostedZone(BaseValidatorModel):
    Id: str
    Name: str
    CallerReference: str
    Config: Optional[HostedZoneConfig] = None
    ResourceRecordSetCount: Optional[int] = None
    LinkedService: Optional[LinkedService] = None


class HostedZoneSummary(BaseValidatorModel):
    HostedZoneId: str
    Name: str
    Owner: HostedZoneOwner


class ListCidrBlocksRequestPaginate(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCidrCollectionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCidrLocationsRequestPaginate(BaseValidatorModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHealthChecksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHostedZonesRequestPaginate(BaseValidatorModel):
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal['PrivateHostedZone']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueryLoggingConfigsRequestPaginate(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceRecordSetsRequestPaginate(BaseValidatorModel):
    HostedZoneId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVPCAssociationAuthorizationsRequestPaginate(BaseValidatorModel):
    HostedZoneId: str
    MaxResults: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCidrLocationsResponse(BaseValidatorModel):
    CidrLocations: List[LocationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrafficPoliciesResponse(BaseValidatorModel):
    TrafficPolicySummaries: List[TrafficPolicySummary]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata

HealthCheckConfigUnion = Union[HealthCheckConfig, HealthCheckConfigOutput]


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTagSet: ResourceTagSet
    ResponseMetadata: ResponseMetadata


class ListTagsForResourcesResponse(BaseValidatorModel):
    ResourceTagSets: List[ResourceTagSet]
    ResponseMetadata: ResponseMetadata


class HealthCheck(BaseValidatorModel):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigOutput
    HealthCheckVersion: int
    LinkedService: Optional[LinkedService] = None
    CloudWatchAlarmConfiguration: Optional[CloudWatchAlarmConfiguration] = None


class ResourceRecordSetOutput(BaseValidatorModel):
    Name: str
    Type: RRTypeType
    SetIdentifier: Optional[str] = None
    Weight: Optional[int] = None
    Region: Optional[ResourceRecordSetRegionType] = None
    GeoLocation: Optional[GeoLocation] = None
    Failover: Optional[ResourceRecordSetFailoverType] = None
    MultiValueAnswer: Optional[bool] = None
    TTL: Optional[int] = None
    ResourceRecords: Optional[List[ResourceRecord]] = None
    AliasTarget: Optional[AliasTarget] = None
    HealthCheckId: Optional[str] = None
    TrafficPolicyInstanceId: Optional[str] = None
    CidrRoutingConfig: Optional[CidrRoutingConfig] = None
    GeoProximityLocation: Optional[GeoProximityLocation] = None


class ResourceRecordSet(BaseValidatorModel):
    Name: str
    Type: RRTypeType
    SetIdentifier: Optional[str] = None
    Weight: Optional[int] = None
    Region: Optional[ResourceRecordSetRegionType] = None
    GeoLocation: Optional[GeoLocation] = None
    Failover: Optional[ResourceRecordSetFailoverType] = None
    MultiValueAnswer: Optional[bool] = None
    TTL: Optional[int] = None
    ResourceRecords: Optional[List[ResourceRecord]] = None
    AliasTarget: Optional[AliasTarget] = None
    HealthCheckId: Optional[str] = None
    TrafficPolicyInstanceId: Optional[str] = None
    CidrRoutingConfig: Optional[CidrRoutingConfig] = None
    GeoProximityLocation: Optional[GeoProximityLocation] = None


class GetHealthCheckLastFailureReasonResponse(BaseValidatorModel):
    HealthCheckObservations: List[HealthCheckObservation]
    ResponseMetadata: ResponseMetadata


class GetHealthCheckStatusResponse(BaseValidatorModel):
    HealthCheckObservations: List[HealthCheckObservation]
    ResponseMetadata: ResponseMetadata


class CreateHostedZoneResponse(BaseValidatorModel):
    HostedZone: HostedZone
    ChangeInfo: ChangeInfo
    DelegationSet: DelegationSet
    VPC: VPC
    Location: str
    ResponseMetadata: ResponseMetadata


class GetHostedZoneResponse(BaseValidatorModel):
    HostedZone: HostedZone
    DelegationSet: DelegationSet
    VPCs: List[VPC]
    ResponseMetadata: ResponseMetadata


class ListHostedZonesByNameResponse(BaseValidatorModel):
    HostedZones: List[HostedZone]
    DNSName: str
    HostedZoneId: str
    IsTruncated: bool
    NextDNSName: str
    NextHostedZoneId: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class ListHostedZonesResponse(BaseValidatorModel):
    HostedZones: List[HostedZone]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class UpdateHostedZoneCommentResponse(BaseValidatorModel):
    HostedZone: HostedZone
    ResponseMetadata: ResponseMetadata


class ListHostedZonesByVPCResponse(BaseValidatorModel):
    HostedZoneSummaries: List[HostedZoneSummary]
    MaxItems: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateHealthCheckRequest(BaseValidatorModel):
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigUnion


class CreateHealthCheckResponse(BaseValidatorModel):
    HealthCheck: HealthCheck
    Location: str
    ResponseMetadata: ResponseMetadata


class GetHealthCheckResponse(BaseValidatorModel):
    HealthCheck: HealthCheck
    ResponseMetadata: ResponseMetadata


class ListHealthChecksResponse(BaseValidatorModel):
    HealthChecks: List[HealthCheck]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


class UpdateHealthCheckResponse(BaseValidatorModel):
    HealthCheck: HealthCheck
    ResponseMetadata: ResponseMetadata


class ListResourceRecordSetsResponse(BaseValidatorModel):
    ResourceRecordSets: List[ResourceRecordSetOutput]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata

ResourceRecordSetUnion = Union[ResourceRecordSet, ResourceRecordSetOutput]


class Change(BaseValidatorModel):
    Action: ChangeActionType
    ResourceRecordSet: ResourceRecordSetUnion


class ChangeBatch(BaseValidatorModel):
    Changes: List[Change]
    Comment: Optional[str] = None


class ChangeResourceRecordSetsRequest(BaseValidatorModel):
    HostedZoneId: str
    ChangeBatch: ChangeBatch