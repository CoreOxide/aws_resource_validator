# Drs Classes

# Account

### accountID
- **Type**: typing.Optional[str]


# AssociateSourceNetworkStackRequest

### cfnStackName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateSourceNetworkStackResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CPU

### cores
- **Type**: typing.Optional[int]

### modelName
- **Type**: typing.Optional[str]


# ConversionProperties

### dataTimestamp
- **Type**: typing.Optional[str]

### forceUefi
- **Type**: typing.Optional[bool]

### rootVolumeName
- **Type**: typing.Optional[str]

### volumeToConversionMap
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### volumeToProductCodes
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.drs_classes.ProductCode]]]

### volumeToVolumeSize
- **Type**: typing.Optional[typing.Dict[str, int]]


# CreateExtendedSourceServerRequest

### sourceServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateExtendedSourceServerResponse

### sourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLaunchConfigurationTemplateRequest

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### exportBucketArn
- **Type**: typing.Optional[str]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### launchIntoSourceInstance
- **Type**: typing.Optional[bool]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.Licensing]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# CreateLaunchConfigurationTemplateResponse

### launchConfigurationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LaunchConfigurationTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicationConfigurationTemplateRequest

### associateDefaultSecurityGroup
- **Type**: <class 'bool'>
- **Required**: Yes

### bandwidthThrottling
- **Type**: <class 'int'>
- **Required**: Yes

### createPublicIP
- **Type**: <class 'bool'>
- **Required**: Yes

### dataPlaneRouting
- **Type**: typing.Literal['PRIVATE_IP', 'PUBLIC_IP']
- **Required**: Yes

### defaultLargeStagingDiskType
- **Type**: typing.Literal['AUTO', 'GP2', 'GP3', 'ST1']
- **Required**: Yes

### ebsEncryption
- **Type**: typing.Literal['CUSTOM', 'DEFAULT', 'NONE']
- **Required**: Yes

### pitPolicy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRule]
- **Required**: Yes

### replicationServerInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### replicationServersSecurityGroupsIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### stagingAreaSubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### stagingAreaTags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### useDedicatedReplicationServer
- **Type**: <class 'bool'>
- **Required**: Yes

### autoReplicateNewDisks
- **Type**: typing.Optional[bool]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSourceNetworkRequest

### originAccountID
- **Type**: <class 'str'>
- **Required**: Yes

### originRegion
- **Type**: <class 'str'>
- **Required**: Yes

### vpcID
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSourceNetworkResponse

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# DataReplicationError

### error
- **Type**: typing.Optional[typing.Literal['AGENT_NOT_SEEN', 'FAILED_TO_ATTACH_STAGING_DISKS', 'FAILED_TO_AUTHENTICATE_WITH_SERVICE', 'FAILED_TO_BOOT_REPLICATION_SERVER', 'FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER', 'FAILED_TO_CREATE_SECURITY_GROUP', 'FAILED_TO_CREATE_STAGING_DISKS', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE', 'FAILED_TO_LAUNCH_REPLICATION_SERVER', 'FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT', 'FAILED_TO_START_DATA_TRANSFER', 'NOT_CONVERGING', 'SNAPSHOTS_FAILURE', 'UNSTABLE_NETWORK']]

### rawError
- **Type**: typing.Optional[str]


# DataReplicationInfo

### dataReplicationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DataReplicationError]

### dataReplicationInitiation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInitiation]

### dataReplicationState
- **Type**: typing.Optional[typing.Literal['BACKLOG', 'CONTINUOUS', 'CREATING_SNAPSHOT', 'DISCONNECTED', 'INITIAL_SYNC', 'INITIATING', 'PAUSED', 'RESCAN', 'STALLED', 'STOPPED']]

### etaDateTime
- **Type**: typing.Optional[str]

### lagDuration
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInfoReplicatedDisk]]

### stagingAvailabilityZone
- **Type**: typing.Optional[str]

### stagingOutpostArn
- **Type**: typing.Optional[str]


# DataReplicationInfoReplicatedDisk

### backloggedStorageBytes
- **Type**: typing.Optional[int]

### deviceName
- **Type**: typing.Optional[str]

### replicatedStorageBytes
- **Type**: typing.Optional[int]

### rescannedStorageBytes
- **Type**: typing.Optional[int]

### totalStorageBytes
- **Type**: typing.Optional[int]

