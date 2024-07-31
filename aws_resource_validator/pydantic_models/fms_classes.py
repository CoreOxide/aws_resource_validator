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
from aws_resource_validator.pydantic_models.fms_constants import *

class AccountScopeOutputTypeDef(BaseModel):
    Accounts: Optional[List[str]] = None
    AllAccountsEnabled: Optional[bool] = None
    ExcludeSpecifiedAccounts: Optional[bool] = None

class AccountScopeTypeDef(BaseModel):
    Accounts: Optional[Sequence[str]] = None
    AllAccountsEnabled: Optional[bool] = None
    ExcludeSpecifiedAccounts: Optional[bool] = None

class ActionTargetTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    Description: Optional[str] = None

class AdminAccountSummaryTypeDef(BaseModel):
    AdminAccount: Optional[str] = None
    DefaultAdmin: Optional[bool] = None
    Status: Optional[OrganizationStatusType] = None

class OrganizationalUnitScopeOutputTypeDef(BaseModel):
    OrganizationalUnits: Optional[List[str]] = None
    AllOrganizationalUnitsEnabled: Optional[bool] = None
    ExcludeSpecifiedOrganizationalUnits: Optional[bool] = None

class PolicyTypeScopeOutputTypeDef(BaseModel):
    PolicyTypes: Optional[List[SecurityServiceTypeType]] = None
    AllPolicyTypesEnabled: Optional[bool] = None

class RegionScopeOutputTypeDef(BaseModel):
    Regions: Optional[List[str]] = None
    AllRegionsEnabled: Optional[bool] = None

class OrganizationalUnitScopeTypeDef(BaseModel):
    OrganizationalUnits: Optional[Sequence[str]] = None
    AllOrganizationalUnitsEnabled: Optional[bool] = None
    ExcludeSpecifiedOrganizationalUnits: Optional[bool] = None

class PolicyTypeScopeTypeDef(BaseModel):
    PolicyTypes: Optional[Sequence[SecurityServiceTypeType]] = None
    AllPolicyTypesEnabled: Optional[bool] = None

class RegionScopeTypeDef(BaseModel):
    Regions: Optional[Sequence[str]] = None
    AllRegionsEnabled: Optional[bool] = None

class AppTypeDef(BaseModel):
    AppName: str
    Protocol: str
    Port: int

class AssociateAdminAccountRequestRequestTypeDef(BaseModel):
    AdminAccount: str

class AssociateThirdPartyFirewallRequestRequestTypeDef(BaseModel):
    ThirdPartyFirewall: ThirdPartyFirewallType

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AwsEc2NetworkInterfaceViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    ViolatingSecurityGroups: Optional[List[str]] = None

class PartialMatchTypeDef(BaseModel):
    Reference: Optional[str] = None
    TargetViolationReasons: Optional[List[str]] = None

class BatchAssociateResourceRequestRequestTypeDef(BaseModel):
    ResourceSetIdentifier: str
    Items: Sequence[str]

class FailedItemTypeDef(BaseModel):
    URI: Optional[str] = None
    Reason: Optional[FailedItemReasonType] = None

class BatchDisassociateResourceRequestRequestTypeDef(BaseModel):
    ResourceSetIdentifier: str
    Items: Sequence[str]

class ComplianceViolatorTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ViolationReason: Optional[ViolationReasonType] = None
    ResourceType: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None

class DeleteAppsListRequestRequestTypeDef(BaseModel):
    ListId: str

class DeletePolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str
    DeleteAllPolicyResources: Optional[bool] = None

class DeleteProtocolsListRequestRequestTypeDef(BaseModel):
    ListId: str

class DeleteResourceSetRequestRequestTypeDef(BaseModel):
    Identifier: str

class DisassociateThirdPartyFirewallRequestRequestTypeDef(BaseModel):
    ThirdPartyFirewall: ThirdPartyFirewallType

class DiscoveredResourceTypeDef(BaseModel):
    URI: Optional[str] = None
    AccountId: Optional[str] = None
    Type: Optional[str] = None
    Name: Optional[str] = None

class DnsDuplicateRuleGroupViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None

class DnsRuleGroupLimitExceededViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    NumberOfRuleGroupsAlreadyAssociated: Optional[int] = None

class DnsRuleGroupPriorityConflictViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    ConflictingPriority: Optional[int] = None
    ConflictingPolicyId: Optional[str] = None
    UnavailablePriorities: Optional[List[int]] = None

