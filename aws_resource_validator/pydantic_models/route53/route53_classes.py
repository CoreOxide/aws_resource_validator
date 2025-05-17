from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53.route53_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountLimit(BaseValidatorModel):
    Type: AccountLimitTypeType
    Value: int


# This class is the input for the 'activate_key_signing_key' function.
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


# This class is the input for the 'create_cidr_collection' function.
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


# This class is the input for the 'create_key_signing_key' function.
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


# This class is the input for the 'create_query_logging_config' function.
class CreateQueryLoggingConfigRequest(BaseValidatorModel):
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


class QueryLoggingConfig(BaseValidatorModel):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


# This class is the input for the 'create_reusable_delegation_set' function.
class CreateReusableDelegationSetRequest(BaseValidatorModel):
    CallerReference: str
    HostedZoneId: Optional[str] = None


# This class is the input for the 'create_traffic_policy_instance' function.
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


# This class is the input for the 'create_traffic_policy' function.
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


# This class is the input for the 'create_traffic_policy_version' function.
class CreateTrafficPolicyVersionRequest(BaseValidatorModel):
    Id: str
    Document: str
    Comment: Optional[str] = None


class DNSSECStatus(BaseValidatorModel):
    ServeSignature: Optional[str] = None
    StatusMessage: Optional[str] = None


# This class is the input for the 'deactivate_key_signing_key' function.
class DeactivateKeySigningKeyRequest(BaseValidatorModel):
    HostedZoneId: str
    Name: str


class DeleteCidrCollectionRequest(BaseValidatorModel):
    Id: str


class DeleteHealthCheckRequest(BaseValidatorModel):
    HealthCheckId: str


# This class is the input for the 'delete_hosted_zone' function.
class DeleteHostedZoneRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'delete_key_signing_key' function.
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


# This class is the input for the 'disable_hosted_zone_dnssec' function.
class DisableHostedZoneDNSSECRequest(BaseValidatorModel):
    HostedZoneId: str


# This class is the input for the 'enable_hosted_zone_dnssec' function.
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


# This class is the input for the 'get_account_limit' function.
class GetAccountLimitRequest(BaseValidatorModel):
    Type: AccountLimitTypeType


# This class is the input for the 'get_change' function.
class GetChangeRequest(BaseValidatorModel):
    Id: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'get_dnssec' function.
class GetDNSSECRequest(BaseValidatorModel):
    HostedZoneId: str


# This class is the input for the 'get_geo_location' function.
class GetGeoLocationRequest(BaseValidatorModel):
    ContinentCode: Optional[str] = None
    CountryCode: Optional[str] = None
    SubdivisionCode: Optional[str] = None


# This class is the input for the 'get_health_check_last_failure_reason' function.
class GetHealthCheckLastFailureReasonRequest(BaseValidatorModel):
    HealthCheckId: str


# This class is the input for the 'get_health_check' function.
class GetHealthCheckRequest(BaseValidatorModel):
    HealthCheckId: str


# This class is the input for the 'get_health_check_status' function.
class GetHealthCheckStatusRequest(BaseValidatorModel):
    HealthCheckId: str


# This class is the input for the 'get_hosted_zone_limit' function.
class GetHostedZoneLimitRequest(BaseValidatorModel):
    Type: HostedZoneLimitTypeType
    HostedZoneId: str


class HostedZoneLimit(BaseValidatorModel):
    Type: HostedZoneLimitTypeType
    Value: int


# This class is the input for the 'get_hosted_zone' function.
class GetHostedZoneRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_query_logging_config' function.
class GetQueryLoggingConfigRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_reusable_delegation_set_limit' function.
class GetReusableDelegationSetLimitRequest(BaseValidatorModel):
    Type: Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
    DelegationSetId: str


class ReusableDelegationSetLimit(BaseValidatorModel):
    Type: Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
    Value: int


# This class is the input for the 'get_reusable_delegation_set' function.
class GetReusableDelegationSetRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_traffic_policy_instance' function.
class GetTrafficPolicyInstanceRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_traffic_policy' function.
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


# This class is the input for the 'list_cidr_blocks' function.
class ListCidrBlocksRequest(BaseValidatorModel):
    CollectionId: str
    LocationName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


# This class is the input for the 'list_cidr_collections' function.
class ListCidrCollectionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