### volumeStatus
- **Type**: typing.Optional[typing.Literal['CONTAINS_MARKETPLACE_PRODUCT_CODES', 'MISSING_VOLUME_ATTRIBUTES', 'MISSING_VOLUME_ATTRIBUTES_AND_PRECHECK_UNAVAILABLE', 'PENDING', 'REGULAR']]


# DataReplicationInitiation

### nextAttemptDateTime
- **Type**: typing.Optional[str]

### startDateTime
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInitiationStep]]


# DataReplicationInitiationStep

### name
- **Type**: typing.Optional[typing.Literal['ATTACH_STAGING_DISKS', 'AUTHENTICATE_WITH_SERVICE', 'BOOT_REPLICATION_SERVER', 'CONNECT_AGENT_TO_REPLICATION_SERVER', 'CREATE_SECURITY_GROUP', 'CREATE_STAGING_DISKS', 'DOWNLOAD_REPLICATION_SOFTWARE', 'LAUNCH_REPLICATION_SERVER', 'PAIR_REPLICATION_SERVER_WITH_AGENT', 'START_DATA_TRANSFER', 'WAIT']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SKIPPED', 'SUCCEEDED']]


# DeleteJobRequest

### jobID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchActionRequest

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchConfigurationTemplateRequest

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryInstanceRequest

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigurationTemplateRequest

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceNetworkRequest

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceServerRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobLogItemsRequest

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobLogItemsRequestPaginate

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeJobLogItemsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.JobLog]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeJobsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequestFilters

### fromDate
- **Type**: typing.Optional[str]

### jobIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### toDate
- **Type**: typing.Optional[str]


# DescribeJobsRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeJobsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeJobsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesRequest

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesRequestPaginate

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeLaunchConfigurationTemplatesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.LaunchConfigurationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRecoveryInstancesRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoveryInstancesRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeRecoveryInstancesRequestFilters

### recoveryInstanceIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### sourceServerIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeRecoveryInstancesRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoveryInstancesRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeRecoveryInstancesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRecoverySnapshotsRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoverySnapshotsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# DescribeRecoverySnapshotsRequestFilters

### fromDateTime
- **Type**: typing.Optional[str]

### toDateTime
- **Type**: typing.Optional[str]


# DescribeRecoverySnapshotsRequestPaginate

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoverySnapshotsRequestFilters]

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeRecoverySnapshotsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoverySnapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeReplicationConfigurationTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeReplicationConfigurationTemplatesRequestPaginate

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeReplicationConfigurationTemplatesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.ReplicationConfigurationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceNetworksRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceNetworksRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceNetworksRequestFilters

### originAccountID
- **Type**: typing.Optional[str]

### originRegion
- **Type**: typing.Optional[str]

### sourceNetworkIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeSourceNetworksRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceNetworksRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeSourceNetworksResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.SourceNetwork]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceServersRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersRequestFilters

### hardwareId
- **Type**: typing.Optional[str]

### sourceServerIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### stagingAccountIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeSourceServersRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceServersRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# DescribeSourceServersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.SourceServer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DisconnectRecoveryInstanceRequest

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# DisconnectSourceServerRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# Disk

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# EventResourceData

### sourceNetworkData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.SourceNetworkData]


# ExportSourceNetworkCfnTemplateRequest

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# ExportSourceNetworkCfnTemplateResponse

### s3DestinationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# GetFailbackReplicationConfigurationRequest

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# GetFailbackReplicationConfigurationResponse

### bandwidthThrottling
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### usePrivateIP
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# GetLaunchConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# GetReplicationConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# IdentificationHints

### awsInstanceID
- **Type**: typing.Optional[str]

### fqdn
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### vmWareUuid
- **Type**: typing.Optional[str]


# Job

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobLog

### event
- **Type**: typing.Optional[typing.Literal['CLEANUP_END', 'CLEANUP_FAIL', 'CLEANUP_START', 'CONVERSION_END', 'CONVERSION_FAIL', 'CONVERSION_START', 'DEPLOY_NETWORK_CONFIGURATION_END', 'DEPLOY_NETWORK_CONFIGURATION_FAILED', 'DEPLOY_NETWORK_CONFIGURATION_START', 'JOB_CANCEL', 'JOB_END', 'JOB_START', 'LAUNCH_FAILED', 'LAUNCH_START', 'NETWORK_RECOVERY_FAIL', 'SERVER_SKIPPED', 'SNAPSHOT_END', 'SNAPSHOT_FAIL', 'SNAPSHOT_START', 'UPDATE_LAUNCH_TEMPLATE_END', 'UPDATE_LAUNCH_TEMPLATE_FAILED', 'UPDATE_LAUNCH_TEMPLATE_START', 'UPDATE_NETWORK_CONFIGURATION_END', 'UPDATE_NETWORK_CONFIGURATION_FAILED', 'UPDATE_NETWORK_CONFIGURATION_START', 'USING_PREVIOUS_SNAPSHOT', 'USING_PREVIOUS_SNAPSHOT_FAILED']]

### eventData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.JobLogEventData]

### logDateTime
- **Type**: typing.Optional[str]


# JobLogEventData

### conversionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.ConversionProperties]

### conversionServerID
- **Type**: typing.Optional[str]

### eventResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.EventResourceData]

### rawError
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]

### targetInstanceID
- **Type**: typing.Optional[str]


# LaunchAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchActionParameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchActionRun

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchAction]

### failureReason
- **Type**: typing.Optional[str]

### runId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# LaunchActionsRequestFilters

### actionIds
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchActionsStatus

### runs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.LaunchActionRun]]

### ssmAgentDiscoveryDatetime
- **Type**: typing.Optional[str]


# LaunchConfiguration

### copyPrivateIp
- **Type**: <class 'bool'>
- **Required**: Yes

### copyTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ec2LaunchTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### launchDisposition
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### launchIntoInstanceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LaunchIntoInstanceProperties'>
- **Required**: Yes

### licensing
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.Licensing'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### postLaunchEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Literal['BASIC', 'IN_AWS', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# LaunchConfigurationTemplate

### arn
- **Type**: typing.Optional[str]

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### exportBucketArn
- **Type**: typing.Optional[str]

### launchConfigurationTemplateID
- **Type**: typing.Optional[str]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### launchIntoSourceInstance
- **Type**: typing.Optional[bool]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.Licensing]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# LaunchIntoInstanceProperties

### launchIntoEC2InstanceID
- **Type**: typing.Optional[str]


# Licensing

### osByol
- **Type**: typing.Optional[bool]


# LifeCycle

### addedToServiceDateTime
- **Type**: typing.Optional[str]

### elapsedReplicationDuration
- **Type**: typing.Optional[str]

### firstByteDateTime
- **Type**: typing.Optional[str]

### lastLaunch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LifeCycleLastLaunch]

### lastSeenByServiceDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastLaunch

### initiated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LifeCycleLastLaunchInitiated]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]


# LifeCycleLastLaunchInitiated

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListExtensibleSourceServersRequest

### stagingAccountID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExtensibleSourceServersRequestPaginate

### stagingAccountID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# ListExtensibleSourceServersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.StagingSourceServer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchActionsRequest

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchActionsRequestPaginate

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# ListLaunchActionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.LaunchAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStagingAccountsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStagingAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfig]


# ListStagingAccountsResponse

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.Account]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# NetworkInterface

### ips
- **Type**: typing.Optional[typing.List[str]]

### isPrimary
- **Type**: typing.Optional[bool]

### macAddress
- **Type**: typing.Optional[str]


# OS

### fullString
- **Type**: typing.Optional[str]


# PITPolicyRule

### interval
- **Type**: <class 'int'>
- **Required**: Yes

### retentionDuration
- **Type**: <class 'int'>
- **Required**: Yes

### units
- **Type**: typing.Literal['DAY', 'HOUR', 'MINUTE']
- **Required**: Yes

### enabled
- **Type**: typing.Optional[bool]

### ruleID
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipatingResource

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### participatingResourceID
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.ParticipatingResourceID]


# ParticipatingResourceID

### sourceNetworkID
- **Type**: typing.Optional[str]


# ParticipatingServer

### launchActionsStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionsStatus]

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### recoveryInstanceID
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]


# ProductCode

### productCodeId
- **Type**: typing.Optional[str]

### productCodeMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PutLaunchActionRequest

### actionCode
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### category
- **Type**: typing.Literal['CONFIGURATION', 'MONITORING', 'OTHER', 'SECURITY', 'VALIDATION']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### optional
- **Type**: <class 'bool'>
- **Required**: Yes

