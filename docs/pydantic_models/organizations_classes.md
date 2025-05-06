# Organizations Classes

# AcceptHandshakeRequest

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptHandshakeResponse

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# Account

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


# AttachPolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelHandshakeRequest

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelHandshakeResponse

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# Child

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']]


# CloseAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]]


# CreateAccountResponse

### CreateAccountStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.CreateAccountStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccountStatus

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


# CreateGovCloudAccountRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]]


# CreateGovCloudAccountResponse

### CreateAccountStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.CreateAccountStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOrganizationRequest

### FeatureSet
- **Type**: typing.Optional[typing.Literal['ALL', 'CONSOLIDATED_BILLING']]


# CreateOrganizationResponse

### Organization
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Organization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOrganizationalUnitRequest

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]]


# CreateOrganizationalUnitResponse

### OrganizationalUnit
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.OrganizationalUnit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyRequest

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
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]]


# CreatePolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DeclineHandshakeRequest

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeclineHandshakeResponse

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DelegatedAdministrator

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


# DelegatedService

### ServicePrincipal
- **Type**: typing.Optional[str]

### DelegationEnabledDate
- **Type**: typing.Optional[datetime.datetime]


# DeleteOrganizationalUnitRequest

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterDelegatedAdministratorRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountResponse

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Account'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCreateAccountStatusRequest

### CreateAccountRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCreateAccountStatusResponse

### CreateAccountStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.CreateAccountStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEffectivePolicyRequest

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'TAG_POLICY']
- **Required**: Yes

### TargetId
- **Type**: typing.Optional[str]


# DescribeEffectivePolicyResponse

### EffectivePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.EffectivePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHandshakeRequest

### HandshakeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHandshakeResponse

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationResponse

### Organization
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Organization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationalUnitRequest

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOrganizationalUnitResponse

### OrganizationalUnit
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.OrganizationalUnit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourcePolicyResponse

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# DetachPolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableAWSServiceAccessRequest

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DisablePolicyTypeRequest

### RootId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes


# DisablePolicyTypeResponse

### Root
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Root'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# EffectivePolicy

### PolicyContent
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### TargetId
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'TAG_POLICY']]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# EnableAWSServiceAccessRequest

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# EnableAllFeaturesResponse

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# EnablePolicyTypeRequest

### RootId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes


# EnablePolicyTypeResponse

### Root
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Root'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# EnabledServicePrincipal

### ServicePrincipal
- **Type**: typing.Optional[str]

### DateEnabled
- **Type**: typing.Optional[datetime.datetime]


# Handshake

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Parties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeParty]]

### State
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'CANCELED', 'DECLINED', 'EXPIRED', 'OPEN', 'REQUESTED']]

### RequestedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[typing.Literal['ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE', 'APPROVE_ALL_FEATURES', 'ENABLE_ALL_FEATURES', 'INVITE']]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeResource]]


# HandshakeFilter

### ActionType
- **Type**: typing.Optional[typing.Literal['ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE', 'APPROVE_ALL_FEATURES', 'ENABLE_ALL_FEATURES', 'INVITE']]

### ParentHandshakeId
- **Type**: typing.Optional[str]


# HandshakePaginator

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Parties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeParty]]

### State
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'CANCELED', 'DECLINED', 'EXPIRED', 'OPEN', 'REQUESTED']]

### RequestedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[typing.Literal['ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE', 'APPROVE_ALL_FEATURES', 'ENABLE_ALL_FEATURES', 'INVITE']]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeResourcePaginator]]


# HandshakeParty

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ACCOUNT', 'EMAIL', 'ORGANIZATION']
- **Required**: Yes


# HandshakeResource

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'EMAIL', 'MASTER_EMAIL', 'MASTER_NAME', 'NOTES', 'ORGANIZATION', 'ORGANIZATION_FEATURE_SET', 'PARENT_HANDSHAKE']]

### Resources
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# HandshakeResourcePaginator

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'EMAIL', 'MASTER_EMAIL', 'MASTER_NAME', 'NOTES', 'ORGANIZATION', 'ORGANIZATION_FEATURE_SET', 'PARENT_HANDSHAKE']]

### Resources
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# InviteAccountToOrganizationRequest

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeParty'>
- **Required**: Yes

