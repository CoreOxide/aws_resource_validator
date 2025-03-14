# Drs Classes

# AccountTypeDef

### accountID
- **Type**: typing.Optional[str]


# AssociateSourceNetworkStackRequestTypeDef

### cfnStackName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateSourceNetworkStackResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CPUTypeDef

### cores
- **Type**: typing.Optional[int]

### modelName
- **Type**: typing.Optional[str]


# ConversionPropertiesTypeDef

### dataTimestamp
- **Type**: typing.Optional[str]

### forceUefi
- **Type**: typing.Optional[bool]

### rootVolumeName
- **Type**: typing.Optional[str]

### volumeToConversionMap
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### volumeToProductCodes
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.drs_classes.ProductCodeTypeDef]]]

### volumeToVolumeSize
- **Type**: typing.Optional[typing.Dict[str, int]]


# CreateExtendedSourceServerRequestTypeDef

### sourceServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateExtendedSourceServerResponseTypeDef

### sourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLaunchConfigurationTemplateRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LicensingTypeDef]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# CreateLaunchConfigurationTemplateResponseTypeDef

### launchConfigurationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LaunchConfigurationTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicationConfigurationTemplateRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRuleTypeDef]
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


# CreateSourceNetworkRequestTypeDef

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


# CreateSourceNetworkResponseTypeDef

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataReplicationErrorTypeDef

### error
- **Type**: typing.Optional[typing.Literal['AGENT_NOT_SEEN', 'FAILED_TO_ATTACH_STAGING_DISKS', 'FAILED_TO_AUTHENTICATE_WITH_SERVICE', 'FAILED_TO_BOOT_REPLICATION_SERVER', 'FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER', 'FAILED_TO_CREATE_SECURITY_GROUP', 'FAILED_TO_CREATE_STAGING_DISKS', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE', 'FAILED_TO_LAUNCH_REPLICATION_SERVER', 'FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT', 'FAILED_TO_START_DATA_TRANSFER', 'NOT_CONVERGING', 'SNAPSHOTS_FAILURE', 'UNSTABLE_NETWORK']]

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

### volumeStatus
- **Type**: typing.Optional[typing.Literal['CONTAINS_MARKETPLACE_PRODUCT_CODES', 'MISSING_VOLUME_ATTRIBUTES', 'MISSING_VOLUME_ATTRIBUTES_AND_PRECHECK_UNAVAILABLE', 'PENDING', 'REGULAR']]


# DataReplicationInfoTypeDef

### dataReplicationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DataReplicationErrorTypeDef]

### dataReplicationInitiation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInitiationTypeDef]

### dataReplicationState
- **Type**: typing.Optional[typing.Literal['BACKLOG', 'CONTINUOUS', 'CREATING_SNAPSHOT', 'DISCONNECTED', 'INITIAL_SYNC', 'INITIATING', 'PAUSED', 'RESCAN', 'STALLED', 'STOPPED']]

### etaDateTime
- **Type**: typing.Optional[str]

### lagDuration
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInfoReplicatedDiskTypeDef]]

### stagingAvailabilityZone
- **Type**: typing.Optional[str]

### stagingOutpostArn
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInitiationStepTypeDef]]


# DeleteJobRequestTypeDef

### jobID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchActionRequestTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchConfigurationTemplateRequestTypeDef

### launchConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryInstanceRequestTypeDef

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigurationTemplateRequestTypeDef

### replicationConfigurationTemplateID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceNetworkRequestTypeDef

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceServerRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobLogItemsRequestPaginateTypeDef

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeJobLogItemsRequestTypeDef

### jobID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobLogItemsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.JobLogTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequestFiltersTypeDef

### fromDate
- **Type**: typing.Optional[str]

### jobIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### toDate
- **Type**: typing.Optional[str]


# DescribeJobsRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeJobsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeJobsRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeJobsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesRequestPaginateTypeDef

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeLaunchConfigurationTemplatesRequestTypeDef

### launchConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeLaunchConfigurationTemplatesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.LaunchConfigurationTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRecoveryInstancesRequestFiltersTypeDef

### recoveryInstanceIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### sourceServerIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeRecoveryInstancesRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoveryInstancesRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeRecoveryInstancesRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoveryInstancesRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeRecoveryInstancesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRecoverySnapshotsRequestFiltersTypeDef