### order
- **Type**: <class 'int'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.drs_classes.LaunchActionParameter]]


# RecoveryInstance

### agentVersion
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### dataReplicationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInfo]

### ec2InstanceID
- **Type**: typing.Optional[str]

### ec2InstanceState
- **Type**: typing.Optional[typing.Literal['NOT_FOUND', 'PENDING', 'RUNNING', 'SHUTTING-DOWN', 'STOPPED', 'STOPPING', 'TERMINATED']]

### failback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceFailback]

### isDrill
- **Type**: typing.Optional[bool]

### jobID
- **Type**: typing.Optional[str]

### originAvailabilityZone
- **Type**: typing.Optional[str]

### originEnvironment
- **Type**: typing.Optional[typing.Literal['AWS', 'ON_PREMISES']]

### pointInTimeSnapshotDateTime
- **Type**: typing.Optional[str]

### recoveryInstanceID
- **Type**: typing.Optional[str]

### recoveryInstanceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceProperties]

### sourceOutpostArn
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecoveryInstanceDataReplicationError

### error
- **Type**: typing.Optional[typing.Literal['AGENT_NOT_SEEN', 'FAILBACK_CLIENT_NOT_SEEN', 'FAILED_GETTING_REPLICATION_STATE', 'FAILED_TO_ATTACH_STAGING_DISKS', 'FAILED_TO_AUTHENTICATE_WITH_SERVICE', 'FAILED_TO_BOOT_REPLICATION_SERVER', 'FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE', 'FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER', 'FAILED_TO_CREATE_SECURITY_GROUP', 'FAILED_TO_CREATE_STAGING_DISKS', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT', 'FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION', 'FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION', 'FAILED_TO_LAUNCH_REPLICATION_SERVER', 'FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE', 'FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT', 'FAILED_TO_START_DATA_TRANSFER', 'NOT_CONVERGING', 'SNAPSHOTS_FAILURE', 'UNSTABLE_NETWORK']]

### rawError
- **Type**: typing.Optional[str]


# RecoveryInstanceDataReplicationInfo

### dataReplicationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationError]

### dataReplicationInitiation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInitiation]

### dataReplicationState
- **Type**: typing.Optional[typing.Literal['BACKLOG', 'CONTINUOUS', 'CREATING_SNAPSHOT', 'DISCONNECTED', 'INITIAL_SYNC', 'INITIATING', 'NOT_STARTED', 'PAUSED', 'REPLICATION_STATE_NOT_AVAILABLE', 'RESCAN', 'STALLED', 'STOPPED']]

### etaDateTime
- **Type**: typing.Optional[str]

### lagDuration
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInfoReplicatedDisk]]

### stagingAvailabilityZone
- **Type**: typing.Optional[str]

### stagingOutpostArn
- **Type**: typing.Optional[str]


# RecoveryInstanceDataReplicationInfoReplicatedDisk

### backloggedStorageBytes
- **Type**: typing.Optional[int]

### deviceName
- **Type**: typing.Optional[str]

### replicatedStorageBytes
- **Type**: typing.Optional[int]

### rescannedStorageBytes
- **Type**: typing.Optional[int]

### totalStorageBytes
- **Type**: typing.Optional[int]


# RecoveryInstanceDataReplicationInitiation

### startDateTime
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInitiationStep]]


# RecoveryInstanceDataReplicationInitiationStep

