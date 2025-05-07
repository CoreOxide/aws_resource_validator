# Identitystore Classes

# Address

### StreetAddress
- **Type**: typing.Optional[str]

### Locality
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### Formatted
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


# AlternateIdentifier

### ExternalId
- **Type**: <class 'NoneType'>

### UniqueAttribute
- **Type**: <class 'NoneType'>


# AttributeOperation

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateGroupMembershipRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.MemberId'>
- **Required**: Yes


# CreateGroupMembershipResponse

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGroupRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateGroupResponse

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Name
- **Type**: <class 'NoneType'>

### DisplayName
- **Type**: typing.Optional[str]

### NickName
- **Type**: typing.Optional[str]

### ProfileUrl
- **Type**: typing.Optional[str]

### Emails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Email]]

### Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Address]]

### PhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PhoneNumber]]

### UserType
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### PreferredLanguage
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]


# CreateUserResponse

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGroupMembershipRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupMembershipRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupMembershipResponse

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.MemberId'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGroupRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupResponse

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ExternalId]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponse

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ExternalId]
- **Required**: Yes

### Name
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Name'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### NickName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Emails
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Email]
- **Required**: Yes

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Address]
- **Required**: Yes

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PhoneNumber]
- **Required**: Yes

### UserType
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### PreferredLanguage
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: <class 'str'>
- **Required**: Yes

### Timezone
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# Email

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


# ExternalId

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# Filter

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupIdRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.AlternateIdentifier'>
- **Required**: Yes


# GetGroupIdResponse

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupMembershipIdRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.MemberId'>
- **Required**: Yes


# GetGroupMembershipIdResponse

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserIdRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.AlternateIdentifier'>
- **Required**: Yes


# GetUserIdResponse

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# Group

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### ExternalIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ExternalId]]

### Description
- **Type**: typing.Optional[str]


# GroupMembership

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### MemberId
- **Type**: <class 'NoneType'>


# GroupMembershipExistenceResult

### GroupId
- **Type**: typing.Optional[str]

### MemberId
- **Type**: <class 'NoneType'>

### MembershipExists
- **Type**: typing.Optional[bool]


# IsMemberInGroupsRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.MemberId'>
- **Required**: Yes

### GroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# IsMemberInGroupsResponse

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.GroupMembershipExistenceResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes


# ListGroupMembershipsForMemberRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.MemberId'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsForMemberRequestPaginate

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.MemberId'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PaginatorConfig]


# ListGroupMembershipsForMemberResponse

### GroupMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.GroupMembership]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsRequestPaginate

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PaginatorConfig]


# ListGroupMembershipsResponse

### GroupMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.GroupMembership]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Filter]]


# ListGroupsRequestPaginate

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PaginatorConfig]


# ListGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Group]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Filter]]


# ListUsersRequestPaginate

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PaginatorConfig]


# ListUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberId

### UserId
- **Type**: typing.Optional[str]


# Name

### Formatted
- **Type**: typing.Optional[str]

### FamilyName
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### MiddleName
- **Type**: typing.Optional[str]

### HonorificPrefix
- **Type**: typing.Optional[str]

### HonorificSuffix
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumber

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


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


# UniqueAttribute

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# UpdateGroupRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.AttributeOperation]
- **Required**: Yes


# UpdateUserRequest

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.AttributeOperation]
- **Required**: Yes


# User

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### ExternalIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.ExternalId]]

### Name
- **Type**: <class 'NoneType'>

### DisplayName
- **Type**: typing.Optional[str]

### NickName
- **Type**: typing.Optional[str]

### ProfileUrl
- **Type**: typing.Optional[str]

### Emails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Email]]

### Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.Address]]

### PhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore.identitystore_classes.PhoneNumber]]

### UserType
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### PreferredLanguage
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]


