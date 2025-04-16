# Lightsail Classes

# AccessKey

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUsed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AccessKeyLastUsed]


# AccessKeyLastUsed

### lastUsedDate
- **Type**: typing.Optional[datetime.datetime]

### region
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# AccessRules

### getObject
- **Type**: typing.Optional[typing.Literal['private', 'public']]

### allowPublicOverrides
- **Type**: typing.Optional[bool]


# AccountLevelBpaSync

### status
- **Type**: typing.Optional[typing.Literal['Defaulted', 'Failed', 'InSync', 'NeverSynced']]

### lastSyncedAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[typing.Literal['DEFAULTED_FOR_SLR_MISSING', 'DEFAULTED_FOR_SLR_MISSING_ON_HOLD', 'SYNC_ON_HOLD', 'Unknown']]

### bpaImpactsLightsail
- **Type**: typing.Optional[bool]


# AddOn

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### snapshotTimeOfDay
- **Type**: typing.Optional[str]

### nextSnapshotTimeOfDay
- **Type**: typing.Optional[str]

### threshold
- **Type**: typing.Optional[str]

### duration
- **Type**: typing.Optional[str]


# AddOnRequest

### addOnType
- **Type**: typing.Literal['AutoSnapshot', 'StopInstanceOnIdle']
- **Required**: Yes

### autoSnapshotAddOnRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AutoSnapshotAddOnRequest]

### stopInstanceOnIdleRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.StopInstanceOnIdleRequest]


# Alarm

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### supportCode
- **Type**: typing.Optional[str]

### monitoredResourceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.MonitoredResourceInfo]

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']]

### evaluationPeriods
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[int]

### threshold
- **Type**: typing.Optional[float]

### datapointsToAlarm
- **Type**: typing.Optional[int]

### treatMissingData
- **Type**: typing.Optional[typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']]

### statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]

### metricName
- **Type**: typing.Optional[typing.Literal['BurstCapacityPercentage', 'BurstCapacityTime', 'CPUUtilization', 'ClientTLSNegotiationErrorCount', 'DatabaseConnections', 'DiskQueueDepth', 'FreeStorageSpace', 'HTTPCode_Instance_2XX_Count', 'HTTPCode_Instance_3XX_Count', 'HTTPCode_Instance_4XX_Count', 'HTTPCode_Instance_5XX_Count', 'HTTPCode_LB_4XX_Count', 'HTTPCode_LB_5XX_Count', 'HealthyHostCount', 'InstanceResponseTime', 'NetworkIn', 'NetworkOut', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'RejectedConnectionCount', 'RequestCount', 'StatusCheckFailed', 'StatusCheckFailed_Instance', 'StatusCheckFailed_System', 'UnhealthyHostCount']]

### state
- **Type**: typing.Optional[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]

### unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### contactProtocols
- **Type**: typing.Optional[typing.List[typing.Literal['Email', 'SMS']]]

### notificationTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]]

### notificationEnabled
- **Type**: typing.Optional[bool]


# AllocateStaticIpRequest

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# AllocateStaticIpResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# AttachCertificateToDistributionRequest

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachCertificateToDistributionResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# AttachDiskRequest

### diskName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### diskPath
- **Type**: <class 'str'>
- **Required**: Yes

### autoMounting
- **Type**: typing.Optional[bool]


# AttachDiskResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# AttachInstancesToLoadBalancerRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AttachInstancesToLoadBalancerResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# AttachLoadBalancerTlsCertificateRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachLoadBalancerTlsCertificateResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# AttachStaticIpRequest

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachStaticIpResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# AttachedDisk

### path
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[int]


# AutoSnapshotAddOnRequest

### snapshotTimeOfDay
- **Type**: typing.Optional[str]


# AutoSnapshotDetails

### date
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'NotFound', 'Success']]

### fromAttachedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AttachedDisk]]


# AvailabilityZone

### zoneName
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blueprint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Bucket

### resourceType
- **Type**: typing.Optional[str]

### accessRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AccessRules]

### arn
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### url
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### name
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### objectVersioning
- **Type**: typing.Optional[str]

### ableToUpdateBundle
- **Type**: typing.Optional[bool]

### readonlyAccessAccounts
- **Type**: typing.Optional[typing.List[str]]

### resourcesReceivingAccess
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ResourceReceivingAccess]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.BucketState]

### accessLogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.BucketAccessLogConfig]


# BucketAccessLogConfig

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### destination
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# BucketBundle

### bundleId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[float]

### storagePerMonthInGb
- **Type**: typing.Optional[int]

### transferPerMonthInGb
- **Type**: typing.Optional[int]

### isActive
- **Type**: typing.Optional[bool]


# BucketState

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# Bundle

### price
- **Type**: typing.Optional[float]

### cpuCount
- **Type**: typing.Optional[int]

### diskSizeInGb
- **Type**: typing.Optional[int]

### bundleId
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### isActive
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### power
- **Type**: typing.Optional[int]

### ramSizeInGb
- **Type**: typing.Optional[float]

### transferPerMonthInGb
- **Type**: typing.Optional[int]

### supportedPlatforms
- **Type**: typing.Optional[typing.List[typing.Literal['LINUX_UNIX', 'WINDOWS']]]

### supportedAppCategories
- **Type**: typing.Optional[typing.List[typing.Literal['LfR']]]

### publicIpv4AddressCount
- **Type**: typing.Optional[int]


# CacheBehavior

### behavior
- **Type**: typing.Optional[typing.Literal['cache', 'dont-cache']]


# CacheBehaviorPerPath

### path
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[typing.Literal['cache', 'dont-cache']]


# CacheSettings

### defaultTTL
- **Type**: typing.Optional[int]

### minimumTTL
- **Type**: typing.Optional[int]

### maximumTTL
- **Type**: typing.Optional[int]

### allowedHTTPMethods
- **Type**: typing.Optional[str]

### cachedHTTPMethods
- **Type**: typing.Optional[str]

### forwardedCookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CookieObject]

### forwardedHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.HeaderObject]

### forwardedQueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.QueryStringObject]


# CacheSettingsOutput

### defaultTTL
- **Type**: typing.Optional[int]

### minimumTTL
- **Type**: typing.Optional[int]

### maximumTTL
- **Type**: typing.Optional[int]

### allowedHTTPMethods
- **Type**: typing.Optional[str]

### cachedHTTPMethods
- **Type**: typing.Optional[str]

### forwardedCookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CookieObjectOutput]

### forwardedHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.HeaderObjectOutput]

### forwardedQueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.QueryStringObjectOutput]


# CacheSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Certificate

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]

### serialNumber
- **Type**: typing.Optional[str]

### subjectAlternativeNames
- **Type**: typing.Optional[typing.List[str]]

### domainValidationRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainValidationRecord]]

### requestFailureReason
- **Type**: typing.Optional[str]

### inUseResourceCount
- **Type**: typing.Optional[int]

### keyAlgorithm
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### issuedAt
- **Type**: typing.Optional[datetime.datetime]

### issuerCA
- **Type**: typing.Optional[str]

