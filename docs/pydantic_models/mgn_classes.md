# Mgn Classes

# Application

### applicationAggregatedStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ApplicationAggregatedStatus]

### applicationID
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### isArchived
- **Type**: typing.Optional[bool]

### lastModifiedDateTime
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### waveID
- **Type**: typing.Optional[str]


# ApplicationAggregatedStatus

### healthStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'HEALTHY', 'LAGGING']]

### lastUpdateDateTime
- **Type**: typing.Optional[str]

### progressStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### totalSourceServers
- **Type**: typing.Optional[int]


# ApplicationResponse

### applicationAggregatedStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ApplicationAggregatedStatus'>
- **Required**: Yes

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### isArchived
- **Type**: <class 'bool'>
- **Required**: Yes

### lastModifiedDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# ArchiveApplicationRequest

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# ArchiveWaveRequest

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# AssociateApplicationsRequest

### applicationIDs
- **Type**: typing.List[str]
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# AssociateSourceServersRequest

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerIDs
- **Type**: typing.List[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CPU

### cores
- **Type**: typing.Optional[int]

### modelName
- **Type**: typing.Optional[str]


# ChangeServerLifeCycleStateRequest

### lifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ChangeServerLifeCycleStateSourceServerLifecycle'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# ChangeServerLifeCycleStateSourceServerLifecycle

### state
- **Type**: typing.Literal['CUTOVER', 'READY_FOR_CUTOVER', 'READY_FOR_TEST']
- **Required**: Yes


# Connector

### arn
- **Type**: typing.Optional[str]

### connectorID
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### ssmCommandConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ConnectorSsmCommandConfig]

### ssmInstanceID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConnectorResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorID
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ssmCommandConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ConnectorSsmCommandConfig'>
- **Required**: Yes

### ssmInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# ConnectorSsmCommandConfig

### cloudWatchOutputEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### s3OutputEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### cloudWatchLogGroupName
- **Type**: typing.Optional[str]

### outputS3BucketName
- **Type**: typing.Optional[str]


# CreateApplicationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectorRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ssmInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### ssmCommandConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ConnectorSsmCommandConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLaunchConfigurationTemplateRequest

### associatePublicIpAddress
- **Type**: typing.Optional[bool]

### bootMode
- **Type**: typing.Optional[typing.Literal['LEGACY_BIOS', 'UEFI', 'USE_SOURCE']]

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### enableMapAutoTagging
- **Type**: typing.Optional[bool]

### largeVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.Licensing]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActions, aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsOutput, NoneType]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


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
- **Type**: typing.Literal['GP2', 'GP3', 'ST1']
- **Required**: Yes

### ebsEncryption
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
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

### useDedicatedReplicationServer
- **Type**: <class 'bool'>
- **Required**: Yes

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# CreateWaveRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataReplicationError

### error
- **Type**: typing.Optional[typing.Literal['AGENT_NOT_SEEN', 'FAILED_TO_ATTACH_STAGING_DISKS', 'FAILED_TO_AUTHENTICATE_WITH_SERVICE', 'FAILED_TO_BOOT_REPLICATION_SERVER', 'FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER', 'FAILED_TO_CREATE_SECURITY_GROUP', 'FAILED_TO_CREATE_STAGING_DISKS', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE', 'FAILED_TO_LAUNCH_REPLICATION_SERVER', 'FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT', 'FAILED_TO_START_DATA_TRANSFER', 'LAST_SNAPSHOT_JOB_FAILED', 'NOT_CONVERGING', 'SNAPSHOTS_FAILURE', 'UNSTABLE_NETWORK', 'UNSUPPORTED_VM_CONFIGURATION']]

### rawError
- **Type**: typing.Optional[str]


# DataReplicationInfo

### dataReplicationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DataReplicationError]

### dataReplicationInitiation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DataReplicationInitiation]

### dataReplicationState
- **Type**: typing.Optional[typing.Literal['BACKLOG', 'CONTINUOUS', 'CREATING_SNAPSHOT', 'DISCONNECTED', 'INITIAL_SYNC', 'INITIATING', 'PAUSED', 'PENDING_SNAPSHOT_SHIPPING', 'RESCAN', 'SHIPPING_SNAPSHOT', 'STALLED', 'STOPPED']]

### etaDateTime
- **Type**: typing.Optional[str]

### lagDuration
- **Type**: typing.Optional[str]

### lastSnapshotDateTime
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.DataReplicationInfoReplicatedDisk]]


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


# DataReplicationInitiation

### nextAttemptDateTime
- **Type**: typing.Optional[str]

### startDateTime
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.DataReplicationInitiationStep]]


