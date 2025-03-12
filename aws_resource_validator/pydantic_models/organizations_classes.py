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

class AcceptHandshakeRequestTypeDef(BaseValidatorModel):
    HandshakeId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AccountTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AccountStatusType] = None
    JoinedMethod: Optional[AccountJoinedMethodType] = None
    JoinedTimestamp: Optional[datetime] = None


class AttachPolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetId: str


class CancelHandshakeRequestTypeDef(BaseValidatorModel):
    HandshakeId: str


class CloseAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateAccountStatusTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    AccountName: Optional[str] = None
    State: Optional[CreateAccountStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    CompletedTimestamp: Optional[datetime] = None
    AccountId: Optional[str] = None
    GovCloudAccountId: Optional[str] = None
    FailureReason: Optional[CreateAccountFailureReasonType] = None


class CreateOrganizationRequestTypeDef(BaseValidatorModel):
    FeatureSet: Optional[OrganizationFeatureSetType] = None


class OrganizationalUnitTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


class DeclineHandshakeRequestTypeDef(BaseValidatorModel):
    HandshakeId: str


class DelegatedAdministratorTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AccountStatusType] = None
    JoinedMethod: Optional[AccountJoinedMethodType] = None
    JoinedTimestamp: Optional[datetime] = None
    DelegationEnabledDate: Optional[datetime] = None


class DelegatedServiceTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    DelegationEnabledDate: Optional[datetime] = None


class DeleteOrganizationalUnitRequestTypeDef(BaseValidatorModel):
    OrganizationalUnitId: str


class DeletePolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str


class DeregisterDelegatedAdministratorRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str


class DescribeAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str


class DescribeCreateAccountStatusRequestTypeDef(BaseValidatorModel):
    CreateAccountRequestId: str


class DescribeEffectivePolicyRequestTypeDef(BaseValidatorModel):
    PolicyType: EffectivePolicyTypeType
    TargetId: Optional[str] = None


class EffectivePolicyTypeDef(BaseValidatorModel):
    PolicyContent: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    TargetId: Optional[str] = None
    PolicyType: Optional[EffectivePolicyTypeType] = None


class DescribeHandshakeRequestTypeDef(BaseValidatorModel):
    HandshakeId: str


class DescribeOrganizationalUnitRequestTypeDef(BaseValidatorModel):
    OrganizationalUnitId: str


class DescribePolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str


class DetachPolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetId: str


class DisableAWSServiceAccessRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: str


