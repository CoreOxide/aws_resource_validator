# Organizations Classes

# AcceptHandshakeRequestRequestTypeDef

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptHandshakeResponseTypeDef

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING_CLOSURE', 'SUSPENDED']]

### JoinedMethod
- **Type**: typing.Optional[typing.Literal['CREATED', 'INVITED']]

### JoinedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AttachPolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelHandshakeRequestRequestTypeDef

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelHandshakeResponseTypeDef

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChildTypeDef

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']]


# CloseAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountRequestRequestTypeDef

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### AccountName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: typing.Optional[str]

### IamUserAccessToBilling
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]]


# CreateAccountResponseTypeDef

### CreateAccountStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.CreateAccountStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccountStatusTypeDef

### Id
- **Type**: typing.Optional[str]

### AccountName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### RequestedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CompletedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### AccountId
- **Type**: typing.Optional[str]

### GovCloudAccountId
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[typing.Literal['ACCOUNT_LIMIT_EXCEEDED', 'CONCURRENT_ACCOUNT_MODIFICATION', 'EMAIL_ALREADY_EXISTS', 'FAILED_BUSINESS_VALIDATION', 'GOVCLOUD_ACCOUNT_ALREADY_EXISTS', 'INTERNAL_FAILURE', 'INVALID_ADDRESS', 'INVALID_EMAIL', 'INVALID_IDENTITY_FOR_BUSINESS_VALIDATION', 'INVALID_PAYMENT_INSTRUMENT', 'MISSING_BUSINESS_VALIDATION', 'MISSING_PAYMENT_INSTRUMENT', 'PENDING_BUSINESS_VALIDATION', 'UNKNOWN_BUSINESS_VALIDATION', 'UPDATE_EXISTING_RESOURCE_POLICY_WITH_TAGS_NOT_SUPPORTED']]


# CreateGovCloudAccountRequestRequestTypeDef

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### AccountName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: typing.Optional[str]

### IamUserAccessToBilling
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]]


# CreateGovCloudAccountResponseTypeDef

### CreateAccountStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.CreateAccountStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOrganizationRequestRequestTypeDef

### FeatureSet
- **Type**: typing.Optional[typing.Literal['ALL', 'CONSOLIDATED_BILLING']]


# CreateOrganizationResponseTypeDef

### Organization
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.OrganizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOrganizationalUnitRequestRequestTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]]


# CreateOrganizationalUnitResponseTypeDef

### OrganizationalUnit
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.OrganizationalUnitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyRequestRequestTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]]


# CreatePolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeclineHandshakeRequestRequestTypeDef

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeclineHandshakeResponseTypeDef

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DelegatedAdministratorTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING_CLOSURE', 'SUSPENDED']]

### JoinedMethod
- **Type**: typing.Optional[typing.Literal['CREATED', 'INVITED']]

### JoinedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DelegationEnabledDate
- **Type**: typing.Optional[datetime.datetime]


# DelegatedServiceTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### DelegationEnabledDate
- **Type**: typing.Optional[datetime.datetime]


# DeleteOrganizationalUnitRequestRequestTypeDef

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterDelegatedAdministratorRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountResponseTypeDef

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.AccountTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCreateAccountStatusRequestRequestTypeDef

### CreateAccountRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCreateAccountStatusResponseTypeDef

### CreateAccountStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.CreateAccountStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEffectivePolicyRequestRequestTypeDef

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'TAG_POLICY']
- **Required**: Yes

### TargetId
- **Type**: typing.Optional[str]


# DescribeEffectivePolicyResponseTypeDef

### EffectivePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.EffectivePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHandshakeRequestRequestTypeDef

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHandshakeResponseTypeDef

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationResponseTypeDef

### Organization
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.OrganizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationalUnitRequestRequestTypeDef

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOrganizationalUnitResponseTypeDef

### OrganizationalUnit
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.OrganizationalUnitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePolicyResponseTypeDef

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachPolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableAWSServiceAccessRequestRequestTypeDef

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DisablePolicyTypeRequestRequestTypeDef

### RootId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes


# DisablePolicyTypeResponseTypeDef

### Root
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.RootTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EffectivePolicyTypeDef

### PolicyContent
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### TargetId
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'TAG_POLICY']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableAWSServiceAccessRequestRequestTypeDef

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# EnableAllFeaturesResponseTypeDef

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnablePolicyTypeRequestRequestTypeDef

### RootId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes


# EnablePolicyTypeResponseTypeDef

### Root
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.RootTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnabledServicePrincipalTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### DateEnabled
- **Type**: typing.Optional[datetime.datetime]


# HandshakeFilterTypeDef

### ActionType
- **Type**: typing.Optional[typing.Literal['ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE', 'APPROVE_ALL_FEATURES', 'ENABLE_ALL_FEATURES', 'INVITE']]

### ParentHandshakeId
- **Type**: typing.Optional[str]


# HandshakePartyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ACCOUNT', 'EMAIL', 'ORGANIZATION']
- **Required**: Yes