# DataReplicationInitiationStep

### name
- **Type**: typing.Optional[typing.Literal['ATTACH_STAGING_DISKS', 'AUTHENTICATE_WITH_SERVICE', 'BOOT_REPLICATION_SERVER', 'CONNECT_AGENT_TO_REPLICATION_SERVER', 'CREATE_SECURITY_GROUP', 'CREATE_STAGING_DISKS', 'DOWNLOAD_REPLICATION_SOFTWARE', 'LAUNCH_REPLICATION_SERVER', 'PAIR_REPLICATION_SERVER_WITH_AGENT', 'START_DATA_TRANSFER', 'WAIT']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SKIPPED', 'SUCCEEDED']]


# DeleteApplicationRequest

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DeleteConnectorRequest

### connectorID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobRequest

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DeleteLaunchConfigurationTemplateRequest

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigurationTemplateRequest

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceServerRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DeleteVcenterClientRequest

### vcenterClientID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWaveRequest

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DescribeJobLogItemsRequest

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobLogItemsRequestPaginate

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# DescribeJobLogItemsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.JobLog]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequest

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DescribeJobsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequestFilters

### fromDate
- **Type**: typing.Optional[str]

### jobIDs
- **Type**: typing.Optional[typing.List[str]]

### toDate
- **Type**: typing.Optional[str]


# DescribeJobsRequestPaginate

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DescribeJobsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# DescribeJobsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesRequest

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesRequestPaginate

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# DescribeLaunchConfigurationTemplatesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchConfigurationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeReplicationConfigurationTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.List[str]]


# DescribeReplicationConfigurationTemplatesRequestPaginate

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# DescribeReplicationConfigurationTemplatesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ReplicationConfigurationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersRequest

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DescribeSourceServersRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersRequestFilters

### applicationIDs
- **Type**: typing.Optional[typing.List[str]]

### isArchived
- **Type**: typing.Optional[bool]

### lifeCycleStates
- **Type**: typing.Optional[typing.List[typing.Literal['CUTOVER', 'CUTTING_OVER', 'DISCONNECTED', 'DISCOVERED', 'NOT_READY', 'PENDING_INSTALLATION', 'READY_FOR_CUTOVER', 'READY_FOR_TEST', 'STOPPED', 'TESTING']]]

### replicationTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']]]

### sourceServerIDs
- **Type**: typing.Optional[typing.List[str]]


# DescribeSourceServersRequestPaginate

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DescribeSourceServersRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# DescribeSourceServersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeVcenterClientsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeVcenterClientsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# DescribeVcenterClientsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.VcenterClient]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DisassociateApplicationsRequest

### applicationIDs
- **Type**: typing.List[str]
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DisassociateSourceServersRequest

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerIDs
- **Type**: typing.List[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DisconnectFromServiceRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# Disk

### bytes
- **Type**: typing.Optional[int]

### deviceName
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# ExportErrorData

### rawError
- **Type**: typing.Optional[str]


# ExportTask

### creationDateTime
- **Type**: typing.Optional[str]

### endDateTime
- **Type**: typing.Optional[str]

### exportID
- **Type**: typing.Optional[str]

### progressPercentage
- **Type**: typing.Optional[float]

### s3Bucket
- **Type**: typing.Optional[str]

### s3BucketOwner
- **Type**: typing.Optional[str]

### s3Key
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ExportTaskSummary]


# ExportTaskError

### errorData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ExportErrorData]

### errorDateTime
- **Type**: typing.Optional[str]


# ExportTaskSummary

### applicationsCount
- **Type**: typing.Optional[int]

### serversCount
- **Type**: typing.Optional[int]

### wavesCount
- **Type**: typing.Optional[int]


# FinalizeCutoverRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# GetLaunchConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# GetReplicationConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# IdentificationHints

### awsInstanceID
- **Type**: typing.Optional[str]

### fqdn
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### vmPath
- **Type**: typing.Optional[str]

### vmWareUuid
- **Type**: typing.Optional[str]


# ImportErrorData

### accountID
- **Type**: typing.Optional[str]

### applicationID
- **Type**: typing.Optional[str]

### ec2LaunchTemplateID
- **Type**: typing.Optional[str]

### rawError
- **Type**: typing.Optional[str]

### rowNumber
- **Type**: typing.Optional[int]

### sourceServerID
- **Type**: typing.Optional[str]

### waveID
- **Type**: typing.Optional[str]


# ImportTask

### creationDateTime
- **Type**: typing.Optional[str]

### endDateTime
- **Type**: typing.Optional[str]

### importID
- **Type**: typing.Optional[str]

### progressPercentage
- **Type**: typing.Optional[float]

### s3BucketSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.S3BucketSource]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTaskSummary]


# ImportTaskError

### errorData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportErrorData]

### errorDateTime
- **Type**: typing.Optional[str]

### errorType
- **Type**: typing.Optional[typing.Literal['PROCESSING_ERROR', 'VALIDATION_ERROR']]


# ImportTaskSummary

### applications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTaskSummaryApplications]

### servers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTaskSummaryServers]

### waves
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTaskSummaryWaves]


