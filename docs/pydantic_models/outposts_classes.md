# Outposts Classes

# AddressTypeDef

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


# AssetInfoTypeDef

### AssetId
- **Type**: typing.Optional[str]

### RackId
- **Type**: typing.Optional[str]

### AssetType
- **Type**: typing.Optional[typing.Literal['COMPUTE']]

### ComputeAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.ComputeAttributesTypeDef]

### AssetLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.AssetLocationTypeDef]


# AssetInstanceTypeCapacityTypeDef

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# AssetInstanceTypeDef

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


# AssetLocationTypeDef

### RackElevation
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockingInstanceTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AwsServiceName
- **Type**: typing.Optional[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]


# CancelCapacityTaskInputTypeDef

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# CancelOrderInputTypeDef

### OrderId
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityTaskFailureTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityTaskSummaryTypeDef

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


# CatalogItemTypeDef

### CatalogItemId
- **Type**: typing.Optional[str]

### ItemStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'DISCONTINUED']]

### EC2Capacities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts_classes.EC2CapacityTypeDef]]

### PowerKva
- **Type**: typing.Optional[float]

### WeightLbs
- **Type**: typing.Optional[int]

### SupportedUplinkGbps
- **Type**: typing.Optional[typing.List[int]]

### SupportedStorage
- **Type**: typing.Optional[typing.List[typing.Literal['EBS', 'S3']]]


# ComputeAttributesTypeDef

### HostId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ISOLATED', 'RETIRING']]

### InstanceFamilies
- **Type**: typing.Optional[typing.List[str]]

### InstanceTypeCapacities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts_classes.AssetInstanceTypeCapacityTypeDef]]

### MaxVcpus
- **Type**: typing.Optional[int]


# ConnectionDetailsTypeDef

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


# CreateOrderInputTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### LineItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.outposts_classes.LineItemRequestTypeDef]
- **Required**: Yes

### PaymentOption
- **Type**: typing.Literal['ALL_UPFRONT', 'NO_UPFRONT', 'PARTIAL_UPFRONT']
- **Required**: Yes

### PaymentTerm
- **Type**: typing.Optional[typing.Literal['FIVE_YEARS', 'ONE_YEAR', 'THREE_YEARS']]


# CreateOrderOutputTypeDef

### Order
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.OrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOutpostInputTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### SupportedHardwareType
- **Type**: typing.Optional[typing.Literal['RACK', 'SERVER']]


# CreateOutpostOutputTypeDef

### Outpost
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.OutpostTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSiteInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OperatingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.AddressTypeDef]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.AddressTypeDef]

### RackPhysicalProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.RackPhysicalPropertiesTypeDef]


# CreateSiteOutputTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOutpostInputTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSiteInputTypeDef

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes


# EC2CapacityTypeDef

### Family
- **Type**: typing.Optional[str]

### MaxSize
- **Type**: typing.Optional[str]

### Quantity
- **Type**: typing.Optional[str]


# GetCapacityTaskInputTypeDef

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCapacityTaskOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.InstanceTypeCapacityTypeDef]
- **Required**: Yes

### InstancesToExclude
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.InstancesToExcludeOutputTypeDef'>
- **Required**: Yes

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### CapacityTaskStatus
- **Type**: typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']
- **Required**: Yes

### Failed
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.CapacityTaskFailureTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCatalogItemInputTypeDef

### CatalogItemId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCatalogItemOutputTypeDef

### CatalogItem
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.CatalogItemTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionResponseTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ConnectionDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrderInputTypeDef

### OrderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrderOutputTypeDef

### Order
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.OrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOutpostInputTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOutpostInstanceTypesInputPaginateTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# GetOutpostInstanceTypesInputTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetOutpostInstanceTypesOutputTypeDef

### InstanceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.InstanceTypeItemTypeDef]
- **Required**: Yes

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### OutpostArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOutpostOutputTypeDef

### Outpost
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.OutpostTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOutpostSupportedInstanceTypesInputPaginateTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OrderId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# GetOutpostSupportedInstanceTypesInputTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### OrderId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOutpostSupportedInstanceTypesOutputTypeDef

### InstanceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.InstanceTypeItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSiteAddressInputTypeDef

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes


# GetSiteAddressOutputTypeDef

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.AddressTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSiteInputTypeDef

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSiteOutputTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceTypeCapacityTypeDef

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# InstanceTypeItemTypeDef

### InstanceType
- **Type**: typing.Optional[str]

### VCPUs
- **Type**: typing.Optional[int]


# InstancesToExcludeOutputTypeDef

### Instances
- **Type**: typing.Optional[typing.List[str]]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### Services
- **Type**: typing.Optional[typing.List[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]


# InstancesToExcludeTypeDef

### Instances
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Services
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]


# InstancesToExcludeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LineItemAssetInformationTypeDef

### AssetId
- **Type**: typing.Optional[str]

### MacAddressList
- **Type**: typing.Optional[typing.List[str]]


# LineItemRequestTypeDef

### CatalogItemId
- **Type**: typing.Optional[str]

### Quantity
- **Type**: typing.Optional[int]


# LineItemTypeDef

### CatalogItemId
- **Type**: typing.Optional[str]

### LineItemId
- **Type**: typing.Optional[str]

### Quantity
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['BUILDING', 'CANCELLED', 'DELIVERED', 'ERROR', 'INSTALLED', 'INSTALLING', 'PREPARING', 'REPLACED', 'SHIPPED']]

### ShipmentInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.ShipmentInformationTypeDef]

### AssetInformationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts_classes.LineItemAssetInformationTypeDef]]

### PreviousLineItemId
- **Type**: typing.Optional[str]

### PreviousOrderId
- **Type**: typing.Optional[str]


# ListAssetInstancesInputPaginateTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AssetIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceTypeFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AwsServiceFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListAssetInstancesInputTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### AssetIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceTypeFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AwsServiceFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS', 'EC2', 'ELASTICACHE', 'ELB', 'RDS', 'ROUTE53']]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssetInstancesOutputTypeDef

### AssetInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.AssetInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssetsInputPaginateTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### HostIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### StatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'ISOLATED', 'RETIRING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListAssetsInputTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### HostIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'ISOLATED', 'RETIRING']]]


# ListAssetsOutputTypeDef

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.AssetInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBlockingInstancesForCapacityTaskInputPaginateTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListBlockingInstancesForCapacityTaskInputTypeDef

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


# ListBlockingInstancesForCapacityTaskOutputTypeDef

### BlockingInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.BlockingInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCapacityTasksInputPaginateTypeDef

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### CapacityTaskStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListCapacityTasksInputTypeDef

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### CapacityTaskStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']]]


# ListCapacityTasksOutputTypeDef

### CapacityTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.CapacityTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCatalogItemsInputPaginateTypeDef

### ItemClassFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['RACK', 'SERVER']]]

### SupportedStorageFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EBS', 'S3']]]

### EC2FamilyFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListCatalogItemsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ItemClassFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['RACK', 'SERVER']]]

### SupportedStorageFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EBS', 'S3']]]

### EC2FamilyFilter
- **Type**: typing.Optional[typing.Sequence[str]]


# ListCatalogItemsOutputTypeDef

### CatalogItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.CatalogItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrdersInputPaginateTypeDef

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListOrdersInputTypeDef

### OutpostIdentifierFilter
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrdersOutputTypeDef

### Orders
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.OrderSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOutpostsInputPaginateTypeDef

### LifeCycleStatusFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZoneFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZoneIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListOutpostsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LifeCycleStatusFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZoneFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### AvailabilityZoneIdFilter
- **Type**: typing.Optional[typing.Sequence[str]]


# ListOutpostsOutputTypeDef

### Outposts
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.OutpostTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSitesInputPaginateTypeDef

### OperatingAddressCountryCodeFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### OperatingAddressStateOrRegionFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### OperatingAddressCityFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.PaginatorConfigTypeDef]


# ListSitesInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### OperatingAddressCountryCodeFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### OperatingAddressStateOrRegionFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### OperatingAddressCityFilter
- **Type**: typing.Optional[typing.Sequence[str]]


# ListSitesOutputTypeDef

### Sites
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.SiteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OrderSummaryTypeDef

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


# OrderTypeDef

### OutpostId
- **Type**: typing.Optional[str]

### OrderId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DELIVERED', 'ERROR', 'FULFILLED', 'INSTALLING', 'IN_PROGRESS', 'PENDING', 'PREPARING', 'PROCESSING', 'RECEIVED']]

### LineItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.outposts_classes.LineItemTypeDef]]

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


# OutpostTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RackPhysicalPropertiesTypeDef

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


# ShipmentInformationTypeDef

### ShipmentTrackingNumber
- **Type**: typing.Optional[str]

### ShipmentCarrier
- **Type**: typing.Optional[typing.Literal['DBS', 'DHL', 'EXPEDITORS', 'FEDEX', 'UPS']]


# SiteTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.RackPhysicalPropertiesTypeDef]


# StartCapacityTaskInputTypeDef

### OutpostIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### InstancePools
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.outposts_classes.InstanceTypeCapacityTypeDef]
- **Required**: Yes

### OrderId
- **Type**: typing.Optional[str]

### InstancesToExclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.outposts_classes.InstancesToExcludeUnionTypeDef]

### DryRun
- **Type**: typing.Optional[bool]

### TaskActionOnBlockingInstances
- **Type**: typing.Optional[typing.Literal['FAIL_TASK', 'WAIT_FOR_EVACUATION']]


# StartCapacityTaskOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.outposts_classes.InstanceTypeCapacityTypeDef]
- **Required**: Yes

### InstancesToExclude
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.InstancesToExcludeOutputTypeDef'>
- **Required**: Yes

### DryRun
- **Type**: <class 'bool'>
- **Required**: Yes

### CapacityTaskStatus
- **Type**: typing.Literal['CANCELLATION_IN_PROGRESS', 'CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'REQUESTED', 'WAITING_FOR_EVACUATION']
- **Required**: Yes

### Failed
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.CapacityTaskFailureTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartConnectionRequestTypeDef

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


# StartConnectionResponseTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UnderlayIpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
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


# UpdateOutpostInputTypeDef

### OutpostId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SupportedHardwareType
- **Type**: typing.Optional[typing.Literal['RACK', 'SERVER']]


# UpdateOutpostOutputTypeDef

### Outpost
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.OutpostTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSiteAddressInputTypeDef

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.AddressTypeDef'>
- **Required**: Yes


# UpdateSiteAddressOutputTypeDef

### AddressType
- **Type**: typing.Literal['OPERATING_ADDRESS', 'SHIPPING_ADDRESS']
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.AddressTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSiteInputTypeDef

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]


# UpdateSiteOutputTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSiteRackPhysicalPropertiesInputTypeDef

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


# UpdateSiteRackPhysicalPropertiesOutputTypeDef

### Site
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.SiteTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.outposts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