### Notes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]]


# InviteAccountToOrganizationResponse

### Handshake
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# ListAWSServiceAccessForOrganizationRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAWSServiceAccessForOrganizationRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListAWSServiceAccessForOrganizationResponse

### EnabledServicePrincipals
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.EnabledServicePrincipal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountsForParentRequest

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountsForParentRequestPaginate

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListAccountsForParentResponse

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Account]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListAccountsResponse

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Account]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChildrenRequest

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


# ListChildrenRequestPaginate

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### ChildType
- **Type**: typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListChildrenResponse

### Children
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Child]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCreateAccountStatusRequest

### States
- **Type**: typing.Optional[typing.List[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCreateAccountStatusRequestPaginate

### States
- **Type**: typing.Optional[typing.List[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListCreateAccountStatusResponse

### CreateAccountStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.CreateAccountStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDelegatedAdministratorsRequest

### ServicePrincipal
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDelegatedAdministratorsRequestPaginate

### ServicePrincipal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListDelegatedAdministratorsResponse

### DelegatedAdministrators
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.DelegatedAdministrator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDelegatedServicesForAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDelegatedServicesForAccountRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListDelegatedServicesForAccountResponse

### DelegatedServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.DelegatedService]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForAccountRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHandshakesForAccountRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListHandshakesForAccountResponse

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForAccountResponsePaginator

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForOrganizationRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHandshakesForOrganizationRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakeFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListHandshakesForOrganizationResponse

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Handshake]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHandshakesForOrganizationResponsePaginator

### Handshakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.HandshakePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationalUnitsForParentRequest

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrganizationalUnitsForParentRequestPaginate

### ParentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListOrganizationalUnitsForParentResponse

### OrganizationalUnits
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.OrganizationalUnit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListParentsRequest

### ChildId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListParentsRequestPaginate

### ChildId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListParentsResponse

### Parents
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Parent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPoliciesForTargetRequest

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


# ListPoliciesForTargetRequestPaginate

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListPoliciesForTargetResponse

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.PolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPoliciesRequest

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPoliciesRequestPaginate

### Filter
- **Type**: typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListPoliciesResponse

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.PolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRootsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRootsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListRootsResponse

### Roots
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Root]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTargetsForPolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTargetsForPolicyRequestPaginate

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.organizations.organizations_classes.PaginatorConfig]


# ListTargetsForPolicyResponse

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.PolicyTargetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MoveAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParentId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationParentId
- **Type**: <class 'str'>
- **Required**: Yes


# Organization

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.PolicyTypeSummary]]


# OrganizationalUnit

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parent

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ORGANIZATIONAL_UNIT', 'ROOT']]


# Policy

### PolicySummary
- **Type**: <class 'NoneType'>

### Content
- **Type**: typing.Optional[str]


# PolicySummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']]

### AwsManaged
- **Type**: typing.Optional[bool]


# PolicyTargetSummary

### TargetId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATIONAL_UNIT', 'ROOT']]


# PolicyTypeSummary

### Type
- **Type**: typing.Optional[typing.Literal['AISERVICES_OPT_OUT_POLICY', 'BACKUP_POLICY', 'CHATBOT_POLICY', 'DECLARATIVE_POLICY_EC2', 'RESOURCE_CONTROL_POLICY', 'SERVICE_CONTROL_POLICY', 'TAG_POLICY']]

### Status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'PENDING_DISABLE', 'PENDING_ENABLE']]


# PutResourcePolicyRequest

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]]


# PutResourcePolicyResponse

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterDelegatedAdministratorRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAccountFromOrganizationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# ResourcePolicy

### ResourcePolicySummary
- **Type**: <class 'NoneType'>

### Content
- **Type**: typing.Optional[str]


# ResourcePolicySummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# ResponseMetadata

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


# Root

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PolicyTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.PolicyTypeSummary]]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.organizations.organizations_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateOrganizationalUnitRequest

### OrganizationalUnitId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateOrganizationalUnitResponse

### OrganizationalUnit
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.OrganizationalUnit'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePolicyRequest

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]


# UpdatePolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.organizations.organizations_classes.ResponseMetadata'>
- **Required**: Yes


