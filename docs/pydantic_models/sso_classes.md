# Sso Classes

# AccountInfo

### accountId
- **Type**: typing.Optional[str]

### accountName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso.sso_classes.ResponseMetadata'>
- **Required**: Yes


# GetRoleCredentialsRequest

### roleName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoleCredentialsResponse

### roleCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sso.sso_classes.RoleCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso.sso_classes.ResponseMetadata'>
- **Required**: Yes


# ListAccountRolesRequest

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccountRolesRequestPaginate

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso.sso_classes.PaginatorConfig]


# ListAccountRolesResponse

### roleList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso.sso_classes.RoleInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso.sso_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAccountsRequest

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccountsRequestPaginate

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso.sso_classes.PaginatorConfig]


# ListAccountsResponse

### accountList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso.sso_classes.AccountInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso.sso_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogoutRequest

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# RoleCredentials

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]

### expiration
- **Type**: typing.Optional[int]


# RoleInfo

### roleName
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]


