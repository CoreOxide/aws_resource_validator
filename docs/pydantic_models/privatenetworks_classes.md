# Pydantic Models in privatenetworks_classes

# AcknowledgeOrderReceiptRequestRequestTypeDef

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


# ActivateDeviceIdentifierRequestRequestTypeDef

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


# ActivateNetworkSiteRequestRequestTypeDef

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


# ConfigureAccessPointRequestRequestTypeDef

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


# CreateNetworkRequestRequestTypeDef

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


# CreateNetworkSiteRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanTypeDef]

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


# DeactivateDeviceIdentifierRequestRequestTypeDef

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


# DeleteNetworkRequestRequestTypeDef

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


# DeleteNetworkSiteRequestRequestTypeDef

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


# GetDeviceIdentifierRequestRequestTypeDef

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


# GetNetworkRequestRequestTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkResourceRequestRequestTypeDef

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


# GetNetworkSiteRequestRequestTypeDef

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


# GetOrderRequestRequestTypeDef

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


# ListDeviceIdentifiersRequestListDeviceIdentifiersPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ORDER', 'STATUS', 'TRAFFIC_GROUP'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListDeviceIdentifiersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNetworkResourcesRequestListNetworkResourcesPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ORDER', 'STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListNetworkResourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNetworkSitesRequestListNetworkSitesPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListNetworkSitesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNetworksRequestListNetworksPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListNetworksRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrdersRequestListOrdersPaginateTypeDef

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['NETWORK_SITE', 'STATUS'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PaginatorConfigTypeDef]


# ListOrdersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### orders
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.OrderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# NetworkResourceDefinitionTypeDef

### count
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DEVICE_IDENTIFIER', 'RADIO_UNIT']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NameValuePairTypeDef]]


# NetworkResourceTypeDef

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NameValuePairTypeDef]]

### commitmentInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.CommitmentInformationTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'INITIAL', 'UNHEALTHY']]

### model
- **Type**: typing.Optional[str]

### networkArn
- **Type**: typing.Optional[str]

### networkResourceArn
- **Type**: typing.Optional[str]

### networkSiteArn
- **Type**: typing.Optional[str]

### orderArn
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.PositionTypeDef]

### returnInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.ReturnInformationTypeDef]

### serialNumber
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING_SHIPPING_LABEL', 'DELETED', 'DELETING', 'PENDING', 'PENDING_RETURN', 'PROVISIONED', 'PROVISIONING', 'SHIPPED']]

### statusReason
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['RADIO_UNIT']]

### vendor
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanTypeDef]

### description
- **Type**: typing.Optional[str]

### pendingPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanTypeDef]

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

### count
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DEVICE_IDENTIFIER', 'RADIO_UNIT']
- **Required**: Yes

### commitmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.CommitmentConfigurationTypeDef]


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


# ReturnInformationTypeDef

### replacementOrderArn
- **Type**: typing.Optional[str]

### returnReason
- **Type**: typing.Optional[str]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks_classes.AddressTypeDef]

### shippingLabel
- **Type**: typing.Optional[str]


# SitePlanTypeDef

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NameValuePairTypeDef]]

### resourceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks_classes.NetworkResourceDefinitionTypeDef]]


# StartNetworkResourceUpdateRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TrackingInformationTypeDef

### trackingNumber
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateNetworkSitePlanRequestRequestTypeDef

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### pendingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks_classes.SitePlanTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateNetworkSiteRequestRequestTypeDef

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


