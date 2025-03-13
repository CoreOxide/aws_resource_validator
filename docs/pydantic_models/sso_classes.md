# Sso Classes

# AccountInfoTypeDef

### accountId
- **Type**: typing.Optional[str]

### accountName
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRoleCredentialsRequestTypeDef

### roleName
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoleCredentialsResponseTypeDef

### roleCredentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.RoleCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountRolesRequestPaginateTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_classes.PaginatorConfigTypeDef]


# ListAccountRolesRequestTypeDef

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


# ListAccountRolesResponseTypeDef

### roleList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_classes.RoleInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAccountsRequestPaginateTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_classes.PaginatorConfigTypeDef]


# ListAccountsRequestTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccountsResponseTypeDef

### accountList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_classes.AccountInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogoutRequestTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# RoleCredentialsTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### sessionToken
- **Type**: typing.Optional[str]

### expiration
- **Type**: typing.Optional[int]


# RoleInfoTypeDef

### roleName
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]


