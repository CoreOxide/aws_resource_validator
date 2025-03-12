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
from aws_resource_validator.pydantic_models.sso_admin_constants import *

class AccessControlAttributeValueOutputTypeDef(BaseValidatorModel):
    Source: List[str]


class AccessControlAttributeValueTypeDef(BaseValidatorModel):
    Source: Sequence[str]


class AccountAssignmentForPrincipalTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class AccountAssignmentOperationStatusMetadataTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None


class AccountAssignmentOperationStatusTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None
    TargetId: Optional[str] = None
    TargetType: Optional[Literal["AWS_ACCOUNT"]] = None


class AccountAssignmentTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ApplicationAssignmentForPrincipalTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[PrincipalTypeType] = None


class ApplicationAssignmentTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class DisplayDataTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    IconUrl: Optional[str] = None


class CustomerManagedPolicyReferenceTypeDef(BaseValidatorModel):
    Name: str
    Path: Optional[str] = None


class AttachManagedPolicyToPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str


class AttachedManagedPolicyTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class IamAuthenticationMethodOutputTypeDef(BaseValidatorModel):
    ActorPolicy: Dict[str, Any]


class IamAuthenticationMethodTypeDef(BaseValidatorModel):
    ActorPolicy: Mapping[str, Any]


class AuthorizationCodeGrantOutputTypeDef(BaseValidatorModel):
    RedirectUris: Optional[List[str]] = None


class AuthorizationCodeGrantTypeDef(BaseValidatorModel):
    RedirectUris: Optional[Sequence[str]] = None


class AuthorizedTokenIssuerOutputTypeDef(BaseValidatorModel):
    AuthorizedAudiences: Optional[List[str]] = None
    TrustedTokenIssuerArn: Optional[str] = None


class AuthorizedTokenIssuerTypeDef(BaseValidatorModel):
    AuthorizedAudiences: Optional[Sequence[str]] = None
    TrustedTokenIssuerArn: Optional[str] = None


class CreateAccountAssignmentRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateApplicationAssignmentRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class PermissionSetTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None


class DeleteAccountAssignmentRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]


class DeleteApplicationAccessScopeRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Scope: str


class DeleteApplicationAssignmentRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class DeleteApplicationAuthenticationMethodRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal["IAM"]


class DeleteApplicationGrantRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    GrantType: GrantTypeType


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str


class DeleteInlinePolicyFromPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef(BaseValidatorModel):
    InstanceArn: str


class DeleteInstanceRequestTypeDef(BaseValidatorModel):
    InstanceArn: str


class DeletePermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DeletePermissionsBoundaryFromPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DeleteTrustedTokenIssuerRequestTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str


class DescribeAccountAssignmentCreationStatusRequestTypeDef(BaseValidatorModel):
    AccountAssignmentCreationRequestId: str
    InstanceArn: str


class DescribeAccountAssignmentDeletionStatusRequestTypeDef(BaseValidatorModel):
    AccountAssignmentDeletionRequestId: str
    InstanceArn: str


class DescribeApplicationAssignmentRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType


class DescribeApplicationProviderRequestTypeDef(BaseValidatorModel):
    ApplicationProviderArn: str


class DescribeApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str


class DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef(BaseValidatorModel):
    InstanceArn: str


class DescribeInstanceRequestTypeDef(BaseValidatorModel):
    InstanceArn: str


class DescribePermissionSetProvisioningStatusRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    ProvisionPermissionSetRequestId: str


class PermissionSetProvisioningStatusTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None


class DescribePermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class DescribeTrustedTokenIssuerRequestTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str


class DetachManagedPolicyFromPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str


class GetApplicationAccessScopeRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Scope: str


class GetApplicationAssignmentConfigurationRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str


class GetApplicationAuthenticationMethodRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal["IAM"]


class GetApplicationGrantRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    GrantType: GrantTypeType


class GetInlinePolicyForPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class GetPermissionsBoundaryForPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str


class InstanceMetadataTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    IdentityStoreId: Optional[str] = None
    InstanceArn: Optional[str] = None
    Name: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    Status: Optional[InstanceStatusType] = None