### notBefore
- **Type**: typing.Optional[datetime.datetime]

### notAfter
- **Type**: typing.Optional[datetime.datetime]

### eligibleToRenew
- **Type**: typing.Optional[str]

### renewalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RenewalSummary]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### revocationReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### supportCode
- **Type**: typing.Optional[str]


# CertificateSummary

### certificateArn
- **Type**: typing.Optional[str]

### certificateName
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### certificateDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Certificate]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CloseInstancePublicPortsRequest

### portInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.PortInfo'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# CloseInstancePublicPortsResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CloudFormationStackRecord

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Started', 'Succeeded']]

### sourceInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CloudFormationStackRecordSourceInfo]]

### destinationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DestinationInfo]


# CloudFormationStackRecordSourceInfo

### resourceType
- **Type**: typing.Optional[typing.Literal['ExportSnapshotRecord']]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# ContactMethod

### contactEndpoint
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Invalid', 'PendingVerification', 'Valid']]

### protocol
- **Type**: typing.Optional[typing.Literal['Email', 'SMS']]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### supportCode
- **Type**: typing.Optional[str]


# Container

### image
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ports
- **Type**: typing.Optional[typing.Mapping[str, typing.Literal['HTTP', 'HTTPS', 'TCP', 'UDP']]]


# ContainerImage

### image
- **Type**: typing.Optional[str]

### digest
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# ContainerOutput

### image
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ports
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['HTTP', 'HTTPS', 'TCP', 'UDP']]]


# ContainerService

### containerServiceName
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### power
- **Type**: typing.Optional[typing.Literal['large', 'medium', 'micro', 'nano', 'small', 'xlarge']]

### powerId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['DELETING', 'DEPLOYING', 'DISABLED', 'PENDING', 'READY', 'RUNNING', 'UPDATING']]

### stateDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceStateDetail]

### scale
- **Type**: typing.Optional[int]

### currentDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeployment]

### nextDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeployment]

### isDisabled
- **Type**: typing.Optional[bool]

### principalArn
- **Type**: typing.Optional[str]

### privateDomainName
- **Type**: typing.Optional[str]

### publicDomainNames
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### url
- **Type**: typing.Optional[str]

### privateRegistryAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PrivateRegistryAccess]


# ContainerServiceDeployment

### version
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'FAILED', 'INACTIVE']]

### containers
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lightsail_classes.ContainerOutput]]

### publicEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceEndpoint]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# ContainerServiceDeploymentRequest

### containers
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lightsail_classes.ContainerUnion]]

### publicEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.EndpointRequest]


# ContainerServiceECRImagePullerRole

### isActive
- **Type**: typing.Optional[bool]

### principalArn
- **Type**: typing.Optional[str]


# ContainerServiceECRImagePullerRoleRequest

### isActive
- **Type**: typing.Optional[bool]


# ContainerServiceEndpoint

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceHealthCheckConfig]


# ContainerServiceHealthCheckConfig

### healthyThreshold
- **Type**: typing.Optional[int]

### unhealthyThreshold
- **Type**: typing.Optional[int]

### timeoutSeconds
- **Type**: typing.Optional[int]

### intervalSeconds
- **Type**: typing.Optional[int]

### path
- **Type**: typing.Optional[str]

### successCodes
- **Type**: typing.Optional[str]


# ContainerServiceLogEvent

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# ContainerServicePower

### powerId
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[float]

### cpuCount
- **Type**: typing.Optional[float]

### ramSizeInGb
- **Type**: typing.Optional[float]

### name
- **Type**: typing.Optional[str]

### isActive
- **Type**: typing.Optional[bool]


# ContainerServiceRegistryLogin

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### registry
- **Type**: typing.Optional[str]


# ContainerServiceStateDetail

### code
- **Type**: typing.Optional[typing.Literal['ACTIVATING_DEPLOYMENT', 'CERTIFICATE_LIMIT_EXCEEDED', 'CREATING_DEPLOYMENT', 'CREATING_NETWORK_INFRASTRUCTURE', 'CREATING_SYSTEM_RESOURCES', 'EVALUATING_HEALTH_CHECK', 'PROVISIONING_CERTIFICATE', 'PROVISIONING_SERVICE', 'UNKNOWN_ERROR']]

### message
- **Type**: typing.Optional[str]


# ContainerServicesListResult

### containerServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerService]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# ContainerUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CookieObject

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### cookiesAllowList
- **Type**: typing.Optional[typing.Sequence[str]]


# CookieObjectOutput

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### cookiesAllowList
- **Type**: typing.Optional[typing.List[str]]


# CopySnapshotRequest

### targetSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRegion
- **Type**: typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
- **Required**: Yes

### sourceSnapshotName
- **Type**: typing.Optional[str]

### sourceResourceName
- **Type**: typing.Optional[str]

### restoreDate
- **Type**: typing.Optional[str]

### useLatestRestorableAutoSnapshot
- **Type**: typing.Optional[bool]


# CopySnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CostEstimate

### usageType
- **Type**: typing.Optional[str]

### resultsByTime
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.EstimateByTime]]


# CreateBucketAccessKeyRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBucketAccessKeyResult

### accessKey
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.AccessKey'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBucketRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### enableObjectVersioning
- **Type**: typing.Optional[bool]


# CreateBucketResult

### bucket
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Bucket'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCertificateRequest

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateCertificateResult

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.CertificateSummary'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCloudFormationStackRequest

### instances
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.InstanceEntry]
- **Required**: Yes


# CreateCloudFormationStackResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContactMethodRequest

### protocol
- **Type**: typing.Literal['Email', 'SMS']
- **Required**: Yes

### contactEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# CreateContactMethodResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContainerServiceDeploymentRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### containers
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lightsail_classes.ContainerUnion]]

### publicEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.EndpointRequest]


# CreateContainerServiceDeploymentResult

### containerService
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerService'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContainerServiceRegistryLoginResult

### registryLogin
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceRegistryLogin'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContainerServiceRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### power
- **Type**: typing.Literal['large', 'medium', 'micro', 'nano', 'small', 'xlarge']
- **Required**: Yes

### scale
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### publicDomainNames
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### deployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeploymentRequest]

### privateRegistryAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PrivateRegistryAccessRequest]


# CreateContainerServiceResult

### containerService
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerService'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDiskFromSnapshotRequest

### diskName
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### sizeInGb
- **Type**: <class 'int'>
- **Required**: Yes

### diskSnapshotName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequest]]

### sourceDiskName
- **Type**: typing.Optional[str]

### restoreDate
- **Type**: typing.Optional[str]

### useLatestRestorableAutoSnapshot
- **Type**: typing.Optional[bool]


# CreateDiskFromSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDiskRequest

### diskName
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### sizeInGb
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequest]]


# CreateDiskResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDiskSnapshotRequest

### diskSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### diskName
- **Type**: typing.Optional[str]

### instanceName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateDiskSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDistributionRequest

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InputOrigin'>
- **Required**: Yes

### defaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.CacheBehavior'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### cacheBehaviorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheSettingsUnion]

### cacheBehaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorPerPath]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### certificateName
- **Type**: typing.Optional[str]

### viewerMinimumTlsProtocolVersion
- **Type**: typing.Optional[typing.Literal['TLSv1.1_2016', 'TLSv1.2_2018', 'TLSv1.2_2019', 'TLSv1.2_2021']]


# CreateDistributionResult

### distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.LightsailDistribution'>
- **Required**: Yes

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainEntryRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryUnion'>
- **Required**: Yes


# CreateDomainEntryResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateDomainResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGUISessionAccessDetailsRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGUISessionAccessDetailsResult

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['failedInstanceCreation', 'failedStartingGUISession', 'failedStoppingGUISession', 'notStarted', 'settingUpInstance', 'startExpired', 'started', 'starting', 'stopped', 'stopping']
- **Required**: Yes

### percentageComplete
- **Type**: <class 'int'>
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Session]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceSnapshotRequest

### instanceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateInstanceSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstancesFromSnapshotRequest

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### attachedDiskMapping
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.DiskMap]]]

### instanceSnapshotName
- **Type**: typing.Optional[str]

### userData
- **Type**: typing.Optional[str]

### keyPairName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequest]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### sourceInstanceName
- **Type**: typing.Optional[str]

### restoreDate
- **Type**: typing.Optional[str]

### useLatestRestorableAutoSnapshot
- **Type**: typing.Optional[bool]


# CreateInstancesFromSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstancesRequest

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### blueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### customImageName
- **Type**: typing.Optional[str]

### userData
- **Type**: typing.Optional[str]

### keyPairName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequest]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]


# CreateInstancesResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeyPairRequest

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateKeyPairResult

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.KeyPair'>
- **Required**: Yes

### publicKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes

### privateKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoadBalancerRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### instancePort
- **Type**: <class 'int'>
- **Required**: Yes

### healthCheckPath
- **Type**: typing.Optional[str]

### certificateName
- **Type**: typing.Optional[str]

### certificateDomainName
- **Type**: typing.Optional[str]

### certificateAlternativeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### tlsPolicyName
- **Type**: typing.Optional[str]


# CreateLoadBalancerResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoadBalancerTlsCertificateRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateAlternativeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateLoadBalancerTlsCertificateResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRelationalDatabaseFromSnapshotRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: typing.Optional[str]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### relationalDatabaseSnapshotName
- **Type**: typing.Optional[str]

### relationalDatabaseBundleId
- **Type**: typing.Optional[str]

### sourceRelationalDatabaseName
- **Type**: typing.Optional[str]

### restoreTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Timestamp]

### useLatestRestorableTime
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateRelationalDatabaseFromSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### relationalDatabaseBlueprintId
- **Type**: <class 'str'>
- **Required**: Yes

### relationalDatabaseBundleId
- **Type**: <class 'str'>
- **Required**: Yes

### masterDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### masterUsername
- **Type**: <class 'str'>
- **Required**: Yes

### availabilityZone
- **Type**: typing.Optional[str]

### masterUserPassword
- **Type**: typing.Optional[str]

### preferredBackupWindow
- **Type**: typing.Optional[str]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateRelationalDatabaseResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRelationalDatabaseSnapshotRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### relationalDatabaseSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]


# CreateRelationalDatabaseSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAlarmRequest

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAlarmResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAutoSnapshotRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### date
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAutoSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBucketAccessKeyRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketAccessKeyResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBucketRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteBucketResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCertificateRequest

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteContactMethodRequest

### protocol
- **Type**: typing.Literal['Email', 'SMS']
- **Required**: Yes


# DeleteContactMethodResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteContainerImageRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### image
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerServiceRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDiskRequest

### diskName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDeleteAddOns
- **Type**: typing.Optional[bool]


# DeleteDiskResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDiskSnapshotRequest

### diskSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDiskSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDistributionRequest

### distributionName
- **Type**: typing.Optional[str]


# DeleteDistributionResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainEntryRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryUnion'>
- **Required**: Yes


# DeleteDomainEntryResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInstanceRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDeleteAddOns
- **Type**: typing.Optional[bool]


# DeleteInstanceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteInstanceSnapshotRequest

### instanceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteKeyPairRequest

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedFingerprint
- **Type**: typing.Optional[str]


# DeleteKeyPairResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteKnownHostKeysRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnownHostKeysResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLoadBalancerRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLoadBalancerTlsCertificateRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteLoadBalancerTlsCertificateResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### skipFinalSnapshot
- **Type**: typing.Optional[bool]

### finalRelationalDatabaseSnapshotName
- **Type**: typing.Optional[str]


# DeleteRelationalDatabaseResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRelationalDatabaseSnapshotRequest

### relationalDatabaseSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRelationalDatabaseSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DetachCertificateFromDistributionRequest

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachCertificateFromDistributionResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DetachDiskRequest

### diskName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachDiskResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DetachInstancesFromLoadBalancerRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DetachInstancesFromLoadBalancerResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DetachStaticIpRequest

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachStaticIpResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# DisableAddOnRequest

### addOnType
- **Type**: typing.Literal['AutoSnapshot', 'StopInstanceOnIdle']
- **Required**: Yes

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DisableAddOnResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# Disk

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### addOns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AddOn]]

### sizeInGb
- **Type**: typing.Optional[int]

### isSystemDisk
- **Type**: typing.Optional[bool]

### iops
- **Type**: typing.Optional[int]

### path
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['available', 'error', 'in-use', 'pending', 'unknown']]

### attachedTo
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]

### attachmentState
- **Type**: typing.Optional[str]

### gbInUse
- **Type**: typing.Optional[int]

### autoMountStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Mounted', 'NotMounted', 'Pending']]


# DiskInfo

### name
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[int]

### isSystemDisk
- **Type**: typing.Optional[bool]


# DiskMap

### originalDiskPath
- **Type**: typing.Optional[str]

### newDiskName
- **Type**: typing.Optional[str]


# DiskSnapshot

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### sizeInGb
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[typing.Literal['completed', 'error', 'pending', 'unknown']]

### progress
- **Type**: typing.Optional[str]

### fromDiskName
- **Type**: typing.Optional[str]

### fromDiskArn
- **Type**: typing.Optional[str]

### fromInstanceName
- **Type**: typing.Optional[str]

### fromInstanceArn
- **Type**: typing.Optional[str]

### isFromAutoSnapshot
- **Type**: typing.Optional[bool]


# DiskSnapshotInfo

### sizeInGb
- **Type**: typing.Optional[int]


# DistributionBundle

### bundleId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[float]

### transferPerMonthInGb
- **Type**: typing.Optional[int]

### isActive
- **Type**: typing.Optional[bool]


# DnsRecordCreationState

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# Domain

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### domainEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryOutput]]

### registeredDomainDelegationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RegisteredDomainDelegationInfo]


# DomainEntryOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainEntryUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainValidationRecord

### domainName
- **Type**: typing.Optional[str]

### resourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceRecord]

### dnsRecordCreationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DnsRecordCreationState]

### validationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]


