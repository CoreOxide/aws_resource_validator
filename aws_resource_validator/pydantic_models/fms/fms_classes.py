from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.fms.fms_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountScopeOutput(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    AllAccountsEnabled: Optional[bool] = None
    ExcludeSpecifiedAccounts: Optional[bool] = None


class AccountScope(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    AllAccountsEnabled: Optional[bool] = None
    ExcludeSpecifiedAccounts: Optional[bool] = None


class ActionTarget(BaseValidatorModel):
    ResourceId: Optional[str] = None
    Description: Optional[str] = None


class AdminAccountSummary(BaseValidatorModel):
    AdminAccount: Optional[str] = None
    DefaultAdmin: Optional[bool] = None
    Status: Optional[OrganizationStatusType] = None


class OrganizationalUnitScopeOutput(BaseValidatorModel):
    OrganizationalUnits: Optional[List[str]] = None
    AllOrganizationalUnitsEnabled: Optional[bool] = None
    ExcludeSpecifiedOrganizationalUnits: Optional[bool] = None


class PolicyTypeScopeOutput(BaseValidatorModel):
    PolicyTypes: Optional[List[SecurityServiceTypeType]] = None
    AllPolicyTypesEnabled: Optional[bool] = None


class RegionScopeOutput(BaseValidatorModel):
    Regions: Optional[List[str]] = None
    AllRegionsEnabled: Optional[bool] = None


class OrganizationalUnitScope(BaseValidatorModel):
    OrganizationalUnits: Optional[List[str]] = None
    AllOrganizationalUnitsEnabled: Optional[bool] = None
    ExcludeSpecifiedOrganizationalUnits: Optional[bool] = None


class PolicyTypeScope(BaseValidatorModel):
    PolicyTypes: Optional[List[SecurityServiceTypeType]] = None
    AllPolicyTypesEnabled: Optional[bool] = None


class RegionScope(BaseValidatorModel):
    Regions: Optional[List[str]] = None
    AllRegionsEnabled: Optional[bool] = None


class App(BaseValidatorModel):
    AppName: str
    Protocol: str
    Port: int

Timestamp = Union[datetime, str]


# This class is the input for the 'associate_admin_account' function.
class AssociateAdminAccountRequest(BaseValidatorModel):
    AdminAccount: str


# This class is the input for the 'associate_third_party_firewall' function.
class AssociateThirdPartyFirewallRequest(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AwsEc2NetworkInterfaceViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolatingSecurityGroups: Optional[List[str]] = None


class PartialMatch(BaseValidatorModel):
    Reference: Optional[str] = None
    TargetViolationReasons: Optional[List[str]] = None


# This class is the input for the 'batch_associate_resource' function.
class BatchAssociateResourceRequest(BaseValidatorModel):
    ResourceSetIdentifier: str
    Items: List[str]


class FailedItem(BaseValidatorModel):
    URI: Optional[str] = None
    Reason: Optional[FailedItemReasonType] = None


# This class is the input for the 'batch_disassociate_resource' function.
class BatchDisassociateResourceRequest(BaseValidatorModel):
    ResourceSetIdentifier: str
    Items: List[str]


class ComplianceViolator(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ViolationReason: Optional[ViolationReasonType] = None
    ResourceType: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_apps_list' function.
class DeleteAppsListRequest(BaseValidatorModel):
    ListId: str


# This class is the input for the 'delete_policy' function.
class DeletePolicyRequest(BaseValidatorModel):
    PolicyId: str
    DeleteAllPolicyResources: Optional[bool] = None


# This class is the input for the 'delete_protocols_list' function.
class DeleteProtocolsListRequest(BaseValidatorModel):
    ListId: str


# This class is the input for the 'delete_resource_set' function.
class DeleteResourceSetRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'disassociate_third_party_firewall' function.
class DisassociateThirdPartyFirewallRequest(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType


class DiscoveredResource(BaseValidatorModel):
    URI: Optional[str] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None
    Name: Optional[str] = None


class DnsDuplicateRuleGroupViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None


class DnsRuleGroupLimitExceededViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    NumberOfRuleGroupsAlreadyAssociated: Optional[int] = None


class DnsRuleGroupPriorityConflictViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    ConflictingPriority: Optional[int] = None
    ConflictingPolicyId: Optional[str] = None
    UnavailablePriorities: Optional[List[int]] = None


class EvaluationResult(BaseValidatorModel):
    ComplianceStatus: Optional[PolicyComplianceStatusTypeType] = None
    ViolatorCount: Optional[int] = None
    EvaluationLimitExceeded: Optional[bool] = None


class ExpectedRoute(BaseValidatorModel):
    IpV4Cidr: Optional[str] = None
    PrefixListId: Optional[str] = None
    IpV6Cidr: Optional[str] = None
    ContributingSubnets: Optional[List[str]] = None
    AllowedTargets: Optional[List[str]] = None
    RouteTableId: Optional[str] = None


class FMSPolicyUpdateFirewallCreationConfigAction(BaseValidatorModel):
    Description: Optional[str] = None
    FirewallCreationConfig: Optional[str] = None


class FirewallSubnetIsOutOfScopeViolation(BaseValidatorModel):
    FirewallSubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None
    VpcEndpointId: Optional[str] = None


class FirewallSubnetMissingVPCEndpointViolation(BaseValidatorModel):
    FirewallSubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None


# This class is the input for the 'get_admin_scope' function.
class GetAdminScopeRequest(BaseValidatorModel):
    AdminAccount: str


# This class is the input for the 'get_apps_list' function.
class GetAppsListRequest(BaseValidatorModel):
    ListId: str
    DefaultList: Optional[bool] = None


# This class is the input for the 'get_compliance_detail' function.
class GetComplianceDetailRequest(BaseValidatorModel):
    PolicyId: str
    MemberAccount: str


# This class is the input for the 'get_policy' function.
class GetPolicyRequest(BaseValidatorModel):
    PolicyId: str


# This class is the input for the 'get_protocols_list' function.
class GetProtocolsListRequest(BaseValidatorModel):
    ListId: str
    DefaultList: Optional[bool] = None


class ProtocolsListDataOutput(BaseValidatorModel):
    ListName: str
    ProtocolsList: List[str]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    PreviousProtocolsList: Optional[Dict[str, List[str]]] = None


# This class is the input for the 'get_resource_set' function.
class GetResourceSetRequest(BaseValidatorModel):
    Identifier: str


class ResourceSetOutput(BaseValidatorModel):
    Name: str
    ResourceTypeList: List[str]
    Id: Optional[str] = None
    Description: Optional[str] = None
    UpdateToken: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None


# This class is the input for the 'get_third_party_firewall_association_status' function.
class GetThirdPartyFirewallAssociationStatusRequest(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType


# This class is the input for the 'get_violation_details' function.
class GetViolationDetailsRequest(BaseValidatorModel):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_admin_accounts_for_organization' function.
class ListAdminAccountsForOrganizationRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_admins_managing_account' function.
class ListAdminsManagingAccountRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_apps_lists' function.
class ListAppsListsRequest(BaseValidatorModel):
    MaxResults: int
    DefaultLists: Optional[bool] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_compliance_status' function.
class ListComplianceStatusRequest(BaseValidatorModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_discovered_resources' function.
class ListDiscoveredResourcesRequest(BaseValidatorModel):
    MemberAccountIds: List[str]
    ResourceType: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_member_accounts' function.
class ListMemberAccountsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_policies' function.
class ListPoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicySummary(BaseValidatorModel):
    PolicyArn: Optional[str] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    ResourceType: Optional[str] = None
    SecurityServiceType: Optional[SecurityServiceTypeType] = None
    RemediationEnabled: Optional[bool] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None


# This class is the input for the 'list_protocols_lists' function.
class ListProtocolsListsRequest(BaseValidatorModel):
    MaxResults: int
    DefaultLists: Optional[bool] = None
    NextToken: Optional[str] = None


class ProtocolsListDataSummary(BaseValidatorModel):
    ListArn: Optional[str] = None
    ListId: Optional[str] = None
    ListName: Optional[str] = None
    ProtocolsList: Optional[List[str]] = None


# This class is the input for the 'list_resource_set_resources' function.
class ListResourceSetResourcesRequest(BaseValidatorModel):
    Identifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Resource(BaseValidatorModel):
    URI: str
    AccountId: Optional[str] = None


# This class is the input for the 'list_resource_sets' function.
class ListResourceSetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceSetSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'list_third_party_firewall_firewall_policies' function.
class ListThirdPartyFirewallFirewallPoliciesRequest(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType
    MaxResults: int
    NextToken: Optional[str] = None


class ThirdPartyFirewallFirewallPolicy(BaseValidatorModel):
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None


class NetworkAclIcmpTypeCode(BaseValidatorModel):
    Code: Optional[int] = None
    Type: Optional[int] = None


class NetworkAclPortRange(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None


class Route(BaseValidatorModel):
    DestinationType: Optional[DestinationTypeType] = None
    TargetType: Optional[TargetTypeType] = None
    Destination: Optional[str] = None
    Target: Optional[str] = None


class NetworkFirewallMissingExpectedRTViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CurrentRouteTable: Optional[str] = None
    ExpectedRouteTable: Optional[str] = None


class NetworkFirewallMissingFirewallViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class NetworkFirewallMissingSubnetViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class StatefulEngineOptions(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None


class StatelessRuleGroup(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    Priority: Optional[int] = None


class NetworkFirewallPolicy(BaseValidatorModel):
    FirewallDeploymentModel: Optional[FirewallDeploymentModelType] = None


class NetworkFirewallStatefulRuleGroupOverride(BaseValidatorModel):
    Action: Optional[Literal['DROP_TO_ALERT']] = None


class ThirdPartyFirewallPolicy(BaseValidatorModel):
    FirewallDeploymentModel: Optional[FirewallDeploymentModelType] = None


class ResourceTag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


# This class is the input for the 'put_notification_channel' function.
class PutNotificationChannelRequest(BaseValidatorModel):
    SnsTopicArn: str
    SnsRoleName: str


class ThirdPartyFirewallMissingExpectedRouteTableViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CurrentRouteTable: Optional[str] = None
    ExpectedRouteTable: Optional[str] = None


class ThirdPartyFirewallMissingFirewallViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class ThirdPartyFirewallMissingSubnetViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class WebACLHasIncompatibleConfigurationViolation(BaseValidatorModel):
    WebACLArn: Optional[str] = None
    Description: Optional[str] = None


class WebACLHasOutOfScopeResourcesViolation(BaseValidatorModel):
    WebACLArn: Optional[str] = None
    OutOfScopeResourceList: Optional[List[str]] = None


class SecurityGroupRuleDescription(BaseValidatorModel):
    IPV4Range: Optional[str] = None
    IPV6Range: Optional[str] = None
    PrefixListId: Optional[str] = None
    Protocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class CreateNetworkAclAction(BaseValidatorModel):
    Description: Optional[str] = None
    Vpc: Optional[ActionTarget] = None
    FMSCanRemediate: Optional[bool] = None


class EC2AssociateRouteTableAction(BaseValidatorModel):
    RouteTableId: ActionTarget
    Description: Optional[str] = None
    SubnetId: Optional[ActionTarget] = None
    GatewayId: Optional[ActionTarget] = None


class EC2CopyRouteTableAction(BaseValidatorModel):
    VpcId: ActionTarget
    RouteTableId: ActionTarget
    Description: Optional[str] = None


class EC2CreateRouteAction(BaseValidatorModel):
    RouteTableId: ActionTarget
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    VpcEndpointId: Optional[ActionTarget] = None
    GatewayId: Optional[ActionTarget] = None


class EC2CreateRouteTableAction(BaseValidatorModel):
    VpcId: ActionTarget
    Description: Optional[str] = None


class EC2DeleteRouteAction(BaseValidatorModel):
    RouteTableId: ActionTarget
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None


class EC2ReplaceRouteAction(BaseValidatorModel):
    RouteTableId: ActionTarget
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    GatewayId: Optional[ActionTarget] = None


class EC2ReplaceRouteTableAssociationAction(BaseValidatorModel):
    AssociationId: ActionTarget
    RouteTableId: ActionTarget
    Description: Optional[str] = None


class ReplaceNetworkAclAssociationAction(BaseValidatorModel):
    Description: Optional[str] = None
    AssociationId: Optional[ActionTarget] = None
    NetworkAclId: Optional[ActionTarget] = None
    FMSCanRemediate: Optional[bool] = None


class AdminScopeOutput(BaseValidatorModel):
    AccountScope: Optional[AccountScopeOutput] = None
    OrganizationalUnitScope: Optional[OrganizationalUnitScopeOutput] = None
    RegionScope: Optional[RegionScopeOutput] = None
    PolicyTypeScope: Optional[PolicyTypeScopeOutput] = None


class AdminScope(BaseValidatorModel):
    AccountScope: Optional[AccountScope] = None
    OrganizationalUnitScope: Optional[OrganizationalUnitScope] = None
    RegionScope: Optional[RegionScope] = None
    PolicyTypeScope: Optional[PolicyTypeScope] = None


class AppsListDataOutput(BaseValidatorModel):
    ListName: str
    AppsList: List[App]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    PreviousAppsList: Optional[Dict[str, List[App]]] = None


class AppsListDataSummary(BaseValidatorModel):
    ListArn: Optional[str] = None
    ListId: Optional[str] = None
    ListName: Optional[str] = None
    AppsList: Optional[List[App]] = None


class AppsListData(BaseValidatorModel):
    ListName: str
    AppsList: List[App]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[Timestamp] = None
    LastUpdateTime: Optional[Timestamp] = None
    PreviousAppsList: Optional[Dict[str, List[App]]] = None


# This class is the input for the 'get_protection_status' function.
class GetProtectionStatusRequest(BaseValidatorModel):
    PolicyId: str
    MemberAccountId: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProtocolsListData(BaseValidatorModel):
    ListName: str
    ProtocolsList: List[str]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[Timestamp] = None
    LastUpdateTime: Optional[Timestamp] = None
    PreviousProtocolsList: Optional[Dict[str, List[str]]] = None


class ResourceSet(BaseValidatorModel):
    Name: str
    ResourceTypeList: List[str]
    Id: Optional[str] = None
    Description: Optional[str] = None
    UpdateToken: Optional[str] = None
    LastUpdateTime: Optional[Timestamp] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None


# This class is the output for the 'associate_third_party_firewall' function.
class AssociateThirdPartyFirewallResponse(BaseValidatorModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_third_party_firewall' function.
class DisassociateThirdPartyFirewallResponse(BaseValidatorModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_notification_channel' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAdminAccountResponse(BaseValidatorModel):
    AdminAccount: str
    RoleStatus: AccountRoleStatusType
    ResponseMetadata: ResponseMetadata


class GetNotificationChannelResponse(BaseValidatorModel):
    SnsTopicArn: str
    SnsRoleName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_protection_status' function.
class GetProtectionStatusResponse(BaseValidatorModel):
    AdminAccountId: str
    ServiceType: SecurityServiceTypeType
    Data: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_third_party_firewall_association_status' function.
class GetThirdPartyFirewallAssociationStatusResponse(BaseValidatorModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    MarketplaceOnboardingStatus: MarketplaceSubscriptionOnboardingStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_admin_accounts_for_organization' function.
class ListAdminAccountsForOrganizationResponse(BaseValidatorModel):
    AdminAccounts: List[AdminAccountSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_admins_managing_account' function.
class ListAdminsManagingAccountResponse(BaseValidatorModel):
    AdminAccounts: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_member_accounts' function.
class ListMemberAccountsResponse(BaseValidatorModel):
    MemberAccounts: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AwsEc2InstanceViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    AwsEc2NetworkInterfaceViolations: Optional[List[AwsEc2NetworkInterfaceViolation]] = None


# This class is the output for the 'batch_associate_resource' function.
class BatchAssociateResourceResponse(BaseValidatorModel):
    ResourceSetIdentifier: str
    FailedItems: List[FailedItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_resource' function.
class BatchDisassociateResourceResponse(BaseValidatorModel):
    ResourceSetIdentifier: str
    FailedItems: List[FailedItem]
    ResponseMetadata: ResponseMetadata


class PolicyComplianceDetail(BaseValidatorModel):
    PolicyOwner: Optional[str] = None
    PolicyId: Optional[str] = None
    MemberAccount: Optional[str] = None
    Violators: Optional[List[ComplianceViolator]] = None
    EvaluationLimitExceeded: Optional[bool] = None
    ExpiredAt: Optional[datetime] = None
    IssueInfoMap: Optional[Dict[DependentServiceNameType, str]] = None


# This class is the output for the 'list_discovered_resources' function.
class ListDiscoveredResourcesResponse(BaseValidatorModel):
    Items: List[DiscoveredResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PolicyComplianceStatus(BaseValidatorModel):
    PolicyOwner: Optional[str] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    MemberAccount: Optional[str] = None
    EvaluationResults: Optional[List[EvaluationResult]] = None
    LastUpdated: Optional[datetime] = None
    IssueInfoMap: Optional[Dict[DependentServiceNameType, str]] = None


class NetworkFirewallMissingExpectedRoutesViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ExpectedRoutes: Optional[List[ExpectedRoute]] = None
    VpcId: Optional[str] = None


# This class is the output for the 'get_protocols_list' function.
class GetProtocolsListResponse(BaseValidatorModel):
    ProtocolsList: ProtocolsListDataOutput
    ProtocolsListArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_protocols_list' function.
class PutProtocolsListResponse(BaseValidatorModel):
    ProtocolsList: ProtocolsListDataOutput
    ProtocolsListArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_set' function.
class GetResourceSetResponse(BaseValidatorModel):
    ResourceSet: ResourceSetOutput
    ResourceSetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_set' function.
class PutResourceSetResponse(BaseValidatorModel):
    ResourceSet: ResourceSetOutput
    ResourceSetArn: str
    ResponseMetadata: ResponseMetadata


class ListAdminAccountsForOrganizationRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAdminsManagingAccountRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAppsListsRequestPaginate(BaseValidatorModel):
    DefaultLists: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComplianceStatusRequestPaginate(BaseValidatorModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMemberAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtocolsListsRequestPaginate(BaseValidatorModel):
    DefaultLists: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThirdPartyFirewallFirewallPoliciesRequestPaginate(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_policies' function.
class ListPoliciesResponse(BaseValidatorModel):
    PolicyList: List[PolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_protocols_lists' function.
class ListProtocolsListsResponse(BaseValidatorModel):
    ProtocolsLists: List[ProtocolsListDataSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_resource_set_resources' function.
class ListResourceSetResourcesResponse(BaseValidatorModel):
    Items: List[Resource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_resource_sets' function.
class ListResourceSetsResponse(BaseValidatorModel):
    ResourceSets: List[ResourceSetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagList: List[Tag]


# This class is the output for the 'list_third_party_firewall_firewall_policies' function.
class ListThirdPartyFirewallFirewallPoliciesResponse(BaseValidatorModel):
    ThirdPartyFirewallFirewallPolicies: List[ThirdPartyFirewallFirewallPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NetworkAclEntry(BaseValidatorModel):
    Protocol: str
    RuleAction: NetworkAclRuleActionType
    Egress: bool
    IcmpTypeCode: Optional[NetworkAclIcmpTypeCode] = None
    PortRange: Optional[NetworkAclPortRange] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None


class NetworkFirewallBlackHoleRouteDetectedViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    RouteTableId: Optional[str] = None
    VpcId: Optional[str] = None
    ViolatingRoutes: Optional[List[Route]] = None


class NetworkFirewallInternetTrafficNotInspectedViolation(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    RouteTableId: Optional[str] = None
    ViolatingRoutes: Optional[List[Route]] = None
    IsRouteTableUsedInDifferentAZ: Optional[bool] = None
    CurrentFirewallSubnetRouteTable: Optional[str] = None
    ExpectedFirewallEndpoint: Optional[str] = None
    FirewallSubnetId: Optional[str] = None
    ExpectedFirewallSubnetRoutes: Optional[List[ExpectedRoute]] = None
    ActualFirewallSubnetRoutes: Optional[List[Route]] = None
    InternetGatewayId: Optional[str] = None
    CurrentInternetGatewayRouteTable: Optional[str] = None
    ExpectedInternetGatewayRoutes: Optional[List[ExpectedRoute]] = None
    ActualInternetGatewayRoutes: Optional[List[Route]] = None
    VpcId: Optional[str] = None


class NetworkFirewallInvalidRouteConfigurationViolation(BaseValidatorModel):
    AffectedSubnets: Optional[List[str]] = None
    RouteTableId: Optional[str] = None
    IsRouteTableUsedInDifferentAZ: Optional[bool] = None
    ViolatingRoute: Optional[Route] = None
    CurrentFirewallSubnetRouteTable: Optional[str] = None
    ExpectedFirewallEndpoint: Optional[str] = None
    ActualFirewallEndpoint: Optional[str] = None
    ExpectedFirewallSubnetId: Optional[str] = None
    ActualFirewallSubnetId: Optional[str] = None
    ExpectedFirewallSubnetRoutes: Optional[List[ExpectedRoute]] = None
    ActualFirewallSubnetRoutes: Optional[List[Route]] = None
    InternetGatewayId: Optional[str] = None
    CurrentInternetGatewayRouteTable: Optional[str] = None
    ExpectedInternetGatewayRoutes: Optional[List[ExpectedRoute]] = None
    ActualInternetGatewayRoutes: Optional[List[Route]] = None
    VpcId: Optional[str] = None


class NetworkFirewallUnexpectedFirewallRoutesViolation(BaseValidatorModel):
    FirewallSubnetId: Optional[str] = None
    ViolatingRoutes: Optional[List[Route]] = None
    RouteTableId: Optional[str] = None
    FirewallEndpoint: Optional[str] = None
    VpcId: Optional[str] = None


class NetworkFirewallUnexpectedGatewayRoutesViolation(BaseValidatorModel):
    GatewayId: Optional[str] = None
    ViolatingRoutes: Optional[List[Route]] = None
    RouteTableId: Optional[str] = None
    VpcId: Optional[str] = None


class RouteHasOutOfScopeEndpointViolation(BaseValidatorModel):
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    RouteTableId: Optional[str] = None
    ViolatingRoutes: Optional[List[Route]] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None
    CurrentFirewallSubnetRouteTable: Optional[str] = None
    FirewallSubnetId: Optional[str] = None
    FirewallSubnetRoutes: Optional[List[Route]] = None
    InternetGatewayId: Optional[str] = None
    CurrentInternetGatewayRouteTable: Optional[str] = None
    InternetGatewayRoutes: Optional[List[Route]] = None


class StatefulRuleGroup(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    Priority: Optional[int] = None
    Override: Optional[NetworkFirewallStatefulRuleGroupOverride] = None


class SecurityGroupRemediationAction(BaseValidatorModel):
    RemediationActionType: Optional[RemediationActionTypeType] = None
    Description: Optional[str] = None
    RemediationResult: Optional[SecurityGroupRuleDescription] = None
    IsDefaultAction: Optional[bool] = None


# This class is the output for the 'get_admin_scope' function.
class GetAdminScopeResponse(BaseValidatorModel):
    AdminScope: AdminScopeOutput
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadata

AdminScopeUnion = Union[AdminScope, AdminScopeOutput]


# This class is the output for the 'get_apps_list' function.
class GetAppsListResponse(BaseValidatorModel):
    AppsList: AppsListDataOutput
    AppsListArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_apps_list' function.
class PutAppsListResponse(BaseValidatorModel):
    AppsList: AppsListDataOutput
    AppsListArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_apps_lists' function.
class ListAppsListsResponse(BaseValidatorModel):
    AppsLists: List[AppsListDataSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

AppsListDataUnion = Union[AppsListData, AppsListDataOutput]

ProtocolsListDataUnion = Union[ProtocolsListData, ProtocolsListDataOutput]

ResourceSetUnion = Union[ResourceSet, ResourceSetOutput]


# This class is the output for the 'get_compliance_detail' function.
class GetComplianceDetailResponse(BaseValidatorModel):
    PolicyComplianceDetail: PolicyComplianceDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_compliance_status' function.
class ListComplianceStatusResponse(BaseValidatorModel):
    PolicyComplianceStatusList: List[PolicyComplianceStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EntryDescription(BaseValidatorModel):
    EntryDetail: Optional[NetworkAclEntry] = None
    EntryRuleNumber: Optional[int] = None
    EntryType: Optional[EntryTypeType] = None


class NetworkAclEntrySetOutput(BaseValidatorModel):
    ForceRemediateForFirstEntries: bool
    ForceRemediateForLastEntries: bool
    FirstEntries: Optional[List[NetworkAclEntry]] = None
    LastEntries: Optional[List[NetworkAclEntry]] = None


class NetworkAclEntrySet(BaseValidatorModel):
    ForceRemediateForFirstEntries: bool
    ForceRemediateForLastEntries: bool
    FirstEntries: Optional[List[NetworkAclEntry]] = None
    LastEntries: Optional[List[NetworkAclEntry]] = None


class NetworkFirewallPolicyDescription(BaseValidatorModel):
    StatelessRuleGroups: Optional[List[StatelessRuleGroup]] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessCustomActions: Optional[List[str]] = None
    StatefulRuleGroups: Optional[List[StatefulRuleGroup]] = None
    StatefulDefaultActions: Optional[List[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptions] = None


class AwsVPCSecurityGroupViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    PartialMatches: Optional[List[PartialMatch]] = None
    PossibleSecurityGroupRemediationActions: Optional[List[SecurityGroupRemediationAction]] = None


# This class is the input for the 'put_admin_account' function.
class PutAdminAccountRequest(BaseValidatorModel):
    AdminAccount: str
    AdminScope: Optional[AdminScopeUnion] = None


# This class is the input for the 'put_apps_list' function.
class PutAppsListRequest(BaseValidatorModel):
    AppsList: AppsListDataUnion
    TagList: Optional[List[Tag]] = None


# This class is the input for the 'put_protocols_list' function.
class PutProtocolsListRequest(BaseValidatorModel):
    ProtocolsList: ProtocolsListDataUnion
    TagList: Optional[List[Tag]] = None


# This class is the input for the 'put_resource_set' function.
class PutResourceSetRequest(BaseValidatorModel):
    ResourceSet: ResourceSetUnion
    TagList: Optional[List[Tag]] = None


class CreateNetworkAclEntriesAction(BaseValidatorModel):
    Description: Optional[str] = None
    NetworkAclId: Optional[ActionTarget] = None
    NetworkAclEntriesToBeCreated: Optional[List[EntryDescription]] = None
    FMSCanRemediate: Optional[bool] = None


class DeleteNetworkAclEntriesAction(BaseValidatorModel):
    Description: Optional[str] = None
    NetworkAclId: Optional[ActionTarget] = None
    NetworkAclEntriesToBeDeleted: Optional[List[EntryDescription]] = None
    FMSCanRemediate: Optional[bool] = None


class EntryViolation(BaseValidatorModel):
    ExpectedEntry: Optional[EntryDescription] = None
    ExpectedEvaluationOrder: Optional[str] = None
    ActualEvaluationOrder: Optional[str] = None
    EntryAtExpectedEvaluationOrder: Optional[EntryDescription] = None
    EntriesWithConflicts: Optional[List[EntryDescription]] = None
    EntryViolationReasons: Optional[List[EntryViolationReasonType]] = None


class NetworkAclCommonPolicyOutput(BaseValidatorModel):
    NetworkAclEntrySet: NetworkAclEntrySetOutput


class NetworkAclCommonPolicy(BaseValidatorModel):
    NetworkAclEntrySet: NetworkAclEntrySet


class NetworkFirewallPolicyModifiedViolation(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    CurrentPolicyDescription: Optional[NetworkFirewallPolicyDescription] = None
    ExpectedPolicyDescription: Optional[NetworkFirewallPolicyDescription] = None


class RemediationAction(BaseValidatorModel):
    Description: Optional[str] = None
    EC2CreateRouteAction: Optional[EC2CreateRouteAction] = None
    EC2ReplaceRouteAction: Optional[EC2ReplaceRouteAction] = None
    EC2DeleteRouteAction: Optional[EC2DeleteRouteAction] = None
    EC2CopyRouteTableAction: Optional[EC2CopyRouteTableAction] = None
    EC2ReplaceRouteTableAssociationAction: Optional[EC2ReplaceRouteTableAssociationAction] = None
    EC2AssociateRouteTableAction: Optional[EC2AssociateRouteTableAction] = None
    EC2CreateRouteTableAction: Optional[EC2CreateRouteTableAction] = None
    FMSPolicyUpdateFirewallCreationConfigAction: Optional[FMSPolicyUpdateFirewallCreationConfigAction] = None
    CreateNetworkAclAction: Optional[CreateNetworkAclAction] = None
    ReplaceNetworkAclAssociationAction: Optional[ReplaceNetworkAclAssociationAction] = None
    CreateNetworkAclEntriesAction: Optional[CreateNetworkAclEntriesAction] = None
    DeleteNetworkAclEntriesAction: Optional[DeleteNetworkAclEntriesAction] = None


class InvalidNetworkAclEntriesViolation(BaseValidatorModel):
    Vpc: Optional[str] = None
    Subnet: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    CurrentAssociatedNetworkAcl: Optional[str] = None
    EntryViolations: Optional[List[EntryViolation]] = None


class PolicyOptionOutput(BaseValidatorModel):
    NetworkFirewallPolicy: Optional[NetworkFirewallPolicy] = None
    ThirdPartyFirewallPolicy: Optional[ThirdPartyFirewallPolicy] = None
    NetworkAclCommonPolicy: Optional[NetworkAclCommonPolicyOutput] = None


class PolicyOption(BaseValidatorModel):
    NetworkFirewallPolicy: Optional[NetworkFirewallPolicy] = None
    ThirdPartyFirewallPolicy: Optional[ThirdPartyFirewallPolicy] = None
    NetworkAclCommonPolicy: Optional[NetworkAclCommonPolicy] = None


class RemediationActionWithOrder(BaseValidatorModel):
    RemediationAction: Optional[RemediationAction] = None
    Order: Optional[int] = None


class SecurityServicePolicyDataOutput(BaseValidatorModel):
    Type: SecurityServiceTypeType
    ManagedServiceData: Optional[str] = None
    PolicyOption: Optional[PolicyOptionOutput] = None


class SecurityServicePolicyData(BaseValidatorModel):
    Type: SecurityServiceTypeType
    ManagedServiceData: Optional[str] = None
    PolicyOption: Optional[PolicyOption] = None


class PossibleRemediationAction(BaseValidatorModel):
    OrderedRemediationActions: List[RemediationActionWithOrder]
    Description: Optional[str] = None
    IsDefaultAction: Optional[bool] = None


class PolicyOutput(BaseValidatorModel):
    PolicyName: str
    SecurityServicePolicyData: SecurityServicePolicyDataOutput
    ResourceType: str
    ExcludeResourceTags: bool
    RemediationEnabled: bool
    PolicyId: Optional[str] = None
    PolicyUpdateToken: Optional[str] = None
    ResourceTypeList: Optional[List[str]] = None
    ResourceTags: Optional[List[ResourceTag]] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    IncludeMap: Optional[Dict[CustomerPolicyScopeIdTypeType, List[str]]] = None
    ExcludeMap: Optional[Dict[CustomerPolicyScopeIdTypeType, List[str]]] = None
    ResourceSetIds: Optional[List[str]] = None
    PolicyDescription: Optional[str] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None
    ResourceTagLogicalOperator: Optional[ResourceTagLogicalOperatorType] = None


class Policy(BaseValidatorModel):
    PolicyName: str
    SecurityServicePolicyData: SecurityServicePolicyData
    ResourceType: str
    ExcludeResourceTags: bool
    RemediationEnabled: bool
    PolicyId: Optional[str] = None
    PolicyUpdateToken: Optional[str] = None
    ResourceTypeList: Optional[List[str]] = None
    ResourceTags: Optional[List[ResourceTag]] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    IncludeMap: Optional[Dict[CustomerPolicyScopeIdTypeType, List[str]]] = None
    ExcludeMap: Optional[Dict[CustomerPolicyScopeIdTypeType, List[str]]] = None
    ResourceSetIds: Optional[List[str]] = None
    PolicyDescription: Optional[str] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None
    ResourceTagLogicalOperator: Optional[ResourceTagLogicalOperatorType] = None


class PossibleRemediationActions(BaseValidatorModel):
    Description: Optional[str] = None
    Actions: Optional[List[PossibleRemediationAction]] = None


# This class is the output for the 'get_policy' function.
class GetPolicyResponse(BaseValidatorModel):
    Policy: PolicyOutput
    PolicyArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_policy' function.
class PutPolicyResponse(BaseValidatorModel):
    Policy: PolicyOutput
    PolicyArn: str
    ResponseMetadata: ResponseMetadata

PolicyUnion = Union[Policy, PolicyOutput]


class ResourceViolation(BaseValidatorModel):
    AwsVPCSecurityGroupViolation: Optional[AwsVPCSecurityGroupViolation] = None
    AwsEc2NetworkInterfaceViolation: Optional[AwsEc2NetworkInterfaceViolation] = None
    AwsEc2InstanceViolation: Optional[AwsEc2InstanceViolation] = None
    NetworkFirewallMissingFirewallViolation: Optional[NetworkFirewallMissingFirewallViolation] = None
    NetworkFirewallMissingSubnetViolation: Optional[NetworkFirewallMissingSubnetViolation] = None
    NetworkFirewallMissingExpectedRTViolation: Optional[NetworkFirewallMissingExpectedRTViolation] = None
    NetworkFirewallPolicyModifiedViolation: Optional[NetworkFirewallPolicyModifiedViolation] = None
    NetworkFirewallInternetTrafficNotInspectedViolation: Optional[NetworkFirewallInternetTrafficNotInspectedViolation] = None
    NetworkFirewallInvalidRouteConfigurationViolation: Optional[NetworkFirewallInvalidRouteConfigurationViolation] = None
    NetworkFirewallBlackHoleRouteDetectedViolation: Optional[NetworkFirewallBlackHoleRouteDetectedViolation] = None
    NetworkFirewallUnexpectedFirewallRoutesViolation: Optional[NetworkFirewallUnexpectedFirewallRoutesViolation] = None
    NetworkFirewallUnexpectedGatewayRoutesViolation: Optional[NetworkFirewallUnexpectedGatewayRoutesViolation] = None
    NetworkFirewallMissingExpectedRoutesViolation: Optional[NetworkFirewallMissingExpectedRoutesViolation] = None
    DnsRuleGroupPriorityConflictViolation: Optional[DnsRuleGroupPriorityConflictViolation] = None
    DnsDuplicateRuleGroupViolation: Optional[DnsDuplicateRuleGroupViolation] = None
    DnsRuleGroupLimitExceededViolation: Optional[DnsRuleGroupLimitExceededViolation] = None
    FirewallSubnetIsOutOfScopeViolation: Optional[FirewallSubnetIsOutOfScopeViolation] = None
    RouteHasOutOfScopeEndpointViolation: Optional[RouteHasOutOfScopeEndpointViolation] = None
    ThirdPartyFirewallMissingFirewallViolation: Optional[ThirdPartyFirewallMissingFirewallViolation] = None
    ThirdPartyFirewallMissingSubnetViolation: Optional[ThirdPartyFirewallMissingSubnetViolation] = None
    ThirdPartyFirewallMissingExpectedRouteTableViolation: Optional[ThirdPartyFirewallMissingExpectedRouteTableViolation] = None
    FirewallSubnetMissingVPCEndpointViolation: Optional[FirewallSubnetMissingVPCEndpointViolation] = None
    InvalidNetworkAclEntriesViolation: Optional[InvalidNetworkAclEntriesViolation] = None
    PossibleRemediationActions: Optional[PossibleRemediationActions] = None
    WebACLHasIncompatibleConfigurationViolation: Optional[WebACLHasIncompatibleConfigurationViolation] = None
    WebACLHasOutOfScopeResourcesViolation: Optional[WebACLHasOutOfScopeResourcesViolation] = None


# This class is the input for the 'put_policy' function.
class PutPolicyRequest(BaseValidatorModel):
    Policy: PolicyUnion
    TagList: Optional[List[Tag]] = None


class ViolationDetail(BaseValidatorModel):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str
    ResourceViolations: List[ResourceViolation]
    ResourceTags: Optional[List[Tag]] = None
    ResourceDescription: Optional[str] = None


# This class is the output for the 'get_violation_details' function.
class GetViolationDetailsResponse(BaseValidatorModel):
    ViolationDetail: ViolationDetail
    ResponseMetadata: ResponseMetadata