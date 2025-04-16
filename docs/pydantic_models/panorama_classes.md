# Panorama Classes

# AlternateSoftwareMetadata

### Version
- **Type**: typing.Optional[str]


# ApplicationInstance

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.panorama_classes.ReportedRuntimeContextState]]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYMENT_ERROR', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_IN_PROGRESS', 'DEPLOYMENT_PENDING', 'DEPLOYMENT_REQUESTED', 'DEPLOYMENT_SUCCEEDED', 'REMOVAL_FAILED', 'REMOVAL_IN_PROGRESS', 'REMOVAL_PENDING', 'REMOVAL_REQUESTED', 'REMOVAL_SUCCEEDED']]

### StatusDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationInstanceRequest

### DefaultRuntimeContextDevice
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ManifestPayload'>
- **Required**: Yes

### ApplicationInstanceIdToReplace
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ManifestOverridesPayload
- **Type**: <class 'NoneType'>

### Name
- **Type**: typing.Optional[str]

### RuntimeRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateApplicationInstanceResponse

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobForDevicesRequest

### DeviceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### JobType
- **Type**: typing.Literal['OTA', 'REBOOT']
- **Required**: Yes

### DeviceJobConfig
- **Type**: <class 'NoneType'>


# CreateJobForDevicesResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNodeFromTemplateJobRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsUnion]]

### NodeDescription
- **Type**: typing.Optional[str]


# CreateNodeFromTemplateJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageImportJobRequest

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobInputConfig'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['MARKETPLACE_NODE_PACKAGE_VERSION', 'NODE_PACKAGE_VERSION']
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobOutputConfig'>
- **Required**: Yes

### JobTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsUnion]]


# CreatePackageImportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageRequest

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePackageResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.StorageLocation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDeviceRequest

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceResponse

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePackageRequest

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeregisterPackageVersionRequest

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


# DescribeApplicationInstanceDetailsRequest

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationInstanceDetailsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ManifestOverridesPayload'>
- **Required**: Yes

### ManifestPayload
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ManifestPayload'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationInstanceRequest

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationInstanceResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.ReportedRuntimeContextState]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeviceJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeviceRequest

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeFromTemplateJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNodeFromTemplateJobResponse

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNodeRequest

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccount
- **Type**: typing.Optional[str]


# DescribeNodeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.NodeInterface'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackageImportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackageImportJobResponse

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobInputConfig'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobTags
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.JobResourceTagsOutput]
- **Required**: Yes

### JobType
- **Type**: typing.Literal['MARKETPLACE_NODE_PACKAGE_VERSION', 'NODE_PACKAGE_VERSION']
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobOutput'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.PackageImportJobOutputConfig'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackageRequest

### PackageId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.StorageLocation'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### WriteAccessPrincipalArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackageVersionRequest

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


# DescribePackageVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# Device

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceJob

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


# DeviceJobConfig

### OTAJobConfig
- **Type**: <class 'NoneType'>


# EthernetPayload

### ConnectionType
- **Type**: typing.Literal['DHCP', 'STATIC_IP']
- **Required**: Yes

### StaticIpConnectionInfo
- **Type**: <class 'NoneType'>


# EthernetPayloadOutput

### ConnectionType
- **Type**: typing.Literal['DHCP', 'STATIC_IP']
- **Required**: Yes

### StaticIpConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.StaticIpConnectionInfoOutput]


# EthernetStatus

### ConnectionStatus
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'CONNECTING', 'NOT_CONNECTED']]

### HwAddress
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]


# Job

### DeviceId
- **Type**: typing.Optional[str]

### JobId
- **Type**: typing.Optional[str]


# JobResourceTags

### ResourceType
- **Type**: typing.Literal['PACKAGE']
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# JobResourceTagsOutput

### ResourceType
- **Type**: typing.Literal['PACKAGE']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# JobResourceTagsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LatestDeviceJob

### ImageVersion
- **Type**: typing.Optional[str]

### JobType
- **Type**: typing.Optional[typing.Literal['OTA', 'REBOOT']]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DOWNLOADING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'REBOOTING', 'VERIFYING']]