### fromDateTime
- **Type**: typing.Optional[str]

### toDateTime
- **Type**: typing.Optional[str]


# DescribeRecoverySnapshotsRequestPaginateTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoverySnapshotsRequestFiltersTypeDef]

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeRecoverySnapshotsRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeRecoverySnapshotsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# DescribeRecoverySnapshotsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoverySnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeReplicationConfigurationTemplatesRequestPaginateTypeDef

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeReplicationConfigurationTemplatesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### replicationConfigurationTemplateIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeReplicationConfigurationTemplatesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.ReplicationConfigurationTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceNetworksRequestFiltersTypeDef

### originAccountID
- **Type**: typing.Optional[str]

### originRegion
- **Type**: typing.Optional[str]

### sourceNetworkIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeSourceNetworksRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceNetworksRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeSourceNetworksRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceNetworksRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceNetworksResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.SourceNetworkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersRequestFiltersTypeDef

### hardwareId
- **Type**: typing.Optional[str]

### sourceServerIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### stagingAccountIDs
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeSourceServersRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceServersRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# DescribeSourceServersRequestTypeDef

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DescribeSourceServersRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeSourceServersResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.SourceServerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DisconnectRecoveryInstanceRequestTypeDef

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# DisconnectSourceServerRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# DiskTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventResourceDataTypeDef

### sourceNetworkData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.SourceNetworkDataTypeDef]


# ExportSourceNetworkCfnTemplateRequestTypeDef

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# ExportSourceNetworkCfnTemplateResponseTypeDef

### s3DestinationUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFailbackReplicationConfigurationRequestTypeDef

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# GetFailbackReplicationConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLaunchConfigurationRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# GetReplicationConfigurationRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# IdentificationHintsTypeDef

### awsInstanceID
- **Type**: typing.Optional[str]

### fqdn
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### vmWareUuid
- **Type**: typing.Optional[str]


# JobLogEventDataTypeDef

### conversionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.ConversionPropertiesTypeDef]

### conversionServerID
- **Type**: typing.Optional[str]

### eventResourceData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.EventResourceDataTypeDef]

### rawError
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]

### targetInstanceID
- **Type**: typing.Optional[str]


# JobLogTypeDef

### event
- **Type**: typing.Optional[typing.Literal['CLEANUP_END', 'CLEANUP_FAIL', 'CLEANUP_START', 'CONVERSION_END', 'CONVERSION_FAIL', 'CONVERSION_START', 'DEPLOY_NETWORK_CONFIGURATION_END', 'DEPLOY_NETWORK_CONFIGURATION_FAILED', 'DEPLOY_NETWORK_CONFIGURATION_START', 'JOB_CANCEL', 'JOB_END', 'JOB_START', 'LAUNCH_FAILED', 'LAUNCH_START', 'NETWORK_RECOVERY_FAIL', 'SERVER_SKIPPED', 'SNAPSHOT_END', 'SNAPSHOT_FAIL', 'SNAPSHOT_START', 'UPDATE_LAUNCH_TEMPLATE_END', 'UPDATE_LAUNCH_TEMPLATE_FAILED', 'UPDATE_LAUNCH_TEMPLATE_START', 'UPDATE_NETWORK_CONFIGURATION_END', 'UPDATE_NETWORK_CONFIGURATION_FAILED', 'UPDATE_NETWORK_CONFIGURATION_START', 'USING_PREVIOUS_SNAPSHOT', 'USING_PREVIOUS_SNAPSHOT_FAILED']]

### eventData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.JobLogEventDataTypeDef]

### logDateTime
- **Type**: typing.Optional[str]


# JobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchActionParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchActionRunTypeDef

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionTypeDef]

### failureReason
- **Type**: typing.Optional[str]

### runId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# LaunchActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchActionsRequestFiltersTypeDef

### actionIds
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchActionsStatusTypeDef

### runs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.LaunchActionRunTypeDef]]

### ssmAgentDiscoveryDatetime
- **Type**: typing.Optional[str]


# LaunchConfigurationTemplateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LicensingTypeDef]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# LaunchConfigurationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LaunchIntoInstancePropertiesTypeDef'>
- **Required**: Yes

### licensing
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LicensingTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LaunchIntoInstancePropertiesTypeDef

### launchIntoEC2InstanceID
- **Type**: typing.Optional[str]