# DownloadDefaultKeyPairResult

### publicKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes

### privateKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# EnableAddOnRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### addOnRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequest'>
- **Required**: Yes


# EnableAddOnResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointRequest

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### containerPort
- **Type**: <class 'int'>
- **Required**: Yes

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceHealthCheckConfig]


# EstimateByTime

### usageCost
- **Type**: typing.Optional[float]

### pricingUnit
- **Type**: typing.Optional[typing.Literal['Bundles', 'GB', 'GB-Mo', 'Hrs', 'Queries']]

### unit
- **Type**: typing.Optional[float]

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### timePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.TimePeriod]


# ExportSnapshotRecord

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Started', 'Succeeded']]

### sourceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ExportSnapshotRecordSourceInfo]

### destinationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DestinationInfo]


# ExportSnapshotRecordSourceInfo

### resourceType
- **Type**: typing.Optional[typing.Literal['DiskSnapshot', 'InstanceSnapshot']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### fromResourceName
- **Type**: typing.Optional[str]

### fromResourceArn
- **Type**: typing.Optional[str]

### instanceSnapshotInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceSnapshotInfo]

### diskSnapshotInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DiskSnapshotInfo]


# ExportSnapshotRequest

### sourceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# ExportSnapshotResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetActiveNamesRequest

### pageToken
- **Type**: typing.Optional[str]


# GetActiveNamesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetActiveNamesResult

### activeNames
- **Type**: typing.List[str]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetAlarmsRequest

### alarmName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]

### monitoredResourceName
- **Type**: typing.Optional[str]


# GetAlarmsResult

### alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Alarm]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetAutoSnapshotsRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAutoSnapshotsResult

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']
- **Required**: Yes

### autoSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AutoSnapshotDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlueprintsRequest

### includeInactive
- **Type**: typing.Optional[bool]

### pageToken
- **Type**: typing.Optional[str]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]


# GetBlueprintsRequestPaginate

### includeInactive
- **Type**: typing.Optional[bool]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetBlueprintsResult

### blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Blueprint]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketAccessKeysRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketAccessKeysResult

### accessKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AccessKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketBundlesRequest

### includeInactive
- **Type**: typing.Optional[bool]


# GetBucketBundlesResult

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.BucketBundle]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketMetricDataRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['BucketSizeBytes', 'NumberOfObjects']
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes


# GetBucketMetricDataResult

### metricName
- **Type**: typing.Literal['BucketSizeBytes', 'NumberOfObjects']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketsRequest

### bucketName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]

### includeConnectedResources
- **Type**: typing.Optional[bool]


# GetBucketsResult

### buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Bucket]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountLevelBpaSync
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.AccountLevelBpaSync'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetBundlesRequest

### includeInactive
- **Type**: typing.Optional[bool]

### pageToken
- **Type**: typing.Optional[str]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]


# GetBundlesRequestPaginate

### includeInactive
- **Type**: typing.Optional[bool]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetBundlesResult

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Bundle]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetCertificatesRequest

### certificateStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]]

### includeCertificateDetails
- **Type**: typing.Optional[bool]

### certificateName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]


# GetCertificatesResult

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CertificateSummary]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetCloudFormationStackRecordsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetCloudFormationStackRecordsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetCloudFormationStackRecordsResult

### cloudFormationStackRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CloudFormationStackRecord]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContactMethodsRequest

### protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Email', 'SMS']]]


# GetContactMethodsResult

### contactMethods
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContactMethod]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerAPIMetadataResult

### metadata
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerImagesRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerImagesResult

### containerImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerImage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerLogRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Timestamp]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Timestamp]

### filterPattern
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]


# GetContainerLogResult

### logEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceLogEvent]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerServiceDeploymentsRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerServiceDeploymentsResult

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerServiceMetricDataRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['CPUUtilization', 'MemoryUtilization']
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetContainerServiceMetricDataResult

### metricName
- **Type**: typing.Literal['CPUUtilization', 'MemoryUtilization']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerServicePowersResult

### powers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServicePower]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetContainerServicesRequest

### serviceName
- **Type**: typing.Optional[str]


# GetCostEstimateRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes


# GetCostEstimateResult

### resourcesBudgetEstimate
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ResourceBudgetEstimate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDiskRequest

### diskName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDiskResult

### disk
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Disk'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDiskSnapshotRequest

### diskSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDiskSnapshotResult

### diskSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DiskSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDiskSnapshotsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetDiskSnapshotsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetDiskSnapshotsResult

### diskSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskSnapshot]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDisksRequest

### pageToken
- **Type**: typing.Optional[str]


# GetDisksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetDisksResult

### disks
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Disk]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionBundlesResult

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DistributionBundle]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionLatestCacheResetRequest

### distributionName
- **Type**: typing.Optional[str]


# GetDistributionLatestCacheResetResult

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionMetricDataRequest

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['BytesDownloaded', 'BytesUploaded', 'Http4xxErrorRate', 'Http5xxErrorRate', 'Requests', 'TotalErrorRate']
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetDistributionMetricDataResult

### metricName
- **Type**: typing.Literal['BytesDownloaded', 'BytesUploaded', 'Http4xxErrorRate', 'Http5xxErrorRate', 'Requests', 'TotalErrorRate']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionsRequest

### distributionName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]


# GetDistributionsResult

### distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LightsailDistribution]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainResult

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Domain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetDomainsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetDomainsResult

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Domain]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetExportSnapshotRecordsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetExportSnapshotRecordsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetExportSnapshotRecordsResult

### exportSnapshotRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ExportSnapshotRecord]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceAccessDetailsRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### protocol
- **Type**: typing.Optional[typing.Literal['rdp', 'ssh']]


# GetInstanceAccessDetailsResult

### accessDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceAccessDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceMetricDataRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['BurstCapacityPercentage', 'BurstCapacityTime', 'CPUUtilization', 'MetadataNoToken', 'NetworkIn', 'NetworkOut', 'StatusCheckFailed', 'StatusCheckFailed_Instance', 'StatusCheckFailed_System']
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetInstanceMetricDataResult

### metricName
- **Type**: typing.Literal['BurstCapacityPercentage', 'BurstCapacityTime', 'CPUUtilization', 'MetadataNoToken', 'NetworkIn', 'NetworkOut', 'StatusCheckFailed', 'StatusCheckFailed_Instance', 'StatusCheckFailed_System']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstancePortStatesRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstancePortStatesResult

### portStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstancePortState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceResult

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Instance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceSnapshotRequest

### instanceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceSnapshotResult

### instanceSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceSnapshotsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetInstanceSnapshotsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetInstanceSnapshotsResult

### instanceSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstanceSnapshot]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceStateRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceStateResult

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceState'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstancesRequest

### pageToken
- **Type**: typing.Optional[str]


# GetInstancesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetInstancesResult

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Instance]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyPairRequest

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyPairResult

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.KeyPair'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyPairsRequest

### pageToken
- **Type**: typing.Optional[str]

### includeDefaultKeyPair
- **Type**: typing.Optional[bool]


