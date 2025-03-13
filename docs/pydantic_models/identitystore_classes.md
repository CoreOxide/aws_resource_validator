# Identitystore Classes

# AddressTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlternateIdentifierTypeDef

### ExternalId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.ExternalIdTypeDef]

### UniqueAttribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.UniqueAttributeTypeDef]


# AttributeOperationTypeDef

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateGroupMembershipRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes


# CreateGroupMembershipResponseTypeDef

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateGroupResponseTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.NameTypeDef]

### DisplayName
- **Type**: typing.Optional[str]

### NickName
- **Type**: typing.Optional[str]

### ProfileUrl
- **Type**: typing.Optional[str]

### Emails
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.EmailTypeDef]]

### Addresses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.AddressTypeDef]]

### PhoneNumbers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.PhoneNumberTypeDef]]

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


# CreateUserResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGroupMembershipRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupMembershipRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupMembershipResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGroupRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupResponseTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.ExternalIdTypeDef]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponseTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.ExternalIdTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.NameTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.EmailTypeDef]
- **Required**: Yes

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.AddressTypeDef]
- **Required**: Yes

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.PhoneNumberTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExternalIdTypeDef

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# FilterTypeDef

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupIdRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.AlternateIdentifierTypeDef'>
- **Required**: Yes


# GetGroupIdResponseTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupMembershipIdRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes


# GetGroupMembershipIdResponseTypeDef

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserIdRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### AlternateIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.AlternateIdentifierTypeDef'>
- **Required**: Yes


# GetUserIdResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupMembershipExistenceResultTypeDef

### GroupId
- **Type**: typing.Optional[str]

### MemberId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef]

### MembershipExists
- **Type**: typing.Optional[bool]


# GroupMembershipTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### MemberId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef]


# GroupTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### ExternalIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore_classes.ExternalIdTypeDef]]

### Description
- **Type**: typing.Optional[str]


# IsMemberInGroupsRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes

### GroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# IsMemberInGroupsResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.GroupMembershipExistenceResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupMembershipsForMemberRequestPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListGroupMembershipsForMemberRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsForMemberResponseTypeDef

### GroupMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.GroupMembershipTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembershipsRequestPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListGroupMembershipsRequestTypeDef

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


# ListGroupMembershipsResponseTypeDef

### GroupMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.GroupMembershipTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.FilterTypeDef]]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.GroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.FilterTypeDef]]


# ListUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.identitystore_classes.UserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberIdTypeDef

### UserId
- **Type**: typing.Optional[str]


# NameTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumberTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# UniqueAttributeTypeDef

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# UpdateGroupRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.AttributeOperationTypeDef]
- **Required**: Yes


# UpdateUserRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.AttributeOperationTypeDef]
- **Required**: Yes


# UserTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### ExternalIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore_classes.ExternalIdTypeDef]]

### Name
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.NameTypeDef]

### DisplayName
- **Type**: typing.Optional[str]

### NickName
- **Type**: typing.Optional[str]

### ProfileUrl
- **Type**: typing.Optional[str]

### Emails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore_classes.EmailTypeDef]]

### Addresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore_classes.AddressTypeDef]]

### PhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.identitystore_classes.PhoneNumberTypeDef]]

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