# ImportTaskSummaryApplications

### createdCount
- **Type**: typing.Optional[int]

### modifiedCount
- **Type**: typing.Optional[int]


# ImportTaskSummaryServers

### createdCount
- **Type**: typing.Optional[int]

### modifiedCount
- **Type**: typing.Optional[int]


# ImportTaskSummaryWaves

### createdCount
- **Type**: typing.Optional[int]

### modifiedCount
- **Type**: typing.Optional[int]


# Job

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[str]

### endDateTime
- **Type**: typing.Optional[str]

### initiatedBy
- **Type**: typing.Optional[typing.Literal['DIAGNOSTIC', 'START_CUTOVER', 'START_TEST', 'TERMINATE']]

### participatingServers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ParticipatingServer]]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'STARTED']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['LAUNCH', 'TERMINATE']]


# JobLog

### event
- **Type**: typing.Optional[typing.Literal['CLEANUP_END', 'CLEANUP_FAIL', 'CLEANUP_START', 'CONVERSION_END', 'CONVERSION_FAIL', 'CONVERSION_START', 'JOB_CANCEL', 'JOB_END', 'JOB_START', 'LAUNCH_FAILED', 'LAUNCH_START', 'SERVER_SKIPPED', 'SNAPSHOT_END', 'SNAPSHOT_FAIL', 'SNAPSHOT_START', 'USING_PREVIOUS_SNAPSHOT']]

### eventData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.JobLogEventData]

### logDateTime
- **Type**: typing.Optional[str]


# JobLogEventData

### conversionServerID
- **Type**: typing.Optional[str]

### rawError
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]

### targetInstanceID
- **Type**: typing.Optional[str]


# JobPostLaunchActionsLaunchStatus

### executionID
- **Type**: typing.Optional[str]

### executionStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### failureReason
- **Type**: typing.Optional[str]

### ssmDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmDocumentOutput]

### ssmDocumentType
- **Type**: typing.Optional[typing.Literal['AUTOMATION', 'COMMAND']]


# LaunchConfiguration

### bootMode
- **Type**: typing.Literal['LEGACY_BIOS', 'UEFI', 'USE_SOURCE']
- **Required**: Yes

