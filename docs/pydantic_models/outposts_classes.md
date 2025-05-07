# Outposts Classes

# Address

### AddressLine1
- **Type**: <class 'str'>
- **Required**: Yes

### City
- **Type**: <class 'str'>
- **Required**: Yes

### StateOrRegion
- **Type**: <class 'str'>
- **Required**: Yes

### PostalCode
- **Type**: <class 'str'>
- **Required**: Yes

### CountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### ContactName
- **Type**: typing.Optional[str]

### ContactPhoneNumber
- **Type**: typing.Optional[str]

### AddressLine2
- **Type**: typing.Optional[str]

### AddressLine3
- **Type**: typing.Optional[str]

### DistrictOrCounty
- **Type**: typing.Optional[str]

### Municipality
- **Type**: typing.Optional[str]


# AssetInfo

### AssetId
- **Type**: typing.Optional[str]

### RackId
- **Type**: typing.Optional[str]

### AssetType
- **Type**: typing.Optional[typing.Literal['COMPUTE']]

### ComputeAttributes
- **Type**: <class 'NoneType'>

### AssetLocation
- **Type**: <class 'NoneType'>


# AssetInstance

### InstanceId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### AssetId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AwsServiceName
- **Type**: typing.Optional[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]


# AssetInstanceTypeCapacity

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# AssetLocation

### RackElevation
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockingInstance

### InstanceId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AwsServiceName
- **Type**: typing.Optional[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]


# CancelCapacityTaskInput

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelOrderInput

### OrderId
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityTaskFailure

### Reason
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['BLOCKING_INSTANCES_NOT_EVACUATED', 'INTERNAL_SERVER_ERROR', 'RESOURCE_NOT_FOUND', 'UNEXPECTED_ASSET_STATE', 'UNSUPPORTED_CAPACITY_CONFIGURATION']]


# CapacityTaskSummary

### CapacityTaskId
- **Type**: typing.Optional[str]

### OutpostId
- **Type**: typing.Optional[str]

### OrderId
- **Type**: typing.Optional[str]

### CapacityTaskStatus
- **Type**: typing.Optional[typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CompletionDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# CatalogItem

### CatalogItemId
- **Type**: typing.Optional[str]

### ItemStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DISCONTINUED']]

### EC2Capacities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.EC2Capacity]]

### PowerKva
- **Type**: typing.Optional[float]

### WeightLbs
- **Type**: typing.Optional[int]

### SupportedUplinkGbps
- **Type**: typing.Optional[typing.List[int]]

### SupportedStorage
- **Type**: typing.Optional[typing.List[typing.Literal['EBS', 'S3']]]


# ComputeAttributes

### HostId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ISOLATED', 'RETIRING']]

### InstanceFamilies
- **Type**: typing.Optional[typing.List[str]]

### InstanceTypeCapacities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.AssetInstanceTypeCapacity]]

### MaxVcpus
- **Type**: typing.Optional[int]


# ConnectionDetails

### ClientPublicKey
- **Type**: typing.Optional[str]

### ServerPublicKey
- **Type**: typing.Optional[str]

### ServerEndpoint
- **Type**: typing.Optional[str]

### ClientTunnelAddress
- **Type**: typing.Optional[str]

### ServerTunnelAddress
- **Type**: typing.Optional[str]

### AllowedIps
- **Type**: typing.Optional[typing.List[str]]


# CreateOrderInput

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LineItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.LineItemRequest]
- **Required**: Yes

### PaymentOption
- **Type**: typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']
- **Required**: Yes

### PaymentTerm
- **Type**: typing.Optional[typing.Literal['FIVE_YEARS', 'ONE_YEAR', 'THREE_YEARS']]


# CreateOrderOutput

### Order
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Order'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOutpostInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### SupportedHardwareType
- **Type**: typing.Optional[typing.Literal['RACK', 'SERVER']]


# CreateOutpostOutput

