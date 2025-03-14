# Panorama Classes

# AlternateSoftwareMetadataTypeDef

### Version
- **Type**: typing.Optional[str]


# ApplicationInstanceTypeDef

### ApplicationInstanceId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### DefaultRuntimeContextDevice
- **Type**: typing.Optional[str]

### DefaultRuntimeContextDeviceName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HealthStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'NOT_AVAILABLE', 'RUNNING']]

### Name
- **Type**: typing.Optional[str]

### RuntimeContextStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.panorama_classes.ReportedRuntimeContextStateTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYMENT_ERROR', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DEPLOYMENT_PENDING', 'DEPLOYMENT_REQUESTED', 'DEPLOYMENT_SUCCEEDED', 'REMOVAL_FAILED', 'REMOVAL_IN_PROGRESS', 'REMOVAL_PENDING', 'REMOVAL_REQUESTED', 'REMOVAL_SUCCEEDED']]

### StatusDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationInstanceRequestTypeDef

### DefaultRuntimeContextDevice
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ManifestPayloadTypeDef'>
- **Required**: Yes

### ApplicationInstanceIdToReplace
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ManifestOverridesPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.ManifestOverridesPayloadTypeDef]

### Name
- **Type**: typing.Optional[str]

### RuntimeRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationInstanceResponseTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobForDevicesRequestTypeDef

### DeviceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### JobType
- **Type**: typing.Literal['OTA', 'REBOOT']
- **Required**: Yes

### DeviceJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.DeviceJobConfigTypeDef]


# CreateJobForDevicesResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNodeFromTemplateJobRequestTypeDef

### NodeName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputPackageName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputPackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateParameters
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['RTSP_CAMERA_STREAM']
- **Required**: Yes

### JobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsUnionTypeDef]]

### NodeDescription
- **Type**: typing.Optional[str]


# CreateNodeFromTemplateJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageImportJobRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobInputConfigTypeDef'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['MARKETPLACE_NODE_PACKAGE_VERSION', 'NODE_PACKAGE_VERSION']
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobOutputConfigTypeDef'>
- **Required**: Yes

### JobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsUnionTypeDef]]


# CreatePackageImportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageRequestTypeDef

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePackageResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.StorageLocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDeviceRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceResponseTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePackageRequestTypeDef

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeregisterPackageVersionRequestTypeDef

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccount
- **Type**: typing.Optional[str]

### UpdatedLatestPatchVersion
- **Type**: typing.Optional[str]


# DescribeApplicationInstanceDetailsRequestTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationInstanceDetailsResponseTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationInstanceIdToReplace
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultRuntimeContextDevice
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestOverridesPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ManifestOverridesPayloadTypeDef'>
- **Required**: Yes

### ManifestPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ManifestPayloadTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationInstanceRequestTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationInstanceResponseTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationInstanceIdToReplace
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultRuntimeContextDevice
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultRuntimeContextDeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HealthStatus
- **Type**: typing.Literal['ERROR', 'NOT_AVAILABLE', 'RUNNING']
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeContextStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.ReportedRuntimeContextStateTypeDef]
- **Required**: Yes

### RuntimeRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DEPLOYMENT_ERROR', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DEPLOYMENT_PENDING', 'DEPLOYMENT_REQUESTED', 'DEPLOYMENT_SUCCEEDED', 'REMOVAL_FAILED', 'REMOVAL_IN_PROGRESS', 'REMOVAL_PENDING', 'REMOVAL_REQUESTED', 'REMOVAL_SUCCEEDED']
- **Required**: Yes

### StatusDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceJobResponseTypeDef

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceType
- **Type**: typing.Literal['PANORAMA_APPLIANCE', 'PANORAMA_APPLIANCE_DEVELOPER_KIT']
- **Required**: Yes

### ImageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['OTA', 'REBOOT']
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DOWNLOADING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'REBOOTING', 'VERIFYING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeFromTemplateJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeFromTemplateJobResponseTypeDef

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsOutputTypeDef]
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NodeDescription
- **Type**: <class 'str'>
- **Required**: Yes

### NodeName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputPackageName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputPackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TemplateType
- **Type**: typing.Literal['RTSP_CAMERA_STREAM']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNodeRequestTypeDef

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccount
- **Type**: typing.Optional[str]


# DescribeNodeResponseTypeDef

### AssetName
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: typing.Literal['BUSINESS_LOGIC', 'MEDIA_SINK', 'MEDIA_SOURCE', 'ML_MODEL']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeInterface
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.NodeInterfaceTypeDef'>
- **Required**: Yes

### OwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### PackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageImportJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackageImportJobResponseTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobInputConfigTypeDef'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsOutputTypeDef]
- **Required**: Yes

