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
from aws_resource_validator.pydantic_models.sso_admin_constants import *

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

class AttachManagedPolicyToPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str

class AttachedManagedPolicyTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class IamAuthenticationMethodTypeDef(BaseValidatorModel):
    ActorPolicy: Dict[str, Any]

class AuthorizationCodeGrantTypeDef(BaseValidatorModel):
    RedirectUris: Optional[List[str]] = None

class AuthorizedTokenIssuerTypeDef(BaseValidatorModel):
    AuthorizedAudiences: Optional[List[str]] = None
    TrustedTokenIssuerArn: Optional[str] = None

class CreateAccountAssignmentRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateApplicationAssignmentRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteAccountAssignmentRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]

class DeleteApplicationAccessScopeRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Scope: str

class DeleteApplicationAssignmentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType

class DeleteApplicationAuthenticationMethodRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal["IAM"]

class DeleteApplicationGrantRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    GrantType: GrantTypeType

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str

class DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str

class DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str

class DeleteInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str

class DeletePermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str

class DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str

class DeleteTrustedTokenIssuerRequestRequestTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str

class DescribeAccountAssignmentCreationStatusRequestRequestTypeDef(BaseValidatorModel):
    AccountAssignmentCreationRequestId: str
    InstanceArn: str

class DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef(BaseValidatorModel):
    AccountAssignmentDeletionRequestId: str
    InstanceArn: str

class DescribeApplicationAssignmentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType

class DescribeApplicationProviderRequestRequestTypeDef(BaseValidatorModel):
    ApplicationProviderArn: str

class DescribeApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str

class DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str

class DescribeInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str

class DescribePermissionSetProvisioningStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    ProvisionPermissionSetRequestId: str

class PermissionSetProvisioningStatusTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    FailureReason: Optional[str] = None
    PermissionSetArn: Optional[str] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None

class DescribePermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str

class DescribeTrustedTokenIssuerRequestRequestTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str

class DetachManagedPolicyFromPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    ManagedPolicyArn: str
    PermissionSetArn: str

class GetApplicationAccessScopeRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Scope: str

class GetApplicationAssignmentConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str

class GetApplicationAuthenticationMethodRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethodType: Literal["IAM"]

class GetApplicationGrantRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    GrantType: GrantTypeType

class GetInlinePolicyForPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str

class GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef(BaseValidatorModel):
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

class ListAccountAssignmentsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAccountsForProvisionedPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None

class ListApplicationAccessScopesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ScopeDetailsTypeDef(BaseValidatorModel):
    Scope: str
    AuthorizedTargets: Optional[List[str]] = None

class ListApplicationAssignmentsFilterTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None

class ListApplicationAssignmentsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationAuthenticationMethodsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    NextToken: Optional[str] = None

class ListApplicationGrantsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    NextToken: Optional[str] = None

class ListApplicationProvidersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationsFilterTypeDef(BaseValidatorModel):
    ApplicationAccount: Optional[str] = None
    ApplicationProvider: Optional[str] = None

class ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListInstancesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListManagedPoliciesInPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PermissionSetProvisioningStatusMetadataTypeDef(BaseValidatorModel):
    CreatedDate: Optional[datetime] = None
    RequestId: Optional[str] = None
    Status: Optional[StatusValuesType] = None

class ListPermissionSetsProvisionedToAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None

class ListPermissionSetsRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    NextToken: Optional[str] = None

class ListTrustedTokenIssuersRequestRequestTypeDef(BaseValidatorModel):
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

class ProvisionPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    TargetType: ProvisionTargetTypeType
    TargetId: Optional[str] = None

class PutApplicationAccessScopeRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Scope: str
    AuthorizedTargets: Optional[Sequence[str]] = None

class PutApplicationAssignmentConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AssignmentRequired: bool

class PutInlinePolicyToPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InlinePolicy: str
    InstanceArn: str
    PermissionSetArn: str

class ResourceServerScopeDetailsTypeDef(BaseValidatorModel):
    DetailedTitle: Optional[str] = None
    LongDescription: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]
    InstanceArn: Optional[str] = None

class UpdateInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Name: str

class UpdatePermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None

class AccessControlAttributeTypeDef(BaseValidatorModel):
    Key: str
    Value: AccessControlAttributeValueTypeDef

class AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef
    InstanceArn: str
    PermissionSetArn: str

class DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef
    InstanceArn: str
    PermissionSetArn: str

class PermissionsBoundaryTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReference: Optional[CustomerManagedPolicyReferenceTypeDef] = None
    ManagedPolicyArn: Optional[str] = None

class AuthenticationMethodTypeDef(BaseValidatorModel):
    Iam: Optional[IamAuthenticationMethodTypeDef] = None

