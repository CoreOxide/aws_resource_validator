# Ssm Classes

# AccountSharingInfoTypeDef

### AccountId
- **Type**: typing.Optional[str]

### SharedDocumentVersion
- **Type**: typing.Optional[str]


# ActivationTypeDef

### ActivationId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultInstanceName
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[str]

### RegistrationLimit
- **Type**: typing.Optional[int]

### RegistrationsCount
- **Type**: typing.Optional[int]

### ExpirationDate
- **Type**: typing.Optional[datetime.datetime]

### Expired
- **Type**: typing.Optional[bool]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]


# AddTagsToResourceRequestTypeDef

### ResourceType
- **Type**: typing.Literal['Association', 'Automation', 'Document', 'MaintenanceWindow', 'ManagedInstance', 'OpsItem', 'OpsMetadata', 'Parameter', 'PatchBaseline']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]
- **Required**: Yes


# AlarmConfigurationOutputTypeDef

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmTypeDef]
- **Required**: Yes

### IgnorePollAlarmFailure
- **Type**: typing.Optional[bool]


# AlarmConfigurationTypeDef

### Alarms
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AlarmTypeDef]
- **Required**: Yes

### IgnorePollAlarmFailure
- **Type**: typing.Optional[bool]


# AlarmConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmStateInformationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ALARM', 'UNKNOWN']
- **Required**: Yes


# AlarmTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateOpsItemRelatedItemRequestTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceUri
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateOpsItemRelatedItemResponseTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociationDescriptionTypeDef

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateAssociationDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AssociationStatusOutputTypeDef]

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AssociationOverviewTypeDef]

### DocumentVersion
- **Type**: typing.Optional[str]

### AutomationTargetParameterName
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### AssociationId
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputLocationTypeDef]

### LastExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### AssociationName
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### ComplianceSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### SyncCompliance
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### ApplyOnlyAtCronInterval
- **Type**: typing.Optional[bool]

### CalendarNames
- **Type**: typing.Optional[typing.List[str]]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationOutputTypeDef]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]


# AssociationExecutionFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociationExecutionTargetTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### ExecutionId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### DetailedStatus
- **Type**: typing.Optional[str]

### LastExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### OutputSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.OutputSourceTypeDef]


# AssociationExecutionTargetsFilterTypeDef

### Key
- **Type**: typing.Literal['ResourceId', 'ResourceType', 'Status']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationExecutionTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### ExecutionId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### DetailedStatus
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### ResourceCountByStatus
- **Type**: typing.Optional[str]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]


# AssociationFilterTypeDef

### key
- **Type**: typing.Literal['AssociationId', 'AssociationName', 'AssociationStatusName', 'InstanceId', 'LastExecutedAfter', 'LastExecutedBefore', 'Name', 'ResourceGroupName']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationOverviewTypeDef

### Status
- **Type**: typing.Optional[str]

### DetailedStatus
- **Type**: typing.Optional[str]

### AssociationStatusAggregatedCount
- **Type**: typing.Optional[typing.Dict[str, int]]


# AssociationStatusOutputTypeDef

### Date
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: typing.Literal['Failed', 'Pending', 'Success']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalInfo
- **Type**: typing.Optional[str]


# AssociationStatusTypeDef

### Date
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef'>
- **Required**: Yes

### Name
- **Type**: typing.Literal['Failed', 'Pending', 'Success']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalInfo
- **Type**: typing.Optional[str]


# AssociationStatusUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociationTypeDef

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### LastExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AssociationOverviewTypeDef]

### ScheduleExpression
- **Type**: typing.Optional[str]

### AssociationName
- **Type**: typing.Optional[str]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]


# AssociationVersionInfoTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputLocationTypeDef]

### AssociationName
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### ComplianceSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### SyncCompliance
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### ApplyOnlyAtCronInterval
- **Type**: typing.Optional[bool]

### CalendarNames
- **Type**: typing.Optional[typing.List[str]]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationOutputTypeDef]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]


# AttachmentContentTypeDef

### Name
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[int]

### Hash
- **Type**: typing.Optional[str]

### HashType
- **Type**: typing.Optional[typing.Literal['Sha256']]

### Url
- **Type**: typing.Optional[str]


# AttachmentInformationTypeDef

### Name
- **Type**: typing.Optional[str]


# AttachmentsSourceTypeDef

### Key
- **Type**: typing.Optional[typing.Literal['AttachmentReference', 'S3FileUrl', 'SourceUrl']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### Name
- **Type**: typing.Optional[str]


# AutomationExecutionFilterTypeDef

### Key
- **Type**: typing.Literal['AutomationSubtype', 'AutomationType', 'CurrentAction', 'DocumentNamePrefix', 'ExecutionId', 'ExecutionStatus', 'OpsItemId', 'ParentExecutionId', 'StartTimeAfter', 'StartTimeBefore', 'TagKey', 'TargetResourceGroup']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AutomationExecutionInputsTypeDef

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### TargetMaps
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Sequence[str]]]]

### TargetLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationUnionTypeDef]]

### TargetLocationsURL
- **Type**: typing.Optional[str]


# AutomationExecutionMetadataTypeDef

### AutomationExecutionId
- **Type**: typing.Optional[str]

### DocumentName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### AutomationExecutionStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'CompletedWithFailure', 'CompletedWithSuccess', 'Exited', 'Failed', 'InProgress', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'RunbookInProgress', 'Scheduled', 'Success', 'TimedOut', 'Waiting']]

### ExecutionStartTime
- **Type**: typing.Optional[datetime.datetime]

### ExecutionEndTime
- **Type**: typing.Optional[datetime.datetime]

### ExecutedBy
- **Type**: typing.Optional[str]

### LogFile
- **Type**: typing.Optional[str]

### Outputs
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Mode
- **Type**: typing.Optional[typing.Literal['Auto', 'Interactive']]

### ParentAutomationExecutionId
- **Type**: typing.Optional[str]

### CurrentStepName
- **Type**: typing.Optional[str]

### CurrentAction
- **Type**: typing.Optional[str]

### FailureMessage
- **Type**: typing.Optional[str]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### ResolvedTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResolvedTargetsTypeDef]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### AutomationType
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'Local']]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]

### TargetLocationsURL
- **Type**: typing.Optional[str]

### AutomationSubtype
- **Type**: typing.Optional[typing.Literal['ChangeRequest']]

### ScheduledTime
- **Type**: typing.Optional[datetime.datetime]

### Runbooks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.RunbookOutputTypeDef]]

### OpsItemId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### ChangeRequestName
- **Type**: typing.Optional[str]


# AutomationExecutionPreviewTypeDef

### StepPreviews
- **Type**: typing.Optional[typing.Dict[typing.Literal['Mutating', 'NonMutating', 'Undetermined'], int]]

### Regions
- **Type**: typing.Optional[typing.List[str]]

### TargetPreviews
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetPreviewTypeDef]]

### TotalAccounts
- **Type**: typing.Optional[int]


# AutomationExecutionTypeDef

### AutomationExecutionId
- **Type**: typing.Optional[str]

### DocumentName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### ExecutionStartTime
- **Type**: typing.Optional[datetime.datetime]

### ExecutionEndTime
- **Type**: typing.Optional[datetime.datetime]

### AutomationExecutionStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'CompletedWithFailure', 'CompletedWithSuccess', 'Exited', 'Failed', 'InProgress', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'RunbookInProgress', 'Scheduled', 'Success', 'TimedOut', 'Waiting']]

### StepExecutions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.StepExecutionTypeDef]]

### StepExecutionsTruncated
- **Type**: typing.Optional[bool]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Outputs
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### FailureMessage
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['Auto', 'Interactive']]

### ParentAutomationExecutionId
- **Type**: typing.Optional[str]

### ExecutedBy
- **Type**: typing.Optional[str]

### CurrentStepName
- **Type**: typing.Optional[str]

### CurrentAction
- **Type**: typing.Optional[str]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### ResolvedTargets
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResolvedTargetsTypeDef]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationOutputTypeDef]]

### ProgressCounters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ProgressCountersTypeDef]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]

### TargetLocationsURL
- **Type**: typing.Optional[str]

### AutomationSubtype
- **Type**: typing.Optional[typing.Literal['ChangeRequest']]

### ScheduledTime
- **Type**: typing.Optional[datetime.datetime]

### Runbooks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.RunbookOutputTypeDef]]

### OpsItemId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### ChangeRequestName
- **Type**: typing.Optional[str]

### Variables
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineOverrideTypeDef

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]

### GlobalFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupUnionTypeDef]

### ApprovalRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchRuleGroupUnionTypeDef]

### ApprovedPatches
- **Type**: typing.Optional[typing.Sequence[str]]

### ApprovedPatchesComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### RejectedPatches
- **Type**: typing.Optional[typing.Sequence[str]]

### RejectedPatchesAction
- **Type**: typing.Optional[typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']]

### ApprovedPatchesEnableNonSecurity
- **Type**: typing.Optional[bool]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchSourceUnionTypeDef]]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelCommandRequestTypeDef

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CancelMaintenanceWindowExecutionRequestTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMaintenanceWindowExecutionResultTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudWatchOutputConfigTypeDef

### CloudWatchLogGroupName
- **Type**: typing.Optional[str]

### CloudWatchOutputEnabled
- **Type**: typing.Optional[bool]


# CommandFilterTypeDef

### key
- **Type**: typing.Literal['DocumentName', 'ExecutionStage', 'InvokedAfter', 'InvokedBefore', 'Status']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CommandInvocationTypeDef

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceName
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### DocumentName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### RequestedDateTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Delayed', 'Failed', 'InProgress', 'Pending', 'Success', 'TimedOut']]

### StatusDetails
- **Type**: typing.Optional[str]

### TraceOutput
- **Type**: typing.Optional[str]

### StandardOutputUrl
- **Type**: typing.Optional[str]

### StandardErrorUrl
- **Type**: typing.Optional[str]

### CommandPlugins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.CommandPluginTypeDef]]

### ServiceRole
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NotificationConfigOutputTypeDef]

### CloudWatchOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CloudWatchOutputConfigTypeDef]


# CommandPluginTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Failed', 'InProgress', 'Pending', 'Success', 'TimedOut']]

### StatusDetails
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[int]

### ResponseStartDateTime
- **Type**: typing.Optional[datetime.datetime]

### ResponseFinishDateTime
- **Type**: typing.Optional[datetime.datetime]

### Output
- **Type**: typing.Optional[str]

### StandardOutputUrl
- **Type**: typing.Optional[str]

### StandardErrorUrl
- **Type**: typing.Optional[str]

### OutputS3Region
- **Type**: typing.Optional[str]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]


# CommandTypeDef

### CommandId
- **Type**: typing.Optional[str]

### DocumentName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### ExpiresAfter
- **Type**: typing.Optional[datetime.datetime]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### RequestedDateTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Cancelling', 'Failed', 'InProgress', 'Pending', 'Success', 'TimedOut']]

### StatusDetails
- **Type**: typing.Optional[str]

### OutputS3Region
- **Type**: typing.Optional[str]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetCount
- **Type**: typing.Optional[int]

### CompletedCount
- **Type**: typing.Optional[int]

### ErrorCount
- **Type**: typing.Optional[int]

### DeliveryTimedOutCount
- **Type**: typing.Optional[int]

### ServiceRole
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NotificationConfigOutputTypeDef]

### CloudWatchOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CloudWatchOutputConfigTypeDef]

### TimeoutSeconds
- **Type**: typing.Optional[int]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]


# ComplianceExecutionSummaryOutputTypeDef

### ExecutionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionId
- **Type**: typing.Optional[str]

### ExecutionType
- **Type**: typing.Optional[str]


# ComplianceExecutionSummaryTypeDef

### ExecutionTime
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef'>
- **Required**: Yes

### ExecutionId
- **Type**: typing.Optional[str]

### ExecutionType
- **Type**: typing.Optional[str]


# ComplianceExecutionSummaryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComplianceItemEntryTypeDef

### Severity
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLIANT', 'NON_COMPLIANT']
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ComplianceItemTypeDef

### ComplianceType
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'NON_COMPLIANT']]

### Severity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ComplianceExecutionSummaryOutputTypeDef]

### Details
- **Type**: typing.Optional[typing.Dict[str, str]]


# ComplianceStringFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComplianceSummaryItemTypeDef

### ComplianceType
- **Type**: typing.Optional[str]

### CompliantSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CompliantSummaryTypeDef]

### NonCompliantSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NonCompliantSummaryTypeDef]


# CompliantSummaryTypeDef

### CompliantCount
- **Type**: typing.Optional[int]

### SeveritySummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.SeveritySummaryTypeDef]


# CreateActivationRequestTypeDef

### IamRole
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DefaultInstanceName
- **Type**: typing.Optional[str]

### RegistrationLimit
- **Type**: typing.Optional[int]

### ExpirationDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### RegistrationMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.RegistrationMetadataItemTypeDef]]


# CreateActivationResultTypeDef

### ActivationId
- **Type**: <class 'str'>
- **Required**: Yes

### ActivationCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssociationBatchRequestEntryOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### AutomationTargetParameterName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputLocationTypeDef]

### AssociationName
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### ComplianceSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### SyncCompliance
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### ApplyOnlyAtCronInterval
- **Type**: typing.Optional[bool]

### CalendarNames
- **Type**: typing.Optional[typing.List[str]]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationOutputTypeDef]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]


# CreateAssociationBatchRequestEntryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### AutomationTargetParameterName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputLocationTypeDef]

### AssociationName
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### ComplianceSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### SyncCompliance
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### ApplyOnlyAtCronInterval
- **Type**: typing.Optional[bool]

### CalendarNames
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationUnionTypeDef]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Sequence[str]]]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]


# CreateAssociationBatchRequestEntryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAssociationBatchRequestTypeDef

### Entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.CreateAssociationBatchRequestEntryUnionTypeDef]
- **Required**: Yes


# CreateAssociationBatchResultTypeDef

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AssociationDescriptionTypeDef]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.FailedCreateAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssociationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputLocationTypeDef]

### AssociationName
- **Type**: typing.Optional[str]

### AutomationTargetParameterName
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### ComplianceSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### SyncCompliance
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### ApplyOnlyAtCronInterval
- **Type**: typing.Optional[bool]

### CalendarNames
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationUnionTypeDef]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Sequence[str]]]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]


# CreateAssociationResultTypeDef

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AssociationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDocumentRequestTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Requires
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DocumentRequiresTypeDef]]

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AttachmentsSourceTypeDef]]

### DisplayName
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### DocumentType
- **Type**: typing.Optional[typing.Literal['ApplicationConfiguration', 'ApplicationConfigurationSchema', 'Automation', 'Automation.ChangeTemplate', 'ChangeCalendar', 'CloudFormation', 'Command', 'ConformancePackTemplate', 'DeploymentStrategy', 'Package', 'Policy', 'ProblemAnalysis', 'ProblemAnalysisTemplate', 'QuickSetup', 'Session']]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]

### TargetType
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]


# CreateDocumentResultTypeDef

### DocumentDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.DocumentDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMaintenanceWindowRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Cutoff
- **Type**: <class 'int'>
- **Required**: Yes

### AllowUnassociatedTargets
- **Type**: <class 'bool'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### ScheduleTimezone
- **Type**: typing.Optional[str]

### ScheduleOffset
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]


# CreateMaintenanceWindowResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOpsItemRequestTypeDef

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### OpsItemType
- **Type**: typing.Optional[str]

### OperationalData
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_classes.OpsItemDataValueTypeDef]]

### Notifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemNotificationTypeDef]]

### Priority
- **Type**: typing.Optional[int]

### RelatedOpsItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.RelatedOpsItemTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### Category
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ActualStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### ActualEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### PlannedStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### PlannedEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### AccountId
- **Type**: typing.Optional[str]


# CreateOpsItemResponseTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### OpsItemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOpsMetadataRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_classes.MetadataValueTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]


# CreateOpsMetadataResultTypeDef

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePatchBaselineRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]

### GlobalFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupUnionTypeDef]

### ApprovalRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchRuleGroupUnionTypeDef]

### ApprovedPatches
- **Type**: typing.Optional[typing.Sequence[str]]

### ApprovedPatchesComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApprovedPatchesEnableNonSecurity
- **Type**: typing.Optional[bool]

### RejectedPatches
- **Type**: typing.Optional[typing.Sequence[str]]

### RejectedPatchesAction
- **Type**: typing.Optional[typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']]

### Description
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchSourceUnionTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]


# CreatePatchBaselineResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceDataSyncRequestTypeDef

### SyncName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncS3DestinationTypeDef]

### SyncType
- **Type**: typing.Optional[str]

### SyncSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncSourceTypeDef]


# DeleteActivationRequestTypeDef

### ActivationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssociationRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]


# DeleteDocumentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# DeleteInventoryRequestTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaDeleteOption
- **Type**: typing.Optional[typing.Literal['DeleteSchema', 'DisableSchema']]

### DryRun
- **Type**: typing.Optional[bool]

### ClientToken
- **Type**: typing.Optional[str]


# DeleteInventoryResultTypeDef

### DeletionId
- **Type**: <class 'str'>
- **Required**: Yes

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.InventoryDeletionSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMaintenanceWindowResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteOpsItemRequestTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOpsMetadataRequestTypeDef

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParameterRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParametersRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteParametersResultTypeDef

### DeletedParameters
- **Type**: typing.List[str]
- **Required**: Yes

### InvalidParameters
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePatchBaselineRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePatchBaselineResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourceDataSyncRequestTypeDef

### SyncName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Optional[str]


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterManagedInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterPatchBaselineForPatchGroupRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterPatchBaselineForPatchGroupResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterTargetFromMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Safe
- **Type**: typing.Optional[bool]


# DeregisterTargetFromMaintenanceWindowResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterTaskFromMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTaskFromMaintenanceWindowResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeActivationsFilterTypeDef

### FilterKey
- **Type**: typing.Optional[typing.Literal['ActivationIds', 'DefaultInstanceName', 'IamRole']]

### FilterValues
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeActivationsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DescribeActivationsFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeActivationsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DescribeActivationsFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeActivationsResultTypeDef

### ActivationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ActivationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionTargetsRequestPaginateTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AssociationExecutionTargetsFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeAssociationExecutionTargetsRequestTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AssociationExecutionTargetsFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionTargetsResultTypeDef

### AssociationExecutionTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AssociationExecutionTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionsRequestPaginateTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AssociationExecutionFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeAssociationExecutionsRequestTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AssociationExecutionFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionsResultTypeDef

### AssociationExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AssociationExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]


# DescribeAssociationResultTypeDef

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AssociationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAutomationExecutionsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AutomationExecutionFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeAutomationExecutionsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AutomationExecutionFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAutomationExecutionsResultTypeDef

### AutomationExecutionMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AutomationExecutionMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAutomationStepExecutionsRequestPaginateTypeDef

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.StepExecutionFilterTypeDef]]

### ReverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeAutomationStepExecutionsRequestTypeDef

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.StepExecutionFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ReverseOrder
- **Type**: typing.Optional[bool]


# DescribeAutomationStepExecutionsResultTypeDef

### StepExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.StepExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAvailablePatchesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeAvailablePatchesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAvailablePatchesResultTypeDef

### Patches
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDocumentPermissionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionType
- **Type**: typing.Literal['Share']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDocumentPermissionResponseTypeDef

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### AccountSharingInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AccountSharingInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDocumentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]


# DescribeDocumentResultTypeDef

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.DocumentDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeEffectiveInstanceAssociationsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEffectiveInstanceAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeEffectivePatchesForPatchBaselineRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEffectivePatchesForPatchBaselineResultTypeDef

### EffectivePatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.EffectivePatchTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceAssociationsStatusRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInstanceAssociationsStatusRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceAssociationsStatusResultTypeDef

### InstanceAssociationStatusInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationStatusInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceInformationRequestPaginateTypeDef

### InstanceInformationFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstanceInformationFilterTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstanceInformationStringFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInstanceInformationRequestTypeDef

### InstanceInformationFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstanceInformationFilterTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstanceInformationStringFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceInformationResultTypeDef

### InstanceInformationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InstanceInformationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstancePatchStateFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInstancePatchStatesForPatchGroupRequestTypeDef

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstancePatchStateFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInstancePatchStatesForPatchGroupResultTypeDef

### InstancePatchStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InstancePatchStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePatchStatesRequestPaginateTypeDef

### InstanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInstancePatchStatesRequestTypeDef

### InstanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInstancePatchStatesResultTypeDef

### InstancePatchStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InstancePatchStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePatchesRequestPaginateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInstancePatchesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInstancePatchesResultTypeDef

### Patches
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchComplianceDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePropertiesRequestPaginateTypeDef

### InstancePropertyFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstancePropertyFilterTypeDef]]

### FiltersWithOperator
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstancePropertyStringFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInstancePropertiesRequestTypeDef

### InstancePropertyFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstancePropertyFilterTypeDef]]

### FiltersWithOperator
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InstancePropertyStringFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePropertiesResultTypeDef

### InstanceProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InstancePropertyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInventoryDeletionsRequestPaginateTypeDef

### DeletionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeInventoryDeletionsRequestTypeDef

### DeletionId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInventoryDeletionsResultTypeDef

### InventoryDeletions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InventoryDeletionStatusItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef

### WindowExecutionTaskInvocationIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowExecutionTaskInvocationIdentityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowExecutionTasksRequestTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTasksResultTypeDef

### WindowExecutionTaskIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowExecutionTaskIdentityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowExecutionsRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionsResultTypeDef

### WindowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowScheduleRequestPaginateTypeDef

### WindowId
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'RESOURCE_GROUP']]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowScheduleRequestTypeDef

### WindowId
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'RESOURCE_GROUP']]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowScheduleResultTypeDef

### ScheduledWindowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ScheduledWindowExecutionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTargetsRequestPaginateTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowTargetsRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTargetsResultTypeDef

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTasksRequestPaginateTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowTasksRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTasksResultTypeDef

### Tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['INSTANCE', 'RESOURCE_GROUP']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowsForTargetRequestTypeDef

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['INSTANCE', 'RESOURCE_GROUP']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsForTargetResultTypeDef

### WindowIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowIdentityForTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeMaintenanceWindowsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsResultTypeDef

### WindowIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowIdentityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOpsItemsRequestPaginateTypeDef

### OpsItemFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeOpsItemsRequestTypeDef

### OpsItemFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOpsItemsResponseTypeDef

### OpsItemSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.OpsItemSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ParametersFilterTypeDef]]

### ParameterFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ParameterStringFilterTypeDef]]

### Shared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeParametersRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ParametersFilterTypeDef]]

### ParameterFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ParameterStringFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Shared
- **Type**: typing.Optional[bool]


# DescribeParametersResultTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ParameterMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchBaselinesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribePatchBaselinesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchBaselinesResultTypeDef

### BaselineIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchBaselineIdentityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchGroupStateRequestTypeDef

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePatchGroupStateResultTypeDef

### Instances
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithInstalledPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithInstalledOtherPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithInstalledPendingRebootPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithInstalledRejectedPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithMissingPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithFailedPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithNotApplicablePatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithUnreportedNotApplicablePatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithCriticalNonCompliantPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithSecurityNonCompliantPatches
- **Type**: <class 'int'>
- **Required**: Yes

### InstancesWithOtherNonCompliantPatches
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePatchGroupsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribePatchGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchOrchestratorFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchGroupsResultTypeDef

### Mappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchGroupPatchBaselineMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchPropertiesRequestPaginateTypeDef

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### Property
- **Type**: typing.Literal['CLASSIFICATION', 'MSRC_SEVERITY', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'SEVERITY']
- **Required**: Yes

### PatchSet
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribePatchPropertiesRequestTypeDef

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### Property
- **Type**: typing.Literal['CLASSIFICATION', 'MSRC_SEVERITY', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'SEVERITY']
- **Required**: Yes

### PatchSet
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OS']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchPropertiesResultTypeDef

### Properties
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSessionsRequestPaginateTypeDef

### State
- **Type**: typing.Literal['Active', 'History']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.SessionFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# DescribeSessionsRequestTypeDef

### State
- **Type**: typing.Literal['Active', 'History']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.SessionFilterTypeDef]]


# DescribeSessionsResponseTypeDef

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.SessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateOpsItemRelatedItemRequestTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentDefaultVersionDescriptionTypeDef

### Name
- **Type**: typing.Optional[str]

### DefaultVersion
- **Type**: typing.Optional[str]

### DefaultVersionName
- **Type**: typing.Optional[str]


# DocumentDescriptionTypeDef

### Sha1
- **Type**: typing.Optional[str]

### Hash
- **Type**: typing.Optional[str]

### HashType
- **Type**: typing.Optional[typing.Literal['Sha1', 'Sha256']]

### Name
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']]

### StatusInformation
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentParameterTypeDef]]

### PlatformTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Linux', 'MacOS', 'Windows']]]

### DocumentType
- **Type**: typing.Optional[typing.Literal['ApplicationConfiguration', 'ApplicationConfigurationSchema', 'Automation', 'Automation.ChangeTemplate', 'ChangeCalendar', 'CloudFormation', 'Command', 'ConformancePackTemplate', 'DeploymentStrategy', 'Package', 'Policy', 'ProblemAnalysis', 'ProblemAnalysisTemplate', 'QuickSetup', 'Session']]

### SchemaVersion
- **Type**: typing.Optional[str]

### LatestVersion
- **Type**: typing.Optional[str]

### DefaultVersion
- **Type**: typing.Optional[str]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]

### TargetType
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### AttachmentsInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AttachmentInformationTypeDef]]

### Requires
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentRequiresTypeDef]]

### Author
- **Type**: typing.Optional[str]

### ReviewInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.ReviewInformationTypeDef]]

### ApprovedVersion
- **Type**: typing.Optional[str]

### PendingReviewVersion
- **Type**: typing.Optional[str]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Category
- **Type**: typing.Optional[typing.List[str]]

### CategoryEnum
- **Type**: typing.Optional[typing.List[str]]


# DocumentFilterTypeDef

### key
- **Type**: typing.Literal['DocumentType', 'Name', 'Owner', 'PlatformTypes']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentIdentifierTypeDef

### Name
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### DisplayName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### PlatformTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Linux', 'MacOS', 'Windows']]]

### DocumentVersion
- **Type**: typing.Optional[str]

### DocumentType
- **Type**: typing.Optional[typing.Literal['ApplicationConfiguration', 'ApplicationConfigurationSchema', 'Automation', 'Automation.ChangeTemplate', 'ChangeCalendar', 'CloudFormation', 'Command', 'ConformancePackTemplate', 'DeploymentStrategy', 'Package', 'Policy', 'ProblemAnalysis', 'ProblemAnalysisTemplate', 'QuickSetup', 'Session']]

### SchemaVersion
- **Type**: typing.Optional[str]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]

### TargetType
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### Requires
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentRequiresTypeDef]]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Author
- **Type**: typing.Optional[str]


# DocumentKeyValuesFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# DocumentMetadataResponseInfoTypeDef

### ReviewerResponse
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentReviewerResponseSourceTypeDef]]


# DocumentParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentRequiresTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### RequireType
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]


# DocumentReviewCommentSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentReviewerResponseSourceTypeDef

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Comment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentReviewCommentSourceTypeDef]]

### Reviewer
- **Type**: typing.Optional[str]


# DocumentReviewsTypeDef

### Action
- **Type**: typing.Literal['Approve', 'Reject', 'SendForReview', 'UpdateReview']
- **Required**: Yes

### Comment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DocumentReviewCommentSourceTypeDef]]


# DocumentVersionInfoTypeDef

### Name
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### IsDefaultVersion
- **Type**: typing.Optional[bool]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']]

### StatusInformation
- **Type**: typing.Optional[str]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]


# EffectivePatchTypeDef

### Patch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchTypeDef]

### PatchStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchStatusTypeDef]


# ExecutionInputsTypeDef

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AutomationExecutionInputsTypeDef]


# ExecutionPreviewTypeDef

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AutomationExecutionPreviewTypeDef]


# FailedCreateAssociationTypeDef

### Entry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CreateAssociationBatchRequestEntryOutputTypeDef]

### Message
- **Type**: typing.Optional[str]

### Fault
- **Type**: typing.Optional[typing.Literal['Client', 'Server', 'Unknown']]


# FailureDetailsTypeDef

### FailureStage
- **Type**: typing.Optional[str]

### FailureType
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# GetAutomationExecutionRequestTypeDef

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAutomationExecutionResultTypeDef

### AutomationExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AutomationExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCalendarStateRequestTypeDef

### CalendarNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AtTime
- **Type**: typing.Optional[str]


# GetCalendarStateResponseTypeDef

### State
- **Type**: typing.Literal['CLOSED', 'OPEN']
- **Required**: Yes

### AtTime
- **Type**: <class 'str'>
- **Required**: Yes

### NextTransitionTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCommandInvocationRequestTypeDef

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginName
- **Type**: typing.Optional[str]


# GetCommandInvocationRequestWaitTypeDef

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginName
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.WaiterConfigTypeDef]


# GetCommandInvocationResultTypeDef

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PluginName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseCode
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutionStartDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionElapsedTime
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionEndDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Cancelled', 'Cancelling', 'Delayed', 'Failed', 'InProgress', 'Pending', 'Success', 'TimedOut']
- **Required**: Yes

### StatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### StandardOutputContent
- **Type**: <class 'str'>
- **Required**: Yes

### StandardOutputUrl
- **Type**: <class 'str'>
- **Required**: Yes

### StandardErrorContent
- **Type**: <class 'str'>
- **Required**: Yes

### StandardErrorUrl
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.CloudWatchOutputConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionStatusRequestTypeDef

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionStatusResponseTypeDef

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['connected', 'notconnected']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDefaultPatchBaselineRequestTypeDef

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]


# GetDefaultPatchBaselineResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeployablePatchSnapshotForInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.BaselineOverrideTypeDef]


# GetDeployablePatchSnapshotForInstanceResultTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotDownloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Product
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDocumentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]


# GetDocumentResultTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Creating', 'Deleting', 'Failed', 'Updating']
- **Required**: Yes

### StatusInformation
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentType
- **Type**: typing.Literal['ApplicationConfiguration', 'ApplicationConfigurationSchema', 'Automation', 'Automation.ChangeTemplate', 'ChangeCalendar', 'CloudFormation', 'Command', 'ConformancePackTemplate', 'DeploymentStrategy', 'Package', 'Policy', 'ProblemAnalysis', 'ProblemAnalysisTemplate', 'QuickSetup', 'Session']
- **Required**: Yes

### DocumentFormat
- **Type**: typing.Literal['JSON', 'TEXT', 'YAML']
- **Required**: Yes

### Requires
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentRequiresTypeDef]
- **Required**: Yes

### AttachmentsContent
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AttachmentContentTypeDef]
- **Required**: Yes

### ReviewStatus
- **Type**: typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExecutionPreviewRequestTypeDef

### ExecutionPreviewId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExecutionPreviewResponseTypeDef

### ExecutionPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### EndedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Failed', 'InProgress', 'Pending', 'Success']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionPreview
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ExecutionPreviewTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInventoryRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryFilterTypeDef]]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryAggregatorPaginatorTypeDef]]

### ResultAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ResultAttributeTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# GetInventoryRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryFilterTypeDef]]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryAggregatorTypeDef]]

### ResultAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ResultAttributeTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetInventoryResultTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InventoryResultEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInventorySchemaRequestPaginateTypeDef

### TypeName
- **Type**: typing.Optional[str]

### Aggregator
- **Type**: typing.Optional[bool]

### SubType
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# GetInventorySchemaRequestTypeDef

### TypeName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Aggregator
- **Type**: typing.Optional[bool]

### SubType
- **Type**: typing.Optional[bool]


# GetInventorySchemaResultTypeDef

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InventoryItemSchemaTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMaintenanceWindowExecutionRequestTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowExecutionResultTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskIds
- **Type**: typing.List[str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED_OVERLAPPING', 'SUCCESS', 'TIMED_OUT']
- **Required**: Yes

### StatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskInvocationResultTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskType
- **Type**: typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']
- **Required**: Yes

### Parameters
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED_OVERLAPPING', 'SUCCESS', 'TIMED_OUT']
- **Required**: Yes

### StatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OwnerInformation
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskRequestTypeDef

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: <class 'str'>
- **Required**: Yes

### EndDate
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleTimezone
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleOffset
- **Type**: <class 'int'>
- **Required**: Yes

### NextExecutionTime
- **Type**: <class 'str'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Cutoff
- **Type**: <class 'int'>
- **Required**: Yes

### AllowUnassociatedTargets
- **Type**: <class 'bool'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMaintenanceWindowTaskRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowTaskResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskType
- **Type**: typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']
- **Required**: Yes

### TaskParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutputTypeDef]
- **Required**: Yes

### TaskInvocationParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskInvocationParametersOutputTypeDef'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### MaxConcurrency
- **Type**: <class 'str'>
- **Required**: Yes

### MaxErrors
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.LoggingInfoTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CutoffBehavior
- **Type**: typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']
- **Required**: Yes

### AlarmConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOpsItemRequestTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### OpsItemArn
- **Type**: typing.Optional[str]


# GetOpsItemResponseTypeDef

### OpsItem
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.OpsItemTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOpsMetadataRequestTypeDef

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOpsMetadataResultTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.MetadataValueTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOpsSummaryRequestPaginateTypeDef

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsFilterTypeDef]]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsAggregatorPaginatorTypeDef]]

### ResultAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsResultAttributeTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# GetOpsSummaryRequestTypeDef

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsFilterTypeDef]]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsAggregatorTypeDef]]

### ResultAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsResultAttributeTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetOpsSummaryResultTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.OpsEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetParameterHistoryRequestPaginateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# GetParameterHistoryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetParameterHistoryResultTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ParameterHistoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetParameterRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]


# GetParameterResultTypeDef

### Parameter
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ParameterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetParametersByPathRequestPaginateTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Recursive
- **Type**: typing.Optional[bool]

### ParameterFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ParameterStringFilterTypeDef]]

### WithDecryption
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# GetParametersByPathRequestTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Recursive
- **Type**: typing.Optional[bool]

### ParameterFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ParameterStringFilterTypeDef]]

### WithDecryption
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetParametersByPathResultTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetParametersRequestTypeDef

### Names
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]


# GetParametersResultTypeDef

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ParameterTypeDef]
- **Required**: Yes

### InvalidParameters
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPatchBaselineForPatchGroupRequestTypeDef

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]


# GetPatchBaselineForPatchGroupResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPatchBaselineRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPatchBaselineResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### GlobalFilters
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupOutputTypeDef'>
- **Required**: Yes

### ApprovalRules
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.PatchRuleGroupOutputTypeDef'>
- **Required**: Yes

### ApprovedPatches
- **Type**: typing.List[str]
- **Required**: Yes

### ApprovedPatchesComplianceLevel
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']
- **Required**: Yes

### ApprovedPatchesEnableNonSecurity
- **Type**: <class 'bool'>
- **Required**: Yes

### RejectedPatches
- **Type**: typing.List[str]
- **Required**: Yes

### RejectedPatchesAction
- **Type**: typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']
- **Required**: Yes

### PatchGroups
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchSourceOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePoliciesRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# GetResourcePoliciesRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetResourcePoliciesResponseEntryTypeDef

### PolicyId
- **Type**: typing.Optional[str]

### PolicyHash
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]


# GetResourcePoliciesResponseTypeDef

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.GetResourcePoliciesResponseEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetServiceSettingRequestTypeDef

### SettingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceSettingResultTypeDef

### ServiceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ServiceSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceAggregatedAssociationOverviewTypeDef

### DetailedStatus
- **Type**: typing.Optional[str]

### InstanceAssociationStatusAggregatedCount
- **Type**: typing.Optional[typing.Dict[str, int]]


# InstanceAssociationOutputLocationTypeDef

### S3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.S3OutputLocationTypeDef]


# InstanceAssociationOutputUrlTypeDef

### S3OutputUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.S3OutputUrlTypeDef]


# InstanceAssociationStatusInfoTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]

### DetailedStatus
- **Type**: typing.Optional[str]

### ExecutionSummary
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### OutputUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputUrlTypeDef]

### AssociationName
- **Type**: typing.Optional[str]


# InstanceAssociationTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]


# InstanceInfoTypeDef

### AgentType
- **Type**: typing.Optional[str]

### AgentVersion
- **Type**: typing.Optional[str]

### ComputerName
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### ManagedStatus
- **Type**: typing.Optional[typing.Literal['All', 'Managed', 'Unmanaged']]

### PlatformType
- **Type**: typing.Optional[typing.Literal['Linux', 'MacOS', 'Windows']]

### PlatformName
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2Instance', 'ManagedInstance']]


# InstanceInformationFilterTypeDef

### key
- **Type**: typing.Literal['ActivationIds', 'AgentVersion', 'AssociationStatus', 'IamRole', 'InstanceIds', 'PingStatus', 'PlatformTypes', 'ResourceType']
- **Required**: Yes

### valueSet
- **Type**: typing.Sequence[str]
- **Required**: Yes


# InstanceInformationStringFilterTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# InstanceInformationTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### PingStatus
- **Type**: typing.Optional[typing.Literal['ConnectionLost', 'Inactive', 'Online']]

### LastPingDateTime
- **Type**: typing.Optional[datetime.datetime]

### AgentVersion
- **Type**: typing.Optional[str]

### IsLatestVersion
- **Type**: typing.Optional[bool]

### PlatformType
- **Type**: typing.Optional[typing.Literal['Linux', 'MacOS', 'Windows']]

### PlatformName
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### ActivationId
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[str]

### RegistrationDate
- **Type**: typing.Optional[datetime.datetime]

### ResourceType
- **Type**: typing.Optional[typing.Literal['EC2Instance', 'ManagedInstance']]

### Name
- **Type**: typing.Optional[str]

### IPAddress
- **Type**: typing.Optional[str]

### ComputerName
- **Type**: typing.Optional[str]

### AssociationStatus
- **Type**: typing.Optional[str]

### LastAssociationExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulAssociationExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### AssociationOverview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAggregatedAssociationOverviewTypeDef]

### SourceId
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['AWS::EC2::Instance', 'AWS::IoT::Thing', 'AWS::SSM::ManagedInstance']]


# InstancePatchStateFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InstancePatchStateTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### OperationStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OperationEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['Install', 'Scan']
- **Required**: Yes

### SnapshotId
- **Type**: typing.Optional[str]

### InstallOverrideList
- **Type**: typing.Optional[str]

### OwnerInformation
- **Type**: typing.Optional[str]

### InstalledCount
- **Type**: typing.Optional[int]

### InstalledOtherCount
- **Type**: typing.Optional[int]

### InstalledPendingRebootCount
- **Type**: typing.Optional[int]

### InstalledRejectedCount
- **Type**: typing.Optional[int]

### MissingCount
- **Type**: typing.Optional[int]

### FailedCount
- **Type**: typing.Optional[int]

### UnreportedNotApplicableCount
- **Type**: typing.Optional[int]

### NotApplicableCount
- **Type**: typing.Optional[int]

### LastNoRebootInstallOperationTime
- **Type**: typing.Optional[datetime.datetime]

### RebootOption
- **Type**: typing.Optional[typing.Literal['NoReboot', 'RebootIfNeeded']]

### CriticalNonCompliantCount
- **Type**: typing.Optional[int]

### SecurityNonCompliantCount
- **Type**: typing.Optional[int]

### OtherNonCompliantCount
- **Type**: typing.Optional[int]


# InstancePropertyFilterTypeDef