# GetKeyPairsRequestPaginate

### includeDefaultKeyPair
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetKeyPairsResult

### keyPairs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.KeyPair]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoadBalancerMetricDataRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['ClientTLSNegotiationErrorCount', 'HTTPCode_Instance_2XX_Count', 'HTTPCode_Instance_3XX_Count', 'HTTPCode_Instance_4XX_Count', 'HTTPCode_Instance_5XX_Count', 'HTTPCode_LB_4XX_Count', 'HTTPCode_LB_5XX_Count', 'HealthyHostCount', 'InstanceResponseTime', 'RejectedConnectionCount', 'RequestCount', 'UnhealthyHostCount']
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetLoadBalancerMetricDataResult

### metricName
- **Type**: typing.Literal['ClientTLSNegotiationErrorCount', 'HTTPCode_Instance_2XX_Count', 'HTTPCode_Instance_3XX_Count', 'HTTPCode_Instance_4XX_Count', 'HTTPCode_Instance_5XX_Count', 'HTTPCode_LB_4XX_Count', 'HTTPCode_LB_5XX_Count', 'HealthyHostCount', 'InstanceResponseTime', 'RejectedConnectionCount', 'RequestCount', 'UnhealthyHostCount']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoadBalancerRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoadBalancerResult

### loadBalancer
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoadBalancerTlsCertificatesRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoadBalancerTlsCertificatesResult

### tlsCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoadBalancerTlsPoliciesRequest

### pageToken
- **Type**: typing.Optional[str]


# GetLoadBalancerTlsPoliciesResult

### tlsPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsPolicy]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoadBalancersRequest

### pageToken
- **Type**: typing.Optional[str]


# GetLoadBalancersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetLoadBalancersResult

### loadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancer]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetOperationRequest

### operationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetOperationsForResourceRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### pageToken
- **Type**: typing.Optional[str]


# GetOperationsForResourceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### nextPageCount
- **Type**: <class 'str'>
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetOperationsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetOperationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetOperationsResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegionsRequest

### includeAvailabilityZones
- **Type**: typing.Optional[bool]

### includeRelationalDatabaseAvailabilityZones
- **Type**: typing.Optional[bool]


# GetRegionsResult

### regions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Region]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseBlueprintsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseBlueprintsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetRelationalDatabaseBlueprintsResult

### blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseBlueprint]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseBundlesRequest

### pageToken
- **Type**: typing.Optional[str]

### includeInactive
- **Type**: typing.Optional[bool]


# GetRelationalDatabaseBundlesRequestPaginate

### includeInactive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetRelationalDatabaseBundlesResult

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseBundle]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseEventsRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: typing.Optional[int]

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseEventsRequestPaginate

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetRelationalDatabaseEventsResult

### relationalDatabaseEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseEvent]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseLogEventsRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Timestamp]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Timestamp]

### startFromHead
- **Type**: typing.Optional[bool]

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseLogEventsResult

### resourceLogEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LogEvent]
- **Required**: Yes

### nextBackwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextForwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseLogStreamsRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelationalDatabaseLogStreamsResult

### logStreams
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseMasterUserPasswordRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### passwordVersion
- **Type**: typing.Optional[typing.Literal['CURRENT', 'PENDING', 'PREVIOUS']]


# GetRelationalDatabaseMasterUserPasswordResult

### masterUserPassword
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseMetricDataRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['CPUUtilization', 'DatabaseConnections', 'DiskQueueDepth', 'FreeStorageSpace', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput']
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Timestamp'>
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetRelationalDatabaseMetricDataResult

### metricName
- **Type**: typing.Literal['CPUUtilization', 'DatabaseConnections', 'DiskQueueDepth', 'FreeStorageSpace', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseParametersRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseParametersRequestPaginate

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetRelationalDatabaseParametersResult

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseParameter]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelationalDatabaseResult

### relationalDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseSnapshotRequest

### relationalDatabaseSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelationalDatabaseSnapshotResult

### relationalDatabaseSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseSnapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabaseSnapshotsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseSnapshotsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetRelationalDatabaseSnapshotsResult

### relationalDatabaseSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseSnapshot]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelationalDatabasesRequest

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabasesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetRelationalDatabasesResult

### relationalDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabase]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetSetupHistoryRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### pageToken
- **Type**: typing.Optional[str]


# GetSetupHistoryResult

### setupHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.SetupHistory]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetStaticIpRequest

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStaticIpResult

### staticIp
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.StaticIp'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# GetStaticIpsRequest

### pageToken
- **Type**: typing.Optional[str]


# GetStaticIpsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfig]


# GetStaticIpsResult

### staticIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.StaticIp]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# HeaderObject

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### headersAllowList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Authorization', 'CloudFront-Forwarded-Proto', 'CloudFront-Is-Desktop-Viewer', 'CloudFront-Is-Mobile-Viewer', 'CloudFront-Is-SmartTV-Viewer', 'CloudFront-Is-Tablet-Viewer', 'CloudFront-Viewer-Country', 'Host', 'Origin', 'Referer']]]


# HeaderObjectOutput

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### headersAllowList
- **Type**: typing.Optional[typing.List[typing.Literal['Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Authorization', 'CloudFront-Forwarded-Proto', 'CloudFront-Is-Desktop-Viewer', 'CloudFront-Is-Mobile-Viewer', 'CloudFront-Is-SmartTV-Viewer', 'CloudFront-Is-Tablet-Viewer', 'CloudFront-Viewer-Country', 'Host', 'Origin', 'Referer']]]


# HostKeyAttributes

### algorithm
- **Type**: typing.Optional[str]

### publicKey
- **Type**: typing.Optional[str]

### witnessedAt
- **Type**: typing.Optional[datetime.datetime]

### fingerprintSHA1
- **Type**: typing.Optional[str]

### fingerprintSHA256
- **Type**: typing.Optional[str]

### notValidBefore
- **Type**: typing.Optional[datetime.datetime]

### notValidAfter
- **Type**: typing.Optional[datetime.datetime]


# ImportKeyPairRequest

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes

### publicKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes


# ImportKeyPairResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# InputOrigin

### name
- **Type**: typing.Optional[str]

### regionName
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### protocolPolicy
- **Type**: typing.Optional[typing.Literal['http-only', 'https-only']]

### responseTimeout
- **Type**: typing.Optional[int]


# Instance

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### blueprintId
- **Type**: typing.Optional[str]

### blueprintName
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]

### addOns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AddOn]]

### isStaticIp
- **Type**: typing.Optional[bool]

### privateIpAddress
- **Type**: typing.Optional[str]

### publicIpAddress
- **Type**: typing.Optional[str]

### ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### hardware
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceHardware]

### networking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceNetworking]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceState]

### username
- **Type**: typing.Optional[str]

### sshKeyName
- **Type**: typing.Optional[str]

### metadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceMetadataOptions]


# InstanceAccessDetails

### certKey
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### ipAddress
- **Type**: typing.Optional[str]

### ipv6Addresses
- **Type**: typing.Optional[typing.List[str]]

### password
- **Type**: typing.Optional[str]

### passwordData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PasswordData]