class JwtBearerGrantTypeDef(BaseValidatorModel):
    AuthorizedTokenIssuers: Optional[List[AuthorizedTokenIssuerTypeDef]] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentDeletionStatusResponseTypeDef(BaseValidatorModel):
    AccountAssignmentsDeletionStatus: List[AccountAssignmentOperationStatusMetadataTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentsForPrincipalResponseTypeDef(BaseValidatorModel):
    AccountAssignments: List[AccountAssignmentForPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentsResponseTypeDef(BaseValidatorModel):
    AccountAssignments: List[AccountAssignmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsForProvisionedPermissionSetResponseTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssignmentsForPrincipalResponseTypeDef(BaseValidatorModel):
    ApplicationAssignments: List[ApplicationAssignmentForPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssignmentsResponseTypeDef(BaseValidatorModel):
    ApplicationAssignments: List[ApplicationAssignmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef(BaseValidatorModel):
    CustomerManagedPolicyReferences: List[CustomerManagedPolicyReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedPoliciesInPermissionSetResponseTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: List[AttachedManagedPolicyTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionSetsProvisionedToAccountResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionSetsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PermissionSets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Name: str
    Description: Optional[str] = None
    RelayState: Optional[str] = None
    SessionDuration: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssignmentCreationStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAccountAssignmentDeletionStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPermissionSetProvisioningStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentsRequestListAccountAssignmentsPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAccessScopesRequestListApplicationAccessScopesPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAssignmentsRequestListApplicationAssignmentsPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAuthenticationMethodsRequestListApplicationAuthenticationMethodsPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationGrantsRequestListApplicationGrantsPaginateTypeDef(BaseValidatorModel):
    ApplicationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationProvidersRequestListApplicationProvidersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesRequestListInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[OperationStatusFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    InstanceArn: str
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPermissionSetsRequestListPermissionSetsPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    InstanceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrustedTokenIssuersRequestListTrustedTokenIssuersPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentsForPrincipalRequestListAccountAssignmentsForPrincipalPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountAssignmentsForPrincipalRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListAccountAssignmentsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationAccessScopesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Scopes: List[ScopeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssignmentsForPrincipalRequestListApplicationAssignmentsForPrincipalPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationAssignmentsForPrincipalRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PrincipalId: str
    PrincipalType: PrincipalTypeType
    Filter: Optional[ListApplicationAssignmentsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    Filter: Optional[ListApplicationsFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPermissionSetProvisioningStatusResponseTypeDef(BaseValidatorModel):
    NextToken: str
    PermissionSetsProvisioningStatus: List[PermissionSetProvisioningStatusMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrustedTokenIssuersResponseTypeDef(BaseValidatorModel):
    NextToken: str
    TrustedTokenIssuers: List[TrustedTokenIssuerMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class InstanceAccessControlAttributeConfigurationTypeDef(BaseValidatorModel):
    AccessControlAttributes: Sequence[AccessControlAttributeTypeDef]

class GetPermissionsBoundaryForPermissionSetResponseTypeDef(BaseValidatorModel):
    PermissionsBoundary: PermissionsBoundaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceArn: str
    PermissionSetArn: str
    PermissionsBoundary: PermissionsBoundaryTypeDef

class AuthenticationMethodItemTypeDef(BaseValidatorModel):
    AuthenticationMethod: Optional[AuthenticationMethodTypeDef] = None
    AuthenticationMethodType: Optional[Literal["IAM"]] = None

class GetApplicationAuthenticationMethodResponseTypeDef(BaseValidatorModel):
    AuthenticationMethod: AuthenticationMethodTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutApplicationAuthenticationMethodRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    AuthenticationMethod: AuthenticationMethodTypeDef
    AuthenticationMethodType: Literal["IAM"]

class GrantTypeDef(BaseValidatorModel):
    AuthorizationCode: Optional[AuthorizationCodeGrantTypeDef] = None
    JwtBearer: Optional[JwtBearerGrantTypeDef] = None
    RefreshToken: Optional[Dict[str, Any]] = None
    TokenExchange: Optional[Dict[str, Any]] = None

class CreateTrustedTokenIssuerRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateTrustedTokenIssuerRequestRequestTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: str
    Name: Optional[str] = None
    TrustedTokenIssuerConfiguration: Optional[       TrustedTokenIssuerUpdateConfigurationTypeDef     ] = None

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

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
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

class CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: (       InstanceAccessControlAttributeConfigurationTypeDef     )
    InstanceArn: str

class DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: (       InstanceAccessControlAttributeConfigurationTypeDef     )
    Status: InstanceAccessControlAttributeConfigurationStatusType
    StatusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    InstanceAccessControlAttributeConfiguration: (       InstanceAccessControlAttributeConfigurationTypeDef     )
    InstanceArn: str

class ListApplicationAuthenticationMethodsResponseTypeDef(BaseValidatorModel):
    AuthenticationMethods: List[AuthenticationMethodItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationGrantResponseTypeDef(BaseValidatorModel):
    Grant: GrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GrantItemTypeDef(BaseValidatorModel):
    Grant: GrantTypeDef
    GrantType: GrantTypeType

class PutApplicationGrantRequestRequestTypeDef(BaseValidatorModel):
    ApplicationArn: str
    Grant: GrantTypeDef
    GrantType: GrantTypeType

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationProvidersResponseTypeDef(BaseValidatorModel):
    ApplicationProviders: List[ApplicationProviderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationGrantsResponseTypeDef(BaseValidatorModel):
    Grants: List[GrantItemTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

