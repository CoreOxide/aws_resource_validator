# Deadline Classes

# AcceleratorCapabilitiesOutputTypeDef

### selections
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorSelectionTypeDef]
- **Required**: Yes

### count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRangeTypeDef]


# AcceleratorCapabilitiesTypeDef

### selections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorSelectionTypeDef]
- **Required**: Yes

### count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRangeTypeDef]


# AcceleratorCountRangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AcceleratorSelectionTypeDef

### name
- **Type**: typing.Literal['a10g', 'l4', 'l40s', 't4']
- **Required**: Yes

### runtime
- **Type**: typing.Optional[str]


# AcceleratorTotalMemoryMiBRangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AcquiredLimitTypeDef

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### count
- **Type**: <class 'int'>
- **Required**: Yes


# AssignedEnvironmentEnterSessionActionDefinitionTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# AssignedEnvironmentExitSessionActionDefinitionTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# AssignedSessionActionDefinitionTypeDef

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedEnvironmentEnterSessionActionDefinitionTypeDef]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedEnvironmentExitSessionActionDefinitionTypeDef]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedTaskRunSessionActionDefinitionTypeDef]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef]


# AssignedSessionActionTypeDef

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionActionDefinitionTypeDef'>
- **Required**: Yes


# AssignedSessionTypeDef

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionActionTypeDef]
- **Required**: Yes

### logConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes


# AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef

### stepId
- **Type**: typing.Optional[str]


# AssignedTaskRunSessionActionDefinitionTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]
- **Required**: Yes


# AssociateMemberToFarmRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# AssociateMemberToFleetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# AssociateMemberToJobRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# AssociateMemberToQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# AssumeFleetRoleForReadRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeFleetRoleForReadResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumeFleetRoleForWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeFleetRoleForWorkerResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumeQueueRoleForReadRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeQueueRoleForReadResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumeQueueRoleForUserRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeQueueRoleForUserResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumeQueueRoleForWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeQueueRoleForWorkerResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachmentsOutputTypeDef

### manifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.ManifestPropertiesOutputTypeDef]
- **Required**: Yes

### fileSystem
- **Type**: typing.Optional[typing.Literal['COPIED', 'VIRTUAL']]


# AttachmentsTypeDef

### manifests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.ManifestPropertiesTypeDef]
- **Required**: Yes

### fileSystem
- **Type**: typing.Optional[typing.Literal['COPIED', 'VIRTUAL']]


# AttachmentsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCredentialsTypeDef

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetJobEntityRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.JobEntityIdentifiersUnionTypeDef]
- **Required**: Yes


# BatchGetJobEntityResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobEntityTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.GetJobEntityErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BudgetActionToAddTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetActionToRemoveTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetScheduleOutputTypeDef

### fixed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FixedBudgetScheduleOutputTypeDef]


# BudgetScheduleTypeDef

### fixed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FixedBudgetScheduleTypeDef]


# BudgetScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetSummaryTypeDef

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResourceTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### usages
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ConsumedUsagesTypeDef'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### updatedBy
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ConsumedUsagesTypeDef

### approximateDollarUsage
- **Type**: <class 'float'>
- **Required**: Yes


# CopyJobTemplateRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### targetS3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.S3LocationTypeDef'>
- **Required**: Yes


# CopyJobTemplateResponseTypeDef

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBudgetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResourceTypeDef'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToAddTypeDef]
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateBudgetResponseTypeDef

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFarmRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFarmResponseTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFleetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationUnionTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### minWorkerCount
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFleetResponseTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### template
- **Type**: typing.Optional[str]

### templateType
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]]

### attachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AttachmentsUnionTypeDef]

### storageProfileId
- **Type**: typing.Optional[str]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['READY', 'SUSPENDED']]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### maxWorkerCount
- **Type**: typing.Optional[int]

### sourceJobId
- **Type**: typing.Optional[str]


# CreateJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseEndpointRequestTypeDef

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLicenseEndpointResponseTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLimitRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### amountRequirementName
- **Type**: <class 'str'>
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateLimitResponseTypeDef

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMonitorRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateMonitorResponseTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQueueEnvironmentRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateQueueEnvironmentResponseTypeDef

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQueueFleetAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueueLimitAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### defaultBudgetAction
- **Type**: typing.Optional[typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']]

### jobAttachmentSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef]

### roleArn
- **Type**: typing.Optional[str]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef]

### requiredFileSystemLocationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResponseTypeDef

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorageProfileRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### fileSystemLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]]


# CreateStorageProfileResponseTypeDef

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesRequestTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# CreateWorkerResponseTypeDef

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerManagedFleetConfigurationOutputTypeDef

### mode
- **Type**: typing.Literal['EVENT_BASED_AUTO_SCALING', 'NO_SCALING']
- **Required**: Yes

### workerCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedWorkerCapabilitiesOutputTypeDef'>
- **Required**: Yes

### storageProfileId
- **Type**: typing.Optional[str]


# CustomerManagedFleetConfigurationTypeDef

### mode
- **Type**: typing.Literal['EVENT_BASED_AUTO_SCALING', 'NO_SCALING']
- **Required**: Yes

### workerCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedWorkerCapabilitiesTypeDef'>
- **Required**: Yes

### storageProfileId
- **Type**: typing.Optional[str]


# CustomerManagedWorkerCapabilitiesOutputTypeDef

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### acceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['gpu']]]

### acceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRangeTypeDef]

### acceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorTotalMemoryMiBRangeTypeDef]

### customAmounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityOutputTypeDef]]


# CustomerManagedWorkerCapabilitiesTypeDef

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### acceleratorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['gpu']]]

### acceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRangeTypeDef]

### acceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorTotalMemoryMiBRangeTypeDef]

### customAmounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityTypeDef]]


# DateTimeFilterExpressionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteBudgetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFarmRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLicenseEndpointRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLimitRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeteredProductRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitorRequestTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueEnvironmentRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueFleetAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueLimitAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageProfileRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# DependencyCountsTypeDef

### dependenciesResolved
- **Type**: <class 'int'>
- **Required**: Yes

### dependenciesUnresolved
- **Type**: <class 'int'>
- **Required**: Yes

### consumersResolved
- **Type**: <class 'int'>
- **Required**: Yes

### consumersUnresolved
- **Type**: <class 'int'>
- **Required**: Yes


# DisassociateMemberFromFarmRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromFleetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromJobRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# Ec2EbsVolumeTypeDef

### sizeGiB
- **Type**: typing.Optional[int]

### iops
- **Type**: typing.Optional[int]

### throughputMiB
- **Type**: typing.Optional[int]


# EnvironmentDetailsEntityTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# EnvironmentDetailsErrorTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentDetailsIdentifiersTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentEnterSessionActionDefinitionSummaryTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentEnterSessionActionDefinitionTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentExitSessionActionDefinitionSummaryTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentExitSessionActionDefinitionTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# FarmMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# FarmSummaryTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# FieldSortExpressionTypeDef

### sortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# FileSystemLocationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FixedBudgetScheduleOutputTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FixedBudgetScheduleTypeDef

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef'>
- **Required**: Yes


# FleetAmountCapabilityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FleetAttributeCapabilityOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# FleetAttributeCapabilityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FleetCapabilitiesTypeDef

### amounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityOutputTypeDef]]


# FleetConfigurationOutputTypeDef

### customerManaged
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedFleetConfigurationOutputTypeDef]

### serviceManagedEc2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2FleetConfigurationOutputTypeDef]


# FleetConfigurationTypeDef

### customerManaged
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedFleetConfigurationTypeDef]

### serviceManagedEc2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2FleetConfigurationTypeDef]


# FleetConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FleetMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# FleetSummaryTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationOutputTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### autoScalingStatus
- **Type**: typing.Optional[typing.Literal['GROWING', 'SHRINKING', 'STEADY']]

### targetWorkerCount
- **Type**: typing.Optional[int]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# GetBudgetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBudgetResponseTypeDef

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResourceTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### usages
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ConsumedUsagesTypeDef'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.ResponseBudgetActionTypeDef]
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleOutputTypeDef'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### queueStoppedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFarmRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFarmResponseTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFleetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFleetRequestWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetFleetResponseTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### autoScalingStatus
- **Type**: typing.Literal['GROWING', 'SHRINKING', 'STEADY']
- **Required**: Yes

### targetWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationOutputTypeDef'>
- **Required**: Yes

### capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetCapabilitiesTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobEntityErrorTypeDef

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsErrorTypeDef]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsErrorTypeDef]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsErrorTypeDef]

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsErrorTypeDef]


# GetJobRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobRequestWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ARCHIVED', 'CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### taskRunStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### targetTaskRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatusCounts
- **Type**: typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### maxFailedTasksCount
- **Type**: <class 'int'>
- **Required**: Yes

### maxRetriesPerTask
- **Type**: <class 'int'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]
- **Required**: Yes

### attachments
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AttachmentsOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### sourceJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLicenseEndpointRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseEndpointRequestWaitExtraTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetLicenseEndpointRequestWaitTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetLicenseEndpointResponseTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'NOT_READY', 'READY']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### dnsName
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLimitRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLimitResponseTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### amountRequirementName
- **Type**: <class 'str'>
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### currentCount
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMonitorRequestTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorResponseTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueEnvironmentRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueEnvironmentResponseTypeDef

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueFleetAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueFleetAssociationRequestWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueFleetAssociationResponseTypeDef

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOPPED', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueLimitAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueLimitAssociationRequestWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueLimitAssociationResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOPPED', 'STOP_LIMIT_USAGE_AND_CANCEL_TASKS', 'STOP_LIMIT_USAGE_AND_COMPLETE_TASKS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueRequestWaitExtraTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueRequestWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueResponseTypeDef

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']
- **Required**: Yes

### defaultBudgetAction
- **Type**: typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### blockedReason
- **Type**: typing.Literal['BUDGET_THRESHOLD_REACHED', 'NO_BUDGET_CONFIGURED']
- **Required**: Yes

### jobAttachmentSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### requiredFileSystemLocationNames
- **Type**: typing.List[str]
- **Required**: Yes

### allowedStorageProfileIds
- **Type**: typing.List[str]
- **Required**: Yes

### jobRunAsUser
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionActionRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionActionResponseTypeDef

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'CANCELING', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'RECLAIMED', 'RECLAIMING', 'RUNNING', 'SCHEDULED', 'SUCCEEDED']
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### workerUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### progressPercent
- **Type**: <class 'float'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### processExitCode
- **Type**: <class 'int'>
- **Required**: Yes

### progressMessage
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionActionDefinitionTypeDef'>
- **Required**: Yes

### acquiredLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AcquiredLimitTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ENDED', 'STARTED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### targetLifecycleStatus
- **Type**: typing.Literal['ENDED']
- **Required**: Yes

### hostProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef'>
- **Required**: Yes

### workerLog
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionsStatisticsAggregationRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# GetSessionsStatisticsAggregationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetSessionsStatisticsAggregationResponseTypeDef

### statistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StatisticsTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'TIMEOUT']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetStepRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStepResponseTypeDef

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### taskRunStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatusCounts
- **Type**: typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]
- **Required**: Yes

### targetTaskRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dependencyCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.DependencyCountsTypeDef'>
- **Required**: Yes

### requiredCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StepRequiredCapabilitiesTypeDef'>
- **Required**: Yes

### parameterSpace
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ParameterSpaceTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStorageProfileForQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageProfileForQueueResponseTypeDef

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### fileSystemLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStorageProfileRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageProfileResponseTypeDef

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### fileSystemLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTaskRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### runStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### targetRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### failureRetryCount
- **Type**: <class 'int'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### latestSessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkerResponseTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']
- **Required**: Yes

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostPropertiesRequestTypeDef

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesUnionTypeDef]

### hostName
- **Type**: typing.Optional[str]


# HostPropertiesResponseTypeDef

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesOutputTypeDef]

### hostName
- **Type**: typing.Optional[str]

### ec2InstanceArn
- **Type**: typing.Optional[str]

### ec2InstanceType
- **Type**: typing.Optional[str]


# IpAddressesOutputTypeDef

### ipV4Addresses
- **Type**: typing.Optional[typing.List[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.List[str]]


# IpAddressesTypeDef

### ipV4Addresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.Sequence[str]]


# IpAddressesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobAttachmentDetailsEntityTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### attachments
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AttachmentsOutputTypeDef'>
- **Required**: Yes


# JobAttachmentDetailsErrorTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentDetailsIdentifiersTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentSettingsTypeDef

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### rootPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetailsEntityTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### jobAttachmentSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef]

### queueRoleArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]]

### pathMappingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.PathMappingRuleTypeDef]]


# JobDetailsErrorTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetailsIdentifiersTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobEntityIdentifiersUnionTypeDef

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsIdentifiersTypeDef]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsIdentifiersTypeDef]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsIdentifiersTypeDef]

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsIdentifiersTypeDef]