class EvaluationResultTypeDef(BaseModel):
    ComplianceStatus: Optional[PolicyComplianceStatusTypeType] = None
    ViolatorCount: Optional[int] = None
    EvaluationLimitExceeded: Optional[bool] = None

class ExpectedRouteTypeDef(BaseModel):
    IpV4Cidr: Optional[str] = None
    PrefixListId: Optional[str] = None
    IpV6Cidr: Optional[str] = None
    ContributingSubnets: Optional[List[str]] = None
    AllowedTargets: Optional[List[str]] = None
    RouteTableId: Optional[str] = None

class FMSPolicyUpdateFirewallCreationConfigActionTypeDef(BaseModel):
    Description: Optional[str] = None
    FirewallCreationConfig: Optional[str] = None

class FirewallSubnetIsOutOfScopeViolationTypeDef(BaseModel):
    FirewallSubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None
    VpcEndpointId: Optional[str] = None

class FirewallSubnetMissingVPCEndpointViolationTypeDef(BaseModel):
    FirewallSubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None

class GetAdminScopeRequestRequestTypeDef(BaseModel):
    AdminAccount: str

class GetAppsListRequestRequestTypeDef(BaseModel):
    ListId: str
    DefaultList: Optional[bool] = None

class GetComplianceDetailRequestRequestTypeDef(BaseModel):
    PolicyId: str
    MemberAccount: str

class GetPolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str

class GetProtocolsListRequestRequestTypeDef(BaseModel):
    ListId: str
    DefaultList: Optional[bool] = None

class ProtocolsListDataOutputTypeDef(BaseModel):
    ListName: str
    ProtocolsList: List[str]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    PreviousProtocolsList: Optional[Dict[str, List[str]]] = None

class GetResourceSetRequestRequestTypeDef(BaseModel):
    Identifier: str

class ResourceSetOutputTypeDef(BaseModel):
    Name: str
    ResourceTypeList: List[str]
    Id: Optional[str] = None
    Description: Optional[str] = None
    UpdateToken: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None

class GetThirdPartyFirewallAssociationStatusRequestRequestTypeDef(BaseModel):
    ThirdPartyFirewall: ThirdPartyFirewallType

class GetViolationDetailsRequestRequestTypeDef(BaseModel):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAdminAccountsForOrganizationRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAdminsManagingAccountRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAppsListsRequestRequestTypeDef(BaseModel):
    MaxResults: int
    DefaultLists: Optional[bool] = None
    NextToken: Optional[str] = None

