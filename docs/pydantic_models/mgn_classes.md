# mgn_classes

# ApplicationAggregatedStatusTypeDef

### healthStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'HEALTHY', 'LAGGING']]

### lastUpdateDateTime
- **Type**: typing.Optional[str]

### progressStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'IN_PROGRESS', 'NOT_STARTED']]

### totalSourceServers
- **Type**: typing.Optional[int]


# ApplicationResponseTypeDef

### applicationAggregatedStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ApplicationAggregatedStatusTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationTypeDef

### applicationAggregatedStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ApplicationAggregatedStatusTypeDef]

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


# ArchiveApplicationRequestRequestTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# ArchiveWaveRequestRequestTypeDef

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# AssociateApplicationsRequestRequestTypeDef

### applicationIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# AssociateSourceServersRequestRequestTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CPUTypeDef

### cores
- **Type**: typing.Optional[int]

### modelName
- **Type**: typing.Optional[str]


# ChangeServerLifeCycleStateRequestRequestTypeDef

### lifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ChangeServerLifeCycleStateSourceServerLifecycleTypeDef'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# ChangeServerLifeCycleStateSourceServerLifecycleTypeDef

### state
- **Type**: typing.Literal['CUTOVER', 'READY_FOR_CUTOVER', 'READY_FOR_TEST']
- **Required**: Yes


# ConnectorResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ConnectorSsmCommandConfigTypeDef'>
- **Required**: Yes

### ssmInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectorSsmCommandConfigTypeDef

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


# ConnectorTypeDef

### arn
- **Type**: typing.Optional[str]

### connectorID
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### ssmCommandConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ConnectorSsmCommandConfigTypeDef]

### ssmInstanceID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateApplicationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConnectorRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ssmInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### ssmCommandConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ConnectorSsmCommandConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLaunchConfigurationTemplateRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsTypeDef]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# CreateReplicationConfigurationTemplateRequestRequestTypeDef

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

### ebsEncryptionKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# CreateWaveRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DataReplicationErrorTypeDef

### error
- **Type**: typing.Optional[typing.Literal['AGENT_NOT_SEEN', 'FAILED_TO_ATTACH_STAGING_DISKS', 'FAILED_TO_AUTHENTICATE_WITH_SERVICE', 'FAILED_TO_BOOT_REPLICATION_SERVER', 'FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER', 'FAILED_TO_CREATE_SECURITY_GROUP', 'FAILED_TO_CREATE_STAGING_DISKS', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE', 'FAILED_TO_LAUNCH_REPLICATION_SERVER', 'FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT', 'FAILED_TO_START_DATA_TRANSFER', 'LAST_SNAPSHOT_JOB_FAILED', 'NOT_CONVERGING', 'SNAPSHOTS_FAILURE', 'UNSTABLE_NETWORK', 'UNSUPPORTED_VM_CONFIGURATION']]

### rawError
- **Type**: typing.Optional[str]


# DataReplicationInfoReplicatedDiskTypeDef

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


# DataReplicationInfoTypeDef

### dataReplicationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DataReplicationErrorTypeDef]

### dataReplicationInitiation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DataReplicationInitiationTypeDef]

### dataReplicationState
- **Type**: typing.Optional[typing.Literal['BACKLOG', 'CONTINUOUS', 'CREATING_SNAPSHOT', 'DISCONNECTED', 'INITIAL_SYNC', 'INITIATING', 'PAUSED', 'PENDING_SNAPSHOT_SHIPPING', 'RESCAN', 'SHIPPING_SNAPSHOT', 'STALLED', 'STOPPED']]

### etaDateTime
- **Type**: typing.Optional[str]

### lagDuration
- **Type**: typing.Optional[str]

### lastSnapshotDateTime
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.DataReplicationInfoReplicatedDiskTypeDef]]


# DataReplicationInitiationStepTypeDef

