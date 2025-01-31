# Snowball Classes

# AddressTypeDef

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

# CancelClusterRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterListEntryTypeDef

### ClusterId
- **Type**: typing.Optional[str]

### ClusterState
- **Type**: typing.Optional[typing.Literal['AwaitingQuorum', 'Cancelled', 'Complete', 'InUse', 'Pending']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]


# ClusterMetadataTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobResourceOutputTypeDef]

### AddressId
- **Type**: typing.Optional[str]

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NotificationOutputTypeDef]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.TaxDocumentsTypeDef]

### OnDeviceServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.OnDeviceServiceConfigurationTypeDef]


# CompatibleImageTypeDef

### AmiId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CreateAddressRequestRequestTypeDef

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.AddressTypeDef'>
- **Required**: Yes


# CreateAddressResultTypeDef

### AddressId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobResourceTypeDef]

### OnDeviceServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.OnDeviceServiceConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### KmsKeyARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NotificationTypeDef]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.TaxDocumentsTypeDef]

### RemoteManagement
- **Type**: typing.Optional[typing.Literal['INSTALLED_AUTOSTART', 'INSTALLED_ONLY', 'NOT_INSTALLED']]

### InitialClusterSize
- **Type**: typing.Optional[int]

### ForceCreateJobs
- **Type**: typing.Optional[bool]

### LongTermPricingIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SnowballCapacityPreference
- **Type**: typing.Optional[typing.Literal['NoPreference', 'T100', 'T13', 'T14', 'T240', 'T32', 'T42', 'T50', 'T8', 'T80', 'T98']]


# CreateClusterResultTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### JobListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.JobListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobRequestRequestTypeDef

### JobType
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]

### Resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobResourceTypeDef]

### OnDeviceServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.OnDeviceServiceConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NotificationTypeDef]

### ClusterId
- **Type**: typing.Optional[str]

### SnowballType
- **Type**: typing.Optional[typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.TaxDocumentsTypeDef]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.DeviceConfigurationTypeDef]

### RemoteManagement
- **Type**: typing.Optional[typing.Literal['INSTALLED_AUTOSTART', 'INSTALLED_ONLY', 'NOT_INSTALLED']]

### LongTermPricingId
- **Type**: typing.Optional[str]

### ImpactLevel
- **Type**: typing.Optional[typing.Literal['IL2', 'IL4', 'IL5', 'IL6', 'IL99']]

### PickupDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PickupDetailsTypeDef]


# CreateJobResultTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLongTermPricingRequestRequestTypeDef

### LongTermPricingType
- **Type**: typing.Literal['OneMonth', 'OneYear', 'ThreeYear']
- **Required**: Yes

### SnowballType
- **Type**: typing.Literal['EDGE', 'EDGE_C', 'EDGE_CG', 'EDGE_S', 'RACK_5U_C', 'SNC1_HDD', 'SNC1_SSD', 'STANDARD', 'V3_5C', 'V3_5S']
- **Required**: Yes

### IsLongTermPricingAutoRenew
- **Type**: typing.Optional[bool]


# CreateLongTermPricingResultTypeDef

### LongTermPricingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReturnShippingLabelRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]


# CreateReturnShippingLabelResultTypeDef

### Status
- **Type**: typing.Literal['Failed', 'InProgress', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataTransferTypeDef

### BytesTransferred
- **Type**: typing.Optional[int]

### ObjectsTransferred
- **Type**: typing.Optional[int]

### TotalBytes
- **Type**: typing.Optional[int]

### TotalObjects
- **Type**: typing.Optional[int]


# DependentServiceTypeDef

### ServiceName
- **Type**: typing.Optional[typing.Literal['EKS_ANYWHERE', 'KUBERNETES']]

### ServiceVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.ServiceVersionTypeDef]


# DescribeAddressRequestRequestTypeDef

### AddressId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAddressResultTypeDef

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.AddressTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAddressesRequestDescribeAddressesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PaginatorConfigTypeDef]


# DescribeAddressesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAddressesResultTypeDef

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.AddressTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeClusterRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResultTypeDef

### ClusterMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ClusterMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobResultTypeDef

### JobMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.JobMetadataTypeDef'>
- **Required**: Yes

### SubJobMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.JobMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReturnShippingLabelRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReturnShippingLabelResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceConfigurationTypeDef

### SnowconeDeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.SnowconeDeviceConfigurationTypeDef]


# EKSOnDeviceServiceConfigurationTypeDef

### KubernetesVersion
- **Type**: typing.Optional[str]

### EKSAnywhereVersion
- **Type**: typing.Optional[str]


# Ec2AmiResourceTypeDef

### AmiId
- **Type**: <class 'str'>
- **Required**: Yes

### SnowballAmiId
- **Type**: typing.Optional[str]


# EventTriggerDefinitionTypeDef