### key
- **Type**: typing.Literal['ActivationIds', 'AgentVersion', 'AssociationStatus', 'DocumentName', 'IamRole', 'InstanceIds', 'PingStatus', 'PlatformTypes', 'ResourceType']
- **Required**: Yes

### valueSet
- **Type**: typing.Sequence[str]
- **Required**: Yes


# InstancePropertyStringFilterTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['BeginWith', 'Equal', 'GreaterThan', 'LessThan', 'NotEqual']]


# InstancePropertyTypeDef

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### InstanceRole
- **Type**: typing.Optional[str]

### KeyName
- **Type**: typing.Optional[str]

### InstanceState
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[str]

### IPAddress
- **Type**: typing.Optional[str]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### PingStatus
- **Type**: typing.Optional[typing.Literal['ConnectionLost', 'Inactive', 'Online']]

### LastPingDateTime
- **Type**: typing.Optional[datetime.datetime]

### AgentVersion
- **Type**: typing.Optional[str]

### PlatformType
- **Type**: typing.Optional[typing.Literal['Linux', 'MacOS', 'Windows']]

### PlatformName
- **Type**: typing.Optional[str]

### PlatformVersion
- **Type**: typing.Optional[str]

### ActivationId
- **Type**: typing.Optional[str]

### IamRole
- **Type**: typing.Optional[str]

### RegistrationDate
- **Type**: typing.Optional[datetime.datetime]

### ResourceType
- **Type**: typing.Optional[str]

### ComputerName
- **Type**: typing.Optional[str]

### AssociationStatus
- **Type**: typing.Optional[str]

### LastAssociationExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulAssociationExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### AssociationOverview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAggregatedAssociationOverviewTypeDef]

### SourceId
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['AWS::EC2::Instance', 'AWS::IoT::Thing', 'AWS::SSM::ManagedInstance']]


# InventoryAggregatorPaginatorTypeDef

### Expression
- **Type**: typing.Optional[str]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### Groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryGroupTypeDef]]


# InventoryAggregatorTypeDef

### Expression
- **Type**: typing.Optional[str]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### Groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryGroupTypeDef]]


# InventoryDeletionStatusItemTypeDef

### DeletionId
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### DeletionStartTime
- **Type**: typing.Optional[datetime.datetime]

### LastStatus
- **Type**: typing.Optional[typing.Literal['Complete', 'InProgress']]

### LastStatusMessage
- **Type**: typing.Optional[str]

### DeletionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InventoryDeletionSummaryTypeDef]

### LastStatusUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# InventoryDeletionSummaryItemTypeDef

### Version
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]

### RemainingCount
- **Type**: typing.Optional[int]


# InventoryDeletionSummaryTypeDef

### TotalCount
- **Type**: typing.Optional[int]

### RemainingCount
- **Type**: typing.Optional[int]

### SummaryItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.InventoryDeletionSummaryItemTypeDef]]


# InventoryFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InventoryGroupTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryFilterTypeDef]
- **Required**: Yes


# InventoryItemAttributeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataType
- **Type**: typing.Literal['number', 'string']
- **Required**: Yes


# InventoryItemSchemaTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.InventoryItemAttributeTypeDef]
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# InventoryItemTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureTime
- **Type**: <class 'str'>
- **Required**: Yes

### ContentHash
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]

### Context
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InventoryResultEntityTypeDef

### Id
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.InventoryResultItemTypeDef]]


# InventoryResultItemTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### CaptureTime
- **Type**: typing.Optional[str]

### ContentHash
- **Type**: typing.Optional[str]


# LabelParameterVersionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Labels
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ParameterVersion
- **Type**: typing.Optional[int]


# LabelParameterVersionResultTypeDef

### InvalidLabels
- **Type**: typing.List[str]
- **Required**: Yes

### ParameterVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociationVersionsRequestPaginateTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListAssociationVersionsRequestTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationVersionsResultTypeDef

### AssociationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AssociationVersionInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsRequestPaginateTypeDef

### AssociationFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AssociationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListAssociationsRequestTypeDef

### AssociationFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AssociationFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.AssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCommandInvocationsRequestPaginateTypeDef

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.CommandFilterTypeDef]]

### Details
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListCommandInvocationsRequestTypeDef

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.CommandFilterTypeDef]]

### Details
- **Type**: typing.Optional[bool]


# ListCommandInvocationsResultTypeDef

### CommandInvocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.CommandInvocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCommandsRequestPaginateTypeDef

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.CommandFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListCommandsRequestTypeDef

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.CommandFilterTypeDef]]


# ListCommandsResultTypeDef

### Commands
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.CommandTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComplianceItemsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceStringFilterTypeDef]]

### ResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListComplianceItemsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceStringFilterTypeDef]]

### ResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComplianceItemsResultTypeDef

### ComplianceItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ComplianceItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComplianceSummariesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceStringFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListComplianceSummariesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceStringFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComplianceSummariesResultTypeDef

### ComplianceSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ComplianceSummaryItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentMetadataHistoryRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Literal['DocumentReviews']
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentMetadataHistoryResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Author
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.DocumentMetadataResponseInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentVersionsRequestPaginateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListDocumentVersionsRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentVersionsResultTypeDef

### DocumentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentVersionInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentsRequestPaginateTypeDef

### DocumentFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DocumentFilterTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DocumentKeyValuesFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListDocumentsRequestTypeDef

### DocumentFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DocumentFilterTypeDef]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.DocumentKeyValuesFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentsResultTypeDef

### DocumentIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.DocumentIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInventoryEntriesRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInventoryEntriesResultTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureTime
- **Type**: <class 'str'>
- **Required**: Yes

### Entries
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequestPaginateTypeDef

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.NodeFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListNodesRequestTypeDef

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.NodeFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNodesResultTypeDef

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.NodeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesSummaryRequestPaginateTypeDef

### Aggregators
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.NodeAggregatorPaginatorTypeDef]
- **Required**: Yes

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.NodeFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListNodesSummaryRequestTypeDef

### Aggregators
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.NodeAggregatorTypeDef]
- **Required**: Yes

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.NodeFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNodesSummaryResultTypeDef

### Summary
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemEventsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemEventFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListOpsItemEventsRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemEventFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemEventsResponseTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.OpsItemEventSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemRelatedItemsRequestPaginateTypeDef

### OpsItemId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemRelatedItemsFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListOpsItemRelatedItemsRequestTypeDef

### OpsItemId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemRelatedItemsFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemRelatedItemsResponseTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.OpsItemRelatedItemSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpsMetadataRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsMetadataFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListOpsMetadataRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsMetadataFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOpsMetadataResultTypeDef

### OpsMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.OpsMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceComplianceSummariesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceStringFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListResourceComplianceSummariesRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceStringFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceComplianceSummariesResultTypeDef

### ResourceComplianceSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ResourceComplianceSummaryItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDataSyncRequestPaginateTypeDef

### SyncType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PaginatorConfigTypeDef]


# ListResourceDataSyncRequestTypeDef

### SyncType
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceDataSyncResultTypeDef

### ResourceDataSyncItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceType
- **Type**: typing.Literal['Association', 'Automation', 'Document', 'MaintenanceWindow', 'ManagedInstance', 'OpsItem', 'OpsMetadata', 'Parameter', 'PatchBaseline']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingInfoTypeDef

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]


# MaintenanceWindowAutomationParametersOutputTypeDef

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# MaintenanceWindowAutomationParametersTypeDef

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# MaintenanceWindowExecutionTaskIdentityTypeDef

### WindowExecutionId
- **Type**: typing.Optional[str]

### TaskExecutionId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED_OVERLAPPING', 'SUCCESS', 'TIMED_OUT']]

### StatusDetails
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### TaskArn
- **Type**: typing.Optional[str]

### TaskType
- **Type**: typing.Optional[typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]


# MaintenanceWindowExecutionTaskInvocationIdentityTypeDef

### WindowExecutionId
- **Type**: typing.Optional[str]

### TaskExecutionId
- **Type**: typing.Optional[str]

### InvocationId
- **Type**: typing.Optional[str]

### ExecutionId
- **Type**: typing.Optional[str]

### TaskType
- **Type**: typing.Optional[typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']]

### Parameters
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED_OVERLAPPING', 'SUCCESS', 'TIMED_OUT']]

### StatusDetails
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### OwnerInformation
- **Type**: typing.Optional[str]

### WindowTargetId
- **Type**: typing.Optional[str]


# MaintenanceWindowExecutionTypeDef

### WindowId
- **Type**: typing.Optional[str]

### WindowExecutionId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'SKIPPED_OVERLAPPING', 'SUCCESS', 'TIMED_OUT']]

### StatusDetails
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# MaintenanceWindowFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# MaintenanceWindowIdentityForTargetTypeDef

### WindowId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MaintenanceWindowIdentityTypeDef

### WindowId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### Duration
- **Type**: typing.Optional[int]

### Cutoff
- **Type**: typing.Optional[int]

### Schedule
- **Type**: typing.Optional[str]

### ScheduleTimezone
- **Type**: typing.Optional[str]

### ScheduleOffset
- **Type**: typing.Optional[int]

### EndDate
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[str]

### NextExecutionTime
- **Type**: typing.Optional[str]


# MaintenanceWindowLambdaParametersOutputTypeDef

### ClientContext
- **Type**: typing.Optional[str]

### Qualifier
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Optional[bytes]


# MaintenanceWindowLambdaParametersTypeDef

### ClientContext
- **Type**: typing.Optional[str]

### Qualifier
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.BlobTypeDef]


# MaintenanceWindowRunCommandParametersOutputTypeDef

### Comment
- **Type**: typing.Optional[str]

### CloudWatchOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CloudWatchOutputConfigTypeDef]

### DocumentHash
- **Type**: typing.Optional[str]

### DocumentHashType
- **Type**: typing.Optional[typing.Literal['Sha1', 'Sha256']]

### DocumentVersion
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NotificationConfigOutputTypeDef]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### TimeoutSeconds
- **Type**: typing.Optional[int]


# MaintenanceWindowRunCommandParametersTypeDef

### Comment
- **Type**: typing.Optional[str]

### CloudWatchOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CloudWatchOutputConfigTypeDef]

### DocumentHash
- **Type**: typing.Optional[str]

### DocumentHashType
- **Type**: typing.Optional[typing.Literal['Sha1', 'Sha256']]

### DocumentVersion
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NotificationConfigTypeDef]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### TimeoutSeconds
- **Type**: typing.Optional[int]


# MaintenanceWindowStepFunctionsParametersTypeDef

### Input
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MaintenanceWindowTargetTypeDef

### WindowId
- **Type**: typing.Optional[str]

### WindowTargetId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'RESOURCE_GROUP']]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### OwnerInformation
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# MaintenanceWindowTaskInvocationParametersOutputTypeDef

### RunCommand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowRunCommandParametersOutputTypeDef]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowAutomationParametersOutputTypeDef]

### StepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowStepFunctionsParametersTypeDef]

### Lambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowLambdaParametersOutputTypeDef]


# MaintenanceWindowTaskInvocationParametersTypeDef

### RunCommand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowRunCommandParametersTypeDef]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowAutomationParametersTypeDef]

### StepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowStepFunctionsParametersTypeDef]

### Lambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowLambdaParametersTypeDef]


# MaintenanceWindowTaskInvocationParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MaintenanceWindowTaskParameterValueExpressionOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# MaintenanceWindowTaskParameterValueExpressionTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# MaintenanceWindowTaskParameterValueExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MaintenanceWindowTaskTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataValueTypeDef

### Value
- **Type**: typing.Optional[str]


# ModifyDocumentPermissionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionType
- **Type**: typing.Literal['Share']
- **Required**: Yes

### AccountIdsToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### AccountIdsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### SharedDocumentVersion
- **Type**: typing.Optional[str]


# NodeAggregatorPaginatorTypeDef

### AggregatorType
- **Type**: typing.Literal['Count']
- **Required**: Yes

### TypeName
- **Type**: typing.Literal['Instance']
- **Required**: Yes

### AttributeName
- **Type**: typing.Literal['AgentVersion', 'PlatformName', 'PlatformType', 'PlatformVersion', 'Region', 'ResourceType']
- **Required**: Yes

### Aggregators
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# NodeAggregatorTypeDef

### AggregatorType
- **Type**: typing.Literal['Count']
- **Required**: Yes

### TypeName
- **Type**: typing.Literal['Instance']
- **Required**: Yes

### AttributeName
- **Type**: typing.Literal['AgentVersion', 'PlatformName', 'PlatformType', 'PlatformVersion', 'Region', 'ResourceType']
- **Required**: Yes

### Aggregators
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# NodeFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NodeOwnerInfoTypeDef

### AccountId
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### OrganizationalUnitPath
- **Type**: typing.Optional[str]


# NodeTypeDef

### CaptureTime
- **Type**: typing.Optional[datetime.datetime]

### Id
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NodeOwnerInfoTypeDef]

### Region
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NodeTypeTypeDef]


# NodeTypeTypeDef

### Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceInfoTypeDef]


# NonCompliantSummaryTypeDef

### NonCompliantCount
- **Type**: typing.Optional[int]

### SeveritySummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.SeveritySummaryTypeDef]


# NotificationConfigOutputTypeDef

### NotificationArn
- **Type**: typing.Optional[str]

### NotificationEvents
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'Cancelled', 'Failed', 'InProgress', 'Success', 'TimedOut']]]

### NotificationType
- **Type**: typing.Optional[typing.Literal['Command', 'Invocation']]


# NotificationConfigTypeDef

### NotificationArn
- **Type**: typing.Optional[str]

### NotificationEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'Cancelled', 'Failed', 'InProgress', 'Success', 'TimedOut']]]

### NotificationType
- **Type**: typing.Optional[typing.Literal['Command', 'Invocation']]


# NotificationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OpsAggregatorPaginatorTypeDef

### AggregatorType
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### AttributeName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsFilterTypeDef]]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# OpsAggregatorTypeDef

### AggregatorType
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### AttributeName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsFilterTypeDef]]

### Aggregators
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# OpsEntityItemTypeDef

### CaptureTime
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# OpsEntityTypeDef

### Id
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.OpsEntityItemTypeDef]]


# OpsFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OpsItemDataValueTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OpsItemEventFilterTypeDef

### Key
- **Type**: typing.Literal['OpsItemId']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Equal']
- **Required**: Yes


# OpsItemEventSummaryTypeDef

### OpsItemId
- **Type**: typing.Optional[str]

### EventId
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### DetailType
- **Type**: typing.Optional[str]

### Detail
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.OpsItemIdentityTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# OpsItemFilterTypeDef

### Key
- **Type**: typing.Literal['AccountId', 'ActualEndTime', 'ActualStartTime', 'AutomationId', 'Category', 'ChangeRequestByApproverArn', 'ChangeRequestByApproverName', 'ChangeRequestByRequesterArn', 'ChangeRequestByRequesterName', 'ChangeRequestByTargetsResourceGroup', 'ChangeRequestByTemplate', 'CreatedBy', 'CreatedTime', 'InsightByType', 'LastModifiedTime', 'OperationalData', 'OperationalDataKey', 'OperationalDataValue', 'OpsItemId', 'OpsItemType', 'PlannedEndTime', 'PlannedStartTime', 'Priority', 'ResourceId', 'Severity', 'Source', 'Status', 'Title']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Contains', 'Equal', 'GreaterThan', 'LessThan']
- **Required**: Yes


# OpsItemIdentityTypeDef

### Arn
- **Type**: typing.Optional[str]


# OpsItemNotificationTypeDef

### Arn
- **Type**: typing.Optional[str]


# OpsItemRelatedItemSummaryTypeDef

### OpsItemId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[str]

### ResourceUri
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.OpsItemIdentityTypeDef]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.OpsItemIdentityTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# OpsItemRelatedItemsFilterTypeDef

### Key
- **Type**: typing.Literal['AssociationId', 'ResourceType', 'ResourceUri']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Equal']
- **Required**: Yes


# OpsItemSummaryTypeDef

### CreatedBy
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Priority
- **Type**: typing.Optional[int]

### Source
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'Closed', 'CompletedWithFailure', 'CompletedWithSuccess', 'Failed', 'InProgress', 'Open', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'Resolved', 'RunbookInProgress', 'Scheduled', 'TimedOut']]

### OpsItemId
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### OperationalData
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.OpsItemDataValueTypeDef]]

### Category
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### OpsItemType
- **Type**: typing.Optional[str]

### ActualStartTime
- **Type**: typing.Optional[datetime.datetime]

### ActualEndTime
- **Type**: typing.Optional[datetime.datetime]

### PlannedStartTime
- **Type**: typing.Optional[datetime.datetime]

### PlannedEndTime
- **Type**: typing.Optional[datetime.datetime]


# OpsItemTypeDef

### CreatedBy
- **Type**: typing.Optional[str]

### OpsItemType
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### LastModifiedBy
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Notifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.OpsItemNotificationTypeDef]]

### Priority
- **Type**: typing.Optional[int]

### RelatedOpsItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.RelatedOpsItemTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'Closed', 'CompletedWithFailure', 'CompletedWithSuccess', 'Failed', 'InProgress', 'Open', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'Resolved', 'RunbookInProgress', 'Scheduled', 'TimedOut']]

### OpsItemId
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### OperationalData
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.OpsItemDataValueTypeDef]]

### Category
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ActualStartTime
- **Type**: typing.Optional[datetime.datetime]

### ActualEndTime
- **Type**: typing.Optional[datetime.datetime]

### PlannedStartTime
- **Type**: typing.Optional[datetime.datetime]

### PlannedEndTime
- **Type**: typing.Optional[datetime.datetime]

### OpsItemArn
- **Type**: typing.Optional[str]


# OpsMetadataFilterTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OpsMetadataTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### OpsMetadataArn
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedUser
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# OpsResultAttributeTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes


# OutputSourceTypeDef

### OutputSourceId
- **Type**: typing.Optional[str]

### OutputSourceType
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterHistoryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterInlinePolicyTypeDef

### PolicyText
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[str]

### PolicyStatus
- **Type**: typing.Optional[str]


# ParameterMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterStringFilterTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Option
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# ParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParametersFilterTypeDef

### Key
- **Type**: typing.Literal['KeyId', 'Name', 'Type']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ParentStepDetailsTypeDef

### StepExecutionId
- **Type**: typing.Optional[str]

### StepName
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### Iteration
- **Type**: typing.Optional[int]

### IteratorValue
- **Type**: typing.Optional[str]


# PatchBaselineIdentityTypeDef

### BaselineId
- **Type**: typing.Optional[str]

### BaselineName
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]

### BaselineDescription
- **Type**: typing.Optional[str]

### DefaultBaseline
- **Type**: typing.Optional[bool]


# PatchComplianceDataTypeDef

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### KBId
- **Type**: <class 'str'>
- **Required**: Yes

### Classification
- **Type**: <class 'str'>
- **Required**: Yes

### Severity
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['FAILED', 'INSTALLED', 'INSTALLED_OTHER', 'INSTALLED_PENDING_REBOOT', 'INSTALLED_REJECTED', 'MISSING', 'NOT_APPLICABLE']
- **Required**: Yes

### InstalledTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CVEIds
- **Type**: typing.Optional[str]


# PatchFilterGroupOutputTypeDef

### PatchFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchFilterOutputTypeDef]
- **Required**: Yes


# PatchFilterGroupTypeDef

### PatchFilters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchFilterUnionTypeDef]
- **Required**: Yes


# PatchFilterGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PatchFilterOutputTypeDef

### Key
- **Type**: typing.Literal['ADVISORY_ID', 'ARCH', 'BUGZILLA_ID', 'CLASSIFICATION', 'CVE_ID', 'EPOCH', 'MSRC_SEVERITY', 'NAME', 'PATCH_ID', 'PATCH_SET', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'RELEASE', 'REPOSITORY', 'SECTION', 'SECURITY', 'SEVERITY', 'VERSION']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PatchFilterTypeDef

