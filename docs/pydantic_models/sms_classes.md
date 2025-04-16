# Sms Classes

# AppSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.LaunchDetails]

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


# AppValidationConfiguration

### validationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### appValidationStrategy
- **Type**: typing.Optional[typing.Literal['SSM']]

### ssmValidationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.SSMValidationParameters]


# AppValidationOutput

### ssmOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.SSMOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Connector

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


# CreateAppRequest

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### serverGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupUnion]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.Tag]]


# CreateAppResponse

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummary'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupOutput]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationJobRequest

### serverId
- **Type**: <class 'str'>
- **Required**: Yes

### seedReplicationTime
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.Timestamp'>
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


# CreateReplicationJobResponse

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppLaunchConfigurationRequest

### appId
- **Type**: typing.Optional[str]


# DeleteAppReplicationConfigurationRequest

### appId
- **Type**: typing.Optional[str]


# DeleteAppRequest

### appId
- **Type**: typing.Optional[str]

### forceStopAppReplication
- **Type**: typing.Optional[bool]

### forceTerminateApp
- **Type**: typing.Optional[bool]


# DeleteAppValidationConfigurationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationJobRequest

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateConnectorRequest

### connectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateChangeSetRequest

### appId
- **Type**: typing.Optional[str]

### changesetFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GenerateChangeSetResponse

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.S3Location'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateTemplateRequest

### appId
- **Type**: typing.Optional[str]

### templateFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# GenerateTemplateResponse

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.S3Location'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppLaunchConfigurationRequest

### appId
- **Type**: typing.Optional[str]


# GetAppLaunchConfigurationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupLaunchConfigurationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppReplicationConfigurationRequest

### appId
- **Type**: typing.Optional[str]


# GetAppReplicationConfigurationResponse

### serverGroupReplicationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupReplicationConfigurationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppRequest

### appId
- **Type**: typing.Optional[str]


# GetAppResponse

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummary'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupOutput]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppValidationConfigurationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppValidationConfigurationResponse

### appValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.AppValidationConfiguration]
- **Required**: Yes

### serverGroupValidationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupValidationConfigurationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppValidationOutputRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppValidationOutputResponse

### validationOutputList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ValidationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectorsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetConnectorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfig]


# GetConnectorsResponse

### connectorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.Connector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetReplicationJobsRequest

### replicationJobId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetReplicationJobsRequestPaginate

### replicationJobId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfig]


# GetReplicationJobsResponse

### replicationJobList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ReplicationJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetReplicationRunsRequest

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetReplicationRunsRequestPaginate

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfig]


# GetReplicationRunsResponse

### replicationJob
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ReplicationJob'>
- **Required**: Yes

### replicationRunList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ReplicationRun]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetServersRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### vmServerAddressList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.VmServerAddress]]


# GetServersRequestPaginate

### vmServerAddressList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.VmServerAddress]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfig]


# GetServersResponse

### lastModifiedOn
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### serverCatalogStatus
- **Type**: typing.Literal['AVAILABLE', 'DELETED', 'EXPIRED', 'IMPORTING', 'NOT_IMPORTED']
- **Required**: Yes

### serverList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.Server]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ImportAppCatalogRequest

### roleName
- **Type**: typing.Optional[str]


# LaunchAppRequest

### appId
- **Type**: typing.Optional[str]


# LaunchDetails

### latestLaunchTime
- **Type**: typing.Optional[datetime.datetime]

### stackName
- **Type**: typing.Optional[str]

### stackId
- **Type**: typing.Optional[str]


# ListAppsRequest

### appIds
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAppsRequestPaginate

### appIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.PaginatorConfig]


# ListAppsResponse

### apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.AppSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NotificationContext

### validationId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'PENDING', 'READY_FOR_VALIDATION', 'SUCCEEDED']]

### statusMessage
- **Type**: typing.Optional[str]


# NotifyAppValidationOutputRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### notificationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.NotificationContext]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAppLaunchConfigurationRequest

### appId
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### autoLaunch
- **Type**: typing.Optional[bool]

### serverGroupLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupLaunchConfigurationUnion]]


# PutAppReplicationConfigurationRequest

### appId
- **Type**: typing.Optional[str]

### serverGroupReplicationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupReplicationConfigurationUnion]]


# PutAppValidationConfigurationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.AppValidationConfiguration]]

### serverGroupValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupValidationConfigurationUnion]]


# ReplicationJob

### replicationJobId
- **Type**: typing.Optional[str]

### serverId
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['VIRTUAL_MACHINE']]

### vmServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.VmServer]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ReplicationRun]]


# ReplicationRun

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicationRunStageDetails

### stage
- **Type**: typing.Optional[str]

### stageProgress
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


# S3Location

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# SSMOutput

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3Location]


# SSMValidationParameters

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Source]

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


# Server

### serverId
- **Type**: typing.Optional[str]

### serverType
- **Type**: typing.Optional[typing.Literal['VIRTUAL_MACHINE']]

### vmServer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.VmServer]

### replicationJobId
- **Type**: typing.Optional[str]

### replicationJobTerminated
- **Type**: typing.Optional[bool]


# ServerGroup

### serverGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.Server]]


# ServerGroupLaunchConfiguration

### serverGroupId
- **Type**: typing.Optional[str]

### launchOrder
- **Type**: typing.Optional[int]

### serverLaunchConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerLaunchConfiguration]]


# ServerGroupLaunchConfigurationOutput

### serverGroupId
- **Type**: typing.Optional[str]

### launchOrder
- **Type**: typing.Optional[int]

### serverLaunchConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerLaunchConfiguration]]


# ServerGroupLaunchConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerGroupOutput

### serverGroupId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.Server]]


# ServerGroupReplicationConfiguration

### serverGroupId
- **Type**: typing.Optional[str]

### serverReplicationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationConfigurationUnion]]


# ServerGroupReplicationConfigurationOutput

### serverGroupId
- **Type**: typing.Optional[str]

### serverReplicationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationConfigurationOutput]]


# ServerGroupReplicationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerGroupValidationConfiguration

### serverGroupId
- **Type**: typing.Optional[str]

### serverValidationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerValidationConfiguration]]


# ServerGroupValidationConfigurationOutput

### serverGroupId
- **Type**: typing.Optional[str]

### serverValidationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerValidationConfiguration]]


# ServerGroupValidationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerLaunchConfiguration

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Server]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.UserData]

### instanceType
- **Type**: typing.Optional[str]

### associatePublicIpAddress
- **Type**: typing.Optional[bool]

### iamInstanceProfileName
- **Type**: typing.Optional[str]

### configureScript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3Location]

### configureScriptType
- **Type**: typing.Optional[typing.Literal['POWERSHELL_SCRIPT', 'SHELL_SCRIPT']]


# ServerReplicationConfiguration

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Server]

### serverReplicationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationParametersUnion]


# ServerReplicationConfigurationOutput

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Server]

### serverReplicationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerReplicationParametersOutput]


# ServerReplicationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerReplicationParameters

### seedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Timestamp]

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


# ServerReplicationParametersOutput

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


# ServerReplicationParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServerValidationConfiguration

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Server]

### validationId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### serverValidationStrategy
- **Type**: typing.Optional[typing.Literal['USERDATA']]

### userDataValidationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.UserDataValidationParameters]


# ServerValidationOutput

### server
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Server]


# Source

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3Location]


# StartAppReplicationRequest

### appId
- **Type**: typing.Optional[str]


# StartOnDemandAppReplicationRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartOnDemandReplicationRunRequest

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartOnDemandReplicationRunResponse

### replicationRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# StopAppReplicationRequest

### appId
- **Type**: typing.Optional[str]


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TerminateAppRequest

### appId
- **Type**: typing.Optional[str]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateAppRequest

### appId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]

### serverGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.ServerGroupUnion]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sms_classes.Tag]]


# UpdateAppResponse

### appSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.AppSummary'>
- **Required**: Yes

### serverGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.ServerGroupOutput]
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sms_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sms_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReplicationJobRequest

### replicationJobId
- **Type**: <class 'str'>
- **Required**: Yes

### frequency
- **Type**: typing.Optional[int]

### nextReplicationRunStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Timestamp]

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


# UserData

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.S3Location]


# UserDataValidationParameters

### source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.Source]

### scriptType
- **Type**: typing.Optional[typing.Literal['POWERSHELL_SCRIPT', 'SHELL_SCRIPT']]


# ValidationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.AppValidationOutput]

### serverValidationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.ServerValidationOutput]


# VmServer

### vmServerAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sms_classes.VmServerAddress]

### vmName
- **Type**: typing.Optional[str]

### vmManagerName
- **Type**: typing.Optional[str]

### vmManagerType
- **Type**: typing.Optional[typing.Literal['HYPERV-MANAGER', 'SCVMM', 'VSPHERE']]

### vmPath
- **Type**: typing.Optional[str]


# VmServerAddress

### vmManagerId
- **Type**: typing.Optional[str]

### vmId
- **Type**: typing.Optional[str]