### EventResourceARN
- **Type**: typing.Optional[str]


# GetJobManifestRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobManifestResultTypeDef

### ManifestURI
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobUnlockCodeRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobUnlockCodeResultTypeDef

### UnlockCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSnowballUsageResultTypeDef

### SnowballLimit
- **Type**: <class 'int'>
- **Required**: Yes

### SnowballsInUse
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSoftwareUpdatesRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSoftwareUpdatesResultTypeDef

### UpdatesURI
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# INDTaxDocumentsTypeDef

### GSTIN
- **Type**: typing.Optional[str]


# JobListEntryTypeDef

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


# JobLogsTypeDef

### JobCompletionReportURI
- **Type**: typing.Optional[str]

### JobSuccessLogURI
- **Type**: typing.Optional[str]

### JobFailureLogURI
- **Type**: typing.Optional[str]


# JobMetadataTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobResourceOutputTypeDef]

### Description
- **Type**: typing.Optional[str]

### KmsKeyARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### AddressId
- **Type**: typing.Optional[str]

### ShippingDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.ShippingDetailsTypeDef]

### SnowballCapacityPreference
- **Type**: typing.Optional[typing.Literal['NoPreference', 'T100', 'T13', 'T14', 'T240', 'T32', 'T42', 'T50', 'T8', 'T80', 'T98']]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NotificationOutputTypeDef]

### DataTransferProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.DataTransferTypeDef]

### JobLogInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobLogsTypeDef]

### ClusterId
- **Type**: typing.Optional[str]

### ForwardingAddressId
- **Type**: typing.Optional[str]

### TaxDocuments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.TaxDocumentsTypeDef]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.DeviceConfigurationTypeDef]

### RemoteManagement
- **Type**: typing.Optional[typing.Literal['INSTALLED_AUTOSTART', 'INSTALLED_ONLY', 'NOT_INSTALLED']]

### LongTermPricingId
- **Type**: typing.Optional[str]

### OnDeviceServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.OnDeviceServiceConfigurationTypeDef]

### ImpactLevel
- **Type**: typing.Optional[typing.Literal['IL2', 'IL4', 'IL5', 'IL6', 'IL99']]

### PickupDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PickupDetailsOutputTypeDef]

### SnowballId
- **Type**: typing.Optional[str]


# JobResourceOutputTypeDef

### S3Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball_classes.S3ResourceOutputTypeDef]]

### LambdaResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball_classes.LambdaResourceOutputTypeDef]]

### Ec2AmiResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball_classes.Ec2AmiResourceTypeDef]]


# JobResourceTypeDef

### S3Resources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.snowball_classes.S3ResourceTypeDef]]

### LambdaResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.snowball_classes.LambdaResourceTypeDef]]

### Ec2AmiResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.snowball_classes.Ec2AmiResourceTypeDef]]


# KeyRangeTypeDef

### BeginMarker
- **Type**: typing.Optional[str]

### EndMarker
- **Type**: typing.Optional[str]


# LambdaResourceOutputTypeDef

### LambdaArn
- **Type**: typing.Optional[str]

### EventTriggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball_classes.EventTriggerDefinitionTypeDef]]


# LambdaResourceTypeDef

### LambdaArn
- **Type**: typing.Optional[str]

### EventTriggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.snowball_classes.EventTriggerDefinitionTypeDef]]


# ListClusterJobsRequestListClusterJobsPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PaginatorConfigTypeDef]


# ListClusterJobsRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClusterJobsResultTypeDef

### JobListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.JobListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestListClustersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PaginatorConfigTypeDef]


# ListClustersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersResultTypeDef

### ClusterListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.ClusterListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCompatibleImagesRequestListCompatibleImagesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PaginatorConfigTypeDef]


# ListCompatibleImagesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCompatibleImagesResultTypeDef

### CompatibleImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.CompatibleImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequestListJobsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PaginatorConfigTypeDef]


# ListJobsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListJobsResultTypeDef

### JobListEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.JobListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLongTermPricingRequestListLongTermPricingPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PaginatorConfigTypeDef]


# ListLongTermPricingRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLongTermPricingResultTypeDef

### LongTermPricingEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.LongTermPricingListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPickupLocationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPickupLocationsResultTypeDef

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.AddressTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServiceVersionsRequestRequestTypeDef

### ServiceName
- **Type**: typing.Literal['EKS_ANYWHERE', 'KUBERNETES']
- **Required**: Yes

### DependentServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.snowball_classes.DependentServiceTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServiceVersionsResultTypeDef

### ServiceVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.ServiceVersionTypeDef]
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['EKS_ANYWHERE', 'KUBERNETES']
- **Required**: Yes

### DependentServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.snowball_classes.DependentServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.snowball_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LongTermPricingListEntryTypeDef

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


# NFSOnDeviceServiceConfigurationTypeDef