### privateKey
- **Type**: typing.Optional[str]

### protocol
- **Type**: typing.Optional[typing.Literal['rdp', 'ssh']]

### instanceName
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]

### hostKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.HostKeyAttributes]]


# InstanceEntry

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceType
- **Type**: <class 'str'>
- **Required**: Yes

### portInfoSource
- **Type**: typing.Literal['CLOSED', 'DEFAULT', 'INSTANCE', 'NONE']
- **Required**: Yes

### availabilityZone
- **Type**: <class 'str'>
- **Required**: Yes

### userData
- **Type**: typing.Optional[str]


# InstanceHardware

### cpuCount
- **Type**: typing.Optional[int]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Disk]]

### ramSizeInGb
- **Type**: typing.Optional[float]


# InstanceHealthSummary

### instanceName
- **Type**: typing.Optional[str]

### instanceHealth
- **Type**: typing.Optional[typing.Literal['draining', 'healthy', 'initial', 'unavailable', 'unhealthy', 'unused']]

### instanceHealthReason
- **Type**: typing.Optional[typing.Literal['Instance.DeregistrationInProgress', 'Instance.FailedHealthChecks', 'Instance.InvalidState', 'Instance.IpUnusable', 'Instance.NotInUse', 'Instance.NotRegistered', 'Instance.ResponseCodeMismatch', 'Instance.Timeout', 'Lb.InitialHealthChecking', 'Lb.InternalError', 'Lb.RegistrationInProgress']]


# InstanceMetadataOptions

### state
- **Type**: typing.Optional[typing.Literal['applied', 'pending']]

### httpTokens
- **Type**: typing.Optional[typing.Literal['optional', 'required']]

### httpEndpoint
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### httpPutResponseHopLimit
- **Type**: typing.Optional[int]

### httpProtocolIpv6
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# InstanceNetworking

### monthlyTransfer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.MonthlyTransfer]

### ports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstancePortInfo]]


# InstancePortInfo

### fromPort
- **Type**: typing.Optional[int]

### toPort
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['all', 'icmp', 'icmpv6', 'tcp', 'udp']]

### accessFrom
- **Type**: typing.Optional[str]

### accessType
- **Type**: typing.Optional[typing.Literal['Private', 'Public']]

### commonName
- **Type**: typing.Optional[str]

### accessDirection
- **Type**: typing.Optional[typing.Literal['inbound', 'outbound']]

### cidrs
- **Type**: typing.Optional[typing.List[str]]

### ipv6Cidrs
- **Type**: typing.Optional[typing.List[str]]

### cidrListAliases
- **Type**: typing.Optional[typing.List[str]]


# InstancePortState

### fromPort
- **Type**: typing.Optional[int]

### toPort
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['all', 'icmp', 'icmpv6', 'tcp', 'udp']]

### state
- **Type**: typing.Optional[typing.Literal['closed', 'open']]

### cidrs
- **Type**: typing.Optional[typing.List[str]]

### ipv6Cidrs
- **Type**: typing.Optional[typing.List[str]]

### cidrListAliases
- **Type**: typing.Optional[typing.List[str]]


# InstanceSnapshot

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### state
- **Type**: typing.Optional[typing.Literal['available', 'error', 'pending']]

### progress
- **Type**: typing.Optional[str]

### fromAttachedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Disk]]

### fromInstanceName
- **Type**: typing.Optional[str]

### fromInstanceArn
- **Type**: typing.Optional[str]

### fromBlueprintId
- **Type**: typing.Optional[str]

### fromBundleId
- **Type**: typing.Optional[str]

### isFromAutoSnapshot
- **Type**: typing.Optional[bool]

### sizeInGb
- **Type**: typing.Optional[int]


# InstanceSnapshotInfo

### fromBundleId
- **Type**: typing.Optional[str]

### fromBlueprintId
- **Type**: typing.Optional[str]

### fromDiskInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskInfo]]


# InstanceState

### code
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]


# IsVpcPeeredResult

### isPeered
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# KeyPair

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### fingerprint
- **Type**: typing.Optional[str]


# LightsailDistribution

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### alternativeDomainNames
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[str]

### isEnabled
- **Type**: typing.Optional[bool]

### domainName
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]

### certificateName
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.Origin]

### originPublicDNS
- **Type**: typing.Optional[str]

### defaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehavior]

### cacheBehaviorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheSettingsOutput]

### cacheBehaviors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorPerPath]]

### ableToUpdateBundle
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### viewerMinimumTlsProtocolVersion
- **Type**: typing.Optional[str]


# LoadBalancer

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### dnsName
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['active', 'active_impaired', 'failed', 'provisioning', 'unknown']]

### protocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTP_HTTPS']]

### publicPorts
- **Type**: typing.Optional[typing.List[int]]

### healthCheckPath
- **Type**: typing.Optional[str]

### instancePort
- **Type**: typing.Optional[int]

### instanceHealthSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstanceHealthSummary]]

### tlsCertificateSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateSummary]]

### configurationOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['HealthCheckPath', 'HttpsRedirectionEnabled', 'SessionStickinessEnabled', 'SessionStickiness_LB_CookieDurationSeconds', 'TlsPolicyName'], str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### httpsRedirectionEnabled
- **Type**: typing.Optional[bool]

### tlsPolicyName
- **Type**: typing.Optional[str]


# LoadBalancerTlsCertificate

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### loadBalancerName
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'UNKNOWN', 'VALIDATION_TIMED_OUT']]

### domainName
- **Type**: typing.Optional[str]

### domainValidationRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateDomainValidationRecord]]

### failureReason
- **Type**: typing.Optional[typing.Literal['ADDITIONAL_VERIFICATION_REQUIRED', 'DOMAIN_NOT_ALLOWED', 'INVALID_PUBLIC_DOMAIN', 'NO_AVAILABLE_CONTACTS', 'OTHER']]

### issuedAt
- **Type**: typing.Optional[datetime.datetime]

### issuer
- **Type**: typing.Optional[str]

### keyAlgorithm
- **Type**: typing.Optional[str]

### notAfter
- **Type**: typing.Optional[datetime.datetime]

### notBefore
- **Type**: typing.Optional[datetime.datetime]

### renewalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateRenewalSummary]

### revocationReason
- **Type**: typing.Optional[typing.Literal['AFFILIATION_CHANGED', 'A_A_COMPROMISE', 'CA_COMPROMISE', 'CERTIFICATE_HOLD', 'CESSATION_OF_OPERATION', 'KEY_COMPROMISE', 'PRIVILEGE_WITHDRAWN', 'REMOVE_FROM_CRL', 'SUPERCEDED', 'UNSPECIFIED']]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### serial
- **Type**: typing.Optional[str]

### signatureAlgorithm
- **Type**: typing.Optional[str]

### subject
- **Type**: typing.Optional[str]

### subjectAlternativeNames
- **Type**: typing.Optional[typing.List[str]]


# LoadBalancerTlsCertificateDnsRecordCreationState

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# LoadBalancerTlsCertificateDomainValidationOption

### domainName
- **Type**: typing.Optional[str]

### validationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]


# LoadBalancerTlsCertificateDomainValidationRecord

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoadBalancerTlsCertificateRenewalSummary

### renewalStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_AUTO_RENEWAL', 'PENDING_VALIDATION', 'SUCCESS']]

### domainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateDomainValidationOption]]


# LoadBalancerTlsCertificateSummary

### name
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]


# LoadBalancerTlsPolicy

### name
- **Type**: typing.Optional[str]

### isDefault
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### protocols
- **Type**: typing.Optional[typing.List[str]]

### ciphers
- **Type**: typing.Optional[typing.List[str]]


# LogEvent

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# MetricDatapoint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MonitoredResourceInfo

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]


# MonthlyTransfer

### gbPerMonthAllocated
- **Type**: typing.Optional[int]


# NameServersUpdateState

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# OpenInstancePublicPortsRequest

### portInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.PortInfo'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# OpenInstancePublicPortsResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# Operation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Origin

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### regionName
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### protocolPolicy
- **Type**: typing.Optional[typing.Literal['http-only', 'https-only']]

### responseTimeout
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PasswordData

### ciphertext
- **Type**: typing.Optional[str]

### keyPairName
- **Type**: typing.Optional[str]


# PeerVpcResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# PendingMaintenanceAction

### action
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### currentApplyDate
- **Type**: typing.Optional[datetime.datetime]


# PendingModifiedRelationalDatabaseValues

### masterUserPassword
- **Type**: typing.Optional[str]

### engineVersion
- **Type**: typing.Optional[str]

### backupRetentionEnabled
- **Type**: typing.Optional[bool]


# PortInfo

### fromPort
- **Type**: typing.Optional[int]

### toPort
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['all', 'icmp', 'icmpv6', 'tcp', 'udp']]

### cidrs
- **Type**: typing.Optional[typing.Sequence[str]]

### ipv6Cidrs
- **Type**: typing.Optional[typing.Sequence[str]]

### cidrListAliases
- **Type**: typing.Optional[typing.Sequence[str]]


# PrivateRegistryAccess

### ecrImagePullerRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceECRImagePullerRole]


# PrivateRegistryAccessRequest

### ecrImagePullerRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceECRImagePullerRoleRequest]


# PutAlarmRequest

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['BurstCapacityPercentage', 'BurstCapacityTime', 'CPUUtilization', 'ClientTLSNegotiationErrorCount', 'DatabaseConnections', 'DiskQueueDepth', 'FreeStorageSpace', 'HTTPCode_Instance_2XX_Count', 'HTTPCode_Instance_3XX_Count', 'HTTPCode_Instance_4XX_Count', 'HTTPCode_Instance_5XX_Count', 'HTTPCode_LB_4XX_Count', 'HTTPCode_LB_5XX_Count', 'HealthyHostCount', 'InstanceResponseTime', 'NetworkIn', 'NetworkOut', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'RejectedConnectionCount', 'RequestCount', 'StatusCheckFailed', 'StatusCheckFailed_Instance', 'StatusCheckFailed_System', 'UnhealthyHostCount']
- **Required**: Yes

### monitoredResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### threshold
- **Type**: <class 'float'>
- **Required**: Yes

### evaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### datapointsToAlarm
- **Type**: typing.Optional[int]

### treatMissingData
- **Type**: typing.Optional[typing.Literal['breaching', 'ignore', 'missing', 'notBreaching']]

### contactProtocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Email', 'SMS']]]

### notificationTriggers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']]]

### notificationEnabled
- **Type**: typing.Optional[bool]


# PutAlarmResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# PutInstancePublicPortsRequest

### portInfos
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.PortInfo]
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# PutInstancePublicPortsResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# QueryStringObject

### option
- **Type**: typing.Optional[bool]

### queryStringsAllowList
- **Type**: typing.Optional[typing.Sequence[str]]


# QueryStringObjectOutput

### option
- **Type**: typing.Optional[bool]

### queryStringsAllowList
- **Type**: typing.Optional[typing.List[str]]


# R53HostedZoneDeletionState

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# RebootInstanceRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# RebootInstanceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# RebootRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RebootRelationalDatabaseResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# Region

### continentCode
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### availabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AvailabilityZone]]

### relationalDatabaseAvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AvailabilityZone]]


# RegisterContainerImageRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### label
- **Type**: <class 'str'>
- **Required**: Yes

### digest
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterContainerImageResult

### containerImage
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerImage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# RegisteredDomainDelegationInfo

### nameServersUpdateState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.NameServersUpdateState]

### r53HostedZoneDeletionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.R53HostedZoneDeletionState]


# RelationalDatabase

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### relationalDatabaseBlueprintId
- **Type**: typing.Optional[str]

### relationalDatabaseBundleId
- **Type**: typing.Optional[str]

### masterDatabaseName
- **Type**: typing.Optional[str]

### hardware
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseHardware]

### state
- **Type**: typing.Optional[str]

### secondaryAvailabilityZone
- **Type**: typing.Optional[str]

### backupRetentionEnabled
- **Type**: typing.Optional[bool]

### pendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PendingModifiedRelationalDatabaseValues]

### engine
- **Type**: typing.Optional[str]

### engineVersion
- **Type**: typing.Optional[str]

### latestRestorableTime
- **Type**: typing.Optional[datetime.datetime]

### masterUsername
- **Type**: typing.Optional[str]

### parameterApplyStatus
- **Type**: typing.Optional[str]

### preferredBackupWindow
- **Type**: typing.Optional[str]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### masterEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseEndpoint]

### pendingMaintenanceActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.PendingMaintenanceAction]]

### caCertificateIdentifier
- **Type**: typing.Optional[str]


# RelationalDatabaseBlueprint

### blueprintId
- **Type**: typing.Optional[str]

### engine
- **Type**: typing.Optional[typing.Literal['mysql']]

### engineVersion
- **Type**: typing.Optional[str]

### engineDescription
- **Type**: typing.Optional[str]

### engineVersionDescription
- **Type**: typing.Optional[str]

### isEngineDefault
- **Type**: typing.Optional[bool]


# RelationalDatabaseBundle

### bundleId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[float]

### ramSizeInGb
- **Type**: typing.Optional[float]

### diskSizeInGb
- **Type**: typing.Optional[int]

### transferPerMonthInGb
- **Type**: typing.Optional[int]

### cpuCount
- **Type**: typing.Optional[int]

### isEncrypted
- **Type**: typing.Optional[bool]

### isActive
- **Type**: typing.Optional[bool]


# RelationalDatabaseEndpoint

### port
- **Type**: typing.Optional[int]

### address
- **Type**: typing.Optional[str]


# RelationalDatabaseEvent

### resource
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]

### eventCategories
- **Type**: typing.Optional[typing.List[str]]


# RelationalDatabaseHardware

### cpuCount
- **Type**: typing.Optional[int]

### diskSizeInGb
- **Type**: typing.Optional[int]

### ramSizeInGb
- **Type**: typing.Optional[float]


# RelationalDatabaseParameter

### allowedValues
- **Type**: typing.Optional[str]

