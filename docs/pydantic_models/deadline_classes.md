# deadline_classes

# AcceleratorCountRangeTypeDef

### min
- **Type**: <class 'int'>
- **Required**: Yes

### max
- **Type**: typing.Optional[int]


# AcceleratorTotalMemoryMiBRangeTypeDef

### min
- **Type**: <class 'int'>
- **Required**: Yes

### max
- **Type**: typing.Optional[int]


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

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedTaskRunSessionActionDefinitionTypeDef]


# AssignedSessionActionTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionActionDefinitionTypeDef'>
- **Required**: Yes

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes


# AssignedSessionTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### logConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionActionTypeDef]
- **Required**: Yes


# AssignedSyncInputJobAttachmentsSessionActionDefinitionTypeDef

### stepId
- **Type**: typing.Optional[str]


# AssignedTaskRunSessionActionDefinitionTypeDef

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMemberToFarmRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# AssociateMemberToFleetRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# AssociateMemberToJobRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMemberToQueueRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeFleetRoleForReadRequestRequestTypeDef

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


# AssumeFleetRoleForWorkerRequestRequestTypeDef

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


# AssumeQueueRoleForReadRequestRequestTypeDef

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


# AssumeQueueRoleForUserRequestRequestTypeDef

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


# AssumeQueueRoleForWorkerRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeQueueRoleForWorkerResponseTypeDef

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachmentsTypeDef

### manifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.ManifestPropertiesTypeDef]
- **Required**: Yes

### fileSystem
- **Type**: typing.Optional[typing.Literal['COPIED', 'VIRTUAL']]


# AwsCredentialsTypeDef

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetJobEntityRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### identifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.JobEntityIdentifiersUnionTypeDef]
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
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

### thresholdPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### type
- **Type**: typing.Literal['STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# BudgetActionToRemoveTypeDef

### thresholdPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### type
- **Type**: typing.Literal['STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes


# BudgetScheduleTypeDef

### fixed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FixedBudgetScheduleTypeDef]


# BudgetSummaryTypeDef

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResourceTypeDef'>
- **Required**: Yes

### usages
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ConsumedUsagesTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# ConsumedUsagesTypeDef

### approximateDollarUsage
- **Type**: <class 'float'>
- **Required**: Yes


# CopyJobTemplateRequestRequestTypeDef

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


# CreateBudgetRequestRequestTypeDef

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToAddTypeDef]
- **Required**: Yes

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleTypeDef'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResourceTypeDef'>
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


# CreateFarmRequestRequestTypeDef

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


# CreateFleetRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationTypeDef'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
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


# CreateJobRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### attachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AttachmentsTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]]

### storageProfileId
- **Type**: typing.Optional[str]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['READY', 'SUSPENDED']]


# CreateJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLicenseEndpointRequestRequestTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
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


# CreateMonitorRequestRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateMonitorResponseTypeDef

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQueueEnvironmentRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
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


# CreateQueueFleetAssociationRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueueRequestRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### allowedStorageProfileIds
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]

