# Pydantic Models in sms_classes

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


# CreateAppRequestRequestTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### serverGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]]


# CreateAppResponseTypeDef

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationJobRequestRequestTypeDef

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### seedReplicationTime
- **Type**: typing.Union[datetime.datetime, str]
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


# DeleteAppLaunchConfigurationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# DeleteAppReplicationConfigurationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# DeleteAppRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### forceStopAppReplication
- **Type**: typing.Optional[bool]

### forceTerminateApp
- **Type**: typing.Optional[bool]


# DeleteAppValidationConfigurationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationJobRequestRequestTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateConnectorRequestRequestTypeDef

### connectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateChangeSetRequestRequestTypeDef

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


# GenerateTemplateRequestRequestTypeDef

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


# GetAppLaunchConfigurationRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupLaunchConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppReplicationConfigurationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# GetAppReplicationConfigurationResponseTypeDef

### serverGroupReplicationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupReplicationConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# GetAppResponseTypeDef

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppValidationConfigurationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppValidationConfigurationResponseTypeDef

### appValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.AppValidationConfigurationTypeDef]
- **Required**: Yes

### serverGroupValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupValidationConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppValidationOutputRequestRequestTypeDef

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


# GetConnectorsRequestGetConnectorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetConnectorsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetConnectorsResponseTypeDef

### connectorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ConnectorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef

### replicationJobId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetReplicationJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetReplicationRunsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServersRequestGetServersPaginateTypeDef

### vmServerAddressList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.VmServerAddressTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# GetServersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportAppCatalogRequestRequestTypeDef

### roleName
- **Type**: typing.Optional[str]


# LaunchAppRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# LaunchDetailsTypeDef

### latestLaunchTime
- **Type**: typing.Optional[datetime.datetime]

### stackName
- **Type**: typing.Optional[str]

### stackId
- **Type**: typing.Optional[str]


# ListAppsRequestListAppsPaginateTypeDef

### appIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfigTypeDef]


# ListAppsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotificationContextTypeDef

### validationId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'READY_FOR_VALIDATION', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# NotifyAppValidationOutputRequestRequestTypeDef

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


# PutAppLaunchConfigurationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### autoLaunch
- **Type**: typing.Optional[bool]

### serverGroupLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupLaunchConfigurationTypeDef]]


# PutAppReplicationConfigurationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### serverGroupReplicationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupReplicationConfigurationTypeDef]]


# PutAppValidationConfigurationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.AppValidationConfigurationTypeDef]]

### serverGroupValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupValidationConfigurationTypeDef]]


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

### replicationRunId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'MISSED', 'PENDING']]

### type
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'ON_DEMAND']]

### stageDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ReplicationRunStageDetailsTypeDef]

### statusMessage
- **Type**: typing.Optional[str]

### amiId
- **Type**: typing.Optional[str]

### scheduledStartTime
- **Type**: typing.Optional[datetime.datetime]

### completedTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# ServerGroupLaunchConfigurationTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### launchOrder
- **Type**: typing.Optional[int]

### serverLaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerLaunchConfigurationTypeDef]]


# ServerGroupReplicationConfigurationTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### serverReplicationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationConfigurationTypeDef]]


# ServerGroupTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]]


# ServerGroupValidationConfigurationTypeDef

### serverGroupId
- **Type**: typing.Optional[str]

### serverValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerValidationConfigurationTypeDef]]


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


# ServerReplicationConfigurationTypeDef

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerTypeDef]

### serverReplicationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationParametersTypeDef]


# ServerReplicationParametersTypeDef

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


# StartAppReplicationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# StartOnDemandAppReplicationRequestRequestTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartOnDemandReplicationRunRequestRequestTypeDef

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


# StopAppReplicationRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TerminateAppRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]


# UpdateAppRequestRequestTypeDef

### appId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### serverGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]]


# UpdateAppResponseTypeDef

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummaryTypeDef'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReplicationJobRequestRequestTypeDef

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### frequency
- **Type**: typing.Optional[int]

### nextReplicationRunStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