### applyMethod
- **Type**: typing.Optional[str]

### applyType
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### isModifiable
- **Type**: typing.Optional[bool]

### parameterName
- **Type**: typing.Optional[str]

### parameterValue
- **Type**: typing.Optional[str]


# RelationalDatabaseSnapshot

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Tag]]

### engine
- **Type**: typing.Optional[str]

### engineVersion
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[str]

### fromRelationalDatabaseName
- **Type**: typing.Optional[str]

### fromRelationalDatabaseArn
- **Type**: typing.Optional[str]

### fromRelationalDatabaseBundleId
- **Type**: typing.Optional[str]

### fromRelationalDatabaseBlueprintId
- **Type**: typing.Optional[str]


# ReleaseStaticIpRequest

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# ReleaseStaticIpResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# RenewalSummary

### domainValidationRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainValidationRecord]]

### renewalStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'PendingAutoRenewal', 'PendingValidation', 'Success']]

### renewalStatusReason
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ResetDistributionCacheRequest

### distributionName
- **Type**: typing.Optional[str]


# ResetDistributionCacheResult

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceBudgetEstimate

### resourceName
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### costEstimates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CostEstimate]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# ResourceLocation

### availabilityZone
- **Type**: typing.Optional[str]

### regionName
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]


# ResourceReceivingAccess

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]


# ResourceRecord

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SendContactMethodVerificationRequest

### protocol
- **Type**: typing.Literal['Email']
- **Required**: Yes


# SendContactMethodVerificationResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# Session

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### isPrimary
- **Type**: typing.Optional[bool]


# SetIpAddressTypeRequest

### resourceType
- **Type**: typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']
- **Required**: Yes

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddressType
- **Type**: typing.Literal['dualstack', 'ipv4', 'ipv6']
- **Required**: Yes

### acceptBundleUpdate
- **Type**: typing.Optional[bool]


# SetIpAddressTypeResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# SetResourceAccessForBucketRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### access
- **Type**: typing.Literal['allow', 'deny']
- **Required**: Yes


# SetResourceAccessForBucketResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# SetupExecutionDetails

### command
- **Type**: typing.Optional[str]

### dateTime
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['failed', 'inProgress', 'succeeded']]

### standardError
- **Type**: typing.Optional[str]

### standardOutput
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# SetupHistory

### operationId
- **Type**: typing.Optional[str]

### request
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.SetupRequest]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.SetupHistoryResource]

### executionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.SetupExecutionDetails]]

### status
- **Type**: typing.Optional[typing.Literal['failed', 'inProgress', 'succeeded']]


# SetupHistoryResource

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]


# SetupInstanceHttpsRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### domainNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### certificateProvider
- **Type**: typing.Literal['LetsEncrypt']
- **Required**: Yes


# SetupInstanceHttpsResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# SetupRequest

### instanceName
- **Type**: typing.Optional[str]

### domainNames
- **Type**: typing.Optional[typing.List[str]]

### certificateProvider
- **Type**: typing.Optional[typing.Literal['LetsEncrypt']]


# StartGUISessionRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# StartGUISessionResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# StartInstanceRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# StartInstanceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# StartRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# StartRelationalDatabaseResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# StaticIp

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocation]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### ipAddress
- **Type**: typing.Optional[str]

### attachedTo
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]


# StopGUISessionRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# StopGUISessionResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# StopInstanceOnIdleRequest

### threshold
- **Type**: typing.Optional[str]

### duration
- **Type**: typing.Optional[str]


# StopInstanceRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# StopInstanceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# StopRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### relationalDatabaseSnapshotName
- **Type**: typing.Optional[str]


# StopRelationalDatabaseResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.Tag]
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]


# TagResourceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# TestAlarmRequest

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']
- **Required**: Yes


# TestAlarmResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# TimePeriod

### start
- **Type**: typing.Optional[datetime.datetime]

### end
- **Type**: typing.Optional[datetime.datetime]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnpeerVpcResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]


# UntagResourceResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBucketBundleRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBucketBundleResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBucketRequest

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### accessRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AccessRules]

### versioning
- **Type**: typing.Optional[str]

### readonlyAccessAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### accessLogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.BucketAccessLogConfig]


# UpdateBucketResult

### bucket
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Bucket'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContainerServiceRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### power
- **Type**: typing.Optional[typing.Literal['large', 'medium', 'micro', 'nano', 'small', 'xlarge']]

### scale
- **Type**: typing.Optional[int]

### isDisabled
- **Type**: typing.Optional[bool]

### publicDomainNames
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### privateRegistryAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PrivateRegistryAccessRequest]


# UpdateContainerServiceResult

### containerService
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerService'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDistributionBundleRequest

### distributionName
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]


# UpdateDistributionBundleResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDistributionRequest

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InputOrigin]

### defaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehavior]

### cacheBehaviorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheSettingsUnion]

### cacheBehaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorPerPath]]

### isEnabled
- **Type**: typing.Optional[bool]

### viewerMinimumTlsProtocolVersion
- **Type**: typing.Optional[typing.Literal['TLSv1.1_2016', 'TLSv1.2_2018', 'TLSv1.2_2019', 'TLSv1.2_2021']]

### certificateName
- **Type**: typing.Optional[str]

### useDefaultCertificate
- **Type**: typing.Optional[bool]


# UpdateDistributionResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainEntryRequest

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryUnion'>
- **Required**: Yes


# UpdateDomainEntryResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInstanceMetadataOptionsRequest

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### httpTokens
- **Type**: typing.Optional[typing.Literal['optional', 'required']]

### httpEndpoint
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### httpPutResponseHopLimit
- **Type**: typing.Optional[int]

### httpProtocolIpv6
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# UpdateInstanceMetadataOptionsResult

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.Operation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLoadBalancerAttributeRequest

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### attributeName
- **Type**: typing.Literal['HealthCheckPath', 'HttpsRedirectionEnabled', 'SessionStickinessEnabled', 'SessionStickiness_LB_CookieDurationSeconds', 'TlsPolicyName']
- **Required**: Yes

### attributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateLoadBalancerAttributeResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRelationalDatabaseParametersRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseParameter]
- **Required**: Yes


# UpdateRelationalDatabaseParametersResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRelationalDatabaseRequest

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### masterUserPassword
- **Type**: typing.Optional[str]

### rotateMasterUserPassword
- **Type**: typing.Optional[bool]

### preferredBackupWindow
- **Type**: typing.Optional[str]

### preferredMaintenanceWindow
- **Type**: typing.Optional[str]

### enableBackupRetention
- **Type**: typing.Optional[bool]

### disableBackupRetention
- **Type**: typing.Optional[bool]

### publiclyAccessible
- **Type**: typing.Optional[bool]

### applyImmediately
- **Type**: typing.Optional[bool]

### caCertificateIdentifier
- **Type**: typing.Optional[str]

### relationalDatabaseBlueprintId
- **Type**: typing.Optional[str]


# UpdateRelationalDatabaseResult

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.Operation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadata'>
- **Required**: Yes


