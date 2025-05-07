# Snowball Classes

# Address

### AddressId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Company
- **Type**: typing.Optional[str]

### Street1
- **Type**: typing.Optional[str]

### Street2
- **Type**: typing.Optional[str]

### Street3
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### StateOrProvince
- **Type**: typing.Optional[str]

### PrefectureOrDistrict
- **Type**: typing.Optional[str]

### Landmark
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### IsRestricted
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_SHIP', 'CUST_PICKUP']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterListEntry

### ClusterId
- **Type**: typing.Optional[str]

### ClusterState
- **Type**: typing.Optional[typing.Literal['AwaitingQuorum', 'Cancelled', 'Complete', 'InUse', 'Pending']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# ClusterMetadata

### ClusterId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### KmsKeyARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### ClusterState
- **Type**: typing.Optional[typing.Literal['AwaitingQuorum', 'Cancelled', 'Complete', 'InUse', 'Pending']]

### JobType
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]

### SnowballType
- **Type**: typing.Optional[typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResourceOutput]

### AddressId
- **Type**: typing.Optional[str]

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.NotificationOutput]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: <class 'NoneType'>

### OnDeviceServiceConfiguration
- **Type**: <class 'NoneType'>


# CompatibleImage

### AmiId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CreateAddressRequest

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.Address'>
- **Required**: Yes


# CreateAddressResult

### AddressId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

### JobType
- **Type**: typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']
- **Required**: Yes

### AddressId
- **Type**: <class 'str'>
- **Required**: Yes

### SnowballType
- **Type**: typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']
- **Required**: Yes

### ShippingOption
- **Type**: typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']
- **Required**: Yes

### Resources
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResource, aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResourceOutput, NoneType]

### OnDeviceServiceConfiguration
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### KmsKeyARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### Notification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.Notification, aws_resource_validator.pydantic_models.snowball.snowball_classes.NotificationOutput, NoneType]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: <class 'NoneType'>

### RemoteManagement
- **Type**: typing.Optional[typing.Literal['INSTALLED_AUTOSTART', 'INSTALLED_ONLY', 'NOT_INSTALLED']]

### InitialClusterSize
- **Type**: typing.Optional[int]

### ForceCreateJobs
- **Type**: typing.Optional[bool]

### LongTermPricingIds
- **Type**: typing.Optional[typing.List[str]]

### SnowballCapacityPreference
- **Type**: typing.Optional[typing.Literal['NoPreference', 'T100', 'T13', 'T14', 'T240', 'T32', 'T42', 'T50', 'T8', 'T80', 'T98']]


# CreateClusterResult

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### JobListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobRequest

### JobType
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]

### Resources
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResource, aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResourceOutput, NoneType]

### OnDeviceServiceConfiguration
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### AddressId
- **Type**: typing.Optional[str]

### KmsKeyARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### SnowballCapacityPreference
- **Type**: typing.Optional[typing.Literal['NoPreference', 'T100', 'T13', 'T14', 'T240', 'T32', 'T42', 'T50', 'T8', 'T80', 'T98']]

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### Notification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.Notification, aws_resource_validator.pydantic_models.snowball.snowball_classes.NotificationOutput, NoneType]

### ClusterId
- **Type**: typing.Optional[str]

### SnowballType
- **Type**: typing.Optional[typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: <class 'NoneType'>

### DeviceConfiguration
- **Type**: <class 'NoneType'>

### RemoteManagement
- **Type**: typing.Optional[typing.Literal['INSTALLED_AUTOSTART', 'INSTALLED_ONLY', 'NOT_INSTALLED']]

### LongTermPricingId
- **Type**: typing.Optional[str]

### ImpactLevel
- **Type**: typing.Optional[typing.Literal['IL2', 'IL4', 'IL5', 'IL6', 'IL99']]

### PickupDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.PickupDetails, aws_resource_validator.pydantic_models.snowball.snowball_classes.PickupDetailsOutput, NoneType]


# CreateJobResult

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLongTermPricingRequest

### LongTermPricingType
- **Type**: typing.Literal['OneMonth', 'OneYear', 'ThreeYear']
- **Required**: Yes

### SnowballType
- **Type**: typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']
- **Required**: Yes

### IsLongTermPricingAutoRenew
- **Type**: typing.Optional[bool]


# CreateLongTermPricingResult

### LongTermPricingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReturnShippingLabelRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]


# CreateReturnShippingLabelResult

### Status
- **Type**: typing.Literal['Failed', 'InProgress', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# DataTransfer

### BytesTransferred
- **Type**: typing.Optional[int]

### ObjectsTransferred
- **Type**: typing.Optional[int]

### TotalBytes
- **Type**: typing.Optional[int]

### TotalObjects
- **Type**: typing.Optional[int]


# DependentService

### ServiceName
- **Type**: typing.Optional[typing.Literal['EKS_ANYWHERE', 'KUBERNETES']]

### ServiceVersion
- **Type**: <class 'NoneType'>


# DescribeAddressRequest

### AddressId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddressResult

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.Address'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAddressesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAddressesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PaginatorConfig]


# DescribeAddressesResult

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.Address]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResult

### ClusterMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ClusterMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobResult

### JobMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.JobMetadata'>
- **Required**: Yes

### SubJobMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReturnShippingLabelRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReturnShippingLabelResult

### Status
- **Type**: typing.Literal['Failed', 'InProgress', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ExpirationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ReturnShippingLabelURI
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceConfiguration

### SnowconeDeviceConfiguration
- **Type**: <class 'NoneType'>


# EKSOnDeviceServiceConfiguration

### KubernetesVersion
- **Type**: typing.Optional[str]

### EKSAnywhereVersion
- **Type**: typing.Optional[str]


# Ec2AmiResource

### AmiId
- **Type**: <class 'str'>
- **Required**: Yes

### SnowballAmiId
- **Type**: typing.Optional[str]


# EventTriggerDefinition

### EventResourceARN
- **Type**: typing.Optional[str]


# GetJobManifestRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobManifestResult

### ManifestURI
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobUnlockCodeRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobUnlockCodeResult

### UnlockCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# GetSnowballUsageResult

### SnowballLimit
- **Type**: <class 'int'>
- **Required**: Yes

### SnowballsInUse
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# GetSoftwareUpdatesRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSoftwareUpdatesResult

### UpdatesURI
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes


# INDTaxDocuments

### GSTIN
- **Type**: typing.Optional[str]


# JobListEntry

### JobId
- **Type**: typing.Optional[str]

### JobState
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'InProgress', 'InTransitToAWS', 'InTransitToCustomer', 'Listing', 'New', 'Pending', 'PreparingAppliance', 'PreparingShipment', 'WithAWS', 'WithAWSSortingFacility', 'WithCustomer']]

### IsMaster
- **Type**: typing.Optional[bool]

### JobType
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]

### SnowballType
- **Type**: typing.Optional[typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# JobLogs

### JobCompletionReportURI
- **Type**: typing.Optional[str]

### JobSuccessLogURI
- **Type**: typing.Optional[str]

### JobFailureLogURI
- **Type**: typing.Optional[str]


# JobMetadata

### JobId
- **Type**: typing.Optional[str]

### JobState
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'InProgress', 'InTransitToAWS', 'InTransitToCustomer', 'Listing', 'New', 'Pending', 'PreparingAppliance', 'PreparingShipment', 'WithAWS', 'WithAWSSortingFacility', 'WithCustomer']]

### JobType
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]

### SnowballType
- **Type**: typing.Optional[typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResourceOutput]

### Description
- **Type**: typing.Optional[str]

### KmsKeyARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### AddressId
- **Type**: typing.Optional[str]

### ShippingDetails
- **Type**: <class 'NoneType'>

### SnowballCapacityPreference
- **Type**: typing.Optional[typing.Literal['NoPreference', 'T100', 'T13', 'T14', 'T240', 'T32', 'T42', 'T50', 'T8', 'T80', 'T98']]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.NotificationOutput]

### DataTransferProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.DataTransfer]

### JobLogInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobLogs]

### ClusterId
- **Type**: typing.Optional[str]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: <class 'NoneType'>

### DeviceConfiguration
- **Type**: <class 'NoneType'>

### RemoteManagement
- **Type**: typing.Optional[typing.Literal['INSTALLED_AUTOSTART', 'INSTALLED_ONLY', 'NOT_INSTALLED']]

### LongTermPricingId
- **Type**: typing.Optional[str]

### OnDeviceServiceConfiguration
- **Type**: <class 'NoneType'>

### ImpactLevel
- **Type**: typing.Optional[typing.Literal['IL2', 'IL4', 'IL5', 'IL6', 'IL99']]

### PickupDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PickupDetailsOutput]

### SnowballId
- **Type**: typing.Optional[str]


# JobResource

### S3Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.S3Resource]]

### LambdaResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.LambdaResource]]

### Ec2AmiResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.Ec2AmiResource]]


# JobResourceOutput

### S3Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.S3ResourceOutput]]

### LambdaResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.LambdaResourceOutput]]

### Ec2AmiResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.Ec2AmiResource]]


# KeyRange

### BeginMarker
- **Type**: typing.Optional[str]

### EndMarker
- **Type**: typing.Optional[str]


# LambdaResource

### LambdaArn
- **Type**: typing.Optional[str]

### EventTriggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.EventTriggerDefinition]]


# LambdaResourceOutput

### LambdaArn
- **Type**: typing.Optional[str]

### EventTriggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.EventTriggerDefinition]]


# ListClusterJobsRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClusterJobsRequestPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PaginatorConfig]


# ListClusterJobsResult

### JobListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PaginatorConfig]


# ListClustersResult

### ClusterListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.ClusterListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCompatibleImagesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCompatibleImagesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PaginatorConfig]


# ListCompatibleImagesResult

### CompatibleImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.CompatibleImage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PaginatorConfig]


# ListJobsResult

### JobListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLongTermPricingRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLongTermPricingRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.PaginatorConfig]


# ListLongTermPricingResult

### LongTermPricingEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.LongTermPricingListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPickupLocationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPickupLocationsResult

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.Address]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceVersionsRequest

### ServiceName
- **Type**: typing.Literal['EKS_ANYWHERE', 'KUBERNETES']
- **Required**: Yes

### DependentServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.DependentService]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceVersionsResult

### ServiceVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.ServiceVersion]
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['EKS_ANYWHERE', 'KUBERNETES']
- **Required**: Yes

### DependentServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.DependentService]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball.snowball_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LongTermPricingListEntry

### LongTermPricingId
- **Type**: typing.Optional[str]

### LongTermPricingEndDate
- **Type**: typing.Optional[datetime.datetime]

### LongTermPricingStartDate
- **Type**: typing.Optional[datetime.datetime]

### LongTermPricingType
- **Type**: typing.Optional[typing.Literal['OneMonth', 'OneYear', 'ThreeYear']]

### CurrentActiveJob
- **Type**: typing.Optional[str]

### ReplacementJob
- **Type**: typing.Optional[str]

### IsLongTermPricingAutoRenew
- **Type**: typing.Optional[bool]

### LongTermPricingStatus
- **Type**: typing.Optional[str]

### SnowballType
- **Type**: typing.Optional[typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']]

### JobIds
- **Type**: typing.Optional[typing.List[str]]


# NFSOnDeviceServiceConfiguration

### StorageLimit
- **Type**: typing.Optional[int]

### StorageUnit
- **Type**: typing.Optional[typing.Literal['TB']]


# Notification

### SnsTopicARN
- **Type**: typing.Optional[str]

### JobStatesToNotify
- **Type**: typing.Optional[typing.List[typing.Literal['Cancelled', 'Complete', 'InProgress', 'InTransitToAWS', 'InTransitToCustomer', 'Listing', 'New', 'Pending', 'PreparingAppliance', 'PreparingShipment', 'WithAWS', 'WithAWSSortingFacility', 'WithCustomer']]]

### NotifyAll
- **Type**: typing.Optional[bool]

### DevicePickupSnsTopicARN
- **Type**: typing.Optional[str]


# NotificationOutput

### SnsTopicARN
- **Type**: typing.Optional[str]

### JobStatesToNotify
- **Type**: typing.Optional[typing.List[typing.Literal['Cancelled', 'Complete', 'InProgress', 'InTransitToAWS', 'InTransitToCustomer', 'Listing', 'New', 'Pending', 'PreparingAppliance', 'PreparingShipment', 'WithAWS', 'WithAWSSortingFacility', 'WithCustomer']]]

### NotifyAll
- **Type**: typing.Optional[bool]

### DevicePickupSnsTopicARN
- **Type**: typing.Optional[str]


# OnDeviceServiceConfiguration

### NFSOnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.NFSOnDeviceServiceConfiguration]

### TGWOnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.TGWOnDeviceServiceConfiguration]

### EKSOnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.EKSOnDeviceServiceConfiguration]

### S3OnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.S3OnDeviceServiceConfiguration]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PickupDetails

### Name
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### IdentificationNumber
- **Type**: typing.Optional[str]

### IdentificationExpirationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### IdentificationIssuingOrg
- **Type**: typing.Optional[str]

### DevicePickupId
- **Type**: typing.Optional[str]


# PickupDetailsOutput

### Name
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### IdentificationNumber
- **Type**: typing.Optional[str]

### IdentificationExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### IdentificationIssuingOrg
- **Type**: typing.Optional[str]

### DevicePickupId
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


# S3OnDeviceServiceConfiguration

### StorageLimit
- **Type**: typing.Optional[float]

### StorageUnit
- **Type**: typing.Optional[typing.Literal['TB']]

### ServiceSize
- **Type**: typing.Optional[int]

### FaultTolerance
- **Type**: typing.Optional[int]


# S3Resource

### BucketArn
- **Type**: typing.Optional[str]

### KeyRange
- **Type**: <class 'NoneType'>

### TargetOnDeviceServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.TargetOnDeviceService]]


# S3ResourceOutput

### BucketArn
- **Type**: typing.Optional[str]

### KeyRange
- **Type**: <class 'NoneType'>

### TargetOnDeviceServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball.snowball_classes.TargetOnDeviceService]]


# ServiceVersion

### Version
- **Type**: typing.Optional[str]


# Shipment

### Status
- **Type**: typing.Optional[str]

### TrackingNumber
- **Type**: typing.Optional[str]


# ShippingDetails

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### InboundShipment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.Shipment]

### OutboundShipment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.Shipment]


# SnowconeDeviceConfiguration

### WirelessConnection
- **Type**: <class 'NoneType'>


# TGWOnDeviceServiceConfiguration

### StorageLimit
- **Type**: typing.Optional[int]

### StorageUnit
- **Type**: typing.Optional[typing.Literal['TB']]


# TargetOnDeviceService

### ServiceName
- **Type**: typing.Optional[typing.Literal['NFS_ON_DEVICE_SERVICE', 'S3_ON_DEVICE_SERVICE']]

### TransferOption
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]


# TaxDocuments

### IND
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball.snowball_classes.INDTaxDocuments]


# UpdateClusterRequest

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResource, aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResourceOutput, NoneType]

### OnDeviceServiceConfiguration
- **Type**: <class 'NoneType'>

### AddressId
- **Type**: typing.Optional[str]

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### Notification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.Notification, aws_resource_validator.pydantic_models.snowball.snowball_classes.NotificationOutput, NoneType]

### ForwardingAddressId
- **Type**: typing.Optional[str]


# UpdateJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### Notification
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.Notification, aws_resource_validator.pydantic_models.snowball.snowball_classes.NotificationOutput, NoneType]

### Resources
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResource, aws_resource_validator.pydantic_models.snowball.snowball_classes.JobResourceOutput, NoneType]

### OnDeviceServiceConfiguration
- **Type**: <class 'NoneType'>

### AddressId
- **Type**: typing.Optional[str]

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### Description
- **Type**: typing.Optional[str]

### SnowballCapacityPreference
- **Type**: typing.Optional[typing.Literal['NoPreference', 'T100', 'T13', 'T14', 'T240', 'T32', 'T42', 'T50', 'T8', 'T80', 'T98']]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### PickupDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.snowball.snowball_classes.PickupDetails, aws_resource_validator.pydantic_models.snowball.snowball_classes.PickupDetailsOutput, NoneType]


# UpdateJobShipmentStateRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ShipmentState
- **Type**: typing.Literal['RECEIVED', 'RETURNED']
- **Required**: Yes


# UpdateLongTermPricingRequest

### LongTermPricingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplacementJob
- **Type**: typing.Optional[str]

### IsLongTermPricingAutoRenew
- **Type**: typing.Optional[bool]


# WirelessConnection

### IsWifiEnabled
- **Type**: typing.Optional[bool]