# HandshakeResourceTypeDef

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'EMAIL', 'MASTER_EMAIL', 'MASTER_NAME', 'NOTES', 'ORGANIZATION', 'ORGANIZATION_FEATURE_SET', 'PARENT_HANDSHAKE']]

### Resources
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# HandshakeTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Parties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakePartyTypeDef]]

### State
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'CANCELED', 'DECLINED', 'EXPIRED', 'OPEN', 'REQUESTED']]

### RequestedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[typing.Literal['ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE', 'APPROVE_ALL_FEATURES', 'ENABLE_ALL_FEATURES', 'INVITE']]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakeResourceTypeDef]]


# InviteAccountToOrganizationRequestRequestTypeDef

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakePartyTypeDef'>
- **Required**: Yes

### Notes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]]


# InviteAccountToOrganizationResponseTypeDef

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAWSServiceAccessForOrganizationRequestListAWSServiceAccessForOrganizationPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListAWSServiceAccessForOrganizationRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAWSServiceAccessForOrganizationResponseTypeDef

### EnabledServicePrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.EnabledServicePrincipalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountsForParentRequestListAccountsForParentPaginateTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListAccountsForParentRequestRequestTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountsForParentResponseTypeDef

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.AccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountsRequestListAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListAccountsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountsResponseTypeDef

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.AccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChildrenRequestListChildrenPaginateTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### ChildType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListChildrenRequestRequestTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### ChildType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListChildrenResponseTypeDef

### Children
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.ChildTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCreateAccountStatusRequestListCreateAccountStatusPaginateTypeDef

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListCreateAccountStatusRequestRequestTypeDef

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCreateAccountStatusResponseTypeDef

### CreateAccountStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.CreateAccountStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDelegatedAdministratorsRequestListDelegatedAdministratorsPaginateTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListDelegatedAdministratorsRequestRequestTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDelegatedAdministratorsResponseTypeDef

### DelegatedAdministrators
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.DelegatedAdministratorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDelegatedServicesForAccountRequestListDelegatedServicesForAccountPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListDelegatedServicesForAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDelegatedServicesForAccountResponseTypeDef

### DelegatedServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.DelegatedServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForAccountRequestListHandshakesForAccountPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListHandshakesForAccountRequestRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHandshakesForAccountResponseTypeDef

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForOrganizationRequestListHandshakesForOrganizationPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListHandshakesForOrganizationRequestRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHandshakesForOrganizationResponseTypeDef

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationalUnitsForParentRequestListOrganizationalUnitsForParentPaginateTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListOrganizationalUnitsForParentRequestRequestTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrganizationalUnitsForParentResponseTypeDef

### OrganizationalUnits
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.OrganizationalUnitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListParentsRequestListParentsPaginateTypeDef

### ChildId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListParentsRequestRequestTypeDef

### ChildId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListParentsResponseTypeDef

### Parents
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.ParentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPoliciesForTargetRequestListPoliciesForTargetPaginateTypeDef

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListPoliciesForTargetRequestRequestTypeDef

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoliciesForTargetResponseTypeDef

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.PolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPoliciesRequestListPoliciesPaginateTypeDef

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListPoliciesRequestRequestTypeDef

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoliciesResponseTypeDef

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.PolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRootsRequestListRootsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListRootsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRootsResponseTypeDef

### Roots
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.RootTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListTargetsForPolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTargetsForPolicyResponseTypeDef

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.PolicyTargetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MoveAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParentId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationParentId
- **Type**: <class 'str'>
- **Required**: Yes


# OrganizationTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### FeatureSet
- **Type**: typing.Optional[typing.Literal['ALL', 'CONSOLIDATED_BILLING']]

### MasterAccountArn
- **Type**: typing.Optional[str]

### MasterAccountId
- **Type**: typing.Optional[str]

### MasterAccountEmail
- **Type**: typing.Optional[str]

### AvailablePolicyTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations_classes.PolicyTypeSummaryTypeDef]]


# OrganizationalUnitTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParentTypeDef

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ORGANIZATIONAL_UNIT', 'ROOT']]


# PolicySummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']]

### AwsManaged
- **Type**: typing.Optional[bool]


# PolicyTargetSummaryTypeDef

### TargetId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']]


# PolicyTypeDef

### PolicySummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PolicySummaryTypeDef]

### Content
- **Type**: typing.Optional[str]


# PolicyTypeSummaryTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']]

### Status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'PENDING_DISABLE', 'PENDING_ENABLE']]


# PutResourcePolicyRequestRequestTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]]


# PutResourcePolicyResponseTypeDef

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterDelegatedAdministratorRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAccountFromOrganizationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# ResourcePolicySummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# ResourcePolicyTypeDef

### ResourcePolicySummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.ResourcePolicySummaryTypeDef]

### Content
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RootTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PolicyTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations_classes.PolicyTypeSummaryTypeDef]]


# TagResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.organizations_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateOrganizationalUnitRequestRequestTypeDef

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateOrganizationalUnitResponseTypeDef

### OrganizationalUnit
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.OrganizationalUnitTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePolicyRequestRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]


# UpdatePolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


