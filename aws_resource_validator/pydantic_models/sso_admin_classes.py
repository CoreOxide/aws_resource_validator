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
from aws_resource_validator.pydantic_models.sso_admin_constants import *

class AccessControlAttributeValueTypeDef(BaseModel):
    Source: Sequence[str]

class AccountAssignmentForPrincipalTypeDef(BaseModel):
    AccountId: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class AccountAssignmentOperationStatusMetadataTypeDef(BaseModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None

class AccountAssignmentOperationStatusTypeDef(BaseModel):
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None
    TargetId: Optional[str] = None
    TargetType: Optional[Literal["AWS_ACCOUNT"]] = None

class AccountAssignmentTypeDef(BaseModel):
    AccountId: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class ApplicationAssignmentForPrincipalTypeDef(BaseModel):
    ApplicationArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None

class ApplicationAssignmentTypeDef(BaseModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType

class DisplayDataTypeDef(BaseModel):
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    IconUrl: Optional[str] = None

class CustomerManagedPolicyReferenceTypeDef(BaseModel):
    Name: str
    Path: Optional[str] = None

class AttachManagedPolicyToPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str

class AttachedManagedPolicyTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class IamAuthenticationMethodTypeDef(BaseModel):
    ActorPolicy: Dict[str, Any]

class AuthorizationCodeGrantTypeDef(BaseModel):
    RedirectUris: Optional[List[str]] = None

class AuthorizedTokenIssuerTypeDef(BaseModel):
    AuthorizedAudiences: Optional[List[str]] = None
    TrustedTokenIssuerArn: Optional[str] = None

class CreateAccountAssignmentRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateApplicationAssignmentRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class PermissionSetTypeDef(BaseModel):
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None

class DeleteAccountAssignmentRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]

class DeleteApplicationAccessScopeRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    Scope: str

class DeleteApplicationAssignmentRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType

class DeleteApplicationAuthenticationMethodRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal["IAM"]

class DeleteApplicationGrantRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    GrantType: GrantTypeType

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    ApplicationArn: str

class DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str

class DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseModel):
    InstanceArn: str

class DeleteInstanceRequestRequestTypeDef(BaseModel):
    InstanceArn: str

class DeletePermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str

class DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str

class DeleteTrustedTokenIssuerRequestRequestTypeDef(BaseModel):
    TrustedTokenIssuerArn: str

class DescribeAccountAssignmentCreationStatusRequestRequestTypeDef(BaseModel):
    AccountAssignmentCreationRequestId: str
    InstanceArn: str

class DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef(BaseModel):
    AccountAssignmentDeletionRequestId: str
    InstanceArn: str

class DescribeApplicationAssignmentRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType

class DescribeApplicationProviderRequestRequestTypeDef(BaseModel):
    ApplicationProviderArn: str

class DescribeApplicationRequestRequestTypeDef(BaseModel):
    ApplicationArn: str

class DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseModel):
    InstanceArn: str

class DescribeInstanceRequestRequestTypeDef(BaseModel):
    InstanceArn: str

class DescribePermissionSetProvisioningStatusRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    ProvisionPermissionSetRequestId: str

class PermissionSetProvisioningStatusTypeDef(BaseModel):
    AccountId: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None

class DescribePermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str

class DescribeTrustedTokenIssuerRequestRequestTypeDef(BaseModel):
    TrustedTokenIssuerArn: str

class DetachManagedPolicyFromPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str

class GetApplicationAccessScopeRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    Scope: str

class GetApplicationAssignmentConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationArn: str

class GetApplicationAuthenticationMethodRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal["IAM"]

class GetApplicationGrantRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    GrantType: GrantTypeType

class GetInlinePolicyForPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str

class GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str

class InstanceMetadataTypeDef(BaseModel):
    CreatedDate: Optional[datetime] = None
    IdentityStoreId: Optional[str] = None
    InstanceArn: Optional[str] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    Status: Optional[InstanceStatusType] = None

