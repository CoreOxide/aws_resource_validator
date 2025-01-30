# lightsail_classes

# AccessKeyLastUsedTypeDef

### lastUsedDate
- **Type**: typing.Optional[datetime.datetime]

### region
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]


# AccessKeyTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### secretAccessKey
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUsed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AccessKeyLastUsedTypeDef]


# AccessRulesTypeDef

### getObject
- **Type**: typing.Optional[typing.Literal['private', 'public']]

### allowPublicOverrides
- **Type**: typing.Optional[bool]


# AccountLevelBpaSyncTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Defaulted', 'Failed', 'InSync', 'NeverSynced']]

### lastSyncedAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[typing.Literal['DEFAULTED_FOR_SLR_MISSING', 'DEFAULTED_FOR_SLR_MISSING_ON_HOLD', 'SYNC_ON_HOLD', 'Unknown']]

### bpaImpactsLightsail
- **Type**: typing.Optional[bool]


# AddOnRequestTypeDef

### addOnType
- **Type**: typing.Literal['AutoSnapshot', 'StopInstanceOnIdle']
- **Required**: Yes

### autoSnapshotAddOnRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AutoSnapshotAddOnRequestTypeDef]

### stopInstanceOnIdleRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.StopInstanceOnIdleRequestTypeDef]


# AddOnTypeDef

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


# AlarmTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### supportCode
- **Type**: typing.Optional[str]

### monitoredResourceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.MonitoredResourceInfoTypeDef]

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


# AllocateStaticIpRequestRequestTypeDef

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# AllocateStaticIpResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachCertificateToDistributionRequestRequestTypeDef

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachCertificateToDistributionResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachDiskRequestRequestTypeDef

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


# AttachDiskResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachInstancesToLoadBalancerRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AttachInstancesToLoadBalancerResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachLoadBalancerTlsCertificateRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachLoadBalancerTlsCertificateResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachStaticIpRequestRequestTypeDef

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachStaticIpResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachedDiskTypeDef

### path
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[int]


# AutoSnapshotAddOnRequestTypeDef

### snapshotTimeOfDay
- **Type**: typing.Optional[str]


# AutoSnapshotDetailsTypeDef

### date
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'NotFound', 'Success']]

### fromAttachedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AttachedDiskTypeDef]]


# AvailabilityZoneTypeDef

### zoneName
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlueprintTypeDef

### blueprintId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### group
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['app', 'os']]

### description
- **Type**: typing.Optional[str]

### isActive
- **Type**: typing.Optional[bool]

### minPower
- **Type**: typing.Optional[int]

### version
- **Type**: typing.Optional[str]

### versionCode
- **Type**: typing.Optional[str]

### productUrl
- **Type**: typing.Optional[str]

### licenseUrl
- **Type**: typing.Optional[str]

### platform
- **Type**: typing.Optional[typing.Literal['LINUX_UNIX', 'WINDOWS']]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]


# BucketAccessLogConfigTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### destination
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# BucketBundleTypeDef

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


# BucketStateTypeDef

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# BucketTypeDef

### resourceType
- **Type**: typing.Optional[str]

### accessRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AccessRulesTypeDef]

### arn
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### url
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### name
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### objectVersioning
- **Type**: typing.Optional[str]

### ableToUpdateBundle
- **Type**: typing.Optional[bool]

### readonlyAccessAccounts
- **Type**: typing.Optional[typing.List[str]]

### resourcesReceivingAccess
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ResourceReceivingAccessTypeDef]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.BucketStateTypeDef]

### accessLogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.BucketAccessLogConfigTypeDef]


# BundleTypeDef

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


# CacheBehaviorPerPathTypeDef

### path
- **Type**: typing.Optional[str]

### behavior
- **Type**: typing.Optional[typing.Literal['cache', 'dont-cache']]


# CacheBehaviorTypeDef

### behavior
- **Type**: typing.Optional[typing.Literal['cache', 'dont-cache']]


# CacheSettingsOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CookieObjectOutputTypeDef]

### forwardedHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.HeaderObjectOutputTypeDef]

### forwardedQueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.QueryStringObjectOutputTypeDef]


# CacheSettingsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CookieObjectTypeDef]

### forwardedHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.HeaderObjectTypeDef]

### forwardedQueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.QueryStringObjectTypeDef]


# CertificateSummaryTypeDef

### certificateArn
- **Type**: typing.Optional[str]

### certificateName
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### certificateDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CertificateTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CertificateTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainValidationRecordTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RenewalSummaryTypeDef]

### revokedAt
- **Type**: typing.Optional[datetime.datetime]

### revocationReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### supportCode
- **Type**: typing.Optional[str]


# CloseInstancePublicPortsRequestRequestTypeDef

### portInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.PortInfoTypeDef'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# CloseInstancePublicPortsResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudFormationStackRecordSourceInfoTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['ExportSnapshotRecord']]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# CloudFormationStackRecordTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Started', 'Succeeded']]

### sourceInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CloudFormationStackRecordSourceInfoTypeDef]]

### destinationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DestinationInfoTypeDef]


# ContactMethodTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### supportCode
- **Type**: typing.Optional[str]


# ContainerImageTypeDef

### image
- **Type**: typing.Optional[str]

### digest
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# ContainerOutputTypeDef

### image
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ports
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['HTTP', 'HTTPS', 'TCP', 'UDP']]]


# ContainerServiceDeploymentRequestTypeDef

### containers
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.lightsail_classes.ContainerTypeDef]]

### publicEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.EndpointRequestTypeDef]


# ContainerServiceDeploymentTypeDef

### version
- **Type**: typing.Optional[int]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'FAILED', 'INACTIVE']]

### containers
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.lightsail_classes.ContainerOutputTypeDef]]

### publicEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceEndpointTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]


# ContainerServiceECRImagePullerRoleRequestTypeDef

### isActive
- **Type**: typing.Optional[bool]


# ContainerServiceECRImagePullerRoleTypeDef

### isActive
- **Type**: typing.Optional[bool]

### principalArn
- **Type**: typing.Optional[str]


# ContainerServiceEndpointTypeDef

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceHealthCheckConfigTypeDef]


# ContainerServiceHealthCheckConfigTypeDef

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


# ContainerServiceLogEventTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# ContainerServicePowerTypeDef

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


# ContainerServiceRegistryLoginTypeDef

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### registry
- **Type**: typing.Optional[str]


# ContainerServiceStateDetailTypeDef

### code
- **Type**: typing.Optional[typing.Literal['ACTIVATING_DEPLOYMENT', 'CERTIFICATE_LIMIT_EXCEEDED', 'CREATING_DEPLOYMENT', 'CREATING_NETWORK_INFRASTRUCTURE', 'CREATING_SYSTEM_RESOURCES', 'EVALUATING_HEALTH_CHECK', 'PROVISIONING_CERTIFICATE', 'PROVISIONING_SERVICE', 'UNKNOWN_ERROR']]

### message
- **Type**: typing.Optional[str]


# ContainerServiceTypeDef

### containerServiceName
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### power
- **Type**: typing.Optional[typing.Literal['large', 'medium', 'micro', 'nano', 'small', 'xlarge']]

### powerId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['DELETING', 'DEPLOYING', 'DISABLED', 'PENDING', 'READY', 'RUNNING', 'UPDATING']]

### stateDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceStateDetailTypeDef]

### scale
- **Type**: typing.Optional[int]

### currentDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeploymentTypeDef]

### nextDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeploymentTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PrivateRegistryAccessTypeDef]


# ContainerServicesListResultTypeDef

### containerServices
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ContainerTypeDef

### image
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ports
- **Type**: typing.Optional[typing.Mapping[str, typing.Literal['HTTP', 'HTTPS', 'TCP', 'UDP']]]


# CookieObjectOutputTypeDef

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### cookiesAllowList
- **Type**: typing.Optional[typing.List[str]]


# CookieObjectTypeDef

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### cookiesAllowList
- **Type**: typing.Optional[typing.Sequence[str]]


# CopySnapshotRequestRequestTypeDef

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


# CopySnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CostEstimateTypeDef

### usageType
- **Type**: typing.Optional[str]

### resultsByTime
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.EstimateByTimeTypeDef]]


# CreateBucketAccessKeyRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBucketAccessKeyResultTypeDef

### accessKey
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.AccessKeyTypeDef'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBucketRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### enableObjectVersioning
- **Type**: typing.Optional[bool]


# CreateBucketResultTypeDef

### bucket
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.BucketTypeDef'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCertificateRequestRequestTypeDef

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### subjectAlternativeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateCertificateResultTypeDef

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.CertificateSummaryTypeDef'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudFormationStackRequestRequestTypeDef

### instances
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.InstanceEntryTypeDef]
- **Required**: Yes


# CreateCloudFormationStackResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContactMethodRequestRequestTypeDef

### protocol
- **Type**: typing.Literal['Email', 'SMS']
- **Required**: Yes

### contactEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# CreateContactMethodResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContainerServiceDeploymentRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### containers
- **Type**: typing.Optional[typing.Mapping[str, typing.Union[aws_resource_validator.pydantic_models.lightsail_classes.ContainerTypeDef, aws_resource_validator.pydantic_models.lightsail_classes.ContainerOutputTypeDef]]]

### publicEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.EndpointRequestTypeDef]


# CreateContainerServiceDeploymentResultTypeDef

### containerService
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContainerServiceRegistryLoginResultTypeDef

### registryLogin
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceRegistryLoginTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContainerServiceRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### publicDomainNames
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### deployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeploymentRequestTypeDef]

### privateRegistryAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PrivateRegistryAccessRequestTypeDef]


# CreateContainerServiceResultTypeDef

### containerService
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDiskFromSnapshotRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequestTypeDef]]

### sourceDiskName
- **Type**: typing.Optional[str]

### restoreDate
- **Type**: typing.Optional[str]

### useLatestRestorableAutoSnapshot
- **Type**: typing.Optional[bool]


# CreateDiskFromSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDiskRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequestTypeDef]]


# CreateDiskResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDiskSnapshotRequestRequestTypeDef

### diskSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### diskName
- **Type**: typing.Optional[str]

### instanceName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateDiskSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDistributionRequestRequestTypeDef

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InputOriginTypeDef'>
- **Required**: Yes

### defaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorTypeDef'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes

### cacheBehaviorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheSettingsTypeDef]

### cacheBehaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorPerPathTypeDef]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### certificateName
- **Type**: typing.Optional[str]

### viewerMinimumTlsProtocolVersion
- **Type**: typing.Optional[typing.Literal['TLSv1.1_2016', 'TLSv1.2_2018', 'TLSv1.2_2019', 'TLSv1.2_2021']]


# CreateDistributionResultTypeDef

### distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.LightsailDistributionTypeDef'>
- **Required**: Yes

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainEntryRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryTypeDef'>
- **Required**: Yes


# CreateDomainEntryResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateDomainResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGUISessionAccessDetailsRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGUISessionAccessDetailsResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.SessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceSnapshotRequestRequestTypeDef

### instanceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateInstanceSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstancesFromSnapshotRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.DiskMapTypeDef]]]

### instanceSnapshotName
- **Type**: typing.Optional[str]

### userData
- **Type**: typing.Optional[str]

### keyPairName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequestTypeDef]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### sourceInstanceName
- **Type**: typing.Optional[str]

### restoreDate
- **Type**: typing.Optional[str]

### useLatestRestorableAutoSnapshot
- **Type**: typing.Optional[bool]


# CreateInstancesFromSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstancesRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### addOns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequestTypeDef]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]


# CreateInstancesResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeyPairRequestRequestTypeDef

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateKeyPairResultTypeDef

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.KeyPairTypeDef'>
- **Required**: Yes

### publicKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes

### privateKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoadBalancerRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### tlsPolicyName
- **Type**: typing.Optional[str]


# CreateLoadBalancerResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoadBalancerTlsCertificateRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateLoadBalancerTlsCertificateResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### useLatestRestorableTime
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateRelationalDatabaseFromSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRelationalDatabaseRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateRelationalDatabaseResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRelationalDatabaseSnapshotRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### relationalDatabaseSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]


# CreateRelationalDatabaseSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAlarmRequestRequestTypeDef

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAlarmResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAutoSnapshotRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### date
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAutoSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBucketAccessKeyRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketAccessKeyResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBucketRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteBucketResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCertificateRequestRequestTypeDef

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteContactMethodRequestRequestTypeDef

### protocol
- **Type**: typing.Literal['Email', 'SMS']
- **Required**: Yes


# DeleteContactMethodResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteContainerImageRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### image
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContainerServiceRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDiskRequestRequestTypeDef

### diskName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDeleteAddOns
- **Type**: typing.Optional[bool]


# DeleteDiskResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDiskSnapshotRequestRequestTypeDef

### diskSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDiskSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDistributionRequestRequestTypeDef

### distributionName
- **Type**: typing.Optional[str]


# DeleteDistributionResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainEntryRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryTypeDef'>
- **Required**: Yes


# DeleteDomainEntryResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInstanceRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDeleteAddOns
- **Type**: typing.Optional[bool]


# DeleteInstanceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteInstanceSnapshotRequestRequestTypeDef

### instanceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKeyPairRequestRequestTypeDef

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes

### expectedFingerprint
- **Type**: typing.Optional[str]


# DeleteKeyPairResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKnownHostKeysRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnownHostKeysResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLoadBalancerRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLoadBalancerTlsCertificateRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### certificateName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteLoadBalancerTlsCertificateResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRelationalDatabaseRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### skipFinalSnapshot
- **Type**: typing.Optional[bool]

### finalRelationalDatabaseSnapshotName
- **Type**: typing.Optional[str]


# DeleteRelationalDatabaseResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRelationalDatabaseSnapshotRequestRequestTypeDef

### relationalDatabaseSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRelationalDatabaseSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationInfoTypeDef

### id
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]


# DetachCertificateFromDistributionRequestRequestTypeDef

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachCertificateFromDistributionResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachDiskRequestRequestTypeDef

### diskName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachDiskResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachInstancesFromLoadBalancerRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DetachInstancesFromLoadBalancerResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachStaticIpRequestRequestTypeDef

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachStaticIpResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableAddOnRequestRequestTypeDef

### addOnType
- **Type**: typing.Literal['AutoSnapshot', 'StopInstanceOnIdle']
- **Required**: Yes

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DisableAddOnResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiskInfoTypeDef

### name
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### sizeInGb
- **Type**: typing.Optional[int]

### isSystemDisk
- **Type**: typing.Optional[bool]


# DiskMapTypeDef

### originalDiskPath
- **Type**: typing.Optional[str]

### newDiskName
- **Type**: typing.Optional[str]


# DiskSnapshotInfoTypeDef

### sizeInGb
- **Type**: typing.Optional[int]


# DiskSnapshotTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

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


# DiskTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### addOns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AddOnTypeDef]]

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


# DistributionBundleTypeDef

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


# DnsRecordCreationStateTypeDef

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# DomainEntryExtraOutputTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### isAlias
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### options
- **Type**: typing.Optional[typing.Dict[str, str]]


# DomainEntryOutputTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### isAlias
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### options
- **Type**: typing.Optional[typing.Dict[str, str]]


# DomainEntryTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### isAlias
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### options
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DomainTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### domainEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryOutputTypeDef]]

### registeredDomainDelegationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RegisteredDomainDelegationInfoTypeDef]


# DomainValidationRecordTypeDef

### domainName
- **Type**: typing.Optional[str]

### resourceRecord
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceRecordTypeDef]

### dnsRecordCreationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DnsRecordCreationStateTypeDef]

### validationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]


# DownloadDefaultKeyPairResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableAddOnRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### addOnRequest
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.AddOnRequestTypeDef'>
- **Required**: Yes


# EnableAddOnResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointRequestTypeDef

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### containerPort
- **Type**: <class 'int'>
- **Required**: Yes

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceHealthCheckConfigTypeDef]


# EstimateByTimeTypeDef

### usageCost
- **Type**: typing.Optional[float]

### pricingUnit
- **Type**: typing.Optional[typing.Literal['Bundles', 'GB', 'GB-Mo', 'Hrs', 'Queries']]

### unit
- **Type**: typing.Optional[float]

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### timePeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.TimePeriodTypeDef]


# ExportSnapshotRecordSourceInfoTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceSnapshotInfoTypeDef]

### diskSnapshotInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DiskSnapshotInfoTypeDef]


# ExportSnapshotRecordTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### state
- **Type**: typing.Optional[typing.Literal['Failed', 'Started', 'Succeeded']]

### sourceInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ExportSnapshotRecordSourceInfoTypeDef]

### destinationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.DestinationInfoTypeDef]


# ExportSnapshotRequestRequestTypeDef

### sourceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# ExportSnapshotResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetActiveNamesRequestGetActiveNamesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetActiveNamesRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetActiveNamesResultTypeDef

### activeNames
- **Type**: typing.List[str]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAlarmsRequestRequestTypeDef

### alarmName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]

### monitoredResourceName
- **Type**: typing.Optional[str]


# GetAlarmsResultTypeDef

### alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AlarmTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAutoSnapshotsRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAutoSnapshotsResultTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']
- **Required**: Yes

### autoSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AutoSnapshotDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlueprintsRequestGetBlueprintsPaginateTypeDef

### includeInactive
- **Type**: typing.Optional[bool]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetBlueprintsRequestRequestTypeDef

### includeInactive
- **Type**: typing.Optional[bool]

### pageToken
- **Type**: typing.Optional[str]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]


# GetBlueprintsResultTypeDef

### blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.BlueprintTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketAccessKeysRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketAccessKeysResultTypeDef

### accessKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AccessKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketBundlesRequestRequestTypeDef

### includeInactive
- **Type**: typing.Optional[bool]


# GetBucketBundlesResultTypeDef

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.BucketBundleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketMetricDataRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['BucketSizeBytes', 'NumberOfObjects']
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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


