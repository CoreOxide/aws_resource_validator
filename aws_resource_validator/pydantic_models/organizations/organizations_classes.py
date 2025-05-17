from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.organizations.organizations_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_handshake' function.
class AcceptHandshakeRequest(BaseValidatorModel):
    HandshakeId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Account(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AccountStatusType] = None
    JoinedMethod: Optional[AccountJoinedMethodType] = None
    JoinedTimestamp: Optional[datetime] = None


# This class is the input for the 'attach_policy' function.
class AttachPolicyRequest(BaseValidatorModel):
    PolicyId: str
    TargetId: str


# This class is the input for the 'cancel_handshake' function.
class CancelHandshakeRequest(BaseValidatorModel):
    HandshakeId: str


class Child(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[ChildTypeType] = None


# This class is the input for the 'close_account' function.
class CloseAccountRequest(BaseValidatorModel):
    AccountId: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CreateAccountStatus(BaseValidatorModel):
    Id: Optional[str] = None
    AccountName: Optional[str] = None
    State: Optional[CreateAccountStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    CompletedTimestamp: Optional[datetime] = None
    AccountId: Optional[str] = None
    GovCloudAccountId: Optional[str] = None
    FailureReason: Optional[CreateAccountFailureReasonType] = None


# This class is the input for the 'create_organization' function.
class CreateOrganizationRequest(BaseValidatorModel):
    FeatureSet: Optional[OrganizationFeatureSetType] = None


class OrganizationalUnit(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'decline_handshake' function.
class DeclineHandshakeRequest(BaseValidatorModel):
    HandshakeId: str


class DelegatedAdministrator(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AccountStatusType] = None
    JoinedMethod: Optional[AccountJoinedMethodType] = None
    JoinedTimestamp: Optional[datetime] = None
    DelegationEnabledDate: Optional[datetime] = None


class DelegatedService(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    DelegationEnabledDate: Optional[datetime] = None


# This class is the input for the 'delete_organizational_unit' function.
class DeleteOrganizationalUnitRequest(BaseValidatorModel):
    OrganizationalUnitId: str


# This class is the input for the 'delete_policy' function.
class DeletePolicyRequest(BaseValidatorModel):
    PolicyId: str


# This class is the input for the 'deregister_delegated_administrator' function.
class DeregisterDelegatedAdministratorRequest(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str


# This class is the input for the 'describe_account' function.
class DescribeAccountRequest(BaseValidatorModel):
    AccountId: str


# This class is the input for the 'describe_create_account_status' function.
class DescribeCreateAccountStatusRequest(BaseValidatorModel):
    CreateAccountRequestId: str


# This class is the input for the 'describe_effective_policy' function.
class DescribeEffectivePolicyRequest(BaseValidatorModel):
    PolicyType: EffectivePolicyTypeType
    TargetId: Optional[str] = None


class EffectivePolicy(BaseValidatorModel):
    PolicyContent: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    TargetId: Optional[str] = None
    PolicyType: Optional[EffectivePolicyTypeType] = None


# This class is the input for the 'describe_handshake' function.
class DescribeHandshakeRequest(BaseValidatorModel):
    HandshakeId: str


# This class is the input for the 'describe_organizational_unit' function.
class DescribeOrganizationalUnitRequest(BaseValidatorModel):
    OrganizationalUnitId: str


# This class is the input for the 'describe_policy' function.
class DescribePolicyRequest(BaseValidatorModel):
    PolicyId: str


# This class is the input for the 'detach_policy' function.
class DetachPolicyRequest(BaseValidatorModel):
    PolicyId: str
    TargetId: str


# This class is the input for the 'disable_aws_service_access' function.
class DisableAWSServiceAccessRequest(BaseValidatorModel):
    ServicePrincipal: str


# This class is the input for the 'disable_policy_type' function.
class DisablePolicyTypeRequest(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType


# This class is the input for the 'enable_aws_service_access' function.
class EnableAWSServiceAccessRequest(BaseValidatorModel):
    ServicePrincipal: str


# This class is the input for the 'enable_policy_type' function.
class EnablePolicyTypeRequest(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType


class EnabledServicePrincipal(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    DateEnabled: Optional[datetime] = None


class HandshakeFilter(BaseValidatorModel):
    ActionType: Optional[ActionTypeType] = None
    ParentHandshakeId: Optional[str] = None


class HandshakeParty(BaseValidatorModel):
    Id: str
    Type: HandshakePartyTypeType


class HandshakeResourcePaginator(BaseValidatorModel):
    Value: Optional[str] = None
    Type: Optional[HandshakeResourceTypeType] = None
    Resources: Optional[List[Dict[str, Any]]] = None


class HandshakeResource(BaseValidatorModel):
    Value: Optional[str] = None
    Type: Optional[HandshakeResourceTypeType] = None
    Resources: Optional[List[Dict[str, Any]]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_aws_service_access_for_organization' function.
class ListAWSServiceAccessForOrganizationRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_accounts_for_parent' function.
class ListAccountsForParentRequest(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_accounts' function.
class ListAccountsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_children' function.
class ListChildrenRequest(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_create_account_status' function.
class ListCreateAccountStatusRequest(BaseValidatorModel):
    States: Optional[List[CreateAccountStateType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_delegated_administrators' function.
class ListDelegatedAdministratorsRequest(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_delegated_services_for_account' function.
class ListDelegatedServicesForAccountRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_organizational_units_for_parent' function.
class ListOrganizationalUnitsForParentRequest(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_parents' function.
class ListParentsRequest(BaseValidatorModel):
    ChildId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Parent(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[ParentTypeType] = None


# This class is the input for the 'list_policies_for_target' function.
class ListPoliciesForTargetRequest(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicySummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PolicyTypeType] = None
    AwsManaged: Optional[bool] = None


# This class is the input for the 'list_policies' function.
class ListPoliciesRequest(BaseValidatorModel):
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_roots' function.
class ListRootsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_targets_for_policy' function.
class ListTargetsForPolicyRequest(BaseValidatorModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PolicyTargetSummary(BaseValidatorModel):
    TargetId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[TargetTypeType] = None


# This class is the input for the 'move_account' function.
class MoveAccountRequest(BaseValidatorModel):
    AccountId: str
    SourceParentId: str
    DestinationParentId: str


class PolicyTypeSummary(BaseValidatorModel):
    Type: Optional[PolicyTypeType] = None
    Status: Optional[PolicyTypeStatusType] = None


# This class is the input for the 'register_delegated_administrator' function.
class RegisterDelegatedAdministratorRequest(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str


# This class is the input for the 'remove_account_from_organization' function.
class RemoveAccountFromOrganizationRequest(BaseValidatorModel):
    AccountId: str


class ResourcePolicySummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: List[str]


# This class is the input for the 'update_organizational_unit' function.
class UpdateOrganizationalUnitRequest(BaseValidatorModel):
    OrganizationalUnitId: str
    Name: Optional[str] = None


# This class is the input for the 'update_policy' function.
class UpdatePolicyRequest(BaseValidatorModel):
    PolicyId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Content: Optional[str] = None


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_account' function.
class DescribeAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_accounts_for_parent' function.
class ListAccountsForParentResponse(BaseValidatorModel):
    Accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_accounts' function.
class ListAccountsResponse(BaseValidatorModel):
    Accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_children' function.
class ListChildrenResponse(BaseValidatorModel):
    Children: List[Child]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_account' function.
class CreateAccountRequest(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_gov_cloud_account' function.
class CreateGovCloudAccountRequest(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_organizational_unit' function.
class CreateOrganizationalUnitRequest(BaseValidatorModel):
    ParentId: str
    Name: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_policy' function.
class CreatePolicyRequest(BaseValidatorModel):
    Content: str
    Description: str
    Name: str
    Type: PolicyTypeType
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    Content: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceId: str
    Tags: List[Tag]


# This class is the output for the 'create_account' function.
class CreateAccountResponse(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_gov_cloud_account' function.
class CreateGovCloudAccountResponse(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_create_account_status' function.
class DescribeCreateAccountStatusResponse(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_create_account_status' function.
class ListCreateAccountStatusResponse(BaseValidatorModel):
    CreateAccountStatuses: List[CreateAccountStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_organizational_unit' function.
class CreateOrganizationalUnitResponse(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_organizational_unit' function.
class DescribeOrganizationalUnitResponse(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_organizational_units_for_parent' function.
class ListOrganizationalUnitsForParentResponse(BaseValidatorModel):
    OrganizationalUnits: List[OrganizationalUnit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_organizational_unit' function.
class UpdateOrganizationalUnitResponse(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnit
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_delegated_administrators' function.
class ListDelegatedAdministratorsResponse(BaseValidatorModel):
    DelegatedAdministrators: List[DelegatedAdministrator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_delegated_services_for_account' function.
class ListDelegatedServicesForAccountResponse(BaseValidatorModel):
    DelegatedServices: List[DelegatedService]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_effective_policy' function.
class DescribeEffectivePolicyResponse(BaseValidatorModel):
    EffectivePolicy: EffectivePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_aws_service_access_for_organization' function.
class ListAWSServiceAccessForOrganizationResponse(BaseValidatorModel):
    EnabledServicePrincipals: List[EnabledServicePrincipal]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'list_handshakes_for_account' function.
class ListHandshakesForAccountRequest(BaseValidatorModel):
    Filter: Optional[HandshakeFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_handshakes_for_organization' function.
class ListHandshakesForOrganizationRequest(BaseValidatorModel):
    Filter: Optional[HandshakeFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'invite_account_to_organization' function.
class InviteAccountToOrganizationRequest(BaseValidatorModel):
    Target: HandshakeParty
    Notes: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class HandshakePaginator(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakeParty]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List[HandshakeResourcePaginator]] = None


class Handshake(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakeParty]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List[HandshakeResource]] = None


class ListAWSServiceAccessForOrganizationRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountsForParentRequestPaginate(BaseValidatorModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChildrenRequestPaginate(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCreateAccountStatusRequestPaginate(BaseValidatorModel):
    States: Optional[List[CreateAccountStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDelegatedAdministratorsRequestPaginate(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDelegatedServicesForAccountRequestPaginate(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHandshakesForAccountRequestPaginate(BaseValidatorModel):
    Filter: Optional[HandshakeFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHandshakesForOrganizationRequestPaginate(BaseValidatorModel):
    Filter: Optional[HandshakeFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationalUnitsForParentRequestPaginate(BaseValidatorModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListParentsRequestPaginate(BaseValidatorModel):
    ChildId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPoliciesForTargetRequestPaginate(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPoliciesRequestPaginate(BaseValidatorModel):
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRootsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetsForPolicyRequestPaginate(BaseValidatorModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_parents' function.
class ListParentsResponse(BaseValidatorModel):
    Parents: List[Parent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_policies_for_target' function.
class ListPoliciesForTargetResponse(BaseValidatorModel):
    Policies: List[PolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_policies' function.
class ListPoliciesResponse(BaseValidatorModel):
    Policies: List[PolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Policy(BaseValidatorModel):
    PolicySummary: Optional[PolicySummary] = None
    Content: Optional[str] = None


# This class is the output for the 'list_targets_for_policy' function.
class ListTargetsForPolicyResponse(BaseValidatorModel):
    Targets: List[PolicyTargetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Organization(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    FeatureSet: Optional[OrganizationFeatureSetType] = None
    MasterAccountArn: Optional[str] = None
    MasterAccountId: Optional[str] = None
    MasterAccountEmail: Optional[str] = None
    AvailablePolicyTypes: Optional[List[PolicyTypeSummary]] = None


class Root(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    PolicyTypes: Optional[List[PolicyTypeSummary]] = None


class ResourcePolicy(BaseValidatorModel):
    ResourcePolicySummary: Optional[ResourcePolicySummary] = None
    Content: Optional[str] = None


class ListHandshakesForAccountResponsePaginator(BaseValidatorModel):
    Handshakes: List[HandshakePaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHandshakesForOrganizationResponsePaginator(BaseValidatorModel):
    Handshakes: List[HandshakePaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'accept_handshake' function.
class AcceptHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_handshake' function.
class CancelHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'decline_handshake' function.
class DeclineHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_handshake' function.
class DescribeHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class EnableAllFeaturesResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'invite_account_to_organization' function.
class InviteAccountToOrganizationResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_handshakes_for_account' function.
class ListHandshakesForAccountResponse(BaseValidatorModel):
    Handshakes: List[Handshake]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_handshakes_for_organization' function.
class ListHandshakesForOrganizationResponse(BaseValidatorModel):
    Handshakes: List[Handshake]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_policy' function.
class CreatePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_policy' function.
class DescribePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_policy' function.
class UpdatePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_organization' function.
class CreateOrganizationResponse(BaseValidatorModel):
    Organization: Organization
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationResponse(BaseValidatorModel):
    Organization: Organization
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_policy_type' function.
class DisablePolicyTypeResponse(BaseValidatorModel):
    Root: Root
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_policy_type' function.
class EnablePolicyTypeResponse(BaseValidatorModel):
    Root: Root
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_roots' function.
class ListRootsResponse(BaseValidatorModel):
    Roots: List[Root]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeResourcePolicyResponse(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata