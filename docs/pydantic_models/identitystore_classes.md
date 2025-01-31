# Identitystore Classes

# AddressTypeDef

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

# CreateGroupMembershipRequestRequestTypeDef

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


# CreateGroupRequestRequestTypeDef

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


# CreateUserRequestRequestTypeDef

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


# DeleteGroupMembershipRequestRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupMembershipRequestRequestTypeDef

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


# DescribeGroupRequestRequestTypeDef

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


# DescribeUserRequestRequestTypeDef

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

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


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


# GetGroupIdRequestRequestTypeDef

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


# GetGroupMembershipIdRequestRequestTypeDef

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


# GetUserIdRequestRequestTypeDef

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


# IsMemberInGroupsRequestRequestTypeDef

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


# ListGroupMembershipsForMemberRequestListGroupMembershipsForMemberPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.MemberIdTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListGroupMembershipsForMemberRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupMembershipsRequestListGroupMembershipsPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListGroupMembershipsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsRequestListGroupsPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListGroupsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestListUsersPaginateTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.identitystore_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.identitystore_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# UniqueAttributeTypeDef

### AttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# UpdateGroupRequestRequestTypeDef

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Operations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.identitystore_classes.AttributeOperationTypeDef]
- **Required**: Yes


# UpdateUserRequestRequestTypeDef

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