# GetBucketMetricDataResultTypeDef

### metricName
- **Type**: typing.Literal['BucketSizeBytes', 'NumberOfObjects']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketsRequestRequestTypeDef

### bucketName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]

### includeConnectedResources
- **Type**: typing.Optional[bool]


# GetBucketsResultTypeDef

### buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.BucketTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### accountLevelBpaSync
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.AccountLevelBpaSyncTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBundlesRequestGetBundlesPaginateTypeDef

### includeInactive
- **Type**: typing.Optional[bool]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetBundlesRequestRequestTypeDef

### includeInactive
- **Type**: typing.Optional[bool]

### pageToken
- **Type**: typing.Optional[str]

### appCategory
- **Type**: typing.Optional[typing.Literal['LfR']]


# GetBundlesResultTypeDef

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.BundleTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCertificatesRequestRequestTypeDef

### certificateStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'VALIDATION_TIMED_OUT']]]

### includeCertificateDetails
- **Type**: typing.Optional[bool]

### certificateName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]


# GetCertificatesResultTypeDef

### certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CertificateSummaryTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCloudFormationStackRecordsRequestGetCloudFormationStackRecordsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetCloudFormationStackRecordsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetCloudFormationStackRecordsResultTypeDef

### cloudFormationStackRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CloudFormationStackRecordTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContactMethodsRequestRequestTypeDef

### protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Email', 'SMS']]]


# GetContactMethodsResultTypeDef

### contactMethods
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContactMethodTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerAPIMetadataResultTypeDef

### metadata
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerImagesRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerImagesResultTypeDef

### containerImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerLogRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### filterPattern
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]


# GetContainerLogResultTypeDef

### logEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceLogEventTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerServiceDeploymentsRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetContainerServiceDeploymentsResultTypeDef

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceDeploymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerServiceMetricDataRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['CPUUtilization', 'MemoryUtilization']
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### period
- **Type**: <class 'int'>
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetContainerServiceMetricDataResultTypeDef

### metricName
- **Type**: typing.Literal['CPUUtilization', 'MemoryUtilization']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerServicePowersResultTypeDef

### powers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServicePowerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContainerServicesRequestRequestTypeDef

### serviceName
- **Type**: typing.Optional[str]


# GetCostEstimateRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetCostEstimateResultTypeDef

### resourcesBudgetEstimate
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ResourceBudgetEstimateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDiskRequestRequestTypeDef

### diskName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDiskResultTypeDef

### disk
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DiskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDiskSnapshotRequestRequestTypeDef

### diskSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDiskSnapshotResultTypeDef

### diskSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DiskSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDiskSnapshotsRequestGetDiskSnapshotsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetDiskSnapshotsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetDiskSnapshotsResultTypeDef

### diskSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskSnapshotTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDisksRequestGetDisksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetDisksRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetDisksResultTypeDef

### disks
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionBundlesResultTypeDef

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DistributionBundleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionLatestCacheResetRequestRequestTypeDef

### distributionName
- **Type**: typing.Optional[str]


# GetDistributionLatestCacheResetResultTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionMetricDataRequestRequestTypeDef

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: typing.Literal['BytesDownloaded', 'BytesUploaded', 'Http4xxErrorRate', 'Http5xxErrorRate', 'Requests', 'TotalErrorRate']
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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


# GetDistributionMetricDataResultTypeDef

### metricName
- **Type**: typing.Literal['BytesDownloaded', 'BytesUploaded', 'Http4xxErrorRate', 'Http5xxErrorRate', 'Requests', 'TotalErrorRate']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionsRequestRequestTypeDef

### distributionName
- **Type**: typing.Optional[str]

### pageToken
- **Type**: typing.Optional[str]


# GetDistributionsResultTypeDef

### distributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LightsailDistributionTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainResultTypeDef

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainsRequestGetDomainsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetDomainsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetDomainsResultTypeDef

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExportSnapshotRecordsRequestGetExportSnapshotRecordsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetExportSnapshotRecordsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetExportSnapshotRecordsResultTypeDef

### exportSnapshotRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.ExportSnapshotRecordTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceAccessDetailsRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### protocol
- **Type**: typing.Optional[typing.Literal['rdp', 'ssh']]


# GetInstanceAccessDetailsResultTypeDef

### accessDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceAccessDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceMetricDataRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetInstanceMetricDataResultTypeDef

### metricName
- **Type**: typing.Literal['BurstCapacityPercentage', 'BurstCapacityTime', 'CPUUtilization', 'MetadataNoToken', 'NetworkIn', 'NetworkOut', 'StatusCheckFailed', 'StatusCheckFailed_Instance', 'StatusCheckFailed_System']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstancePortStatesRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstancePortStatesResultTypeDef

### portStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstancePortStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceResultTypeDef

### instance
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceSnapshotRequestRequestTypeDef

### instanceSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceSnapshotResultTypeDef

### instanceSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceSnapshotsRequestGetInstanceSnapshotsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetInstanceSnapshotsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetInstanceSnapshotsResultTypeDef

### instanceSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstanceSnapshotTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceStateRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceStateResultTypeDef

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.InstanceStateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstancesRequestGetInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetInstancesRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetInstancesResultTypeDef

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstanceTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyPairRequestRequestTypeDef

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyPairResultTypeDef

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.KeyPairTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyPairsRequestGetKeyPairsPaginateTypeDef

### includeDefaultKeyPair
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetKeyPairsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]

### includeDefaultKeyPair
- **Type**: typing.Optional[bool]


# GetKeyPairsResultTypeDef

### keyPairs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.KeyPairTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoadBalancerMetricDataRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetLoadBalancerMetricDataResultTypeDef

### metricName
- **Type**: typing.Literal['ClientTLSNegotiationErrorCount', 'HTTPCode_Instance_2XX_Count', 'HTTPCode_Instance_3XX_Count', 'HTTPCode_Instance_4XX_Count', 'HTTPCode_Instance_5XX_Count', 'HTTPCode_LB_4XX_Count', 'HTTPCode_LB_5XX_Count', 'HealthyHostCount', 'InstanceResponseTime', 'RejectedConnectionCount', 'RequestCount', 'UnhealthyHostCount']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoadBalancerRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoadBalancerResultTypeDef

### loadBalancer
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoadBalancerTlsCertificatesRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoadBalancerTlsCertificatesResultTypeDef

### tlsCertificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoadBalancerTlsPoliciesRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetLoadBalancerTlsPoliciesResultTypeDef

### tlsPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsPolicyTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoadBalancersRequestGetLoadBalancersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetLoadBalancersRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetLoadBalancersResultTypeDef

### loadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOperationRequestRequestTypeDef

### operationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetOperationResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOperationsForResourceRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### pageToken
- **Type**: typing.Optional[str]


# GetOperationsForResourceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### nextPageCount
- **Type**: <class 'str'>
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOperationsRequestGetOperationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetOperationsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetOperationsResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegionsRequestRequestTypeDef

### includeAvailabilityZones
- **Type**: typing.Optional[bool]

### includeRelationalDatabaseAvailabilityZones
- **Type**: typing.Optional[bool]


# GetRegionsResultTypeDef

### regions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RegionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseBlueprintsRequestGetRelationalDatabaseBlueprintsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetRelationalDatabaseBlueprintsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseBlueprintsResultTypeDef

### blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseBlueprintTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseBundlesRequestGetRelationalDatabaseBundlesPaginateTypeDef

### includeInactive
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetRelationalDatabaseBundlesRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]

### includeInactive
- **Type**: typing.Optional[bool]


# GetRelationalDatabaseBundlesResultTypeDef

### bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseBundleTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseEventsRequestGetRelationalDatabaseEventsPaginateTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetRelationalDatabaseEventsRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### durationInMinutes
- **Type**: typing.Optional[int]

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseEventsResultTypeDef

### relationalDatabaseEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseEventTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseLogEventsRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### startFromHead
- **Type**: typing.Optional[bool]

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseLogEventsResultTypeDef

### resourceLogEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LogEventTypeDef]
- **Required**: Yes

### nextBackwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextForwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseLogStreamsRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelationalDatabaseLogStreamsResultTypeDef

### logStreams
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### passwordVersion
- **Type**: typing.Optional[typing.Literal['CURRENT', 'PENDING', 'PREVIOUS']]


# GetRelationalDatabaseMasterUserPasswordResultTypeDef

### masterUserPassword
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseMetricDataRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### unit
- **Type**: typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]
- **Required**: Yes


# GetRelationalDatabaseMetricDataResultTypeDef

### metricName
- **Type**: typing.Literal['CPUUtilization', 'DatabaseConnections', 'DiskQueueDepth', 'FreeStorageSpace', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput']
- **Required**: Yes

### metricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.MetricDatapointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseParametersRequestGetRelationalDatabaseParametersPaginateTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetRelationalDatabaseParametersRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseParametersResultTypeDef

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseParameterTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelationalDatabaseResultTypeDef

### relationalDatabase
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseSnapshotRequestRequestTypeDef

### relationalDatabaseSnapshotName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelationalDatabaseSnapshotResultTypeDef

### relationalDatabaseSnapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseSnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabaseSnapshotsRequestGetRelationalDatabaseSnapshotsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetRelationalDatabaseSnapshotsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabaseSnapshotsResultTypeDef

### relationalDatabaseSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseSnapshotTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelationalDatabasesRequestGetRelationalDatabasesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetRelationalDatabasesRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetRelationalDatabasesResultTypeDef

### relationalDatabases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSetupHistoryRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### pageToken
- **Type**: typing.Optional[str]


# GetSetupHistoryResultTypeDef

### setupHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.SetupHistoryTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStaticIpRequestRequestTypeDef

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStaticIpResultTypeDef

### staticIp
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.StaticIpTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStaticIpsRequestGetStaticIpsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PaginatorConfigTypeDef]


# GetStaticIpsRequestRequestTypeDef

### pageToken
- **Type**: typing.Optional[str]


# GetStaticIpsResultTypeDef

### staticIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.StaticIpTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HeaderObjectOutputTypeDef

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### headersAllowList
- **Type**: typing.Optional[typing.List[typing.Literal['Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Authorization', 'CloudFront-Forwarded-Proto', 'CloudFront-Is-Desktop-Viewer', 'CloudFront-Is-Mobile-Viewer', 'CloudFront-Is-SmartTV-Viewer', 'CloudFront-Is-Tablet-Viewer', 'CloudFront-Viewer-Country', 'Host', 'Origin', 'Referer']]]


# HeaderObjectTypeDef

### option
- **Type**: typing.Optional[typing.Literal['all', 'allow-list', 'none']]

### headersAllowList
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Accept', 'Accept-Charset', 'Accept-Datetime', 'Accept-Encoding', 'Accept-Language', 'Authorization', 'CloudFront-Forwarded-Proto', 'CloudFront-Is-Desktop-Viewer', 'CloudFront-Is-Mobile-Viewer', 'CloudFront-Is-SmartTV-Viewer', 'CloudFront-Is-Tablet-Viewer', 'CloudFront-Viewer-Country', 'Host', 'Origin', 'Referer']]]


# HostKeyAttributesTypeDef

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


# ImportKeyPairRequestRequestTypeDef

### keyPairName
- **Type**: <class 'str'>
- **Required**: Yes

### publicKeyBase64
- **Type**: <class 'str'>
- **Required**: Yes


# ImportKeyPairResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputOriginTypeDef

### name
- **Type**: typing.Optional[str]

### regionName
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### protocolPolicy
- **Type**: typing.Optional[typing.Literal['http-only', 'https-only']]

### responseTimeout
- **Type**: typing.Optional[int]


# InstanceAccessDetailsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PasswordDataTypeDef]

### privateKey
- **Type**: typing.Optional[str]

### protocol
- **Type**: typing.Optional[typing.Literal['rdp', 'ssh']]

### instanceName
- **Type**: typing.Optional[str]

### username
- **Type**: typing.Optional[str]

### hostKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.HostKeyAttributesTypeDef]]


# InstanceEntryTypeDef

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


# InstanceHardwareTypeDef

