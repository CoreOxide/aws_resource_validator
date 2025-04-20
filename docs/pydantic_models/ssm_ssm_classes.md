# Ssm Ssm Classes

# AccountSharingInfo

### AccountId
- **Type**: typing.Optional[str]

### SharedDocumentVersion
- **Type**: typing.Optional[str]


# Activation

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]


# AddTagsToResourceRequest

### ResourceType
- **Type**: typing.Literal['Association', 'Automation', 'Document', 'MaintenanceWindow', 'ManagedInstance', 'OpsItem', 'OpsMetadata', 'Parameter', 'PatchBaseline']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]
- **Required**: Yes


# Alarm

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AlarmConfiguration

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Alarm]
- **Required**: Yes

### IgnorePollAlarmFailure
- **Type**: typing.Optional[bool]


# AlarmConfigurationOutput

### Alarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Alarm]
- **Required**: Yes

### IgnorePollAlarmFailure
- **Type**: typing.Optional[bool]


# AlarmStateInformation

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ALARM', 'UNKNOWN']
- **Required**: Yes


# AssociateOpsItemRelatedItemRequest

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


# AssociateOpsItemRelatedItemResponse

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# Association

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### LastExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationOverview]

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


# AssociationDescription

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationStatusOutput]

### Overview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationOverview]

### DocumentVersion
- **Type**: typing.Optional[str]

### AutomationTargetParameterName
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### AssociationId
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputLocation]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]


# AssociationExecution

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]


# AssociationExecutionFilter

### Key
- **Type**: typing.Literal['CreatedTime', 'ExecutionId', 'Status']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['EQUAL', 'GREATER_THAN', 'LESS_THAN']
- **Required**: Yes


# AssociationExecutionTarget

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
- **Type**: <class 'NoneType'>


# AssociationExecutionTargetsFilter

### Key
- **Type**: typing.Literal['ResourceId', 'ResourceType', 'Status']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationFilter

### key
- **Type**: typing.Literal['AssociationId', 'AssociationName', 'AssociationStatusName', 'InstanceId', 'LastExecutedAfter', 'LastExecutedBefore', 'Name', 'ResourceGroupName']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationOverview

### Status
- **Type**: typing.Optional[str]

### DetailedStatus
- **Type**: typing.Optional[str]

### AssociationStatusAggregatedCount
- **Type**: typing.Optional[typing.Dict[str, int]]


# AssociationStatus

### Date
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Name
- **Type**: typing.Literal['Failed', 'Pending', 'Success']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalInfo
- **Type**: typing.Optional[str]


# AssociationStatusOutput

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


# AssociationVersionInfo

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputLocation]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]


# AttachmentContent

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


# AttachmentInformation

### Name
- **Type**: typing.Optional[str]


# AttachmentsSource

### Key
- **Type**: typing.Optional[typing.Literal['AttachmentReference', 'S3FileUrl', 'SourceUrl']]

### Values
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]


# AutomationExecution

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.StepExecution]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### ResolvedTargets
- **Type**: <class 'NoneType'>

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]

### ProgressCounters
- **Type**: <class 'NoneType'>

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]

### TargetLocationsURL
- **Type**: typing.Optional[str]

### AutomationSubtype
- **Type**: typing.Optional[typing.Literal['ChangeRequest']]

### ScheduledTime
- **Type**: typing.Optional[datetime.datetime]

### Runbooks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.RunbookOutput]]

### OpsItemId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### ChangeRequestName
- **Type**: typing.Optional[str]

### Variables
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# AutomationExecutionFilter

### Key
- **Type**: typing.Literal['AutomationSubtype', 'AutomationType', 'CurrentAction', 'DocumentNamePrefix', 'ExecutionId', 'ExecutionStatus', 'OpsItemId', 'ParentExecutionId', 'StartTimeAfter', 'StartTimeBefore', 'TagKey', 'TargetResourceGroup']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# AutomationExecutionInputs

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### TargetLocations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocation, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]]

### TargetLocationsURL
- **Type**: typing.Optional[str]


# AutomationExecutionMetadata

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### ResolvedTargets
- **Type**: <class 'NoneType'>

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### AutomationType
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'Local']]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]

### TargetLocationsURL
- **Type**: typing.Optional[str]

### AutomationSubtype
- **Type**: typing.Optional[typing.Literal['ChangeRequest']]

### ScheduledTime
- **Type**: typing.Optional[datetime.datetime]

### Runbooks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.RunbookOutput]]

### OpsItemId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### ChangeRequestName
- **Type**: typing.Optional[str]


# AutomationExecutionPreview

### StepPreviews
- **Type**: typing.Optional[typing.Dict[typing.Literal['Mutating', 'NonMutating', 'Undetermined'], int]]

### Regions
- **Type**: typing.Optional[typing.List[str]]

### TargetPreviews
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetPreview]]

### TotalAccounts
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineOverride

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]

### GlobalFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput, NoneType]

### ApprovalRules
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroupOutput, NoneType]

### ApprovedPatches
- **Type**: typing.Optional[typing.List[str]]

### ApprovedPatchesComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### RejectedPatches
- **Type**: typing.Optional[typing.List[str]]

### RejectedPatchesAction
- **Type**: typing.Optional[typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']]

### ApprovedPatchesEnableNonSecurity
- **Type**: typing.Optional[bool]

### Sources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSource, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSourceOutput]]]


# CancelCommandRequest

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# CancelMaintenanceWindowExecutionRequest

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelMaintenanceWindowExecutionResult

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CloudWatchOutputConfig

### CloudWatchLogGroupName
- **Type**: typing.Optional[str]

### CloudWatchOutputEnabled
- **Type**: typing.Optional[bool]


# Command

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.NotificationConfigOutput]

### CloudWatchOutputConfig
- **Type**: <class 'NoneType'>

### TimeoutSeconds
- **Type**: typing.Optional[int]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]


# CommandFilter

### key
- **Type**: typing.Literal['DocumentName', 'ExecutionStage', 'InvokedAfter', 'InvokedBefore', 'Status']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CommandInvocation

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.CommandPlugin]]

### ServiceRole
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.NotificationConfigOutput]

### CloudWatchOutputConfig
- **Type**: <class 'NoneType'>


# CommandPlugin

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


# ComplianceExecutionSummary

### ExecutionTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ExecutionId
- **Type**: typing.Optional[str]

### ExecutionType
- **Type**: typing.Optional[str]


# ComplianceExecutionSummaryOutput

### ExecutionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionId
- **Type**: typing.Optional[str]

### ExecutionType
- **Type**: typing.Optional[str]


# ComplianceItem

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceExecutionSummaryOutput]

### Details
- **Type**: typing.Optional[typing.Dict[str, str]]


# ComplianceItemEntry

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# ComplianceStringFilter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['BEGIN_WITH', 'EQUAL', 'GREATER_THAN', 'LESS_THAN', 'NOT_EQUAL']]