### copyPrivateIp
- **Type**: <class 'bool'>
- **Required**: Yes

### copyTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ec2LaunchTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### enableMapAutoTagging
- **Type**: <class 'bool'>
- **Required**: Yes

### launchDisposition
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### licensing
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.Licensing'>
- **Required**: Yes

### mapAutoTaggingMpeID
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### postLaunchActions
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsOutput'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Literal['BASIC', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# LaunchConfigurationTemplate

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### associatePublicIpAddress
- **Type**: typing.Optional[bool]

### bootMode
- **Type**: typing.Optional[typing.Literal['LEGACY_BIOS', 'UEFI', 'USE_SOURCE']]

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### ec2LaunchTemplateID
- **Type**: typing.Optional[str]

### enableMapAutoTagging
- **Type**: typing.Optional[bool]

### largeVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.Licensing]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsOutput]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# LaunchConfigurationTemplateResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### associatePublicIpAddress
- **Type**: <class 'bool'>
- **Required**: Yes

### bootMode
- **Type**: typing.Literal['LEGACY_BIOS', 'UEFI', 'USE_SOURCE']
- **Required**: Yes

### copyPrivateIp
- **Type**: <class 'bool'>
- **Required**: Yes

### copyTags
- **Type**: <class 'bool'>
- **Required**: Yes

### ec2LaunchTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### enableMapAutoTagging
- **Type**: <class 'bool'>
- **Required**: Yes

### largeVolumeConf
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf'>
- **Required**: Yes

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### launchDisposition
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### licensing
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.Licensing'>
- **Required**: Yes

### mapAutoTaggingMpeID
- **Type**: <class 'str'>
- **Required**: Yes

### postLaunchActions
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsOutput'>
- **Required**: Yes

### smallVolumeConf
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf'>
- **Required**: Yes

### smallVolumeMaxSize
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Literal['BASIC', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# LaunchTemplateDiskConf

### iops
- **Type**: typing.Optional[int]

### throughput
- **Type**: typing.Optional[int]

### volumeType
- **Type**: typing.Optional[typing.Literal['gp2', 'gp3', 'io1', 'io2', 'sc1', 'st1', 'standard']]


# LaunchedInstance

### ec2InstanceID
- **Type**: typing.Optional[str]

### firstBoot
- **Type**: typing.Optional[typing.Literal['STOPPED', 'SUCCEEDED', 'UNKNOWN', 'WAITING']]

### jobID
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

### lastCutover
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastCutover]

### lastSeenByServiceDateTime
- **Type**: typing.Optional[str]

### lastTest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastTest]

### state
- **Type**: typing.Optional[typing.Literal['CUTOVER', 'CUTTING_OVER', 'DISCONNECTED', 'DISCOVERED', 'NOT_READY', 'PENDING_INSTALLATION', 'READY_FOR_CUTOVER', 'READY_FOR_TEST', 'STOPPED', 'TESTING']]


# LifeCycleLastCutover

### finalized
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastCutoverFinalized]

### initiated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastCutoverInitiated]

### reverted
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastCutoverReverted]


# LifeCycleLastCutoverFinalized

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastCutoverInitiated

### apiCallDateTime
- **Type**: typing.Optional[str]

### jobID
- **Type**: typing.Optional[str]


# LifeCycleLastCutoverReverted

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastTest

### finalized
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastTestFinalized]

### initiated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastTestInitiated]

### reverted
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycleLastTestReverted]


# LifeCycleLastTestFinalized

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastTestInitiated

### apiCallDateTime
- **Type**: typing.Optional[str]

### jobID
- **Type**: typing.Optional[str]


# LifeCycleLastTestReverted

### apiCallDateTime
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListApplicationsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestFilters

### applicationIDs
- **Type**: typing.Optional[typing.List[str]]

### isArchived
- **Type**: typing.Optional[bool]

### waveIDs
- **Type**: typing.Optional[typing.List[str]]


# ListApplicationsRequestPaginate

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListApplicationsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListApplicationsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.Application]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListConnectorsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestFilters

### connectorIDs
- **Type**: typing.Optional[typing.List[str]]


# ListConnectorsRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListConnectorsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListConnectorsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.Connector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExportErrorsRequest

### exportID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExportErrorsRequestPaginate

### exportID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListExportErrorsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ExportTaskError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExportsRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListExportsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExportsRequestFilters

### exportIDs
- **Type**: typing.Optional[typing.List[str]]


# ListExportsRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListExportsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListExportsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ExportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportErrorsRequest

### importID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportErrorsRequestPaginate

### importID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListImportErrorsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTaskError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportsRequest

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListImportsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportsRequestFilters

### importIDs
- **Type**: typing.Optional[typing.List[str]]


# ListImportsRequestPaginate

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListImportsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListImportsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedAccountsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListManagedAccountsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ManagedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceServerActionsRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServerActionsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSourceServerActionsRequestPaginate

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServerActionsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListSourceServerActionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServerActionDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplateActionsRequest

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.TemplateActionsRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateActionsRequestPaginate

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.TemplateActionsRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListTemplateActionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.TemplateActionDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWavesRequest

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListWavesRequestFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWavesRequestFilters

### isArchived
- **Type**: typing.Optional[bool]

### waveIDs
- **Type**: typing.Optional[typing.List[str]]


# ListWavesRequestPaginate

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ListWavesRequestFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PaginatorConfig]


# ListWavesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.Wave]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ManagedAccount

### accountId
- **Type**: typing.Optional[str]


# MarkAsArchivedRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipatingServer

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### launchedEc2InstanceID
- **Type**: typing.Optional[str]

### postLaunchActionsStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsStatus]


# PauseReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# PostLaunchActions

### cloudWatchLogGroupName
- **Type**: typing.Optional[str]

### deployment
- **Type**: typing.Optional[typing.Literal['CUTOVER_ONLY', 'TEST_AND_CUTOVER', 'TEST_ONLY']]

### s3LogBucket
- **Type**: typing.Optional[str]

### s3OutputKeyPrefix
- **Type**: typing.Optional[str]

### ssmDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmDocument]]


# PostLaunchActionsOutput

### cloudWatchLogGroupName
- **Type**: typing.Optional[str]

### deployment
- **Type**: typing.Optional[typing.Literal['CUTOVER_ONLY', 'TEST_AND_CUTOVER', 'TEST_ONLY']]

### s3LogBucket
- **Type**: typing.Optional[str]

### s3OutputKeyPrefix
- **Type**: typing.Optional[str]

### ssmDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmDocumentOutput]]


# PostLaunchActionsStatus

### postLaunchActionsLaunchStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.JobPostLaunchActionsLaunchStatus]]

### ssmAgentDiscoveryDatetime
- **Type**: typing.Optional[str]


# PutSourceServerActionRequest

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: <class 'int'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### active
- **Type**: typing.Optional[bool]

### category
- **Type**: typing.Optional[typing.Literal['BACKUP', 'CONFIGURATION', 'DISASTER_RECOVERY', 'LICENSE_AND_SUBSCRIPTION', 'NETWORKING', 'OBSERVABILITY', 'OPERATING_SYSTEM', 'OTHER', 'REFACTORING', 'SECURITY', 'VALIDATION']]

### description
- **Type**: typing.Optional[str]

### documentVersion
- **Type**: typing.Optional[str]

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# PutTemplateActionRequest

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: <class 'int'>
- **Required**: Yes

### active
- **Type**: typing.Optional[bool]

### category
- **Type**: typing.Optional[typing.Literal['BACKUP', 'CONFIGURATION', 'DISASTER_RECOVERY', 'LICENSE_AND_SUBSCRIPTION', 'NETWORKING', 'OBSERVABILITY', 'OPERATING_SYSTEM', 'OTHER', 'REFACTORING', 'SECURITY', 'VALIDATION']]

### description
- **Type**: typing.Optional[str]

