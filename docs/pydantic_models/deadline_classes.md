# Deadline Classes

# AcceleratorCapabilities

### selections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorSelection]
- **Required**: Yes

### count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRange]


# AcceleratorCapabilitiesOutput

### selections
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorSelection]
- **Required**: Yes

### count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRange]


# AcceleratorCountRange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AcceleratorSelection

### name
- **Type**: typing.Literal['a10g', 'l4', 'l40s', 't4']
- **Required**: Yes

### runtime
- **Type**: typing.Optional[str]


# AcceleratorTotalMemoryMiBRange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AcquiredLimit

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### count
- **Type**: <class 'int'>
- **Required**: Yes


# AssignedEnvironmentEnterSessionActionDefinition

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# AssignedEnvironmentExitSessionActionDefinition

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# AssignedSession

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionAction]
- **Required**: Yes

### logConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfiguration'>
- **Required**: Yes


# AssignedSessionAction

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AssignedSessionActionDefinition'>
- **Required**: Yes


# AssignedSessionActionDefinition

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedEnvironmentEnterSessionActionDefinition]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedEnvironmentExitSessionActionDefinition]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedTaskRunSessionActionDefinition]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AssignedSyncInputJobAttachmentsSessionActionDefinition]


# AssignedSyncInputJobAttachmentsSessionActionDefinition

### stepId
- **Type**: typing.Optional[str]


# AssignedTaskRunSessionActionDefinition

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValue]
- **Required**: Yes


# AssociateMemberToFarmRequest

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


# AssociateMemberToFleetRequest

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


# AssociateMemberToJobRequest

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


# AssociateMemberToQueueRequest

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


# AssumeFleetRoleForReadRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeFleetRoleForReadResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeFleetRoleForWorkerRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeFleetRoleForWorkerResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeQueueRoleForReadRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeQueueRoleForReadResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeQueueRoleForUserRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeQueueRoleForUserResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeQueueRoleForWorkerRequest

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


# AssumeQueueRoleForWorkerResponse

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AwsCredentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# Attachments

### manifests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.ManifestProperties]
- **Required**: Yes

### fileSystem
- **Type**: typing.Optional[typing.Literal['COPIED', 'VIRTUAL']]


# AttachmentsOutput

### manifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.ManifestPropertiesOutput]
- **Required**: Yes

### fileSystem
- **Type**: typing.Optional[typing.Literal['COPIED', 'VIRTUAL']]


# AttachmentsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AwsCredentials

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

# BatchGetJobEntityRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.JobEntityIdentifiersUnion]
- **Required**: Yes


# BatchGetJobEntityResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobEntity]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.GetJobEntityError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# BudgetActionToAdd

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetActionToRemove

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetSchedule

### fixed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FixedBudgetSchedule]


# BudgetScheduleOutput

### fixed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FixedBudgetScheduleOutput]


# BudgetScheduleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BudgetSummary

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResource'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ConsumedUsages'>
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


# ConsumedUsages

### approximateDollarUsage
- **Type**: <class 'float'>
- **Required**: Yes


# CopyJobTemplateRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.S3Location'>
- **Required**: Yes


# CopyJobTemplateResponse

### templateType
- **Type**: typing.Literal['JSON', 'YAML']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBudgetRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResource'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### approximateDollarLimit
- **Type**: <class 'float'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToAdd]
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleUnion'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateBudgetResponse

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFarmRequest

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


# CreateFarmResponse

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFleetRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationUnion'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### minWorkerCount
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFleetResponse

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobRequest

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameter]]

### attachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AttachmentsUnion]

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


# CreateJobResponse

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLicenseEndpointRequest

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


# CreateLicenseEndpointResponse

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLimitRequest

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


# CreateLimitResponse

### limitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMonitorRequest

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


# CreateMonitorResponse

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### identityCenterApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQueueEnvironmentRequest

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


# CreateQueueEnvironmentResponse

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQueueFleetAssociationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueueLimitAssociationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueueRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettings]

### roleArn
- **Type**: typing.Optional[str]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUser]

### requiredFileSystemLocationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIds
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQueueResponse

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStorageProfileRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocation]]


# CreateStorageProfileResponse

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkerRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesRequest]

### clientToken
- **Type**: typing.Optional[str]


# CreateWorkerResponse

### workerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerManagedFleetConfiguration

### mode
- **Type**: typing.Literal['EVENT_BASED_AUTO_SCALING', 'NO_SCALING']
- **Required**: Yes

### workerCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedWorkerCapabilities'>
- **Required**: Yes

### storageProfileId
- **Type**: typing.Optional[str]


# CustomerManagedFleetConfigurationOutput

### mode
- **Type**: typing.Literal['EVENT_BASED_AUTO_SCALING', 'NO_SCALING']
- **Required**: Yes

### workerCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedWorkerCapabilitiesOutput'>
- **Required**: Yes

### storageProfileId
- **Type**: typing.Optional[str]


# CustomerManagedWorkerCapabilities

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRange'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRange'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRange]

### acceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorTotalMemoryMiBRange]

### customAmounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapability]]

### customAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapability]]


# CustomerManagedWorkerCapabilitiesOutput

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRange'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRange'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCountRange]

### acceleratorTotalMemoryMiB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorTotalMemoryMiBRange]

### customAmounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapability]]

### customAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityOutput]]


# DateTimeFilterExpression

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteBudgetRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFarmRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFleetRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLicenseEndpointRequest

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLimitRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeteredProductRequest

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitorRequest

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueEnvironmentRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueFleetAssociationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueLimitAssociationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueueRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageProfileRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# DependencyCounts

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


# DisassociateMemberFromFarmRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromFleetRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromJobRequest

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


# DisassociateMemberFromQueueRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes


# Ec2EbsVolume

### sizeGiB
- **Type**: typing.Optional[int]

### iops
- **Type**: typing.Optional[int]

### throughputMiB
- **Type**: typing.Optional[int]


# EnvironmentDetailsEntity

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


# EnvironmentDetailsError

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


# EnvironmentDetailsIdentifiers

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentEnterSessionActionDefinition

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentEnterSessionActionDefinitionSummary

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentExitSessionActionDefinition

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentExitSessionActionDefinitionSummary

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# FarmMember

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


# FarmSummary

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


# FieldSortExpression

### sortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# FileSystemLocation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FixedBudgetSchedule

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.Timestamp'>
- **Required**: Yes


# FixedBudgetScheduleOutput

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FleetAmountCapability

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FleetAttributeCapability

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FleetAttributeCapabilityOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# FleetCapabilities

### amounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapability]]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityOutput]]


# FleetConfiguration

### customerManaged
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedFleetConfiguration]

### serviceManagedEc2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2FleetConfiguration]


# FleetConfigurationOutput

### customerManaged
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.CustomerManagedFleetConfigurationOutput]

### serviceManagedEc2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2FleetConfigurationOutput]


# FleetConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FleetMember

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


# FleetSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationOutput'>
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


# GetBudgetRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBudgetResponse

### budgetId
- **Type**: <class 'str'>
- **Required**: Yes

### usageTrackingResource
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.UsageTrackingResource'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ConsumedUsages'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.ResponseBudgetAction]
- **Required**: Yes

### schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetFarmRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFarmResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetFleetRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFleetRequestWait

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFleetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationOutput'>
- **Required**: Yes

### capabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.FleetCapabilities'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobEntityError

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsError]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsError]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsError]

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsError]


# GetJobRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobRequestWait

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
- **Type**: <class 'NoneType'>


# GetJobResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameter]
- **Required**: Yes

### attachments
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AttachmentsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetLicenseEndpointRequest

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLicenseEndpointRequestWait

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetLicenseEndpointRequestWaitExtra

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetLicenseEndpointResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetLimitRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLimitResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetMonitorRequest

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueEnvironmentRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueEnvironmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueFleetAssociationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueFleetAssociationRequestWait

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
- **Type**: <class 'NoneType'>


# GetQueueFleetAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueLimitAssociationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### limitId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueLimitAssociationRequestWait

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
- **Type**: <class 'NoneType'>


# GetQueueLimitAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueRequestWait

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetQueueRequestWaitExtra

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetQueueResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettings'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUser'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionActionRequest

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


# GetSessionActionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionActionDefinition'>
- **Required**: Yes

### acquiredLimits
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.AcquiredLimit]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionRequest

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


# GetSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponse'>
- **Required**: Yes

### workerLog
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionsStatisticsAggregationRequest

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


# GetSessionsStatisticsAggregationRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# GetSessionsStatisticsAggregationResponse

### statistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.Statistics]
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'TIMEOUT']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetStepRequest

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


# GetStepResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.DependencyCounts'>
- **Required**: Yes

### requiredCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.StepRequiredCapabilities'>
- **Required**: Yes

### parameterSpace
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ParameterSpace'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetStorageProfileForQueueRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageProfileForQueueResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetStorageProfileRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageProfileResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetTaskRequest

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


# GetTaskResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValue]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkerRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### workerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponse'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']
- **Required**: Yes

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# HostPropertiesRequest

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesUnion]

### hostName
- **Type**: typing.Optional[str]


# HostPropertiesResponse

### ipAddresses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.IpAddressesOutput]

### hostName
- **Type**: typing.Optional[str]

### ec2InstanceArn
- **Type**: typing.Optional[str]

### ec2InstanceType
- **Type**: typing.Optional[str]


# IpAddresses

### ipV4Addresses
- **Type**: typing.Optional[typing.Sequence[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.Sequence[str]]


# IpAddressesOutput

### ipV4Addresses
- **Type**: typing.Optional[typing.List[str]]

### ipV6Addresses
- **Type**: typing.Optional[typing.List[str]]


# IpAddressesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobAttachmentDetailsEntity

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### attachments
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.AttachmentsOutput'>
- **Required**: Yes


# JobAttachmentDetailsError

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentDetailsIdentifiers

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobAttachmentSettings

### s3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### rootPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetailsEntity

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettings]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUser]

### queueRoleArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameter]]

### pathMappingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.PathMappingRule]]


# JobDetailsError

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Literal['AccessDeniedException', 'ConflictException', 'InternalServerException', 'MaxPayloadSizeExceeded', 'ResourceNotFoundException', 'ValidationException']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# JobDetailsIdentifiers

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# JobEntity

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsEntity]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsEntity]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsEntity]

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsEntity]


# JobEntityIdentifiersUnion

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobDetailsIdentifiers]

### jobAttachmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentDetailsIdentifiers]

### stepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StepDetailsIdentifiers]

### environmentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentDetailsIdentifiers]


# JobMember

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


# JobParameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunAsUser

### runAs
- **Type**: typing.Literal['QUEUE_CONFIGURED_USER', 'WORKER_AGENT_USER']
- **Required**: Yes

### posix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PosixUser]

### windows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WindowsUser]


# JobSearchSummary

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.JobParameter]]

### maxWorkerCount
- **Type**: typing.Optional[int]

### sourceJobId
- **Type**: typing.Optional[str]


# JobSummary

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


# LicenseEndpointSummary

### licenseEndpointId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'NOT_READY', 'READY']]

### statusMessage
- **Type**: typing.Optional[str]

### vpcId
- **Type**: typing.Optional[str]


# LimitSummary

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


# ListAvailableMeteredProductsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAvailableMeteredProductsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListAvailableMeteredProductsResponse

### meteredProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MeteredProductSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBudgetsRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# ListBudgetsRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListBudgetsResponse

### budgets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.BudgetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFarmMembersRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFarmMembersRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListFarmMembersResponse

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FarmMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFarmsRequest

### nextToken
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFarmsRequestPaginate

### principalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListFarmsResponse

### farms
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FarmSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetMembersRequest

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


# ListFleetMembersRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListFleetMembersResponse

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFleetsRequest

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


# ListFleetsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListFleetsResponse

### fleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobMembersRequest

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


# ListJobMembersRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListJobMembersResponse

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobParameterDefinitionsRequest

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


# ListJobParameterDefinitionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListJobParameterDefinitionsResponse

### jobParameterDefinitions
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

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


# ListJobsRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListJobsResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLicenseEndpointsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLicenseEndpointsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListLicenseEndpointsResponse

### licenseEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.LicenseEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLimitsRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLimitsRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListLimitsResponse

### limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.LimitSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMeteredProductsRequest

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMeteredProductsRequestPaginate

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListMeteredProductsResponse

### meteredProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MeteredProductSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMonitorsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMonitorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListMonitorsResponse

### monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.MonitorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueEnvironmentsRequest

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


# ListQueueEnvironmentsRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListQueueEnvironmentsResponse

### environments
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueEnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueFleetAssociationsRequest

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


# ListQueueFleetAssociationsRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### fleetId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListQueueFleetAssociationsResponse

### queueFleetAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueFleetAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueLimitAssociationsRequest

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


# ListQueueLimitAssociationsRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: typing.Optional[str]

### limitId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListQueueLimitAssociationsResponse

### queueLimitAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueLimitAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueueMembersRequest

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


# ListQueueMembersRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListQueueMembersResponse

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueuesRequest

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


# ListQueuesRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### principalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['IDLE', 'SCHEDULING', 'SCHEDULING_BLOCKED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListQueuesResponse

### queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.QueueSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionActionsRequest

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


# ListSessionActionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListSessionActionsResponse

### sessionActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.SessionActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsForWorkerRequest

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


# ListSessionsForWorkerRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListSessionsForWorkerResponse

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequest

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


# ListSessionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListSessionsResponse

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStepConsumersRequest

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


# ListStepConsumersRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListStepConsumersResponse

### consumers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepConsumer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStepDependenciesRequest

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


# ListStepDependenciesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListStepDependenciesResponse

### dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepDependency]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStepsRequest

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


# ListStepsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListStepsResponse

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStorageProfilesForQueueRequest

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


# ListStorageProfilesForQueueRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### queueId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListStorageProfilesForQueueResponse

### storageProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StorageProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStorageProfilesRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStorageProfilesRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListStorageProfilesResponse

### storageProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StorageProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# ListTasksRequest

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


# ListTasksRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.TaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkersRequest

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


# ListWorkersRequestPaginate

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### fleetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.PaginatorConfig]


# ListWorkersResponse

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogConfiguration

### logDriver
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### error
- **Type**: typing.Optional[str]


# ManifestProperties

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


# ManifestPropertiesOutput

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


# MemoryMiBRange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MeteredProductSummary

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


# MonitorSummary

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterFilterExpression

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterSortExpression

### sortOrder
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ParameterSpace

### parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepParameter]
- **Required**: Yes

### combination
- **Type**: typing.Optional[str]


# PathMappingRule

### sourcePathFormat
- **Type**: typing.Literal['posix', 'windows']
- **Required**: Yes

### sourcePath
- **Type**: <class 'str'>
- **Required**: Yes

### destinationPath
- **Type**: <class 'str'>
- **Required**: Yes


# PosixUser

### user
- **Type**: <class 'str'>
- **Required**: Yes

### group
- **Type**: <class 'str'>
- **Required**: Yes


# PutMeteredProductRequest

### licenseEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes


# QueueEnvironmentSummary

### queueEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes


# QueueFleetAssociationSummary

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


# QueueLimitAssociationSummary

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


# QueueMember

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


# QueueSummary

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


# ResponseBudgetAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes


# SearchFilterExpression

### dateTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.DateTimeFilterExpression]

### parameterFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterFilterExpression]

### searchTermFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchTermFilterExpression]

### stringFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.StringFilterExpression]

### groupFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# SearchGroupedFilterExpressions

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchJobsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressions]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpression]]

### pageSize
- **Type**: typing.Optional[int]


# SearchJobsResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.JobSearchSummary]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# SearchSortExpression