### Key
- **Type**: typing.Literal['ADVISORY_ID', 'ARCH', 'BUGZILLA_ID', 'CLASSIFICATION', 'CVE_ID', 'EPOCH', 'MSRC_SEVERITY', 'NAME', 'PATCH_ID', 'PATCH_SET', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'RELEASE', 'REPOSITORY', 'SECTION', 'SECURITY', 'SEVERITY', 'VERSION']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PatchFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PatchGroupPatchBaselineMappingTypeDef

### PatchGroup
- **Type**: typing.Optional[str]

### BaselineIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchBaselineIdentityTypeDef]


# PatchOrchestratorFilterTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# PatchRuleGroupOutputTypeDef

### PatchRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchRuleOutputTypeDef]
- **Required**: Yes


# PatchRuleGroupTypeDef

### PatchRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchRuleUnionTypeDef]
- **Required**: Yes


# PatchRuleGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PatchRuleOutputTypeDef

### PatchFilterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupOutputTypeDef'>
- **Required**: Yes

### ComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApproveAfterDays
- **Type**: typing.Optional[int]

### ApproveUntilDate
- **Type**: typing.Optional[str]

### EnableNonSecurity
- **Type**: typing.Optional[bool]


# PatchRuleTypeDef

### PatchFilterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupUnionTypeDef'>
- **Required**: Yes

### ComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApproveAfterDays
- **Type**: typing.Optional[int]

### ApproveUntilDate
- **Type**: typing.Optional[str]

### EnableNonSecurity
- **Type**: typing.Optional[bool]


# PatchRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PatchSourceOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Products
- **Type**: typing.List[str]
- **Required**: Yes

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes


# PatchSourceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Products
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes


# PatchSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PatchStatusTypeDef

### DeploymentStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'EXPLICIT_APPROVED', 'EXPLICIT_REJECTED', 'PENDING_APPROVAL']]

### ComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApprovalDate
- **Type**: typing.Optional[datetime.datetime]


# PatchTypeDef

### Id
- **Type**: typing.Optional[str]

### ReleaseDate
- **Type**: typing.Optional[datetime.datetime]

### Title
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ContentUrl
- **Type**: typing.Optional[str]

### Vendor
- **Type**: typing.Optional[str]

### ProductFamily
- **Type**: typing.Optional[str]

### Product
- **Type**: typing.Optional[str]

### Classification
- **Type**: typing.Optional[str]

### MsrcSeverity
- **Type**: typing.Optional[str]

### KbNumber
- **Type**: typing.Optional[str]

### MsrcNumber
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### AdvisoryIds
- **Type**: typing.Optional[typing.List[str]]

### BugzillaIds
- **Type**: typing.Optional[typing.List[str]]

### CVEIds
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]

### Epoch
- **Type**: typing.Optional[int]

### Version
- **Type**: typing.Optional[str]

### Release
- **Type**: typing.Optional[str]

### Arch
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### Repository
- **Type**: typing.Optional[str]


# ProgressCountersTypeDef

### TotalSteps
- **Type**: typing.Optional[int]

### SuccessSteps
- **Type**: typing.Optional[int]

### FailedSteps
- **Type**: typing.Optional[int]

### CancelledSteps
- **Type**: typing.Optional[int]

### TimedOutSteps
- **Type**: typing.Optional[int]


# PutComplianceItemsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceType
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ComplianceExecutionSummaryUnionTypeDef'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ComplianceItemEntryTypeDef]
- **Required**: Yes

### ItemContentHash
- **Type**: typing.Optional[str]

### UploadType
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'PARTIAL']]


# PutInventoryRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.InventoryItemTypeDef]
- **Required**: Yes


# PutInventoryResultTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutParameterResultTypeDef

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### Tier
- **Type**: typing.Literal['Advanced', 'Intelligent-Tiering', 'Standard']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyId
- **Type**: typing.Optional[str]

### PolicyHash
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterDefaultPatchBaselineRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterDefaultPatchBaselineResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterPatchBaselineForPatchGroupRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterPatchBaselineForPatchGroupResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterTargetWithMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['INSTANCE', 'RESOURCE_GROUP']
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]
- **Required**: Yes

### OwnerInformation
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# RegisterTargetWithMaintenanceWindowResultTypeDef

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterTaskWithMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskType
- **Type**: typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### TaskParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskParameterValueExpressionUnionTypeDef]]

### TaskInvocationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskInvocationParametersUnionTypeDef]

### Priority
- **Type**: typing.Optional[int]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.LoggingInfoTypeDef]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### CutoffBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]


# RegisterTaskWithMaintenanceWindowResultTypeDef

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistrationMetadataItemTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# RelatedOpsItemTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsFromResourceRequestTypeDef

### ResourceType
- **Type**: typing.Literal['Association', 'Automation', 'Document', 'MaintenanceWindow', 'ManagedInstance', 'OpsItem', 'OpsMetadata', 'Parameter', 'PatchBaseline']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetServiceSettingRequestTypeDef

### SettingId
- **Type**: <class 'str'>
- **Required**: Yes


# ResetServiceSettingResultTypeDef

### ServiceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ServiceSettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResolvedTargetsTypeDef

### ParameterValues
- **Type**: typing.Optional[typing.List[str]]

### Truncated
- **Type**: typing.Optional[bool]


# ResourceComplianceSummaryItemTypeDef

### ComplianceType
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'NON_COMPLIANT']]

### OverallSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ComplianceExecutionSummaryOutputTypeDef]

### CompliantSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CompliantSummaryTypeDef]

### NonCompliantSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NonCompliantSummaryTypeDef]


# ResourceDataSyncAwsOrganizationsSourceOutputTypeDef

### OrganizationSourceType
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncOrganizationalUnitTypeDef]]


# ResourceDataSyncAwsOrganizationsSourceTypeDef

### OrganizationSourceType
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncOrganizationalUnitTypeDef]]


# ResourceDataSyncAwsOrganizationsSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceDataSyncDestinationDataSharingTypeDef

### DestinationDataSharingType
- **Type**: typing.Optional[str]


# ResourceDataSyncItemTypeDef

### SyncName
- **Type**: typing.Optional[str]

### SyncType
- **Type**: typing.Optional[str]

### SyncSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncSourceWithStateTypeDef]

### S3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncS3DestinationTypeDef]

### LastSyncTime
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulSyncTime
- **Type**: typing.Optional[datetime.datetime]

### SyncLastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Successful']]

### SyncCreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastSyncStatusMessage
- **Type**: typing.Optional[str]


# ResourceDataSyncOrganizationalUnitTypeDef

### OrganizationalUnitId
- **Type**: typing.Optional[str]


# ResourceDataSyncS3DestinationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncFormat
- **Type**: typing.Literal['JsonSerDe']
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### AWSKMSKeyARN
- **Type**: typing.Optional[str]

### DestinationDataSharing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncDestinationDataSharingTypeDef]


# ResourceDataSyncSourceTypeDef

### SourceType
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRegions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AwsOrganizationsSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncAwsOrganizationsSourceUnionTypeDef]

### IncludeFutureRegions
- **Type**: typing.Optional[bool]

### EnableAllOpsDataSources
- **Type**: typing.Optional[bool]


# ResourceDataSyncSourceWithStateTypeDef

### SourceType
- **Type**: typing.Optional[str]

### AwsOrganizationsSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncAwsOrganizationsSourceOutputTypeDef]

### SourceRegions
- **Type**: typing.Optional[typing.List[str]]

### IncludeFutureRegions
- **Type**: typing.Optional[bool]

### State
- **Type**: typing.Optional[str]

### EnableAllOpsDataSources
- **Type**: typing.Optional[bool]


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


# ResultAttributeTypeDef

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeSessionRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeSessionResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### TokenValue
- **Type**: <class 'str'>
- **Required**: Yes

### StreamUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReviewInformationTypeDef

### ReviewedTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Reviewer
- **Type**: typing.Optional[str]


# RunbookOutputTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationOutputTypeDef]]


# RunbookTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### TargetMaps
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Sequence[str]]]]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationUnionTypeDef]]


# RunbookUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3OutputLocationTypeDef

### OutputS3Region
- **Type**: typing.Optional[str]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]


# S3OutputUrlTypeDef

### OutputUrl
- **Type**: typing.Optional[str]


# ScheduledWindowExecutionTypeDef

### WindowId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ExecutionTime
- **Type**: typing.Optional[str]


# SendAutomationSignalRequestTypeDef

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### SignalType
- **Type**: typing.Literal['Approve', 'Reject', 'Resume', 'StartStep', 'StopStep']
- **Required**: Yes

### Payload
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# SendCommandRequestTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### DocumentVersion
- **Type**: typing.Optional[str]

### DocumentHash
- **Type**: typing.Optional[str]

### DocumentHashType
- **Type**: typing.Optional[typing.Literal['Sha1', 'Sha256']]

### TimeoutSeconds
- **Type**: typing.Optional[int]

### Comment
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### OutputS3Region
- **Type**: typing.Optional[str]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.NotificationConfigUnionTypeDef]

### CloudWatchOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.CloudWatchOutputConfigTypeDef]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]


# SendCommandResultTypeDef

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.CommandTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceSettingTypeDef

### SettingId
- **Type**: typing.Optional[str]

### SettingValue
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedUser
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# SessionFilterTypeDef

### key
- **Type**: typing.Literal['InvokedAfter', 'InvokedBefore', 'Owner', 'SessionId', 'Status', 'Target']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SessionManagerOutputUrlTypeDef

### S3OutputUrl
- **Type**: typing.Optional[str]

### CloudWatchOutputUrl
- **Type**: typing.Optional[str]


# SessionTypeDef

### SessionId
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Connected', 'Connecting', 'Disconnected', 'Failed', 'Terminated', 'Terminating']]

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### EndDate
- **Type**: typing.Optional[datetime.datetime]

### DocumentName
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[str]

### OutputUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.SessionManagerOutputUrlTypeDef]

### MaxSessionDuration
- **Type**: typing.Optional[str]


# SeveritySummaryTypeDef

### CriticalCount
- **Type**: typing.Optional[int]

### HighCount
- **Type**: typing.Optional[int]

