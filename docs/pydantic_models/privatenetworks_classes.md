# Privatenetworks Classes

# AcknowledgeOrderReceiptRequestTypeDef

### orderArn
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeOrderReceiptResponseTypeDef

### order
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.OrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivateDeviceIdentifierRequestTypeDef

### deviceIdentifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ActivateDeviceIdentifierResponseTypeDef

### deviceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.DeviceIdentifierTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivateNetworkSiteRequestTypeDef

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### shippingAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.AddressTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### commitmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.CommitmentConfigurationTypeDef]


# ActivateNetworkSiteResponseTypeDef

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkSiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddressTypeDef

### city
- **Type**: <class 'str'>
- **Required**: Yes

### country
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### postalCode
- **Type**: <class 'str'>
- **Required**: Yes

### stateOrProvince
- **Type**: <class 'str'>
- **Required**: Yes

### street1
- **Type**: <class 'str'>
- **Required**: Yes

### company
- **Type**: typing.Optional[str]

### emailAddress
- **Type**: typing.Optional[str]

### phoneNumber
- **Type**: typing.Optional[str]

### street2
- **Type**: typing.Optional[str]

### street3
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CommitmentConfigurationTypeDef

### automaticRenewal
- **Type**: <class 'bool'>
- **Required**: Yes

### commitmentLength
- **Type**: typing.Literal['ONE_YEAR', 'SIXTY_DAYS', 'THREE_YEARS']
- **Required**: Yes


# CommitmentInformationTypeDef

### commitmentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.CommitmentConfigurationTypeDef'>
- **Required**: Yes

### expiresOn
- **Type**: typing.Optional[datetime.datetime]

### startAt
- **Type**: typing.Optional[datetime.datetime]


# ConfigureAccessPointRequestTypeDef

### accessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### cpiSecretKey
- **Type**: typing.Optional[str]

### cpiUserId
- **Type**: typing.Optional[str]

### cpiUserPassword
- **Type**: typing.Optional[str]

### cpiUsername
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PositionTypeDef]


# ConfigureAccessPointResponseTypeDef

### accessPoint
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkRequestTypeDef

### networkName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateNetworkResponseTypeDef

### network
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkSiteRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### networkSiteName
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: typing.Optional[str]

### availabilityZoneId
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### pendingPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateNetworkSiteResponseTypeDef

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkSiteTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeactivateDeviceIdentifierRequestTypeDef

### deviceIdentifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeactivateDeviceIdentifierResponseTypeDef

### deviceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.DeviceIdentifierTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNetworkRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteNetworkResponseTypeDef

### network
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNetworkSiteRequestTypeDef

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteNetworkSiteResponseTypeDef

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkSiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceIdentifierTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### deviceIdentifierArn
- **Type**: typing.Optional[str]

### iccid
- **Type**: typing.Optional[str]

### imsi
- **Type**: typing.Optional[str]

### networkArn
- **Type**: typing.Optional[str]

### orderArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### trafficGroupArn
- **Type**: typing.Optional[str]

### vendor
- **Type**: typing.Optional[str]


# GetDeviceIdentifierRequestTypeDef

### deviceIdentifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceIdentifierResponseTypeDef

### deviceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.DeviceIdentifierTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkResourceRequestTypeDef

### networkResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkResourceResponseTypeDef

### networkResource
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkResponseTypeDef

### network
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkSiteRequestTypeDef

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkSiteResponseTypeDef

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkSiteTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrderRequestTypeDef

### orderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrderResponseTypeDef

### order
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.OrderTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeviceIdentifiersRequestPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ORDER', 'STATUS', 'TRAFFIC_GROUP'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListDeviceIdentifiersRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ORDER', 'STATUS', 'TRAFFIC_GROUP'], typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListDeviceIdentifiersResponseTypeDef

### deviceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.DeviceIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkResourcesRequestPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ORDER', 'STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListNetworkResourcesRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ORDER', 'STATUS'], typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListNetworkResourcesResponseTypeDef

### networkResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSitesRequestPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListNetworkSitesRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['STATUS'], typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListNetworkSitesResponseTypeDef

### networkSites
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkSiteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworksRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListNetworksRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['STATUS'], typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListNetworksResponseTypeDef

### networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrdersRequestPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['NETWORK_SITE', 'STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListOrdersRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['NETWORK_SITE', 'STATUS'], typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListOrdersResponseTypeDef

### orders
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.OrderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NameValuePairTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# NetworkResourceDefinitionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkResourceDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkSiteTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### networkSiteName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'DELETED', 'DEPROVISIONING', 'PROVISIONING']
- **Required**: Yes

### availabilityZone
- **Type**: typing.Optional[str]

### availabilityZoneId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### currentPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanOutputTypeDef]

### description
- **Type**: typing.Optional[str]

### pendingPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanOutputTypeDef]

### statusReason
- **Type**: typing.Optional[str]


# NetworkTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### networkName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'DELETED', 'DEPROVISIONING', 'PROVISIONING']
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]


# OrderTypeDef

### acknowledgmentStatus
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGED', 'ACKNOWLEDGING', 'UNACKNOWLEDGED']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### networkArn
- **Type**: typing.Optional[str]

### networkSiteArn
- **Type**: typing.Optional[str]

### orderArn
- **Type**: typing.Optional[str]

### orderedResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.OrderedResourceDefinitionTypeDef]]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.AddressTypeDef]

### trackingInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.TrackingInformationTypeDef]]


# OrderedResourceDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PingResponseTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PositionTypeDef

### elevation
- **Type**: typing.Optional[float]

### elevationReference
- **Type**: typing.Optional[typing.Literal['AGL', 'AMSL']]

### elevationUnit
- **Type**: typing.Optional[typing.Literal['FEET']]

### latitude
- **Type**: typing.Optional[float]

### longitude
- **Type**: typing.Optional[float]


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


# ReturnInformationTypeDef

### replacementOrderArn
- **Type**: typing.Optional[str]

### returnReason
- **Type**: typing.Optional[str]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.AddressTypeDef]

### shippingLabel
- **Type**: typing.Optional[str]


# SitePlanOutputTypeDef

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NameValuePairTypeDef]]

### resourceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceDefinitionOutputTypeDef]]


# SitePlanTypeDef

### options
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.privatenetworks_classes.NameValuePairTypeDef]]

### resourceDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceDefinitionTypeDef]]


# SitePlanUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartNetworkResourceUpdateRequestTypeDef

### networkResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateType
- **Type**: typing.Literal['COMMITMENT', 'REPLACE', 'RETURN']
- **Required**: Yes

### commitmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.CommitmentConfigurationTypeDef]

### returnReason
- **Type**: typing.Optional[str]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.AddressTypeDef]


# StartNetworkResourceUpdateResponseTypeDef

### networkResource
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TrackingInformationTypeDef

### trackingNumber
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateNetworkSitePlanRequestTypeDef

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### pendingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateNetworkSiteRequestTypeDef

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateNetworkSiteResponseTypeDef

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkSiteTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