# LicensingTypeDef

### osByol
- **Type**: typing.Optional[bool]


# LifeCycleLastLaunchInitiatedTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifeCycleLastLaunchTypeDef

### initiated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LifeCycleLastLaunchInitiatedTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]


# LifeCycleTypeDef

### addedToServiceDateTime
- **Type**: typing.Optional[str]

### elapsedReplicationDuration
- **Type**: typing.Optional[str]

### firstByteDateTime
- **Type**: typing.Optional[str]

### lastLaunch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LifeCycleLastLaunchTypeDef]

### lastSeenByServiceDateTime
- **Type**: typing.Optional[str]


# ListExtensibleSourceServersRequestPaginateTypeDef

### stagingAccountID
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# ListExtensibleSourceServersRequestTypeDef

### stagingAccountID
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExtensibleSourceServersResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.StagingSourceServerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchActionsRequestPaginateTypeDef

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionsRequestFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# ListLaunchActionsRequestTypeDef

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionsRequestFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchActionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.LaunchActionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStagingAccountsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.PaginatorConfigTypeDef]


# ListStagingAccountsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStagingAccountsResponseTypeDef

### accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.AccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PITPolicyRuleTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipatingResourceIDTypeDef

### sourceNetworkID
- **Type**: typing.Optional[str]


# ParticipatingResourceTypeDef

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### participatingResourceID
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.ParticipatingResourceIDTypeDef]


# ParticipatingServerTypeDef

### launchActionsStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchActionsStatusTypeDef]

### launchStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'LAUNCHED', 'PENDING', 'TERMINATED']]

### recoveryInstanceID
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]


# ProductCodeTypeDef

### productCodeId
- **Type**: typing.Optional[str]

### productCodeMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PutLaunchActionRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.drs_classes.LaunchActionParameterTypeDef]]


# RecoveryInstanceDataReplicationErrorTypeDef

### error
- **Type**: typing.Optional[typing.Literal['AGENT_NOT_SEEN', 'FAILBACK_CLIENT_NOT_SEEN', 'FAILED_GETTING_REPLICATION_STATE', 'FAILED_TO_ATTACH_STAGING_DISKS', 'FAILED_TO_AUTHENTICATE_WITH_SERVICE', 'FAILED_TO_BOOT_REPLICATION_SERVER', 'FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE', 'FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER', 'FAILED_TO_CREATE_SECURITY_GROUP', 'FAILED_TO_CREATE_STAGING_DISKS', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE', 'FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT', 'FAILED_TO_ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION', 'FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION', 'FAILED_TO_LAUNCH_REPLICATION_SERVER', 'FAILED_TO_PAIR_AGENT_WITH_REPLICATION_SOFTWARE', 'FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT', 'FAILED_TO_START_DATA_TRANSFER', 'NOT_CONVERGING', 'SNAPSHOTS_FAILURE', 'UNSTABLE_NETWORK']]

### rawError
- **Type**: typing.Optional[str]


# RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef

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


# RecoveryInstanceDataReplicationInfoTypeDef

### dataReplicationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationErrorTypeDef]

### dataReplicationInitiation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInitiationTypeDef]

### dataReplicationState
- **Type**: typing.Optional[typing.Literal['BACKLOG', 'CONTINUOUS', 'CREATING_SNAPSHOT', 'DISCONNECTED', 'INITIAL_SYNC', 'INITIATING', 'NOT_STARTED', 'PAUSED', 'REPLICATION_STATE_NOT_AVAILABLE', 'RESCAN', 'STALLED', 'STOPPED']]

### etaDateTime
- **Type**: typing.Optional[str]

### lagDuration
- **Type**: typing.Optional[str]

### replicatedDisks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInfoReplicatedDiskTypeDef]]

### stagingAvailabilityZone
- **Type**: typing.Optional[str]

### stagingOutpostArn
- **Type**: typing.Optional[str]


# RecoveryInstanceDataReplicationInitiationStepTypeDef

### name
- **Type**: typing.Optional[typing.Literal['ATTACH_STAGING_DISKS', 'AUTHENTICATE_WITH_SERVICE', 'BOOT_REPLICATION_SERVER', 'COMPLETE_VOLUME_MAPPING', 'CONFIGURE_REPLICATION_SOFTWARE', 'CONNECT_AGENT_TO_REPLICATION_SERVER', 'CREATE_SECURITY_GROUP', 'CREATE_STAGING_DISKS', 'DOWNLOAD_REPLICATION_SOFTWARE', 'DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT', 'ESTABLISH_AGENT_REPLICATOR_SOFTWARE_COMMUNICATION', 'ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION', 'LAUNCH_REPLICATION_SERVER', 'LINK_FAILBACK_CLIENT_WITH_RECOVERY_INSTANCE', 'PAIR_AGENT_WITH_REPLICATION_SOFTWARE', 'PAIR_REPLICATION_SERVER_WITH_AGENT', 'START_DATA_TRANSFER', 'WAIT']]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SKIPPED', 'SUCCEEDED']]


# RecoveryInstanceDataReplicationInitiationTypeDef

### startDateTime
- **Type**: typing.Optional[str]

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInitiationStepTypeDef]]


# RecoveryInstanceDiskTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecoveryInstanceFailbackTypeDef

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


# RecoveryInstancePropertiesTypeDef

### cpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.CPUTypeDef]]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDiskTypeDef]]

### identificationHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.IdentificationHintsTypeDef]

### lastUpdatedDateTime
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.NetworkInterfaceTypeDef]]

### os
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.OSTypeDef]

### ramBytes
- **Type**: typing.Optional[int]


# RecoveryInstanceTypeDef

### agentVersion
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### dataReplicationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceDataReplicationInfoTypeDef]

### ec2InstanceID
- **Type**: typing.Optional[str]

### ec2InstanceState
- **Type**: typing.Optional[typing.Literal['NOT_FOUND', 'PENDING', 'RUNNING', 'SHUTTING-DOWN', 'STOPPED', 'STOPPING', 'TERMINATED']]

### failback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstanceFailbackTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryInstancePropertiesTypeDef]

### sourceOutpostArn
- **Type**: typing.Optional[str]

### sourceServerID
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecoveryLifeCycleTypeDef

### apiCallDateTime
- **Type**: typing.Optional[datetime.datetime]

### jobID
- **Type**: typing.Optional[str]

### lastRecoveryResult
- **Type**: typing.Optional[typing.Literal['ASSOCIATE_FAIL', 'ASSOCIATE_SUCCESS', 'FAIL', 'IN_PROGRESS', 'NOT_STARTED', 'PARTIAL_SUCCESS', 'SUCCESS']]


# RecoverySnapshotTypeDef

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


# ReplicationConfigurationReplicatedDiskTypeDef

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


# ReplicationConfigurationTemplateResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRuleTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicationConfigurationTemplateTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRuleTypeDef]]

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


# ReplicationConfigurationTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRuleTypeDef]
- **Required**: Yes

### replicatedDisks
- **Type**: typing.List[aws_resource_validator.pydantic_models.drs_classes.ReplicationConfigurationReplicatedDiskTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
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


# RetryDataReplicationRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# ReverseReplicationRequestTypeDef

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# ReverseReplicationResponseTypeDef

### reversedDirectionSourceServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceCloudPropertiesTypeDef

### originAccountID
- **Type**: typing.Optional[str]

### originAvailabilityZone
- **Type**: typing.Optional[str]

### originRegion
- **Type**: typing.Optional[str]

### sourceOutpostArn
- **Type**: typing.Optional[str]


# SourceNetworkDataTypeDef

### sourceNetworkID
- **Type**: typing.Optional[str]

### sourceVpc
- **Type**: typing.Optional[str]

### stackName
- **Type**: typing.Optional[str]

### targetVpc
- **Type**: typing.Optional[str]


# SourceNetworkTypeDef

### arn
- **Type**: typing.Optional[str]

### cfnStackName
- **Type**: typing.Optional[str]

### lastRecovery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.RecoveryLifeCycleTypeDef]

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


# SourcePropertiesTypeDef

### cpus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.CPUTypeDef]]

### disks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.DiskTypeDef]]

### identificationHints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.IdentificationHintsTypeDef]

### lastUpdatedDateTime
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.drs_classes.NetworkInterfaceTypeDef]]

### os
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.OSTypeDef]

### ramBytes
- **Type**: typing.Optional[int]

### recommendedInstanceType
- **Type**: typing.Optional[str]

### supportsNitroInstances
- **Type**: typing.Optional[bool]


