# Pydantic Models in license_manager_linux_subscriptions_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeregisterSubscriptionProviderRequestRequestTypeDef

### SubscriptionProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[typing.Literal['Contains', 'Equal', 'NotEqual']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetRegisteredSubscriptionProviderRequestRequestTypeDef

### SubscriptionProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegisteredSubscriptionProviderResponseTypeDef

### LastSuccessfulDataRetrievalTime
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionProviderSource
- **Type**: typing.Literal['RedHat']
- **Required**: Yes

### SubscriptionProviderStatus
- **Type**: typing.Literal['ACTIVE', 'INVALID', 'PENDING']
- **Required**: Yes

### SubscriptionProviderStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceSettingsResponseTypeDef

### HomeRegions
- **Type**: typing.List[str]
- **Required**: Yes

### LinuxSubscriptionsDiscovery
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### LinuxSubscriptionsDiscoverySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.LinuxSubscriptionsDiscoverySettingsOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Successful']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceTypeDef

### AccountID
- **Type**: typing.Optional[str]

### AmiId
- **Type**: typing.Optional[str]

### DualSubscription
- **Type**: typing.Optional[str]

### InstanceID
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[str]

### OsVersion
- **Type**: typing.Optional[str]

### ProductCode
- **Type**: typing.Optional[typing.List[str]]

### Region
- **Type**: typing.Optional[str]

### RegisteredWithSubscriptionProvider
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubscriptionName
- **Type**: typing.Optional[str]

### SubscriptionProviderCreateTime
- **Type**: typing.Optional[str]

### SubscriptionProviderUpdateTime
- **Type**: typing.Optional[str]

### UsageOperation
- **Type**: typing.Optional[str]


# LinuxSubscriptionsDiscoverySettingsOutputTypeDef

### OrganizationIntegration
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### SourceRegions
- **Type**: typing.List[str]
- **Required**: Yes


# LinuxSubscriptionsDiscoverySettingsTypeDef

### OrganizationIntegration
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### SourceRegions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListLinuxSubscriptionInstancesRequestListLinuxSubscriptionInstancesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.PaginatorConfigTypeDef]


# ListLinuxSubscriptionInstancesRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLinuxSubscriptionInstancesResponseTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLinuxSubscriptionsRequestListLinuxSubscriptionsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.PaginatorConfigTypeDef]


# ListLinuxSubscriptionsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLinuxSubscriptionsResponseTypeDef

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.SubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegisteredSubscriptionProvidersRequestListRegisteredSubscriptionProvidersPaginateTypeDef

### SubscriptionProviderSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['RedHat']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.PaginatorConfigTypeDef]


# ListRegisteredSubscriptionProvidersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SubscriptionProviderSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['RedHat']]]


# ListRegisteredSubscriptionProvidersResponseTypeDef

### RegisteredSubscriptionProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.RegisteredSubscriptionProviderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterSubscriptionProviderRequestRequestTypeDef

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionProviderSource
- **Type**: typing.Literal['RedHat']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterSubscriptionProviderResponseTypeDef

### SubscriptionProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionProviderSource
- **Type**: typing.Literal['RedHat']
- **Required**: Yes

### SubscriptionProviderStatus
- **Type**: typing.Literal['ACTIVE', 'INVALID', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisteredSubscriptionProviderTypeDef

### LastSuccessfulDataRetrievalTime
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SubscriptionProviderArn
- **Type**: typing.Optional[str]

### SubscriptionProviderSource
- **Type**: typing.Optional[typing.Literal['RedHat']]

### SubscriptionProviderStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INVALID', 'PENDING']]

### SubscriptionProviderStatusMessage
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


# SubscriptionTypeDef

### InstanceCount
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateServiceSettingsRequestRequestTypeDef

### LinuxSubscriptionsDiscovery
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### LinuxSubscriptionsDiscoverySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.LinuxSubscriptionsDiscoverySettingsTypeDef'>
- **Required**: Yes

### AllowUpdate
- **Type**: typing.Optional[bool]


# UpdateServiceSettingsResponseTypeDef

### HomeRegions
- **Type**: typing.List[str]
- **Required**: Yes

### LinuxSubscriptionsDiscovery
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### LinuxSubscriptionsDiscoverySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.LinuxSubscriptionsDiscoverySettingsOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Successful']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


