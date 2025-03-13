# License Manager User Subscriptions Classes

# ActiveDirectoryIdentityProviderOutputTypeDef

### ActiveDirectorySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ActiveDirectorySettingsOutputTypeDef]

### ActiveDirectoryType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'SELF_MANAGED']]

### DirectoryId
- **Type**: typing.Optional[str]


# ActiveDirectoryIdentityProviderTypeDef

### ActiveDirectorySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ActiveDirectorySettingsTypeDef]

### ActiveDirectoryType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'SELF_MANAGED']]

### DirectoryId
- **Type**: typing.Optional[str]


# ActiveDirectorySettingsOutputTypeDef

### DomainCredentialsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.CredentialsProviderTypeDef]

### DomainIpv4List
- **Type**: typing.Optional[typing.List[str]]

### DomainName
- **Type**: typing.Optional[str]

### DomainNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.DomainNetworkSettingsOutputTypeDef]


# ActiveDirectorySettingsTypeDef

### DomainCredentialsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.CredentialsProviderTypeDef]

### DomainIpv4List
- **Type**: typing.Optional[typing.Sequence[str]]

### DomainName
- **Type**: typing.Optional[str]

### DomainNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.DomainNetworkSettingsTypeDef]


# AssociateUserRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AssociateUserResponseTypeDef

### InstanceUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.InstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLicenseServerEndpointRequestTypeDef

### IdentityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseServerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.LicenseServerSettingsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLicenseServerEndpointResponseTypeDef

### IdentityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseServerEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialsProviderTypeDef

### SecretsManagerCredentialsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.SecretsManagerCredentialsProviderTypeDef]


# DeleteLicenseServerEndpointRequestTypeDef

### LicenseServerEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerType
- **Type**: typing.Literal['RDS_SAL']
- **Required**: Yes


# DeleteLicenseServerEndpointResponseTypeDef

### LicenseServerEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.LicenseServerEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterIdentityProviderRequestTypeDef

### IdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef]

### IdentityProviderArn
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# DeregisterIdentityProviderResponseTypeDef

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateUserRequestTypeDef

### Domain
- **Type**: typing.Optional[str]

### IdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceUserArn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# DisassociateUserResponseTypeDef

### InstanceUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.InstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainNetworkSettingsOutputTypeDef

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# DomainNetworkSettingsTypeDef

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FilterTypeDef

### Attribute
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# IdentityProviderOutputTypeDef

### ActiveDirectoryIdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ActiveDirectoryIdentityProviderOutputTypeDef]


# IdentityProviderSummaryTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderOutputTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.SettingsOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### FailureMessage
- **Type**: typing.Optional[str]

### IdentityProviderArn
- **Type**: typing.Optional[str]


# IdentityProviderTypeDef

### ActiveDirectoryIdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ActiveDirectoryIdentityProviderTypeDef]


# IdentityProviderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstanceSummaryTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Products
- **Type**: typing.List[str]
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### LastStatusCheckDate
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# InstanceUserSummaryTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderOutputTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationDate
- **Type**: typing.Optional[str]

### DisassociationDate
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### InstanceUserArn
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# LicenseServerEndpointTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### IdentityProviderArn
- **Type**: typing.Optional[str]

### LicenseServerEndpointArn
- **Type**: typing.Optional[str]

### LicenseServerEndpointId
- **Type**: typing.Optional[str]

### LicenseServerEndpointProvisioningStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'DELETION_FAILED', 'PROVISIONED', 'PROVISIONING', 'PROVISIONING_FAILED']]

### LicenseServers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.LicenseServerTypeDef]]

### ServerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ServerEndpointTypeDef]

### ServerType
- **Type**: typing.Optional[typing.Literal['RDS_SAL']]

### StatusMessage
- **Type**: typing.Optional[str]


# LicenseServerSettingsTypeDef

### ServerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ServerSettingsTypeDef'>
- **Required**: Yes

### ServerType
- **Type**: typing.Literal['RDS_SAL']
- **Required**: Yes


# LicenseServerTypeDef

### HealthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'NOT_APPLICABLE', 'UNHEALTHY']]

### Ipv4Address
- **Type**: typing.Optional[str]

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'DELETION_FAILED', 'PROVISIONED', 'PROVISIONING', 'PROVISIONING_FAILED']]


# ListIdentityProvidersRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListIdentityProvidersRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersResponseTypeDef

### IdentityProviderSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListInstancesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesResponseTypeDef

### InstanceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.InstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseServerEndpointsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListLicenseServerEndpointsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseServerEndpointsResponseTypeDef

### LicenseServerEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.LicenseServerEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProductSubscriptionsRequestPaginateTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### Product
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListProductSubscriptionsRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# ListProductSubscriptionsResponseTypeDef

### ProductUserSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ProductUserSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserAssociationsRequestPaginateTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListUserAssociationsRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUserAssociationsResponseTypeDef

### InstanceUserSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.InstanceUserSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductUserSummaryTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderOutputTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### ProductUserArn
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### SubscriptionEndDate
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Optional[str]


# RdsSalSettingsTypeDef

### RdsSalCredentialsProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.CredentialsProviderTypeDef'>
- **Required**: Yes


# RegisterIdentityProviderRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.SettingsUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterIdentityProviderResponseTypeDef

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# SecretsManagerCredentialsProviderTypeDef

### SecretId
- **Type**: typing.Optional[str]


# ServerEndpointTypeDef

### Endpoint
- **Type**: typing.Optional[str]


# ServerSettingsTypeDef

### RdsSalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.RdsSalSettingsTypeDef]


# SettingsOutputTypeDef

### SecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# SettingsTypeDef

### SecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartProductSubscriptionRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartProductSubscriptionResponseTypeDef

### ProductUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ProductUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopProductSubscriptionRequestTypeDef

### Domain
- **Type**: typing.Optional[str]

### IdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef]

### Product
- **Type**: typing.Optional[str]

### ProductUserArn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# StopProductSubscriptionResponseTypeDef

### ProductUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ProductUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIdentityProviderSettingsRequestTypeDef

### UpdateSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.UpdateSettingsTypeDef'>
- **Required**: Yes

### IdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderUnionTypeDef]

### IdentityProviderArn
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# UpdateIdentityProviderSettingsResponseTypeDef

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSettingsTypeDef

### AddSubnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RemoveSubnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupId
- **Type**: typing.Optional[str]