# ComplianceSummaryItem

### ComplianceType
- **Type**: typing.Optional[str]

### CompliantSummary
- **Type**: <class 'NoneType'>

### NonCompliantSummary
- **Type**: <class 'NoneType'>


# CompliantSummary

### CompliantCount
- **Type**: typing.Optional[int]

### SeveritySummary
- **Type**: <class 'NoneType'>


# CreateActivationRequest

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### RegistrationMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.RegistrationMetadataItem]]


# CreateActivationResult

### ActivationId
- **Type**: <class 'str'>
- **Required**: Yes

### ActivationCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssociationBatchRequest

### Entries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.CreateAssociationBatchRequestEntry, aws_resource_validator.pydantic_models.ssm.ssm_classes.CreateAssociationBatchRequestEntryOutput]]
- **Required**: Yes


# CreateAssociationBatchRequestEntry

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputLocation]

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocation, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]


# CreateAssociationBatchRequestEntryOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputLocation]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]


# CreateAssociationBatchResult

### Successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationDescription]
- **Required**: Yes

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.FailedCreateAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssociationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputLocation]

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
- **Type**: typing.Optional[typing.List[str]]

### TargetLocations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocation, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]


# CreateAssociationResult

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDocumentRequest

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Requires
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentRequires]]

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AttachmentsSource]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]


# CreateDocumentResult

### DocumentDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMaintenanceWindowRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]


# CreateMaintenanceWindowResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOpsItemRequest

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemDataValue]]

### Notifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemNotification]]

### Priority
- **Type**: typing.Optional[int]

### RelatedOpsItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.RelatedOpsItem]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### Category
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ActualStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ActualEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PlannedStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PlannedEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### AccountId
- **Type**: typing.Optional[str]


# CreateOpsItemResponse

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### OpsItemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOpsMetadataRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MetadataValue]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]


# CreateOpsMetadataResult

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePatchBaselineRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]

### GlobalFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput, NoneType]

### ApprovalRules
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroupOutput, NoneType]

### ApprovedPatches
- **Type**: typing.Optional[typing.List[str]]

### ApprovedPatchesComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApprovedPatchesEnableNonSecurity
- **Type**: typing.Optional[bool]

### RejectedPatches
- **Type**: typing.Optional[typing.List[str]]

### RejectedPatchesAction
- **Type**: typing.Optional[typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']]

### Description
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSource, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSourceOutput]]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]


# CreatePatchBaselineResult

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceDataSyncRequest

### SyncName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncS3Destination]

### SyncType
- **Type**: typing.Optional[str]

### SyncSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncSource]


# DeleteActivationRequest

### ActivationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssociationRequest

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]


# DeleteDocumentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### Force
- **Type**: typing.Optional[bool]


# DeleteInventoryRequest

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaDeleteOption
- **Type**: typing.Optional[typing.Literal['DeleteSchema', 'DisableSchema']]

### DryRun
- **Type**: typing.Optional[bool]

### ClientToken
- **Type**: typing.Optional[str]


# DeleteInventoryResult

### DeletionId
- **Type**: <class 'str'>
- **Required**: Yes

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryDeletionSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMaintenanceWindowRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMaintenanceWindowResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteOpsItemRequest

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOpsMetadataRequest

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParameterRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteParametersRequest

### Names
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteParametersResult

### DeletedParameters
- **Type**: typing.List[str]
- **Required**: Yes

### InvalidParameters
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePatchBaselineRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePatchBaselineResult

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourceDataSyncRequest

### SyncName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Optional[str]


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterManagedInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterPatchBaselineForPatchGroupRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterPatchBaselineForPatchGroupResult

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterTargetFromMaintenanceWindowRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Safe
- **Type**: typing.Optional[bool]


# DeregisterTargetFromMaintenanceWindowResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterTaskFromMaintenanceWindowRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTaskFromMaintenanceWindowResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeActivationsFilter

### FilterKey
- **Type**: typing.Optional[typing.Literal['ActivationIds', 'DefaultInstanceName', 'IamRole']]

### FilterValues
- **Type**: typing.Optional[typing.List[str]]


# DescribeActivationsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DescribeActivationsFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeActivationsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DescribeActivationsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeActivationsResult

### ActivationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Activation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionTargetsRequest

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationExecutionTargetsFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionTargetsRequestPaginate

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationExecutionTargetsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeAssociationExecutionTargetsResult

### AssociationExecutionTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationExecutionTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionsRequest

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationExecutionFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationExecutionsRequestPaginate

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationExecutionFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeAssociationExecutionsResult

### AssociationExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAssociationRequest

### Name
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### AssociationId
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]


# DescribeAssociationResult

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAutomationExecutionsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AutomationExecutionFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAutomationExecutionsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AutomationExecutionFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeAutomationExecutionsResult

### AutomationExecutionMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AutomationExecutionMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAutomationStepExecutionsRequest

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.StepExecutionFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ReverseOrder
- **Type**: typing.Optional[bool]


# DescribeAutomationStepExecutionsRequestPaginate

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.StepExecutionFilter]]

### ReverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeAutomationStepExecutionsResult

### StepExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.StepExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAvailablePatchesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAvailablePatchesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeAvailablePatchesResult

### Patches
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Patch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDocumentPermissionRequest

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


# DescribeDocumentPermissionResponse

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### AccountSharingInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AccountSharingInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDocumentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]


# DescribeDocumentResult

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEffectiveInstanceAssociationsRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEffectiveInstanceAssociationsRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeEffectiveInstanceAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEffectivePatchesForPatchBaselineRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeEffectivePatchesForPatchBaselineRequestPaginate

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeEffectivePatchesForPatchBaselineResult

### EffectivePatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.EffectivePatch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceAssociationsStatusRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceAssociationsStatusRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInstanceAssociationsStatusResult

### InstanceAssociationStatusInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationStatusInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceInformationRequest

### InstanceInformationFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceInformationFilter]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceInformationStringFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstanceInformationRequestPaginate

### InstanceInformationFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceInformationFilter]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceInformationStringFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInstanceInformationResult

### InstanceInformationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePatchStatesForPatchGroupRequest

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePatchStateFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInstancePatchStatesForPatchGroupRequestPaginate

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePatchStateFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInstancePatchStatesForPatchGroupResult

### InstancePatchStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePatchState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePatchStatesRequest

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInstancePatchStatesRequestPaginate

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInstancePatchStatesResult

### InstancePatchStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePatchState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePatchesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInstancePatchesRequestPaginate

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInstancePatchesResult

### Patches
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchComplianceData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePropertiesRequest

### InstancePropertyFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePropertyFilter]]

### FiltersWithOperator
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePropertyStringFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeInstancePropertiesRequestPaginate

### InstancePropertyFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePropertyFilter]]

### FiltersWithOperator
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstancePropertyStringFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInstancePropertiesResult

### InstanceProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceProperty]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeInventoryDeletionsRequest

### DeletionId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeInventoryDeletionsRequestPaginate

### DeletionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeInventoryDeletionsResult

### InventoryDeletions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryDeletionStatusItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTaskInvocationsRequest

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginate

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowExecutionTaskInvocationsResult

### WindowExecutionTaskInvocationIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowExecutionTaskInvocationIdentity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTasksRequest

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionTasksRequestPaginate

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowExecutionTasksResult

### WindowExecutionTaskIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowExecutionTaskIdentity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionsRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowExecutionsRequestPaginate

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowExecutionsResult

### WindowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowScheduleRequest

### WindowId
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'RESOURCE_GROUP']]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowScheduleRequestPaginate

### WindowId
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'RESOURCE_GROUP']]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowScheduleResult

### ScheduledWindowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ScheduledWindowExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTargetsRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTargetsRequestPaginate

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowTargetsResult

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTasksRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowTasksRequestPaginate

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowTasksResult

### Tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsForTargetRequest

### Targets
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['INSTANCE', 'RESOURCE_GROUP']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsForTargetRequestPaginate

### Targets
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['INSTANCE', 'RESOURCE_GROUP']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowsForTargetResult

### WindowIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowIdentityForTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMaintenanceWindowsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeMaintenanceWindowsResult

### WindowIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowIdentity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOpsItemsRequest

### OpsItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOpsItemsRequestPaginate

### OpsItemFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeOpsItemsResponse

### OpsItemSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeParametersRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParametersFilter]]

### ParameterFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterStringFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Shared
- **Type**: typing.Optional[bool]


# DescribeParametersRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParametersFilter]]

### ParameterFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterStringFilter]]

### Shared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeParametersResult

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchBaselinesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchBaselinesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribePatchBaselinesResult

### BaselineIdentities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchBaselineIdentity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchGroupStateRequest

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePatchGroupStateResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePatchGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchGroupsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchOrchestratorFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribePatchGroupsResult

### Mappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchGroupPatchBaselineMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePatchPropertiesRequest

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


# DescribePatchPropertiesRequestPaginate

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### Property
- **Type**: typing.Literal['CLASSIFICATION', 'MSRC_SEVERITY', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'SEVERITY']
- **Required**: Yes

### PatchSet
- **Type**: typing.Optional[typing.Literal['APPLICATION', 'OS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribePatchPropertiesResult

### Properties
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSessionsRequest

### State
- **Type**: typing.Literal['Active', 'History']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.SessionFilter]]


# DescribeSessionsRequestPaginate

### State
- **Type**: typing.Literal['Active', 'History']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.SessionFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# DescribeSessionsResponse

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Session]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateOpsItemRelatedItemRequest

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentDefaultVersionDescription

### Name
- **Type**: typing.Optional[str]

### DefaultVersion
- **Type**: typing.Optional[str]

### DefaultVersionName
- **Type**: typing.Optional[str]


# DocumentDescription

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentParameter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### AttachmentsInformation
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AttachmentInformation]]

### Requires
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentRequires]]

### Author
- **Type**: typing.Optional[str]

### ReviewInformation
- **Type**: typing.Optional[typing.List[NoneType]]

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


# DocumentFilter

### key
- **Type**: typing.Literal['DocumentType', 'Name', 'Owner', 'PlatformTypes']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentIdentifier

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### Requires
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentRequires]]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Author
- **Type**: typing.Optional[str]


# DocumentKeyValuesFilter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# DocumentMetadataResponseInfo

### ReviewerResponse
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentReviewerResponseSource]]


# DocumentParameter

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['String', 'StringList']]

### Description
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]


# DocumentRequires

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### RequireType
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]


# DocumentReviewCommentSource

### Type
- **Type**: typing.Optional[typing.Literal['Comment']]

### Content
- **Type**: typing.Optional[str]


# DocumentReviewerResponseSource

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ReviewStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Comment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentReviewCommentSource]]

### Reviewer
- **Type**: typing.Optional[str]


# DocumentReviews

### Action
- **Type**: typing.Literal['Approve', 'Reject', 'SendForReview', 'UpdateReview']
- **Required**: Yes

### Comment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentReviewCommentSource]]


# DocumentVersionInfo

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


# EffectivePatch

### Patch
- **Type**: <class 'NoneType'>

### PatchStatus
- **Type**: <class 'NoneType'>


# ExecutionInputs

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AutomationExecutionInputs]


# ExecutionPreview

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AutomationExecutionPreview]


# FailedCreateAssociation

### Entry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.CreateAssociationBatchRequestEntryOutput]

### Message
- **Type**: typing.Optional[str]

### Fault
- **Type**: typing.Optional[typing.Literal['Client', 'Server', 'Unknown']]


# FailureDetails

### FailureStage
- **Type**: typing.Optional[str]

### FailureType
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# GetAutomationExecutionRequest

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAutomationExecutionResult

### AutomationExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AutomationExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetCalendarStateRequest

### CalendarNames
- **Type**: typing.List[str]
- **Required**: Yes

### AtTime
- **Type**: typing.Optional[str]


# GetCalendarStateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetCommandInvocationRequest

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginName
- **Type**: typing.Optional[str]


# GetCommandInvocationRequestWait

### CommandId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PluginName
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetCommandInvocationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.CloudWatchOutputConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionStatusRequest

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionStatusResponse

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['connected', 'notconnected']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDefaultPatchBaselineRequest

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]


# GetDefaultPatchBaselineResult

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeployablePatchSnapshotForInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineOverride
- **Type**: <class 'NoneType'>


# GetDeployablePatchSnapshotForInstanceResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetDocumentRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]

### DocumentVersion
- **Type**: typing.Optional[str]

### DocumentFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'TEXT', 'YAML']]


# GetDocumentResult

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentRequires]
- **Required**: Yes

### AttachmentsContent
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AttachmentContent]
- **Required**: Yes

### ReviewStatus
- **Type**: typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetExecutionPreviewRequest

### ExecutionPreviewId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExecutionPreviewResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ExecutionPreview'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetInventoryRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryFilter]]

### Aggregators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryAggregator]]

### ResultAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResultAttribute]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetInventoryRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryFilter]]

### Aggregators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryAggregatorPaginator]]

### ResultAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResultAttribute]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# GetInventoryResult

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryResultEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInventorySchemaRequest

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


# GetInventorySchemaRequestPaginate

### TypeName
- **Type**: typing.Optional[str]

### Aggregator
- **Type**: typing.Optional[bool]

### SubType
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# GetInventorySchemaResult

### Schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryItemSchema]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMaintenanceWindowExecutionRequest

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowExecutionResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskInvocationRequest

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskInvocationResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskRequest

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowExecutionTaskResult

### WindowExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRole
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']
- **Required**: Yes

### TaskParameters
- **Type**: typing.List[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutput]]
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

### AlarmConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput'>
- **Required**: Yes

### TriggeredAlarms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetMaintenanceWindowRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetMaintenanceWindowTaskRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMaintenanceWindowTaskResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]
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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutput]
- **Required**: Yes

### TaskInvocationParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskInvocationParametersOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.LoggingInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpsItemRequest

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### OpsItemArn
- **Type**: typing.Optional[str]


# GetOpsItemResponse

### OpsItem
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpsMetadataRequest

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOpsMetadataResult

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MetadataValue]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOpsSummaryRequest

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsFilter]]

### Aggregators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsAggregator]]

### ResultAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsResultAttribute]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetOpsSummaryRequestPaginate

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsFilter]]

### Aggregators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsAggregatorPaginator]]

### ResultAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsResultAttribute]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# GetOpsSummaryResult

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetParameterHistoryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetParameterHistoryRequestPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# GetParameterHistoryResult

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterHistory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetParameterRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]


# GetParameterResult

### Parameter
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.Parameter'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetParametersByPathRequest

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Recursive
- **Type**: typing.Optional[bool]

### ParameterFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterStringFilter]]

### WithDecryption
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetParametersByPathRequestPaginate

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Recursive
- **Type**: typing.Optional[bool]

### ParameterFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterStringFilter]]

### WithDecryption
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# GetParametersByPathResult

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Parameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetParametersRequest

### Names
- **Type**: typing.List[str]
- **Required**: Yes

### WithDecryption
- **Type**: typing.Optional[bool]


# GetParametersResult

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Parameter]
- **Required**: Yes

### InvalidParameters
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetPatchBaselineForPatchGroupRequest

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: typing.Optional[typing.Literal['ALMA_LINUX', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'AMAZON_LINUX_2022', 'AMAZON_LINUX_2023', 'CENTOS', 'DEBIAN', 'MACOS', 'ORACLE_LINUX', 'RASPBIAN', 'REDHAT_ENTERPRISE_LINUX', 'ROCKY_LINUX', 'SUSE', 'UBUNTU', 'WINDOWS']]


# GetPatchBaselineForPatchGroupResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetPatchBaselineRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPatchBaselineResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput'>
- **Required**: Yes

### ApprovalRules
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroupOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSourceOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePoliciesRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetResourcePoliciesRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# GetResourcePoliciesResponse

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.GetResourcePoliciesResponseEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePoliciesResponseEntry

### PolicyId
- **Type**: typing.Optional[str]

### PolicyHash
- **Type**: typing.Optional[str]

### Policy
- **Type**: typing.Optional[str]


# GetServiceSettingRequest

### SettingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceSettingResult

### ServiceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ServiceSetting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceAggregatedAssociationOverview

### DetailedStatus
- **Type**: typing.Optional[str]

### InstanceAssociationStatusAggregatedCount
- **Type**: typing.Optional[typing.Dict[str, int]]


# InstanceAssociation

### AssociationId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### AssociationVersion
- **Type**: typing.Optional[str]


# InstanceAssociationOutputLocation

### S3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.S3OutputLocation]


# InstanceAssociationOutputUrl

### S3OutputUrl
- **Type**: <class 'NoneType'>


# InstanceAssociationStatusInfo

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputUrl]

### AssociationName
- **Type**: typing.Optional[str]


# InstanceInfo

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


# InstanceInformation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAggregatedAssociationOverview]

### SourceId
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['AWS::EC2::Instance', 'AWS::IoT::Thing', 'AWS::SSM::ManagedInstance']]


# InstanceInformationFilter

### key
- **Type**: typing.Literal['ActivationIds', 'AgentVersion', 'AssociationStatus', 'IamRole', 'InstanceIds', 'PingStatus', 'PlatformTypes', 'ResourceType']
- **Required**: Yes

### valueSet
- **Type**: typing.List[str]
- **Required**: Yes


# InstanceInformationStringFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# InstancePatchState

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


# InstancePatchStateFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Type
- **Type**: typing.Literal['Equal', 'GreaterThan', 'LessThan', 'NotEqual']
- **Required**: Yes


# InstanceProperty

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAggregatedAssociationOverview]

### SourceId
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['AWS::EC2::Instance', 'AWS::IoT::Thing', 'AWS::SSM::ManagedInstance']]


# InstancePropertyFilter

### key
- **Type**: typing.Literal['ActivationIds', 'AgentVersion', 'AssociationStatus', 'DocumentName', 'IamRole', 'InstanceIds', 'PingStatus', 'PlatformTypes', 'ResourceType']
- **Required**: Yes

### valueSet
- **Type**: typing.List[str]
- **Required**: Yes


# InstancePropertyStringFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['BeginWith', 'Equal', 'GreaterThan', 'LessThan', 'NotEqual']]


# InventoryAggregator

### Expression
- **Type**: typing.Optional[str]

### Aggregators
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryGroup]]


# InventoryAggregatorPaginator

### Expression
- **Type**: typing.Optional[str]

### Aggregators
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryGroup]]


# InventoryDeletionStatusItem

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryDeletionSummary]

### LastStatusUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# InventoryDeletionSummary

### TotalCount
- **Type**: typing.Optional[int]

### RemainingCount
- **Type**: typing.Optional[int]

### SummaryItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryDeletionSummaryItem]]


# InventoryDeletionSummaryItem

### Version
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]

### RemainingCount
- **Type**: typing.Optional[int]


# InventoryFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['BeginWith', 'Equal', 'Exists', 'GreaterThan', 'LessThan', 'NotEqual']]


# InventoryGroup

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryFilter]
- **Required**: Yes


# InventoryItem

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
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]

### Context
- **Type**: typing.Optional[typing.Dict[str, str]]


# InventoryItemAttribute

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DataType
- **Type**: typing.Literal['number', 'string']
- **Required**: Yes


# InventoryItemSchema

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryItemAttribute]
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# InventoryResultEntity

### Id
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryResultItem]]


# InventoryResultItem

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


# LabelParameterVersionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### ParameterVersion
- **Type**: typing.Optional[int]


# LabelParameterVersionResult

### InvalidLabels
- **Type**: typing.List[str]
- **Required**: Yes

### ParameterVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# ListAssociationVersionsRequest

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationVersionsRequestPaginate

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListAssociationVersionsResult

### AssociationVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationVersionInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsRequest

### AssociationFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsRequestPaginate

### AssociationFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Association]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCommandInvocationsRequest

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.CommandFilter]]

### Details
- **Type**: typing.Optional[bool]


# ListCommandInvocationsRequestPaginate

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.CommandFilter]]

### Details
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListCommandInvocationsResult

### CommandInvocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.CommandInvocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCommandsRequest

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.CommandFilter]]


# ListCommandsRequestPaginate

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.CommandFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListCommandsResult

### Commands
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Command]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComplianceItemsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceStringFilter]]

### ResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComplianceItemsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceStringFilter]]

### ResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListComplianceItemsResult

### ComplianceItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComplianceSummariesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceStringFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComplianceSummariesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceStringFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListComplianceSummariesResult

### ComplianceSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceSummaryItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentMetadataHistoryRequest

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


# ListDocumentMetadataHistoryResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentMetadataResponseInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentVersionsRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentVersionsRequestPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListDocumentVersionsResult

### DocumentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentVersionInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentsRequest

### DocumentFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentFilter]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentKeyValuesFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentsRequestPaginate

### DocumentFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentFilter]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentKeyValuesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListDocumentsResult

### DocumentIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInventoryEntriesRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInventoryEntriesResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequest

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNodesRequestPaginate

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListNodesResult

### Nodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Node]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesSummaryRequest

### Aggregators
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeAggregator]
- **Required**: Yes

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNodesSummaryRequestPaginate

### Aggregators
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeAggregatorPaginator]
- **Required**: Yes

### SyncName
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListNodesSummaryResult

### Summary
- **Type**: typing.List[typing.Dict[str, str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemEventsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemEventFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemEventsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemEventFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListOpsItemEventsResponse

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemEventSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemRelatedItemsRequest

### OpsItemId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemRelatedItemsFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOpsItemRelatedItemsRequestPaginate

### OpsItemId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemRelatedItemsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListOpsItemRelatedItemsResponse

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemRelatedItemSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOpsMetadataRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsMetadataFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOpsMetadataRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsMetadataFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListOpsMetadataResult

### OpsMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceComplianceSummariesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceStringFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceComplianceSummariesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceStringFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListResourceComplianceSummariesResult

### ResourceComplianceSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceComplianceSummaryItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDataSyncRequest

### SyncType
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceDataSyncRequestPaginate

### SyncType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PaginatorConfig]


# ListResourceDataSyncResult

### ResourceDataSyncItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceType
- **Type**: typing.Literal['Association', 'Automation', 'Document', 'MaintenanceWindow', 'ManagedInstance', 'OpsItem', 'OpsMetadata', 'Parameter', 'PatchBaseline']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingInfo

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Region
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]


# MaintenanceWindowAutomationParameters

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# MaintenanceWindowAutomationParametersOutput

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# MaintenanceWindowExecution

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


# MaintenanceWindowExecutionTaskIdentity

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]


# MaintenanceWindowExecutionTaskInvocationIdentity

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


# MaintenanceWindowFilter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# MaintenanceWindowIdentity

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


# MaintenanceWindowIdentityForTarget

### WindowId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MaintenanceWindowLambdaParameters

### ClientContext
- **Type**: typing.Optional[str]

### Qualifier
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# MaintenanceWindowLambdaParametersOutput

### ClientContext
- **Type**: typing.Optional[str]

### Qualifier
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Optional[bytes]


# MaintenanceWindowRunCommandParameters

### Comment
- **Type**: typing.Optional[str]

### CloudWatchOutputConfig
- **Type**: <class 'NoneType'>

### DocumentHash
- **Type**: typing.Optional[str]

### DocumentHashType
- **Type**: typing.Optional[typing.Literal['Sha1', 'Sha256']]

### DocumentVersion
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: <class 'NoneType'>

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


# MaintenanceWindowRunCommandParametersOutput

### Comment
- **Type**: typing.Optional[str]

### CloudWatchOutputConfig
- **Type**: <class 'NoneType'>

### DocumentHash
- **Type**: typing.Optional[str]

### DocumentHashType
- **Type**: typing.Optional[typing.Literal['Sha1', 'Sha256']]

### DocumentVersion
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.NotificationConfigOutput]

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


# MaintenanceWindowStepFunctionsParameters

### Input
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MaintenanceWindowTarget

### WindowId
- **Type**: typing.Optional[str]

### WindowTargetId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['INSTANCE', 'RESOURCE_GROUP']]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### OwnerInformation
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# MaintenanceWindowTask

### WindowId
- **Type**: typing.Optional[str]

### WindowTaskId
- **Type**: typing.Optional[str]

### TaskArn
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['AUTOMATION', 'LAMBDA', 'RUN_COMMAND', 'STEP_FUNCTIONS']]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### TaskParameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutput]]

### Priority
- **Type**: typing.Optional[int]

### LoggingInfo
- **Type**: <class 'NoneType'>

### ServiceRoleArn
- **Type**: typing.Optional[str]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CutoffBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']]

### AlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]


# MaintenanceWindowTaskInvocationParameters

### RunCommand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowRunCommandParameters]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowAutomationParameters]

### StepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowStepFunctionsParameters]

### Lambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowLambdaParameters]


# MaintenanceWindowTaskInvocationParametersOutput

### RunCommand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowRunCommandParametersOutput]

### Automation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowAutomationParametersOutput]

### StepFunctions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowStepFunctionsParameters]

### Lambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowLambdaParametersOutput]


# MaintenanceWindowTaskParameterValueExpression

### Values
- **Type**: typing.Optional[typing.List[str]]


# MaintenanceWindowTaskParameterValueExpressionOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# MetadataValue

### Value
- **Type**: typing.Optional[str]


# ModifyDocumentPermissionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionType
- **Type**: typing.Literal['Share']
- **Required**: Yes

### AccountIdsToAdd
- **Type**: typing.Optional[typing.List[str]]

### AccountIdsToRemove
- **Type**: typing.Optional[typing.List[str]]

### SharedDocumentVersion
- **Type**: typing.Optional[str]


# Node

### CaptureTime
- **Type**: typing.Optional[datetime.datetime]

### Id
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.NodeOwnerInfo]

### Region
- **Type**: typing.Optional[str]

### NodeType
- **Type**: <class 'NoneType'>


# NodeAggregator

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
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# NodeAggregatorPaginator

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
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# NodeFilter

### Key
- **Type**: typing.Literal['AccountId', 'AgentType', 'AgentVersion', 'ComputerName', 'InstanceId', 'InstanceStatus', 'IpAddress', 'ManagedStatus', 'OrganizationalUnitId', 'OrganizationalUnitPath', 'PlatformName', 'PlatformType', 'PlatformVersion', 'Region', 'ResourceType']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['BeginWith', 'Equal', 'NotEqual']]


# NodeOwnerInfo

### AccountId
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### OrganizationalUnitPath
- **Type**: typing.Optional[str]


# NodeType

### Instance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceInfo]


# NonCompliantSummary

### NonCompliantCount
- **Type**: typing.Optional[int]

### SeveritySummary
- **Type**: <class 'NoneType'>


