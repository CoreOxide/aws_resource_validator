# Cognito Identity Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CognitoIdentityProvider

### ProviderName
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### ServerSideTokenCheck
- **Type**: typing.Optional[bool]


# CreateIdentityPoolInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_identity_classes.CognitoIdentityProvider]]

### SamlProviderARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### IdentityPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# Credentials

### AccessKeyId
- **Type**: typing.Optional[str]

### SecretKey
- **Type**: typing.Optional[str]

### SessionToken
- **Type**: typing.Optional[str]

### Expiration
- **Type**: typing.Optional[datetime.datetime]


# DeleteIdentitiesInput

### IdentityIdsToDelete
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteIdentitiesResponse

### UnprocessedIdentityIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.UnprocessedIdentityId]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIdentityPoolInput

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityInput

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityPoolInput

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# GetCredentialsForIdentityInput

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CustomRoleArn
- **Type**: typing.Optional[str]


# GetCredentialsForIdentityResponse

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.Credentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdInput

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### Logins
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetIdResponse

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityPoolRolesInput

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityPoolRolesResponse

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RoleMappings
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.cognito_identity_classes.RoleMappingOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpenIdTokenForDeveloperIdentityInput

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


# GetOpenIdTokenForDeveloperIdentityResponse

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpenIdTokenInput

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetOpenIdTokenResponse

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# GetPrincipalTagAttributeMapInput

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrincipalTagAttributeMapResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityDescription

### IdentityId
- **Type**: typing.Optional[str]

### Logins
- **Type**: typing.Optional[typing.List[str]]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# IdentityDescriptionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityPool

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.CognitoIdentityProvider]
- **Required**: Yes

### SamlProviderARNs
- **Type**: typing.List[str]
- **Required**: Yes

### IdentityPoolTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityPoolRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_identity_classes.CognitoIdentityProvider]]

### SamlProviderARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### IdentityPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# IdentityPoolShortDescription

### IdentityPoolId
- **Type**: typing.Optional[str]

### IdentityPoolName
- **Type**: typing.Optional[str]


# ListIdentitiesInput

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


# ListIdentitiesResponse

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identities
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.IdentityDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoolsInput

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityPoolsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_identity_classes.PaginatorConfig]


# ListIdentityPoolsResponse

### IdentityPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.IdentityPoolShortDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# LookupDeveloperIdentityInput

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


# LookupDeveloperIdentityResponse

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### DeveloperUserIdentifierList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MappingRule

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


# MergeDeveloperIdentitiesInput

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


# MergeDeveloperIdentitiesResponse

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
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


# RoleMappingOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RoleMappingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RulesConfigurationType

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_identity_classes.MappingRule]
- **Required**: Yes


# RulesConfigurationTypeOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_identity_classes.MappingRule]
- **Required**: Yes


# SetIdentityPoolRolesInput

### IdentityPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Roles
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### RoleMappings
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.cognito_identity_classes.RoleMappingUnion]]


# SetPrincipalTagAttributeMapInput

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


# SetPrincipalTagAttributeMapResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_identity_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UnlinkDeveloperIdentityInput

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


# UnlinkIdentityInput

### IdentityId
- **Type**: <class 'str'>
- **Required**: Yes

### Logins
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### LoginsToRemove
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnprocessedIdentityId

### IdentityId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'InternalServerError']]


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


