# sso_classes

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


# GetRoleCredentialsRequestRequestTypeDef

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


# ListAccountRolesRequestListAccountRolesPaginateTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_classes.PaginatorConfigTypeDef]


# ListAccountRolesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### roleList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_classes.RoleInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountsRequestListAccountsPaginateTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_classes.PaginatorConfigTypeDef]


# ListAccountsRequestRequestTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccountsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_classes.AccountInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogoutRequestRequestTypeDef

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


