# Ds Data Classes

# AddGroupMemberRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### MemberRealm
- **Type**: typing.Optional[str]


# AttributeValue

### BOOL
- **Type**: typing.Optional[bool]

### N
- **Type**: typing.Optional[int]

### S
- **Type**: typing.Optional[str]

### SS
- **Type**: typing.Optional[typing.List[str]]


# AttributeValueOutput

### BOOL
- **Type**: typing.Optional[bool]

### N
- **Type**: typing.Optional[int]

### S
- **Type**: typing.Optional[str]

### SS
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateGroupRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### GroupScope
- **Type**: typing.Optional[typing.Literal['BuiltinLocal', 'DomainLocal', 'Global', 'Universal']]

### GroupType
- **Type**: typing.Optional[typing.Literal['Distribution', 'Security']]

### OtherAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValue, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]]]


# CreateGroupResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### OtherAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValue, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]]]

### Surname
- **Type**: typing.Optional[str]


# CreateUserResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGroupRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteUserRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DescribeGroupRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### OtherAttributes
- **Type**: typing.Optional[typing.List[str]]

### Realm
- **Type**: typing.Optional[str]


# DescribeGroupResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DistinguishedName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupScope
- **Type**: typing.Literal['BuiltinLocal', 'DomainLocal', 'Global', 'Universal']
- **Required**: Yes

### GroupType
- **Type**: typing.Literal['Distribution', 'Security']
- **Required**: Yes

### OtherAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### OtherAttributes
- **Type**: typing.Optional[typing.List[str]]

### Realm
- **Type**: typing.Optional[str]


# DescribeUserResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DistinguishedName
- **Type**: <class 'str'>
- **Required**: Yes

### EmailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### GivenName
- **Type**: <class 'str'>
- **Required**: Yes

### OtherAttributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes

### Surname
- **Type**: <class 'str'>
- **Required**: Yes

### UserPrincipalName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes


# DisableUserRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# Group

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### DistinguishedName
- **Type**: typing.Optional[str]

### GroupScope
- **Type**: typing.Optional[typing.Literal['BuiltinLocal', 'DomainLocal', 'Global', 'Universal']]

### GroupType
- **Type**: typing.Optional[typing.Literal['Distribution', 'Security']]

### OtherAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]]

### SID
- **Type**: typing.Optional[str]


# GroupSummary

### GroupScope
- **Type**: typing.Literal['BuiltinLocal', 'DomainLocal', 'Global', 'Universal']
- **Required**: Yes

### GroupType
- **Type**: typing.Literal['Distribution', 'Security']
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes


# ListGroupMembersRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### MemberRealm
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]


# ListGroupMembersRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberRealm
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.PaginatorConfig]


# ListGroupMembersResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberRealm
- **Type**: <class 'str'>
- **Required**: Yes

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.Member]
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsForMemberRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### MemberRealm
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]


# ListGroupsForMemberRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberRealm
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.PaginatorConfig]


# ListGroupsForMemberResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.GroupSummary]
- **Required**: Yes

### MemberRealm
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.PaginatorConfig]


# ListGroupsResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.GroupSummary]
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]


# ListUsersRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.PaginatorConfig]


# ListUsersResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.UserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Member

### MemberType
- **Type**: typing.Literal['COMPUTER', 'GROUP', 'USER']
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RemoveGroupMemberRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### MemberRealm
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


# SearchGroupsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchAttributes
- **Type**: typing.List[str]
- **Required**: Yes

### SearchString
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]


# SearchGroupsRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchAttributes
- **Type**: typing.List[str]
- **Required**: Yes

### SearchString
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.PaginatorConfig]


# SearchGroupsResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.Group]
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchUsersRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchAttributes
- **Type**: typing.List[str]
- **Required**: Yes

### SearchString
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Realm
- **Type**: typing.Optional[str]


# SearchUsersRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SearchAttributes
- **Type**: typing.List[str]
- **Required**: Yes

### SearchString
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.PaginatorConfig]


# SearchUsersResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_data.ds_data_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# UpdateGroupRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### GroupScope
- **Type**: typing.Optional[typing.Literal['BuiltinLocal', 'DomainLocal', 'Global', 'Universal']]

### GroupType
- **Type**: typing.Optional[typing.Literal['Distribution', 'Security']]

### OtherAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValue, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]]]

### UpdateType
- **Type**: typing.Optional[typing.Literal['ADD', 'REMOVE', 'REPLACE']]


# UpdateUserRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### GivenName
- **Type**: typing.Optional[str]

### OtherAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValue, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]]]

### Surname
- **Type**: typing.Optional[str]

### UpdateType
- **Type**: typing.Optional[typing.Literal['ADD', 'REMOVE', 'REPLACE']]


# User

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### DistinguishedName
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### GivenName
- **Type**: typing.Optional[str]

### OtherAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ds_data.ds_data_classes.AttributeValueOutput]]

### SID
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]

### UserPrincipalName
- **Type**: typing.Optional[str]


# UserSummary

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SAMAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### SID
- **Type**: <class 'str'>
- **Required**: Yes

### GivenName
- **Type**: typing.Optional[str]

### Surname
- **Type**: typing.Optional[str]


