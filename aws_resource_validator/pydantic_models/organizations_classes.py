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
from aws_resource_validator.pydantic_models.organizations_constants import *

class AcceptHandshakeRequestRequestTypeDef(BaseValidatorModel):
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

class AttachPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetId: str

class CancelHandshakeRequestRequestTypeDef(BaseValidatorModel):
    HandshakeId: str

class ChildTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[ChildTypeType] = None

class CloseAccountRequestRequestTypeDef(BaseValidatorModel):
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

class CreateOrganizationRequestRequestTypeDef(BaseValidatorModel):
    FeatureSet: Optional[OrganizationFeatureSetType] = None

class OrganizationalUnitTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None

class DeclineHandshakeRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteOrganizationalUnitRequestRequestTypeDef(BaseValidatorModel):
    OrganizationalUnitId: str

class DeletePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str

class DeregisterDelegatedAdministratorRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str

class DescribeAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class DescribeCreateAccountStatusRequestRequestTypeDef(BaseValidatorModel):
    CreateAccountRequestId: str

class DescribeEffectivePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyType: EffectivePolicyTypeType
    TargetId: Optional[str] = None

class EffectivePolicyTypeDef(BaseValidatorModel):
    PolicyContent: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    TargetId: Optional[str] = None
    PolicyType: Optional[EffectivePolicyTypeType] = None

class DescribeHandshakeRequestRequestTypeDef(BaseValidatorModel):
    HandshakeId: str

class DescribeOrganizationalUnitRequestRequestTypeDef(BaseValidatorModel):
    OrganizationalUnitId: str

class DescribePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str

class DetachPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    TargetId: str

class DisableAWSServiceAccessRequestRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: str

class DisablePolicyTypeRequestRequestTypeDef(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType

class EnableAWSServiceAccessRequestRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: str

class EnablePolicyTypeRequestRequestTypeDef(BaseValidatorModel):
    RootId: str
    PolicyType: PolicyTypeType

class EnabledServicePrincipalTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    DateEnabled: Optional[datetime] = None

class HandshakeFilterTypeDef(BaseValidatorModel):
    ActionType: Optional[ActionTypeType] = None
    ParentHandshakeId: Optional[str] = None

class HandshakePartyTypeDef(BaseValidatorModel):
    Id: str
    Type: HandshakePartyTypeType

class HandshakeResourceTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Type: Optional[HandshakeResourceTypeType] = None
    Resources: Optional[List[Dict[str, Any]]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAWSServiceAccessForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAccountsForParentRequestRequestTypeDef(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAccountsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListChildrenRequestRequestTypeDef(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCreateAccountStatusRequestRequestTypeDef(BaseValidatorModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDelegatedAdministratorsRequestRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDelegatedServicesForAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListOrganizationalUnitsForParentRequestRequestTypeDef(BaseValidatorModel):
    ParentId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListParentsRequestRequestTypeDef(BaseValidatorModel):
    ChildId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ParentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[ParentTypeType] = None

class ListPoliciesForTargetRequestRequestTypeDef(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicySummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[PolicyTypeType] = None
    AwsManaged: Optional[bool] = None

class ListPoliciesRequestRequestTypeDef(BaseValidatorModel):
    Filter: PolicyTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRootsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None

class ListTargetsForPolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PolicyTargetSummaryTypeDef(BaseValidatorModel):
    TargetId: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[TargetTypeType] = None

class MoveAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    SourceParentId: str
    DestinationParentId: str

class PolicyTypeSummaryTypeDef(BaseValidatorModel):
    Type: Optional[PolicyTypeType] = None
    Status: Optional[PolicyTypeStatusType] = None

class RegisterDelegatedAdministratorRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ServicePrincipal: str

class RemoveAccountFromOrganizationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class ResourcePolicySummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]

class UpdateOrganizationalUnitRequestRequestTypeDef(BaseValidatorModel):
    OrganizationalUnitId: str
    Name: Optional[str] = None

class UpdatePolicyRequestRequestTypeDef(BaseValidatorModel):
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

class ListChildrenResponseTypeDef(BaseValidatorModel):
    Children: List[ChildTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateAccountRequestRequestTypeDef(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateGovCloudAccountRequestRequestTypeDef(BaseValidatorModel):
    Email: str
    AccountName: str
    RoleName: Optional[str] = None
    IamUserAccessToBilling: Optional[IAMUserAccessToBillingType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateOrganizationalUnitRequestRequestTypeDef(BaseValidatorModel):
    ParentId: str
    Name: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePolicyRequestRequestTypeDef(BaseValidatorModel):
    Content: str
    Description: str
    Name: str
    Type: PolicyTypeType
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    Content: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class ListHandshakesForAccountRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHandshakesForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class HandshakeTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Parties: Optional[List[HandshakePartyTypeDef]] = None
    State: Optional[HandshakeStateType] = None
    RequestedTimestamp: Optional[datetime] = None
    ExpirationTimestamp: Optional[datetime] = None
    Action: Optional[ActionTypeType] = None
    Resources: Optional[List["HandshakeResourceTypeDef"]] = None

class InviteAccountToOrganizationRequestRequestTypeDef(BaseValidatorModel):
    Target: HandshakePartyTypeDef
    Notes: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsForParentRequestListAccountsForParentPaginateTypeDef(BaseValidatorModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsRequestListAccountsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChildrenRequestListChildrenPaginateTypeDef(BaseValidatorModel):
    ParentId: str
    ChildType: ChildTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCreateAccountStatusRequestListCreateAccountStatusPaginateTypeDef(BaseValidatorModel):
    States: Optional[Sequence[CreateAccountStateType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHandshakesForAccountRequestListHandshakesForAccountPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateTypeDef(BaseValidatorModel):
    Filter: Optional[HandshakeFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateTypeDef(BaseValidatorModel):
    ParentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListParentsRequestListParentsPaginateTypeDef(BaseValidatorModel):
    ChildId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesForTargetRequestListPoliciesForTargetPaginateTypeDef(BaseValidatorModel):
    TargetId: str
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseValidatorModel):
    Filter: PolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRootsRequestListRootsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef(BaseValidatorModel):
    PolicyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListParentsResponseTypeDef(BaseValidatorModel):
    Parents: List[ParentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class ListTargetsForPolicyResponseTypeDef(BaseValidatorModel):
    Targets: List[PolicyTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