# JobEntityTypeDef

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsEntityTypeDef]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsEntityTypeDef]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsEntityTypeDef]

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsEntityTypeDef]


# JobMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# JobParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunAsUserTypeDef

### runAs
- **Type**: typing.Literal['QUEUE_CONFIGURED_USER', 'WORKER_AGENT_USER']
- **Required**: Yes

### posix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PosixUserTypeDef]

### windows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WindowsUserTypeDef]


# JobSearchSummaryTypeDef

### jobId
- **Type**: typing.Optional[str]

### queueId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### lifecycleStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']]

### lifecycleStatusMessage
- **Type**: typing.Optional[str]

### taskRunStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatusCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]]

### priority
- **Type**: typing.Optional[int]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### createdBy
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### jobParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]]

### maxWorkerCount
- **Type**: typing.Optional[int]

### sourceJobId
- **Type**: typing.Optional[str]


# JobSummaryTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ARCHIVED', 'CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### taskRunStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatusCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### maxWorkerCount
- **Type**: typing.Optional[int]

### sourceJobId
- **Type**: typing.Optional[str]


# LicenseEndpointSummaryTypeDef

### licenseEndpointId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'NOT_READY', 'READY']]

### statusMessage
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]


# LimitSummaryTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### amountRequirementName
- **Type**: <class 'str'>
- **Required**: Yes

### maxCount
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### currentCount
- **Type**: <class 'int'>
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# ListAvailableMeteredProductsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListAvailableMeteredProductsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAvailableMeteredProductsResponseTypeDef

### meteredProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MeteredProductSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBudgetsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListBudgetsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListBudgetsResponseTypeDef

### budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.BudgetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFarmMembersRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFarmMembersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFarmMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FarmMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFarmsRequestPaginateTypeDef

### principalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFarmsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFarmsResponseTypeDef

### farms
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FarmSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetMembersRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFleetMembersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFleetsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFleetsResponseTypeDef

### fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobMembersRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListJobMembersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListJobMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobParameterDefinitionsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListJobParameterDefinitionsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListJobParameterDefinitionsResponseTypeDef

### jobParameterDefinitions
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListJobsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLicenseEndpointsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListLicenseEndpointsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLicenseEndpointsResponseTypeDef

### licenseEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.LicenseEndpointSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLimitsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListLimitsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLimitsResponseTypeDef

### limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.LimitSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMeteredProductsRequestPaginateTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListMeteredProductsRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMeteredProductsResponseTypeDef

### meteredProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MeteredProductSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMonitorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListMonitorsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMonitorsResponseTypeDef

### monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MonitorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueEnvironmentsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueEnvironmentsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListQueueEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueEnvironmentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueFleetAssociationsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### fleetId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueFleetAssociationsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### fleetId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListQueueFleetAssociationsResponseTypeDef

### queueFleetAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueFleetAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueLimitAssociationsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### limitId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueLimitAssociationsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### limitId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListQueueLimitAssociationsResponseTypeDef

### queueLimitAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueLimitAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueMembersRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueMembersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListQueueMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueuesRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueuesRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListQueuesResponseTypeDef

### queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionActionsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: typing.Optional[str]

### taskId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListSessionActionsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: typing.Optional[str]

### taskId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSessionActionsResponseTypeDef

### sessionActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.SessionActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsForWorkerRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListSessionsForWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSessionsForWorkerResponseTypeDef

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListSessionsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSessionsResponseTypeDef

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStepConsumersRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStepConsumersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStepConsumersResponseTypeDef

### consumers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepConsumerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStepDependenciesRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStepDependenciesRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStepDependenciesResponseTypeDef

### dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepDependencyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStepsRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStepsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStepsResponseTypeDef

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStorageProfilesForQueueRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStorageProfilesForQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStorageProfilesForQueueResponseTypeDef

### storageProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StorageProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStorageProfilesRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStorageProfilesRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStorageProfilesResponseTypeDef

### storageProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StorageProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTasksRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListTasksRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.TaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkersRequestPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListWorkersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkersResponseTypeDef

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogConfigurationTypeDef

### logDriver
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### error
- **Type**: typing.Optional[str]


# ManifestPropertiesOutputTypeDef

### rootPath
- **Type**: <class 'str'>
- **Required**: Yes

### rootPathFormat
- **Type**: typing.Literal['posix', 'windows']
- **Required**: Yes

### fileSystemLocationName
- **Type**: typing.Optional[str]

### outputRelativeDirectories
- **Type**: typing.Optional[typing.List[str]]

### inputManifestPath
- **Type**: typing.Optional[str]

### inputManifestHash
- **Type**: typing.Optional[str]


# ManifestPropertiesTypeDef

### rootPath
- **Type**: <class 'str'>
- **Required**: Yes

### rootPathFormat
- **Type**: typing.Literal['posix', 'windows']
- **Required**: Yes

### fileSystemLocationName
- **Type**: typing.Optional[str]

### outputRelativeDirectories
- **Type**: typing.Optional[typing.Sequence[str]]

### inputManifestPath
- **Type**: typing.Optional[str]

### inputManifestHash
- **Type**: typing.Optional[str]


# MemoryMiBRangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MeteredProductSummaryTypeDef

### productId
- **Type**: <class 'str'>
- **Required**: Yes

### family
- **Type**: <class 'str'>
- **Required**: Yes

### vendor
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes


# MonitorSummaryTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterFilterExpressionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterSortExpressionTypeDef

### sortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ParameterSpaceTypeDef

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepParameterTypeDef]
- **Required**: Yes

### combination
- **Type**: typing.Optional[str]


# PathMappingRuleTypeDef

### sourcePathFormat
- **Type**: typing.Literal['posix', 'windows']
- **Required**: Yes

### sourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### destinationPath
- **Type**: <class 'str'>
- **Required**: Yes


# PosixUserTypeDef

### user
- **Type**: <class 'str'>
- **Required**: Yes

### group
- **Type**: <class 'str'>
- **Required**: Yes


# PutMeteredProductRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueEnvironmentSummaryTypeDef

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes


# QueueFleetAssociationSummaryTypeDef

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOPPED', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# QueueLimitAssociationSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOPPED', 'STOP_LIMIT_USAGE_AND_CANCEL_TASKS', 'STOP_LIMIT_USAGE_AND_COMPLETE_TASKS']
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# QueueMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes


# QueueSummaryTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']
- **Required**: Yes

### defaultBudgetAction
- **Type**: typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### blockedReason
- **Type**: typing.Optional[typing.Literal['BUDGET_THRESHOLD_REACHED', 'NO_BUDGET_CONFIGURED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# ResponseBudgetActionTypeDef

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

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SearchFilterExpressionTypeDef

### dateTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.DateTimeFilterExpressionTypeDef]

### parameterFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterFilterExpressionTypeDef]

### searchTermFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchTermFilterExpressionTypeDef]

### stringFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StringFilterExpressionTypeDef]

### groupFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# SearchGroupedFilterExpressionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchJobsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]

### pageSize
- **Type**: typing.Optional[int]


# SearchJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobSearchSummaryTypeDef]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchSortExpressionTypeDef

### userJobsFirst
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.UserJobsFirstTypeDef]

### fieldSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FieldSortExpressionTypeDef]

### parameterSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterSortExpressionTypeDef]


# SearchStepsRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### jobId
- **Type**: typing.Optional[str]

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]

### pageSize
- **Type**: typing.Optional[int]


# SearchStepsResponseTypeDef

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepSearchSummaryTypeDef]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchTasksRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### jobId
- **Type**: typing.Optional[str]

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]

### pageSize
- **Type**: typing.Optional[int]


# SearchTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.TaskSearchSummaryTypeDef]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchTermFilterExpressionTypeDef

### searchTerm
- **Type**: <class 'str'>
- **Required**: Yes


# SearchWorkersRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]

### pageSize
- **Type**: typing.Optional[int]


# SearchWorkersResponseTypeDef

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSearchSummaryTypeDef]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceManagedEc2FleetConfigurationOutputTypeDef

### instanceCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceCapabilitiesOutputTypeDef'>
- **Required**: Yes

### instanceMarketOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceMarketOptionsTypeDef'>
- **Required**: Yes


# ServiceManagedEc2FleetConfigurationTypeDef

### instanceCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceCapabilitiesTypeDef'>
- **Required**: Yes

### instanceMarketOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceMarketOptionsTypeDef'>
- **Required**: Yes


# ServiceManagedEc2InstanceCapabilitiesOutputTypeDef

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'WINDOWS']
- **Required**: Yes

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### rootEbsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Ec2EbsVolumeTypeDef]

### acceleratorCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCapabilitiesOutputTypeDef]

### allowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### customAmounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityOutputTypeDef]]


# ServiceManagedEc2InstanceCapabilitiesTypeDef

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'WINDOWS']
- **Required**: Yes

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### rootEbsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Ec2EbsVolumeTypeDef]

### acceleratorCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCapabilitiesTypeDef]

### allowedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### customAmounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityTypeDef]]


# ServiceManagedEc2InstanceMarketOptionsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SessionActionDefinitionSummaryTypeDef

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentEnterSessionActionDefinitionSummaryTypeDef]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentExitSessionActionDefinitionSummaryTypeDef]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TaskRunSessionActionDefinitionSummaryTypeDef]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef]


# SessionActionDefinitionTypeDef

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentEnterSessionActionDefinitionTypeDef]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentExitSessionActionDefinitionTypeDef]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TaskRunSessionActionDefinitionTypeDef]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SyncInputJobAttachmentsSessionActionDefinitionTypeDef]


# SessionActionSummaryTypeDef

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'CANCELING', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'RECLAIMED', 'RECLAIMING', 'RUNNING', 'SCHEDULED', 'SUCCEEDED']
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionActionDefinitionSummaryTypeDef'>
- **Required**: Yes

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### workerUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### progressPercent
- **Type**: typing.Optional[float]


# SessionSummaryTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ENDED', 'STARTED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### targetLifecycleStatus
- **Type**: typing.Optional[typing.Literal['ENDED']]


# SessionsStatisticsResourcesTypeDef

### queueIds
- **Type**: typing.Optional[typing.Sequence[str]]

### fleetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# StartSessionsStatisticsAggregationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIds
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionsStatisticsResourcesTypeDef'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef'>
- **Required**: Yes

### groupBy
- **Type**: typing.Sequence[typing.Literal['FLEET_ID', 'INSTANCE_TYPE', 'JOB_ID', 'LICENSE_PRODUCT', 'QUEUE_ID', 'USAGE_TYPE', 'USER_ID']]
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['AVG', 'MAX', 'MIN', 'SUM']]
- **Required**: Yes

### timezone
- **Type**: typing.Optional[str]

### period
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY', 'WEEKLY']]


# StartSessionsStatisticsAggregationResponseTypeDef

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatisticsTypeDef

### count
- **Type**: <class 'int'>
- **Required**: Yes

### costInUsd
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StatsTypeDef'>
- **Required**: Yes

### runtimeInSeconds
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StatsTypeDef'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### fleetId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['COMPUTE', 'LICENSE']]

### licenseProduct
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### aggregationStartTime
- **Type**: typing.Optional[datetime.datetime]

### aggregationEndTime
- **Type**: typing.Optional[datetime.datetime]


# StatsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepAmountCapabilityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepAttributeCapabilityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### anyOf
- **Type**: typing.Optional[typing.List[str]]

### allOf
- **Type**: typing.Optional[typing.List[str]]


# StepConsumerTypeDef

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['RESOLVED', 'UNRESOLVED']
- **Required**: Yes


# StepDependencyTypeDef

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['RESOLVED', 'UNRESOLVED']
- **Required**: Yes


# StepDetailsEntityTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### dependencies
- **Type**: typing.List[str]
- **Required**: Yes


# StepDetailsErrorTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# StepDetailsIdentifiersTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# StepParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepRequiredCapabilitiesTypeDef

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepAttributeCapabilityTypeDef]
- **Required**: Yes

### amounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepAmountCapabilityTypeDef]
- **Required**: Yes


# StepSearchSummaryTypeDef

### stepId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### queueId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### lifecycleStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']]

### lifecycleStatusMessage
- **Type**: typing.Optional[str]

### taskRunStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatusCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### parameterSpace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterSpaceTypeDef]


# StepSummaryTypeDef

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### taskRunStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatusCounts
- **Type**: typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: typing.Optional[str]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### dependencyCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.DependencyCountsTypeDef]


# StorageProfileSummaryTypeDef

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes


# StringFilterExpressionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef

### stepId
- **Type**: typing.Optional[str]


# SyncInputJobAttachmentsSessionActionDefinitionTypeDef

### stepId
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TaskParameterValueTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskRunSessionActionDefinitionSummaryTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# TaskRunSessionActionDefinitionTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]
- **Required**: Yes


# TaskSearchSummaryTypeDef

### taskId
- **Type**: typing.Optional[str]

### stepId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### queueId
- **Type**: typing.Optional[str]

### runStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### targetRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]]

### failureRetryCount
- **Type**: typing.Optional[int]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]


# TaskSummaryTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### runStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### targetRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### failureRetryCount
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### latestSessionActionId
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBudgetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### approximateDollarLimit
- **Type**: typing.Optional[float]

### actionsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToAddTypeDef]]

### actionsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToRemoveTypeDef]]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleUnionTypeDef]


# UpdateFarmRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateFleetRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### minWorkerCount
- **Type**: typing.Optional[int]

### maxWorkerCount
- **Type**: typing.Optional[int]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationUnionTypeDef]


# UpdateJobRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### priority
- **Type**: typing.Optional[int]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### lifecycleStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED']]

### maxWorkerCount
- **Type**: typing.Optional[int]


# UpdateLimitRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### maxCount
- **Type**: typing.Optional[int]


# UpdateMonitorRequestTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateQueueEnvironmentRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### templateType
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]

### template
- **Type**: typing.Optional[str]


# UpdateQueueFleetAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes


# UpdateQueueLimitAssociationRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOP_LIMIT_USAGE_AND_CANCEL_TASKS', 'STOP_LIMIT_USAGE_AND_COMPLETE_TASKS']
- **Required**: Yes


# UpdateQueueRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### defaultBudgetAction
- **Type**: typing.Optional[typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']]

### jobAttachmentSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef]

### roleArn
- **Type**: typing.Optional[str]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef]

### requiredFileSystemLocationNamesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### requiredFileSystemLocationNamesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateSessionRequestTypeDef

### targetLifecycleStatus
- **Type**: typing.Literal['ENDED']
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateStepRequestTypeDef

### targetTaskRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateStorageProfileRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### osFamily
- **Type**: typing.Optional[typing.Literal['LINUX', 'MACOS', 'WINDOWS']]

### fileSystemLocationsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]]

### fileSystemLocationsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]]


# UpdateTaskRequestTypeDef

### targetRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateWorkerRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED', 'STOPPING']]

### capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WorkerCapabilitiesTypeDef]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesRequestTypeDef]


# UpdateWorkerResponseTypeDef

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkerScheduleRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedSessionActions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.deadline_classes.UpdatedSessionActionInfoTypeDef]]


# UpdateWorkerScheduleResponseTypeDef

### assignedSessions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionTypeDef]
- **Required**: Yes

### cancelSessionActions
- **Type**: typing.Dict[str, typing.List[str]]
- **Required**: Yes

### desiredWorkerStatus
- **Type**: typing.Literal['STOPPED']
- **Required**: Yes

### updateIntervalSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatedSessionActionInfoTypeDef

### completedStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'SUCCEEDED']]

### processExitCode
- **Type**: typing.Optional[int]

### progressMessage
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef]

### endedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef]

### updatedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TimestampTypeDef]

### progressPercent
- **Type**: typing.Optional[float]


# UsageTrackingResourceTypeDef

### queueId
- **Type**: typing.Optional[str]


# UserJobsFirstTypeDef

### userIdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# VCpuCountRangeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WindowsUserTypeDef

### user
- **Type**: <class 'str'>
- **Required**: Yes

### passwordArn
- **Type**: <class 'str'>
- **Required**: Yes


# WorkerAmountCapabilityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# WorkerAttributeCapabilityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkerCapabilitiesTypeDef

### amounts
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.WorkerAmountCapabilityTypeDef]
- **Required**: Yes

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.WorkerAttributeCapabilityTypeDef]
- **Required**: Yes


# WorkerSearchSummaryTypeDef

### fleetId
- **Type**: typing.Optional[str]

### workerId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef]

### createdBy
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# WorkerSessionSummaryTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ENDED', 'STARTED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### targetLifecycleStatus
- **Type**: typing.Optional[typing.Literal['ENDED']]


# WorkerSummaryTypeDef

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef]

### log
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