### userJobsFirst
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.UserJobsFirst]

### fieldSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FieldSortExpression]

### parameterSort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterSortExpression]


# SearchStepsRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressions]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpression]]

### pageSize
- **Type**: typing.Optional[int]


# SearchStepsResponse

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepSearchSummary]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# SearchTasksRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressions]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpression]]

### pageSize
- **Type**: typing.Optional[int]


# SearchTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.TaskSearchSummary]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# SearchTermFilterExpression

### searchTerm
- **Type**: <class 'str'>
- **Required**: Yes


# SearchWorkersRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SearchGroupedFilterExpressions]

### sortExpressions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.SearchSortExpression]]

### pageSize
- **Type**: typing.Optional[int]


# SearchWorkersResponse

### workers
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.WorkerSearchSummary]
- **Required**: Yes

### nextItemOffset
- **Type**: <class 'int'>
- **Required**: Yes

### totalResults
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# ServiceManagedEc2FleetConfiguration

### instanceCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceCapabilities'>
- **Required**: Yes

### instanceMarketOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceMarketOptions'>
- **Required**: Yes


# ServiceManagedEc2FleetConfigurationOutput

### instanceCapabilities
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceCapabilitiesOutput'>
- **Required**: Yes

### instanceMarketOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ServiceManagedEc2InstanceMarketOptions'>
- **Required**: Yes


# ServiceManagedEc2InstanceCapabilities

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRange'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRange'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'WINDOWS']
- **Required**: Yes

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### rootEbsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Ec2EbsVolume]

### acceleratorCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCapabilities]

### allowedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### customAmounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapability]]

### customAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapability]]


# ServiceManagedEc2InstanceCapabilitiesOutput

### vCpuCount
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.VCpuCountRange'>
- **Required**: Yes

### memoryMiB
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.MemoryMiBRange'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'WINDOWS']
- **Required**: Yes

### cpuArchitectureType
- **Type**: typing.Literal['arm64', 'x86_64']
- **Required**: Yes

### rootEbsVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Ec2EbsVolume]

### acceleratorCapabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.AcceleratorCapabilitiesOutput]

### allowedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### excludedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### customAmounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAmountCapability]]

### customAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.deadline_classes.FleetAttributeCapabilityOutput]]


# ServiceManagedEc2InstanceMarketOptions

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SessionActionDefinition

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentEnterSessionActionDefinition]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentExitSessionActionDefinition]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TaskRunSessionActionDefinition]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SyncInputJobAttachmentsSessionActionDefinition]


# SessionActionDefinitionSummary

### envEnter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentEnterSessionActionDefinitionSummary]

### envExit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.EnvironmentExitSessionActionDefinitionSummary]

### taskRun
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.TaskRunSessionActionDefinitionSummary]

### syncInputJobAttachments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.SyncInputJobAttachmentsSessionActionDefinitionSummary]


# SessionActionSummary

### sessionActionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ASSIGNED', 'CANCELED', 'CANCELING', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'RECLAIMED', 'RECLAIMING', 'RUNNING', 'SCHEDULED', 'SUCCEEDED']
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionActionDefinitionSummary'>
- **Required**: Yes

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### workerUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### progressPercent
- **Type**: typing.Optional[float]


# SessionSummary

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


# SessionsStatisticsResources

### queueIds
- **Type**: typing.Optional[typing.Sequence[str]]

### fleetIds
- **Type**: typing.Optional[typing.Sequence[str]]


# StartSessionsStatisticsAggregationRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceIds
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.SessionsStatisticsResources'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.Timestamp'>
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


# StartSessionsStatisticsAggregationResponse

### aggregationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# Statistics

### count
- **Type**: <class 'int'>
- **Required**: Yes

### costInUsd
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.Stats'>
- **Required**: Yes

### runtimeInSeconds
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.Stats'>
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


# Stats

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepAmountCapability

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepAttributeCapability

### name
- **Type**: <class 'str'>
- **Required**: Yes

### anyOf
- **Type**: typing.Optional[typing.List[str]]