### Outpost
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Outpost'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSiteInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### OperatingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.Address]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.Address]

### RackPhysicalProperties
- **Type**: <class 'NoneType'>


# CreateSiteOutput

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOutpostInput

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteInput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes


# EC2Capacity

### Family
- **Type**: typing.Optional[str]

### MaxSize
- **Type**: typing.Optional[str]

### Quantity
- **Type**: typing.Optional[str]


# GetCapacityTaskInput

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapacityTaskOutput

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### OrderId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedInstancePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.InstanceTypeCapacity]
- **Required**: Yes

### InstancesToExclude
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.InstancesToExcludeOutput'>
- **Required**: Yes

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### CapacityTaskStatus
- **Type**: typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']
- **Required**: Yes

### Failed
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.CapacityTaskFailure'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskActionOnBlockingInstances
- **Type**: typing.Literal['FAIL_TASK', 'WAIT_FOR_EVACUATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# GetCatalogItemInput

### CatalogItemId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCatalogItemOutput

### CatalogItem
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.CatalogItem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionResponse

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ConnectionDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# GetOrderInput

### OrderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrderOutput

### Order
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Order'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# GetOutpostInput

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOutpostInstanceTypesInput

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetOutpostInstanceTypesInputPaginate

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# GetOutpostInstanceTypesOutput

### InstanceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.InstanceTypeItem]
- **Required**: Yes

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOutpostOutput

### Outpost
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Outpost'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# GetOutpostSupportedInstanceTypesInput

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OrderId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOutpostSupportedInstanceTypesInputPaginate

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OrderId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# GetOutpostSupportedInstanceTypesOutput

### InstanceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.InstanceTypeItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSiteAddressInput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes


# GetSiteAddressOutput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Address'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# GetSiteInput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSiteOutput

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceTypeCapacity

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# InstanceTypeItem

### InstanceType
- **Type**: typing.Optional[str]

### VCPUs
- **Type**: typing.Optional[int]


# InstancesToExclude

### Instances
- **Type**: typing.Optional[typing.List[str]]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### Services
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]


# InstancesToExcludeOutput

### Instances
- **Type**: typing.Optional[typing.List[str]]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### Services
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]


# LineItem

### CatalogItemId
- **Type**: typing.Optional[str]

### LineItemId
- **Type**: typing.Optional[str]

### Quantity
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['BUILDING', 'CANCELLED', 'DELIVERED', 'ERROR', 'INSTALLED', 'INSTALLING', 'PREPARING', 'REPLACED', 'SHIPPED']]

### ShipmentInformation
- **Type**: <class 'NoneType'>

### AssetInformationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.LineItemAssetInformation]]

### PreviousLineItemId
- **Type**: typing.Optional[str]

### PreviousOrderId
- **Type**: typing.Optional[str]


# LineItemAssetInformation

### AssetId
- **Type**: typing.Optional[str]

### MacAddressList
- **Type**: typing.Optional[typing.List[str]]


# LineItemRequest

### CatalogItemId
- **Type**: typing.Optional[str]

### Quantity
- **Type**: typing.Optional[int]


# ListAssetInstancesInput

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AssetIdFilter
- **Type**: typing.Optional[typing.List[str]]

### InstanceTypeFilter
- **Type**: typing.Optional[typing.List[str]]

### AccountIdFilter
- **Type**: typing.Optional[typing.List[str]]

### AwsServiceFilter
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssetInstancesInputPaginate

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AssetIdFilter
- **Type**: typing.Optional[typing.List[str]]

### InstanceTypeFilter
- **Type**: typing.Optional[typing.List[str]]

### AccountIdFilter
- **Type**: typing.Optional[typing.List[str]]

### AwsServiceFilter
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListAssetInstancesOutput

### AssetInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.AssetInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssetsInput

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### HostIdFilter
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'ISOLATED', 'RETIRING']]]


# ListAssetsInputPaginate

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### HostIdFilter
- **Type**: typing.Optional[typing.List[str]]

### StatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'ISOLATED', 'RETIRING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListAssetsOutput

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.AssetInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBlockingInstancesForCapacityTaskInput

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBlockingInstancesForCapacityTaskInputPaginate

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListBlockingInstancesForCapacityTaskOutput

### BlockingInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.BlockingInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCapacityTasksInput

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### CapacityTaskStatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']]]


# ListCapacityTasksInputPaginate

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### CapacityTaskStatusFilter
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListCapacityTasksOutput

### CapacityTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.CapacityTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCatalogItemsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ItemClassFilter
- **Type**: typing.Optional[typing.List[typing.Literal['RACK', 'SERVER']]]

### SupportedStorageFilter
- **Type**: typing.Optional[typing.List[typing.Literal['EBS', 'S3']]]

### EC2FamilyFilter
- **Type**: typing.Optional[typing.List[str]]


# ListCatalogItemsInputPaginate

### ItemClassFilter
- **Type**: typing.Optional[typing.List[typing.Literal['RACK', 'SERVER']]]

### SupportedStorageFilter
- **Type**: typing.Optional[typing.List[typing.Literal['EBS', 'S3']]]

### EC2FamilyFilter
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListCatalogItemsOutput

### CatalogItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.CatalogItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrdersInput

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrdersInputPaginate

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListOrdersOutput

### Orders
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.OrderSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LifeCycleStatusFilter
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZoneFilter
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZoneIdFilter
- **Type**: typing.Optional[typing.List[str]]


# ListOutpostsInputPaginate

### LifeCycleStatusFilter
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZoneFilter
- **Type**: typing.Optional[typing.List[str]]

### AvailabilityZoneIdFilter
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListOutpostsOutput

### Outposts
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.Outpost]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSitesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### OperatingAddressCountryCodeFilter
- **Type**: typing.Optional[typing.List[str]]

### OperatingAddressStateOrRegionFilter
- **Type**: typing.Optional[typing.List[str]]

### OperatingAddressCityFilter
- **Type**: typing.Optional[typing.List[str]]


# ListSitesInputPaginate

### OperatingAddressCountryCodeFilter
- **Type**: typing.Optional[typing.List[str]]

### OperatingAddressStateOrRegionFilter
- **Type**: typing.Optional[typing.List[str]]

### OperatingAddressCityFilter
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts.outposts_classes.PaginatorConfig]


# ListSitesOutput

### Sites
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.Site]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# Order

### OutpostId
- **Type**: typing.Optional[str]

### OrderId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELIVERED', 'ERROR', 'FULFILLED', 'INSTALLING', 'IN_PROGRESS', 'PENDING', 'PREPARING', 'PROCESSING', 'RECEIVED']]

### LineItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.LineItem]]

