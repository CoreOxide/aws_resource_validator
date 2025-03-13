# Sms Classes

# AppSummaryTypeDef

### appId
- **Type**: typing.Optional[str]

### importedAppId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATING']]

### statusMessage
- **Type**: typing.Optional[str]

### replicationConfigurationStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURED', 'NOT_CONFIGURED']]

### replicationStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURATION_INVALID', 'CONFIGURATION_IN_PROGRESS', 'DELTA_REPLICATED', 'DELTA_REPLICATION_FAILED', 'DELTA_REPLICATION_IN_PROGRESS', 'PARTIALLY_REPLICATED', 'READY_FOR_CONFIGURATION', 'READY_FOR_REPLICATION', 'REPLICATED', 'REPLICATION_FAILED', 'REPLICATION_IN_PROGRESS', 'REPLICATION_PENDING', 'REPLICATION_STOPPED', 'REPLICATION_STOPPING', 'REPLICATION_STOP_FAILED', 'VALIDATION_IN_PROGRESS']]

### replicationStatusMessage
- **Type**: typing.Optional[str]

### latestReplicationTime
- **Type**: typing.Optional[datetime.datetime]

### launchConfigurationStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURED', 'NOT_CONFIGURED']]

### launchStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURATION_INVALID', 'CONFIGURATION_IN_PROGRESS', 'DELTA_LAUNCH_FAILED', 'DELTA_LAUNCH_IN_PROGRESS', 'LAUNCHED', 'LAUNCH_FAILED', 'LAUNCH_IN_PROGRESS', 'LAUNCH_PENDING', 'PARTIALLY_LAUNCHED', 'READY_FOR_CONFIGURATION', 'READY_FOR_LAUNCH', 'TERMINATED', 'TERMINATE_FAILED', 'TERMINATE_IN_PROGRESS', 'VALIDATION_IN_PROGRESS']]

### launchStatusMessage
- **Type**: typing.Optional[str]

### launchDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.LaunchDetailsTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### roleName
- **Type**: typing.Optional[str]

### totalServerGroups
- **Type**: typing.Optional[int]

### totalServers
- **Type**: typing.Optional[int]


# AppValidationConfigurationTypeDef

### validationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### appValidationStrategy
- **Type**: typing.Optional[typing.Literal['SSM']]

### ssmValidationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.SSMValidationParametersTypeDef]


# AppValidationOutputTypeDef

### ssmOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.SSMOutputTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectorTypeDef

### connectorId
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### capabilityList
- **Type**: typing.Optional[typing.List[typing.Literal['HYPERV-MANAGER', 'SCVMM', 'SMS_OPTIMIZED', 'SNAPSHOT_BATCHING', 'VSPHERE']]]

### vmManagerName
- **Type**: typing.Optional[str]

### vmManagerType
- **Type**: typing.Optional[typing.Literal['HYPERV-MANAGER', 'SCVMM', 'VSPHERE']]

### vmManagerId
- **Type**: typing.Optional[str]

### ipAddress
- **Type**: typing.Optional[str]

### macAddress
- **Type**: typing.Optional[str]

### associatedOn
- **Type**: typing.Optional[datetime.datetime]


# CreateAppRequestTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### serverGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupUnionTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]]


# CreateAppResponseTypeDef

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationJobRequestTypeDef

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### seedReplicationTime
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.TimestampTypeDef'>
- **Required**: Yes

### frequency
- **Type**: typing.Optional[int]

### runOnce
- **Type**: typing.Optional[bool]

### licenseType
- **Type**: typing.Optional[typing.Literal['AWS', 'BYOL']]

### roleName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### numberOfRecentAmisToKeep
- **Type**: typing.Optional[int]

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]


# CreateReplicationJobResponseTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppLaunchConfigurationRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# DeleteAppReplicationConfigurationRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# DeleteAppRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### forceStopAppReplication
- **Type**: typing.Optional[bool]

### forceTerminateApp
- **Type**: typing.Optional[bool]


# DeleteAppValidationConfigurationRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationJobRequestTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateConnectorRequestTypeDef

### connectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateChangeSetRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### changesetFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GenerateChangeSetResponseTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.S3LocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateTemplateRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### templateFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GenerateTemplateResponseTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.S3LocationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppLaunchConfigurationRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# GetAppLaunchConfigurationResponseTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### roleName
- **Type**: <class 'str'>
- **Required**: Yes

### autoLaunch
- **Type**: <class 'bool'>
- **Required**: Yes

### serverGroupLaunchConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupLaunchConfigurationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppReplicationConfigurationRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# GetAppReplicationConfigurationResponseTypeDef

### serverGroupReplicationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupReplicationConfigurationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# GetAppResponseTypeDef

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppValidationConfigurationRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppValidationConfigurationResponseTypeDef

### appValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.AppValidationConfigurationTypeDef]
- **Required**: Yes

### serverGroupValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupValidationConfigurationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppValidationOutputRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppValidationOutputResponseTypeDef

### validationOutputList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ValidationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetConnectorsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetConnectorsResponseTypeDef

### connectorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ConnectorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetReplicationJobsRequestPaginateTypeDef

### replicationJobId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetReplicationJobsRequestTypeDef

### replicationJobId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetReplicationJobsResponseTypeDef

### replicationJobList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ReplicationJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetReplicationRunsRequestPaginateTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetReplicationRunsRequestTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetReplicationRunsResponseTypeDef

### replicationJob
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ReplicationJobTypeDef'>
- **Required**: Yes

### replicationRunList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ReplicationRunTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetServersRequestPaginateTypeDef

### vmServerAddressList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.VmServerAddressTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetServersRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### vmServerAddressList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.VmServerAddressTypeDef]]


# GetServersResponseTypeDef

### lastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### serverCatalogStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETED', 'EXPIRED', 'IMPORTING', 'NOT_IMPORTED']
- **Required**: Yes

### serverList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ImportAppCatalogRequestTypeDef

### roleName
- **Type**: typing.Optional[str]


# LaunchAppRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# LaunchDetailsTypeDef

### latestLaunchTime
- **Type**: typing.Optional[datetime.datetime]

### stackName
- **Type**: typing.Optional[str]

### stackId
- **Type**: typing.Optional[str]


# ListAppsRequestPaginateTypeDef

### appIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# ListAppsRequestTypeDef

### appIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAppsResponseTypeDef

### apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NotificationContextTypeDef

### validationId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'READY_FOR_VALIDATION', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# NotifyAppValidationOutputRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### notificationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.NotificationContextTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAppLaunchConfigurationRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### autoLaunch
- **Type**: typing.Optional[bool]

### serverGroupLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupLaunchConfigurationUnionTypeDef]]


# PutAppReplicationConfigurationRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### serverGroupReplicationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupReplicationConfigurationUnionTypeDef]]


# PutAppValidationConfigurationRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.AppValidationConfigurationTypeDef]]

### serverGroupValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupValidationConfigurationUnionTypeDef]]


# ReplicationJobTypeDef

### replicationJobId
- **Type**: typing.Optional[str]

### serverId
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['VIRTUAL_MACHINE']]

### vmServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.VmServerTypeDef]

### seedReplicationTime
- **Type**: typing.Optional[datetime.datetime]

### frequency
- **Type**: typing.Optional[int]

### runOnce
- **Type**: typing.Optional[bool]

### nextReplicationRunStartTime
- **Type**: typing.Optional[datetime.datetime]

### licenseType
- **Type**: typing.Optional[typing.Literal['AWS', 'BYOL']]

### roleName
- **Type**: typing.Optional[str]

### latestAmiId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'FAILING', 'PAUSED_ON_FAILURE', 'PENDING']]

### statusMessage
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### numberOfRecentAmisToKeep
- **Type**: typing.Optional[int]

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]

### replicationRunList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ReplicationRunTypeDef]]


# ReplicationRunStageDetailsTypeDef

### stage
- **Type**: typing.Optional[str]

### stageProgress
- **Type**: typing.Optional[str]


# ReplicationRunTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# SSMOutputTypeDef

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3LocationTypeDef]


# SSMValidationParametersTypeDef

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.SourceTypeDef]

### instanceId
- **Type**: typing.Optional[str]

### scriptType
- **Type**: typing.Optional[typing.Literal['POWERSHELL_SCRIPT', 'SHELL_SCRIPT']]

### command
- **Type**: typing.Optional[str]

### executionTimeoutSeconds
- **Type**: typing.Optional[int]

### outputS3BucketName
- **Type**: typing.Optional[str]


# ServerGroupLaunchConfigurationOutputTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### launchOrder
- **Type**: typing.Optional[int]

### serverLaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerLaunchConfigurationTypeDef]]


# ServerGroupLaunchConfigurationTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### launchOrder
- **Type**: typing.Optional[int]

### serverLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerLaunchConfigurationTypeDef]]


# ServerGroupLaunchConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerGroupOutputTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]]


# ServerGroupReplicationConfigurationOutputTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### serverReplicationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationConfigurationOutputTypeDef]]


# ServerGroupReplicationConfigurationTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### serverReplicationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationConfigurationUnionTypeDef]]


# ServerGroupReplicationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerGroupTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]]


# ServerGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerGroupValidationConfigurationOutputTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### serverValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerValidationConfigurationTypeDef]]


# ServerGroupValidationConfigurationTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### serverValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerValidationConfigurationTypeDef]]


# ServerGroupValidationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerLaunchConfigurationTypeDef

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]

### logicalId
- **Type**: typing.Optional[str]

### vpc
- **Type**: typing.Optional[str]

### subnet
- **Type**: typing.Optional[str]

### securityGroup
- **Type**: typing.Optional[str]

### ec2KeyName
- **Type**: typing.Optional[str]

### userData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.UserDataTypeDef]

### instanceType
- **Type**: typing.Optional[str]

### associatePublicIpAddress
- **Type**: typing.Optional[bool]

### iamInstanceProfileName
- **Type**: typing.Optional[str]

### configureScript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3LocationTypeDef]

### configureScriptType
- **Type**: typing.Optional[typing.Literal['POWERSHELL_SCRIPT', 'SHELL_SCRIPT']]


# ServerReplicationConfigurationOutputTypeDef

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]

### serverReplicationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationParametersOutputTypeDef]


# ServerReplicationConfigurationTypeDef

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]

### serverReplicationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationParametersUnionTypeDef]


# ServerReplicationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerReplicationParametersOutputTypeDef

### seedTime
- **Type**: typing.Optional[datetime.datetime]

### frequency
- **Type**: typing.Optional[int]

### runOnce
- **Type**: typing.Optional[bool]

### licenseType
- **Type**: typing.Optional[typing.Literal['AWS', 'BYOL']]

### numberOfRecentAmisToKeep
- **Type**: typing.Optional[int]

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]


# ServerReplicationParametersTypeDef

### seedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.TimestampTypeDef]

### frequency
- **Type**: typing.Optional[int]

### runOnce
- **Type**: typing.Optional[bool]

### licenseType
- **Type**: typing.Optional[typing.Literal['AWS', 'BYOL']]

### numberOfRecentAmisToKeep
- **Type**: typing.Optional[int]

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]


# ServerReplicationParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerTypeDef

### serverId
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['VIRTUAL_MACHINE']]

### vmServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.VmServerTypeDef]

### replicationJobId
- **Type**: typing.Optional[str]

### replicationJobTerminated
- **Type**: typing.Optional[bool]


# ServerValidationConfigurationTypeDef

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]

### validationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverValidationStrategy
- **Type**: typing.Optional[typing.Literal['USERDATA']]

### userDataValidationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.UserDataValidationParametersTypeDef]


# ServerValidationOutputTypeDef

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]


# SourceTypeDef

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3LocationTypeDef]


# StartAppReplicationRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# StartOnDemandAppReplicationRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartOnDemandReplicationRunRequestTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartOnDemandReplicationRunResponseTypeDef

### replicationRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAppReplicationRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TerminateAppRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateAppRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### serverGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupUnionTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]]


# UpdateAppResponseTypeDef

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupOutputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReplicationJobRequestTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### frequency
- **Type**: typing.Optional[int]

### nextReplicationRunStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.TimestampTypeDef]

### licenseType
- **Type**: typing.Optional[typing.Literal['AWS', 'BYOL']]

### roleName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### numberOfRecentAmisToKeep
- **Type**: typing.Optional[int]

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]


# UserDataTypeDef

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3LocationTypeDef]


# UserDataValidationParametersTypeDef

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.SourceTypeDef]

### scriptType
- **Type**: typing.Optional[typing.Literal['POWERSHELL_SCRIPT', 'SHELL_SCRIPT']]


# ValidationOutputTypeDef

### validationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'READY_FOR_VALIDATION', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]

### latestValidationTime
- **Type**: typing.Optional[datetime.datetime]

### appValidationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.AppValidationOutputTypeDef]

### serverValidationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerValidationOutputTypeDef]


# VmServerAddressTypeDef

### vmManagerId
- **Type**: typing.Optional[str]

### vmId
- **Type**: typing.Optional[str]


# VmServerTypeDef

### vmServerAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.VmServerAddressTypeDef]

### vmName
- **Type**: typing.Optional[str]

### vmManagerName
- **Type**: typing.Optional[str]

### vmManagerType
- **Type**: typing.Optional[typing.Literal['HYPERV-MANAGER', 'SCVMM', 'VSPHERE']]

### vmPath
- **Type**: typing.Optional[str]