### allOf
- **Type**: typing.Optional[typing.List[str]]


# StepConsumer

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['RESOLVED', 'UNRESOLVED']
- **Required**: Yes


# StepDependency

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['RESOLVED', 'UNRESOLVED']
- **Required**: Yes


# StepDetailsEntity

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


# StepDetailsError

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


# StepDetailsIdentifiers

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# StepParameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepRequiredCapabilities

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepAttributeCapability]
- **Required**: Yes

### amounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.deadline_classes.StepAmountCapability]
- **Required**: Yes


# StepSearchSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.ParameterSpace]


# StepSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.DependencyCounts]


# StorageProfileSummary

### storageProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### osFamily
- **Type**: typing.Literal['LINUX', 'MACOS', 'WINDOWS']
- **Required**: Yes


# StringFilterExpression

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SyncInputJobAttachmentsSessionActionDefinition

### stepId
- **Type**: typing.Optional[str]


# SyncInputJobAttachmentsSessionActionDefinitionSummary

### stepId
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TaskParameterValue

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskRunSessionActionDefinition

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValue]
- **Required**: Yes


# TaskRunSessionActionDefinitionSummary

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes


# TaskSearchSummary

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValue]]

### failureRetryCount
- **Type**: typing.Optional[int]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]


# TaskSummary

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.TaskParameterValue]]

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


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBudgetRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToAdd]]

### actionsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.BudgetActionToRemove]]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.BudgetScheduleUnion]


# UpdateFarmRequest

### farmId
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateFleetRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.FleetConfigurationUnion]


# UpdateJobRequest

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


# UpdateLimitRequest

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


# UpdateMonitorRequest

### monitorId
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# UpdateQueueEnvironmentRequest

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


# UpdateQueueFleetAssociationRequest

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


# UpdateQueueLimitAssociationRequest

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


# UpdateQueueRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobAttachmentSettings]

### roleArn
- **Type**: typing.Optional[str]

### jobRunAsUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.JobRunAsUser]

### requiredFileSystemLocationNamesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### requiredFileSystemLocationNamesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedStorageProfileIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateSessionRequest

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


# UpdateStepRequest

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


# UpdateStorageProfileRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocation]]

### fileSystemLocationsToRemove
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.FileSystemLocation]]


# UpdateTaskRequest

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


# UpdateWorkerRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.WorkerCapabilities]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesRequest]


# UpdateWorkerResponse

### log
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.LogConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkerScheduleRequest

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.deadline_classes.UpdatedSessionActionInfo]]


# UpdateWorkerScheduleResponse

### assignedSessions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.deadline_classes.AssignedSession]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.deadline_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatedSessionActionInfo

### completedStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'INTERRUPTED', 'NEVER_ATTEMPTED', 'SUCCEEDED']]

### processExitCode
- **Type**: typing.Optional[int]

### progressMessage
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Timestamp]

### endedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Timestamp]

### updatedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.Timestamp]

### progressPercent
- **Type**: typing.Optional[float]


# UsageTrackingResource

### queueId
- **Type**: typing.Optional[str]


# UserJobsFirst

### userIdentityId
- **Type**: <class 'str'>
- **Required**: Yes


# VCpuCountRange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WindowsUser

### user
- **Type**: <class 'str'>
- **Required**: Yes

### passwordArn
- **Type**: <class 'str'>
- **Required**: Yes


# WorkerAmountCapability

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# WorkerAttributeCapability

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkerCapabilities

### amounts
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.WorkerAmountCapability]
- **Required**: Yes

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.deadline_classes.WorkerAttributeCapability]
- **Required**: Yes


# WorkerSearchSummary

### fleetId
- **Type**: typing.Optional[str]

### workerId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'IDLE', 'NOT_COMPATIBLE', 'NOT_RESPONDING', 'RUNNING', 'STARTED', 'STOPPED', 'STOPPING']]

### hostProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponse]

### createdBy
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# WorkerSessionSummary

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


# WorkerSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.HostPropertiesResponse]

### log
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.deadline_classes.LogConfiguration]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]