### documentVersion
- **Type**: typing.Optional[str]

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### operatingSystem
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# RemoveSourceServerActionRequest

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# RemoveTemplateActionRequest

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# ReplicationConfiguration

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
- **Type**: typing.Literal['GP2', 'GP3', 'ST1']
- **Required**: Yes

### ebsEncryption
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### ebsEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### replicatedDisks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ReplicationConfigurationReplicatedDisk]
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

### useFipsEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# ReplicationConfigurationReplicatedDisk

### deviceName
- **Type**: typing.Optional[str]

### iops
- **Type**: typing.Optional[int]

### isBootDisk
- **Type**: typing.Optional[bool]

### stagingDiskType
- **Type**: typing.Optional[typing.Literal['AUTO', 'GP2', 'GP3', 'IO1', 'IO2', 'SC1', 'ST1', 'STANDARD']]

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

### bandwidthThrottling
- **Type**: typing.Optional[int]

### createPublicIP
- **Type**: typing.Optional[bool]

### dataPlaneRouting
- **Type**: typing.Optional[typing.Literal['PRIVATE_IP', 'PUBLIC_IP']]

### defaultLargeStagingDiskType
- **Type**: typing.Optional[typing.Literal['GP2', 'GP3', 'ST1']]

### ebsEncryption
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

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

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# ReplicationConfigurationTemplateResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

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
- **Type**: typing.Literal['GP2', 'GP3', 'ST1']
- **Required**: Yes

### ebsEncryption
- **Type**: typing.Literal['CUSTOM', 'DEFAULT']
- **Required**: Yes

### ebsEncryptionKeyArn
- **Type**: <class 'str'>
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

### useFipsEndpoint
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
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


# ResumeReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# RetryDataReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# S3BucketSource

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Key
- **Type**: <class 'str'>
- **Required**: Yes

### s3BucketOwner
- **Type**: typing.Optional[str]


# SourceProperties

### cpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.CPU]]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.Disk]]

### identificationHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.IdentificationHints]

### lastUpdatedDateTime
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.NetworkInterface]]

### os
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.OS]

### ramBytes
- **Type**: typing.Optional[int]

### recommendedInstanceType
- **Type**: typing.Optional[str]


# SourceServer

### applicationID
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### connectorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServerConnectorAction]

### dataReplicationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.DataReplicationInfo]

### fqdnForActionFramework
- **Type**: typing.Optional[str]

### isArchived
- **Type**: typing.Optional[bool]

### launchedInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchedInstance]

### lifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycle]

### replicationType
- **Type**: typing.Optional[typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']]

### sourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceProperties]

### sourceServerID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### userProvidedID
- **Type**: typing.Optional[str]

### vcenterClientID
- **Type**: typing.Optional[str]


# SourceServerActionDocument

### actionID
- **Type**: typing.Optional[str]

### actionName
- **Type**: typing.Optional[str]

### active
- **Type**: typing.Optional[bool]

### category
- **Type**: typing.Optional[typing.Literal['BACKUP', 'CONFIGURATION', 'DISASTER_RECOVERY', 'LICENSE_AND_SUBSCRIPTION', 'NETWORKING', 'OBSERVABILITY', 'OPERATING_SYSTEM', 'OTHER', 'REFACTORING', 'SECURITY', 'VALIDATION']]

### description
- **Type**: typing.Optional[str]

### documentIdentifier
- **Type**: typing.Optional[str]

### documentVersion
- **Type**: typing.Optional[str]

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### order
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# SourceServerActionDocumentResponse

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### category
- **Type**: typing.Literal['BACKUP', 'CONFIGURATION', 'DISASTER_RECOVERY', 'LICENSE_AND_SUBSCRIPTION', 'NETWORKING', 'OBSERVABILITY', 'OPERATING_SYSTEM', 'OTHER', 'REFACTORING', 'SECURITY', 'VALIDATION']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### documentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### externalParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]
- **Required**: Yes

### mustSucceedForCutover
- **Type**: <class 'bool'>
- **Required**: Yes

### order
- **Type**: <class 'int'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]
- **Required**: Yes

### timeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# SourceServerActionsRequestFilters

### actionIDs
- **Type**: typing.Optional[typing.List[str]]


# SourceServerConnectorAction

### connectorArn
- **Type**: typing.Optional[str]

### credentialsSecretArn
- **Type**: typing.Optional[str]


# SourceServerResponse

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorAction
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServerConnectorAction'>
- **Required**: Yes

### dataReplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.DataReplicationInfo'>
- **Required**: Yes

### fqdnForActionFramework
- **Type**: <class 'str'>
- **Required**: Yes

### isArchived
- **Type**: <class 'bool'>
- **Required**: Yes

### launchedInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchedInstance'>
- **Required**: Yes

### lifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.LifeCycle'>
- **Required**: Yes

### replicationType
- **Type**: typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']
- **Required**: Yes

### sourceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceProperties'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### userProvidedID
- **Type**: <class 'str'>
- **Required**: Yes

### vcenterClientID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# SsmDocument

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### ssmDocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# SsmDocumentOutput

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### ssmDocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# SsmExternalParameter

### dynamicPath
- **Type**: typing.Optional[str]


# SsmParameterStoreParameter

### parameterName
- **Type**: <class 'str'>
- **Required**: Yes

### parameterType
- **Type**: typing.Literal['STRING']
- **Required**: Yes


# StartCutoverRequest

### sourceServerIDs
- **Type**: typing.List[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartCutoverResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# StartExportRequest

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Key
- **Type**: <class 'str'>
- **Required**: Yes

### s3BucketOwner
- **Type**: typing.Optional[str]


# StartExportResponse

### exportTask
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ExportTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportRequest

### s3BucketSource
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.S3BucketSource'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartImportResponse

### importTask
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ImportTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# StartReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# StartTestRequest

### sourceServerIDs
- **Type**: typing.List[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartTestResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# StopReplicationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TemplateActionDocument

### actionID
- **Type**: typing.Optional[str]

### actionName
- **Type**: typing.Optional[str]

### active
- **Type**: typing.Optional[bool]

### category
- **Type**: typing.Optional[typing.Literal['BACKUP', 'CONFIGURATION', 'DISASTER_RECOVERY', 'LICENSE_AND_SUBSCRIPTION', 'NETWORKING', 'OBSERVABILITY', 'OPERATING_SYSTEM', 'OTHER', 'REFACTORING', 'SECURITY', 'VALIDATION']]

### description
- **Type**: typing.Optional[str]

### documentIdentifier
- **Type**: typing.Optional[str]

### documentVersion
- **Type**: typing.Optional[str]

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### operatingSystem
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# TemplateActionDocumentResponse

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### category
- **Type**: typing.Literal['BACKUP', 'CONFIGURATION', 'DISASTER_RECOVERY', 'LICENSE_AND_SUBSCRIPTION', 'NETWORKING', 'OBSERVABILITY', 'OPERATING_SYSTEM', 'OTHER', 'REFACTORING', 'SECURITY', 'VALIDATION']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### documentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### externalParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmExternalParameter]
- **Required**: Yes

### mustSucceedForCutover
- **Type**: <class 'bool'>
- **Required**: Yes

### operatingSystem
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: <class 'int'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.SsmParameterStoreParameter]]
- **Required**: Yes

### timeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# TemplateActionsRequestFilters

### actionIDs
- **Type**: typing.Optional[typing.List[str]]


# TerminateTargetInstancesRequest

### sourceServerIDs
- **Type**: typing.List[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TerminateTargetInstancesResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


# UnarchiveApplicationRequest

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# UnarchiveWaveRequest

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationRequest

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateConnectorRequest

### connectorID
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### ssmCommandConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.ConnectorSsmCommandConfig]


# UpdateLaunchConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### bootMode
- **Type**: typing.Optional[typing.Literal['LEGACY_BIOS', 'UEFI', 'USE_SOURCE']]

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### enableMapAutoTagging
- **Type**: typing.Optional[bool]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.Licensing]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActions, aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsOutput, NoneType]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# UpdateLaunchConfigurationTemplateRequest

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### associatePublicIpAddress
- **Type**: typing.Optional[bool]