# This class is the input for the 'list_cidr_locations' function.
class ListCidrLocationsRequest(BaseValidatorModel):
    CollectionId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class LocationSummary(BaseValidatorModel):
    LocationName: Optional[str] = None


# This class is the input for the 'list_geo_locations' function.
class ListGeoLocationsRequest(BaseValidatorModel):
    StartContinentCode: Optional[str] = None
    StartCountryCode: Optional[str] = None
    StartSubdivisionCode: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_health_checks' function.
class ListHealthChecksRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_hosted_zones_by_name' function.
class ListHostedZonesByNameRequest(BaseValidatorModel):
    DNSName: Optional[str] = None
    HostedZoneId: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_hosted_zones_by_vpc' function.
class ListHostedZonesByVPCRequest(BaseValidatorModel):
    VPCId: str
    VPCRegion: VPCRegionType
    MaxItems: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_hosted_zones' function.
class ListHostedZonesRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None
    DelegationSetId: Optional[str] = None
    HostedZoneType: Optional[Literal['PrivateHostedZone']] = None


# This class is the input for the 'list_query_logging_configs' function.
class ListQueryLoggingConfigsRequest(BaseValidatorModel):
    HostedZoneId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


# This class is the input for the 'list_resource_record_sets' function.
class ListResourceRecordSetsRequest(BaseValidatorModel):
    HostedZoneId: str
    StartRecordName: Optional[str] = None
    StartRecordType: Optional[RRTypeType] = None
    StartRecordIdentifier: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_reusable_delegation_sets' function.
class ListReusableDelegationSetsRequest(BaseValidatorModel):
    Marker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceId: str


# This class is the input for the 'list_tags_for_resources' function.
class ListTagsForResourcesRequest(BaseValidatorModel):
    ResourceType: TagResourceTypeType
    ResourceIds: List[str]


# This class is the input for the 'list_traffic_policies' function.
class ListTrafficPoliciesRequest(BaseValidatorModel):
    TrafficPolicyIdMarker: Optional[str] = None
    MaxItems: Optional[str] = None


class TrafficPolicySummary(BaseValidatorModel):
    Id: str
    Name: str
    Type: RRTypeType
    LatestVersion: int
    TrafficPolicyCount: int


# This class is the input for the 'list_traffic_policy_instances_by_hosted_zone' function.
class ListTrafficPolicyInstancesByHostedZoneRequest(BaseValidatorModel):
    HostedZoneId: str
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_traffic_policy_instances_by_policy' function.
class ListTrafficPolicyInstancesByPolicyRequest(BaseValidatorModel):
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_traffic_policy_instances' function.
class ListTrafficPolicyInstancesRequest(BaseValidatorModel):
    HostedZoneIdMarker: Optional[str] = None
    TrafficPolicyInstanceNameMarker: Optional[str] = None
    TrafficPolicyInstanceTypeMarker: Optional[RRTypeType] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_traffic_policy_versions' function.
class ListTrafficPolicyVersionsRequest(BaseValidatorModel):
    Id: str
    TrafficPolicyVersionMarker: Optional[str] = None
    MaxItems: Optional[str] = None


# This class is the input for the 'list_vpc_association_authorizations' function.
class ListVPCAssociationAuthorizationsRequest(BaseValidatorModel):
    HostedZoneId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[str] = None


class ResourceRecord(BaseValidatorModel):
    Value: str


# This class is the input for the 'test_dns_answer' function.
class TestDNSAnswerRequest(BaseValidatorModel):
    HostedZoneId: str
    RecordName: str
    RecordType: RRTypeType
    ResolverIP: Optional[str] = None
    EDNS0ClientSubnetIP: Optional[str] = None
    EDNS0ClientSubnetMask: Optional[str] = None


# This class is the input for the 'update_hosted_zone_comment' function.
class UpdateHostedZoneCommentRequest(BaseValidatorModel):
    Id: str
    Comment: Optional[str] = None


# This class is the input for the 'update_traffic_policy_comment' function.
class UpdateTrafficPolicyCommentRequest(BaseValidatorModel):
    Id: str
    Version: int
    Comment: str


# This class is the input for the 'update_traffic_policy_instance' function.
class UpdateTrafficPolicyInstanceRequest(BaseValidatorModel):
    Id: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int