class OperationStatusFilterTypeDef(BaseValidatorModel):
    Status: Optional[StatusValuesType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountAssignmentsFilterTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None


class ListAccountAssignmentsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAccountsForProvisionedPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None


class ListApplicationAccessScopesRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ScopeDetailsTypeDef(BaseValidatorModel):
    Scope: str
    AuthorizedTargets: Optional[List[str]] = None


class ListApplicationAssignmentsFilterTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None


class ListApplicationAssignmentsRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationAuthenticationMethodsRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    NextToken: Optional[str] = None


class ListApplicationGrantsRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    NextToken: Optional[str] = None


class ListApplicationProvidersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationsFilterTypeDef(BaseValidatorModel):
    ApplicationAccount: Optional[str] = None
    ApplicationProvider: Optional[str] = None


class ListCustomerManagedPolicyReferencesInPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstancesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListManagedPoliciesInPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PermissionSetProvisioningStatusMetadataTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None


class ListPermissionSetsProvisionedToAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None


class ListPermissionSetsRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    NextToken: Optional[str] = None


class ListTrustedTokenIssuersRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TrustedTokenIssuerMetadataTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    TrustedTokenIssuerArn: Optional[str] = None
    TrustedTokenIssuerType: Optional[Literal["OIDC_JWT"]] = None


class OidcJwtConfigurationTypeDef(BaseValidatorModel):
    ClaimAttributePath: str
    IdentityStoreAttributePath: str
    IssuerUrl: str
    JwksRetrievalOption: Literal["OPEN_ID_DISCOVERY"]


class OidcJwtUpdateConfigurationTypeDef(BaseValidatorModel):
    ClaimAttributePath: Optional[str] = None
    IdentityStoreAttributePath: Optional[str] = None
    JwksRetrievalOption: Optional[Literal["OPEN_ID_DISCOVERY"]] = None


class SignInOptionsTypeDef(BaseValidatorModel):
    Origin: SignInOriginType
    ApplicationUrl: Optional[str] = None


class ProvisionPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    TargetType: ProvisionTargetTypeType
    TargetId: Optional[str] = None


class PutApplicationAccessScopeRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Scope: str
    AuthorizedTargets: Optional[Sequence[str]] = None


class PutApplicationAssignmentConfigurationRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AssignmentRequired: bool


class PutInlinePolicyToPermissionSetRequestTypeDef(BaseValidatorModel):
    InlinePolicy: str
    InstanceArn: str
    PermissionSetArn: str


class ResourceServerScopeDetailsTypeDef(BaseValidatorModel):
    DetailedTitle: Optional[str] = None
    LongDescription: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]
    InstanceArn: Optional[str] = None


class UpdateInstanceRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Name: str


class UpdatePermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None


class AccessControlAttributeOutputTypeDef(BaseValidatorModel):
    Key: str
    Value: AccessControlAttributeValueOutputTypeDef


class AccessControlAttributeTypeDef(BaseValidatorModel):
    Key: str
    Value: AccessControlAttributeValueTypeDef


class AttachCustomerManagedPolicyReferenceToPermissionSetRequestTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef
    InstanceArn: str
    PermissionSetArn: str


class DetachCustomerManagedPolicyReferenceFromPermissionSetRequestTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef
    InstanceArn: str
    PermissionSetArn: str


class PermissionsBoundaryTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReference: Optional[CustomerManagedPolicyReferenceTypeDef] = None
    ManagedPolicyArn: Optional[str] = None


class AuthenticationMethodOutputTypeDef(BaseValidatorModel):
    Iam: Optional[IamAuthenticationMethodOutputTypeDef] = None


class AuthenticationMethodTypeDef(BaseValidatorModel):
    Iam: Optional[IamAuthenticationMethodTypeDef] = None


class JwtBearerGrantOutputTypeDef(BaseValidatorModel):
    AuthorizedTokenIssuers: Optional[List[AuthorizedTokenIssuerOutputTypeDef]] = None


class JwtBearerGrantTypeDef(BaseValidatorModel):
    AuthorizedTokenIssuers: Optional[Sequence[AuthorizedTokenIssuerTypeDef]] = None