### name
- **Type**: typing.Optional[typing.Literal['ATTACH_STAGING_DISKS', 'AUTHENTICATE_WITH_SERVICE', 'BOOT_REPLICATION_SERVER', 'CONNECT_AGENT_TO_REPLICATION_SERVER', 'CREATE_SECURITY_GROUP', 'CREATE_STAGING_DISKS', 'DOWNLOAD_REPLICATION_SOFTWARE', 'LAUNCH_REPLICATION_SERVER', 'PAIR_REPLICATION_SERVER_WITH_AGENT', 'START_DATA_TRANSFER', 'WAIT']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SKIPPED', 'SUCCEEDED']]


# DataReplicationInitiationTypeDef

### nextAttemptDateTime
- **Type**: typing.Optional[str]

### startDateTime
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.DataReplicationInitiationStepTypeDef]]


# DeleteApplicationRequestRequestTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DeleteConnectorRequestRequestTypeDef

### connectorID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobRequestRequestTypeDef

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DeleteLaunchConfigurationTemplateRequestRequestTypeDef

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigurationTemplateRequestRequestTypeDef

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceServerRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DeleteVcenterClientRequestRequestTypeDef

### vcenterClientID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWaveRequestRequestTypeDef

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DescribeJobLogItemsRequestDescribeJobLogItemsPaginateTypeDef

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# DescribeJobLogItemsRequestRequestTypeDef

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobLogItemsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.JobLogTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobsRequestDescribeJobsPaginateTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DescribeJobsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# DescribeJobsRequestFiltersTypeDef

### fromDate
- **Type**: typing.Optional[str]

### jobIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### toDate
- **Type**: typing.Optional[str]


# DescribeJobsRequestRequestTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DescribeJobsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsResponsePaginatorTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.JobPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.JobTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLaunchConfigurationTemplatesRequestDescribeLaunchConfigurationTemplatesPaginateTypeDef

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# DescribeLaunchConfigurationTemplatesRequestRequestTypeDef

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesResponsePaginatorTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.LaunchConfigurationTemplatePaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLaunchConfigurationTemplatesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.LaunchConfigurationTemplateTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationConfigurationTemplatesRequestDescribeReplicationConfigurationTemplatesPaginateTypeDef

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# DescribeReplicationConfigurationTemplatesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeReplicationConfigurationTemplatesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ReplicationConfigurationTemplateTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSourceServersRequestDescribeSourceServersPaginateTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DescribeSourceServersRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# DescribeSourceServersRequestFiltersTypeDef

### applicationIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### isArchived
- **Type**: typing.Optional[bool]

### lifeCycleStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CUTOVER', 'CUTTING_OVER', 'DISCONNECTED', 'DISCOVERED', 'NOT_READY', 'PENDING_INSTALLATION', 'READY_FOR_CUTOVER', 'READY_FOR_TEST', 'STOPPED', 'TESTING']]]

### replicationTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']]]

### sourceServerIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeSourceServersRequestRequestTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DescribeSourceServersRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.SourceServerTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVcenterClientsRequestDescribeVcenterClientsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# DescribeVcenterClientsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeVcenterClientsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.VcenterClientTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateApplicationsRequestRequestTypeDef

### applicationIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DisassociateSourceServersRequestRequestTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DisconnectFromServiceRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# DiskTypeDef

### bytes
- **Type**: typing.Optional[int]

### deviceName
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportErrorDataTypeDef

### rawError
- **Type**: typing.Optional[str]


# ExportTaskErrorTypeDef

### errorData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ExportErrorDataTypeDef]

### errorDateTime
- **Type**: typing.Optional[str]


# ExportTaskSummaryTypeDef

### applicationsCount
- **Type**: typing.Optional[int]

### serversCount
- **Type**: typing.Optional[int]

### wavesCount
- **Type**: typing.Optional[int]


# ExportTaskTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ExportTaskSummaryTypeDef]


# FinalizeCutoverRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# GetLaunchConfigurationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# GetReplicationConfigurationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# IdentificationHintsTypeDef

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


# ImportErrorDataTypeDef

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


# ImportTaskErrorTypeDef

### errorData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ImportErrorDataTypeDef]

### errorDateTime
- **Type**: typing.Optional[str]

### errorType
- **Type**: typing.Optional[typing.Literal['PROCESSING_ERROR', 'VALIDATION_ERROR']]


# ImportTaskSummaryApplicationsTypeDef

### createdCount
- **Type**: typing.Optional[int]