### MediumCount
- **Type**: typing.Optional[int]

### LowCount
- **Type**: typing.Optional[int]

### InformationalCount
- **Type**: typing.Optional[int]

### UnspecifiedCount
- **Type**: typing.Optional[int]


# StartAssociationsOnceRequestTypeDef

### AssociationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StartAutomationExecutionRequestTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ClientToken
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['Auto', 'Interactive']]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### TargetMaps
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Sequence[str]]]]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]

### TargetLocationsURL
- **Type**: typing.Optional[str]


# StartAutomationExecutionResultTypeDef

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartChangeRequestExecutionRequestTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### Runbooks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.RunbookUnionTypeDef]
- **Required**: Yes

### ScheduledTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### ChangeRequestName
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### AutoApprove
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TagTypeDef]]

### ScheduledEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### ChangeDetails
- **Type**: typing.Optional[str]


# StartChangeRequestExecutionResultTypeDef

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExecutionPreviewRequestTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### ExecutionInputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ExecutionInputsTypeDef]


# StartExecutionPreviewResponseTypeDef

### ExecutionPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSessionRequestTypeDef

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentName
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# StartSessionResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### TokenValue
- **Type**: <class 'str'>
- **Required**: Yes

### StreamUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StepExecutionFilterTypeDef

### Key
- **Type**: typing.Literal['Action', 'ParentStepExecutionId', 'ParentStepIteration', 'ParentStepIteratorValue', 'StartTimeAfter', 'StartTimeBefore', 'StepExecutionId', 'StepExecutionStatus', 'StepName']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StepExecutionTypeDef

### StepName
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[str]

### TimeoutSeconds
- **Type**: typing.Optional[int]

### OnFailure
- **Type**: typing.Optional[str]

### MaxAttempts
- **Type**: typing.Optional[int]

### ExecutionStartTime
- **Type**: typing.Optional[datetime.datetime]

### ExecutionEndTime
- **Type**: typing.Optional[datetime.datetime]

### StepStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'CompletedWithFailure', 'CompletedWithSuccess', 'Exited', 'Failed', 'InProgress', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'RunbookInProgress', 'Scheduled', 'Success', 'TimedOut', 'Waiting']]

### ResponseCode
- **Type**: typing.Optional[str]

### Inputs
- **Type**: typing.Optional[typing.Dict[str, str]]

### Outputs
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Response
- **Type**: typing.Optional[str]

### FailureMessage
- **Type**: typing.Optional[str]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.FailureDetailsTypeDef]

### StepExecutionId
- **Type**: typing.Optional[str]

### OverriddenParameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### IsEnd
- **Type**: typing.Optional[bool]

### NextStep
- **Type**: typing.Optional[str]

### IsCritical
- **Type**: typing.Optional[bool]

### ValidNextSteps
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### TargetLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationOutputTypeDef]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.AlarmStateInformationTypeDef]]

### ParentStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.ParentStepDetailsTypeDef]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetLocationOutputTypeDef

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]

### TargetLocationMaxConcurrency
- **Type**: typing.Optional[str]

### TargetLocationMaxErrors
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### TargetLocationAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef]

### IncludeChildOrganizationUnits
- **Type**: typing.Optional[bool]

### ExcludeAccounts
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]]

### TargetsMaxConcurrency
- **Type**: typing.Optional[str]

### TargetsMaxErrors
- **Type**: typing.Optional[str]


# TargetLocationTypeDef

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetLocationMaxConcurrency
- **Type**: typing.Optional[str]

### TargetLocationMaxErrors
- **Type**: typing.Optional[str]

### ExecutionRoleName
- **Type**: typing.Optional[str]

### TargetLocationAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]

### IncludeChildOrganizationUnits
- **Type**: typing.Optional[bool]

### ExcludeAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### TargetsMaxConcurrency
- **Type**: typing.Optional[str]

### TargetsMaxErrors
- **Type**: typing.Optional[str]


# TargetLocationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TargetPreviewTypeDef

### Count
- **Type**: typing.Optional[int]

### TargetType
- **Type**: typing.Optional[str]


# TargetTypeDef

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# TargetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TerminateSessionRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateSessionResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnlabelParameterVersionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Labels
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnlabelParameterVersionResultTypeDef

### RemovedLabels
- **Type**: typing.List[str]
- **Required**: Yes

### InvalidLabels
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssociationRequestTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### DocumentVersion
- **Type**: typing.Optional[str]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.InstanceAssociationOutputLocationTypeDef]

### Name
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### AssociationName
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]

### AutomationTargetParameterName
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### ComplianceSeverity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### SyncCompliance
- **Type**: typing.Optional[typing.Literal['AUTO', 'MANUAL']]

### ApplyOnlyAtCronInterval
- **Type**: typing.Optional[bool]

### CalendarNames
- **Type**: typing.Optional[typing.Sequence[str]]

### TargetLocations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetLocationUnionTypeDef]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Sequence[str]]]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]


# UpdateAssociationResultTypeDef

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AssociationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssociationStatusRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AssociationStatusUnionTypeDef'>
- **Required**: Yes


# UpdateAssociationStatusResultTypeDef

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AssociationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDocumentDefaultVersionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDocumentDefaultVersionResultTypeDef

### Description
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.DocumentDefaultVersionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDocumentMetadataRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentReviews
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.DocumentReviewsTypeDef'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]


# UpdateDocumentRequestTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.AttachmentsSourceTypeDef]]

### DisplayName
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]

### TargetType
- **Type**: typing.Optional[str]


# UpdateDocumentResultTypeDef

### DocumentDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.DocumentDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMaintenanceWindowRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### StartDate
- **Type**: typing.Optional[str]

### EndDate
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### ScheduleTimezone
- **Type**: typing.Optional[str]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### Cutoff
- **Type**: typing.Optional[int]

### AllowUnassociatedTargets
- **Type**: typing.Optional[bool]

### Enabled
- **Type**: typing.Optional[bool]

### Replace
- **Type**: typing.Optional[bool]


# UpdateMaintenanceWindowResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: <class 'str'>
- **Required**: Yes

### EndDate
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleTimezone
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleOffset
- **Type**: <class 'int'>
- **Required**: Yes

### Duration
- **Type**: <class 'int'>
- **Required**: Yes

### Cutoff
- **Type**: <class 'int'>
- **Required**: Yes

### AllowUnassociatedTargets
- **Type**: <class 'bool'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMaintenanceWindowTargetRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### OwnerInformation
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Replace
- **Type**: typing.Optional[bool]


# UpdateMaintenanceWindowTargetResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]
- **Required**: Yes

### OwnerInformation
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMaintenanceWindowTaskRequestTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.TargetUnionTypeDef]]

### TaskArn
- **Type**: typing.Optional[str]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### TaskParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskParameterValueExpressionUnionTypeDef]]

### TaskInvocationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskInvocationParametersUnionTypeDef]

### Priority
- **Type**: typing.Optional[int]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.LoggingInfoTypeDef]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Replace
- **Type**: typing.Optional[bool]

### CutoffBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationUnionTypeDef]


# UpdateMaintenanceWindowTaskResultTypeDef

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.TargetOutputTypeDef]
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutputTypeDef]
- **Required**: Yes

### TaskInvocationParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.MaintenanceWindowTaskInvocationParametersOutputTypeDef'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### MaxConcurrency
- **Type**: <class 'str'>
- **Required**: Yes

### MaxErrors
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.LoggingInfoTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CutoffBehavior
- **Type**: typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']
- **Required**: Yes

### AlarmConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.AlarmConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateManagedInstanceRoleRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IamRole
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOpsItemRequestTypeDef

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OperationalData
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_classes.OpsItemDataValueTypeDef]]

### OperationalDataToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### Notifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.OpsItemNotificationTypeDef]]

### Priority
- **Type**: typing.Optional[int]

### RelatedOpsItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.RelatedOpsItemTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'Closed', 'CompletedWithFailure', 'CompletedWithSuccess', 'Failed', 'InProgress', 'Open', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'Resolved', 'RunbookInProgress', 'Scheduled', 'TimedOut']]

### Title
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ActualStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### ActualEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### PlannedStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### PlannedEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.TimestampTypeDef]

### OpsItemArn
- **Type**: typing.Optional[str]


# UpdateOpsMetadataRequestTypeDef

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetadataToUpdate
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.ssm_classes.MetadataValueTypeDef]]

### KeysToDelete
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateOpsMetadataResultTypeDef

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePatchBaselineRequestTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### GlobalFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupUnionTypeDef]

### ApprovalRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_classes.PatchRuleGroupUnionTypeDef]

### ApprovedPatches
- **Type**: typing.Optional[typing.Sequence[str]]

### ApprovedPatchesComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApprovedPatchesEnableNonSecurity
- **Type**: typing.Optional[bool]

### RejectedPatches
- **Type**: typing.Optional[typing.Sequence[str]]

### RejectedPatchesAction
- **Type**: typing.Optional[typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']]

### Description
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ssm_classes.PatchSourceUnionTypeDef]]

### Replace
- **Type**: typing.Optional[bool]


# UpdatePatchBaselineResultTypeDef

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### GlobalFilters
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.PatchFilterGroupOutputTypeDef'>
- **Required**: Yes

### ApprovalRules
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.PatchRuleGroupOutputTypeDef'>
- **Required**: Yes

### ApprovedPatches
- **Type**: typing.List[str]
- **Required**: Yes

### ApprovedPatchesComplianceLevel
- **Type**: typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']
- **Required**: Yes

### ApprovedPatchesEnableNonSecurity
- **Type**: <class 'bool'>
- **Required**: Yes

### RejectedPatches
- **Type**: typing.List[str]
- **Required**: Yes

### RejectedPatchesAction
- **Type**: typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_classes.PatchSourceOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResourceDataSyncRequestTypeDef

### SyncName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: <class 'str'>
- **Required**: Yes

### SyncSource
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_classes.ResourceDataSyncSourceTypeDef'>
- **Required**: Yes


# UpdateServiceSettingRequestTypeDef

### SettingId
- **Type**: <class 'str'>
- **Required**: Yes

### SettingValue
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


