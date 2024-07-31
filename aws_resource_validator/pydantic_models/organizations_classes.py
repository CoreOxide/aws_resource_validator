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
from aws_resource_validator.pydantic_models.organizations_constants import *

class AcceptHandshakeRequestRequestTypeDef(BaseModel):
    HandshakeId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AccountTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AccountStatusType] = None
    JoinedMethod: Optional[AccountJoinedMethodType] = None
    JoinedTimestamp: Optional[datetime] = None

class AttachPolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str
    TargetId: str

class CancelHandshakeRequestRequestTypeDef(BaseModel):
    HandshakeId: str

class ChildTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[ChildTypeType] = None

class CloseAccountRequestRequestTypeDef(BaseModel):
    AccountId: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateAccountStatusTypeDef(BaseModel):
    Id: Optional[str] = None
    AccountName: Optional[str] = None
    State: Optional[CreateAccountStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    CompletedTimestamp: Optional[datetime] = None
    AccountId: Optional[str] = None
    GovCloudAccountId: Optional[str] = None
    FailureReason: Optional[CreateAccountFailureReasonType] = None

class CreateOrganizationRequestRequestTypeDef(BaseModel):
    FeatureSet: Optional[OrganizationFeatureSetType] = None

class OrganizationalUnitTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None

class DeclineHandshakeRequestRequestTypeDef(BaseModel):
    HandshakeId: str

class DelegatedAdministratorTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Email: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[AccountStatusType] = None
    JoinedMethod: Optional[AccountJoinedMethodType] = None
    JoinedTimestamp: Optional[datetime] = None
    DelegationEnabledDate: Optional[datetime] = None

class DelegatedServiceTypeDef(BaseModel):
    ServicePrincipal: Optional[str] = None
    DelegationEnabledDate: Optional[datetime] = None

class DeleteOrganizationalUnitRequestRequestTypeDef(BaseModel):
    OrganizationalUnitId: str

class DeletePolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str

class DeregisterDelegatedAdministratorRequestRequestTypeDef(BaseModel):
    AccountId: str
    ServicePrincipal: str

class DescribeAccountRequestRequestTypeDef(BaseModel):
    AccountId: str

class DescribeCreateAccountStatusRequestRequestTypeDef(BaseModel):
    CreateAccountRequestId: str

class DescribeEffectivePolicyRequestRequestTypeDef(BaseModel):
    PolicyType: EffectivePolicyTypeType
    TargetId: Optional[str] = None

class EffectivePolicyTypeDef(BaseModel):
    PolicyContent: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    TargetId: Optional[str] = None
    PolicyType: Optional[EffectivePolicyTypeType] = None

class DescribeHandshakeRequestRequestTypeDef(BaseModel):
    HandshakeId: str

class DescribeOrganizationalUnitRequestRequestTypeDef(BaseModel):
    OrganizationalUnitId: str

class DescribePolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str

class DetachPolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str
    TargetId: str

class DisableAWSServiceAccessRequestRequestTypeDef(BaseModel):
    ServicePrincipal: str

class DisablePolicyTypeRequestRequestTypeDef(BaseModel):
    RootId: str
    PolicyType: PolicyTypeType

class EnableAWSServiceAccessRequestRequestTypeDef(BaseModel):
    ServicePrincipal: str

class EnablePolicyTypeRequestRequestTypeDef(BaseModel):
    RootId: str
    PolicyType: PolicyTypeType

class EnabledServicePrincipalTypeDef(BaseModel):
    ServicePrincipal: Optional[str] = None
    DateEnabled: Optional[datetime] = None

class HandshakeFilterTypeDef(BaseModel):
    ActionType: Optional[ActionTypeType] = None
    ParentHandshakeId: Optional[str] = None

class HandshakePartyTypeDef(BaseModel):
    Id: str
    Type: HandshakePartyTypeType

class HandshakeResourceTypeDef(BaseModel):
    Value: Optional[str] = None
    Type: Optional[HandshakeResourceTypeType] = None
    Resources: Optional[List[Dict[str, Any]]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAWSServiceAccessForOrganizationRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAccountsForParentRequestRequestTypeDef(BaseModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAccountsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListChildrenRequestRequestTypeDef(BaseModel):
    ParentId: str
    ChildType: ChildTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCreateAccountStatusRequestRequestTypeDef(BaseModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDelegatedAdministratorsRequestRequestTypeDef(BaseModel):
    ServicePrincipal: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDelegatedServicesForAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListOrganizationalUnitsForParentRequestRequestTypeDef(BaseModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListParentsRequestRequestTypeDef(BaseModel):
    ChildId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ParentTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[ParentTypeType] = None

class ListPoliciesForTargetRequestRequestTypeDef(BaseModel):
    TargetId: str
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicySummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PolicyTypeType] = None
    AwsManaged: Optional[bool] = None

class ListPoliciesRequestRequestTypeDef(BaseModel):
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRootsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    NextToken: Optional[str] = None

class ListTargetsForPolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicyTargetSummaryTypeDef(BaseModel):
    TargetId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[TargetTypeType] = None

class MoveAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    SourceParentId: str
    DestinationParentId: str

class PolicyTypeSummaryTypeDef(BaseModel):
    Type: Optional[PolicyTypeType] = None
    Status: Optional[PolicyTypeStatusType] = None

class RegisterDelegatedAdministratorRequestRequestTypeDef(BaseModel):
    AccountId: str
    ServicePrincipal: str

class RemoveAccountFromOrganizationRequestRequestTypeDef(BaseModel):
    AccountId: str

class ResourcePolicySummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagKeys: Sequence[str]

class UpdateOrganizationalUnitRequestRequestTypeDef(BaseModel):
    OrganizationalUnitId: str
    Name: Optional[str] = None

class UpdatePolicyRequestRequestTypeDef(BaseModel):
    PolicyId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Content: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountResponseTypeDef(BaseModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsForParentResponseTypeDef(BaseModel):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAccountsResponseTypeDef(BaseModel):
    Accounts: List[AccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListChildrenResponseTypeDef(BaseModel):
    Children: List[ChildTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateAccountRequestRequestTypeDef(BaseModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateGovCloudAccountRequestRequestTypeDef(BaseModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOrganizationalUnitRequestRequestTypeDef(BaseModel):
    ParentId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePolicyRequestRequestTypeDef(BaseModel):
    Content: str
    Description: str
    Name: str
    Type: PolicyTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    Content: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateAccountResponseTypeDef(BaseModel):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGovCloudAccountResponseTypeDef(BaseModel):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCreateAccountStatusResponseTypeDef(BaseModel):
    CreateAccountStatus: CreateAccountStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCreateAccountStatusResponseTypeDef(BaseModel):
    CreateAccountStatuses: List[CreateAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateOrganizationalUnitResponseTypeDef(BaseModel):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationalUnitResponseTypeDef(BaseModel):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrganizationalUnitsForParentResponseTypeDef(BaseModel):
    OrganizationalUnits: List[OrganizationalUnitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateOrganizationalUnitResponseTypeDef(BaseModel):
    OrganizationalUnit: OrganizationalUnitTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDelegatedAdministratorsResponseTypeDef(BaseModel):
    DelegatedAdministrators: List[DelegatedAdministratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDelegatedServicesForAccountResponseTypeDef(BaseModel):
    DelegatedServices: List[DelegatedServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEffectivePolicyResponseTypeDef(BaseModel):
    EffectivePolicy: EffectivePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAWSServiceAccessForOrganizationResponseTypeDef(BaseModel):
    EnabledServicePrincipals: List[EnabledServicePrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHandshakesForAccountRequestRequestTypeDef(BaseModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHandshakesForOrganizationRequestRequestTypeDef(BaseModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class HandshakeTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakePartyTypeDef]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List["HandshakeResourceTypeDef"]] = None

class InviteAccountToOrganizationRequestRequestTypeDef(BaseModel):
    Target: HandshakePartyTypeDef
    Notes: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsForParentRequestListAccountsForParentPaginateTypeDef(BaseModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsRequestListAccountsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChildrenRequestListChildrenPaginateTypeDef(BaseModel):
    ParentId: str
    ChildType: ChildTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCreateAccountStatusRequestListCreateAccountStatusPaginateTypeDef(BaseModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateTypeDef(BaseModel):
    ServicePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateTypeDef(BaseModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHandshakesForAccountRequestListHandshakesForAccountPaginateTypeDef(BaseModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateTypeDef(BaseModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateTypeDef(BaseModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListParentsRequestListParentsPaginateTypeDef(BaseModel):
    ChildId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesForTargetRequestListPoliciesForTargetPaginateTypeDef(BaseModel):
    TargetId: str
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseModel):
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRootsRequestListRootsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef(BaseModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListParentsResponseTypeDef(BaseModel):
    Parents: List[ParentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPoliciesForTargetResponseTypeDef(BaseModel):
    Policies: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPoliciesResponseTypeDef(BaseModel):
    Policies: List[PolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PolicyTypeDef(BaseModel):
    PolicySummary: Optional[PolicySummaryTypeDef] = None
    Content: Optional[str] = None

class ListTargetsForPolicyResponseTypeDef(BaseModel):
    Targets: List[PolicyTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OrganizationTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    FeatureSet: Optional[OrganizationFeatureSetType] = None
    MasterAccountArn: Optional[str] = None
    MasterAccountId: Optional[str] = None
    MasterAccountEmail: Optional[str] = None
    AvailablePolicyTypes: Optional[List[PolicyTypeSummaryTypeDef]] = None

class RootTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    PolicyTypes: Optional[List[PolicyTypeSummaryTypeDef]] = None

class ResourcePolicyTypeDef(BaseModel):
    ResourcePolicySummary: Optional[ResourcePolicySummaryTypeDef] = None
    Content: Optional[str] = None

class AcceptHandshakeResponseTypeDef(BaseModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelHandshakeResponseTypeDef(BaseModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineHandshakeResponseTypeDef(BaseModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHandshakeResponseTypeDef(BaseModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAllFeaturesResponseTypeDef(BaseModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InviteAccountToOrganizationResponseTypeDef(BaseModel):
    Handshake: HandshakeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHandshakesForAccountResponseTypeDef(BaseModel):
    Handshakes: List[HandshakeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHandshakesForOrganizationResponseTypeDef(BaseModel):
    Handshakes: List[HandshakeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyResponseTypeDef(BaseModel):
    Policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOrganizationResponseTypeDef(BaseModel):
    Organization: OrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationResponseTypeDef(BaseModel):
    Organization: OrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisablePolicyTypeResponseTypeDef(BaseModel):
    Root: RootTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnablePolicyTypeResponseTypeDef(BaseModel):
    Root: RootTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRootsResponseTypeDef(BaseModel):
    Roots: List[RootTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeResourcePolicyResponseTypeDef(BaseModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