### defaultBudgetAction
- **Type**: typing.Optional[typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']]

### description
- **Type**: typing.Optional[str]

### jobAttachmentSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef]

### requiredFileSystemLocationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResponseTypeDef

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorageProfileRequestRequestTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
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


# CreateWorkerRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesRequestTypeDef]


# CreateWorkerResponseTypeDef

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerManagedFleetConfigurationPaginatorTypeDef

### mode
- **Type**: typing.Literal['EVENT_BASED_AUTO_SCALING', 'NO_SCALING']
- **Required**: Yes

### workerCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedWorkerCapabilitiesPaginatorTypeDef'>
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


# CustomerManagedWorkerCapabilitiesPaginatorTypeDef

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### acceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRangeTypeDef]

### acceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorTotalMemoryMiBRangeTypeDef]

### acceleratorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['gpu']]]

### customAmounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityPaginatorTypeDef]]


# CustomerManagedWorkerCapabilitiesTypeDef

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### acceleratorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRangeTypeDef]

### acceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorTotalMemoryMiBRangeTypeDef]

### acceleratorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['gpu']]]

### customAmounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityTypeDef]]


# DateTimeFilterExpressionTypeDef

### dateTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUAL', 'GREATER_THAN', 'GREATER_THAN_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_EQUAL_TO', 'NOT_EQUAL']
- **Required**: Yes


# DeleteBudgetRequestRequestTypeDef

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFarmRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLicenseEndpointRequestRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeteredProductRequestRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitorRequestRequestTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueEnvironmentRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueFleetAssociationRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageProfileRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerRequestRequestTypeDef

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

### consumersResolved
- **Type**: <class 'int'>
- **Required**: Yes

### consumersUnresolved
- **Type**: <class 'int'>
- **Required**: Yes

### dependenciesResolved
- **Type**: <class 'int'>
- **Required**: Yes

### dependenciesUnresolved
- **Type**: <class 'int'>
- **Required**: Yes


# DisassociateMemberFromFarmRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromFleetRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromJobRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromQueueRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# Ec2EbsVolumeTypeDef

### iops
- **Type**: typing.Optional[int]

### sizeGiB
- **Type**: typing.Optional[int]

### throughputMiB
- **Type**: typing.Optional[int]


# EnvironmentDetailsEntityTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# EnvironmentDetailsErrorTypeDef

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentDetailsIdentifiersTypeDef

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
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

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# FarmSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# FieldSortExpressionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# FileSystemLocationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### path
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['LOCAL', 'SHARED']
- **Required**: Yes


# FixedBudgetScheduleTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# FleetAmountCapabilityTypeDef

### min
- **Type**: <class 'float'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### max
- **Type**: typing.Optional[float]


# FleetAttributeCapabilityPaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityTypeDef]]


# FleetConfigurationPaginatorTypeDef

### customerManaged
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedFleetConfigurationPaginatorTypeDef]

### serviceManagedEc2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2FleetConfigurationPaginatorTypeDef]


# FleetConfigurationTypeDef

### customerManaged
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedFleetConfigurationTypeDef]

### serviceManagedEc2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2FleetConfigurationTypeDef]


# FleetMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# FleetSummaryPaginatorTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationPaginatorTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### autoScalingStatus
- **Type**: typing.Optional[typing.Literal['GROWING', 'SHRINKING', 'STEADY']]

### targetWorkerCount
- **Type**: typing.Optional[int]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# FleetSummaryTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### autoScalingStatus
- **Type**: typing.Optional[typing.Literal['GROWING', 'SHRINKING', 'STEADY']]

### targetWorkerCount
- **Type**: typing.Optional[int]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# GetBudgetRequestRequestTypeDef

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBudgetResponseTypeDef

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.ResponseBudgetActionTypeDef]
- **Required**: Yes

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### queueStoppedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResourceTypeDef'>
- **Required**: Yes

### usages
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ConsumedUsagesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFarmRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFarmResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
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


# GetFleetRequestFleetActiveWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetFleetRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFleetResponseTypeDef

### autoScalingStatus
- **Type**: typing.Literal['GROWING', 'SHRINKING', 'STEADY']
- **Required**: Yes

### capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetCapabilitiesTypeDef'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### targetWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobEntityErrorTypeDef

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsErrorTypeDef]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsErrorTypeDef]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsErrorTypeDef]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsErrorTypeDef]


# GetJobRequestJobCreateCompleteWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetJobRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponseTypeDef

### attachments
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AttachmentsTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ARCHIVED', 'CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### maxFailedTasksCount
- **Type**: <class 'int'>
- **Required**: Yes

### maxRetriesPerTask
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### targetTaskRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatusCounts
- **Type**: typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]
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


# GetLicenseEndpointRequestLicenseEndpointDeletedWaitTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetLicenseEndpointRequestLicenseEndpointValidWaitTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetLicenseEndpointRequestRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseEndpointResponseTypeDef

### dnsName
- **Type**: <class 'str'>
- **Required**: Yes

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'NOT_READY', 'READY']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMonitorRequestRequestTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueueEnvironmentRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueEnvironmentResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
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


# GetQueueFleetAssociationRequestQueueFleetAssociationStoppedWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueFleetAssociationRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueFleetAssociationResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOPPED', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
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


# GetQueueRequestQueueSchedulingBlockedWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueRequestQueueSchedulingWaitTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WaiterConfigTypeDef]


# GetQueueRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueResponseTypeDef

### allowedStorageProfileIds
- **Type**: typing.List[str]
- **Required**: Yes