### bootMode
- **Type**: typing.Optional[typing.Literal['LEGACY_BIOS', 'UEFI', 'USE_SOURCE']]

### copyPrivateIp
- **Type**: typing.Optional[bool]

### copyTags
- **Type**: typing.Optional[bool]

### enableMapAutoTagging
- **Type**: typing.Optional[bool]

### largeVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.Licensing]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActions, aws_resource_validator.pydantic_models.mgn.mgn_classes.PostLaunchActionsOutput, NoneType]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.LaunchTemplateDiskConf]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# UpdateReplicationConfigurationRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### associateDefaultSecurityGroup
- **Type**: typing.Optional[bool]

### bandwidthThrottling
- **Type**: typing.Optional[int]

### createPublicIP
- **Type**: typing.Optional[bool]

### dataPlaneRouting
- **Type**: typing.Optional[typing.Literal['PRIVATE_IP', 'PUBLIC_IP']]

### defaultLargeStagingDiskType
- **Type**: typing.Optional[typing.Literal['GP2', 'GP3', 'ST1']]

### ebsEncryption
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn.mgn_classes.ReplicationConfigurationReplicatedDisk]]

### replicationServerInstanceType
- **Type**: typing.Optional[str]

### replicationServersSecurityGroupsIDs
- **Type**: typing.Optional[typing.List[str]]

### stagingAreaSubnetId
- **Type**: typing.Optional[str]

### stagingAreaTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### useDedicatedReplicationServer
- **Type**: typing.Optional[bool]

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# UpdateReplicationConfigurationTemplateRequest

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### associateDefaultSecurityGroup
- **Type**: typing.Optional[bool]

### bandwidthThrottling
- **Type**: typing.Optional[int]

### createPublicIP
- **Type**: typing.Optional[bool]

### dataPlaneRouting
- **Type**: typing.Optional[typing.Literal['PRIVATE_IP', 'PUBLIC_IP']]

### defaultLargeStagingDiskType
- **Type**: typing.Optional[typing.Literal['GP2', 'GP3', 'ST1']]

### ebsEncryption
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'DEFAULT']]

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### replicationServerInstanceType
- **Type**: typing.Optional[str]

### replicationServersSecurityGroupsIDs
- **Type**: typing.Optional[typing.List[str]]

### stagingAreaSubnetId
- **Type**: typing.Optional[str]

### stagingAreaTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### useDedicatedReplicationServer
- **Type**: typing.Optional[bool]

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# UpdateSourceServerReplicationTypeRequest

### replicationType
- **Type**: typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# UpdateSourceServerRequest

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### connectorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.SourceServerConnectorAction]


# UpdateWaveRequest

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# VcenterClient

### arn
- **Type**: typing.Optional[str]

### datacenterName
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### lastSeenDatetime
- **Type**: typing.Optional[str]

### sourceServerTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vcenterClientID
- **Type**: typing.Optional[str]

### vcenterUUID
- **Type**: typing.Optional[str]


# Wave

### arn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### isArchived
- **Type**: typing.Optional[bool]

### lastModifiedDateTime
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### waveAggregatedStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn.mgn_classes.WaveAggregatedStatus]

### waveID
- **Type**: typing.Optional[str]


# WaveAggregatedStatus

### healthStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'HEALTHY', 'LAGGING']]

### lastUpdateDateTime
- **Type**: typing.Optional[str]

### progressStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### replicationStartedDateTime
- **Type**: typing.Optional[str]

### totalApplications
- **Type**: typing.Optional[int]


# WaveResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### isArchived
- **Type**: <class 'bool'>
- **Required**: Yes

### lastModifiedDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### waveAggregatedStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.WaveAggregatedStatus'>
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn.mgn_classes.ResponseMetadata'>
- **Required**: Yes