# ListApplicationInstanceDependenciesRequest

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstanceDependenciesResponse

### PackageObjects
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.PackageObject]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstanceNodeInstancesRequest

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstanceNodeInstancesResponse

### NodeInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationInstancesRequest

### DeviceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['DEPLOYMENT_ERROR', 'DEPLOYMENT_FAILED', 'DEPLOYMENT_SUCCEEDED', 'PROCESSING_DEPLOYMENT', 'PROCESSING_REMOVAL', 'REMOVAL_FAILED', 'REMOVAL_SUCCEEDED']]


# ListApplicationInstancesResponse

### ApplicationInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.ApplicationInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesJobsRequest

### DeviceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesJobsResponse

### DeviceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.DeviceJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesRequest

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


# ListDevicesResponse

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.Device]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodeFromTemplateJobsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodeFromTemplateJobsResponse

### NodeFromTemplateJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeFromTemplateJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequest

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


# ListNodesResponse

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.Node]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackageImportJobsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackageImportJobsResponse

### PackageImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.PackageImportJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagesResponse

### Packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.PackageListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# ManifestOverridesPayload

### PayloadData
- **Type**: typing.Optional[str]


# ManifestPayload

### PayloadData
- **Type**: typing.Optional[str]


# NetworkPayload

### Ethernet0
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayload]

### Ethernet1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayload]

### Ntp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NtpPayload]


# NetworkPayloadOutput

### Ethernet0
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayloadOutput]

### Ethernet1
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetPayloadOutput]

### Ntp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NtpPayloadOutput]


# NetworkPayloadUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkStatus

### Ethernet0Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetStatus]

### Ethernet1Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.EthernetStatus]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### NtpStatus
- **Type**: <class 'NoneType'>


# Node

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


# NodeFromTemplateJob

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


# NodeInputPort

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeInstance

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


# NodeInterface

### Inputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeInputPort]
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.panorama_classes.NodeOutputPort]
- **Required**: Yes


# NodeOutputPort

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeSignal

### NodeInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Signal
- **Type**: typing.Literal['PAUSE', 'RESUME']
- **Required**: Yes


# NtpPayload

### NtpServers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# NtpPayloadOutput

### NtpServers
- **Type**: typing.List[str]
- **Required**: Yes


# NtpStatus

### ConnectionStatus
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'CONNECTING', 'NOT_CONNECTED']]

### IpAddress
- **Type**: typing.Optional[str]

### NtpServerName
- **Type**: typing.Optional[str]


# OTAJobConfig

### ImageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### AllowMajorVersionUpdate
- **Type**: typing.Optional[bool]


# OutPutS3Location

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes


# PackageImportJob

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


# PackageImportJobInputConfig

### PackageVersionInputConfig
- **Type**: <class 'NoneType'>


# PackageImportJobOutput

### OutputS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.OutPutS3Location'>
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


# PackageImportJobOutputConfig

### PackageVersionOutputConfig
- **Type**: <class 'NoneType'>


# PackageListItem

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


# PackageObject

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PatchVersion
- **Type**: <class 'str'>
- **Required**: Yes


# PackageVersionInputConfig

### S3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.S3Location'>
- **Required**: Yes


# PackageVersionOutputConfig

### PackageName
- **Type**: <class 'str'>
- **Required**: Yes

### PackageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### MarkLatest
- **Type**: typing.Optional[bool]


# ProvisionDeviceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### NetworkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.panorama_classes.NetworkPayloadUnion]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ProvisionDeviceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterPackageVersionRequest

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


# RemoveApplicationInstanceRequest

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# ReportedRuntimeContextState

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


# S3Location

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]


# SignalApplicationInstanceNodeInstancesRequest

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### NodeSignals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.panorama_classes.NodeSignal]
- **Required**: Yes


# SignalApplicationInstanceNodeInstancesResponse

### ApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


# StaticIpConnectionInfo

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


# StaticIpConnectionInfoOutput

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


# StorageLocation

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


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceMetadataRequest

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDeviceMetadataResponse

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.panorama_classes.ResponseMetadata'>
- **Required**: Yes