class CreateAccountAssignmentResponseTypeDef(BaseValidatorModel):
    AccountAssignmentCreationStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    ApplicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstanceResponseTypeDef(BaseValidatorModel):
    InstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrustedTokenIssuerResponseTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAccountAssignmentResponseTypeDef(BaseValidatorModel):
    AccountAssignmentDeletionStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountAssignmentCreationStatusResponseTypeDef(BaseValidatorModel):
    AccountAssignmentCreationStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountAssignmentDeletionStatusResponseTypeDef(BaseValidatorModel):
    AccountAssignmentDeletionStatus: AccountAssignmentOperationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeApplicationAssignmentResponseTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInstanceResponseTypeDef(BaseValidatorModel):
    CreatedDate: datetime
    IdentityStoreId: str
    InstanceArn: str
    Name: str
    OwnerAccountId: str
    Status: InstanceStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationAccessScopeResponseTypeDef(BaseValidatorModel):
    AuthorizedTargets: List[str]
    Scope: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationAssignmentConfigurationResponseTypeDef(BaseValidatorModel):
    AssignmentRequired: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetInlinePolicyForPermissionSetResponseTypeDef(BaseValidatorModel):
    InlinePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountAssignmentCreationStatusResponseTypeDef(BaseValidatorModel):
    AccountAssignmentsCreationStatus: List[AccountAssignmentOperationStatusMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccountAssignmentDeletionStatusResponseTypeDef(BaseValidatorModel):
    AccountAssignmentsDeletionStatus: List[AccountAssignmentOperationStatusMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccountAssignmentsForPrincipalResponseTypeDef(BaseValidatorModel):
    AccountAssignments: List[AccountAssignmentForPrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccountAssignmentsResponseTypeDef(BaseValidatorModel):
    AccountAssignments: List[AccountAssignmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccountsForProvisionedPermissionSetResponseTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationAssignmentsForPrincipalResponseTypeDef(BaseValidatorModel):
    ApplicationAssignments: List[ApplicationAssignmentForPrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationAssignmentsResponseTypeDef(BaseValidatorModel):
    ApplicationAssignments: List[ApplicationAssignmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReferences: List[CustomerManagedPolicyReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListManagedPoliciesInPermissionSetResponseTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: List[AttachedManagedPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPermissionSetsProvisionedToAccountResponseTypeDef(BaseValidatorModel):
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPermissionSetsResponseTypeDef(BaseValidatorModel):
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateInstanceRequestTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreatePermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Name: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]
    InstanceArn: Optional[str] = None


class CreatePermissionSetResponseTypeDef(BaseValidatorModel):
    PermissionSet: PermissionSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePermissionSetResponseTypeDef(BaseValidatorModel):
    PermissionSet: PermissionSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePermissionSetProvisioningStatusResponseTypeDef(BaseValidatorModel):
    PermissionSetProvisioningStatus: PermissionSetProvisioningStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ProvisionPermissionSetResponseTypeDef(BaseValidatorModel):
    PermissionSetProvisioningStatus: PermissionSetProvisioningStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListInstancesResponseTypeDef(BaseValidatorModel):
    Instances: List[InstanceMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAccountAssignmentCreationStatusRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAccountAssignmentDeletionStatusRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPermissionSetProvisioningStatusRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAccountAssignmentCreationStatusRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountAssignmentDeletionStatusRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountAssignmentsRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountsForProvisionedPermissionSetRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationAccessScopesRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationAssignmentsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationAuthenticationMethodsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationGrantsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationProvidersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstancesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedPoliciesInPermissionSetRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionSetProvisioningStatusRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionSetsProvisionedToAccountRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPermissionSetsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrustedTokenIssuersRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountAssignmentsForPrincipalRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountAssignmentsForPrincipalRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationAccessScopesResponseTypeDef(BaseValidatorModel):
    Scopes: List[ScopeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationAssignmentsForPrincipalRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationAssignmentsForPrincipalRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPermissionSetProvisioningStatusResponseTypeDef(BaseValidatorModel):
    PermissionSetsProvisioningStatus: List[PermissionSetProvisioningStatusMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTrustedTokenIssuersResponseTypeDef(BaseValidatorModel):
    TrustedTokenIssuers: List[TrustedTokenIssuerMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TrustedTokenIssuerConfigurationTypeDef(BaseValidatorModel):
    OidcJwtConfiguration: Optional[OidcJwtConfigurationTypeDef] = None


class TrustedTokenIssuerUpdateConfigurationTypeDef(BaseValidatorModel):
    OidcJwtConfiguration: Optional[OidcJwtUpdateConfigurationTypeDef] = None


class PortalOptionsTypeDef(BaseValidatorModel):
    SignInOptions: Optional[SignInOptionsTypeDef] = None
    Visibility: Optional[ApplicationVisibilityType] = None


class UpdateApplicationPortalOptionsTypeDef(BaseValidatorModel):
    SignInOptions: Optional[SignInOptionsTypeDef] = None


class ResourceServerConfigTypeDef(BaseValidatorModel):
    Scopes: Optional[Dict[str, ResourceServerScopeDetailsTypeDef]] = None


class InstanceAccessControlAttributeConfigurationOutputTypeDef(BaseValidatorModel):
    AccessControlAttributes: List[AccessControlAttributeOutputTypeDef]


class InstanceAccessControlAttributeConfigurationTypeDef(BaseValidatorModel):
    AccessControlAttributes: Sequence[AccessControlAttributeTypeDef]


class GetPermissionsBoundaryForPermissionSetResponseTypeDef(BaseValidatorModel):
    PermissionsBoundary: PermissionsBoundaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutPermissionsBoundaryToPermissionSetRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PermissionsBoundary: PermissionsBoundaryTypeDef


class AuthenticationMethodItemTypeDef(BaseValidatorModel):
    AuthenticationMethod: Optional[AuthenticationMethodOutputTypeDef] = None
    AuthenticationMethodType: Optional[Literal["IAM"]] = None


class GetApplicationAuthenticationMethodResponseTypeDef(BaseValidatorModel):
    AuthenticationMethod: AuthenticationMethodOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GrantOutputTypeDef(BaseValidatorModel):
    AuthorizationCode: Optional[AuthorizationCodeGrantOutputTypeDef] = None
    JwtBearer: Optional[JwtBearerGrantOutputTypeDef] = None
    RefreshToken: Optional[Dict[str, Any]] = None
    TokenExchange: Optional[Dict[str, Any]] = None


class GrantTypeDef(BaseValidatorModel):
    AuthorizationCode: Optional[AuthorizationCodeGrantTypeDef] = None
    JwtBearer: Optional[JwtBearerGrantTypeDef] = None
    RefreshToken: Optional[Mapping[str, Any]] = None
    TokenExchange: Optional[Mapping[str, Any]] = None


class CreateTrustedTokenIssuerRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Name: str
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfigurationTypeDef
    TrustedTokenIssuerType: Literal["OIDC_JWT"]
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeTrustedTokenIssuerResponseTypeDef(BaseValidatorModel):
    Name: str
    TrustedTokenIssuerArn: str
    TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfigurationTypeDef
    TrustedTokenIssuerType: Literal["OIDC_JWT"]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTrustedTokenIssuerRequestTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str
    Name: Optional[str] = None
    TrustedTokenIssuerConfiguration: Optional[TrustedTokenIssuerUpdateConfigurationTypeDef] = None


class ApplicationTypeDef(BaseValidatorModel):
    ApplicationAccount: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ApplicationProviderArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    InstanceArn: Optional[str] = None
    Name: Optional[str] = None
    PortalOptions: Optional[PortalOptionsTypeDef] = None
    Status: Optional[ApplicationStatusType] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationProviderArn: str
    InstanceArn: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PortalOptions: Optional[PortalOptionsTypeDef] = None
    Status: Optional[ApplicationStatusType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeApplicationResponseTypeDef(BaseValidatorModel):
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


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Description: Optional[str] = None
    Name: Optional[str] = None
    PortalOptions: Optional[UpdateApplicationPortalOptionsTypeDef] = None
    Status: Optional[ApplicationStatusType] = None


class ApplicationProviderTypeDef(BaseValidatorModel):
    ApplicationProviderArn: str
    DisplayData: Optional[DisplayDataTypeDef] = None
    FederationProtocol: Optional[FederationProtocolType] = None
    ResourceServerConfig: Optional[ResourceServerConfigTypeDef] = None


class DescribeApplicationProviderResponseTypeDef(BaseValidatorModel):
    ApplicationProviderArn: str
    DisplayData: DisplayDataTypeDef
    FederationProtocol: FederationProtocolType
    ResourceServerConfig: ResourceServerConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: ( InstanceAccessControlAttributeConfigurationOutputTypeDef )
    Status: InstanceAccessControlAttributeConfigurationStatusType
    StatusReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationAuthenticationMethodsResponseTypeDef(BaseValidatorModel):
    AuthenticationMethods: List[AuthenticationMethodItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AuthenticationMethodUnionTypeDef(BaseValidatorModel):
    pass


class PutApplicationAuthenticationMethodRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethod: AuthenticationMethodUnionTypeDef
    AuthenticationMethodType: Literal["IAM"]


class GetApplicationGrantResponseTypeDef(BaseValidatorModel):
    Grant: GrantOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GrantItemTypeDef(BaseValidatorModel):
    Grant: GrantOutputTypeDef
    GrantType: GrantTypeType


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationProvidersResponseTypeDef(BaseValidatorModel):
    ApplicationProviders: List[ApplicationProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InstanceAccessControlAttributeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateInstanceAccessControlAttributeConfigurationRequestTypeDef(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: ( InstanceAccessControlAttributeConfigurationUnionTypeDef )
    InstanceArn: str


class UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: ( InstanceAccessControlAttributeConfigurationUnionTypeDef )
    InstanceArn: str


class ListApplicationGrantsResponseTypeDef(BaseValidatorModel):
    Grants: List[GrantItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GrantUnionTypeDef(BaseValidatorModel):
    pass


class PutApplicationGrantRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Grant: GrantUnionTypeDef
    GrantType: GrantTypeType