# SourceServerResponseTypeDef

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### dataReplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.DataReplicationInfoTypeDef'>
- **Required**: Yes

### lastLaunchResult
- **Type**: typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### lifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LifeCycleTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceCloudPropertiesTypeDef'>
- **Required**: Yes

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes

### sourceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourcePropertiesTypeDef'>
- **Required**: Yes

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### stagingArea
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.StagingAreaTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceServerTypeDef

### agentVersion
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### dataReplicationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.DataReplicationInfoTypeDef]

### lastLaunchResult
- **Type**: typing.Optional[typing.Literal['FAILED', 'NOT_STARTED', 'PENDING', 'SUCCEEDED']]

### lifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LifeCycleTypeDef]

### recoveryInstanceId
- **Type**: typing.Optional[str]

### replicationDirection
- **Type**: typing.Optional[typing.Literal['FAILBACK', 'FAILOVER']]

### reversedDirectionSourceServerArn
- **Type**: typing.Optional[str]

### sourceCloudProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.SourceCloudPropertiesTypeDef]

### sourceNetworkID
- **Type**: typing.Optional[str]

### sourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.SourcePropertiesTypeDef]

### sourceServerID
- **Type**: typing.Optional[str]

### stagingArea
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.StagingAreaTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StagingAreaTypeDef

### errorMessage
- **Type**: typing.Optional[str]

### stagingAccountID
- **Type**: typing.Optional[str]

### stagingSourceServerArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['EXTENDED', 'EXTENSION_ERROR', 'NOT_EXTENDED']]


# StagingSourceServerTypeDef

### arn
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartFailbackLaunchRequestTypeDef

### recoveryInstanceIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartFailbackLaunchResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRecoveryRequestSourceServerTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes

### recoverySnapshotID
- **Type**: typing.Optional[str]


# StartRecoveryRequestTypeDef

### sourceServers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.StartRecoveryRequestSourceServerTypeDef]
- **Required**: Yes

### isDrill
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartRecoveryResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReplicationRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# StartReplicationResponseTypeDef

### sourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSourceNetworkRecoveryRequestNetworkEntryTypeDef

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes

### cfnStackName
- **Type**: typing.Optional[str]


# StartSourceNetworkRecoveryRequestTypeDef

### sourceNetworks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.StartSourceNetworkRecoveryRequestNetworkEntryTypeDef]
- **Required**: Yes

### deployAsNew
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartSourceNetworkRecoveryResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSourceNetworkReplicationRequestTypeDef

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# StartSourceNetworkReplicationResponseTypeDef

### sourceNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopFailbackRequestTypeDef

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationRequestTypeDef

### sourceServerID
- **Type**: <class 'str'>
- **Required**: Yes


# StopReplicationResponseTypeDef

### sourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceServerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSourceNetworkReplicationRequestTypeDef

### sourceNetworkID
- **Type**: <class 'str'>
- **Required**: Yes


# StopSourceNetworkReplicationResponseTypeDef

### sourceNetwork
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.SourceNetworkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TerminateRecoveryInstancesRequestTypeDef

### recoveryInstanceIDs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TerminateRecoveryInstancesResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFailbackReplicationConfigurationRequestTypeDef

### recoveryInstanceID
- **Type**: <class 'str'>
- **Required**: Yes

### bandwidthThrottling
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### usePrivateIP
- **Type**: typing.Optional[bool]


# UpdateLaunchConfigurationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LaunchIntoInstancePropertiesTypeDef]

### licensing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LicensingTypeDef]

### name
- **Type**: typing.Optional[str]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# UpdateLaunchConfigurationTemplateRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.drs_classes.LicensingTypeDef]

### postLaunchEnabled
- **Type**: typing.Optional[bool]

### targetInstanceTypeRightSizingMethod
- **Type**: typing.Optional[typing.Literal['BASIC', 'IN_AWS', 'NONE']]


# UpdateLaunchConfigurationTemplateResponseTypeDef

### launchConfigurationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.LaunchConfigurationTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.drs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReplicationConfigurationRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRuleTypeDef]]

### replicatedDisks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.ReplicationConfigurationReplicatedDiskTypeDef]]

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


# UpdateReplicationConfigurationTemplateRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.drs_classes.PITPolicyRuleTypeDef]]

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