class ListComplianceStatusRequestRequestTypeDef(BaseModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDiscoveredResourcesRequestRequestTypeDef(BaseModel):
    MemberAccountIds: Sequence[str]
    ResourceType: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMemberAccountsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPoliciesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicySummaryTypeDef(BaseModel):
    PolicyArn: Optional[str] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    ResourceType: Optional[str] = None
    SecurityServiceType: Optional[SecurityServiceTypeType] = None
    RemediationEnabled: Optional[bool] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None

class ListProtocolsListsRequestRequestTypeDef(BaseModel):
    MaxResults: int
    DefaultLists: Optional[bool] = None
    NextToken: Optional[str] = None

class ProtocolsListDataSummaryTypeDef(BaseModel):
    ListArn: Optional[str] = None
    ListId: Optional[str] = None
    ListName: Optional[str] = None
    ProtocolsList: Optional[List[str]] = None

class ListResourceSetResourcesRequestRequestTypeDef(BaseModel):
    Identifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResourceTypeDef(BaseModel):
    URI: str
    AccountId: Optional[str] = None

class ListResourceSetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResourceSetSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ListThirdPartyFirewallFirewallPoliciesRequestRequestTypeDef(BaseModel):
    ThirdPartyFirewall: ThirdPartyFirewallType
    MaxResults: int
    NextToken: Optional[str] = None

class ThirdPartyFirewallFirewallPolicyTypeDef(BaseModel):
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None

class NetworkAclIcmpTypeCodeTypeDef(BaseModel):
    Code: Optional[int] = None
    Type: Optional[int] = None

class NetworkAclPortRangeTypeDef(BaseModel):
    From: Optional[int] = None
    To: Optional[int] = None

class RouteTypeDef(BaseModel):
    DestinationType: Optional[DestinationTypeType] = None
    TargetType: Optional[TargetTypeType] = None
    Destination: Optional[str] = None
    Target: Optional[str] = None

class NetworkFirewallMissingExpectedRTViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CurrentRouteTable: Optional[str] = None
    ExpectedRouteTable: Optional[str] = None

class NetworkFirewallMissingFirewallViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None

class NetworkFirewallMissingSubnetViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None

class StatefulEngineOptionsTypeDef(BaseModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None

class StatelessRuleGroupTypeDef(BaseModel):
    RuleGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    Priority: Optional[int] = None

class NetworkFirewallPolicyTypeDef(BaseModel):
    FirewallDeploymentModel: Optional[FirewallDeploymentModelType] = None

class NetworkFirewallStatefulRuleGroupOverrideTypeDef(BaseModel):
    Action: Optional[Literal["DROP_TO_ALERT"]] = None

class ThirdPartyFirewallPolicyTypeDef(BaseModel):
    FirewallDeploymentModel: Optional[FirewallDeploymentModelType] = None

class ResourceTagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class PutNotificationChannelRequestRequestTypeDef(BaseModel):
    SnsTopicArn: str
    SnsRoleName: str

class ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CurrentRouteTable: Optional[str] = None
    ExpectedRouteTable: Optional[str] = None

class ThirdPartyFirewallMissingFirewallViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None

class ThirdPartyFirewallMissingSubnetViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None

class SecurityGroupRuleDescriptionTypeDef(BaseModel):
    IPV4Range: Optional[str] = None
    IPV6Range: Optional[str] = None
    PrefixListId: Optional[str] = None
    Protocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateNetworkAclActionTypeDef(BaseModel):
    Description: Optional[str] = None
    Vpc: Optional[ActionTargetTypeDef] = None
    FMSCanRemediate: Optional[bool] = None

class EC2AssociateRouteTableActionTypeDef(BaseModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    SubnetId: Optional[ActionTargetTypeDef] = None
    GatewayId: Optional[ActionTargetTypeDef] = None

class EC2CopyRouteTableActionTypeDef(BaseModel):
    VpcId: ActionTargetTypeDef
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None

class EC2CreateRouteActionTypeDef(BaseModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    VpcEndpointId: Optional[ActionTargetTypeDef] = None
    GatewayId: Optional[ActionTargetTypeDef] = None

class EC2CreateRouteTableActionTypeDef(BaseModel):
    VpcId: ActionTargetTypeDef
    Description: Optional[str] = None

class EC2DeleteRouteActionTypeDef(BaseModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None

class EC2ReplaceRouteActionTypeDef(BaseModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    GatewayId: Optional[ActionTargetTypeDef] = None

class EC2ReplaceRouteTableAssociationActionTypeDef(BaseModel):
    AssociationId: ActionTargetTypeDef
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None

class ReplaceNetworkAclAssociationActionTypeDef(BaseModel):
    Description: Optional[str] = None
    AssociationId: Optional[ActionTargetTypeDef] = None
    NetworkAclId: Optional[ActionTargetTypeDef] = None
    FMSCanRemediate: Optional[bool] = None

class AdminScopeOutputTypeDef(BaseModel):
    AccountScope: Optional[AccountScopeOutputTypeDef] = None
    OrganizationalUnitScope: Optional[OrganizationalUnitScopeOutputTypeDef] = None
    RegionScope: Optional[RegionScopeOutputTypeDef] = None
    PolicyTypeScope: Optional[PolicyTypeScopeOutputTypeDef] = None

class AdminScopeTypeDef(BaseModel):
    AccountScope: Optional[AccountScopeTypeDef] = None
    OrganizationalUnitScope: Optional[OrganizationalUnitScopeTypeDef] = None
    RegionScope: Optional[RegionScopeTypeDef] = None
    PolicyTypeScope: Optional[PolicyTypeScopeTypeDef] = None

class AppsListDataOutputTypeDef(BaseModel):
    ListName: str
    AppsList: List[AppTypeDef]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    PreviousAppsList: Optional[Dict[str, List[AppTypeDef]]] = None

class AppsListDataSummaryTypeDef(BaseModel):
    ListArn: Optional[str] = None
    ListId: Optional[str] = None
    ListName: Optional[str] = None
    AppsList: Optional[List[AppTypeDef]] = None

class AppsListDataTypeDef(BaseModel):
    ListName: str
    AppsList: Sequence[AppTypeDef]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[TimestampTypeDef] = None
    LastUpdateTime: Optional[TimestampTypeDef] = None
    PreviousAppsList: Optional[Mapping[str, Sequence[AppTypeDef]]] = None

class GetProtectionStatusRequestRequestTypeDef(BaseModel):
    PolicyId: str
    MemberAccountId: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProtocolsListDataTypeDef(BaseModel):
    ListName: str
    ProtocolsList: Sequence[str]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[TimestampTypeDef] = None
    LastUpdateTime: Optional[TimestampTypeDef] = None
    PreviousProtocolsList: Optional[Mapping[str, Sequence[str]]] = None

class ResourceSetTypeDef(BaseModel):
    Name: str
    ResourceTypeList: Sequence[str]
    Id: Optional[str] = None
    Description: Optional[str] = None
    UpdateToken: Optional[str] = None
    LastUpdateTime: Optional[TimestampTypeDef] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None

class AssociateThirdPartyFirewallResponseTypeDef(BaseModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateThirdPartyFirewallResponseTypeDef(BaseModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAdminAccountResponseTypeDef(BaseModel):
    AdminAccount: str
    RoleStatus: AccountRoleStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotificationChannelResponseTypeDef(BaseModel):
    SnsTopicArn: str
    SnsRoleName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProtectionStatusResponseTypeDef(BaseModel):
    AdminAccountId: str
    ServiceType: SecurityServiceTypeType
    Data: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetThirdPartyFirewallAssociationStatusResponseTypeDef(BaseModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    MarketplaceOnboardingStatus: MarketplaceSubscriptionOnboardingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListAdminAccountsForOrganizationResponseTypeDef(BaseModel):
    AdminAccounts: List[AdminAccountSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAdminsManagingAccountResponseTypeDef(BaseModel):
    AdminAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMemberAccountsResponseTypeDef(BaseModel):
    MemberAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AwsEc2InstanceViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    AwsEc2NetworkInterfaceViolations: Optional[       List[AwsEc2NetworkInterfaceViolationTypeDef]     ] = None

class BatchAssociateResourceResponseTypeDef(BaseModel):
    ResourceSetIdentifier: str
    FailedItems: List[FailedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateResourceResponseTypeDef(BaseModel):
    ResourceSetIdentifier: str
    FailedItems: List[FailedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyComplianceDetailTypeDef(BaseModel):
    PolicyOwner: Optional[str] = None
    PolicyId: Optional[str] = None
    MemberAccount: Optional[str] = None
    Violators: Optional[List[ComplianceViolatorTypeDef]] = None
    EvaluationLimitExceeded: Optional[bool] = None
    ExpiredAt: Optional[datetime] = None
    IssueInfoMap: Optional[Dict[DependentServiceNameType, str]] = None

class ListDiscoveredResourcesResponseTypeDef(BaseModel):
    Items: List[DiscoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PolicyComplianceStatusTypeDef(BaseModel):
    PolicyOwner: Optional[str] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    MemberAccount: Optional[str] = None
    EvaluationResults: Optional[List[EvaluationResultTypeDef]] = None
    LastUpdated: Optional[datetime] = None
    IssueInfoMap: Optional[Dict[DependentServiceNameType, str]] = None

class NetworkFirewallMissingExpectedRoutesViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    ExpectedRoutes: Optional[List[ExpectedRouteTypeDef]] = None
    VpcId: Optional[str] = None

class GetProtocolsListResponseTypeDef(BaseModel):
    ProtocolsList: ProtocolsListDataOutputTypeDef
    ProtocolsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutProtocolsListResponseTypeDef(BaseModel):
    ProtocolsList: ProtocolsListDataOutputTypeDef
    ProtocolsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSetResponseTypeDef(BaseModel):
    ResourceSet: ResourceSetOutputTypeDef
    ResourceSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourceSetResponseTypeDef(BaseModel):
    ResourceSet: ResourceSetOutputTypeDef
    ResourceSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAdminAccountsForOrganizationRequestListAdminAccountsForOrganizationPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAdminsManagingAccountRequestListAdminsManagingAccountPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppsListsRequestListAppsListsPaginateTypeDef(BaseModel):
    DefaultLists: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComplianceStatusRequestListComplianceStatusPaginateTypeDef(BaseModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMemberAccountsRequestListMemberAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtocolsListsRequestListProtocolsListsPaginateTypeDef(BaseModel):
    DefaultLists: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThirdPartyFirewallFirewallPoliciesRequestListThirdPartyFirewallFirewallPoliciesPaginateTypeDef(BaseModel):
    ThirdPartyFirewall: ThirdPartyFirewallType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesResponseTypeDef(BaseModel):
    PolicyList: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProtocolsListsResponseTypeDef(BaseModel):
    ProtocolsLists: List[ProtocolsListDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceSetResourcesResponseTypeDef(BaseModel):
    Items: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceSetsResponseTypeDef(BaseModel):
    ResourceSets: List[ResourceSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagList: Sequence[TagTypeDef]

class ListThirdPartyFirewallFirewallPoliciesResponseTypeDef(BaseModel):
    ThirdPartyFirewallFirewallPolicies: List[ThirdPartyFirewallFirewallPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetworkAclEntryTypeDef(BaseModel):
    Protocol: str
    RuleAction: NetworkAclRuleActionType
    Egress: bool
    IcmpTypeCode: Optional[NetworkAclIcmpTypeCodeTypeDef] = None
    PortRange: Optional[NetworkAclPortRangeTypeDef] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None

class NetworkFirewallBlackHoleRouteDetectedViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    RouteTableId: Optional[str] = None
    VpcId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None

class NetworkFirewallInternetTrafficNotInspectedViolationTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    RouteTableId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None
    IsRouteTableUsedInDifferentAZ: Optional[bool] = None
    CurrentFirewallSubnetRouteTable: Optional[str] = None
    ExpectedFirewallEndpoint: Optional[str] = None
    FirewallSubnetId: Optional[str] = None
    ExpectedFirewallSubnetRoutes: Optional[List[ExpectedRouteTypeDef]] = None
    ActualFirewallSubnetRoutes: Optional[List[RouteTypeDef]] = None
    InternetGatewayId: Optional[str] = None
    CurrentInternetGatewayRouteTable: Optional[str] = None
    ExpectedInternetGatewayRoutes: Optional[List[ExpectedRouteTypeDef]] = None
    ActualInternetGatewayRoutes: Optional[List[RouteTypeDef]] = None
    VpcId: Optional[str] = None

class NetworkFirewallInvalidRouteConfigurationViolationTypeDef(BaseModel):
    AffectedSubnets: Optional[List[str]] = None
    RouteTableId: Optional[str] = None
    IsRouteTableUsedInDifferentAZ: Optional[bool] = None
    ViolatingRoute: Optional[RouteTypeDef] = None
    CurrentFirewallSubnetRouteTable: Optional[str] = None
    ExpectedFirewallEndpoint: Optional[str] = None
    ActualFirewallEndpoint: Optional[str] = None
    ExpectedFirewallSubnetId: Optional[str] = None
    ActualFirewallSubnetId: Optional[str] = None
    ExpectedFirewallSubnetRoutes: Optional[List[ExpectedRouteTypeDef]] = None
    ActualFirewallSubnetRoutes: Optional[List[RouteTypeDef]] = None
    InternetGatewayId: Optional[str] = None
    CurrentInternetGatewayRouteTable: Optional[str] = None
    ExpectedInternetGatewayRoutes: Optional[List[ExpectedRouteTypeDef]] = None
    ActualInternetGatewayRoutes: Optional[List[RouteTypeDef]] = None
    VpcId: Optional[str] = None

class NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef(BaseModel):
    FirewallSubnetId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None
    RouteTableId: Optional[str] = None
    FirewallEndpoint: Optional[str] = None
    VpcId: Optional[str] = None

class NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef(BaseModel):
    GatewayId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None
    RouteTableId: Optional[str] = None
    VpcId: Optional[str] = None

class RouteHasOutOfScopeEndpointViolationTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    RouteTableId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None
    CurrentFirewallSubnetRouteTable: Optional[str] = None
    FirewallSubnetId: Optional[str] = None
    FirewallSubnetRoutes: Optional[List[RouteTypeDef]] = None
    InternetGatewayId: Optional[str] = None
    CurrentInternetGatewayRouteTable: Optional[str] = None
    InternetGatewayRoutes: Optional[List[RouteTypeDef]] = None

class StatefulRuleGroupTypeDef(BaseModel):
    RuleGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    Priority: Optional[int] = None
    Override: Optional[NetworkFirewallStatefulRuleGroupOverrideTypeDef] = None

class SecurityGroupRemediationActionTypeDef(BaseModel):
    RemediationActionType: Optional[RemediationActionTypeType] = None
    Description: Optional[str] = None
    RemediationResult: Optional[SecurityGroupRuleDescriptionTypeDef] = None
    IsDefaultAction: Optional[bool] = None

class GetAdminScopeResponseTypeDef(BaseModel):
    AdminScope: AdminScopeOutputTypeDef
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutAdminAccountRequestRequestTypeDef(BaseModel):
    AdminAccount: str
    AdminScope: Optional[AdminScopeTypeDef] = None

class GetAppsListResponseTypeDef(BaseModel):
    AppsList: AppsListDataOutputTypeDef
    AppsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppsListResponseTypeDef(BaseModel):
    AppsList: AppsListDataOutputTypeDef
    AppsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppsListsResponseTypeDef(BaseModel):
    AppsLists: List[AppsListDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAppsListRequestRequestTypeDef(BaseModel):
    AppsList: AppsListDataTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None

class PutProtocolsListRequestRequestTypeDef(BaseModel):
    ProtocolsList: ProtocolsListDataTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None

class PutResourceSetRequestRequestTypeDef(BaseModel):
    ResourceSet: ResourceSetTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None

class GetComplianceDetailResponseTypeDef(BaseModel):
    PolicyComplianceDetail: PolicyComplianceDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListComplianceStatusResponseTypeDef(BaseModel):
    PolicyComplianceStatusList: List[PolicyComplianceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EntryDescriptionTypeDef(BaseModel):
    EntryDetail: Optional[NetworkAclEntryTypeDef] = None
    EntryRuleNumber: Optional[int] = None
    EntryType: Optional[EntryTypeType] = None

class NetworkAclEntrySetOutputTypeDef(BaseModel):
    ForceRemediateForFirstEntries: bool
    ForceRemediateForLastEntries: bool
    FirstEntries: Optional[List[NetworkAclEntryTypeDef]] = None
    LastEntries: Optional[List[NetworkAclEntryTypeDef]] = None

class NetworkAclEntrySetTypeDef(BaseModel):
    ForceRemediateForFirstEntries: bool
    ForceRemediateForLastEntries: bool
    FirstEntries: Optional[Sequence[NetworkAclEntryTypeDef]] = None
    LastEntries: Optional[Sequence[NetworkAclEntryTypeDef]] = None

class NetworkFirewallPolicyDescriptionTypeDef(BaseModel):
    StatelessRuleGroups: Optional[List[StatelessRuleGroupTypeDef]] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessCustomActions: Optional[List[str]] = None
    StatefulRuleGroups: Optional[List[StatefulRuleGroupTypeDef]] = None
    StatefulDefaultActions: Optional[List[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptionsTypeDef] = None

class AwsVPCSecurityGroupViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    PartialMatches: Optional[List[PartialMatchTypeDef]] = None
    PossibleSecurityGroupRemediationActions: Optional[       List[SecurityGroupRemediationActionTypeDef]     ] = None

class CreateNetworkAclEntriesActionTypeDef(BaseModel):
    Description: Optional[str] = None
    NetworkAclId: Optional[ActionTargetTypeDef] = None
    NetworkAclEntriesToBeCreated: Optional[List[EntryDescriptionTypeDef]] = None
    FMSCanRemediate: Optional[bool] = None

class DeleteNetworkAclEntriesActionTypeDef(BaseModel):
    Description: Optional[str] = None
    NetworkAclId: Optional[ActionTargetTypeDef] = None
    NetworkAclEntriesToBeDeleted: Optional[List[EntryDescriptionTypeDef]] = None
    FMSCanRemediate: Optional[bool] = None

class EntryViolationTypeDef(BaseModel):
    ExpectedEntry: Optional[EntryDescriptionTypeDef] = None
    ExpectedEvaluationOrder: Optional[str] = None
    ActualEvaluationOrder: Optional[str] = None
    EntryAtExpectedEvaluationOrder: Optional[EntryDescriptionTypeDef] = None
    EntriesWithConflicts: Optional[List[EntryDescriptionTypeDef]] = None
    EntryViolationReasons: Optional[List[EntryViolationReasonType]] = None

class NetworkAclCommonPolicyOutputTypeDef(BaseModel):
    NetworkAclEntrySet: NetworkAclEntrySetOutputTypeDef

class NetworkAclCommonPolicyTypeDef(BaseModel):
    NetworkAclEntrySet: NetworkAclEntrySetTypeDef

class NetworkFirewallPolicyModifiedViolationTypeDef(BaseModel):
    ViolationTarget: Optional[str] = None
    CurrentPolicyDescription: Optional[NetworkFirewallPolicyDescriptionTypeDef] = None
    ExpectedPolicyDescription: Optional[NetworkFirewallPolicyDescriptionTypeDef] = None

class RemediationActionTypeDef(BaseModel):
    Description: Optional[str] = None
    EC2CreateRouteAction: Optional[EC2CreateRouteActionTypeDef] = None
    EC2ReplaceRouteAction: Optional[EC2ReplaceRouteActionTypeDef] = None
    EC2DeleteRouteAction: Optional[EC2DeleteRouteActionTypeDef] = None
    EC2CopyRouteTableAction: Optional[EC2CopyRouteTableActionTypeDef] = None
    EC2ReplaceRouteTableAssociationAction: Optional[       EC2ReplaceRouteTableAssociationActionTypeDef     ] = None
    EC2AssociateRouteTableAction: Optional[EC2AssociateRouteTableActionTypeDef] = None
    EC2CreateRouteTableAction: Optional[EC2CreateRouteTableActionTypeDef] = None
    FMSPolicyUpdateFirewallCreationConfigAction: Optional[       FMSPolicyUpdateFirewallCreationConfigActionTypeDef     ] = None
    CreateNetworkAclAction: Optional[CreateNetworkAclActionTypeDef] = None
    ReplaceNetworkAclAssociationAction: Optional[       ReplaceNetworkAclAssociationActionTypeDef     ] = None
    CreateNetworkAclEntriesAction: Optional[CreateNetworkAclEntriesActionTypeDef] = None
    DeleteNetworkAclEntriesAction: Optional[DeleteNetworkAclEntriesActionTypeDef] = None

class InvalidNetworkAclEntriesViolationTypeDef(BaseModel):
    Vpc: Optional[str] = None
    Subnet: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    CurrentAssociatedNetworkAcl: Optional[str] = None
    EntryViolations: Optional[List[EntryViolationTypeDef]] = None

class PolicyOptionOutputTypeDef(BaseModel):
    NetworkFirewallPolicy: Optional[NetworkFirewallPolicyTypeDef] = None
    ThirdPartyFirewallPolicy: Optional[ThirdPartyFirewallPolicyTypeDef] = None
    NetworkAclCommonPolicy: Optional[NetworkAclCommonPolicyOutputTypeDef] = None

class PolicyOptionTypeDef(BaseModel):
    NetworkFirewallPolicy: Optional[NetworkFirewallPolicyTypeDef] = None
    ThirdPartyFirewallPolicy: Optional[ThirdPartyFirewallPolicyTypeDef] = None
    NetworkAclCommonPolicy: Optional[NetworkAclCommonPolicyTypeDef] = None

class RemediationActionWithOrderTypeDef(BaseModel):
    RemediationAction: Optional[RemediationActionTypeDef] = None
    Order: Optional[int] = None

class SecurityServicePolicyDataOutputTypeDef(BaseModel):
    Type: SecurityServiceTypeType
    ManagedServiceData: Optional[str] = None
    PolicyOption: Optional[PolicyOptionOutputTypeDef] = None

class SecurityServicePolicyDataTypeDef(BaseModel):
    Type: SecurityServiceTypeType
    ManagedServiceData: Optional[str] = None
    PolicyOption: Optional[PolicyOptionTypeDef] = None

class PossibleRemediationActionTypeDef(BaseModel):
    OrderedRemediationActions: List[RemediationActionWithOrderTypeDef]
    Description: Optional[str] = None
    IsDefaultAction: Optional[bool] = None

class PolicyOutputTypeDef(BaseModel):
    PolicyName: str
    SecurityServicePolicyData: SecurityServicePolicyDataOutputTypeDef
    ResourceType: str
    ExcludeResourceTags: bool
    RemediationEnabled: bool
    PolicyId: Optional[str] = None
    PolicyUpdateToken: Optional[str] = None
    ResourceTypeList: Optional[List[str]] = None
    ResourceTags: Optional[List[ResourceTagTypeDef]] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    IncludeMap: Optional[Dict[CustomerPolicyScopeIdTypeType, List[str]]] = None
    ExcludeMap: Optional[Dict[CustomerPolicyScopeIdTypeType, List[str]]] = None
    ResourceSetIds: Optional[List[str]] = None
    PolicyDescription: Optional[str] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None

class PolicyTypeDef(BaseModel):
    PolicyName: str
    SecurityServicePolicyData: SecurityServicePolicyDataTypeDef
    ResourceType: str
    ExcludeResourceTags: bool
    RemediationEnabled: bool
    PolicyId: Optional[str] = None
    PolicyUpdateToken: Optional[str] = None
    ResourceTypeList: Optional[Sequence[str]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    IncludeMap: Optional[Mapping[CustomerPolicyScopeIdTypeType, Sequence[str]]] = None
    ExcludeMap: Optional[Mapping[CustomerPolicyScopeIdTypeType, Sequence[str]]] = None
    ResourceSetIds: Optional[Sequence[str]] = None
    PolicyDescription: Optional[str] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None

class PossibleRemediationActionsTypeDef(BaseModel):
    Description: Optional[str] = None
    Actions: Optional[List[PossibleRemediationActionTypeDef]] = None

class GetPolicyResponseTypeDef(BaseModel):
    Policy: PolicyOutputTypeDef
    PolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutPolicyResponseTypeDef(BaseModel):
    Policy: PolicyOutputTypeDef
    PolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutPolicyRequestRequestTypeDef(BaseModel):
    Policy: PolicyTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None

class ResourceViolationTypeDef(BaseModel):
    AwsVPCSecurityGroupViolation: Optional[AwsVPCSecurityGroupViolationTypeDef] = None
    AwsEc2NetworkInterfaceViolation: Optional[AwsEc2NetworkInterfaceViolationTypeDef] = None
    AwsEc2InstanceViolation: Optional[AwsEc2InstanceViolationTypeDef] = None
    NetworkFirewallMissingFirewallViolation: Optional[       NetworkFirewallMissingFirewallViolationTypeDef     ] = None
    NetworkFirewallMissingSubnetViolation: Optional[       NetworkFirewallMissingSubnetViolationTypeDef     ] = None
    NetworkFirewallMissingExpectedRTViolation: Optional[       NetworkFirewallMissingExpectedRTViolationTypeDef     ] = None
    NetworkFirewallPolicyModifiedViolation: Optional[       NetworkFirewallPolicyModifiedViolationTypeDef     ] = None
    NetworkFirewallInternetTrafficNotInspectedViolation: Optional[       NetworkFirewallInternetTrafficNotInspectedViolationTypeDef     ] = None
    NetworkFirewallInvalidRouteConfigurationViolation: Optional[       NetworkFirewallInvalidRouteConfigurationViolationTypeDef     ] = None
    NetworkFirewallBlackHoleRouteDetectedViolation: Optional[       NetworkFirewallBlackHoleRouteDetectedViolationTypeDef     ] = None
    NetworkFirewallUnexpectedFirewallRoutesViolation: Optional[       NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef     ] = None
    NetworkFirewallUnexpectedGatewayRoutesViolation: Optional[       NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef     ] = None
    NetworkFirewallMissingExpectedRoutesViolation: Optional[       NetworkFirewallMissingExpectedRoutesViolationTypeDef     ] = None
    DnsRuleGroupPriorityConflictViolation: Optional[       DnsRuleGroupPriorityConflictViolationTypeDef     ] = None
    DnsDuplicateRuleGroupViolation: Optional[DnsDuplicateRuleGroupViolationTypeDef] = None
    DnsRuleGroupLimitExceededViolation: Optional[       DnsRuleGroupLimitExceededViolationTypeDef     ] = None
    FirewallSubnetIsOutOfScopeViolation: Optional[       FirewallSubnetIsOutOfScopeViolationTypeDef     ] = None
    RouteHasOutOfScopeEndpointViolation: Optional[       RouteHasOutOfScopeEndpointViolationTypeDef     ] = None
    ThirdPartyFirewallMissingFirewallViolation: Optional[       ThirdPartyFirewallMissingFirewallViolationTypeDef     ] = None
    ThirdPartyFirewallMissingSubnetViolation: Optional[       ThirdPartyFirewallMissingSubnetViolationTypeDef     ] = None
    ThirdPartyFirewallMissingExpectedRouteTableViolation: Optional[       ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef     ] = None
    FirewallSubnetMissingVPCEndpointViolation: Optional[       FirewallSubnetMissingVPCEndpointViolationTypeDef     ] = None
    InvalidNetworkAclEntriesViolation: Optional[InvalidNetworkAclEntriesViolationTypeDef] = None
    PossibleRemediationActions: Optional[PossibleRemediationActionsTypeDef] = None

class ViolationDetailTypeDef(BaseModel):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str
    ResourceViolations: List[ResourceViolationTypeDef]
    ResourceTags: Optional[List[TagTypeDef]] = None
    ResourceDescription: Optional[str] = None

class GetViolationDetailsResponseTypeDef(BaseModel):
    ViolationDetail: ViolationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