class DisablePolicyTypeRequestTypeDef(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType


class EnableAWSServiceAccessRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: str


class EnablePolicyTypeRequestTypeDef(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType


class EnabledServicePrincipalTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    DateEnabled: Optional[datetime] = None


class HandshakeFilterTypeDef(BaseValidatorModel):
    ActionType: Optional[ActionTypeType] = None
    ParentHandshakeId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAWSServiceAccessForOrganizationRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccountsForParentRequestTypeDef(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAccountsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListChildrenRequestTypeDef(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCreateAccountStatusRequestTypeDef(BaseValidatorModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDelegatedAdministratorsRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDelegatedServicesForAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOrganizationalUnitsForParentRequestTypeDef(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListParentsRequestTypeDef(BaseValidatorModel):
    ChildId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoliciesForTargetRequestTypeDef(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPoliciesRequestTypeDef(BaseValidatorModel):
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRootsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None


class ListTargetsForPolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MoveAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    SourceParentId: str
    DestinationParentId: str


class RegisterDelegatedAdministratorRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str


class RemoveAccountFromOrganizationRequestTypeDef(BaseValidatorModel):
    AccountId: str


class ResourcePolicySummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]


class UpdateOrganizationalUnitRequestTypeDef(BaseValidatorModel):
    OrganizationalUnitId: str
    Name: Optional[str] = None


class UpdatePolicyRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Content: Optional[str] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountResponseTypeDef(BaseValidatorModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountsForParentResponseTypeDef(BaseValidatorModel):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccountsResponseTypeDef(BaseValidatorModel):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ChildTypeDef(BaseValidatorModel):
    pass


class ListChildrenResponseTypeDef(BaseValidatorModel):
    Children: List[ChildTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateAccountRequestTypeDef(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateGovCloudAccountRequestTypeDef(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateOrganizationalUnitRequestTypeDef(BaseValidatorModel):
    ParentId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    Content: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]


class CreateAccountResponseTypeDef(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGovCloudAccountResponseTypeDef(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCreateAccountStatusResponseTypeDef(BaseValidatorModel):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCreateAccountStatusResponseTypeDef(BaseValidatorModel):
    CreateAccountStatuses: List[CreateAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateOrganizationalUnitResponseTypeDef(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationalUnitResponseTypeDef(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListOrganizationalUnitsForParentResponseTypeDef(BaseValidatorModel):
    OrganizationalUnits: List[OrganizationalUnitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateOrganizationalUnitResponseTypeDef(BaseValidatorModel):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDelegatedAdministratorsResponseTypeDef(BaseValidatorModel):
    DelegatedAdministrators: List[DelegatedAdministratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDelegatedServicesForAccountResponseTypeDef(BaseValidatorModel):
    DelegatedServices: List[DelegatedServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeEffectivePolicyResponseTypeDef(BaseValidatorModel):
    EffectivePolicy: EffectivePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAWSServiceAccessForOrganizationResponseTypeDef(BaseValidatorModel):
    EnabledServicePrincipals: List[EnabledServicePrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListHandshakesForAccountRequestTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHandshakesForOrganizationRequestTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class HandshakePartyTypeDef(BaseValidatorModel):
    pass


class InviteAccountToOrganizationRequestTypeDef(BaseValidatorModel):
    Target: HandshakePartyTypeDef
    Notes: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class HandshakeResourcePaginatorTypeDef(BaseValidatorModel):
    pass


class HandshakePaginatorTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakePartyTypeDef]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List[HandshakeResourcePaginatorTypeDef]] = None


class HandshakeResourceTypeDef(BaseValidatorModel):
    pass


class HandshakeTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakePartyTypeDef]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List[HandshakeResourceTypeDef]] = None


class ListAWSServiceAccessForOrganizationRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountsForParentRequestPaginateTypeDef(BaseValidatorModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListChildrenRequestPaginateTypeDef(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCreateAccountStatusRequestPaginateTypeDef(BaseValidatorModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDelegatedAdministratorsRequestPaginateTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDelegatedServicesForAccountRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHandshakesForAccountRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHandshakesForOrganizationRequestPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOrganizationalUnitsForParentRequestPaginateTypeDef(BaseValidatorModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListParentsRequestPaginateTypeDef(BaseValidatorModel):
    ChildId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoliciesForTargetRequestPaginateTypeDef(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRootsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetsForPolicyRequestPaginateTypeDef(BaseValidatorModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ParentTypeDef(BaseValidatorModel):
    pass


class ListParentsResponseTypeDef(BaseValidatorModel):
    Parents: List[ParentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PolicySummaryTypeDef(BaseValidatorModel):
    pass


class ListPoliciesForTargetResponseTypeDef(BaseValidatorModel):
    Policies: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPoliciesResponseTypeDef(BaseValidatorModel):
    Policies: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PolicyTypeDef(BaseValidatorModel):
    PolicySummary: Optional[PolicySummaryTypeDef] = None
    Content: Optional[str] = None


class PolicyTargetSummaryTypeDef(BaseValidatorModel):
    pass


class ListTargetsForPolicyResponseTypeDef(BaseValidatorModel):
    Targets: List[PolicyTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PolicyTypeSummaryTypeDef(BaseValidatorModel):
    pass


class OrganizationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    FeatureSet: Optional[OrganizationFeatureSetType] = None
    MasterAccountArn: Optional[str] = None
    MasterAccountId: Optional[str] = None
    MasterAccountEmail: Optional[str] = None
    AvailablePolicyTypes: Optional[List[PolicyTypeSummaryTypeDef]] = None


class RootTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    PolicyTypes: Optional[List[PolicyTypeSummaryTypeDef]] = None


class ResourcePolicyTypeDef(BaseValidatorModel):
    ResourcePolicySummary: Optional[ResourcePolicySummaryTypeDef] = None
    Content: Optional[str] = None


class ListHandshakesForAccountResponsePaginatorTypeDef(BaseValidatorModel):
    Handshakes: List[HandshakePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListHandshakesForOrganizationResponsePaginatorTypeDef(BaseValidatorModel):
    Handshakes: List[HandshakePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AcceptHandshakeResponseTypeDef(BaseValidatorModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CancelHandshakeResponseTypeDef(BaseValidatorModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeclineHandshakeResponseTypeDef(BaseValidatorModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeHandshakeResponseTypeDef(BaseValidatorModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnableAllFeaturesResponseTypeDef(BaseValidatorModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InviteAccountToOrganizationResponseTypeDef(BaseValidatorModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListHandshakesForAccountResponseTypeDef(BaseValidatorModel):
    Handshakes: List[HandshakeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListHandshakesForOrganizationResponseTypeDef(BaseValidatorModel):
    Handshakes: List[HandshakeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreatePolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePolicyResponseTypeDef(BaseValidatorModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOrganizationResponseTypeDef(BaseValidatorModel):
    Organization: OrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOrganizationResponseTypeDef(BaseValidatorModel):
    Organization: OrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisablePolicyTypeResponseTypeDef(BaseValidatorModel):
    Root: RootTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnablePolicyTypeResponseTypeDef(BaseValidatorModel):
    Root: RootTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRootsResponseTypeDef(BaseValidatorModel):
    Roots: List[RootTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