### cpuCount
- **Type**: typing.Optional[int]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskTypeDef]]

### ramSizeInGb
- **Type**: typing.Optional[float]


# InstanceHealthSummaryTypeDef

### instanceName
- **Type**: typing.Optional[str]

### instanceHealth
- **Type**: typing.Optional[typing.Literal['draining', 'healthy', 'initial', 'unavailable', 'unhealthy', 'unused']]

### instanceHealthReason
- **Type**: typing.Optional[typing.Literal['Instance.DeregistrationInProgress', 'Instance.FailedHealthChecks', 'Instance.InvalidState', 'Instance.IpUnusable', 'Instance.NotInUse', 'Instance.NotRegistered', 'Instance.ResponseCodeMismatch', 'Instance.Timeout', 'Lb.InitialHealthChecking', 'Lb.InternalError', 'Lb.RegistrationInProgress']]


# InstanceMetadataOptionsTypeDef

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


# InstanceNetworkingTypeDef

### monthlyTransfer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.MonthlyTransferTypeDef]

### ports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstancePortInfoTypeDef]]


# InstancePortInfoTypeDef

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


# InstancePortStateTypeDef

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


# InstanceSnapshotInfoTypeDef

### fromBundleId
- **Type**: typing.Optional[str]

### fromBlueprintId
- **Type**: typing.Optional[str]

### fromDiskInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskInfoTypeDef]]


# InstanceSnapshotTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### state
- **Type**: typing.Optional[typing.Literal['available', 'error', 'pending']]

### progress
- **Type**: typing.Optional[str]

### fromAttachedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DiskTypeDef]]

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


# InstanceStateTypeDef

### code
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]


# InstanceTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### blueprintId
- **Type**: typing.Optional[str]

### blueprintName
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]

### addOns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AddOnTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceHardwareTypeDef]

### networking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceNetworkingTypeDef]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceStateTypeDef]

### username
- **Type**: typing.Optional[str]

### sshKeyName
- **Type**: typing.Optional[str]

### metadataOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InstanceMetadataOptionsTypeDef]


# IsVpcPeeredResultTypeDef

### isPeered
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KeyPairTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### fingerprint
- **Type**: typing.Optional[str]


# LightsailDistributionTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.OriginTypeDef]

### originPublicDNS
- **Type**: typing.Optional[str]

### defaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorTypeDef]

### cacheBehaviorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheSettingsOutputTypeDef]

### cacheBehaviors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorPerPathTypeDef]]

### ableToUpdateBundle
- **Type**: typing.Optional[bool]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### viewerMinimumTlsProtocolVersion
- **Type**: typing.Optional[str]


# LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# LoadBalancerTlsCertificateDomainValidationOptionTypeDef

### domainName
- **Type**: typing.Optional[str]

### validationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]


# LoadBalancerTlsCertificateDomainValidationRecordTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### validationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_VALIDATION', 'SUCCESS']]

### domainName
- **Type**: typing.Optional[str]

### dnsRecordCreationState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef]


# LoadBalancerTlsCertificateRenewalSummaryTypeDef

### renewalStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING_AUTO_RENEWAL', 'PENDING_VALIDATION', 'SUCCESS']]

### domainValidationOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateDomainValidationOptionTypeDef]]


# LoadBalancerTlsCertificateSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]


# LoadBalancerTlsCertificateTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### loadBalancerName
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['EXPIRED', 'FAILED', 'INACTIVE', 'ISSUED', 'PENDING_VALIDATION', 'REVOKED', 'UNKNOWN', 'VALIDATION_TIMED_OUT']]

### domainName
- **Type**: typing.Optional[str]

### domainValidationRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateDomainValidationRecordTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateRenewalSummaryTypeDef]

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


# LoadBalancerTlsPolicyTypeDef

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


# LoadBalancerTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.InstanceHealthSummaryTypeDef]]

### tlsCertificateSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.LoadBalancerTlsCertificateSummaryTypeDef]]

### configurationOptions
- **Type**: typing.Optional[typing.Dict[typing.Literal['HealthCheckPath', 'HttpsRedirectionEnabled', 'SessionStickinessEnabled', 'SessionStickiness_LB_CookieDurationSeconds', 'TlsPolicyName'], str]]

### ipAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4', 'ipv6']]

### httpsRedirectionEnabled
- **Type**: typing.Optional[bool]

### tlsPolicyName
- **Type**: typing.Optional[str]


# LogEventTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


# MetricDatapointTypeDef

### average
- **Type**: typing.Optional[float]

### maximum
- **Type**: typing.Optional[float]

### minimum
- **Type**: typing.Optional[float]

### sampleCount
- **Type**: typing.Optional[float]

### sum
- **Type**: typing.Optional[float]

### timestamp
- **Type**: typing.Optional[datetime.datetime]

### unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MonitoredResourceInfoTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]


# MonthlyTransferTypeDef

### gbPerMonthAllocated
- **Type**: typing.Optional[int]


# NameServersUpdateStateTypeDef

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# OpenInstancePublicPortsRequestRequestTypeDef

### portInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.PortInfoTypeDef'>
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# OpenInstancePublicPortsResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OperationTypeDef

### id
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### isTerminal
- **Type**: typing.Optional[bool]

### operationDetails
- **Type**: typing.Optional[str]