# NotificationConfig

### NotificationArn
- **Type**: typing.Optional[str]

### NotificationEvents
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'Cancelled', 'Failed', 'InProgress', 'Success', 'TimedOut']]]

### NotificationType
- **Type**: typing.Optional[typing.Literal['Command', 'Invocation']]


# NotificationConfigOutput

### NotificationArn
- **Type**: typing.Optional[str]

### NotificationEvents
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'Cancelled', 'Failed', 'InProgress', 'Success', 'TimedOut']]]

### NotificationType
- **Type**: typing.Optional[typing.Literal['Command', 'Invocation']]


# OpsAggregator

### AggregatorType
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### AttributeName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Dict[str, str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsFilter]]

### Aggregators
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# OpsAggregatorPaginator

### AggregatorType
- **Type**: typing.Optional[str]

### TypeName
- **Type**: typing.Optional[str]

### AttributeName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Dict[str, str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsFilter]]

### Aggregators
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# OpsEntity

### Id
- **Type**: typing.Optional[str]

### Data
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsEntityItem]]


# OpsEntityItem

### CaptureTime
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]


# OpsFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['BeginWith', 'Equal', 'Exists', 'GreaterThan', 'LessThan', 'NotEqual']]


# OpsItem

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemNotification]]

### Priority
- **Type**: typing.Optional[int]

### RelatedOpsItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.RelatedOpsItem]]

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemDataValue]]

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


# OpsItemDataValue

### Value
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['SearchableString', 'String']]


# OpsItemEventFilter

### Key
- **Type**: typing.Literal['OpsItemId']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Equal']
- **Required**: Yes


# OpsItemEventSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemIdentity]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# OpsItemFilter

### Key
- **Type**: typing.Literal['AccountId', 'ActualEndTime', 'ActualStartTime', 'AutomationId', 'Category', 'ChangeRequestByApproverArn', 'ChangeRequestByApproverName', 'ChangeRequestByRequesterArn', 'ChangeRequestByRequesterName', 'ChangeRequestByTargetsResourceGroup', 'ChangeRequestByTemplate', 'CreatedBy', 'CreatedTime', 'InsightByType', 'LastModifiedTime', 'OperationalData', 'OperationalDataKey', 'OperationalDataValue', 'OpsItemId', 'OpsItemType', 'PlannedEndTime', 'PlannedStartTime', 'Priority', 'ResourceId', 'Severity', 'Source', 'Status', 'Title']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Contains', 'Equal', 'GreaterThan', 'LessThan']
- **Required**: Yes


# OpsItemIdentity

### Arn
- **Type**: typing.Optional[str]


# OpsItemNotification

### Arn
- **Type**: typing.Optional[str]


# OpsItemRelatedItemSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemIdentity]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemIdentity]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# OpsItemRelatedItemsFilter

### Key
- **Type**: typing.Literal['AssociationId', 'ResourceType', 'ResourceUri']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['Equal']
- **Required**: Yes


# OpsItemSummary

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemDataValue]]

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


# OpsMetadata

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


# OpsMetadataFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# OpsResultAttribute

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes


# OutputSource

### OutputSourceId
- **Type**: typing.Optional[str]

### OutputSourceType
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['SecureString', 'String', 'StringList']]

### Value
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Selector
- **Type**: typing.Optional[str]

### SourceResult
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### ARN
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]


# ParameterHistory

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['SecureString', 'String', 'StringList']]

### KeyId
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedUser
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### AllowedPattern
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Labels
- **Type**: typing.Optional[typing.List[str]]

### Tier
- **Type**: typing.Optional[typing.Literal['Advanced', 'Intelligent-Tiering', 'Standard']]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterInlinePolicy]]

### DataType
- **Type**: typing.Optional[str]


# ParameterInlinePolicy

### PolicyText
- **Type**: typing.Optional[str]

### PolicyType
- **Type**: typing.Optional[str]

### PolicyStatus
- **Type**: typing.Optional[str]


# ParameterMetadata

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['SecureString', 'String', 'StringList']]

### KeyId
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedUser
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AllowedPattern
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Tier
- **Type**: typing.Optional[typing.Literal['Advanced', 'Intelligent-Tiering', 'Standard']]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ParameterInlinePolicy]]

### DataType
- **Type**: typing.Optional[str]


# ParameterStringFilter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Option
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# ParametersFilter

### Key
- **Type**: typing.Literal['KeyId', 'Name', 'Type']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ParentStepDetails

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


# Patch

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


# PatchBaselineIdentity

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


# PatchComplianceData

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


# PatchFilter

### Key
- **Type**: typing.Literal['ADVISORY_ID', 'ARCH', 'BUGZILLA_ID', 'CLASSIFICATION', 'CVE_ID', 'EPOCH', 'MSRC_SEVERITY', 'NAME', 'PATCH_ID', 'PATCH_SET', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'RELEASE', 'REPOSITORY', 'SECTION', 'SECURITY', 'SEVERITY', 'VERSION']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PatchFilterGroup

### PatchFilters
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilter, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterOutput]]
- **Required**: Yes


# PatchFilterGroupOutput

### PatchFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterOutput]
- **Required**: Yes


# PatchFilterOutput

### Key
- **Type**: typing.Literal['ADVISORY_ID', 'ARCH', 'BUGZILLA_ID', 'CLASSIFICATION', 'CVE_ID', 'EPOCH', 'MSRC_SEVERITY', 'NAME', 'PATCH_ID', 'PATCH_SET', 'PRIORITY', 'PRODUCT', 'PRODUCT_FAMILY', 'RELEASE', 'REPOSITORY', 'SECTION', 'SECURITY', 'SEVERITY', 'VERSION']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# PatchGroupPatchBaselineMapping

### PatchGroup
- **Type**: typing.Optional[str]

### BaselineIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchBaselineIdentity]


# PatchOrchestratorFilter

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# PatchRule

### PatchFilterGroup
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput]
- **Required**: Yes

### ComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApproveAfterDays
- **Type**: typing.Optional[int]

### ApproveUntilDate
- **Type**: typing.Optional[str]

### EnableNonSecurity
- **Type**: typing.Optional[bool]


# PatchRuleGroup

### PatchRules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRule, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleOutput]]
- **Required**: Yes


# PatchRuleGroupOutput

### PatchRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleOutput]
- **Required**: Yes


# PatchRuleOutput

### PatchFilterGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput'>
- **Required**: Yes

### ComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApproveAfterDays
- **Type**: typing.Optional[int]

### ApproveUntilDate
- **Type**: typing.Optional[str]

### EnableNonSecurity
- **Type**: typing.Optional[bool]


# PatchSource

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Products
- **Type**: typing.List[str]
- **Required**: Yes

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes


# PatchSourceOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Products
- **Type**: typing.List[str]
- **Required**: Yes

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes


# PatchStatus

### DeploymentStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'EXPLICIT_APPROVED', 'EXPLICIT_REJECTED', 'PENDING_APPROVAL']]

### ComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApprovalDate
- **Type**: typing.Optional[datetime.datetime]


# ProgressCounters

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


# PutComplianceItemsRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceExecutionSummary, aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceExecutionSummaryOutput]
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceItemEntry]
- **Required**: Yes

### ItemContentHash
- **Type**: typing.Optional[str]

### UploadType
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'PARTIAL']]


# PutInventoryRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.InventoryItem]
- **Required**: Yes


# PutInventoryResult

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# PutParameterRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['SecureString', 'String', 'StringList']]

### KeyId
- **Type**: typing.Optional[str]

### Overwrite
- **Type**: typing.Optional[bool]

### AllowedPattern
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### Tier
- **Type**: typing.Optional[typing.Literal['Advanced', 'Intelligent-Tiering', 'Standard']]

### Policies
- **Type**: typing.Optional[str]

### DataType
- **Type**: typing.Optional[str]


# PutParameterResult

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### Tier
- **Type**: typing.Literal['Advanced', 'Intelligent-Tiering', 'Standard']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

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


# PutResourcePolicyResponse

### PolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterDefaultPatchBaselineRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterDefaultPatchBaselineResult

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterPatchBaselineForPatchGroupRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterPatchBaselineForPatchGroupResult

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### PatchGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterTargetWithMaintenanceWindowRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['INSTANCE', 'RESOURCE_GROUP']
- **Required**: Yes

### Targets
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]
- **Required**: Yes

### OwnerInformation
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# RegisterTargetWithMaintenanceWindowResult

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterTaskWithMaintenanceWindowRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### TaskParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpression, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutput]]]

### TaskInvocationParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskInvocationParameters, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskInvocationParametersOutput, NoneType]

### Priority
- **Type**: typing.Optional[int]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### LoggingInfo
- **Type**: <class 'NoneType'>

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### CutoffBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']]

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]


# RegisterTaskWithMaintenanceWindowResult

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# RegistrationMetadataItem

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# RelatedOpsItem

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsFromResourceRequest

### ResourceType
- **Type**: typing.Literal['Association', 'Automation', 'Document', 'MaintenanceWindow', 'ManagedInstance', 'OpsItem', 'OpsMetadata', 'Parameter', 'PatchBaseline']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# ResetServiceSettingRequest

### SettingId
- **Type**: <class 'str'>
- **Required**: Yes


# ResetServiceSettingResult

### ServiceSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ServiceSetting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# ResolvedTargets

### ParameterValues
- **Type**: typing.Optional[typing.List[str]]

### Truncated
- **Type**: typing.Optional[bool]


# ResourceComplianceSummaryItem

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ComplianceExecutionSummaryOutput]

### CompliantSummary
- **Type**: <class 'NoneType'>

### NonCompliantSummary
- **Type**: <class 'NoneType'>


# ResourceDataSyncAwsOrganizationsSource

### OrganizationSourceType
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncOrganizationalUnit]]


# ResourceDataSyncAwsOrganizationsSourceOutput

### OrganizationSourceType
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncOrganizationalUnit]]


# ResourceDataSyncDestinationDataSharing

### DestinationDataSharingType
- **Type**: typing.Optional[str]


# ResourceDataSyncItem

### SyncName
- **Type**: typing.Optional[str]

### SyncType
- **Type**: typing.Optional[str]

### SyncSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncSourceWithState]

### S3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncS3Destination]

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


# ResourceDataSyncOrganizationalUnit

### OrganizationalUnitId
- **Type**: typing.Optional[str]


# ResourceDataSyncS3Destination

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncDestinationDataSharing]


# ResourceDataSyncSource

### SourceType
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRegions
- **Type**: typing.List[str]
- **Required**: Yes

### AwsOrganizationsSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncAwsOrganizationsSource, aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncAwsOrganizationsSourceOutput, NoneType]

### IncludeFutureRegions
- **Type**: typing.Optional[bool]

### EnableAllOpsDataSources
- **Type**: typing.Optional[bool]


# ResourceDataSyncSourceWithState

### SourceType
- **Type**: typing.Optional[str]

### AwsOrganizationsSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncAwsOrganizationsSourceOutput]

### SourceRegions
- **Type**: typing.Optional[typing.List[str]]

### IncludeFutureRegions
- **Type**: typing.Optional[bool]

### State
- **Type**: typing.Optional[str]

### EnableAllOpsDataSources
- **Type**: typing.Optional[bool]


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


# ResultAttribute

### TypeName
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeSessionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# ResumeSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# ReviewInformation

### ReviewedTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['APPROVED', 'NOT_REVIEWED', 'PENDING', 'REJECTED']]

### Reviewer
- **Type**: typing.Optional[str]


# Runbook

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocation, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]]


# RunbookOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]


# S3OutputLocation

### OutputS3Region
- **Type**: typing.Optional[str]

### OutputS3BucketName
- **Type**: typing.Optional[str]

### OutputS3KeyPrefix
- **Type**: typing.Optional[str]


# S3OutputUrl

### OutputUrl
- **Type**: typing.Optional[str]


# ScheduledWindowExecution

### WindowId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ExecutionTime
- **Type**: typing.Optional[str]


# SendAutomationSignalRequest

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### SignalType
- **Type**: typing.Literal['Approve', 'Reject', 'Resume', 'StartStep', 'StopStep']
- **Required**: Yes

### Payload
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# SendCommandRequest

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.NotificationConfig, aws_resource_validator.pydantic_models.ssm.ssm_classes.NotificationConfigOutput, NoneType]

### CloudWatchOutputConfig
- **Type**: <class 'NoneType'>

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]


# SendCommandResult

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.Command'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# ServiceSetting

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


# Session

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.SessionManagerOutputUrl]

### MaxSessionDuration
- **Type**: typing.Optional[str]


# SessionFilter

### key
- **Type**: typing.Literal['InvokedAfter', 'InvokedBefore', 'Owner', 'SessionId', 'Status', 'Target']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SessionManagerOutputUrl

### S3OutputUrl
- **Type**: typing.Optional[str]

### CloudWatchOutputUrl
- **Type**: typing.Optional[str]


# SeveritySummary

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


# StartAssociationsOnceRequest

### AssociationIds
- **Type**: typing.List[str]
- **Required**: Yes


# StartAutomationExecutionRequest

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ClientToken
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['Auto', 'Interactive']]

### TargetParameterName
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### TargetLocations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocation, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]

### TargetLocationsURL
- **Type**: typing.Optional[str]


# StartAutomationExecutionResult

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# StartChangeRequestExecutionRequest

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### Runbooks
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Runbook, aws_resource_validator.pydantic_models.ssm.ssm_classes.RunbookOutput]]
- **Required**: Yes

### ScheduledTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DocumentVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### ChangeRequestName
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### AutoApprove
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.Tag]]

### ScheduledEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ChangeDetails
- **Type**: typing.Optional[str]


# StartChangeRequestExecutionResult

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# StartExecutionPreviewRequest

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]

### ExecutionInputs
- **Type**: <class 'NoneType'>


# StartExecutionPreviewResponse

### ExecutionPreviewId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# StartSessionRequest

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentName
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# StartSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# StepExecution

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
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### TargetLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]

### TriggeredAlarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmStateInformation]]

### ParentStepDetails
- **Type**: <class 'NoneType'>


# StepExecutionFilter

### Key
- **Type**: typing.Literal['Action', 'ParentStepExecutionId', 'ParentStepIteration', 'ParentStepIteratorValue', 'StartTimeAfter', 'StartTimeBefore', 'StepExecutionId', 'StepExecutionStatus', 'StepName']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StopAutomationExecutionRequest

### AutomationExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['Cancel', 'Complete']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# Target

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TargetLocation

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]

### IncludeChildOrganizationUnits
- **Type**: typing.Optional[bool]

### ExcludeAccounts
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### TargetsMaxConcurrency
- **Type**: typing.Optional[str]

### TargetsMaxErrors
- **Type**: typing.Optional[str]


# TargetLocationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput]

### IncludeChildOrganizationUnits
- **Type**: typing.Optional[bool]

### ExcludeAccounts
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]

### TargetsMaxConcurrency
- **Type**: typing.Optional[str]

### TargetsMaxErrors
- **Type**: typing.Optional[str]


# TargetOutput

### Key
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# TargetPreview

### Count
- **Type**: typing.Optional[int]

### TargetType
- **Type**: typing.Optional[str]


# TerminateSessionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateSessionResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UnlabelParameterVersionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Labels
- **Type**: typing.List[str]
- **Required**: Yes


# UnlabelParameterVersionResult

### RemovedLabels
- **Type**: typing.List[str]
- **Required**: Yes

### InvalidLabels
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssociationRequest

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### DocumentVersion
- **Type**: typing.Optional[str]

### ScheduleExpression
- **Type**: typing.Optional[str]

### OutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm.ssm_classes.InstanceAssociationOutputLocation]

### Name
- **Type**: typing.Optional[str]

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

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
- **Type**: typing.Optional[typing.List[str]]

### TargetLocations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocation, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetLocationOutput]]]

### ScheduleOffset
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[int]

### TargetMaps
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.List[str]]]]

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]


# UpdateAssociationResult

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssociationStatusRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationStatus
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationStatus, aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationStatusOutput]
- **Required**: Yes


# UpdateAssociationStatusResult

### AssociationDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AssociationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDocumentDefaultVersionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDocumentDefaultVersionResult

### Description
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentDefaultVersionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDocumentMetadataRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentReviews
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentReviews'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]


# UpdateDocumentRequest

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.AttachmentsSource]]

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


# UpdateDocumentResult

### DocumentDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.DocumentDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMaintenanceWindowRequest

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


# UpdateMaintenanceWindowResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMaintenanceWindowTargetRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### OwnerInformation
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Replace
- **Type**: typing.Optional[bool]


# UpdateMaintenanceWindowTargetResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMaintenanceWindowTaskRequest

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.Target, aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]]]

### TaskArn
- **Type**: typing.Optional[str]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### TaskParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpression, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutput]]]

### TaskInvocationParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskInvocationParameters, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskInvocationParametersOutput, NoneType]

### Priority
- **Type**: typing.Optional[int]

### MaxConcurrency
- **Type**: typing.Optional[str]

### MaxErrors
- **Type**: typing.Optional[str]

### LoggingInfo
- **Type**: <class 'NoneType'>

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Replace
- **Type**: typing.Optional[bool]

### CutoffBehavior
- **Type**: typing.Optional[typing.Literal['CANCEL_TASK', 'CONTINUE_TASK']]

### AlarmConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfiguration, aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput, NoneType]


# UpdateMaintenanceWindowTaskResult

### WindowId
- **Type**: <class 'str'>
- **Required**: Yes

### WindowTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.TargetOutput]
- **Required**: Yes

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskParameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskParameterValueExpressionOutput]
- **Required**: Yes

### TaskInvocationParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.MaintenanceWindowTaskInvocationParametersOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.LoggingInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.AlarmConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateManagedInstanceRoleRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IamRole
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOpsItemRequest

### OpsItemId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OperationalData
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemDataValue]]

### OperationalDataToDelete
- **Type**: typing.Optional[typing.List[str]]

### Notifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.OpsItemNotification]]

### Priority
- **Type**: typing.Optional[int]

### RelatedOpsItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.RelatedOpsItem]]

### Status
- **Type**: typing.Optional[typing.Literal['Approved', 'Cancelled', 'Cancelling', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'Closed', 'CompletedWithFailure', 'CompletedWithSuccess', 'Failed', 'InProgress', 'Open', 'Pending', 'PendingApproval', 'PendingChangeCalendarOverride', 'Rejected', 'Resolved', 'RunbookInProgress', 'Scheduled', 'TimedOut']]

### Title
- **Type**: typing.Optional[str]

### Category
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[str]

### ActualStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ActualEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PlannedStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PlannedEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### OpsItemArn
- **Type**: typing.Optional[str]


# UpdateOpsMetadataRequest

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetadataToUpdate
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.ssm.ssm_classes.MetadataValue]]

### KeysToDelete
- **Type**: typing.Optional[typing.List[str]]


# UpdateOpsMetadataResult

### OpsMetadataArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePatchBaselineRequest

### BaselineId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### GlobalFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput, NoneType]

### ApprovalRules
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroup, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroupOutput, NoneType]

### ApprovedPatches
- **Type**: typing.Optional[typing.List[str]]

### ApprovedPatchesComplianceLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNSPECIFIED']]

### ApprovedPatchesEnableNonSecurity
- **Type**: typing.Optional[bool]

### RejectedPatches
- **Type**: typing.Optional[typing.List[str]]

### RejectedPatchesAction
- **Type**: typing.Optional[typing.Literal['ALLOW_AS_DEPENDENCY', 'BLOCK']]

### Description
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSource, aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSourceOutput]]]

### Replace
- **Type**: typing.Optional[bool]


# UpdatePatchBaselineResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchFilterGroupOutput'>
- **Required**: Yes

### ApprovalRules
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchRuleGroupOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm.ssm_classes.PatchSourceOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResourceDataSyncRequest

### SyncName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: <class 'str'>
- **Required**: Yes

### SyncSource
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm.ssm_classes.ResourceDataSyncSource'>
- **Required**: Yes


# UpdateServiceSettingRequest

### SettingId
- **Type**: <class 'str'>
- **Required**: Yes

### SettingValue
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


