# Cognito Identity Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CognitoIdentityProviderTypeDef

### ProviderName
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### ServerSideTokenCheck
- **Type**: typing.Optional[bool]


# CreateIdentityPoolInputTypeDef

### IdentityPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### AllowUnauthenticatedIdentities
- **Type**: <class 'bool'>
- **Required**: Yes

### AllowClassicFlow
- **Type**: typing.Optional[bool]

### SupportedLoginProviders
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DeveloperProviderName
- **Type**: typing.Optional[str]

### OpenIdConnectProviderARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### CognitoIdentityProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_identity_classes.CognitoIdentityProviderTypeDef]]

### SamlProviderARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### IdentityPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CredentialsTypeDef

### AccessKeyId
- **Type**: typing.Optional[str]

### SecretKey
- **Type**: typing.Optional[str]

### SessionToken
- **Type**: typing.Optional[str]

### Expiration
- **Type**: typing.Optional[datetime.datetime]


# DeleteIdentitiesInputTypeDef

### IdentityIdsToDelete
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteIdentitiesResponseTypeDef

### UnprocessedIdentityIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.UnprocessedIdentityIdTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIdentityPoolInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityInputTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityPoolInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCredentialsForIdentityInputTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CustomRoleArn
- **Type**: typing.Optional[str]


# GetCredentialsForIdentityResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.CredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### Logins
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetIdResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityPoolRolesInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityPoolRolesResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RoleMappings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.cognito_identity_classes.RoleMappingOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOpenIdTokenForDeveloperIdentityInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### IdentityId
- **Type**: typing.Optional[str]

### PrincipalTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TokenDuration
- **Type**: typing.Optional[int]


# GetOpenIdTokenForDeveloperIdentityResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOpenIdTokenInputTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetOpenIdTokenResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPrincipalTagAttributeMapInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrincipalTagAttributeMapResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### UseDefaults
- **Type**: <class 'bool'>
- **Required**: Yes

### PrincipalTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityDescriptionResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.List[str]
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityDescriptionTypeDef

### IdentityId
- **Type**: typing.Optional[str]

### Logins
- **Type**: typing.Optional[typing.List[str]]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# IdentityPoolRequestTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### AllowUnauthenticatedIdentities
- **Type**: <class 'bool'>
- **Required**: Yes

### AllowClassicFlow
- **Type**: typing.Optional[bool]

### SupportedLoginProviders
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DeveloperProviderName
- **Type**: typing.Optional[str]

### OpenIdConnectProviderARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### CognitoIdentityProviders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_identity_classes.CognitoIdentityProviderTypeDef]]

### SamlProviderARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### IdentityPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# IdentityPoolShortDescriptionTypeDef

### IdentityPoolId
- **Type**: typing.Optional[str]

### IdentityPoolName
- **Type**: typing.Optional[str]


# IdentityPoolTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### AllowUnauthenticatedIdentities
- **Type**: <class 'bool'>
- **Required**: Yes

### AllowClassicFlow
- **Type**: <class 'bool'>
- **Required**: Yes

### SupportedLoginProviders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DeveloperProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### OpenIdConnectProviderARNs
- **Type**: typing.List[str]
- **Required**: Yes

### CognitoIdentityProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.CognitoIdentityProviderTypeDef]
- **Required**: Yes

### SamlProviderARNs
- **Type**: typing.List[str]
- **Required**: Yes

### IdentityPoolTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdentitiesInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### HideDisabled
- **Type**: typing.Optional[bool]


# ListIdentitiesResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identities
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.IdentityDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoolsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_identity_classes.PaginatorConfigTypeDef]


# ListIdentityPoolsInputTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoolsResponseTypeDef

### IdentityPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.IdentityPoolShortDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LookupDeveloperIdentityInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: typing.Optional[str]

### DeveloperUserIdentifier
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# LookupDeveloperIdentityResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DeveloperUserIdentifierList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MappingRuleTypeDef

### Claim
- **Type**: <class 'str'>
- **Required**: Yes

### MatchType
- **Type**: typing.Literal['Contains', 'Equals', 'NotEqual', 'StartsWith']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# MergeDeveloperIdentitiesInputTypeDef

### SourceUserIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationUserIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### DeveloperProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# MergeDeveloperIdentitiesResponseTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
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


# RoleMappingOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RoleMappingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RulesConfigurationTypeOutputTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.MappingRuleTypeDef]
- **Required**: Yes


# RulesConfigurationTypeTypeDef

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_identity_classes.MappingRuleTypeDef]
- **Required**: Yes


# SetIdentityPoolRolesInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### RoleMappings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.cognito_identity_classes.RoleMappingUnionTypeDef]]


# SetPrincipalTagAttributeMapInputTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### UseDefaults
- **Type**: typing.Optional[bool]

### PrincipalTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SetPrincipalTagAttributeMapResponseTypeDef

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### UseDefaults
- **Type**: <class 'bool'>
- **Required**: Yes

### PrincipalTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UnlinkDeveloperIdentityInputTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### DeveloperProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### DeveloperUserIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# UnlinkIdentityInputTypeDef

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### LoginsToRemove
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnprocessedIdentityIdTypeDef

### IdentityId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'InternalServerError']]


# UntagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