### StorageLimit
- **Type**: typing.Optional[int]

### StorageUnit
- **Type**: typing.Optional[typing.Literal['TB']]


# NotificationOutputTypeDef

### SnsTopicARN
- **Type**: typing.Optional[str]

### JobStatesToNotify
- **Type**: typing.Optional[typing.List[typing.Literal['Cancelled', 'Complete', 'InProgress', 'InTransitToAWS', 'InTransitToCustomer', 'Listing', 'New', 'Pending', 'PreparingAppliance', 'PreparingShipment', 'WithAWS', 'WithAWSSortingFacility', 'WithCustomer']]]

### NotifyAll
- **Type**: typing.Optional[bool]

### DevicePickupSnsTopicARN
- **Type**: typing.Optional[str]


# NotificationTypeDef

### SnsTopicARN
- **Type**: typing.Optional[str]

### JobStatesToNotify
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Cancelled', 'Complete', 'InProgress', 'InTransitToAWS', 'InTransitToCustomer', 'Listing', 'New', 'Pending', 'PreparingAppliance', 'PreparingShipment', 'WithAWS', 'WithAWSSortingFacility', 'WithCustomer']]]

### NotifyAll
- **Type**: typing.Optional[bool]

### DevicePickupSnsTopicARN
- **Type**: typing.Optional[str]


# OnDeviceServiceConfigurationTypeDef

### NFSOnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NFSOnDeviceServiceConfigurationTypeDef]

### TGWOnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.TGWOnDeviceServiceConfigurationTypeDef]

### EKSOnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.EKSOnDeviceServiceConfigurationTypeDef]

### S3OnDeviceService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.S3OnDeviceServiceConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PickupDetailsOutputTypeDef

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


# PickupDetailsTypeDef

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


# S3OnDeviceServiceConfigurationTypeDef

### StorageLimit
- **Type**: typing.Optional[float]

### StorageUnit
- **Type**: typing.Optional[typing.Literal['TB']]

### ServiceSize
- **Type**: typing.Optional[int]

### FaultTolerance
- **Type**: typing.Optional[int]


# S3ResourceOutputTypeDef

### BucketArn
- **Type**: typing.Optional[str]

### KeyRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.KeyRangeTypeDef]

### TargetOnDeviceServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.snowball_classes.TargetOnDeviceServiceTypeDef]]


# S3ResourceTypeDef

### BucketArn
- **Type**: typing.Optional[str]

### KeyRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.KeyRangeTypeDef]

### TargetOnDeviceServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.snowball_classes.TargetOnDeviceServiceTypeDef]]


# ServiceVersionTypeDef

### Version
- **Type**: typing.Optional[str]


# ShipmentTypeDef

### Status
- **Type**: typing.Optional[str]

### TrackingNumber
- **Type**: typing.Optional[str]


# ShippingDetailsTypeDef

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### InboundShipment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.ShipmentTypeDef]

### OutboundShipment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.ShipmentTypeDef]


# SnowconeDeviceConfigurationTypeDef

### WirelessConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.WirelessConnectionTypeDef]


# TGWOnDeviceServiceConfigurationTypeDef

### StorageLimit
- **Type**: typing.Optional[int]

### StorageUnit
- **Type**: typing.Optional[typing.Literal['TB']]


# TargetOnDeviceServiceTypeDef

### ServiceName
- **Type**: typing.Optional[typing.Literal['NFS_ON_DEVICE_SERVICE', 'S3_ON_DEVICE_SERVICE']]

### TransferOption
- **Type**: typing.Optional[typing.Literal['EXPORT', 'IMPORT', 'LOCAL_USE']]


# TaxDocumentsTypeDef

### IND
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.INDTaxDocumentsTypeDef]


# UpdateClusterRequestRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobResourceTypeDef]

### OnDeviceServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.OnDeviceServiceConfigurationTypeDef]

### AddressId
- **Type**: typing.Optional[str]

### ShippingOption
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'NEXT_DAY', 'SECOND_DAY', 'STANDARD']]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NotificationTypeDef]

### ForwardingAddressId
- **Type**: typing.Optional[str]


# UpdateJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: typing.Optional[str]

### Notification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.NotificationTypeDef]

### Resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.JobResourceTypeDef]

### OnDeviceServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.OnDeviceServiceConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.snowball_classes.PickupDetailsTypeDef]


# UpdateJobShipmentStateRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ShipmentState
- **Type**: typing.Literal['RECEIVED', 'RETURNED']
- **Required**: Yes


# UpdateLongTermPricingRequestRequestTypeDef

### LongTermPricingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplacementJob
- **Type**: typing.Optional[str]

### IsLongTermPricingAutoRenew
- **Type**: typing.Optional[bool]


# WirelessConnectionTypeDef

### IsWifiEnabled
- **Type**: typing.Optional[bool]