### modifiedCount
- **Type**: typing.Optional[int]


# ImportTaskSummaryServersTypeDef

### createdCount
- **Type**: typing.Optional[int]

### modifiedCount
- **Type**: typing.Optional[int]


# ImportTaskSummaryTypeDef

### applications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ImportTaskSummaryApplicationsTypeDef]

### servers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ImportTaskSummaryServersTypeDef]

### waves
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ImportTaskSummaryWavesTypeDef]


# ImportTaskSummaryWavesTypeDef

### createdCount
- **Type**: typing.Optional[int]

### modifiedCount
- **Type**: typing.Optional[int]


# ImportTaskTypeDef

### creationDateTime
- **Type**: typing.Optional[str]

### endDateTime
- **Type**: typing.Optional[str]

### importID
- **Type**: typing.Optional[str]

### progressPercentage
- **Type**: typing.Optional[float]

### s3BucketSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.S3BucketSourceTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STARTED', 'SUCCEEDED']]

### summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ImportTaskSummaryTypeDef]


# JobLogEventDataTypeDef

### conversionServerID
- **Type**: typing.Optional[str]

### rawError
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]

### targetInstanceID
- **Type**: typing.Optional[str]


# JobLogTypeDef

### event
- **Type**: typing.Optional[typing.Literal['CLEANUP_END', 'CLEANUP_FAIL', 'CLEANUP_START', 'CONVERSION_END', 'CONVERSION_FAIL', 'CONVERSION_START', 'JOB_CANCEL', 'JOB_END', 'JOB_START', 'LAUNCH_FAILED', 'LAUNCH_START', 'SERVER_SKIPPED', 'SNAPSHOT_END', 'SNAPSHOT_FAIL', 'SNAPSHOT_START', 'USING_PREVIOUS_SNAPSHOT']]

### eventData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.JobLogEventDataTypeDef]

### logDateTime
- **Type**: typing.Optional[str]


# JobPaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.ParticipatingServerPaginatorTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'STARTED']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['LAUNCH', 'TERMINATE']]


# JobPostLaunchActionsLaunchStatusPaginatorTypeDef

### executionID
- **Type**: typing.Optional[str]

### executionStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### failureReason
- **Type**: typing.Optional[str]

### ssmDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SsmDocumentPaginatorTypeDef]

### ssmDocumentType
- **Type**: typing.Optional[typing.Literal['AUTOMATION', 'COMMAND']]


# JobPostLaunchActionsLaunchStatusTypeDef

### executionID
- **Type**: typing.Optional[str]

### executionStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### failureReason
- **Type**: typing.Optional[str]

### ssmDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SsmDocumentTypeDef]

### ssmDocumentType
- **Type**: typing.Optional[typing.Literal['AUTOMATION', 'COMMAND']]


# JobTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.ParticipatingServerTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'PENDING', 'STARTED']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['LAUNCH', 'TERMINATE']]


# LaunchConfigurationTemplatePaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsPaginatorTypeDef]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# LaunchConfigurationTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef'>
- **Required**: Yes

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### launchDisposition
- **Type**: typing.Literal['STARTED', 'STOPPED']
- **Required**: Yes

### licensing
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef'>
- **Required**: Yes

### mapAutoTaggingMpeID
- **Type**: <class 'str'>
- **Required**: Yes

### postLaunchActions
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsTypeDef'>
- **Required**: Yes

### smallVolumeConf
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LaunchConfigurationTemplateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsTypeDef]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# LaunchConfigurationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef'>
- **Required**: Yes

### mapAutoTaggingMpeID
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### postLaunchActions
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsTypeDef'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Literal['BASIC', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LaunchTemplateDiskConfTypeDef

### iops
- **Type**: typing.Optional[int]

### throughput
- **Type**: typing.Optional[int]

### volumeType
- **Type**: typing.Optional[typing.Literal['gp2', 'gp3', 'io1', 'io2', 'sc1', 'st1', 'standard']]


# LaunchedInstanceTypeDef

### ec2InstanceID
- **Type**: typing.Optional[str]

### firstBoot
- **Type**: typing.Optional[typing.Literal['STOPPED', 'SUCCEEDED', 'UNKNOWN', 'WAITING']]

