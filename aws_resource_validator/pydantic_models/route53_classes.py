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
from aws_resource_validator.pydantic_models.route53_constants import *

class AccountLimitTypeDef(BaseValidatorModel):
    Type: AccountLimitTypeType
    Value: int

class ActivateKeySigningKeyRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str

class ChangeInfoTypeDef(BaseValidatorModel):
    Id: str
    Status: ChangeStatusType
    SubmittedAt: datetime
    Comment: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class CreateCidrCollectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    CallerReference: str

class HostedZoneConfigTypeDef(BaseValidatorModel):
    Comment: Optional[str] = None
    PrivateZone: Optional[bool] = None

class DelegationSetTypeDef(BaseValidatorModel):
    NameServers: List[str]
    Id: Optional[str] = None
    CallerReference: Optional[str] = None

class CreateKeySigningKeyRequestRequestTypeDef(BaseValidatorModel):
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

class CreateQueryLoggingConfigRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str

class QueryLoggingConfigTypeDef(BaseValidatorModel):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str

class CreateReusableDelegationSetRequestRequestTypeDef(BaseValidatorModel):
    CallerReference: str
    HostedZoneId: Optional[str] = None

class CreateTrafficPolicyInstanceRequestRequestTypeDef(BaseValidatorModel):
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

class CreateTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Document: str
    Comment: Optional[str] = None

class TrafficPolicyTypeDef(BaseValidatorModel):
    Id: str
    Version: int
    Name: str
    Type: RRTypeType
    Document: str
    Comment: Optional[str] = None

class CreateTrafficPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Document: str
    Comment: Optional[str] = None

class DNSSECStatusTypeDef(BaseValidatorModel):
    ServeSignature: Optional[str] = None
    StatusMessage: Optional[str] = None

class DeactivateKeySigningKeyRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str

class DeleteCidrCollectionRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteHealthCheckRequestRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str

class DeleteHostedZoneRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteKeySigningKeyRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    Name: str

class DeleteQueryLoggingConfigRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteReusableDelegationSetRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteTrafficPolicyInstanceRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class DeleteTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Version: int

class DisableHostedZoneDNSSECRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str

class EnableHostedZoneDNSSECRequestRequestTypeDef(BaseValidatorModel):
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

class GetAccountLimitRequestRequestTypeDef(BaseValidatorModel):
    Type: AccountLimitTypeType

class GetChangeRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetDNSSECRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str

