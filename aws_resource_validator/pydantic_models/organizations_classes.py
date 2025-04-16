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
from aws_resource_validator.pydantic_models.organizations_constants import *

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


class AttachPolicyRequest(BaseValidatorModel):
    PolicyId: str
    TargetId: str


class CancelHandshakeRequest(BaseValidatorModel):
    HandshakeId: str


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


class CreateOrganizationRequest(BaseValidatorModel):
    FeatureSet: Optional[OrganizationFeatureSetType] = None


class OrganizationalUnit(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


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


class DeleteOrganizationalUnitRequest(BaseValidatorModel):
    OrganizationalUnitId: str


class DeletePolicyRequest(BaseValidatorModel):
    PolicyId: str


class DeregisterDelegatedAdministratorRequest(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str


class DescribeAccountRequest(BaseValidatorModel):
    AccountId: str


class DescribeCreateAccountStatusRequest(BaseValidatorModel):
    CreateAccountRequestId: str


class DescribeEffectivePolicyRequest(BaseValidatorModel):
    PolicyType: EffectivePolicyTypeType
    TargetId: Optional[str] = None


class EffectivePolicy(BaseValidatorModel):
    PolicyContent: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    TargetId: Optional[str] = None
    PolicyType: Optional[EffectivePolicyTypeType] = None


class DescribeHandshakeRequest(BaseValidatorModel):
    HandshakeId: str


class DescribeOrganizationalUnitRequest(BaseValidatorModel):
    OrganizationalUnitId: str


class DescribePolicyRequest(BaseValidatorModel):
    PolicyId: str


class DetachPolicyRequest(BaseValidatorModel):
    PolicyId: str
    TargetId: str


class DisableAWSServiceAccessRequest(BaseValidatorModel):
    ServicePrincipal: str


class DisablePolicyTypeRequest(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType


class EnableAWSServiceAccessRequest(BaseValidatorModel):
    ServicePrincipal: str


class EnablePolicyTypeRequest(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType


class EnabledServicePrincipal(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    DateEnabled: Optional[datetime] = None


class HandshakeFilter(BaseValidatorModel):
    ActionType: Optional[ActionTypeType] = None
    ParentHandshakeId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAWSServiceAccessForOrganizationRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccountsForParentRequest(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccountsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListChildrenRequest(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCreateAccountStatusRequest(BaseValidatorModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDelegatedAdministratorsRequest(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDelegatedServicesForAccountRequest(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOrganizationalUnitsForParentRequest(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListParentsRequest(BaseValidatorModel):
    ChildId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoliciesForTargetRequest(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoliciesRequest(BaseValidatorModel):
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRootsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None


class ListTargetsForPolicyRequest(BaseValidatorModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MoveAccountRequest(BaseValidatorModel):
    AccountId: str
    SourceParentId: str
    DestinationParentId: str


class RegisterDelegatedAdministratorRequest(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str


class RemoveAccountFromOrganizationRequest(BaseValidatorModel):
    AccountId: str


class ResourcePolicySummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]


class UpdateOrganizationalUnitRequest(BaseValidatorModel):
    OrganizationalUnitId: str
    Name: Optional[str] = None


class UpdatePolicyRequest(BaseValidatorModel):
    PolicyId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Content: Optional[str] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class DescribeAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


class ListAccountsForParentResponse(BaseValidatorModel):
    Accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccountsResponse(BaseValidatorModel):
    Accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Child(BaseValidatorModel):
    pass


class ListChildrenResponse(BaseValidatorModel):
    Children: List[Child]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateAccountRequest(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateGovCloudAccountRequest(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateOrganizationalUnitRequest(BaseValidatorModel):
    ParentId: str
    Name: str
    Tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    Content: str
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[Tag]


class CreateAccountResponse(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatus
    ResponseMetadata: ResponseMetadata


class CreateGovCloudAccountResponse(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatus
    ResponseMetadata: ResponseMetadata


class DescribeCreateAccountStatusResponse(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatus
    ResponseMetadata: ResponseMetadata


class ListCreateAccountStatusResponse(BaseValidatorModel):
    CreateAccountStatuses: List[CreateAccountStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateOrganizationalUnitResponse(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnit
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationalUnitResponse(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnit
    ResponseMetadata: ResponseMetadata


class ListOrganizationalUnitsForParentResponse(BaseValidatorModel):
    OrganizationalUnits: List[OrganizationalUnit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateOrganizationalUnitResponse(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnit
    ResponseMetadata: ResponseMetadata


class ListDelegatedAdministratorsResponse(BaseValidatorModel):
    DelegatedAdministrators: List[DelegatedAdministrator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDelegatedServicesForAccountResponse(BaseValidatorModel):
    DelegatedServices: List[DelegatedService]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEffectivePolicyResponse(BaseValidatorModel):
    EffectivePolicy: EffectivePolicy
    ResponseMetadata: ResponseMetadata


class ListAWSServiceAccessForOrganizationResponse(BaseValidatorModel):
    EnabledServicePrincipals: List[EnabledServicePrincipal]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHandshakesForAccountRequest(BaseValidatorModel):
    Filter: Optional[HandshakeFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHandshakesForOrganizationRequest(BaseValidatorModel):
    Filter: Optional[HandshakeFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class HandshakeParty(BaseValidatorModel):
    pass


class InviteAccountToOrganizationRequest(BaseValidatorModel):
    Target: HandshakeParty
    Notes: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class HandshakeResourcePaginator(BaseValidatorModel):
    pass


class HandshakePaginator(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakeParty]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List[HandshakeResourcePaginator]] = None


class HandshakeResource(BaseValidatorModel):
    pass


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
    States: Optional[Sequence[CreateAccountStateType]] = None
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


class Parent(BaseValidatorModel):
    pass


class ListParentsResponse(BaseValidatorModel):
    Parents: List[Parent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PolicySummary(BaseValidatorModel):
    pass


class ListPoliciesForTargetResponse(BaseValidatorModel):
    Policies: List[PolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPoliciesResponse(BaseValidatorModel):
    Policies: List[PolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Policy(BaseValidatorModel):
    PolicySummary: Optional[PolicySummary] = None
    Content: Optional[str] = None


class PolicyTargetSummary(BaseValidatorModel):
    pass


class ListTargetsForPolicyResponse(BaseValidatorModel):
    Targets: List[PolicyTargetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PolicyTypeSummary(BaseValidatorModel):
    pass


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


class AcceptHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class CancelHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class DeclineHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class DescribeHandshakeResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class EnableAllFeaturesResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class InviteAccountToOrganizationResponse(BaseValidatorModel):
    Handshake: Handshake
    ResponseMetadata: ResponseMetadata


class ListHandshakesForAccountResponse(BaseValidatorModel):
    Handshakes: List[Handshake]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHandshakesForOrganizationResponse(BaseValidatorModel):
    Handshakes: List[Handshake]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreatePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class DescribePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class UpdatePolicyResponse(BaseValidatorModel):
    Policy: Policy
    ResponseMetadata: ResponseMetadata


class CreateOrganizationResponse(BaseValidatorModel):
    Organization: Organization
    ResponseMetadata: ResponseMetadata


class DescribeOrganizationResponse(BaseValidatorModel):
    Organization: Organization
    ResponseMetadata: ResponseMetadata


class DisablePolicyTypeResponse(BaseValidatorModel):
    Root: Root
    ResponseMetadata: ResponseMetadata


class EnablePolicyTypeResponse(BaseValidatorModel):
    Root: Root
    ResponseMetadata: ResponseMetadata


class ListRootsResponse(BaseValidatorModel):
    Roots: List[Root]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeResourcePolicyResponse(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


