from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sso_admin.sso_admin_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessControlAttributeValueOutput(BaseValidatorModel):
    Source: List[str]


class AccessControlAttributeValue(BaseValidatorModel):
    Source: List[str]


class AccountAssignmentForPrincipal(BaseValidatorModel):
    AccountId: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class AccountAssignmentOperationStatusMetadata(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None


class AccountAssignmentOperationStatus(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None
    TargetId: Optional[str] = None
    TargetType: Optional[Literal['AWS_ACCOUNT']] = None


class AccountAssignment(BaseValidatorModel):
    AccountId: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ApplicationAssignmentForPrincipal(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ApplicationAssignment(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class DisplayData(BaseValidatorModel):
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    IconUrl: Optional[str] = None


class CustomerManagedPolicyReference(BaseValidatorModel):
    Name: str
    Path: Optional[str] = None


class AttachManagedPolicyToPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str


class AttachedManagedPolicy(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class IamAuthenticationMethodOutput(BaseValidatorModel):
    ActorPolicy: Dict[str, Any]


class IamAuthenticationMethod(BaseValidatorModel):
    ActorPolicy: Dict[str, Any]


class AuthorizationCodeGrantOutput(BaseValidatorModel):
    RedirectUris: Optional[List[str]] = None


class AuthorizationCodeGrant(BaseValidatorModel):
    RedirectUris: Optional[List[str]] = None


class AuthorizedTokenIssuerOutput(BaseValidatorModel):
    AuthorizedAudiences: Optional[List[str]] = None
    TrustedTokenIssuerArn: Optional[str] = None


class AuthorizedTokenIssuer(BaseValidatorModel):
    AuthorizedAudiences: Optional[List[str]] = None
    TrustedTokenIssuerArn: Optional[str] = None


class CreateAccountAssignmentRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal['AWS_ACCOUNT']


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateApplicationAssignmentRequest(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class PermissionSet(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None


class DeleteAccountAssignmentRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal['AWS_ACCOUNT']


class DeleteApplicationAccessScopeRequest(BaseValidatorModel):
    ApplicationArn: str
    Scope: str


class DeleteApplicationAssignmentRequest(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class DeleteApplicationAuthenticationMethodRequest(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal['IAM']


class DeleteApplicationGrantRequest(BaseValidatorModel):
    ApplicationArn: str
    GrantType: GrantTypeType


class DeleteApplicationRequest(BaseValidatorModel):
    ApplicationArn: str


class DeleteInlinePolicyFromPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DeleteInstanceAccessControlAttributeConfigurationRequest(BaseValidatorModel):
    InstanceArn: str


class DeleteInstanceRequest(BaseValidatorModel):
    InstanceArn: str


class DeletePermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DeletePermissionsBoundaryFromPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DeleteTrustedTokenIssuerRequest(BaseValidatorModel):
    TrustedTokenIssuerArn: str


class DescribeAccountAssignmentCreationStatusRequest(BaseValidatorModel):
    AccountAssignmentCreationRequestId: str
    InstanceArn: str


class DescribeAccountAssignmentDeletionStatusRequest(BaseValidatorModel):
    AccountAssignmentDeletionRequestId: str
    InstanceArn: str


class DescribeApplicationAssignmentRequest(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class DescribeApplicationProviderRequest(BaseValidatorModel):
    ApplicationProviderArn: str


class DescribeApplicationRequest(BaseValidatorModel):
    ApplicationArn: str


class DescribeInstanceAccessControlAttributeConfigurationRequest(BaseValidatorModel):
    InstanceArn: str


class DescribeInstanceRequest(BaseValidatorModel):
    InstanceArn: str


class DescribePermissionSetProvisioningStatusRequest(BaseValidatorModel):
    InstanceArn: str
    ProvisionPermissionSetRequestId: str


class PermissionSetProvisioningStatus(BaseValidatorModel):
    AccountId: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None


class DescribePermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DescribeTrustedTokenIssuerRequest(BaseValidatorModel):
    TrustedTokenIssuerArn: str


class DetachManagedPolicyFromPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str


class GetApplicationAccessScopeRequest(BaseValidatorModel):
    ApplicationArn: str
    Scope: str


class GetApplicationAssignmentConfigurationRequest(BaseValidatorModel):
    ApplicationArn: str


class GetApplicationAuthenticationMethodRequest(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal['IAM']


class GetApplicationGrantRequest(BaseValidatorModel):
    ApplicationArn: str
    GrantType: GrantTypeType


class GetInlinePolicyForPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class GetPermissionsBoundaryForPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class InstanceMetadata(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    IdentityStoreId: Optional[str] = None
    InstanceArn: Optional[str] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    Status: Optional[InstanceStatusType] = None


class OperationStatusFilter(BaseValidatorModel):
    Status: Optional[StatusValuesType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountAssignmentsFilter(BaseValidatorModel):
    AccountId: Optional[str] = None


class ListAccountAssignmentsRequest(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAccountsForProvisionedPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None


class ListApplicationAccessScopesRequest(BaseValidatorModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ScopeDetails(BaseValidatorModel):
    Scope: str
    AuthorizedTargets: Optional[List[str]] = None


class ListApplicationAssignmentsFilter(BaseValidatorModel):
    ApplicationArn: Optional[str] = None


class ListApplicationAssignmentsRequest(BaseValidatorModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationAuthenticationMethodsRequest(BaseValidatorModel):
    ApplicationArn: str
    NextToken: Optional[str] = None


class ListApplicationGrantsRequest(BaseValidatorModel):
    ApplicationArn: str
    NextToken: Optional[str] = None


class ListApplicationProvidersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationsFilter(BaseValidatorModel):
    ApplicationAccount: Optional[str] = None
    ApplicationProvider: Optional[str] = None


class ListCustomerManagedPolicyReferencesInPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstancesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListManagedPoliciesInPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PermissionSetProvisioningStatusMetadata(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None


class ListPermissionSetsProvisionedToAccountRequest(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None


class ListPermissionSetsRequest(BaseValidatorModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    NextToken: Optional[str] = None


class ListTrustedTokenIssuersRequest(BaseValidatorModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TrustedTokenIssuerMetadata(BaseValidatorModel):
    Name: Optional[str] = None
    TrustedTokenIssuerArn: Optional[str] = None
    TrustedTokenIssuerType: Optional[Literal['OIDC_JWT']] = None


class OidcJwtConfiguration(BaseValidatorModel):
    ClaimAttributePath: str
    IdentityStoreAttributePath: str
    IssuerUrl: str
    JwksRetrievalOption: Literal['OPEN_ID_DISCOVERY']


class OidcJwtUpdateConfiguration(BaseValidatorModel):
    ClaimAttributePath: Optional[str] = None
    IdentityStoreAttributePath: Optional[str] = None
    JwksRetrievalOption: Optional[Literal['OPEN_ID_DISCOVERY']] = None


class SignInOptions(BaseValidatorModel):
    Origin: SignInOriginType
    ApplicationUrl: Optional[str] = None


class ProvisionPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    TargetType: ProvisionTargetTypeType
    TargetId: Optional[str] = None


class PutApplicationAccessScopeRequest(BaseValidatorModel):
    ApplicationArn: str
    Scope: str
    AuthorizedTargets: Optional[List[str]] = None


class PutApplicationAssignmentConfigurationRequest(BaseValidatorModel):
    ApplicationArn: str
    AssignmentRequired: bool


class PutInlinePolicyToPermissionSetRequest(BaseValidatorModel):
    InlinePolicy: str
    InstanceArn: str
    PermissionSetArn: str


class ResourceServerScopeDetails(BaseValidatorModel):
    DetailedTitle: Optional[str] = None
    LongDescription: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]
    InstanceArn: Optional[str] = None


class UpdateInstanceRequest(BaseValidatorModel):
    InstanceArn: str
    Name: str


class UpdatePermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None


class AccessControlAttributeOutput(BaseValidatorModel):
    Key: str
    Value: AccessControlAttributeValueOutput


class AccessControlAttribute(BaseValidatorModel):
    Key: str
    Value: AccessControlAttributeValue


class AttachCustomerManagedPolicyReferenceToPermissionSetRequest(BaseValidatorModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReference
    InstanceArn: str
    PermissionSetArn: str


class DetachCustomerManagedPolicyReferenceFromPermissionSetRequest(BaseValidatorModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReference
    InstanceArn: str
    PermissionSetArn: str


class PermissionsBoundary(BaseValidatorModel):
    CustomerManagedPolicyReference: Optional[CustomerManagedPolicyReference] = None
    ManagedPolicyArn: Optional[str] = None


class AuthenticationMethodOutput(BaseValidatorModel):
    Iam: Optional[IamAuthenticationMethodOutput] = None


class AuthenticationMethod(BaseValidatorModel):
    Iam: Optional[IamAuthenticationMethod] = None


class JwtBearerGrantOutput(BaseValidatorModel):
    AuthorizedTokenIssuers: Optional[List[AuthorizedTokenIssuerOutput]] = None


class JwtBearerGrant(BaseValidatorModel):
    AuthorizedTokenIssuers: Optional[List[AuthorizedTokenIssuer]] = None


class CreateAccountAssignmentResponse(BaseValidatorModel):
    AccountAssignmentCreationStatus: AccountAssignmentOperationStatus
    ResponseMetadata: ResponseMetadata


class CreateApplicationResponse(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceResponse(BaseValidatorModel):
    InstanceArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrustedTokenIssuerResponse(BaseValidatorModel):
    TrustedTokenIssuerArn: str
    ResponseMetadata: ResponseMetadata


class DeleteAccountAssignmentResponse(BaseValidatorModel):
    AccountAssignmentDeletionStatus: AccountAssignmentOperationStatus
    ResponseMetadata: ResponseMetadata


class DescribeAccountAssignmentCreationStatusResponse(BaseValidatorModel):
    AccountAssignmentCreationStatus: AccountAssignmentOperationStatus
    ResponseMetadata: ResponseMetadata


class DescribeAccountAssignmentDeletionStatusResponse(BaseValidatorModel):
    AccountAssignmentDeletionStatus: AccountAssignmentOperationStatus
    ResponseMetadata: ResponseMetadata


class DescribeApplicationAssignmentResponse(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    ResponseMetadata: ResponseMetadata


class DescribeInstanceResponse(BaseValidatorModel):
    CreatedDate: datetime
    IdentityStoreId: str
    InstanceArn: str
    Name: str
    OwnerAccountId: str
    Status: InstanceStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetApplicationAccessScopeResponse(BaseValidatorModel):
    AuthorizedTargets: List[str]
    Scope: str
    ResponseMetadata: ResponseMetadata


class GetApplicationAssignmentConfigurationResponse(BaseValidatorModel):
    AssignmentRequired: bool
    ResponseMetadata: ResponseMetadata


class GetInlinePolicyForPermissionSetResponse(BaseValidatorModel):
    InlinePolicy: str
    ResponseMetadata: ResponseMetadata


class ListAccountAssignmentCreationStatusResponse(BaseValidatorModel):
    AccountAssignmentsCreationStatus: List[AccountAssignmentOperationStatusMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccountAssignmentDeletionStatusResponse(BaseValidatorModel):
    AccountAssignmentsDeletionStatus: List[AccountAssignmentOperationStatusMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccountAssignmentsForPrincipalResponse(BaseValidatorModel):
    AccountAssignments: List[AccountAssignmentForPrincipal]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccountAssignmentsResponse(BaseValidatorModel):
    AccountAssignments: List[AccountAssignment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccountsForProvisionedPermissionSetResponse(BaseValidatorModel):
    AccountIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationAssignmentsForPrincipalResponse(BaseValidatorModel):
    ApplicationAssignments: List[ApplicationAssignmentForPrincipal]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationAssignmentsResponse(BaseValidatorModel):
    ApplicationAssignments: List[ApplicationAssignment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCustomerManagedPolicyReferencesInPermissionSetResponse(BaseValidatorModel):
    CustomerManagedPolicyReferences: List[CustomerManagedPolicyReference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListManagedPoliciesInPermissionSetResponse(BaseValidatorModel):
    AttachedManagedPolicies: List[AttachedManagedPolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPermissionSetsProvisionedToAccountResponse(BaseValidatorModel):
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPermissionSetsResponse(BaseValidatorModel):
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateInstanceRequest(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class CreatePermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    Name: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    InstanceArn: Optional[str] = None


class CreatePermissionSetResponse(BaseValidatorModel):
    PermissionSet: PermissionSet
    ResponseMetadata: ResponseMetadata


class DescribePermissionSetResponse(BaseValidatorModel):
    PermissionSet: PermissionSet
    ResponseMetadata: ResponseMetadata


class DescribePermissionSetProvisioningStatusResponse(BaseValidatorModel):
    PermissionSetProvisioningStatus: PermissionSetProvisioningStatus
    ResponseMetadata: ResponseMetadata


class ProvisionPermissionSetResponse(BaseValidatorModel):
    PermissionSetProvisioningStatus: PermissionSetProvisioningStatus
    ResponseMetadata: ResponseMetadata


class ListInstancesResponse(BaseValidatorModel):
    Instances: List[InstanceMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAccountAssignmentCreationStatusRequest(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAccountAssignmentDeletionStatusRequest(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPermissionSetProvisioningStatusRequest(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAccountAssignmentCreationStatusRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountAssignmentDeletionStatusRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountAssignmentsRequestPaginate(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountsForProvisionedPermissionSetRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationAccessScopesRequestPaginate(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationAssignmentsRequestPaginate(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationAuthenticationMethodsRequestPaginate(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationGrantsRequestPaginate(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationProvidersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedPoliciesInPermissionSetRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPermissionSetProvisioningStatusRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPermissionSetsProvisionedToAccountRequestPaginate(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPermissionSetsRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrustedTokenIssuersRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountAssignmentsForPrincipalRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountAssignmentsForPrincipalRequest(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationAccessScopesResponse(BaseValidatorModel):
    Scopes: List[ScopeDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationAssignmentsForPrincipalRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationAssignmentsForPrincipalRequest(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsRequest(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPermissionSetProvisioningStatusResponse(BaseValidatorModel):
    PermissionSetsProvisioningStatus: List[PermissionSetProvisioningStatusMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrustedTokenIssuersResponse(BaseValidatorModel):
    TrustedTokenIssuers: List[TrustedTokenIssuerMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TrustedTokenIssuerConfiguration(BaseValidatorModel):
    OidcJwtConfiguration: Optional[OidcJwtConfiguration] = None


class TrustedTokenIssuerUpdateConfiguration(BaseValidatorModel):
    OidcJwtConfiguration: Optional[OidcJwtUpdateConfiguration] = None


class PortalOptions(BaseValidatorModel):
    SignInOptions: Optional[SignInOptions] = None
    Visibility: Optional[ApplicationVisibilityType] = None


class UpdateApplicationPortalOptions(BaseValidatorModel):
    SignInOptions: Optional[SignInOptions] = None


class ResourceServerConfig(BaseValidatorModel):
    Scopes: Optional[Dict[str, ResourceServerScopeDetails]] = None


class InstanceAccessControlAttributeConfigurationOutput(BaseValidatorModel):
    AccessControlAttributes: List[AccessControlAttributeOutput]


class InstanceAccessControlAttributeConfiguration(BaseValidatorModel):
    AccessControlAttributes: List[AccessControlAttribute]


class GetPermissionsBoundaryForPermissionSetResponse(BaseValidatorModel):
    PermissionsBoundary: PermissionsBoundary
    ResponseMetadata: ResponseMetadata


class PutPermissionsBoundaryToPermissionSetRequest(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PermissionsBoundary: PermissionsBoundary


class AuthenticationMethodItem(BaseValidatorModel):
    AuthenticationMethod: Optional[AuthenticationMethodOutput] = None
    AuthenticationMethodType: Optional[Literal['IAM']] = None


class GetApplicationAuthenticationMethodResponse(BaseValidatorModel):
    AuthenticationMethod: AuthenticationMethodOutput
    ResponseMetadata: ResponseMetadata

AuthenticationMethodUnion = Union[AuthenticationMethod, AuthenticationMethodOutput]


class GrantOutput(BaseValidatorModel):
    AuthorizationCode: Optional[AuthorizationCodeGrantOutput] = None
    JwtBearer: Optional[JwtBearerGrantOutput] = None
    RefreshToken: Optional[Dict[str, Any]] = None
    TokenExchange: Optional[Dict[str, Any]] = None


class Grant(BaseValidatorModel):
    AuthorizationCode: Optional[AuthorizationCodeGrant] = None
    JwtBearer: Optional[JwtBearerGrant] = None
    RefreshToken: Optional[Dict[str, Any]] = None
    TokenExchange: Optional[Dict[str, Any]] = None


class CreateTrustedTokenIssuerRequest(BaseValidatorModel):
    InstanceArn: str
    Name: str
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfiguration
    TrustedTokenIssuerType: Literal['OIDC_JWT']
    ClientToken: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DescribeTrustedTokenIssuerResponse(BaseValidatorModel):
    Name: str
    TrustedTokenIssuerArn: str
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfiguration
    TrustedTokenIssuerType: Literal['OIDC_JWT']
    ResponseMetadata: ResponseMetadata


class UpdateTrustedTokenIssuerRequest(BaseValidatorModel):
    TrustedTokenIssuerArn: str
    Name: Optional[str] = None
    TrustedTokenIssuerConfiguration: Optional[TrustedTokenIssuerUpdateConfiguration] = None


class Application(BaseValidatorModel):
    ApplicationAccount: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ApplicationProviderArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    InstanceArn: Optional[str] = None
    Name: Optional[str] = None
    PortalOptions: Optional[PortalOptions] = None
    Status: Optional[ApplicationStatusType] = None


class CreateApplicationRequest(BaseValidatorModel):
    ApplicationProviderArn: str
    InstanceArn: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PortalOptions: Optional[PortalOptions] = None
    Status: Optional[ApplicationStatusType] = None
    Tags: Optional[List[Tag]] = None


class DescribeApplicationResponse(BaseValidatorModel):
    ApplicationAccount: str
    ApplicationArn: str
    ApplicationProviderArn: str
    CreatedDate: datetime
    Description: str
    InstanceArn: str
    Name: str
    PortalOptions: PortalOptions
    Status: ApplicationStatusType
    ResponseMetadata: ResponseMetadata


class UpdateApplicationRequest(BaseValidatorModel):
    ApplicationArn: str
    Description: Optional[str] = None
    Name: Optional[str] = None
    PortalOptions: Optional[UpdateApplicationPortalOptions] = None
    Status: Optional[ApplicationStatusType] = None


class ApplicationProvider(BaseValidatorModel):
    ApplicationProviderArn: str
    DisplayData: Optional[DisplayData] = None
    FederationProtocol: Optional[FederationProtocolType] = None
    ResourceServerConfig: Optional[ResourceServerConfig] = None


class DescribeApplicationProviderResponse(BaseValidatorModel):
    ApplicationProviderArn: str
    DisplayData: DisplayData
    FederationProtocol: FederationProtocolType
    ResourceServerConfig: ResourceServerConfig
    ResponseMetadata: ResponseMetadata


class DescribeInstanceAccessControlAttributeConfigurationResponse(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfigurationOutput
    Status: InstanceAccessControlAttributeConfigurationStatusType
    StatusReason: str
    ResponseMetadata: ResponseMetadata

InstanceAccessControlAttributeConfigurationUnion = Union[InstanceAccessControlAttributeConfiguration, InstanceAccessControlAttributeConfigurationOutput]


class ListApplicationAuthenticationMethodsResponse(BaseValidatorModel):
    AuthenticationMethods: List[AuthenticationMethodItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutApplicationAuthenticationMethodRequest(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethod: AuthenticationMethodUnion
    AuthenticationMethodType: Literal['IAM']


class GetApplicationGrantResponse(BaseValidatorModel):
    Grant: GrantOutput
    ResponseMetadata: ResponseMetadata


class GrantItem(BaseValidatorModel):
    Grant: GrantOutput
    GrantType: GrantTypeType

GrantUnion = Union[Grant, GrantOutput]


class ListApplicationsResponse(BaseValidatorModel):
    Applications: List[Application]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationProvidersResponse(BaseValidatorModel):
    ApplicationProviders: List[ApplicationProvider]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateInstanceAccessControlAttributeConfigurationRequest(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfigurationUnion
    InstanceArn: str


class UpdateInstanceAccessControlAttributeConfigurationRequest(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfigurationUnion
    InstanceArn: str


class ListApplicationGrantsResponse(BaseValidatorModel):
    Grants: List[GrantItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutApplicationGrantRequest(BaseValidatorModel):
    ApplicationArn: str
    Grant: GrantUnion
    GrantType: GrantTypeType