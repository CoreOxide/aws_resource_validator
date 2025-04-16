# License Manager Linux Subscriptions Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeregisterSubscriptionProviderRequest

### SubscriptionProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# Filter

### Name
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[typing.Literal['Contains', 'Equal', 'NotEqual']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetRegisteredSubscriptionProviderRequest

### SubscriptionProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegisteredSubscriptionProviderResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceSettingsResponse

### HomeRegions
- **Type**: typing.List[str]
- **Required**: Yes

### LinuxSubscriptionsDiscovery
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### LinuxSubscriptionsDiscoverySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.LinuxSubscriptionsDiscoverySettingsOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Successful']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# Instance

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


# LinuxSubscriptionsDiscoverySettings

### OrganizationIntegration
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### SourceRegions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# LinuxSubscriptionsDiscoverySettingsOutput

### OrganizationIntegration
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### SourceRegions
- **Type**: typing.List[str]
- **Required**: Yes


# LinuxSubscriptionsDiscoverySettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListLinuxSubscriptionInstancesRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLinuxSubscriptionInstancesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.PaginatorConfig]


# ListLinuxSubscriptionInstancesResponse

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLinuxSubscriptionsRequest

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLinuxSubscriptionsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.PaginatorConfig]


# ListLinuxSubscriptionsResponse

### Subscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.Subscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRegisteredSubscriptionProvidersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SubscriptionProviderSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['RedHat']]]


# ListRegisteredSubscriptionProvidersRequestPaginate

### SubscriptionProviderSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['RedHat']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.PaginatorConfig]


# ListRegisteredSubscriptionProvidersResponse

### RegisteredSubscriptionProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.RegisteredSubscriptionProvider]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterSubscriptionProviderRequest

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubscriptionProviderSource
- **Type**: typing.Literal['RedHat']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RegisterSubscriptionProviderResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


# RegisteredSubscriptionProvider

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


# Subscription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateServiceSettingsRequest

### LinuxSubscriptionsDiscovery
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### LinuxSubscriptionsDiscoverySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.LinuxSubscriptionsDiscoverySettingsUnion'>
- **Required**: Yes

### AllowUpdate
- **Type**: typing.Optional[bool]


# UpdateServiceSettingsResponse

### HomeRegions
- **Type**: typing.List[str]
- **Required**: Yes

### LinuxSubscriptionsDiscovery
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### LinuxSubscriptionsDiscoverySettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.LinuxSubscriptionsDiscoverySettingsOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Successful']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_linux_subscriptions_classes.ResponseMetadata'>
- **Required**: Yes