class GetGeoLocationRequestRequestTypeDef(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None

class GetHealthCheckLastFailureReasonRequestRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str

class GetHealthCheckRequestRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str

class GetHealthCheckStatusRequestRequestTypeDef(BaseValidatorModel):
    HealthCheckId: str

class GetHostedZoneLimitRequestRequestTypeDef(BaseValidatorModel):
    Type: HostedZoneLimitTypeType
    HostedZoneId: str

class HostedZoneLimitTypeDef(BaseValidatorModel):
    Type: HostedZoneLimitTypeType
    Value: int

class GetHostedZoneRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class GetQueryLoggingConfigRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class GetReusableDelegationSetLimitRequestRequestTypeDef(BaseValidatorModel):
    Type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"]
    DelegationSetId: str

class ReusableDelegationSetLimitTypeDef(BaseValidatorModel):
    Type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"]
    Value: int

class GetReusableDelegationSetRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class GetTrafficPolicyInstanceRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class GetTrafficPolicyRequestRequestTypeDef(BaseValidatorModel):
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

class ListCidrBlocksRequestRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ListCidrCollectionsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ListCidrLocationsRequestRequestTypeDef(BaseValidatorModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class LocationSummaryTypeDef(BaseValidatorModel):
    LocationName: Optional[str] = None

class ListGeoLocationsRequestRequestTypeDef(BaseValidatorModel):
    StartContinentCode: Optional[str] = None
    StartCountryCode: Optional[str] = None
    StartSubdivisionCode: Optional[str] = None
    MaxItems: Optional[str] = None

class ListHealthChecksRequestRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListHostedZonesByNameRequestRequestTypeDef(BaseValidatorModel):
    DNSName: Optional[str] = None
    HostedZoneId: Optional[str] = None
    MaxItems: Optional[str] = None

class ListHostedZonesByVPCRequestRequestTypeDef(BaseValidatorModel):
    VPCId: str
    VPCRegion: VPCRegionType
    MaxItems: Optional[str] = None
    NextToken: Optional[str] = None

class ListHostedZonesRequestRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal["PrivateHostedZone"]] = None

class ListQueryLoggingConfigsRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ListResourceRecordSetsRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    StartRecordName: Optional[str] = None
    StartRecordType: Optional[RRTypeType] = None
    StartRecordIdentifier: Optional[str] = None
    MaxItems: Optional[str] = None

class ListReusableDelegationSetsRequestRequestTypeDef(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str

class ListTagsForResourcesRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceIds: Sequence[str]

class ListTrafficPoliciesRequestRequestTypeDef(BaseValidatorModel):
    TrafficPolicyIdMarker: Optional[str] = None
    MaxItems: Optional[str] = None

class TrafficPolicySummaryTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Type: RRTypeType
    LatestVersion: int
    TrafficPolicyCount: int

class ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None

class ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef(BaseValidatorModel):
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None

class ListTrafficPolicyInstancesRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None

class ListTrafficPolicyVersionsRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    TrafficPolicyVersionMarker: Optional[str] = None
    MaxItems: Optional[str] = None

class ListVPCAssociationAuthorizationsRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None

class ResourceRecordTypeDef(BaseValidatorModel):
    Value: str

class TestDNSAnswerRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    RecordName: str
    RecordType: RRTypeType
    ResolverIP: Optional[str] = None
    EDNS0ClientSubnetIP: Optional[str] = None
    EDNS0ClientSubnetMask: Optional[str] = None

class UpdateHostedZoneCommentRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Comment: Optional[str] = None

class UpdateTrafficPolicyCommentRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Version: int
    Comment: str

class UpdateTrafficPolicyInstanceRequestRequestTypeDef(BaseValidatorModel):
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

class TestDNSAnswerResponseTypeDef(BaseValidatorModel):
    Nameserver: str
    RecordName: str
    RecordType: RRTypeType
    RecordData: List[str]
    ResponseCode: str
    Protocol: str
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckConfigPaginatorTypeDef(BaseValidatorModel):
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

class HealthCheckConfigTypeDef(BaseValidatorModel):
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

class UpdateHealthCheckRequestRequestTypeDef(BaseValidatorModel):
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

class AssociateVPCWithHostedZoneRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: Optional[str] = None

class CreateVPCAssociationAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef

class CreateVPCAssociationAuthorizationResponseTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVPCAssociationAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef

class DisassociateVPCFromHostedZoneRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: Optional[str] = None

class ListVPCAssociationAuthorizationsResponseTypeDef(BaseValidatorModel):
    HostedZoneId: str
    NextToken: str
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeCidrCollectionRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    Changes: Sequence[CidrCollectionChangeTypeDef]
    CollectionVersion: Optional[int] = None

class ChangeTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str
    AddTags: Optional[Sequence[TagTypeDef]] = None
    RemoveTagKeys: Optional[Sequence[str]] = None

class ResourceTagSetTypeDef(BaseValidatorModel):
    ResourceType: Optional[TagResourceTypeType] = None
    ResourceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ListCidrBlocksResponseTypeDef(BaseValidatorModel):
    NextToken: str
    CidrBlocks: List[CidrBlockSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCidrCollectionResponseTypeDef(BaseValidatorModel):
    Collection: CidrCollectionTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    CidrCollections: List[CollectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GeoProximityLocationTypeDef(BaseValidatorModel):
    AWSRegion: Optional[str] = None
    LocalZoneGroup: Optional[str] = None
    Coordinates: Optional[CoordinatesTypeDef] = None
    Bias: Optional[int] = None

class CreateHostedZoneRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetChangeRequestResourceRecordSetsChangedWaitTypeDef(BaseValidatorModel):
    Id: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetHostedZoneLimitResponseTypeDef(BaseValidatorModel):
    Limit: HostedZoneLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListCidrBlocksRequestListCidrBlocksPaginateTypeDef(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCidrCollectionsRequestListCidrCollectionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCidrLocationsRequestListCidrLocationsPaginateTypeDef(BaseValidatorModel):
    CollectionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHealthChecksRequestListHealthChecksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHostedZonesRequestListHostedZonesPaginateTypeDef(BaseValidatorModel):
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal["PrivateHostedZone"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateTypeDef(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceRecordSetsRequestListResourceRecordSetsPaginateTypeDef(BaseValidatorModel):
    HostedZoneId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateTypeDef(BaseValidatorModel):
    HostedZoneId: str
    MaxResults: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCidrLocationsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    CidrLocations: List[LocationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPoliciesResponseTypeDef(BaseValidatorModel):
    TrafficPolicySummaries: List[TrafficPolicySummaryTypeDef]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHealthCheckRequestRequestTypeDef(BaseValidatorModel):
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTagSet: ResourceTagSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourcesResponseTypeDef(BaseValidatorModel):
    ResourceTagSets: List[ResourceTagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckPaginatorTypeDef(BaseValidatorModel):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigPaginatorTypeDef
    HealthCheckVersion: int
    LinkedService: Optional[LinkedServiceTypeDef] = None
    CloudWatchAlarmConfiguration: Optional[CloudWatchAlarmConfigurationTypeDef] = None

class HealthCheckTypeDef(BaseValidatorModel):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigTypeDef
    HealthCheckVersion: int
    LinkedService: Optional[LinkedServiceTypeDef] = None
    CloudWatchAlarmConfiguration: Optional[CloudWatchAlarmConfigurationTypeDef] = None

class ResourceRecordSetPaginatorTypeDef(BaseValidatorModel):
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

class ResourceRecordSetTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHealthChecksResponsePaginatorTypeDef(BaseValidatorModel):
    HealthChecks: List[HealthCheckPaginatorTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListResourceRecordSetsResponsePaginatorTypeDef(BaseValidatorModel):
    ResourceRecordSets: List[ResourceRecordSetPaginatorTypeDef]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeTypeDef(BaseValidatorModel):
    Action: ChangeActionType
    ResourceRecordSet: ResourceRecordSetTypeDef

class ListResourceRecordSetsResponseTypeDef(BaseValidatorModel):
    ResourceRecordSets: List[ResourceRecordSetTypeDef]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeBatchTypeDef(BaseValidatorModel):
    Changes: Sequence[ChangeTypeDef]
    Comment: Optional[str] = None

class ChangeResourceRecordSetsRequestRequestTypeDef(BaseValidatorModel):
    HostedZoneId: str
    ChangeBatch: ChangeBatchTypeDef