### PaymentOption
- **Type**: typing.Optional[typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']]

### OrderSubmissionDate
- **Type**: typing.Optional[datetime.datetime]

### OrderFulfilledDate
- **Type**: typing.Optional[datetime.datetime]

### PaymentTerm
- **Type**: typing.Optional[typing.Literal['FIVE_YEARS', 'ONE_YEAR', 'THREE_YEARS']]

### OrderType
- **Type**: typing.Optional[typing.Literal['OUTPOST', 'REPLACEMENT']]


# OrderSummary

### OutpostId
- **Type**: typing.Optional[str]

### OrderId
- **Type**: typing.Optional[str]

### OrderType
- **Type**: typing.Optional[typing.Literal['OUTPOST', 'REPLACEMENT']]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELIVERED', 'ERROR', 'FULFILLED', 'INSTALLING', 'IN_PROGRESS', 'PENDING', 'PREPARING', 'PROCESSING', 'RECEIVED']]

### LineItemCountsByStatus
- **Type**: typing.Optional[typing.Dict[typing.Literal['BUILDING', 'CANCELLED', 'DELIVERED', 'ERROR', 'INSTALLED', 'INSTALLING', 'PREPARING', 'REPLACED', 'SHIPPED'], int]]

### OrderSubmissionDate
- **Type**: typing.Optional[datetime.datetime]

### OrderFulfilledDate
- **Type**: typing.Optional[datetime.datetime]


# Outpost

### OutpostId
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### SiteId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LifeCycleStatus
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### SiteArn
- **Type**: typing.Optional[str]

### SupportedHardwareType
- **Type**: typing.Optional[typing.Literal['RACK', 'SERVER']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RackPhysicalProperties

### PowerDrawKva
- **Type**: typing.Optional[typing.Literal['POWER_10_KVA', 'POWER_15_KVA', 'POWER_30_KVA', 'POWER_5_KVA']]

### PowerPhase
- **Type**: typing.Optional[typing.Literal['SINGLE_PHASE', 'THREE_PHASE']]

### PowerConnector
- **Type**: typing.Optional[typing.Literal['AH530P7W', 'AH532P6W', 'CS8365C', 'IEC309', 'L6_30P']]

### PowerFeedDrop
- **Type**: typing.Optional[typing.Literal['ABOVE_RACK', 'BELOW_RACK']]

### UplinkGbps
- **Type**: typing.Optional[typing.Literal['UPLINK_100G', 'UPLINK_10G', 'UPLINK_1G', 'UPLINK_40G']]

### UplinkCount
- **Type**: typing.Optional[typing.Literal['UPLINK_COUNT_1', 'UPLINK_COUNT_12', 'UPLINK_COUNT_16', 'UPLINK_COUNT_2', 'UPLINK_COUNT_3', 'UPLINK_COUNT_4', 'UPLINK_COUNT_5', 'UPLINK_COUNT_6', 'UPLINK_COUNT_7', 'UPLINK_COUNT_8']]

### FiberOpticCableType
- **Type**: typing.Optional[typing.Literal['MULTI_MODE', 'SINGLE_MODE']]

### OpticalStandard
- **Type**: typing.Optional[typing.Literal['OPTIC_1000BASE_LX', 'OPTIC_1000BASE_SX', 'OPTIC_100GBASE_CWDM4', 'OPTIC_100GBASE_LR4', 'OPTIC_100GBASE_SR4', 'OPTIC_100G_PSM4_MSA', 'OPTIC_10GBASE_IR', 'OPTIC_10GBASE_LR', 'OPTIC_10GBASE_SR', 'OPTIC_40GBASE_ESR', 'OPTIC_40GBASE_IR4_LR4L', 'OPTIC_40GBASE_LR4', 'OPTIC_40GBASE_SR']]

### MaximumSupportedWeightLbs
- **Type**: typing.Optional[typing.Literal['MAX_1400_LBS', 'MAX_1600_LBS', 'MAX_1800_LBS', 'MAX_2000_LBS', 'NO_LIMIT']]


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


# ShipmentInformation

### ShipmentTrackingNumber
- **Type**: typing.Optional[str]

### ShipmentCarrier
- **Type**: typing.Optional[typing.Literal['DBS', 'DHL', 'EXPEDITORS', 'FEDEX', 'UPS']]


# Site

### SiteId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### SiteArn
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### OperatingAddressCountryCode
- **Type**: typing.Optional[str]

### OperatingAddressStateOrRegion
- **Type**: typing.Optional[str]

### OperatingAddressCity
- **Type**: typing.Optional[str]

### RackPhysicalProperties
- **Type**: <class 'NoneType'>


# StartCapacityTaskInput

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### InstancePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.InstanceTypeCapacity]
- **Required**: Yes

### OrderId
- **Type**: typing.Optional[str]

### InstancesToExclude
- **Type**: typing.Union[aws_resource_validator.pydantic_models.outposts.outposts_classes.InstancesToExclude, aws_resource_validator.pydantic_models.outposts.outposts_classes.InstancesToExcludeOutput, NoneType]

### DryRun
- **Type**: typing.Optional[bool]

### TaskActionOnBlockingInstances
- **Type**: typing.Optional[typing.Literal['FAIL_TASK', 'WAIT_FOR_EVACUATION']]


# StartCapacityTaskOutput

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### OrderId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedInstancePools
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts.outposts_classes.InstanceTypeCapacity]
- **Required**: Yes

### InstancesToExclude
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.InstancesToExcludeOutput'>
- **Required**: Yes

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### CapacityTaskStatus
- **Type**: typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']
- **Required**: Yes

### Failed
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.CapacityTaskFailure'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TaskActionOnBlockingInstances
- **Type**: typing.Literal['FAIL_TASK', 'WAIT_FOR_EVACUATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# StartConnectionRequest

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceDeviceIndex
- **Type**: <class 'int'>
- **Required**: Yes

### DeviceSerialNumber
- **Type**: typing.Optional[str]


# StartConnectionResponse

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UnderlayIpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
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


# UpdateOutpostInput

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SupportedHardwareType
- **Type**: typing.Optional[typing.Literal['RACK', 'SERVER']]


# UpdateOutpostOutput

### Outpost
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Outpost'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSiteAddressInput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Address'>
- **Required**: Yes


# UpdateSiteAddressOutput

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Address'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSiteInput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]


# UpdateSiteOutput

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSiteRackPhysicalPropertiesInput

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### PowerDrawKva
- **Type**: typing.Optional[typing.Literal['POWER_10_KVA', 'POWER_15_KVA', 'POWER_30_KVA', 'POWER_5_KVA']]

### PowerPhase
- **Type**: typing.Optional[typing.Literal['SINGLE_PHASE', 'THREE_PHASE']]

### PowerConnector
- **Type**: typing.Optional[typing.Literal['AH530P7W', 'AH532P6W', 'CS8365C', 'IEC309', 'L6_30P']]

### PowerFeedDrop
- **Type**: typing.Optional[typing.Literal['ABOVE_RACK', 'BELOW_RACK']]

### UplinkGbps
- **Type**: typing.Optional[typing.Literal['UPLINK_100G', 'UPLINK_10G', 'UPLINK_1G', 'UPLINK_40G']]

### UplinkCount
- **Type**: typing.Optional[typing.Literal['UPLINK_COUNT_1', 'UPLINK_COUNT_12', 'UPLINK_COUNT_16', 'UPLINK_COUNT_2', 'UPLINK_COUNT_3', 'UPLINK_COUNT_4', 'UPLINK_COUNT_5', 'UPLINK_COUNT_6', 'UPLINK_COUNT_7', 'UPLINK_COUNT_8']]

### FiberOpticCableType
- **Type**: typing.Optional[typing.Literal['MULTI_MODE', 'SINGLE_MODE']]

### OpticalStandard
- **Type**: typing.Optional[typing.Literal['OPTIC_1000BASE_LX', 'OPTIC_1000BASE_SX', 'OPTIC_100GBASE_CWDM4', 'OPTIC_100GBASE_LR4', 'OPTIC_100GBASE_SR4', 'OPTIC_100G_PSM4_MSA', 'OPTIC_10GBASE_IR', 'OPTIC_10GBASE_LR', 'OPTIC_10GBASE_SR', 'OPTIC_40GBASE_ESR', 'OPTIC_40GBASE_IR4_LR4L', 'OPTIC_40GBASE_LR4', 'OPTIC_40GBASE_SR']]

### MaximumSupportedWeightLbs
- **Type**: typing.Optional[typing.Literal['MAX_1400_LBS', 'MAX_1600_LBS', 'MAX_1800_LBS', 'MAX_2000_LBS', 'NO_LIMIT']]


# UpdateSiteRackPhysicalPropertiesOutput

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.Site'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts.outposts_classes.ResponseMetadata'>
- **Required**: Yes