### operationType
- **Type**: typing.Optional[typing.Literal['AllocateStaticIp', 'AttachCertificateToDistribution', 'AttachDisk', 'AttachInstancesToLoadBalancer', 'AttachLoadBalancerTlsCertificate', 'AttachStaticIp', 'CloseInstancePublicPorts', 'CreateBucket', 'CreateBucketAccessKey', 'CreateCertificate', 'CreateContactMethod', 'CreateContainerService', 'CreateContainerServiceDeployment', 'CreateContainerServiceRegistryLogin', 'CreateDisk', 'CreateDiskFromSnapshot', 'CreateDiskSnapshot', 'CreateDistribution', 'CreateDomain', 'CreateInstance', 'CreateInstanceSnapshot', 'CreateInstancesFromSnapshot', 'CreateLoadBalancer', 'CreateLoadBalancerTlsCertificate', 'CreateRelationalDatabase', 'CreateRelationalDatabaseFromSnapshot', 'CreateRelationalDatabaseSnapshot', 'DeleteAlarm', 'DeleteBucket', 'DeleteBucketAccessKey', 'DeleteCertificate', 'DeleteContactMethod', 'DeleteContainerImage', 'DeleteContainerService', 'DeleteDisk', 'DeleteDiskSnapshot', 'DeleteDistribution', 'DeleteDomain', 'DeleteDomainEntry', 'DeleteInstance', 'DeleteInstanceSnapshot', 'DeleteKnownHostKeys', 'DeleteLoadBalancer', 'DeleteLoadBalancerTlsCertificate', 'DeleteRelationalDatabase', 'DeleteRelationalDatabaseSnapshot', 'DetachCertificateFromDistribution', 'DetachDisk', 'DetachInstancesFromLoadBalancer', 'DetachStaticIp', 'DisableAddOn', 'EnableAddOn', 'GetAlarms', 'GetContactMethods', 'OpenInstancePublicPorts', 'PutAlarm', 'PutInstancePublicPorts', 'RebootInstance', 'RebootRelationalDatabase', 'RegisterContainerImage', 'ReleaseStaticIp', 'ResetDistributionCache', 'SendContactMethodVerification', 'SetIpAddressType', 'SetResourceAccessForBucket', 'SetupInstanceHttps', 'StartGUISession', 'StartInstance', 'StartRelationalDatabase', 'StopGUISession', 'StopInstance', 'StopRelationalDatabase', 'TestAlarm', 'UpdateBucket', 'UpdateBucketBundle', 'UpdateContainerService', 'UpdateDistribution', 'UpdateDistributionBundle', 'UpdateDomainEntry', 'UpdateInstanceMetadataOptions', 'UpdateLoadBalancerAttribute', 'UpdateRelationalDatabase', 'UpdateRelationalDatabaseParameters']]

### status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'NotStarted', 'Started', 'Succeeded']]

### statusChangedAt
- **Type**: typing.Optional[datetime.datetime]

### errorCode
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[str]


# OriginTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PasswordDataTypeDef

### ciphertext
- **Type**: typing.Optional[str]

### keyPairName
- **Type**: typing.Optional[str]


# PeerVpcResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PendingMaintenanceActionTypeDef

### action
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### currentApplyDate
- **Type**: typing.Optional[datetime.datetime]


# PendingModifiedRelationalDatabaseValuesTypeDef

### masterUserPassword
- **Type**: typing.Optional[str]

### engineVersion
- **Type**: typing.Optional[str]

### backupRetentionEnabled
- **Type**: typing.Optional[bool]


# PortInfoTypeDef

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


# PrivateRegistryAccessRequestTypeDef

### ecrImagePullerRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceECRImagePullerRoleRequestTypeDef]


# PrivateRegistryAccessTypeDef

### ecrImagePullerRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceECRImagePullerRoleTypeDef]


# PutAlarmRequestRequestTypeDef

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


# PutAlarmResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutInstancePublicPortsRequestRequestTypeDef

### portInfos
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.PortInfoTypeDef]
- **Required**: Yes

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# PutInstancePublicPortsResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryStringObjectOutputTypeDef

### option
- **Type**: typing.Optional[bool]

### queryStringsAllowList
- **Type**: typing.Optional[typing.List[str]]


# QueryStringObjectTypeDef

### option
- **Type**: typing.Optional[bool]

### queryStringsAllowList
- **Type**: typing.Optional[typing.Sequence[str]]


# R53HostedZoneDeletionStateTypeDef

### code
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### message
- **Type**: typing.Optional[str]


# RebootInstanceRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# RebootInstanceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootRelationalDatabaseRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RebootRelationalDatabaseResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegionTypeDef

### continentCode
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### availabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AvailabilityZoneTypeDef]]

### relationalDatabaseAvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.AvailabilityZoneTypeDef]]


# RegisterContainerImageRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### label
- **Type**: <class 'str'>
- **Required**: Yes

### digest
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterContainerImageResultTypeDef

### containerImage
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisteredDomainDelegationInfoTypeDef

### nameServersUpdateState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.NameServersUpdateStateTypeDef]

### r53HostedZoneDeletionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.R53HostedZoneDeletionStateTypeDef]


# RelationalDatabaseBlueprintTypeDef

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


# RelationalDatabaseBundleTypeDef

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


# RelationalDatabaseEndpointTypeDef

### port
- **Type**: typing.Optional[int]

### address
- **Type**: typing.Optional[str]


# RelationalDatabaseEventTypeDef

### resource
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]

### eventCategories
- **Type**: typing.Optional[typing.List[str]]


# RelationalDatabaseHardwareTypeDef

### cpuCount
- **Type**: typing.Optional[int]

### diskSizeInGb
- **Type**: typing.Optional[int]

### ramSizeInGb
- **Type**: typing.Optional[float]


# RelationalDatabaseParameterTypeDef

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


# RelationalDatabaseSnapshotTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

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


# RelationalDatabaseTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]]

### relationalDatabaseBlueprintId
- **Type**: typing.Optional[str]

### relationalDatabaseBundleId
- **Type**: typing.Optional[str]

### masterDatabaseName
- **Type**: typing.Optional[str]

### hardware
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseHardwareTypeDef]

### state
- **Type**: typing.Optional[str]

### secondaryAvailabilityZone
- **Type**: typing.Optional[str]

### backupRetentionEnabled
- **Type**: typing.Optional[bool]

### pendingModifiedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PendingModifiedRelationalDatabaseValuesTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseEndpointTypeDef]

### pendingMaintenanceActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.PendingMaintenanceActionTypeDef]]

### caCertificateIdentifier
- **Type**: typing.Optional[str]


# ReleaseStaticIpRequestRequestTypeDef

### staticIpName
- **Type**: <class 'str'>
- **Required**: Yes


# ReleaseStaticIpResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RenewalSummaryTypeDef

### domainValidationRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.DomainValidationRecordTypeDef]]

### renewalStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'PendingAutoRenewal', 'PendingValidation', 'Success']]

### renewalStatusReason
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ResetDistributionCacheRequestRequestTypeDef

### distributionName
- **Type**: typing.Optional[str]


# ResetDistributionCacheResultTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceBudgetEstimateTypeDef

### resourceName
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### costEstimates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.CostEstimateTypeDef]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# ResourceLocationTypeDef

### availabilityZone
- **Type**: typing.Optional[str]

### regionName
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]


# ResourceReceivingAccessTypeDef

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]


# ResourceRecordTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
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


# SendContactMethodVerificationRequestRequestTypeDef

### protocol
- **Type**: typing.Literal['Email']
- **Required**: Yes


# SendContactMethodVerificationResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SessionTypeDef

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### isPrimary
- **Type**: typing.Optional[bool]


# SetIpAddressTypeRequestRequestTypeDef

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


# SetIpAddressTypeResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetResourceAccessForBucketRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### access
- **Type**: typing.Literal['allow', 'deny']
- **Required**: Yes


# SetResourceAccessForBucketResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetupExecutionDetailsTypeDef

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


# SetupHistoryResourceTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]


# SetupHistoryTypeDef

### operationId
- **Type**: typing.Optional[str]

### request
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.SetupRequestTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.SetupHistoryResourceTypeDef]

### executionDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lightsail_classes.SetupExecutionDetailsTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['failed', 'inProgress', 'succeeded']]


# SetupInstanceHttpsRequestRequestTypeDef

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


# SetupInstanceHttpsResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetupRequestTypeDef

### instanceName
- **Type**: typing.Optional[str]

### domainNames
- **Type**: typing.Optional[typing.List[str]]

### certificateProvider
- **Type**: typing.Optional[typing.Literal['LetsEncrypt']]


# StartGUISessionRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# StartGUISessionResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartInstanceRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# StartInstanceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRelationalDatabaseRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# StartRelationalDatabaseResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StaticIpTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### supportCode
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.ResourceLocationTypeDef]

### resourceType
- **Type**: typing.Optional[typing.Literal['Alarm', 'Bucket', 'Certificate', 'CloudFormationStackRecord', 'ContactMethod', 'ContainerService', 'Disk', 'DiskSnapshot', 'Distribution', 'Domain', 'ExportSnapshotRecord', 'Instance', 'InstanceSnapshot', 'KeyPair', 'LoadBalancer', 'LoadBalancerTlsCertificate', 'PeeredVpc', 'RelationalDatabase', 'RelationalDatabaseSnapshot', 'StaticIp']]

### ipAddress
- **Type**: typing.Optional[str]

### attachedTo
- **Type**: typing.Optional[str]

### isAttached
- **Type**: typing.Optional[bool]


# StopGUISessionRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes


# StopGUISessionResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopInstanceOnIdleRequestTypeDef

### threshold
- **Type**: typing.Optional[str]

### duration
- **Type**: typing.Optional[str]


# StopInstanceRequestRequestTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# StopInstanceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRelationalDatabaseRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### relationalDatabaseSnapshotName
- **Type**: typing.Optional[str]


# StopRelationalDatabaseResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.TagTypeDef]
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]


# TagResourceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TestAlarmRequestRequestTypeDef

### alarmName
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ALARM', 'INSUFFICIENT_DATA', 'OK']
- **Required**: Yes


# TestAlarmResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimePeriodTypeDef

### start
- **Type**: typing.Optional[datetime.datetime]

### end
- **Type**: typing.Optional[datetime.datetime]


# UnpeerVpcResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceName
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]


# UntagResourceResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBucketBundleRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bundleId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBucketBundleResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBucketRequestRequestTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### accessRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.AccessRulesTypeDef]

### versioning
- **Type**: typing.Optional[str]

### readonlyAccessAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### accessLogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.BucketAccessLogConfigTypeDef]


# UpdateBucketResultTypeDef

### bucket
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.BucketTypeDef'>
- **Required**: Yes

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContainerServiceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.PrivateRegistryAccessRequestTypeDef]


# UpdateContainerServiceResultTypeDef

### containerService
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ContainerServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDistributionBundleRequestRequestTypeDef

### distributionName
- **Type**: typing.Optional[str]

### bundleId
- **Type**: typing.Optional[str]


# UpdateDistributionBundleResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDistributionRequestRequestTypeDef

### distributionName
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.InputOriginTypeDef]

### defaultCacheBehavior
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorTypeDef]

### cacheBehaviorSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lightsail_classes.CacheSettingsTypeDef]

### cacheBehaviors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.CacheBehaviorPerPathTypeDef]]

### isEnabled
- **Type**: typing.Optional[bool]

### viewerMinimumTlsProtocolVersion
- **Type**: typing.Optional[typing.Literal['TLSv1.1_2016', 'TLSv1.2_2018', 'TLSv1.2_2019', 'TLSv1.2_2021']]

### certificateName
- **Type**: typing.Optional[str]

### useDefaultCertificate
- **Type**: typing.Optional[bool]


# UpdateDistributionResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainEntryRequestRequestTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### domainEntry
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.DomainEntryTypeDef'>
- **Required**: Yes


# UpdateDomainEntryResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInstanceMetadataOptionsRequestRequestTypeDef

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


# UpdateInstanceMetadataOptionsResultTypeDef

### operation
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLoadBalancerAttributeRequestRequestTypeDef

### loadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### attributeName
- **Type**: typing.Literal['HealthCheckPath', 'HttpsRedirectionEnabled', 'SessionStickinessEnabled', 'SessionStickiness_LB_CookieDurationSeconds', 'TlsPolicyName']
- **Required**: Yes

### attributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateLoadBalancerAttributeResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRelationalDatabaseParametersRequestRequestTypeDef

### relationalDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lightsail_classes.RelationalDatabaseParameterTypeDef]
- **Required**: Yes


# UpdateRelationalDatabaseParametersResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRelationalDatabaseRequestRequestTypeDef

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


# UpdateRelationalDatabaseResultTypeDef

### operations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lightsail_classes.OperationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lightsail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