### blockedReason
- **Type**: typing.Literal['BUDGET_THRESHOLD_REACHED', 'NO_BUDGET_CONFIGURED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### defaultBudgetAction
- **Type**: typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobAttachmentSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef'>
- **Required**: Yes

### jobRunAsUser
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### requiredFileSystemLocationNames
- **Type**: typing.List[str]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']
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


# GetSessionActionRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionActionResponseTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionActionDefinitionTypeDef'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### processExitCode
- **Type**: <class 'int'>
- **Required**: Yes

### progressMessage
- **Type**: <class 'str'>
- **Required**: Yes

### progressPercent
- **Type**: <class 'float'>
- **Required**: Yes

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'CANCELING', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'RECLAIMED', 'RECLAIMING', 'RUNNING', 'SCHEDULED', 'SUCCEEDED']
- **Required**: Yes

### workerUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ENDED', 'STARTED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetLifecycleStatus
- **Type**: typing.Literal['ENDED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### workerLog
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionsStatisticsAggregationRequestGetSessionsStatisticsAggregationPaginateTypeDef

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# GetSessionsStatisticsAggregationRequestRequestTypeDef

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetSessionsStatisticsAggregationResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

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


# GetStepRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStepResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### dependencyCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.DependencyCountsTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### parameterSpace
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ParameterSpaceTypeDef'>
- **Required**: Yes

### requiredCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StepRequiredCapabilitiesTypeDef'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### targetTaskRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatusCounts
- **Type**: typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]
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


# GetStorageProfileForQueueRequestRequestTypeDef

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

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### fileSystemLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStorageProfileRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageProfileResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### fileSystemLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### storageProfileId
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


# GetTaskRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTaskResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureRetryCount
- **Type**: <class 'int'>
- **Required**: Yes

### latestSessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]
- **Required**: Yes

### runStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### targetRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskId
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


# GetWorkerRequestRequestTypeDef

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

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef'>
- **Required**: Yes

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostPropertiesRequestTypeDef

### hostName
- **Type**: typing.Optional[str]

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesTypeDef]


# HostPropertiesResponsePaginatorTypeDef

### ec2InstanceArn
- **Type**: typing.Optional[str]

### ec2InstanceType
- **Type**: typing.Optional[str]

### hostName
- **Type**: typing.Optional[str]

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesPaginatorTypeDef]


# HostPropertiesResponseTypeDef

### ec2InstanceArn
- **Type**: typing.Optional[str]

### ec2InstanceType
- **Type**: typing.Optional[str]

### hostName
- **Type**: typing.Optional[str]

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesTypeDef]


# IpAddressesPaginatorTypeDef

### ipV4Addresses
- **Type**: typing.Optional[typing.List[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.List[str]]


# IpAddressesTypeDef

### ipV4Addresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.Sequence[str]]


# JobAttachmentDetailsEntityTypeDef

### attachments
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AttachmentsTypeDef'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentDetailsErrorTypeDef

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentDetailsIdentifiersTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentSettingsTypeDef

### rootPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### s3BucketName
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

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]]

### pathMappingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.PathMappingRuleTypeDef]]

### queueRoleArn
- **Type**: typing.Optional[str]


# JobDetailsErrorTypeDef

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetailsIdentifiersTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobEntityIdentifiersUnionTypeDef

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsIdentifiersTypeDef]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsIdentifiersTypeDef]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsIdentifiersTypeDef]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsIdentifiersTypeDef]


# JobEntityTypeDef

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsEntityTypeDef]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsEntityTypeDef]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsEntityTypeDef]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsEntityTypeDef]


# JobMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# JobParameterTypeDef

### float
- **Type**: typing.Optional[str]

### int
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### string
- **Type**: typing.Optional[str]


# JobRunAsUserTypeDef

### runAs
- **Type**: typing.Literal['QUEUE_CONFIGURED_USER', 'WORKER_AGENT_USER']
- **Required**: Yes

### posix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PosixUserTypeDef]

### windows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WindowsUserTypeDef]


# JobSearchSummaryTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### jobId
- **Type**: typing.Optional[str]

### jobParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameterTypeDef]]

### lifecycleStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']]

### lifecycleStatusMessage
- **Type**: typing.Optional[str]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### queueId
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatusCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]]


# JobSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ARCHIVED', 'CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED', 'UPLOAD_FAILED', 'UPLOAD_IN_PROGRESS']
- **Required**: Yes

### lifecycleStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatusCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
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


# ListAvailableMeteredProductsRequestListAvailableMeteredProductsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListAvailableMeteredProductsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAvailableMeteredProductsResponseTypeDef

### meteredProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MeteredProductSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBudgetsRequestListBudgetsPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListBudgetsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListBudgetsResponseTypeDef

### budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.BudgetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFarmMembersRequestListFarmMembersPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFarmMembersRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFarmMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FarmMemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFarmsRequestListFarmsPaginateTypeDef

### principalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFarmsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]


# ListFarmsResponseTypeDef

### farms
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FarmSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetMembersRequestListFleetMembersPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFleetMembersRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFleetMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetMemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetsRequestListFleetsPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListFleetsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]


# ListFleetsResponsePaginatorTypeDef

### fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetSummaryPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFleetsResponseTypeDef

### fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobMembersRequestListJobMembersPaginateTypeDef

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


# ListJobMembersRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobMemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestListJobsPaginateTypeDef

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


# ListJobsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]


# ListJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLicenseEndpointsRequestListLicenseEndpointsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListLicenseEndpointsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLicenseEndpointsResponseTypeDef

### licenseEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.LicenseEndpointSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMeteredProductsRequestListMeteredProductsPaginateTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListMeteredProductsRequestRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMeteredProductsResponseTypeDef

### meteredProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MeteredProductSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMonitorsRequestListMonitorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListMonitorsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMonitorsResponseTypeDef

### monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MonitorSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueueEnvironmentsRequestListQueueEnvironmentsPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueEnvironmentsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQueueEnvironmentsResponseTypeDef

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueEnvironmentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueueFleetAssociationsRequestListQueueFleetAssociationsPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: typing.Optional[str]

### queueId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueFleetAssociationsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### queueId
- **Type**: typing.Optional[str]


# ListQueueFleetAssociationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### queueFleetAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueFleetAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueueMembersRequestListQueueMembersPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueueMembersRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQueueMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueMemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueuesRequestListQueuesPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListQueuesRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']]


# ListQueuesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSessionActionsRequestListSessionActionsPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: typing.Optional[str]

### taskId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListSessionActionsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### taskId
- **Type**: typing.Optional[str]


# ListSessionActionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessionActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.SessionActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSessionsForWorkerRequestListSessionsForWorkerPaginateTypeDef

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


# ListSessionsForWorkerRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsForWorkerResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSessionsRequestListSessionsPaginateTypeDef

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


# ListSessionsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStepConsumersRequestListStepConsumersPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStepConsumersRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStepConsumersResponseTypeDef

### consumers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepConsumerTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStepDependenciesRequestListStepDependenciesPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStepDependenciesRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStepDependenciesResponseTypeDef

### dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepDependencyTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStepsRequestListStepsPaginateTypeDef

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


# ListStepsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStepsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStorageProfilesForQueueRequestListStorageProfilesForQueuePaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStorageProfilesForQueueRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStorageProfilesForQueueResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StorageProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStorageProfilesRequestListStorageProfilesPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListStorageProfilesRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStorageProfilesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StorageProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTasksRequestListTasksPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListTasksRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTasksResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.TaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkersRequestListWorkersPaginateTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfigTypeDef]


# ListWorkersRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkersResponsePaginatorTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSummaryPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkersResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogConfigurationTypeDef

### logDriver
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ManifestPropertiesTypeDef

### rootPath
- **Type**: <class 'str'>
- **Required**: Yes

### rootPathFormat
- **Type**: typing.Literal['posix', 'windows']
- **Required**: Yes

### fileSystemLocationName
- **Type**: typing.Optional[str]

### inputManifestHash
- **Type**: typing.Optional[str]

### inputManifestPath
- **Type**: typing.Optional[str]

### outputRelativeDirectories
- **Type**: typing.Optional[typing.List[str]]


# MemoryMiBRangeTypeDef

### min
- **Type**: <class 'int'>
- **Required**: Yes

### max
- **Type**: typing.Optional[int]


# MeteredProductSummaryTypeDef

### family
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'int'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes

### vendor
- **Type**: <class 'str'>
- **Required**: Yes


# MonitorSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### url
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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUAL', 'GREATER_THAN', 'GREATER_THAN_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_EQUAL_TO', 'NOT_EQUAL']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ParameterSortExpressionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# ParameterSpaceTypeDef

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepParameterTypeDef]
- **Required**: Yes

### combination
- **Type**: typing.Optional[str]


# PathMappingRuleTypeDef

### destinationPath
- **Type**: <class 'str'>
- **Required**: Yes

### sourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### sourcePathFormat
- **Type**: typing.Literal['posix', 'windows']
- **Required**: Yes


# PosixUserTypeDef

### group
- **Type**: <class 'str'>
- **Required**: Yes

### user
- **Type**: <class 'str'>
- **Required**: Yes


# PutMeteredProductRequestRequestTypeDef

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueEnvironmentSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueFleetAssociationSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOPPED', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# QueueMemberTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### identityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipLevel
- **Type**: typing.Literal['CONTRIBUTOR', 'MANAGER', 'OWNER', 'VIEWER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### principalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### defaultBudgetAction
- **Type**: typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']
- **Required**: Yes

### blockedReason
- **Type**: typing.Optional[typing.Literal['BUDGET_THRESHOLD_REACHED', 'NO_BUDGET_CONFIGURED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# ResponseBudgetActionTypeDef

### thresholdPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### type
- **Type**: typing.Literal['STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes

### description
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

### groupFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### parameterFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterFilterExpressionTypeDef]

### searchTermFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchTermFilterExpressionTypeDef]

### stringFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StringFilterExpressionTypeDef]


# SearchGroupedFilterExpressionsTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchFilterExpressionTypeDef]
- **Required**: Yes

### operator
- **Type**: typing.Literal['AND', 'OR']
- **Required**: Yes


# SearchJobsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### queueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### pageSize
- **Type**: typing.Optional[int]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]


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

### fieldSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FieldSortExpressionTypeDef]

### parameterSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterSortExpressionTypeDef]

### userJobsFirst
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.UserJobsFirstTypeDef]


# SearchStepsRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### queueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### jobId
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]


# SearchStepsResponseTypeDef

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepSearchSummaryTypeDef]
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchTasksRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### itemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### queueIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### filterExpressions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressionsTypeDef]

### jobId
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]


# SearchTasksResponseTypeDef

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.TaskSearchSummaryTypeDef]
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


# SearchWorkersRequestRequestTypeDef

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

### pageSize
- **Type**: typing.Optional[int]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpressionTypeDef]]


# SearchWorkersResponseTypeDef

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSearchSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceManagedEc2FleetConfigurationPaginatorTypeDef

### instanceCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceCapabilitiesPaginatorTypeDef'>
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


# ServiceManagedEc2InstanceCapabilitiesPaginatorTypeDef

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'WINDOWS']
- **Required**: Yes

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### allowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### customAmounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityPaginatorTypeDef]]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### rootEbsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Ec2EbsVolumeTypeDef]


# ServiceManagedEc2InstanceCapabilitiesTypeDef

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRangeTypeDef'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'WINDOWS']
- **Required**: Yes

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRangeTypeDef'>
- **Required**: Yes

### allowedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### customAmounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapabilityTypeDef]]

### customAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityTypeDef]]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### rootEbsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Ec2EbsVolumeTypeDef]


# ServiceManagedEc2InstanceMarketOptionsTypeDef

### type
- **Type**: typing.Literal['on-demand', 'spot']
- **Required**: Yes


# SessionActionDefinitionSummaryTypeDef

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentEnterSessionActionDefinitionSummaryTypeDef]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentExitSessionActionDefinitionSummaryTypeDef]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TaskRunSessionActionDefinitionSummaryTypeDef]


# SessionActionDefinitionTypeDef

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentEnterSessionActionDefinitionTypeDef]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentExitSessionActionDefinitionTypeDef]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SyncInputJobAttachmentsSessionActionDefinitionTypeDef]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TaskRunSessionActionDefinitionTypeDef]


# SessionActionSummaryTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionActionDefinitionSummaryTypeDef'>
- **Required**: Yes

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'CANCELING', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'RECLAIMED', 'RECLAIMING', 'RUNNING', 'SCHEDULED', 'SUCCEEDED']
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### progressPercent
- **Type**: typing.Optional[float]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### workerUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# SessionSummaryTypeDef

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ENDED', 'STARTED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### targetLifecycleStatus
- **Type**: typing.Optional[typing.Literal['ENDED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# SessionsStatisticsResourcesTypeDef

### fleetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### queueIds
- **Type**: typing.Optional[typing.Sequence[str]]


# StartSessionsStatisticsAggregationRequestRequestTypeDef

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### groupBy
- **Type**: typing.Sequence[typing.Literal['FLEET_ID', 'INSTANCE_TYPE', 'JOB_ID', 'LICENSE_PRODUCT', 'QUEUE_ID', 'USAGE_TYPE', 'USER_ID']]
- **Required**: Yes

### resourceIds
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionsStatisticsResourcesTypeDef'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### statistics
- **Type**: typing.Sequence[typing.Literal['AVG', 'MAX', 'MIN', 'SUM']]
- **Required**: Yes

### period
- **Type**: typing.Optional[typing.Literal['DAILY', 'HOURLY', 'MONTHLY', 'WEEKLY']]

### timezone
- **Type**: typing.Optional[str]


# StartSessionsStatisticsAggregationResponseTypeDef

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatisticsTypeDef

### costInUsd
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StatsTypeDef'>
- **Required**: Yes

### count
- **Type**: <class 'int'>
- **Required**: Yes

### runtimeInSeconds
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StatsTypeDef'>
- **Required**: Yes

### aggregationEndTime
- **Type**: typing.Optional[datetime.datetime]

### aggregationStartTime
- **Type**: typing.Optional[datetime.datetime]

### fleetId
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### licenseProduct
- **Type**: typing.Optional[str]

### queueId
- **Type**: typing.Optional[str]

### usageType
- **Type**: typing.Optional[typing.Literal['COMPUTE', 'LICENSE']]

### userId
- **Type**: typing.Optional[str]


# StatsTypeDef

### avg
- **Type**: typing.Optional[float]

### max
- **Type**: typing.Optional[float]

### min
- **Type**: typing.Optional[float]

### sum
- **Type**: typing.Optional[float]


# StepAmountCapabilityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### max
- **Type**: typing.Optional[float]

### min
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[float]


# StepAttributeCapabilityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### allOf
- **Type**: typing.Optional[typing.List[str]]

### anyOf
- **Type**: typing.Optional[typing.List[str]]


# StepConsumerTypeDef

### status
- **Type**: typing.Literal['RESOLVED', 'UNRESOLVED']
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# StepDependencyTypeDef

### status
- **Type**: typing.Literal['RESOLVED', 'UNRESOLVED']
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# StepDetailsEntityTypeDef

### dependencies
- **Type**: typing.List[str]
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### template
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# StepDetailsErrorTypeDef

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['FLOAT', 'INT', 'PATH', 'STRING']
- **Required**: Yes


# StepRequiredCapabilitiesTypeDef

### amounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepAmountCapabilityTypeDef]
- **Required**: Yes

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepAttributeCapabilityTypeDef]
- **Required**: Yes


# StepSearchSummaryTypeDef

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### jobId
- **Type**: typing.Optional[str]

### lifecycleStatus
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']]

### lifecycleStatusMessage
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### parameterSpace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterSpaceTypeDef]

### queueId
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### stepId
- **Type**: typing.Optional[str]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### taskRunStatusCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]]


# StepSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['CREATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskRunStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskRunStatusCounts
- **Type**: typing.Dict[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED'], int]
- **Required**: Yes

### dependencyCounts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.DependencyCountsTypeDef]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleStatusMessage
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# StorageProfileSummaryTypeDef

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# StringFilterExpressionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUAL', 'GREATER_THAN', 'GREATER_THAN_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_EQUAL_TO', 'NOT_EQUAL']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SyncInputJobAttachmentsSessionActionDefinitionSummaryTypeDef

### stepId
- **Type**: typing.Optional[str]


# SyncInputJobAttachmentsSessionActionDefinitionTypeDef

### stepId
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TaskParameterValueTypeDef

### float
- **Type**: typing.Optional[str]

### int
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]

### string
- **Type**: typing.Optional[str]


# TaskRunSessionActionDefinitionSummaryTypeDef

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# TaskRunSessionActionDefinitionTypeDef

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# TaskSearchSummaryTypeDef

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### failureRetryCount
- **Type**: typing.Optional[int]

### jobId
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]]