class OperationStatusFilterTypeDef(BaseModel):
    Status: Optional[StatusValuesType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccountAssignmentsFilterTypeDef(BaseModel):
    AccountId: Optional[str] = None

class ListAccountAssignmentsRequestRequestTypeDef(BaseModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAccountsForProvisionedPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None

class ListApplicationAccessScopesRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ScopeDetailsTypeDef(BaseModel):
    Scope: str
    AuthorizedTargets: Optional[List[str]] = None

class ListApplicationAssignmentsFilterTypeDef(BaseModel):
    ApplicationArn: Optional[str] = None

class ListApplicationAssignmentsRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationAuthenticationMethodsRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    NextToken: Optional[str] = None

class ListApplicationGrantsRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    NextToken: Optional[str] = None

class ListApplicationProvidersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationsFilterTypeDef(BaseModel):
    ApplicationAccount: Optional[str] = None
    ApplicationProvider: Optional[str] = None

class ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInstancesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListManagedPoliciesInPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PermissionSetProvisioningStatusMetadataTypeDef(BaseModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None

class ListPermissionSetsProvisionedToAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None

class ListPermissionSetsRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    NextToken: Optional[str] = None

class ListTrustedTokenIssuersRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TrustedTokenIssuerMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    TrustedTokenIssuerArn: Optional[str] = None
    TrustedTokenIssuerType: Optional[Literal["OIDC_JWT"]] = None

class OidcJwtConfigurationTypeDef(BaseModel):
    ClaimAttributePath: str
    IdentityStoreAttributePath: str
    IssuerUrl: str
    JwksRetrievalOption: Literal["OPEN_ID_DISCOVERY"]

class OidcJwtUpdateConfigurationTypeDef(BaseModel):
    ClaimAttributePath: Optional[str] = None
    IdentityStoreAttributePath: Optional[str] = None
    JwksRetrievalOption: Optional[Literal["OPEN_ID_DISCOVERY"]] = None

class SignInOptionsTypeDef(BaseModel):
    Origin: SignInOriginType
    ApplicationUrl: Optional[str] = None

class ProvisionPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    TargetType: ProvisionTargetTypeType
    TargetId: Optional[str] = None

class PutApplicationAccessScopeRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    Scope: str
    AuthorizedTargets: Optional[Sequence[str]] = None

class PutApplicationAssignmentConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    AssignmentRequired: bool

class PutInlinePolicyToPermissionSetRequestRequestTypeDef(BaseModel):
    InlinePolicy: str
    InstanceArn: str
    PermissionSetArn: str

class ResourceServerScopeDetailsTypeDef(BaseModel):
    DetailedTitle: Optional[str] = None
    LongDescription: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]
    InstanceArn: Optional[str] = None

class UpdateInstanceRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Name: str

class UpdatePermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None

class AccessControlAttributeTypeDef(BaseModel):
    Key: str
    Value: AccessControlAttributeValueTypeDef

class AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef(BaseModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef
    InstanceArn: str
    PermissionSetArn: str

class DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef(BaseModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef
    InstanceArn: str
    PermissionSetArn: str

class PermissionsBoundaryTypeDef(BaseModel):
    CustomerManagedPolicyReference: Optional[CustomerManagedPolicyReferenceTypeDef] = None
    ManagedPolicyArn: Optional[str] = None

class AuthenticationMethodTypeDef(BaseModel):
    Iam: Optional[IamAuthenticationMethodTypeDef] = None

class JwtBearerGrantTypeDef(BaseModel):
    AuthorizedTokenIssuers: Optional[List[AuthorizedTokenIssuerTypeDef]] = None

class CreateAccountAssignmentResponseTypeDef(BaseModel):
    AccountAssignmentCreationStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceResponseTypeDef(BaseModel):
    InstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustedTokenIssuerResponseTypeDef(BaseModel):
    TrustedTokenIssuerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountAssignmentResponseTypeDef(BaseModel):
    AccountAssignmentDeletionStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAssignmentCreationStatusResponseTypeDef(BaseModel):
    AccountAssignmentCreationStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAssignmentDeletionStatusResponseTypeDef(BaseModel):
    AccountAssignmentDeletionStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationAssignmentResponseTypeDef(BaseModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceResponseTypeDef(BaseModel):
    CreatedDate: datetime
    IdentityStoreId: str
    InstanceArn: str
    Name: str
    OwnerAccountId: str
    Status: InstanceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationAccessScopeResponseTypeDef(BaseModel):
    AuthorizedTargets: List[str]
    Scope: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationAssignmentConfigurationResponseTypeDef(BaseModel):
    AssignmentRequired: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetInlinePolicyForPermissionSetResponseTypeDef(BaseModel):
    InlinePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentCreationStatusResponseTypeDef(BaseModel):
    AccountAssignmentsCreationStatus: List[AccountAssignmentOperationStatusMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentDeletionStatusResponseTypeDef(BaseModel):
    AccountAssignmentsDeletionStatus: List[AccountAssignmentOperationStatusMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentsForPrincipalResponseTypeDef(BaseModel):
    AccountAssignments: List[AccountAssignmentForPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentsResponseTypeDef(BaseModel):
    AccountAssignments: List[AccountAssignmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsForProvisionedPermissionSetResponseTypeDef(BaseModel):
    AccountIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssignmentsForPrincipalResponseTypeDef(BaseModel):
    ApplicationAssignments: List[ApplicationAssignmentForPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssignmentsResponseTypeDef(BaseModel):
    ApplicationAssignments: List[ApplicationAssignmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef(BaseModel):
    CustomerManagedPolicyReferences: List[CustomerManagedPolicyReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedPoliciesInPermissionSetResponseTypeDef(BaseModel):
    AttachedManagedPolicies: List[AttachedManagedPolicyTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionSetsProvisionedToAccountResponseTypeDef(BaseModel):
    NextToken: str
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionSetsResponseTypeDef(BaseModel):
    NextToken: str
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceRequestRequestTypeDef(BaseModel):
    ClientToken: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Name: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    NextToken: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]
    InstanceArn: Optional[str] = None

class CreatePermissionSetResponseTypeDef(BaseModel):
    PermissionSet: PermissionSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePermissionSetResponseTypeDef(BaseModel):
    PermissionSet: PermissionSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePermissionSetProvisioningStatusResponseTypeDef(BaseModel):
    PermissionSetProvisioningStatus: PermissionSetProvisioningStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionPermissionSetResponseTypeDef(BaseModel):
    PermissionSetProvisioningStatus: PermissionSetProvisioningStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstancesResponseTypeDef(BaseModel):
    Instances: List[InstanceMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentCreationStatusRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAccountAssignmentDeletionStatusRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPermissionSetProvisioningStatusRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentsRequestListAccountAssignmentsPaginateTypeDef(BaseModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAccessScopesRequestListApplicationAccessScopesPaginateTypeDef(BaseModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAssignmentsRequestListApplicationAssignmentsPaginateTypeDef(BaseModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAuthenticationMethodsRequestListApplicationAuthenticationMethodsPaginateTypeDef(BaseModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationGrantsRequestListApplicationGrantsPaginateTypeDef(BaseModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationProvidersRequestListApplicationProvidersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesRequestListInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateTypeDef(BaseModel):
    AccountId: str
    InstanceArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionSetsRequestListPermissionSetsPaginateTypeDef(BaseModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrustedTokenIssuersRequestListTrustedTokenIssuersPaginateTypeDef(BaseModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentsForPrincipalRequestListAccountAssignmentsForPrincipalPaginateTypeDef(BaseModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentsForPrincipalRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationAccessScopesResponseTypeDef(BaseModel):
    NextToken: str
    Scopes: List[ScopeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssignmentsForPrincipalRequestListApplicationAssignmentsForPrincipalPaginateTypeDef(BaseModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAssignmentsForPrincipalRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPermissionSetProvisioningStatusResponseTypeDef(BaseModel):
    NextToken: str
    PermissionSetsProvisioningStatus: List[PermissionSetProvisioningStatusMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustedTokenIssuersResponseTypeDef(BaseModel):
    NextToken: str
    TrustedTokenIssuers: List[TrustedTokenIssuerMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrustedTokenIssuerConfigurationTypeDef(BaseModel):
    OidcJwtConfiguration: Optional[OidcJwtConfigurationTypeDef] = None

class TrustedTokenIssuerUpdateConfigurationTypeDef(BaseModel):
    OidcJwtConfiguration: Optional[OidcJwtUpdateConfigurationTypeDef] = None

class PortalOptionsTypeDef(BaseModel):
    SignInOptions: Optional[SignInOptionsTypeDef] = None
    Visibility: Optional[ApplicationVisibilityType] = None

class UpdateApplicationPortalOptionsTypeDef(BaseModel):
    SignInOptions: Optional[SignInOptionsTypeDef] = None

class ResourceServerConfigTypeDef(BaseModel):
    Scopes: Optional[Dict[str, ResourceServerScopeDetailsTypeDef]] = None

class InstanceAccessControlAttributeConfigurationTypeDef(BaseModel):
    AccessControlAttributes: Sequence[AccessControlAttributeTypeDef]

class GetPermissionsBoundaryForPermissionSetResponseTypeDef(BaseModel):
    PermissionsBoundary: PermissionsBoundaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    PermissionSetArn: str
    PermissionsBoundary: PermissionsBoundaryTypeDef

class AuthenticationMethodItemTypeDef(BaseModel):
    AuthenticationMethod: Optional[AuthenticationMethodTypeDef] = None
    AuthenticationMethodType: Optional[Literal["IAM"]] = None

class GetApplicationAuthenticationMethodResponseTypeDef(BaseModel):
    AuthenticationMethod: AuthenticationMethodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutApplicationAuthenticationMethodRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    AuthenticationMethod: AuthenticationMethodTypeDef
    AuthenticationMethodType: Literal["IAM"]

class GrantTypeDef(BaseModel):
    AuthorizationCode: Optional[AuthorizationCodeGrantTypeDef] = None
    JwtBearer: Optional[JwtBearerGrantTypeDef] = None
    RefreshToken: Optional[Dict[str, Any]] = None
    TokenExchange: Optional[Dict[str, Any]] = None

class CreateTrustedTokenIssuerRequestRequestTypeDef(BaseModel):
    InstanceArn: str
    Name: str
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfigurationTypeDef
    TrustedTokenIssuerType: Literal["OIDC_JWT"]
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeTrustedTokenIssuerResponseTypeDef(BaseModel):
    Name: str
    TrustedTokenIssuerArn: str
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfigurationTypeDef
    TrustedTokenIssuerType: Literal["OIDC_JWT"]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustedTokenIssuerRequestRequestTypeDef(BaseModel):
    TrustedTokenIssuerArn: str
    Name: Optional[str] = None
    TrustedTokenIssuerConfiguration: Optional[       TrustedTokenIssuerUpdateConfigurationTypeDef     ] = None

class ApplicationTypeDef(BaseModel):
    ApplicationAccount: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ApplicationProviderArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    InstanceArn: Optional[str] = None
    Name: Optional[str] = None
    PortalOptions: Optional[PortalOptionsTypeDef] = None
    Status: Optional[ApplicationStatusType] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationProviderArn: str
    InstanceArn: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PortalOptions: Optional[PortalOptionsTypeDef] = None
    Status: Optional[ApplicationStatusType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeApplicationResponseTypeDef(BaseModel):
    ApplicationAccount: str
    ApplicationArn: str
    ApplicationProviderArn: str
    CreatedDate: datetime
    Description: str
    InstanceArn: str
    Name: str
    PortalOptions: PortalOptionsTypeDef
    Status: ApplicationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    Description: Optional[str] = None
    Name: Optional[str] = None
    PortalOptions: Optional[UpdateApplicationPortalOptionsTypeDef] = None
    Status: Optional[ApplicationStatusType] = None

class ApplicationProviderTypeDef(BaseModel):
    ApplicationProviderArn: str
    DisplayData: Optional[DisplayDataTypeDef] = None
    FederationProtocol: Optional[FederationProtocolType] = None
    ResourceServerConfig: Optional[ResourceServerConfigTypeDef] = None

class DescribeApplicationProviderResponseTypeDef(BaseModel):
    ApplicationProviderArn: str
    DisplayData: DisplayDataTypeDef
    FederationProtocol: FederationProtocolType
    ResourceServerConfig: ResourceServerConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseModel):
    InstanceAccessControlAttributeConfiguration: (       InstanceAccessControlAttributeConfigurationTypeDef     )
    InstanceArn: str

class DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef(BaseModel):
    InstanceAccessControlAttributeConfiguration: (       InstanceAccessControlAttributeConfigurationTypeDef     )
    Status: InstanceAccessControlAttributeConfigurationStatusType
    StatusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseModel):
    InstanceAccessControlAttributeConfiguration: (       InstanceAccessControlAttributeConfigurationTypeDef     )
    InstanceArn: str

class ListApplicationAuthenticationMethodsResponseTypeDef(BaseModel):
    AuthenticationMethods: List[AuthenticationMethodItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationGrantResponseTypeDef(BaseModel):
    Grant: GrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GrantItemTypeDef(BaseModel):
    Grant: GrantTypeDef
    GrantType: GrantTypeType

class PutApplicationGrantRequestRequestTypeDef(BaseModel):
    ApplicationArn: str
    Grant: GrantTypeDef
    GrantType: GrantTypeType

class ListApplicationsResponseTypeDef(BaseModel):
    Applications: List[ApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationProvidersResponseTypeDef(BaseModel):
    ApplicationProviders: List[ApplicationProviderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationGrantsResponseTypeDef(BaseModel):
    Grants: List[GrantItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

