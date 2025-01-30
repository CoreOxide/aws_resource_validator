# license_manager_user_subscriptions_classes

# ActiveDirectoryIdentityProviderTypeDef

### DirectoryId
- **Type**: typing.Optional[str]


# AssociateUserRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]


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

# DeregisterIdentityProviderRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterIdentityProviderResponseTypeDef

### IdentityProviderSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateUserRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]


# DisassociateUserResponseTypeDef

### InstanceUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.InstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilterTypeDef

### Attribute
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# IdentityProviderSummaryTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.SettingsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### FailureMessage
- **Type**: typing.Optional[str]


# IdentityProviderTypeDef

### ActiveDirectoryIdentityProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ActiveDirectoryIdentityProviderTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
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

### StatusMessage
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListIdentityProvidersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersResponseTypeDef

### IdentityProviderSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstancesRequestListInstancesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListInstancesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProductSubscriptionsRequestListProductSubscriptionsPaginateTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListProductSubscriptionsRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListProductSubscriptionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ProductUserSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ProductUserSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserAssociationsRequestListUserAssociationsPaginateTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.PaginatorConfigTypeDef]


# ListUserAssociationsRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProductUserSummaryTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
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

### StatusMessage
- **Type**: typing.Optional[str]

### SubscriptionEndDate
- **Type**: typing.Optional[str]

### SubscriptionStartDate
- **Type**: typing.Optional[str]


# RegisterIdentityProviderRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.SettingsTypeDef]


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


# SettingsTypeDef

### SecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# StartProductSubscriptionRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]


# StartProductSubscriptionResponseTypeDef

### ProductUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ProductUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopProductSubscriptionRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]


# StopProductSubscriptionResponseTypeDef

### ProductUserSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ProductUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdentityProviderSettingsRequestRequestTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.license_manager_user_subscriptions_classes.UpdateSettingsTypeDef'>
- **Required**: Yes


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