### queueId
- **Type**: typing.Optional[str]

### runStatus
- **Type**: typing.Optional[typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### stepId
- **Type**: typing.Optional[str]

### targetRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### taskId
- **Type**: typing.Optional[str]


# TaskSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### runStatus
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'FAILED', 'INTERRUPTING', 'NOT_COMPATIBLE', 'PENDING', 'READY', 'RUNNING', 'SCHEDULED', 'STARTING', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### failureRetryCount
- **Type**: typing.Optional[int]

### latestSessionActionId
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValueTypeDef]]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### targetRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBudgetRequestRequestTypeDef

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### actionsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToAddTypeDef]]

### actionsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToRemoveTypeDef]]

### approximateDollarLimit
- **Type**: typing.Optional[float]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# UpdateFarmRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# UpdateFleetRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationTypeDef]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### maxWorkerCount
- **Type**: typing.Optional[int]

### minWorkerCount
- **Type**: typing.Optional[int]

### roleArn
- **Type**: typing.Optional[str]


# UpdateJobRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### lifecycleStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED']]

### maxFailedTasksCount
- **Type**: typing.Optional[int]

### maxRetriesPerTask
- **Type**: typing.Optional[int]

### priority
- **Type**: typing.Optional[int]

### targetTaskRunStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']]


# UpdateMonitorRequestRequestTypeDef

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### subdomain
- **Type**: typing.Optional[str]


# UpdateQueueEnvironmentRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### template
- **Type**: typing.Optional[str]

### templateType
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML']]


# UpdateQueueFleetAssociationRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']
- **Required**: Yes


# UpdateQueueRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### allowedStorageProfileIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]

### defaultBudgetAction
- **Type**: typing.Optional[typing.Literal['NONE', 'STOP_SCHEDULING_AND_CANCEL_TASKS', 'STOP_SCHEDULING_AND_COMPLETE_TASKS']]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### jobAttachmentSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettingsTypeDef]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUserTypeDef]

### requiredFileSystemLocationNamesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### requiredFileSystemLocationNamesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### roleArn
- **Type**: typing.Optional[str]


# UpdateSessionRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### targetLifecycleStatus
- **Type**: typing.Literal['ENDED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateStepRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### targetTaskRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateStorageProfileRequestRequestTypeDef

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

### fileSystemLocationsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]]

### fileSystemLocationsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocationTypeDef]]

### osFamily
- **Type**: typing.Optional[typing.Literal['LINUX', 'MACOS', 'WINDOWS']]


# UpdateTaskRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### targetRunStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'PENDING', 'READY', 'SUCCEEDED', 'SUSPENDED']
- **Required**: Yes

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateWorkerRequestRequestTypeDef

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WorkerCapabilitiesTypeDef]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesRequestTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['STARTED', 'STOPPED', 'STOPPING']]


# UpdateWorkerResponseTypeDef

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkerScheduleRequestRequestTypeDef

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

### endedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### processExitCode
- **Type**: typing.Optional[int]

### progressMessage
- **Type**: typing.Optional[str]

### progressPercent
- **Type**: typing.Optional[float]

### startedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### updatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UsageTrackingResourceTypeDef

### queueId
- **Type**: typing.Optional[str]


# UserJobsFirstTypeDef

### userIdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# VCpuCountRangeTypeDef

### min
- **Type**: <class 'int'>
- **Required**: Yes

### max
- **Type**: typing.Optional[int]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WindowsUserTypeDef

### passwordArn
- **Type**: <class 'str'>
- **Required**: Yes

### user
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

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### fleetId
- **Type**: typing.Optional[str]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponseTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### workerId
- **Type**: typing.Optional[str]


# WorkerSessionSummaryTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### lifecycleStatus
- **Type**: typing.Literal['ENDED', 'STARTED', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCEEDED']
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### targetLifecycleStatus
- **Type**: typing.Optional[typing.Literal['ENDED']]


# WorkerSummaryPaginatorTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
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

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponsePaginatorTypeDef]

### log
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.LogConfigurationTypeDef]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


# WorkerSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
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

### workerId
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


