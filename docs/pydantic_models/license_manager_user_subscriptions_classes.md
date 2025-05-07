# License Manager User Subscriptions Classes

# ActiveDirectoryIdentityProvider

### ActiveDirectorySettings
- **Type**: <class 'NoneType'>

### ActiveDirectoryType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'SELF_MANAGED']]

### DirectoryId
- **Type**: typing.Optional[str]


# ActiveDirectoryIdentityProviderOutput

### ActiveDirectorySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ActiveDirectorySettingsOutput]

### ActiveDirectoryType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'SELF_MANAGED']]

### DirectoryId
- **Type**: typing.Optional[str]


# ActiveDirectorySettings

### DomainCredentialsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.CredentialsProvider]

### DomainIpv4List
- **Type**: typing.Optional[typing.List[str]]

### DomainName
- **Type**: typing.Optional[str]

### DomainNetworkSettings
- **Type**: <class 'NoneType'>


# ActiveDirectorySettingsOutput

### DomainCredentialsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.CredentialsProvider]

### DomainIpv4List
- **Type**: typing.Optional[typing.List[str]]

### DomainName
- **Type**: typing.Optional[str]

### DomainNetworkSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.DomainNetworkSettingsOutput]


# AssociateUserRequest

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssociateUserResponse

### InstanceUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.InstanceUserSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLicenseServerEndpointRequest

### IdentityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseServerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.LicenseServerSettings'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLicenseServerEndpointResponse

### IdentityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseServerEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# CredentialsProvider

### SecretsManagerCredentialsProvider
- **Type**: <class 'NoneType'>


# DeleteLicenseServerEndpointRequest

### LicenseServerEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerType
- **Type**: typing.Literal['RDS_SAL']
- **Required**: Yes


# DeleteLicenseServerEndpointResponse

### LicenseServerEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.LicenseServerEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterIdentityProviderRequest

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput, NoneType]

### IdentityProviderArn
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# DeregisterIdentityProviderResponse

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateUserRequest

### Domain
- **Type**: typing.Optional[str]

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput, NoneType]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceUserArn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# DisassociateUserResponse

### InstanceUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.InstanceUserSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# DomainNetworkSettings

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# DomainNetworkSettingsOutput

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# Filter

### Attribute
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# IdentityProvider

### ActiveDirectoryIdentityProvider
- **Type**: <class 'NoneType'>


# IdentityProviderOutput

### ActiveDirectoryIdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ActiveDirectoryIdentityProviderOutput]


# IdentityProviderSummary

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.SettingsOutput'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### FailureMessage
- **Type**: typing.Optional[str]

### IdentityProviderArn
- **Type**: typing.Optional[str]


# InstanceSummary

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


# InstanceUserSummary

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput'>
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


# LicenseServer

### HealthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'NOT_APPLICABLE', 'UNHEALTHY']]

### Ipv4Address
- **Type**: typing.Optional[str]

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'DELETION_FAILED', 'PROVISIONED', 'PROVISIONING', 'PROVISIONING_FAILED']]


# LicenseServerEndpoint

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.LicenseServer]]

### ServerEndpoint
- **Type**: <class 'NoneType'>

### ServerType
- **Type**: typing.Optional[typing.Literal['RDS_SAL']]

### StatusMessage
- **Type**: typing.Optional[str]


# LicenseServerSettings

### ServerSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ServerSettings'>
- **Required**: Yes

### ServerType
- **Type**: typing.Literal['RDS_SAL']
- **Required**: Yes


# ListIdentityProvidersRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.PaginatorConfig]


# ListIdentityProvidersResponse

### IdentityProviderSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.PaginatorConfig]


# ListInstancesResponse

### InstanceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.InstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseServerEndpointsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLicenseServerEndpointsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.PaginatorConfig]


# ListLicenseServerEndpointsResponse

### LicenseServerEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.LicenseServerEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProductSubscriptionsRequest

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# ListProductSubscriptionsRequestPaginate

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### Product
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.PaginatorConfig]


# ListProductSubscriptionsResponse

### ProductUserSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ProductUserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# ListUserAssociationsRequest

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUserAssociationsRequestPaginate

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.PaginatorConfig]


# ListUserAssociationsResponse

### InstanceUserSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.InstanceUserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductUserSummary

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput'>
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


# RdsSalSettings

### RdsSalCredentialsProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.CredentialsProvider'>
- **Required**: Yes


# RegisterIdentityProviderRequest

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.Settings, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.SettingsOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RegisterIdentityProviderResponse

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


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


# SecretsManagerCredentialsProvider

### SecretId
- **Type**: typing.Optional[str]


# ServerEndpoint

### Endpoint
- **Type**: typing.Optional[str]


# ServerSettings

### RdsSalSettings
- **Type**: <class 'NoneType'>


# Settings

### SecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# SettingsOutput

### SecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# StartProductSubscriptionRequest

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartProductSubscriptionResponse

### ProductUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ProductUserSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# StopProductSubscriptionRequest

### Domain
- **Type**: typing.Optional[str]

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput, NoneType]

### Product
- **Type**: typing.Optional[str]

### ProductUserArn
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# StopProductSubscriptionResponse

### ProductUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ProductUserSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateIdentityProviderSettingsRequest

### UpdateSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.UpdateSettings'>
- **Required**: Yes

### IdentityProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProvider, aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderOutput, NoneType]

### IdentityProviderArn
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]


# UpdateIdentityProviderSettingsResponse

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.IdentityProviderSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions.license_manager_user_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSettings

### AddSubnets
- **Type**: typing.List[str]
- **Required**: Yes

### RemoveSubnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupId
- **Type**: typing.Optional[str]


