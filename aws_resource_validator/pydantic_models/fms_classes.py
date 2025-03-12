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
from aws_resource_validator.pydantic_models.fms_constants import *

class AccountScopeOutputTypeDef(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    AllAccountsEnabled: Optional[bool] = None
    ExcludeSpecifiedAccounts: Optional[bool] = None


class AccountScopeTypeDef(BaseValidatorModel):
    Accounts: Optional[Sequence[str]] = None
    AllAccountsEnabled: Optional[bool] = None
    ExcludeSpecifiedAccounts: Optional[bool] = None


class ActionTargetTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    Description: Optional[str] = None


class AdminAccountSummaryTypeDef(BaseValidatorModel):
    AdminAccount: Optional[str] = None
    DefaultAdmin: Optional[bool] = None
    Status: Optional[OrganizationStatusType] = None


class OrganizationalUnitScopeOutputTypeDef(BaseValidatorModel):
    OrganizationalUnits: Optional[List[str]] = None
    AllOrganizationalUnitsEnabled: Optional[bool] = None
    ExcludeSpecifiedOrganizationalUnits: Optional[bool] = None


class PolicyTypeScopeOutputTypeDef(BaseValidatorModel):
    PolicyTypes: Optional[List[SecurityServiceTypeType]] = None
    AllPolicyTypesEnabled: Optional[bool] = None


class RegionScopeOutputTypeDef(BaseValidatorModel):
    Regions: Optional[List[str]] = None
    AllRegionsEnabled: Optional[bool] = None


class OrganizationalUnitScopeTypeDef(BaseValidatorModel):
    OrganizationalUnits: Optional[Sequence[str]] = None
    AllOrganizationalUnitsEnabled: Optional[bool] = None
    ExcludeSpecifiedOrganizationalUnits: Optional[bool] = None


class PolicyTypeScopeTypeDef(BaseValidatorModel):
    PolicyTypes: Optional[Sequence[SecurityServiceTypeType]] = None
    AllPolicyTypesEnabled: Optional[bool] = None


class RegionScopeTypeDef(BaseValidatorModel):
    Regions: Optional[Sequence[str]] = None
    AllRegionsEnabled: Optional[bool] = None


class AssociateAdminAccountRequestTypeDef(BaseValidatorModel):
    AdminAccount: str


class AssociateThirdPartyFirewallRequestTypeDef(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AwsEc2NetworkInterfaceViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolatingSecurityGroups: Optional[List[str]] = None


class PartialMatchTypeDef(BaseValidatorModel):
    Reference: Optional[str] = None
    TargetViolationReasons: Optional[List[str]] = None


class BatchAssociateResourceRequestTypeDef(BaseValidatorModel):
    ResourceSetIdentifier: str
    Items: Sequence[str]


class FailedItemTypeDef(BaseValidatorModel):
    URI: Optional[str] = None
    Reason: Optional[FailedItemReasonType] = None


class BatchDisassociateResourceRequestTypeDef(BaseValidatorModel):
    ResourceSetIdentifier: str
    Items: Sequence[str]


class ComplianceViolatorTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ViolationReason: Optional[ViolationReasonType] = None
    ResourceType: Optional[str] = None
    Metadata: Optional[Dict[str, str]] = None


class DeleteAppsListRequestTypeDef(BaseValidatorModel):
    ListId: str


class DeletePolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    DeleteAllPolicyResources: Optional[bool] = None


class DeleteProtocolsListRequestTypeDef(BaseValidatorModel):
    ListId: str


class DeleteResourceSetRequestTypeDef(BaseValidatorModel):
    Identifier: str


class DisassociateThirdPartyFirewallRequestTypeDef(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType


class DnsDuplicateRuleGroupViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None


class DnsRuleGroupLimitExceededViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    NumberOfRuleGroupsAlreadyAssociated: Optional[int] = None


class DnsRuleGroupPriorityConflictViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    ConflictingPriority: Optional[int] = None
    ConflictingPolicyId: Optional[str] = None
    UnavailablePriorities: Optional[List[int]] = None


class EvaluationResultTypeDef(BaseValidatorModel):
    ComplianceStatus: Optional[PolicyComplianceStatusTypeType] = None
    ViolatorCount: Optional[int] = None
    EvaluationLimitExceeded: Optional[bool] = None


class ExpectedRouteTypeDef(BaseValidatorModel):
    IpV4Cidr: Optional[str] = None
    PrefixListId: Optional[str] = None
    IpV6Cidr: Optional[str] = None
    ContributingSubnets: Optional[List[str]] = None
    AllowedTargets: Optional[List[str]] = None
    RouteTableId: Optional[str] = None


class FMSPolicyUpdateFirewallCreationConfigActionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    FirewallCreationConfig: Optional[str] = None


class FirewallSubnetIsOutOfScopeViolationTypeDef(BaseValidatorModel):
    FirewallSubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None
    VpcEndpointId: Optional[str] = None


class FirewallSubnetMissingVPCEndpointViolationTypeDef(BaseValidatorModel):
    FirewallSubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    SubnetAvailabilityZoneId: Optional[str] = None


class GetAdminScopeRequestTypeDef(BaseValidatorModel):
    AdminAccount: str


class GetAppsListRequestTypeDef(BaseValidatorModel):
    ListId: str
    DefaultList: Optional[bool] = None


class GetComplianceDetailRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    MemberAccount: str


class GetPolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str


class GetProtocolsListRequestTypeDef(BaseValidatorModel):
    ListId: str
    DefaultList: Optional[bool] = None


class ProtocolsListDataOutputTypeDef(BaseValidatorModel):
    ListName: str
    ProtocolsList: List[str]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    PreviousProtocolsList: Optional[Dict[str, List[str]]] = None


class GetResourceSetRequestTypeDef(BaseValidatorModel):
    Identifier: str


class ResourceSetOutputTypeDef(BaseValidatorModel):
    Name: str
    ResourceTypeList: List[str]
    Id: Optional[str] = None
    Description: Optional[str] = None
    UpdateToken: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None


class GetThirdPartyFirewallAssociationStatusRequestTypeDef(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType


class GetViolationDetailsRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAdminAccountsForOrganizationRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAdminsManagingAccountRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAppsListsRequestTypeDef(BaseValidatorModel):
    MaxResults: int
    DefaultLists: Optional[bool] = None
    NextToken: Optional[str] = None


class ListComplianceStatusRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDiscoveredResourcesRequestTypeDef(BaseValidatorModel):
    MemberAccountIds: Sequence[str]
    ResourceType: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMemberAccountsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoliciesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicySummaryTypeDef(BaseValidatorModel):
    PolicyArn: Optional[str] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    ResourceType: Optional[str] = None
    SecurityServiceType: Optional[SecurityServiceTypeType] = None
    RemediationEnabled: Optional[bool] = None
    DeleteUnusedFMManagedResources: Optional[bool] = None
    PolicyStatus: Optional[CustomerPolicyStatusType] = None


class ListProtocolsListsRequestTypeDef(BaseValidatorModel):
    MaxResults: int
    DefaultLists: Optional[bool] = None
    NextToken: Optional[str] = None


class ProtocolsListDataSummaryTypeDef(BaseValidatorModel):
    ListArn: Optional[str] = None
    ListId: Optional[str] = None
    ListName: Optional[str] = None
    ProtocolsList: Optional[List[str]] = None


class ListResourceSetResourcesRequestTypeDef(BaseValidatorModel):
    Identifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ResourceTypeDef(BaseValidatorModel):
    URI: str
    AccountId: Optional[str] = None


class ListResourceSetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceSetSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ListThirdPartyFirewallFirewallPoliciesRequestTypeDef(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType
    MaxResults: int
    NextToken: Optional[str] = None


class ThirdPartyFirewallFirewallPolicyTypeDef(BaseValidatorModel):
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None


class NetworkAclPortRangeTypeDef(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None


class RouteTypeDef(BaseValidatorModel):
    DestinationType: Optional[DestinationTypeType] = None
    TargetType: Optional[TargetTypeType] = None
    Destination: Optional[str] = None
    Target: Optional[str] = None


class NetworkFirewallMissingExpectedRTViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CurrentRouteTable: Optional[str] = None
    ExpectedRouteTable: Optional[str] = None


class NetworkFirewallMissingFirewallViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class NetworkFirewallMissingSubnetViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class StatefulEngineOptionsTypeDef(BaseValidatorModel):
    RuleOrder: Optional[RuleOrderType] = None
    StreamExceptionPolicy: Optional[StreamExceptionPolicyType] = None


class StatelessRuleGroupTypeDef(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    Priority: Optional[int] = None


class NetworkFirewallPolicyTypeDef(BaseValidatorModel):
    FirewallDeploymentModel: Optional[FirewallDeploymentModelType] = None


class NetworkFirewallStatefulRuleGroupOverrideTypeDef(BaseValidatorModel):
    Action: Optional[Literal["DROP_TO_ALERT"]] = None


class ThirdPartyFirewallPolicyTypeDef(BaseValidatorModel):
    FirewallDeploymentModel: Optional[FirewallDeploymentModelType] = None


class ResourceTagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class PutNotificationChannelRequestTypeDef(BaseValidatorModel):
    SnsTopicArn: str
    SnsRoleName: str


class ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CurrentRouteTable: Optional[str] = None
    ExpectedRouteTable: Optional[str] = None


class ThirdPartyFirewallMissingFirewallViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class ThirdPartyFirewallMissingSubnetViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    VPC: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    TargetViolationReason: Optional[str] = None


class WebACLHasIncompatibleConfigurationViolationTypeDef(BaseValidatorModel):
    WebACLArn: Optional[str] = None
    Description: Optional[str] = None


class WebACLHasOutOfScopeResourcesViolationTypeDef(BaseValidatorModel):
    WebACLArn: Optional[str] = None
    OutOfScopeResourceList: Optional[List[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class CreateNetworkAclActionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Vpc: Optional[ActionTargetTypeDef] = None
    FMSCanRemediate: Optional[bool] = None


class EC2AssociateRouteTableActionTypeDef(BaseValidatorModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    SubnetId: Optional[ActionTargetTypeDef] = None
    GatewayId: Optional[ActionTargetTypeDef] = None


class EC2CopyRouteTableActionTypeDef(BaseValidatorModel):
    VpcId: ActionTargetTypeDef
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None


class EC2CreateRouteActionTypeDef(BaseValidatorModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    VpcEndpointId: Optional[ActionTargetTypeDef] = None
    GatewayId: Optional[ActionTargetTypeDef] = None


class EC2CreateRouteTableActionTypeDef(BaseValidatorModel):
    VpcId: ActionTargetTypeDef
    Description: Optional[str] = None


class EC2DeleteRouteActionTypeDef(BaseValidatorModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None


class EC2ReplaceRouteActionTypeDef(BaseValidatorModel):
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    GatewayId: Optional[ActionTargetTypeDef] = None


class EC2ReplaceRouteTableAssociationActionTypeDef(BaseValidatorModel):
    AssociationId: ActionTargetTypeDef
    RouteTableId: ActionTargetTypeDef
    Description: Optional[str] = None


class ReplaceNetworkAclAssociationActionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    AssociationId: Optional[ActionTargetTypeDef] = None
    NetworkAclId: Optional[ActionTargetTypeDef] = None
    FMSCanRemediate: Optional[bool] = None


class AdminScopeOutputTypeDef(BaseValidatorModel):
    AccountScope: Optional[AccountScopeOutputTypeDef] = None
    OrganizationalUnitScope: Optional[OrganizationalUnitScopeOutputTypeDef] = None
    RegionScope: Optional[RegionScopeOutputTypeDef] = None
    PolicyTypeScope: Optional[PolicyTypeScopeOutputTypeDef] = None


class AdminScopeTypeDef(BaseValidatorModel):
    AccountScope: Optional[AccountScopeTypeDef] = None
    OrganizationalUnitScope: Optional[OrganizationalUnitScopeTypeDef] = None
    RegionScope: Optional[RegionScopeTypeDef] = None
    PolicyTypeScope: Optional[PolicyTypeScopeTypeDef] = None


class AppTypeDef(BaseValidatorModel):
    pass


class AppsListDataOutputTypeDef(BaseValidatorModel):
    ListName: str
    AppsList: List[AppTypeDef]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    PreviousAppsList: Optional[Dict[str, List[AppTypeDef]]] = None


class AppsListDataSummaryTypeDef(BaseValidatorModel):
    ListArn: Optional[str] = None
    ListId: Optional[str] = None
    ListName: Optional[str] = None
    AppsList: Optional[List[AppTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class AppsListDataTypeDef(BaseValidatorModel):
    ListName: str
    AppsList: Sequence[AppTypeDef]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[TimestampTypeDef] = None
    LastUpdateTime: Optional[TimestampTypeDef] = None
    PreviousAppsList: Optional[Mapping[str, Sequence[AppTypeDef]]] = None


class GetProtectionStatusRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    MemberAccountId: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProtocolsListDataTypeDef(BaseValidatorModel):
    ListName: str
    ProtocolsList: Sequence[str]
    ListId: Optional[str] = None
    ListUpdateToken: Optional[str] = None
    CreateTime: Optional[TimestampTypeDef] = None
    LastUpdateTime: Optional[TimestampTypeDef] = None
    PreviousProtocolsList: Optional[Mapping[str, Sequence[str]]] = None


class ResourceSetTypeDef(BaseValidatorModel):
    Name: str
    ResourceTypeList: Sequence[str]
    Id: Optional[str] = None
    Description: Optional[str] = None
    UpdateToken: Optional[str] = None
    LastUpdateTime: Optional[TimestampTypeDef] = None
    ResourceSetStatus: Optional[ResourceSetStatusType] = None


class AssociateThirdPartyFirewallResponseTypeDef(BaseValidatorModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateThirdPartyFirewallResponseTypeDef(BaseValidatorModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAdminAccountResponseTypeDef(BaseValidatorModel):
    AdminAccount: str
    RoleStatus: AccountRoleStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetNotificationChannelResponseTypeDef(BaseValidatorModel):
    SnsTopicArn: str
    SnsRoleName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetProtectionStatusResponseTypeDef(BaseValidatorModel):
    AdminAccountId: str
    ServiceType: SecurityServiceTypeType
    Data: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetThirdPartyFirewallAssociationStatusResponseTypeDef(BaseValidatorModel):
    ThirdPartyFirewallStatus: ThirdPartyFirewallAssociationStatusType
    MarketplaceOnboardingStatus: MarketplaceSubscriptionOnboardingStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListAdminAccountsForOrganizationResponseTypeDef(BaseValidatorModel):
    AdminAccounts: List[AdminAccountSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAdminsManagingAccountResponseTypeDef(BaseValidatorModel):
    AdminAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMemberAccountsResponseTypeDef(BaseValidatorModel):
    MemberAccounts: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AwsEc2InstanceViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    AwsEc2NetworkInterfaceViolations: Optional[List[AwsEc2NetworkInterfaceViolationTypeDef]] = None


class BatchAssociateResourceResponseTypeDef(BaseValidatorModel):
    ResourceSetIdentifier: str
    FailedItems: List[FailedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDisassociateResourceResponseTypeDef(BaseValidatorModel):
    ResourceSetIdentifier: str
    FailedItems: List[FailedItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PolicyComplianceDetailTypeDef(BaseValidatorModel):
    PolicyOwner: Optional[str] = None
    PolicyId: Optional[str] = None
    MemberAccount: Optional[str] = None
    Violators: Optional[List[ComplianceViolatorTypeDef]] = None
    EvaluationLimitExceeded: Optional[bool] = None
    ExpiredAt: Optional[datetime] = None
    IssueInfoMap: Optional[Dict[DependentServiceNameType, str]] = None


class DiscoveredResourceTypeDef(BaseValidatorModel):
    pass


class ListDiscoveredResourcesResponseTypeDef(BaseValidatorModel):
    Items: List[DiscoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PolicyComplianceStatusTypeDef(BaseValidatorModel):
    PolicyOwner: Optional[str] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    MemberAccount: Optional[str] = None
    EvaluationResults: Optional[List[EvaluationResultTypeDef]] = None
    LastUpdated: Optional[datetime] = None
    IssueInfoMap: Optional[Dict[DependentServiceNameType, str]] = None


class NetworkFirewallMissingExpectedRoutesViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ExpectedRoutes: Optional[List[ExpectedRouteTypeDef]] = None
    VpcId: Optional[str] = None


class GetProtocolsListResponseTypeDef(BaseValidatorModel):
    ProtocolsList: ProtocolsListDataOutputTypeDef
    ProtocolsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutProtocolsListResponseTypeDef(BaseValidatorModel):
    ProtocolsList: ProtocolsListDataOutputTypeDef
    ProtocolsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSet: ResourceSetOutputTypeDef
    ResourceSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSet: ResourceSetOutputTypeDef
    ResourceSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAdminAccountsForOrganizationRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAdminsManagingAccountRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAppsListsRequestPaginateTypeDef(BaseValidatorModel):
    DefaultLists: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComplianceStatusRequestPaginateTypeDef(BaseValidatorModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMemberAccountsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProtocolsListsRequestPaginateTypeDef(BaseValidatorModel):
    DefaultLists: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThirdPartyFirewallFirewallPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    ThirdPartyFirewall: ThirdPartyFirewallType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoliciesResponseTypeDef(BaseValidatorModel):
    PolicyList: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProtocolsListsResponseTypeDef(BaseValidatorModel):
    ProtocolsLists: List[ProtocolsListDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceSetResourcesResponseTypeDef(BaseValidatorModel):
    Items: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceSetsResponseTypeDef(BaseValidatorModel):
    ResourceSets: List[ResourceSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagList: Sequence[TagTypeDef]


class ListThirdPartyFirewallFirewallPoliciesResponseTypeDef(BaseValidatorModel):
    ThirdPartyFirewallFirewallPolicies: List[ThirdPartyFirewallFirewallPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class NetworkFirewallBlackHoleRouteDetectedViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    RouteTableId: Optional[str] = None
    VpcId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None


class NetworkFirewallInternetTrafficNotInspectedViolationTypeDef(BaseValidatorModel):
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


class NetworkFirewallInvalidRouteConfigurationViolationTypeDef(BaseValidatorModel):
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


class NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef(BaseValidatorModel):
    FirewallSubnetId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None
    RouteTableId: Optional[str] = None
    FirewallEndpoint: Optional[str] = None
    VpcId: Optional[str] = None


class NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef(BaseValidatorModel):
    GatewayId: Optional[str] = None
    ViolatingRoutes: Optional[List[RouteTypeDef]] = None
    RouteTableId: Optional[str] = None
    VpcId: Optional[str] = None


class RouteHasOutOfScopeEndpointViolationTypeDef(BaseValidatorModel):
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


class StatefulRuleGroupTypeDef(BaseValidatorModel):
    RuleGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    Priority: Optional[int] = None
    Override: Optional[NetworkFirewallStatefulRuleGroupOverrideTypeDef] = None


class SecurityGroupRuleDescriptionTypeDef(BaseValidatorModel):
    pass


class SecurityGroupRemediationActionTypeDef(BaseValidatorModel):
    RemediationActionType: Optional[RemediationActionTypeType] = None
    Description: Optional[str] = None
    RemediationResult: Optional[SecurityGroupRuleDescriptionTypeDef] = None
    IsDefaultAction: Optional[bool] = None


class GetAdminScopeResponseTypeDef(BaseValidatorModel):
    AdminScope: AdminScopeOutputTypeDef
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppsListResponseTypeDef(BaseValidatorModel):
    AppsList: AppsListDataOutputTypeDef
    AppsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutAppsListResponseTypeDef(BaseValidatorModel):
    AppsList: AppsListDataOutputTypeDef
    AppsListArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAppsListsResponseTypeDef(BaseValidatorModel):
    AppsLists: List[AppsListDataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetComplianceDetailResponseTypeDef(BaseValidatorModel):
    PolicyComplianceDetail: PolicyComplianceDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListComplianceStatusResponseTypeDef(BaseValidatorModel):
    PolicyComplianceStatusList: List[PolicyComplianceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class NetworkAclEntryTypeDef(BaseValidatorModel):
    pass


class EntryDescriptionTypeDef(BaseValidatorModel):
    EntryDetail: Optional[NetworkAclEntryTypeDef] = None
    EntryRuleNumber: Optional[int] = None
    EntryType: Optional[EntryTypeType] = None


class NetworkAclEntrySetOutputTypeDef(BaseValidatorModel):
    ForceRemediateForFirstEntries: bool
    ForceRemediateForLastEntries: bool
    FirstEntries: Optional[List[NetworkAclEntryTypeDef]] = None
    LastEntries: Optional[List[NetworkAclEntryTypeDef]] = None


class NetworkAclEntrySetTypeDef(BaseValidatorModel):
    ForceRemediateForFirstEntries: bool
    ForceRemediateForLastEntries: bool
    FirstEntries: Optional[Sequence[NetworkAclEntryTypeDef]] = None
    LastEntries: Optional[Sequence[NetworkAclEntryTypeDef]] = None


class NetworkFirewallPolicyDescriptionTypeDef(BaseValidatorModel):
    StatelessRuleGroups: Optional[List[StatelessRuleGroupTypeDef]] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessCustomActions: Optional[List[str]] = None
    StatefulRuleGroups: Optional[List[StatefulRuleGroupTypeDef]] = None
    StatefulDefaultActions: Optional[List[str]] = None
    StatefulEngineOptions: Optional[StatefulEngineOptionsTypeDef] = None


class AwsVPCSecurityGroupViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    ViolationTargetDescription: Optional[str] = None
    PartialMatches: Optional[List[PartialMatchTypeDef]] = None
    PossibleSecurityGroupRemediationActions: Optional[ List[SecurityGroupRemediationActionTypeDef] ] = None


class AdminScopeUnionTypeDef(BaseValidatorModel):
    pass


class PutAdminAccountRequestTypeDef(BaseValidatorModel):
    AdminAccount: str
    AdminScope: Optional[AdminScopeUnionTypeDef] = None


class AppsListDataUnionTypeDef(BaseValidatorModel):
    pass


class PutAppsListRequestTypeDef(BaseValidatorModel):
    AppsList: AppsListDataUnionTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None


class ProtocolsListDataUnionTypeDef(BaseValidatorModel):
    pass


class PutProtocolsListRequestTypeDef(BaseValidatorModel):
    ProtocolsList: ProtocolsListDataUnionTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None


class ResourceSetUnionTypeDef(BaseValidatorModel):
    pass


class PutResourceSetRequestTypeDef(BaseValidatorModel):
    ResourceSet: ResourceSetUnionTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None


class CreateNetworkAclEntriesActionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    NetworkAclId: Optional[ActionTargetTypeDef] = None
    NetworkAclEntriesToBeCreated: Optional[List[EntryDescriptionTypeDef]] = None
    FMSCanRemediate: Optional[bool] = None


class DeleteNetworkAclEntriesActionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    NetworkAclId: Optional[ActionTargetTypeDef] = None
    NetworkAclEntriesToBeDeleted: Optional[List[EntryDescriptionTypeDef]] = None
    FMSCanRemediate: Optional[bool] = None


class EntryViolationTypeDef(BaseValidatorModel):
    ExpectedEntry: Optional[EntryDescriptionTypeDef] = None
    ExpectedEvaluationOrder: Optional[str] = None
    ActualEvaluationOrder: Optional[str] = None
    EntryAtExpectedEvaluationOrder: Optional[EntryDescriptionTypeDef] = None
    EntriesWithConflicts: Optional[List[EntryDescriptionTypeDef]] = None
    EntryViolationReasons: Optional[List[EntryViolationReasonType]] = None


class NetworkAclCommonPolicyOutputTypeDef(BaseValidatorModel):
    NetworkAclEntrySet: NetworkAclEntrySetOutputTypeDef


class NetworkAclCommonPolicyTypeDef(BaseValidatorModel):
    NetworkAclEntrySet: NetworkAclEntrySetTypeDef


class NetworkFirewallPolicyModifiedViolationTypeDef(BaseValidatorModel):
    ViolationTarget: Optional[str] = None
    CurrentPolicyDescription: Optional[NetworkFirewallPolicyDescriptionTypeDef] = None
    ExpectedPolicyDescription: Optional[NetworkFirewallPolicyDescriptionTypeDef] = None


class RemediationActionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    EC2CreateRouteAction: Optional[EC2CreateRouteActionTypeDef] = None
    EC2ReplaceRouteAction: Optional[EC2ReplaceRouteActionTypeDef] = None
    EC2DeleteRouteAction: Optional[EC2DeleteRouteActionTypeDef] = None
    EC2CopyRouteTableAction: Optional[EC2CopyRouteTableActionTypeDef] = None
    EC2ReplaceRouteTableAssociationAction: Optional[EC2ReplaceRouteTableAssociationActionTypeDef] = None
    EC2AssociateRouteTableAction: Optional[EC2AssociateRouteTableActionTypeDef] = None
    EC2CreateRouteTableAction: Optional[EC2CreateRouteTableActionTypeDef] = None
    FMSPolicyUpdateFirewallCreationConfigAction: Optional[ FMSPolicyUpdateFirewallCreationConfigActionTypeDef ] = None
    CreateNetworkAclAction: Optional[CreateNetworkAclActionTypeDef] = None
    ReplaceNetworkAclAssociationAction: Optional[ReplaceNetworkAclAssociationActionTypeDef] = None
    CreateNetworkAclEntriesAction: Optional[CreateNetworkAclEntriesActionTypeDef] = None
    DeleteNetworkAclEntriesAction: Optional[DeleteNetworkAclEntriesActionTypeDef] = None


class InvalidNetworkAclEntriesViolationTypeDef(BaseValidatorModel):
    Vpc: Optional[str] = None
    Subnet: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None
    CurrentAssociatedNetworkAcl: Optional[str] = None
    EntryViolations: Optional[List[EntryViolationTypeDef]] = None


class PolicyOptionOutputTypeDef(BaseValidatorModel):
    NetworkFirewallPolicy: Optional[NetworkFirewallPolicyTypeDef] = None
    ThirdPartyFirewallPolicy: Optional[ThirdPartyFirewallPolicyTypeDef] = None
    NetworkAclCommonPolicy: Optional[NetworkAclCommonPolicyOutputTypeDef] = None


class PolicyOptionTypeDef(BaseValidatorModel):
    NetworkFirewallPolicy: Optional[NetworkFirewallPolicyTypeDef] = None
    ThirdPartyFirewallPolicy: Optional[ThirdPartyFirewallPolicyTypeDef] = None
    NetworkAclCommonPolicy: Optional[NetworkAclCommonPolicyTypeDef] = None


class RemediationActionWithOrderTypeDef(BaseValidatorModel):
    RemediationAction: Optional[RemediationActionTypeDef] = None
    Order: Optional[int] = None


class PossibleRemediationActionTypeDef(BaseValidatorModel):
    OrderedRemediationActions: List[RemediationActionWithOrderTypeDef]
    Description: Optional[str] = None
    IsDefaultAction: Optional[bool] = None


class SecurityServicePolicyDataOutputTypeDef(BaseValidatorModel):
    pass


class PolicyOutputTypeDef(BaseValidatorModel):
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
    ResourceTagLogicalOperator: Optional[ResourceTagLogicalOperatorType] = None


class SecurityServicePolicyDataTypeDef(BaseValidatorModel):
    pass


class PolicyTypeDef(BaseValidatorModel):
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
    ResourceTagLogicalOperator: Optional[ResourceTagLogicalOperatorType] = None


class PossibleRemediationActionsTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Actions: Optional[List[PossibleRemediationActionTypeDef]] = None


class GetPolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyOutputTypeDef
    PolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutPolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyOutputTypeDef
    PolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceViolationTypeDef(BaseValidatorModel):
    AwsVPCSecurityGroupViolation: Optional[AwsVPCSecurityGroupViolationTypeDef] = None
    AwsEc2NetworkInterfaceViolation: Optional[AwsEc2NetworkInterfaceViolationTypeDef] = None
    AwsEc2InstanceViolation: Optional[AwsEc2InstanceViolationTypeDef] = None
    NetworkFirewallMissingFirewallViolation: Optional[ NetworkFirewallMissingFirewallViolationTypeDef ] = None
    NetworkFirewallMissingSubnetViolation: Optional[NetworkFirewallMissingSubnetViolationTypeDef] = None
    NetworkFirewallMissingExpectedRTViolation: Optional[ NetworkFirewallMissingExpectedRTViolationTypeDef ] = None
    NetworkFirewallPolicyModifiedViolation: Optional[ NetworkFirewallPolicyModifiedViolationTypeDef ] = None
    NetworkFirewallInternetTrafficNotInspectedViolation: Optional[ NetworkFirewallInternetTrafficNotInspectedViolationTypeDef ] = None
    NetworkFirewallInvalidRouteConfigurationViolation: Optional[ NetworkFirewallInvalidRouteConfigurationViolationTypeDef ] = None
    NetworkFirewallBlackHoleRouteDetectedViolation: Optional[ NetworkFirewallBlackHoleRouteDetectedViolationTypeDef ] = None
    NetworkFirewallUnexpectedFirewallRoutesViolation: Optional[ NetworkFirewallUnexpectedFirewallRoutesViolationTypeDef ] = None
    NetworkFirewallUnexpectedGatewayRoutesViolation: Optional[ NetworkFirewallUnexpectedGatewayRoutesViolationTypeDef ] = None
    NetworkFirewallMissingExpectedRoutesViolation: Optional[ NetworkFirewallMissingExpectedRoutesViolationTypeDef ] = None
    DnsRuleGroupPriorityConflictViolation: Optional[DnsRuleGroupPriorityConflictViolationTypeDef] = None
    DnsDuplicateRuleGroupViolation: Optional[DnsDuplicateRuleGroupViolationTypeDef] = None
    DnsRuleGroupLimitExceededViolation: Optional[DnsRuleGroupLimitExceededViolationTypeDef] = None
    FirewallSubnetIsOutOfScopeViolation: Optional[FirewallSubnetIsOutOfScopeViolationTypeDef] = None
    RouteHasOutOfScopeEndpointViolation: Optional[RouteHasOutOfScopeEndpointViolationTypeDef] = None
    ThirdPartyFirewallMissingFirewallViolation: Optional[ ThirdPartyFirewallMissingFirewallViolationTypeDef ] = None
    ThirdPartyFirewallMissingSubnetViolation: Optional[ ThirdPartyFirewallMissingSubnetViolationTypeDef ] = None
    ThirdPartyFirewallMissingExpectedRouteTableViolation: Optional[ ThirdPartyFirewallMissingExpectedRouteTableViolationTypeDef ] = None
    FirewallSubnetMissingVPCEndpointViolation: Optional[ FirewallSubnetMissingVPCEndpointViolationTypeDef ] = None
    InvalidNetworkAclEntriesViolation: Optional[InvalidNetworkAclEntriesViolationTypeDef] = None
    PossibleRemediationActions: Optional[PossibleRemediationActionsTypeDef] = None
    WebACLHasIncompatibleConfigurationViolation: Optional[ WebACLHasIncompatibleConfigurationViolationTypeDef ] = None
    WebACLHasOutOfScopeResourcesViolation: Optional[WebACLHasOutOfScopeResourcesViolationTypeDef] = None


class PolicyUnionTypeDef(BaseValidatorModel):
    pass


class PutPolicyRequestTypeDef(BaseValidatorModel):
    Policy: PolicyUnionTypeDef
    TagList: Optional[Sequence[TagTypeDef]] = None


class ViolationDetailTypeDef(BaseValidatorModel):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str
    ResourceViolations: List[ResourceViolationTypeDef]
    ResourceTags: Optional[List[TagTypeDef]] = None
    ResourceDescription: Optional[str] = None


class GetViolationDetailsResponseTypeDef(BaseValidatorModel):
    ViolationDetail: ViolationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