### name
- **Type**: typing.Optional[typing.Literal['ATTACH_STAGING_DISKS', 'AUTHENTICATE_WITH_SERVICE', 'BOOT_REPLICATION_SERVER', 'COMPLETE_VOLUME_MAPPING', 'CONFIGURE_REPLICATION_SOFTWARE', 'CONNECT_AGENT_TO_REPLICATION_SERVER', 'CREATE_SECURITY_GROUP', 'CREATE_STAGING_DISKS', 'DOWNLOAD_REPLICATION_SOFTWARE', 'DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT', 'ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION', 'ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION', 'LAUNCH_REPLICATION_SERVER', 'LINK_FAILBACK_CLIENT_WITH_RECOVERY_INSTANCE', 'PAIR_AGENT_WITH_REPLICATION_SOFTWARE', 'PAIR_REPLICATION_SERVER_WITH_AGENT', 'START_DATA_TRANSFER', 'WAIT']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SKIPPED', 'SUCCEEDED']]


# RecoveryInstanceDisk

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecoveryInstanceFailback

### agentLastSeenByServiceDateTime
- **Type**: typing.Optional[str]

### elapsedReplicationDuration
- **Type**: typing.Optional[str]

### failbackClientID
- **Type**: typing.Optional[str]

### failbackClientLastSeenByServiceDateTime
- **Type**: typing.Optional[str]

### failbackInitiationTime
- **Type**: typing.Optional[str]

### failbackJobID
- **Type**: typing.Optional[str]

### failbackLaunchType
- **Type**: typing.Optional[typing.Literal['DRILL', 'RECOVERY']]

### failbackToOriginalServer
- **Type**: typing.Optional[bool]

### firstByteDateTime
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['FAILBACK_COMPLETED', 'FAILBACK_ERROR', 'FAILBACK_IN_PROGRESS', 'FAILBACK_LAUNCH_STATE_NOT_AVAILABLE', 'FAILBACK_NOT_READY_FOR_LAUNCH', 'FAILBACK_NOT_STARTED', 'FAILBACK_READY_FOR_LAUNCH']]


# RecoveryInstanceProperties

### cpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.CPU]]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDisk]]

### identificationHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.IdentificationHints]

### lastUpdatedDateTime
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.NetworkInterface]]

### os
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.OS]

### ramBytes
- **Type**: typing.Optional[int]


# RecoveryLifeCycle

### apiCallDateTime
- **Type**: typing.Optional[datetime.datetime]

### jobID
- **Type**: typing.Optional[str]

### lastRecoveryResult
- **Type**: typing.Optional[typing.Literal['ASSOCIATE_FAIL', 'ASSOCIATE_SUCCESS', 'FAIL', 'IN_PROGRESS', 'NOT_STARTED', 'PARTIAL_SUCCESS', 'SUCCESS']]


# RecoverySnapshot

### expectedTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### snapshotID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### ebsSnapshots
- **Type**: typing.Optional[typing.List[str]]

### timestamp
- **Type**: typing.Optional[str]


# ReplicationConfiguration

### associateDefaultSecurityGroup
- **Type**: <class 'bool'>
- **Required**: Yes

### autoReplicateNewDisks
- **Type**: <class 'bool'>
- **Required**: Yes

### bandwidthThrottling
- **Type**: <class 'int'>
- **Required**: Yes

### createPublicIP
- **Type**: <class 'bool'>
- **Required**: Yes

### dataPlaneRouting
- **Type**: typing.Literal['PRIVATE_IP', 'PUBLIC_IP']
- **Required**: Yes

### defaultLargeStagingDiskType
- **Type**: typing.Literal['AUTO', 'GP2', 'GP3', 'ST1']
- **Required**: Yes

### ebsEncryption
- **Type**: typing.Literal['CUSTOM', 'DEFAULT', 'NONE']
- **Required**: Yes

### ebsEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pitPolicy
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRule]
- **Required**: Yes

### replicatedDisks
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.ReplicationConfigurationReplicatedDisk]
- **Required**: Yes

### replicationServerInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### replicationServersSecurityGroupsIDs
- **Type**: typing.List[str]
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### stagingAreaSubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### stagingAreaTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### useDedicatedReplicationServer
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# ReplicationConfigurationReplicatedDisk

### deviceName
- **Type**: typing.Optional[str]

### iops
- **Type**: typing.Optional[int]

### isBootDisk
- **Type**: typing.Optional[bool]

### optimizedStagingDiskType
- **Type**: typing.Optional[typing.Literal['AUTO', 'GP2', 'GP3', 'IO1', 'SC1', 'ST1', 'STANDARD']]

### stagingDiskType
- **Type**: typing.Optional[typing.Literal['AUTO', 'GP2', 'GP3', 'IO1', 'SC1', 'ST1', 'STANDARD']]

### throughput
- **Type**: typing.Optional[int]


# ReplicationConfigurationTemplate

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### associateDefaultSecurityGroup
- **Type**: typing.Optional[bool]

### autoReplicateNewDisks
- **Type**: typing.Optional[bool]

### bandwidthThrottling
- **Type**: typing.Optional[int]

### createPublicIP
- **Type**: typing.Optional[bool]

### dataPlaneRouting
- **Type**: typing.Optional[typing.Literal['PRIVATE_IP', 'PUBLIC_IP']]

