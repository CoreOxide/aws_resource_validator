# Privatenetworks Privatenetworks Classes

# AcknowledgeOrderReceiptRequest

### orderArn
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeOrderReceiptResponse

### order
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Order'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# ActivateDeviceIdentifierRequest

### deviceIdentifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ActivateDeviceIdentifierResponse

### deviceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.DeviceIdentifier'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# ActivateNetworkSiteRequest

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### shippingAddress
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Address'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### commitmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.CommitmentConfiguration]


# ActivateNetworkSiteResponse

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkSite'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# Address

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

# CommitmentConfiguration

### automaticRenewal
- **Type**: <class 'bool'>
- **Required**: Yes

### commitmentLength
- **Type**: typing.Literal['ONE_YEAR', 'SIXTY_DAYS', 'THREE_YEARS']
- **Required**: Yes


# CommitmentInformation

### commitmentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.CommitmentConfiguration'>
- **Required**: Yes

### expiresOn
- **Type**: typing.Optional[datetime.datetime]

### startAt
- **Type**: typing.Optional[datetime.datetime]


# ConfigureAccessPointRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Position]


# ConfigureAccessPointResponse

### accessPoint
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkRequest

### networkName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNetworkResponse

### network
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Network'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkSiteRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.SitePlan, aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.SitePlanOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNetworkSiteResponse

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkSite'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# DeactivateDeviceIdentifierRequest

### deviceIdentifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeactivateDeviceIdentifierResponse

### deviceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.DeviceIdentifier'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNetworkRequest

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteNetworkResponse

### network
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Network'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNetworkSiteRequest

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteNetworkSiteResponse

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkSite'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceIdentifier

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


# GetDeviceIdentifierRequest

### deviceIdentifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceIdentifierResponse

### deviceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.DeviceIdentifier'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkRequest

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkResourceRequest

### networkResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkResourceResponse

### networkResource
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkResource'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkResponse

### network
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Network'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkSiteRequest

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkSiteResponse

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkSite'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# GetOrderRequest

### orderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrderResponse

### order
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Order'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# ListDeviceIdentifiersRequest

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['ORDER', 'STATUS', 'TRAFFIC_GROUP'], typing.List[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListDeviceIdentifiersRequestPaginate

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['ORDER', 'STATUS', 'TRAFFIC_GROUP'], typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.PaginatorConfig]


# ListDeviceIdentifiersResponse

### deviceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.DeviceIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkResourcesRequest

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['ORDER', 'STATUS'], typing.List[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListNetworkResourcesRequestPaginate

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['ORDER', 'STATUS'], typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.PaginatorConfig]


# ListNetworkResourcesResponse

### networkResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSitesRequest

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['STATUS'], typing.List[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListNetworkSitesRequestPaginate

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['STATUS'], typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.PaginatorConfig]


# ListNetworkSitesResponse

### networkSites
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkSite]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworksRequest

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['STATUS'], typing.List[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListNetworksRequestPaginate

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['STATUS'], typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.PaginatorConfig]


# ListNetworksResponse

### networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Network]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrdersRequest

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['NETWORK_SITE', 'STATUS'], typing.List[str]]]

### maxResults
- **Type**: typing.Optional[int]

### startToken
- **Type**: typing.Optional[str]


# ListOrdersRequestPaginate

### networkArn
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Dict[typing.Literal['NETWORK_SITE', 'STATUS'], typing.List[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.PaginatorConfig]


# ListOrdersResponse

### orders
- **Type**: typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Order]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# NameValuePair

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# Network

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


# NetworkResource

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NameValuePair]]

### commitmentInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.CommitmentInformation]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Position]

### returnInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ReturnInformation]

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


# NetworkResourceDefinition

### count
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DEVICE_IDENTIFIER', 'RADIO_UNIT']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NameValuePair]]


# NetworkResourceDefinitionOutput

### count
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DEVICE_IDENTIFIER', 'RADIO_UNIT']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NameValuePair]]


# NetworkSite

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.SitePlanOutput]

### description
- **Type**: typing.Optional[str]

### pendingPlan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.SitePlanOutput]

### statusReason
- **Type**: typing.Optional[str]


# Order

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.OrderedResourceDefinition]]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Address]

### trackingInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.TrackingInformation]]


# OrderedResourceDefinition

### count
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DEVICE_IDENTIFIER', 'RADIO_UNIT']
- **Required**: Yes

### commitmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.CommitmentConfiguration]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PingResponse

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# Position

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


# ReturnInformation

### replacementOrderArn
- **Type**: typing.Optional[str]

### returnReason
- **Type**: typing.Optional[str]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Address]

### shippingLabel
- **Type**: typing.Optional[str]


# SitePlan

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NameValuePair]]

### resourceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkResourceDefinition]]


# SitePlanOutput

### options
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NameValuePair]]

### resourceDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkResourceDefinitionOutput]]


# StartNetworkResourceUpdateRequest

### networkResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateType
- **Type**: typing.Literal['COMMITMENT', 'REPLACE', 'RETURN']
- **Required**: Yes

### commitmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.CommitmentConfiguration]

### returnReason
- **Type**: typing.Optional[str]

### shippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.Address]


# StartNetworkResourceUpdateResponse

### networkResource
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TrackingInformation

### trackingNumber
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateNetworkSitePlanRequest

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### pendingPlan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.SitePlan, aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.SitePlanOutput]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateNetworkSiteRequest

### networkSiteArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateNetworkSiteResponse

### networkSite
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.NetworkSite'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.privatenetworks.privatenetworks_classes.ResponseMetadata'>
- **Required**: Yes