### JobType
- **Type**: typing.Literal['MARKETPLACE_NODE_PACKAGE_VERSION', 'NODE_PACKAGE_VERSION']
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobOutputTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobOutputConfigTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageRequestTypeDef

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackageResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### ReadAccessPrincipalArns
- **Type**: typing.List[str]
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.StorageLocationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### WriteAccessPrincipalArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageVersionRequestTypeDef

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccount
- **Type**: typing.Optional[str]

### PatchVersion
- **Type**: typing.Optional[str]


# DescribePackageVersionResponseTypeDef

### IsLatestPatch
- **Type**: <class 'bool'>
- **Required**: Yes

### OwnerAccount
- **Type**: <class 'str'>
- **Required**: Yes

### PackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RegisteredTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DELETING', 'FAILED', 'REGISTER_COMPLETED', 'REGISTER_PENDING']
- **Required**: Yes

### StatusDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceJobConfigTypeDef

### OTAJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.OTAJobConfigTypeDef]


# DeviceJobTypeDef

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### DeviceId
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### JobId
- **Type**: typing.Optional[str]

### JobType
- **Type**: typing.Optional[typing.Literal['OTA', 'REBOOT']]


# DeviceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EthernetPayloadOutputTypeDef

### ConnectionType
- **Type**: typing.Literal['DHCP', 'STATIC_IP']
- **Required**: Yes

### StaticIpConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.StaticIpConnectionInfoOutputTypeDef]


# EthernetPayloadTypeDef

### ConnectionType
- **Type**: typing.Literal['DHCP', 'STATIC_IP']
- **Required**: Yes

### StaticIpConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.StaticIpConnectionInfoTypeDef]


# EthernetStatusTypeDef

### ConnectionStatus
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'CONNECTING', 'NOT_CONNECTED']]

### HwAddress
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# JobResourceTagsOutputTypeDef

### ResourceType
- **Type**: typing.Literal['PACKAGE']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# JobResourceTagsTypeDef

### ResourceType
- **Type**: typing.Literal['PACKAGE']
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# JobResourceTagsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTypeDef

### DeviceId
- **Type**: typing.Optional[str]

### JobId
- **Type**: typing.Optional[str]


# LatestDeviceJobTypeDef

### ImageVersion
- **Type**: typing.Optional[str]

### JobType
- **Type**: typing.Optional[typing.Literal['OTA', 'REBOOT']]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DOWNLOADING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'REBOOTING', 'VERIFYING']]


# ListApplicationInstanceDependenciesRequestTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstanceDependenciesResponseTypeDef

### PackageObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.PackageObjectTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstanceNodeInstancesRequestTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstanceNodeInstancesResponseTypeDef

### NodeInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstancesRequestTypeDef

### DeviceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['DEPLOYMENT_ERROR', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_SUCCEEDED', 'PROCESSING_DEPLOYMENT', 'PROCESSING_REMOVAL', 'REMOVAL_FAILED', 'REMOVAL_SUCCEEDED']]


# ListApplicationInstancesResponseTypeDef

### ApplicationInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.ApplicationInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesJobsRequestTypeDef

### DeviceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesJobsResponseTypeDef

### DeviceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.DeviceJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesRequestTypeDef

### DeviceAggregatedStatusFilter
- **Type**: typing.Optional[typing.Literal['AWAITING_PROVISIONING', 'DELETING', 'ERROR', 'FAILED', 'LEASE_EXPIRED', 'OFFLINE', 'ONLINE', 'PENDING', 'REBOOTING', 'UPDATE_NEEDED']]

### MaxResults
- **Type**: typing.Optional[int]

### NameFilter
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATED_TIME', 'DEVICE_AGGREGATED_STATUS', 'DEVICE_ID', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListDevicesResponseTypeDef

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.DeviceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodeFromTemplateJobsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodeFromTemplateJobsResponseTypeDef

### NodeFromTemplateJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeFromTemplateJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequestTypeDef

### Category
- **Type**: typing.Optional[typing.Literal['BUSINESS_LOGIC', 'MEDIA_SINK', 'MEDIA_SOURCE', 'ML_MODEL']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### PackageVersion
- **Type**: typing.Optional[str]

### PatchVersion
- **Type**: typing.Optional[str]


# ListNodesResponseTypeDef

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackageImportJobsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackageImportJobsResponseTypeDef

### PackageImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesResponseTypeDef

### Packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.PackageListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManifestOverridesPayloadTypeDef

### PayloadData
- **Type**: typing.Optional[str]


# ManifestPayloadTypeDef

### PayloadData
- **Type**: typing.Optional[str]


# NetworkPayloadOutputTypeDef

### Ethernet0
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayloadOutputTypeDef]

### Ethernet1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayloadOutputTypeDef]

### Ntp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NtpPayloadOutputTypeDef]


# NetworkPayloadTypeDef

### Ethernet0
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayloadTypeDef]

### Ethernet1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayloadTypeDef]

### Ntp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NtpPayloadTypeDef]


# NetworkPayloadUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkStatusTypeDef

### Ethernet0Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetStatusTypeDef]

### Ethernet1Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetStatusTypeDef]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### NtpStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NtpStatusTypeDef]


# NodeFromTemplateJobTypeDef

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### JobId
- **Type**: typing.Optional[str]

### NodeName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]

### TemplateType
- **Type**: typing.Optional[typing.Literal['RTSP_CAMERA_STREAM']]


# NodeInputPortTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeInstanceTypeDef

### CurrentStatus
- **Type**: typing.Literal['ERROR', 'NOT_AVAILABLE', 'PAUSED', 'RUNNING']
- **Required**: Yes

### NodeInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: typing.Optional[str]

### NodeName
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### PackagePatchVersion
- **Type**: typing.Optional[str]

### PackageVersion
- **Type**: typing.Optional[str]


# NodeInterfaceTypeDef

### Inputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeInputPortTypeDef]
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeOutputPortTypeDef]
- **Required**: Yes


# NodeOutputPortTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeSignalTypeDef

### NodeInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Signal
- **Type**: typing.Literal['PAUSE', 'RESUME']
- **Required**: Yes


# NodeTypeDef

### Category
- **Type**: typing.Literal['BUSINESS_LOGIC', 'MEDIA_SINK', 'MEDIA_SOURCE', 'ML_MODEL']
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OwnerAccount
- **Type**: typing.Optional[str]

### PackageArn
- **Type**: typing.Optional[str]


# NtpPayloadOutputTypeDef

### NtpServers
- **Type**: typing.List[str]
- **Required**: Yes


# NtpPayloadTypeDef

### NtpServers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# NtpStatusTypeDef

### ConnectionStatus
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'CONNECTING', 'NOT_CONNECTED']]

### IpAddress
- **Type**: typing.Optional[str]

### NtpServerName
- **Type**: typing.Optional[str]


# OTAJobConfigTypeDef

### ImageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### AllowMajorVersionUpdate
- **Type**: typing.Optional[bool]


# OutPutS3LocationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes


# PackageImportJobInputConfigTypeDef

### PackageVersionInputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.PackageVersionInputConfigTypeDef]


# PackageImportJobOutputConfigTypeDef

### PackageVersionOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.PackageVersionOutputConfigTypeDef]


# PackageImportJobOutputTypeDef

### OutputS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.OutPutS3LocationTypeDef'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes


# PackageImportJobTypeDef

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### JobId
- **Type**: typing.Optional[str]

### JobType
- **Type**: typing.Optional[typing.Literal['MARKETPLACE_NODE_PACKAGE_VERSION', 'NODE_PACKAGE_VERSION']]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]


# PackageListItemTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### PackageId
- **Type**: typing.Optional[str]

### PackageName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PackageObjectTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes


# PackageVersionInputConfigTypeDef

### S3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.S3LocationTypeDef'>
- **Required**: Yes


# PackageVersionOutputConfigTypeDef

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### MarkLatest
- **Type**: typing.Optional[bool]


# ProvisionDeviceRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### NetworkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NetworkPayloadUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ProvisionDeviceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: <class 'bytes'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### IotThingName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AWAITING_PROVISIONING', 'DELETING', 'ERROR', 'FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterPackageVersionRequestTypeDef

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes

### MarkLatest
- **Type**: typing.Optional[bool]

### OwnerAccount
- **Type**: typing.Optional[str]


# RemoveApplicationInstanceRequestTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# ReportedRuntimeContextStateTypeDef

### DesiredState
- **Type**: typing.Literal['REMOVED', 'RUNNING', 'STOPPED']
- **Required**: Yes

### DeviceReportedStatus
- **Type**: typing.Literal['INSTALL_ERROR', 'INSTALL_IN_PROGRESS', 'LAUNCHED', 'LAUNCH_ERROR', 'REMOVAL_FAILED', 'REMOVAL_IN_PROGRESS', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'STOP_ERROR']
- **Required**: Yes

### DeviceReportedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RuntimeContextName
- **Type**: <class 'str'>
- **Required**: Yes


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


# S3LocationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]


# SignalApplicationInstanceNodeInstancesRequestTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeSignals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.panorama_classes.NodeSignalTypeDef]
- **Required**: Yes


# SignalApplicationInstanceNodeInstancesResponseTypeDef

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StaticIpConnectionInfoOutputTypeDef

### DefaultGateway
- **Type**: <class 'str'>
- **Required**: Yes

### Dns
- **Type**: typing.List[str]
- **Required**: Yes

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Mask
- **Type**: <class 'str'>
- **Required**: Yes


# StaticIpConnectionInfoTypeDef

### DefaultGateway
- **Type**: <class 'str'>
- **Required**: Yes

### Dns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Mask
- **Type**: <class 'str'>
- **Required**: Yes


# StorageLocationTypeDef

### BinaryPrefixLocation
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### GeneratedPrefixLocation
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestPrefixLocation
- **Type**: <class 'str'>
- **Required**: Yes

### RepoPrefixLocation
- **Type**: <class 'str'>
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


# UpdateDeviceMetadataRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDeviceMetadataResponseTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