### jobID
- **Type**: typing.Optional[str]


# LicensingTypeDef

### osByol
- **Type**: typing.Optional[bool]


# LifeCycleLastCutoverFinalizedTypeDef

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastCutoverInitiatedTypeDef

### apiCallDateTime
- **Type**: typing.Optional[str]

### jobID
- **Type**: typing.Optional[str]


# LifeCycleLastCutoverRevertedTypeDef

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastCutoverTypeDef

### finalized
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastCutoverFinalizedTypeDef]

### initiated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastCutoverInitiatedTypeDef]

### reverted
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastCutoverRevertedTypeDef]


# LifeCycleLastTestFinalizedTypeDef

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastTestInitiatedTypeDef

### apiCallDateTime
- **Type**: typing.Optional[str]

### jobID
- **Type**: typing.Optional[str]


# LifeCycleLastTestRevertedTypeDef

### apiCallDateTime
- **Type**: typing.Optional[str]


# LifeCycleLastTestTypeDef

### finalized
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastTestFinalizedTypeDef]

### initiated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastTestInitiatedTypeDef]

### reverted
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastTestRevertedTypeDef]


# LifeCycleTypeDef

### addedToServiceDateTime
- **Type**: typing.Optional[str]

### elapsedReplicationDuration
- **Type**: typing.Optional[str]

### firstByteDateTime
- **Type**: typing.Optional[str]

### lastCutover
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastCutoverTypeDef]

### lastSeenByServiceDateTime
- **Type**: typing.Optional[str]

### lastTest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleLastTestTypeDef]

### state
- **Type**: typing.Optional[typing.Literal['CUTOVER', 'CUTTING_OVER', 'DISCONNECTED', 'DISCOVERED', 'NOT_READY', 'PENDING_INSTALLATION', 'READY_FOR_CUTOVER', 'READY_FOR_TEST', 'STOPPED', 'TESTING']]


# ListApplicationsRequestFiltersTypeDef

### applicationIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### isArchived
- **Type**: typing.Optional[bool]

### waveIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# ListApplicationsRequestListApplicationsPaginateTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListApplicationsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListApplicationsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ApplicationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConnectorsRequestFiltersTypeDef

### connectorIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# ListConnectorsRequestListConnectorsPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListConnectorsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListConnectorsRequestRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListConnectorsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ConnectorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExportErrorsRequestListExportErrorsPaginateTypeDef

### exportID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListExportErrorsRequestRequestTypeDef

### exportID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExportErrorsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ExportTaskErrorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExportsRequestFiltersTypeDef

### exportIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# ListExportsRequestListExportsPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListExportsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListExportsRequestRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListExportsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExportsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ExportTaskTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportErrorsRequestListImportErrorsPaginateTypeDef

### importID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListImportErrorsRequestRequestTypeDef

### importID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportErrorsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ImportTaskErrorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportsRequestFiltersTypeDef

### importIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# ListImportsRequestListImportsPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListImportsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListImportsRequestRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListImportsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ImportTaskTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedAccountsRequestListManagedAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListManagedAccountsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedAccountsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ManagedAccountTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSourceServerActionsRequestListSourceServerActionsPaginateTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SourceServerActionsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListSourceServerActionsRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SourceServerActionsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSourceServerActionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.SourceServerActionDocumentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateActionsRequestListTemplateActionsPaginateTypeDef

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.TemplateActionsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListTemplateActionsRequestRequestTypeDef

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.TemplateActionsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateActionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.TemplateActionDocumentTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWavesRequestFiltersTypeDef

### isArchived
- **Type**: typing.Optional[bool]

### waveIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# ListWavesRequestListWavesPaginateTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListWavesRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PaginatorConfigTypeDef]


# ListWavesRequestRequestTypeDef

### accountID
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ListWavesRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWavesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.WaveTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedAccountTypeDef

### accountId
- **Type**: typing.Optional[str]


# MarkAsArchivedRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# NetworkInterfaceTypeDef

### ips
- **Type**: typing.Optional[typing.List[str]]

### isPrimary
- **Type**: typing.Optional[bool]

### macAddress
- **Type**: typing.Optional[str]


# OSTypeDef