# This class is the output for the 'activate_key_signing_key' function.
class ActivateKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_vpc_with_hosted_zone' function.
class AssociateVPCWithHostedZoneResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'change_cidr_collection' function.
class ChangeCidrCollectionResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'change_resource_record_sets' function.
class ChangeResourceRecordSetsResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deactivate_key_signing_key' function.
class DeactivateKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_hosted_zone' function.
class DeleteHostedZoneResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_key_signing_key' function.
class DeleteKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_hosted_zone_dnssec' function.
class DisableHostedZoneDNSSECResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_vpc_from_hosted_zone' function.
class DisassociateVPCFromHostedZoneResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_hosted_zone_dnssec' function.
class EnableHostedZoneDNSSECResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_account_limit' function.
class GetAccountLimitResponse(BaseValidatorModel):
    Limit: AccountLimit
    Count: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_change' function.
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


# This class is the output for the 'test_dns_answer' function.
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


# This class is the input for the 'update_health_check' function.
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


# This class is the input for the 'associate_vpc_with_hosted_zone' function.
class AssociateVPCWithHostedZoneRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC
    Comment: Optional[str] = None


# This class is the input for the 'create_vpc_association_authorization' function.
class CreateVPCAssociationAuthorizationRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC


# This class is the output for the 'create_vpc_association_authorization' function.
class CreateVPCAssociationAuthorizationResponse(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC
    ResponseMetadata: ResponseMetadata


class DeleteVPCAssociationAuthorizationRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC


# This class is the input for the 'disassociate_vpc_from_hosted_zone' function.
class DisassociateVPCFromHostedZoneRequest(BaseValidatorModel):
    HostedZoneId: str
    VPC: VPC
    Comment: Optional[str] = None


# This class is the output for the 'list_vpc_association_authorizations' function.
class ListVPCAssociationAuthorizationsResponse(BaseValidatorModel):
    HostedZoneId: str
    VPCs: List[VPC]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'change_cidr_collection' function.
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


# This class is the output for the 'list_cidr_blocks' function.
class ListCidrBlocksResponse(BaseValidatorModel):
    CidrBlocks: List[CidrBlockSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_cidr_collection' function.
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


# This class is the output for the 'list_cidr_collections' function.
class ListCidrCollectionsResponse(BaseValidatorModel):
    CidrCollections: List[CollectionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GeoProximityLocation(BaseValidatorModel):
    AWSRegion: Optional[str] = None
    LocalZoneGroup: Optional[str] = None
    Coordinates: Optional[Coordinates] = None
    Bias: Optional[int] = None


# This class is the input for the 'create_hosted_zone' function.
class CreateHostedZoneRequest(BaseValidatorModel):
    Name: str
    CallerReference: str
    VPC: Optional[VPC] = None
    HostedZoneConfig: Optional[HostedZoneConfig] = None
    DelegationSetId: Optional[str] = None


# This class is the output for the 'create_reusable_delegation_set' function.
class CreateReusableDelegationSetResponse(BaseValidatorModel):
    DelegationSet: DelegationSet
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_reusable_delegation_set' function.
class GetReusableDelegationSetResponse(BaseValidatorModel):
    DelegationSet: DelegationSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_reusable_delegation_sets' function.
class ListReusableDelegationSetsResponse(BaseValidatorModel):
    DelegationSets: List[DelegationSet]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_key_signing_key' function.
class CreateKeySigningKeyResponse(BaseValidatorModel):
    ChangeInfo: ChangeInfo
    KeySigningKey: KeySigningKey
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_query_logging_config' function.
class CreateQueryLoggingConfigResponse(BaseValidatorModel):
    QueryLoggingConfig: QueryLoggingConfig
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_logging_config' function.
class GetQueryLoggingConfigResponse(BaseValidatorModel):
    QueryLoggingConfig: QueryLoggingConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_query_logging_configs' function.
class ListQueryLoggingConfigsResponse(BaseValidatorModel):
    QueryLoggingConfigs: List[QueryLoggingConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_traffic_policy_instance' function.
class CreateTrafficPolicyInstanceResponse(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstance
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_traffic_policy_instance' function.
class GetTrafficPolicyInstanceResponse(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_traffic_policy_instances_by_hosted_zone' function.
class ListTrafficPolicyInstancesByHostedZoneResponse(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstance]
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_traffic_policy_instances_by_policy' function.
class ListTrafficPolicyInstancesByPolicyResponse(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstance]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_traffic_policy_instances' function.
class ListTrafficPolicyInstancesResponse(BaseValidatorModel):
    TrafficPolicyInstances: List[TrafficPolicyInstance]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_traffic_policy_instance' function.
class UpdateTrafficPolicyInstanceResponse(BaseValidatorModel):
    TrafficPolicyInstance: TrafficPolicyInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_traffic_policy' function.
class CreateTrafficPolicyResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_traffic_policy_version' function.
class CreateTrafficPolicyVersionResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_traffic_policy' function.
class GetTrafficPolicyResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_traffic_policy_versions' function.
class ListTrafficPolicyVersionsResponse(BaseValidatorModel):
    TrafficPolicies: List[TrafficPolicy]
    IsTruncated: bool
    TrafficPolicyVersionMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_traffic_policy_comment' function.
class UpdateTrafficPolicyCommentResponse(BaseValidatorModel):
    TrafficPolicy: TrafficPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_dnssec' function.
class GetDNSSECResponse(BaseValidatorModel):
    Status: DNSSECStatus
    KeySigningKeys: List[KeySigningKey]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_geo_location' function.
class GetGeoLocationResponse(BaseValidatorModel):
    GeoLocationDetails: GeoLocationDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_geo_locations' function.
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


# This class is the output for the 'get_hosted_zone_limit' function.
class GetHostedZoneLimitResponse(BaseValidatorModel):
    Limit: HostedZoneLimit
    Count: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_reusable_delegation_set_limit' function.
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


# This class is the output for the 'list_cidr_locations' function.
class ListCidrLocationsResponse(BaseValidatorModel):
    CidrLocations: List[LocationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_traffic_policies' function.
class ListTrafficPoliciesResponse(BaseValidatorModel):
    TrafficPolicySummaries: List[TrafficPolicySummary]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata

HealthCheckConfigUnion = Union[HealthCheckConfig, HealthCheckConfigOutput]


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTagSet: ResourceTagSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resources' function.
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


# This class is the output for the 'get_health_check_last_failure_reason' function.
class GetHealthCheckLastFailureReasonResponse(BaseValidatorModel):
    HealthCheckObservations: List[HealthCheckObservation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_health_check_status' function.
class GetHealthCheckStatusResponse(BaseValidatorModel):
    HealthCheckObservations: List[HealthCheckObservation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hosted_zone' function.
class CreateHostedZoneResponse(BaseValidatorModel):
    HostedZone: HostedZone
    ChangeInfo: ChangeInfo
    DelegationSet: DelegationSet
    VPC: VPC
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_hosted_zone' function.
class GetHostedZoneResponse(BaseValidatorModel):
    HostedZone: HostedZone
    DelegationSet: DelegationSet
    VPCs: List[VPC]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_hosted_zones_by_name' function.
class ListHostedZonesByNameResponse(BaseValidatorModel):
    HostedZones: List[HostedZone]
    DNSName: str
    HostedZoneId: str
    IsTruncated: bool
    NextDNSName: str
    NextHostedZoneId: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_hosted_zones' function.
class ListHostedZonesResponse(BaseValidatorModel):
    HostedZones: List[HostedZone]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_hosted_zone_comment' function.
class UpdateHostedZoneCommentResponse(BaseValidatorModel):
    HostedZone: HostedZone
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_hosted_zones_by_vpc' function.
class ListHostedZonesByVPCResponse(BaseValidatorModel):
    HostedZoneSummaries: List[HostedZoneSummary]
    MaxItems: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_health_check' function.
class CreateHealthCheckRequest(BaseValidatorModel):
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigUnion


# This class is the output for the 'create_health_check' function.
class CreateHealthCheckResponse(BaseValidatorModel):
    HealthCheck: HealthCheck
    Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_health_check' function.
class GetHealthCheckResponse(BaseValidatorModel):
    HealthCheck: HealthCheck
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_health_checks' function.
class ListHealthChecksResponse(BaseValidatorModel):
    HealthChecks: List[HealthCheck]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_health_check' function.
class UpdateHealthCheckResponse(BaseValidatorModel):
    HealthCheck: HealthCheck
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resource_record_sets' function.
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


# This class is the input for the 'change_resource_record_sets' function.
class ChangeResourceRecordSetsRequest(BaseValidatorModel):
    HostedZoneId: str
    ChangeBatch: ChangeBatch