### defaultLargeStagingDiskType
- **Type**: typing.Optional[typing.Literal['AUTO', 'GP2', 'GP3', 'ST1']]

### ebsEncryption
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT', 'NONE']]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### pitPolicy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRule]]

### replicationServerInstanceType
- **Type**: typing.Optional[str]

### replicationServersSecurityGroupsIDs
- **Type**: typing.Optional[typing.List[str]]

### stagingAreaSubnetId
- **Type**: typing.Optional[str]

### stagingAreaTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### useDedicatedReplicationServer
- **Type**: typing.Optional[bool]


# ReplicationConfigurationTemplateResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### associateDefaultSecurityGroup
- **Type**: <class 'bool'>
- **Required**: Yes

### autoReplicateNewDisks
- **Type**: <class 'bool'>
- **Required**: Yes

### bandwidthThrottling
- **Type**: <class 'int'>
- **Required**: Yes

### createPublicIP
- **Type**: <class 'bool'>
- **Required**: Yes

### dataPlaneRouting
- **Type**: typing.Literal['PRIVATE_IP', 'PUBLIC_IP']
- **Required**: Yes

### defaultLargeStagingDiskType
- **Type**: typing.Literal['AUTO', 'GP2', 'GP3', 'ST1']
- **Required**: Yes

### ebsEncryption
- **Type**: typing.Literal['CUSTOM', 'DEFAULT', 'NONE']
- **Required**: Yes

### ebsEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### pitPolicy
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRule]
- **Required**: Yes

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### replicationServerInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### replicationServersSecurityGroupsIDs
- **Type**: typing.List[str]
- **Required**: Yes

### stagingAreaSubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### stagingAreaTags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### useDedicatedReplicationServer
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
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


# RetryDataReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# ReverseReplicationRequest

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# ReverseReplicationResponse

### reversedDirectionSourceServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# SourceCloudProperties

### originAccountID
- **Type**: typing.Optional[str]

### originAvailabilityZone
- **Type**: typing.Optional[str]

### originRegion
- **Type**: typing.Optional[str]

### sourceOutpostArn
- **Type**: typing.Optional[str]


# SourceNetwork

### arn
- **Type**: typing.Optional[str]

### cfnStackName
- **Type**: typing.Optional[str]

### lastRecovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryLifeCycle]

### launchedVpcID
- **Type**: typing.Optional[str]

### replicationStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'IN_PROGRESS', 'PROTECTED', 'STOPPED']]

### replicationStatusDetails
- **Type**: typing.Optional[str]

### sourceAccountID
- **Type**: typing.Optional[str]

### sourceNetworkID
- **Type**: typing.Optional[str]

### sourceRegion
- **Type**: typing.Optional[str]

### sourceVpcID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SourceNetworkData

### sourceNetworkID
- **Type**: typing.Optional[str]

### sourceVpc
- **Type**: typing.Optional[str]

### stackName
- **Type**: typing.Optional[str]

### targetVpc
- **Type**: typing.Optional[str]


# SourceProperties

### cpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.CPU]]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.Disk]]

### identificationHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.IdentificationHints]

### lastUpdatedDateTime
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.NetworkInterface]]

### os
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.OS]

### ramBytes
- **Type**: typing.Optional[int]

### recommendedInstanceType
- **Type**: typing.Optional[str]

### supportsNitroInstances
- **Type**: typing.Optional[bool]


# SourceServer

### agentVersion
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### dataReplicationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInfo]

### lastLaunchResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCEEDED']]

### lifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LifeCycle]

### recoveryInstanceId
- **Type**: typing.Optional[str]

### replicationDirection
- **Type**: typing.Optional[typing.Literal['FAILBACK', 'FAILOVER']]

### reversedDirectionSourceServerArn
- **Type**: typing.Optional[str]

### sourceCloudProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.SourceCloudProperties]

### sourceNetworkID
- **Type**: typing.Optional[str]

### sourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.SourceProperties]

### sourceServerID
- **Type**: typing.Optional[str]

### stagingArea
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.StagingArea]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SourceServerResponse

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### dataReplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.DataReplicationInfo'>
- **Required**: Yes

### lastLaunchResult
- **Type**: typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### lifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LifeCycle'>
- **Required**: Yes

### recoveryInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### replicationDirection
- **Type**: typing.Literal['FAILBACK', 'FAILOVER']
- **Required**: Yes

### reversedDirectionSourceServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceCloudProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceCloudProperties'>
- **Required**: Yes

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceProperties'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### stagingArea
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.StagingArea'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StagingArea

### errorMessage
- **Type**: typing.Optional[str]

### stagingAccountID
- **Type**: typing.Optional[str]

### stagingSourceServerArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['EXTENDED', 'EXTENSION_ERROR', 'NOT_EXTENDED']]


# StagingSourceServer

### arn
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartFailbackLaunchRequest

### recoveryInstanceIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartFailbackLaunchResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StartRecoveryRequest

### sourceServers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.StartRecoveryRequestSourceServer]
- **Required**: Yes

### isDrill
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartRecoveryRequestSourceServer

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### recoverySnapshotID
- **Type**: typing.Optional[str]


# StartRecoveryResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StartReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# StartReplicationResponse

### sourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StartSourceNetworkRecoveryRequest

### sourceNetworks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.StartSourceNetworkRecoveryRequestNetworkEntry]
- **Required**: Yes

### deployAsNew
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSourceNetworkRecoveryRequestNetworkEntry

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes

### cfnStackName
- **Type**: typing.Optional[str]


# StartSourceNetworkRecoveryResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StartSourceNetworkReplicationRequest

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# StartSourceNetworkReplicationResponse

### sourceNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StopFailbackRequest

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationResponse

### sourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# StopSourceNetworkReplicationRequest

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# StopSourceNetworkReplicationResponse

### sourceNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceNetwork'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TerminateRecoveryInstancesRequest

### recoveryInstanceIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TerminateRecoveryInstancesResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFailbackReplicationConfigurationRequest

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidthThrottling
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### usePrivateIP
- **Type**: typing.Optional[bool]


# UpdateLaunchConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### launchIntoInstanceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchIntoInstanceProperties]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.Licensing]

### name
- **Type**: typing.Optional[str]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# UpdateLaunchConfigurationTemplateRequest

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### exportBucketArn
- **Type**: typing.Optional[str]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### launchIntoSourceInstance
- **Type**: typing.Optional[bool]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.Licensing]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# UpdateLaunchConfigurationTemplateResponse

### launchConfigurationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LaunchConfigurationTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReplicationConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### associateDefaultSecurityGroup
- **Type**: typing.Optional[bool]

### autoReplicateNewDisks
- **Type**: typing.Optional[bool]

### bandwidthThrottling
- **Type**: typing.Optional[int]

### createPublicIP
- **Type**: typing.Optional[bool]

### dataPlaneRouting
- **Type**: typing.Optional[typing.Literal['PRIVATE_IP', 'PUBLIC_IP']]

### defaultLargeStagingDiskType
- **Type**: typing.Optional[typing.Literal['AUTO', 'GP2', 'GP3', 'ST1']]

### ebsEncryption
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT', 'NONE']]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### pitPolicy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRule]]

### replicatedDisks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.ReplicationConfigurationReplicatedDisk]]

### replicationServerInstanceType
- **Type**: typing.Optional[str]

### replicationServersSecurityGroupsIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### stagingAreaSubnetId
- **Type**: typing.Optional[str]

### stagingAreaTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useDedicatedReplicationServer
- **Type**: typing.Optional[bool]


# UpdateReplicationConfigurationTemplateRequest

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### associateDefaultSecurityGroup
- **Type**: typing.Optional[bool]

### autoReplicateNewDisks
- **Type**: typing.Optional[bool]

### bandwidthThrottling
- **Type**: typing.Optional[int]

### createPublicIP
- **Type**: typing.Optional[bool]

### dataPlaneRouting
- **Type**: typing.Optional[typing.Literal['PRIVATE_IP', 'PUBLIC_IP']]

### defaultLargeStagingDiskType
- **Type**: typing.Optional[typing.Literal['AUTO', 'GP2', 'GP3', 'ST1']]

### ebsEncryption
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT', 'NONE']]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### pitPolicy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRule]]

### replicationServerInstanceType
- **Type**: typing.Optional[str]

### replicationServersSecurityGroupsIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### stagingAreaSubnetId
- **Type**: typing.Optional[str]

### stagingAreaTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useDedicatedReplicationServer
- **Type**: typing.Optional[bool]