### fullString
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipatingServerPaginatorTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### launchedEc2InstanceID
- **Type**: typing.Optional[str]

### postLaunchActionsStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsStatusPaginatorTypeDef]


# ParticipatingServerTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### launchedEc2InstanceID
- **Type**: typing.Optional[str]

### postLaunchActionsStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsStatusTypeDef]


# PauseReplicationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# PostLaunchActionsPaginatorTypeDef

### cloudWatchLogGroupName
- **Type**: typing.Optional[str]

### deployment
- **Type**: typing.Optional[typing.Literal['CUTOVER_ONLY', 'TEST_AND_CUTOVER', 'TEST_ONLY']]

### s3LogBucket
- **Type**: typing.Optional[str]

### s3OutputKeyPrefix
- **Type**: typing.Optional[str]

### ssmDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.SsmDocumentPaginatorTypeDef]]


# PostLaunchActionsStatusPaginatorTypeDef

### postLaunchActionsLaunchStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.JobPostLaunchActionsLaunchStatusPaginatorTypeDef]]

### ssmAgentDiscoveryDatetime
- **Type**: typing.Optional[str]


# PostLaunchActionsStatusTypeDef

### postLaunchActionsLaunchStatusList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.JobPostLaunchActionsLaunchStatusTypeDef]]

### ssmAgentDiscoveryDatetime
- **Type**: typing.Optional[str]


# PostLaunchActionsTypeDef

### cloudWatchLogGroupName
- **Type**: typing.Optional[str]

### deployment
- **Type**: typing.Optional[typing.Literal['CUTOVER_ONLY', 'TEST_AND_CUTOVER', 'TEST_ONLY']]

### s3LogBucket
- **Type**: typing.Optional[str]

### s3OutputKeyPrefix
- **Type**: typing.Optional[str]

### ssmDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mgn_classes.SsmDocumentTypeDef]]


# PutSourceServerActionRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# PutTemplateActionRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### operatingSystem
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# RemoveSourceServerActionRequestRequestTypeDef

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# RemoveTemplateActionRequestRequestTypeDef

### actionID
- **Type**: <class 'str'>
- **Required**: Yes

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# ReplicationConfigurationReplicatedDiskTypeDef

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


# ReplicationConfigurationTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicationConfigurationTemplateTypeDef

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


# ReplicationConfigurationTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mgn_classes.ReplicationConfigurationReplicatedDiskTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
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


# ResumeReplicationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# RetryDataReplicationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# S3BucketSourceTypeDef

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Key
- **Type**: <class 'str'>
- **Required**: Yes

### s3BucketOwner
- **Type**: typing.Optional[str]


# SourcePropertiesTypeDef

### cpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.CPUTypeDef]]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.DiskTypeDef]]

### identificationHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.IdentificationHintsTypeDef]

### lastUpdatedDateTime
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mgn_classes.NetworkInterfaceTypeDef]]

### os
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.OSTypeDef]

### ramBytes
- **Type**: typing.Optional[int]

### recommendedInstanceType
- **Type**: typing.Optional[str]


# SourceServerActionDocumentResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]
- **Required**: Yes

### mustSucceedForCutover
- **Type**: <class 'bool'>
- **Required**: Yes

### order
- **Type**: <class 'int'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]
- **Required**: Yes

### timeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceServerActionDocumentTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### order
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# SourceServerActionsRequestFiltersTypeDef

### actionIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# SourceServerConnectorActionTypeDef

### connectorArn
- **Type**: typing.Optional[str]

### credentialsSecretArn
- **Type**: typing.Optional[str]


# SourceServerResponseTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorAction
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.SourceServerConnectorActionTypeDef'>
- **Required**: Yes

### dataReplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.DataReplicationInfoTypeDef'>
- **Required**: Yes

### fqdnForActionFramework
- **Type**: <class 'str'>
- **Required**: Yes

### isArchived
- **Type**: <class 'bool'>
- **Required**: Yes

### launchedInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.LaunchedInstanceTypeDef'>
- **Required**: Yes

### lifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.LifeCycleTypeDef'>
- **Required**: Yes

### replicationType
- **Type**: typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']
- **Required**: Yes

### sourceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.SourcePropertiesTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceServerTypeDef

### applicationID
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### connectorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SourceServerConnectorActionTypeDef]

### dataReplicationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.DataReplicationInfoTypeDef]

### fqdnForActionFramework
- **Type**: typing.Optional[str]

### isArchived
- **Type**: typing.Optional[bool]

### launchedInstance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchedInstanceTypeDef]

### lifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LifeCycleTypeDef]

### replicationType
- **Type**: typing.Optional[typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']]

### sourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SourcePropertiesTypeDef]

### sourceServerID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### userProvidedID
- **Type**: typing.Optional[str]

### vcenterClientID
- **Type**: typing.Optional[str]


# SsmDocumentPaginatorTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### ssmDocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### externalParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# SsmDocumentTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### ssmDocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### externalParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# SsmExternalParameterTypeDef

### dynamicPath
- **Type**: typing.Optional[str]


# SsmParameterStoreParameterTypeDef

### parameterName
- **Type**: <class 'str'>
- **Required**: Yes

### parameterType
- **Type**: typing.Literal['STRING']
- **Required**: Yes


# StartCutoverRequestRequestTypeDef

### sourceServerIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartCutoverResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExportRequestRequestTypeDef

### s3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### s3Key
- **Type**: <class 'str'>
- **Required**: Yes

### s3BucketOwner
- **Type**: typing.Optional[str]


# StartExportResponseTypeDef

### exportTask
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ExportTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportRequestRequestTypeDef

### s3BucketSource
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.S3BucketSourceTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartImportResponseTypeDef

### importTask
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ImportTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReplicationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# StartTestRequestRequestTypeDef

### sourceServerIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartTestResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopReplicationRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateActionDocumentResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]
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
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]
- **Required**: Yes

### timeoutSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TemplateActionDocumentTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.mgn_classes.SsmExternalParameterTypeDef]]

### mustSucceedForCutover
- **Type**: typing.Optional[bool]

### operatingSystem
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.mgn_classes.SsmParameterStoreParameterTypeDef]]]

### timeoutSeconds
- **Type**: typing.Optional[int]


# TemplateActionsRequestFiltersTypeDef

### actionIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# TerminateTargetInstancesRequestRequestTypeDef

### sourceServerIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TerminateTargetInstancesResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UnarchiveApplicationRequestRequestTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# UnarchiveWaveRequestRequestTypeDef

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

### applicationID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# UpdateConnectorRequestRequestTypeDef

### connectorID
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### ssmCommandConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.ConnectorSsmCommandConfigTypeDef]


# UpdateLaunchConfigurationRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsTypeDef]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# UpdateLaunchConfigurationTemplateRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### launchDisposition
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED']]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LicensingTypeDef]

### mapAutoTaggingMpeID
- **Type**: typing.Optional[str]

### postLaunchActions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.PostLaunchActionsTypeDef]

### smallVolumeConf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.LaunchTemplateDiskConfTypeDef]

### smallVolumeMaxSize
- **Type**: typing.Optional[int]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'NONE']]


# UpdateReplicationConfigurationRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mgn_classes.ReplicationConfigurationReplicatedDiskTypeDef]]

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

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# UpdateReplicationConfigurationTemplateRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### stagingAreaSubnetId
- **Type**: typing.Optional[str]

### stagingAreaTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### useDedicatedReplicationServer
- **Type**: typing.Optional[bool]

### useFipsEndpoint
- **Type**: typing.Optional[bool]


# UpdateSourceServerReplicationTypeRequestRequestTypeDef

### replicationType
- **Type**: typing.Literal['AGENT_BASED', 'SNAPSHOT_SHIPPING']
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]


# UpdateSourceServerRequestRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### connectorAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.SourceServerConnectorActionTypeDef]


# UpdateWaveRequestRequestTypeDef

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### accountID
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# VcenterClientTypeDef

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


# WaveAggregatedStatusTypeDef

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


# WaveResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.WaveAggregatedStatusTypeDef'>
- **Required**: Yes

### waveID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mgn_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaveTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mgn_classes.WaveAggregatedStatusTypeDef]

### waveID
- **Type**: typing.Optional[str]


