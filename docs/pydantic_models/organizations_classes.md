# Organizations Classes

# AcceptHandshakeRequestTypeDef

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


# AttachPolicyRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelHandshakeRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloseAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountRequestTypeDef

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


# CreateGovCloudAccountRequestTypeDef

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


# CreateOrganizationRequestTypeDef

### FeatureSet
- **Type**: typing.Optional[typing.Literal['ALL', 'CONSOLIDATED_BILLING']]


# CreateOrganizationResponseTypeDef

### Organization
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.OrganizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOrganizationalUnitRequestTypeDef

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


# CreatePolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeclineHandshakeRequestTypeDef

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


# DeleteOrganizationalUnitRequestTypeDef

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterDelegatedAdministratorRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountRequestTypeDef

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


# DescribeCreateAccountStatusRequestTypeDef

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


# DescribeEffectivePolicyRequestTypeDef

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'TAG_POLICY']
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


# DescribeHandshakeRequestTypeDef

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


# DescribeOrganizationalUnitRequestTypeDef

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


# DescribePolicyRequestTypeDef

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


# DetachPolicyRequestTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableAWSServiceAccessRequestTypeDef

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DisablePolicyTypeRequestTypeDef

### RootId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
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
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'TAG_POLICY']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableAWSServiceAccessRequestTypeDef

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


# EnablePolicyTypeRequestTypeDef

### RootId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
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


# HandshakePaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakeResourcePaginatorTypeDef]]


# HandshakePartyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HandshakeResourcePaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HandshakeResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# InviteAccountToOrganizationRequestTypeDef

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


# ListAWSServiceAccessForOrganizationRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListAWSServiceAccessForOrganizationRequestTypeDef

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


# ListAccountsForParentRequestPaginateTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListAccountsForParentRequestTypeDef

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


# ListAccountsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListAccountsRequestTypeDef

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


# ListChildrenRequestPaginateTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### ChildType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListChildrenRequestTypeDef

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


# ListCreateAccountStatusRequestPaginateTypeDef

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListCreateAccountStatusRequestTypeDef

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


# ListDelegatedAdministratorsRequestPaginateTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListDelegatedAdministratorsRequestTypeDef

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


# ListDelegatedServicesForAccountRequestPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListDelegatedServicesForAccountRequestTypeDef

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


# ListHandshakesForAccountRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListHandshakesForAccountRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHandshakesForAccountResponsePaginatorTypeDef

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakePaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForAccountResponseTypeDef

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForOrganizationRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListHandshakesForOrganizationRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.HandshakeFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHandshakesForOrganizationResponsePaginatorTypeDef

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakePaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForOrganizationResponseTypeDef

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations_classes.HandshakeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationalUnitsForParentRequestPaginateTypeDef

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListOrganizationalUnitsForParentRequestTypeDef

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


# ListParentsRequestPaginateTypeDef

### ChildId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListParentsRequestTypeDef

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


# ListPoliciesForTargetRequestPaginateTypeDef

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListPoliciesForTargetRequestTypeDef

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
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


# ListPoliciesRequestPaginateTypeDef

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListPoliciesRequestTypeDef

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
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


# ListRootsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListRootsRequestTypeDef

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


# ListTagsForResourceRequestPaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

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


# ListTargetsForPolicyRequestPaginateTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PaginatorConfigTypeDef]


# ListTargetsForPolicyRequestTypeDef

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


# MoveAccountRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PolicyTargetSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PolicyTypeDef

### PolicySummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations_classes.PolicySummaryTypeDef]

### Content
- **Type**: typing.Optional[str]


# PolicyTypeSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutResourcePolicyRequestTypeDef

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


# RegisterDelegatedAdministratorRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAccountFromOrganizationRequestTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateOrganizationalUnitRequestTypeDef

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


# UpdatePolicyRequestTypeDef

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


