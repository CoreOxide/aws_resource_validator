# Backup Classes

# AdvancedBackupSetting

### ResourceType
- **Type**: typing.Optional[str]

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# AdvancedBackupSettingOutput

### ResourceType
- **Type**: typing.Optional[str]

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# BackupJob

### AccountId
- **Type**: typing.Optional[str]

### BackupJobId
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### BackupVaultArn
- **Type**: typing.Optional[str]

### RecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CompletionDate
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']]

### StatusMessage
- **Type**: typing.Optional[str]

### PercentDone
- **Type**: typing.Optional[str]

### BackupSizeInBytes
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointCreator]

### ExpectedCompletionDate
- **Type**: typing.Optional[datetime.datetime]

### StartBy
- **Type**: typing.Optional[datetime.datetime]

### ResourceType
- **Type**: typing.Optional[str]

### BytesTransferred
- **Type**: typing.Optional[int]

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### BackupType
- **Type**: typing.Optional[str]

### ParentJobId
- **Type**: typing.Optional[str]

### IsParent
- **Type**: typing.Optional[bool]

### ResourceName
- **Type**: typing.Optional[str]

### InitiationDate
- **Type**: typing.Optional[datetime.datetime]

### MessageCategory
- **Type**: typing.Optional[str]


# BackupJobSummary

### Region
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'AGGREGATE_ALL', 'ANY', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']]

### ResourceType
- **Type**: typing.Optional[str]

### MessageCategory
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# BackupPlan

### BackupPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupRule]
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSettingOutput]]


# BackupPlanInput

### BackupPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupRuleInput]
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSetting, aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSettingOutput]]]


# BackupPlanTemplatesListMember

### BackupPlanTemplateId
- **Type**: typing.Optional[str]

### BackupPlanTemplateName
- **Type**: typing.Optional[str]


# BackupPlansListMember

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### DeletionDate
- **Type**: typing.Optional[datetime.datetime]

### VersionId
- **Type**: typing.Optional[str]

### BackupPlanName
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### LastExecutionDate
- **Type**: typing.Optional[datetime.datetime]

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSettingOutput]]


# BackupRule

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### Lifecycle
- **Type**: <class 'NoneType'>

### RecoveryPointTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RuleId
- **Type**: typing.Optional[str]

### CopyActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.CopyAction]]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### IndexActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.IndexActionOutput]]


# BackupRuleInput

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### CompletionWindowMinutes
- **Type**: typing.Optional[int]

### Lifecycle
- **Type**: <class 'NoneType'>

### RecoveryPointTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### CopyActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.CopyAction]]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### IndexActions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.IndexAction, aws_resource_validator.pydantic_models.backup.backup_classes.IndexActionOutput]]]


# BackupSelection

### SelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.List[str]]

### ListOfTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.Condition]]

### NotResources
- **Type**: typing.Optional[typing.List[str]]

### Conditions
- **Type**: <class 'NoneType'>


# BackupSelectionOutput

### SelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.List[str]]

### ListOfTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.Condition]]

### NotResources
- **Type**: typing.Optional[typing.List[str]]

### Conditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionsOutput]


# BackupSelectionsListMember

### SelectionId
- **Type**: typing.Optional[str]

### SelectionName
- **Type**: typing.Optional[str]

### BackupPlanId
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CreatorRequestId
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# BackupVaultListMember

### BackupVaultName
- **Type**: typing.Optional[str]

### BackupVaultArn
- **Type**: typing.Optional[str]

### VaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### VaultState
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'FAILED']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]

### NumberOfRecoveryPoints
- **Type**: typing.Optional[int]

### Locked
- **Type**: typing.Optional[bool]

### MinRetentionDays
- **Type**: typing.Optional[int]

### MaxRetentionDays
- **Type**: typing.Optional[int]

### LockDate
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CalculatedLifecycle

### MoveToColdStorageAt
- **Type**: typing.Optional[datetime.datetime]

### DeleteAt
- **Type**: typing.Optional[datetime.datetime]


# CancelLegalHoldInput

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### CancelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### RetainRecordInDays
- **Type**: typing.Optional[int]


# Condition

### ConditionType
- **Type**: typing.Literal['STRINGEQUALS']
- **Required**: Yes

### ConditionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ConditionValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConditionParameter

### ConditionKey
- **Type**: typing.Optional[str]

### ConditionValue
- **Type**: typing.Optional[str]


# Conditions

### StringEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]

### StringNotEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]

### StringLike
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]

### StringNotLike
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]


# ConditionsOutput

### StringEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]

### StringNotEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]

### StringLike
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]

### StringNotLike
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ConditionParameter]]


# ControlInputParameter

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# ControlScope

### ComplianceResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ControlScopeOutput

### ComplianceResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CopyAction

### DestinationBackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: <class 'NoneType'>


# CopyJob

### AccountId
- **Type**: typing.Optional[str]

### CopyJobId
- **Type**: typing.Optional[str]

### SourceBackupVaultArn
- **Type**: typing.Optional[str]

### SourceRecoveryPointArn
- **Type**: typing.Optional[str]

### DestinationBackupVaultArn
- **Type**: typing.Optional[str]

### DestinationRecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CompletionDate
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PARTIAL', 'RUNNING']]

### StatusMessage
- **Type**: typing.Optional[str]

### BackupSizeInBytes
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointCreator]

### ResourceType
- **Type**: typing.Optional[str]

### ParentJobId
- **Type**: typing.Optional[str]

### IsParent
- **Type**: typing.Optional[bool]

### CompositeMemberIdentifier
- **Type**: typing.Optional[str]

### NumberOfChildJobs
- **Type**: typing.Optional[int]

### ChildJobsInState
- **Type**: typing.Optional[typing.Dict[typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PARTIAL', 'RUNNING'], int]]

### ResourceName
- **Type**: typing.Optional[str]

### MessageCategory
- **Type**: typing.Optional[str]


# CopyJobSummary

### Region
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'AGGREGATE_ALL', 'ANY', 'COMPLETED', 'COMPLETING', 'CREATED', 'FAILED', 'FAILING', 'PARTIAL', 'RUNNING']]

### ResourceType
- **Type**: typing.Optional[str]

### MessageCategory
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# CreateBackupPlanInput

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlanInput'>
- **Required**: Yes

### BackupPlanTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateBackupPlanOutput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSettingOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackupSelectionInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupSelection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.BackupSelection, aws_resource_validator.pydantic_models.backup.backup_classes.BackupSelectionOutput]
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateBackupSelectionOutput

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackupVaultInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateBackupVaultOutput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFrameworkInput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkControls
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.FrameworkControl, aws_resource_validator.pydantic_models.backup.backup_classes.FrameworkControlOutput]]
- **Required**: Yes

### FrameworkDescription
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]

### FrameworkTags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateFrameworkOutput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLegalHoldInput

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]

### RecoveryPointSelection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointSelection, aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointSelectionOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLegalHoldOutput

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'CANCELING', 'CREATING']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### LegalHoldArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RecoveryPointSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointSelectionOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLogicallyAirGappedBackupVaultInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### MinRetentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### MaxRetentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### BackupVaultTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateLogicallyAirGappedBackupVaultOutput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VaultState
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReportPlanInput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportDeliveryChannel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ReportDeliveryChannel, aws_resource_validator.pydantic_models.backup.backup_classes.ReportDeliveryChannelOutput]
- **Required**: Yes

### ReportSetting
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ReportSetting, aws_resource_validator.pydantic_models.backup.backup_classes.ReportSettingOutput]
- **Required**: Yes

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportPlanTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateReportPlanOutput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRestoreTestingPlanInput

### RestoreTestingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingPlanForCreate'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRestoreTestingPlanOutput

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RestoreTestingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRestoreTestingSelectionInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingSelectionForCreate'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateRestoreTestingSelectionOutput

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RestoreTestingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DateRange

### FromDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DateRangeOutput

### FromDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ToDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DeleteBackupPlanInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupPlanOutput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackupSelectionInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultAccessPolicyInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultLockConfigurationInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultNotificationsInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFrameworkInput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryPointInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportPlanInput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestoreTestingPlanInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestoreTestingSelectionInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBackupJobInput

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBackupJobOutput

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ABORTED', 'ABORTING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### PercentDone
- **Type**: <class 'str'>
- **Required**: Yes

### BackupSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointCreator'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### BytesTransferred
- **Type**: <class 'int'>
- **Required**: Yes

### ExpectedCompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartBy
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BackupOptions
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### BackupType
- **Type**: <class 'str'>
- **Required**: Yes

### ParentJobId
- **Type**: <class 'str'>
- **Required**: Yes

### IsParent
- **Type**: <class 'bool'>
- **Required**: Yes

### NumberOfChildJobs
- **Type**: <class 'int'>
- **Required**: Yes

### ChildJobsInState
- **Type**: typing.Dict[typing.Literal['ABORTED', 'ABORTING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING'], int]
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### InitiationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MessageCategory
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBackupVaultInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# DescribeBackupVaultOutput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### VaultType
- **Type**: typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']
- **Required**: Yes

### VaultState
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'FAILED']
- **Required**: Yes

### EncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfRecoveryPoints
- **Type**: <class 'int'>
- **Required**: Yes

### Locked
- **Type**: <class 'bool'>
- **Required**: Yes

### MinRetentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### MaxRetentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### LockDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCopyJobInput

### CopyJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCopyJobOutput

### CopyJob
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.CopyJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFrameworkInput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFrameworkOutput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkDescription
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.FrameworkControlOutput]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeploymentStatus
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkStatus
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGlobalSettingsOutput

### GlobalSettings
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProtectedResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProtectedResourceOutput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### LastBackupTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### LastBackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastRecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRestoreExecutionTimeMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### LatestRestoreJobCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestRestoreRecoveryPointCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecoveryPointInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# DescribeRecoveryPointOutput

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceBackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointCreator'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETING', 'EXPIRED', 'PARTIAL']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BackupSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### CalculatedLifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.CalculatedLifecycle'>
- **Required**: Yes

### Lifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.Lifecycle'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### IsEncrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### StorageClass
- **Type**: typing.Literal['COLD', 'DELETED', 'WARM']
- **Required**: Yes

### LastRestoreTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ParentRecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CompositeMemberIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### IsParent
- **Type**: <class 'bool'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### VaultType
- **Type**: typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']
- **Required**: Yes

### IndexStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### IndexStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRegionSettingsOutput

### ResourceTypeOptInPreference
- **Type**: typing.Dict[str, bool]
- **Required**: Yes

### ResourceTypeManagementPreference
- **Type**: typing.Dict[str, bool]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReportJobInput

### ReportJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReportJobOutput

### ReportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ReportJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReportPlanInput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReportPlanOutput

### ReportPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ReportPlan'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRestoreJobInput

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRestoreJobOutput

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### PercentDone
- **Type**: <class 'str'>
- **Required**: Yes

### BackupSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpectedCompletionTimeMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### CreatedResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreJobCreator'>
- **Required**: Yes

### ValidationStatus
- **Type**: typing.Literal['FAILED', 'SUCCESSFUL', 'TIMED_OUT', 'VALIDATING']
- **Required**: Yes

### ValidationStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionStatus
- **Type**: typing.Literal['DELETING', 'FAILED', 'SUCCESSFUL']
- **Required**: Yes

### DeletionStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateRecoveryPointFromParentInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRecoveryPointInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# ExportBackupPlanTemplateInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportBackupPlanTemplateOutput

### BackupPlanTemplateJson
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# Framework

### FrameworkName
- **Type**: typing.Optional[str]

### FrameworkArn
- **Type**: typing.Optional[str]

### FrameworkDescription
- **Type**: typing.Optional[str]

### NumberOfControls
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### DeploymentStatus
- **Type**: typing.Optional[str]


# FrameworkControl

### ControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ControlInputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ControlInputParameter]]

### ControlScope
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ControlScope, aws_resource_validator.pydantic_models.backup.backup_classes.ControlScopeOutput, NoneType]


# FrameworkControlOutput

### ControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ControlInputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ControlInputParameter]]

### ControlScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.ControlScopeOutput]


# GetBackupPlanFromJSONInput

### BackupPlanTemplateJson
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupPlanFromJSONOutput

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlan'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackupPlanFromTemplateInput

### BackupPlanTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupPlanFromTemplateOutput

### BackupPlanDocument
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlan'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackupPlanInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# GetBackupPlanOutput

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlan'>
- **Required**: Yes

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastExecutionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSettingOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackupSelectionInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupSelectionOutput

### BackupSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.BackupSelectionOutput'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatorRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackupVaultAccessPolicyInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupVaultAccessPolicyOutput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackupVaultNotificationsInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupVaultNotificationsOutput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultEvents
- **Type**: typing.List[typing.Literal['BACKUP_JOB_COMPLETED', 'BACKUP_JOB_EXPIRED', 'BACKUP_JOB_FAILED', 'BACKUP_JOB_STARTED', 'BACKUP_JOB_SUCCESSFUL', 'BACKUP_PLAN_CREATED', 'BACKUP_PLAN_MODIFIED', 'COPY_JOB_FAILED', 'COPY_JOB_STARTED', 'COPY_JOB_SUCCESSFUL', 'RECOVERY_POINT_MODIFIED', 'RESTORE_JOB_COMPLETED', 'RESTORE_JOB_FAILED', 'RESTORE_JOB_STARTED', 'RESTORE_JOB_SUCCESSFUL', 'S3_BACKUP_OBJECT_FAILED', 'S3_RESTORE_OBJECT_FAILED']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetLegalHoldInput

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLegalHoldOutput

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CANCELED', 'CANCELING', 'CREATING']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CancelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### LegalHoldArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CancellationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RetainRecordUntil
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RecoveryPointSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointSelectionOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecoveryPointIndexDetailsInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecoveryPointIndexDetailsOutput

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IndexDeletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IndexCompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IndexStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### IndexStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### TotalItemsIndexed
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecoveryPointRestoreMetadataInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# GetRecoveryPointRestoreMetadataOutput

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetRestoreJobMetadataInput

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestoreJobMetadataOutput

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetRestoreTestingInferredMetadataInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# GetRestoreTestingInferredMetadataOutput

### InferredMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetRestoreTestingPlanInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestoreTestingPlanOutput

### RestoreTestingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingPlanForGet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetRestoreTestingSelectionInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestoreTestingSelectionOutput

### RestoreTestingSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingSelectionForGet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# GetSupportedResourceTypesOutput

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# IndexAction

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]


# IndexActionOutput

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]


# IndexedRecoveryPoint

### RecoveryPointArn
- **Type**: typing.Optional[str]

### SourceResourceArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]

### BackupCreationDate
- **Type**: typing.Optional[datetime.datetime]

### ResourceType
- **Type**: typing.Optional[str]

### IndexCreationDate
- **Type**: typing.Optional[datetime.datetime]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### IndexStatusMessage
- **Type**: typing.Optional[str]

### BackupVaultArn
- **Type**: typing.Optional[str]


# KeyValue

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# LegalHold

### Title
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CANCELED', 'CANCELING', 'CREATING']]

### Description
- **Type**: typing.Optional[str]

### LegalHoldId
- **Type**: typing.Optional[str]

### LegalHoldArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CancellationDate
- **Type**: typing.Optional[datetime.datetime]


# Lifecycle

### MoveToColdStorageAfterDays
- **Type**: typing.Optional[int]

### DeleteAfterDays
- **Type**: typing.Optional[int]

### OptInToArchiveForSupportedResources
- **Type**: typing.Optional[bool]


# ListBackupJobSummariesInput

### AccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'AGGREGATE_ALL', 'ANY', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']]

### ResourceType
- **Type**: typing.Optional[str]

### MessageCategory
- **Type**: typing.Optional[str]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['FOURTEEN_DAYS', 'ONE_DAY', 'SEVEN_DAYS']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBackupJobSummariesOutput

### BackupJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupJobSummary]
- **Required**: Yes

### AggregationPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupJobsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']]

### ByBackupVaultName
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByResourceType
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCompleteBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]


# ListBackupJobsInputPaginate

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']]

### ByBackupVaultName
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByResourceType
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCompleteBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListBackupJobsOutput

### BackupJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupPlanTemplatesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupPlanTemplatesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListBackupPlanTemplatesOutput

### BackupPlanTemplatesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlanTemplatesListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupPlanVersionsInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupPlanVersionsInputPaginate

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListBackupPlanVersionsOutput

### BackupPlanVersionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlansListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupPlansInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeDeleted
- **Type**: typing.Optional[bool]


# ListBackupPlansInputPaginate

### IncludeDeleted
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListBackupPlansOutput

### BackupPlansList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlansListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupSelectionsInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupSelectionsInputPaginate

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListBackupSelectionsOutput

### BackupSelectionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupSelectionsListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupVaultsInput

### ByVaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### ByShared
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupVaultsInputPaginate

### ByVaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### ByShared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListBackupVaultsOutput

### BackupVaultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.BackupVaultListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCopyJobSummariesInput

### AccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'AGGREGATE_ALL', 'ANY', 'COMPLETED', 'COMPLETING', 'CREATED', 'FAILED', 'FAILING', 'PARTIAL', 'RUNNING']]

### ResourceType
- **Type**: typing.Optional[str]

### MessageCategory
- **Type**: typing.Optional[str]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['FOURTEEN_DAYS', 'ONE_DAY', 'SEVEN_DAYS']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCopyJobSummariesOutput

### CopyJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.CopyJobSummary]
- **Required**: Yes

### AggregationPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCopyJobsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PARTIAL', 'RUNNING']]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByResourceType
- **Type**: typing.Optional[str]

### ByDestinationVaultArn
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCompleteAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]


# ListCopyJobsInputPaginate

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PARTIAL', 'RUNNING']]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByResourceType
- **Type**: typing.Optional[str]

### ByDestinationVaultArn
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCompleteAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListCopyJobsOutput

### CopyJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.CopyJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFrameworksInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFrameworksOutput

### Frameworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.Framework]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndexedRecoveryPointsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SourceResourceArn
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ResourceType
- **Type**: typing.Optional[str]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# ListIndexedRecoveryPointsInputPaginate

### SourceResourceArn
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ResourceType
- **Type**: typing.Optional[str]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListIndexedRecoveryPointsOutput

### IndexedRecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.IndexedRecoveryPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLegalHoldsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLegalHoldsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListLegalHoldsOutput

### LegalHolds
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.LegalHold]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectedResourcesByBackupVaultInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectedResourcesByBackupVaultInputPaginate

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListProtectedResourcesByBackupVaultOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectedResourcesInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectedResourcesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListProtectedResourcesOutput

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsByBackupVaultInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ByResourceArn
- **Type**: typing.Optional[str]

### ByResourceType
- **Type**: typing.Optional[str]

### ByBackupPlanId
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByParentRecoveryPointArn
- **Type**: typing.Optional[str]


# ListRecoveryPointsByBackupVaultInputPaginate

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### ByResourceArn
- **Type**: typing.Optional[str]

### ByResourceType
- **Type**: typing.Optional[str]

### ByBackupPlanId
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByParentRecoveryPointArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRecoveryPointsByBackupVaultOutput

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointByBackupVault]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsByLegalHoldInput

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRecoveryPointsByLegalHoldInputPaginate

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRecoveryPointsByLegalHoldOutput

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsByResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ManagedByAWSBackupOnly
- **Type**: typing.Optional[bool]


# ListRecoveryPointsByResourceInputPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedByAWSBackupOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRecoveryPointsByResourceOutput

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointByResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReportJobsInput

### ByReportPlanName
- **Type**: typing.Optional[str]

### ByCreationBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreationAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByStatus
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReportJobsOutput

### ReportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ReportJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReportPlansInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReportPlansOutput

### ReportPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.ReportPlan]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobSummariesInput

### AccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'AGGREGATE_ALL', 'ANY', 'COMPLETED', 'CREATED', 'FAILED', 'PENDING', 'RUNNING']]

### ResourceType
- **Type**: typing.Optional[str]

### AggregationPeriod
- **Type**: typing.Optional[typing.Literal['FOURTEEN_DAYS', 'ONE_DAY', 'SEVEN_DAYS']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobSummariesOutput

### RestoreJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreJobSummary]
- **Required**: Yes

### AggregationPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobsByProtectedResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByRecoveryPointCreationDateAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByRecoveryPointCreationDateBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRestoreJobsByProtectedResourceInputPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByRecoveryPointCreationDateAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByRecoveryPointCreationDateBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRestoreJobsByProtectedResourceOutput

### RestoreJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreJobsListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ByAccountId
- **Type**: typing.Optional[str]

### ByResourceType
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByCompleteBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCompleteAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByRestoreTestingPlanArn
- **Type**: typing.Optional[str]


# ListRestoreJobsInputPaginate

### ByAccountId
- **Type**: typing.Optional[str]

### ByResourceType
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByCompleteBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByCompleteAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ByRestoreTestingPlanArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRestoreJobsOutput

### RestoreJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreJobsListMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingPlansInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingPlansInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRestoreTestingPlansOutput

### RestoreTestingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingPlanForList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingSelectionsInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingSelectionsInputPaginate

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.PaginatorConfig]


# ListRestoreTestingSelectionsOutput

### RestoreTestingSelections
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingSelectionForList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProtectedResource

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### LastBackupTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceName
- **Type**: typing.Optional[str]

### LastBackupVaultArn
- **Type**: typing.Optional[str]

### LastRecoveryPointArn
- **Type**: typing.Optional[str]


# ProtectedResourceConditions

### StringEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.KeyValue]]

### StringNotEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.KeyValue]]


# ProtectedResourceConditionsOutput

### StringEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.KeyValue]]

### StringNotEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.KeyValue]]


# PutBackupVaultAccessPolicyInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: typing.Optional[str]


# PutBackupVaultLockConfigurationInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### MinRetentionDays
- **Type**: typing.Optional[int]

### MaxRetentionDays
- **Type**: typing.Optional[int]

### ChangeableForDays
- **Type**: typing.Optional[int]


# PutBackupVaultNotificationsInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultEvents
- **Type**: typing.List[typing.Literal['BACKUP_JOB_COMPLETED', 'BACKUP_JOB_EXPIRED', 'BACKUP_JOB_FAILED', 'BACKUP_JOB_STARTED', 'BACKUP_JOB_SUCCESSFUL', 'BACKUP_PLAN_CREATED', 'BACKUP_PLAN_MODIFIED', 'COPY_JOB_FAILED', 'COPY_JOB_STARTED', 'COPY_JOB_SUCCESSFUL', 'RECOVERY_POINT_MODIFIED', 'RESTORE_JOB_COMPLETED', 'RESTORE_JOB_FAILED', 'RESTORE_JOB_STARTED', 'RESTORE_JOB_SUCCESSFUL', 'S3_BACKUP_OBJECT_FAILED', 'S3_RESTORE_OBJECT_FAILED']]
- **Required**: Yes


# PutRestoreValidationResultInput

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationStatus
- **Type**: typing.Literal['FAILED', 'SUCCESSFUL', 'TIMED_OUT', 'VALIDATING']
- **Required**: Yes

### ValidationStatusMessage
- **Type**: typing.Optional[str]


# RecoveryPointByBackupVault

### RecoveryPointArn
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]

### BackupVaultArn
- **Type**: typing.Optional[str]

### SourceBackupVaultArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.RecoveryPointCreator]

### IamRoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETING', 'EXPIRED', 'PARTIAL']]

### StatusMessage
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CompletionDate
- **Type**: typing.Optional[datetime.datetime]

### BackupSizeInBytes
- **Type**: typing.Optional[int]

### CalculatedLifecycle
- **Type**: <class 'NoneType'>

### Lifecycle
- **Type**: <class 'NoneType'>

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### IsEncrypted
- **Type**: typing.Optional[bool]

### LastRestoreTime
- **Type**: typing.Optional[datetime.datetime]

### ParentRecoveryPointArn
- **Type**: typing.Optional[str]

### CompositeMemberIdentifier
- **Type**: typing.Optional[str]

### IsParent
- **Type**: typing.Optional[bool]

### ResourceName
- **Type**: typing.Optional[str]

### VaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### IndexStatusMessage
- **Type**: typing.Optional[str]


# RecoveryPointByResource

### RecoveryPointArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETING', 'EXPIRED', 'PARTIAL']]

### StatusMessage
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### BackupSizeBytes
- **Type**: typing.Optional[int]

### BackupVaultName
- **Type**: typing.Optional[str]

### IsParent
- **Type**: typing.Optional[bool]

### ParentRecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]

### VaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### IndexStatusMessage
- **Type**: typing.Optional[str]


# RecoveryPointCreator

### BackupPlanId
- **Type**: typing.Optional[str]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanVersion
- **Type**: typing.Optional[str]

### BackupRuleId
- **Type**: typing.Optional[str]


# RecoveryPointMember

### RecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]


# RecoveryPointSelection

### VaultNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DateRange
- **Type**: <class 'NoneType'>


# RecoveryPointSelectionOutput

### VaultNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.DateRangeOutput]


# ReportDeliveryChannel

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]

### Formats
- **Type**: typing.Optional[typing.List[str]]


# ReportDeliveryChannelOutput

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]

### Formats
- **Type**: typing.Optional[typing.List[str]]


# ReportDestination

### S3BucketName
- **Type**: typing.Optional[str]

### S3Keys
- **Type**: typing.Optional[typing.List[str]]


# ReportJob

### ReportJobId
- **Type**: typing.Optional[str]

### ReportPlanArn
- **Type**: typing.Optional[str]

### ReportTemplate
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### ReportDestination
- **Type**: <class 'NoneType'>


# ReportPlan

### ReportPlanArn
- **Type**: typing.Optional[str]

### ReportPlanName
- **Type**: typing.Optional[str]

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.ReportSettingOutput]

### ReportDeliveryChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.ReportDeliveryChannelOutput]

### DeploymentStatus
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastAttemptedExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulExecutionTime
- **Type**: typing.Optional[datetime.datetime]


# ReportSetting

### ReportTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArns
- **Type**: typing.Optional[typing.List[str]]

### NumberOfFrameworks
- **Type**: typing.Optional[int]

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### OrganizationUnits
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# ReportSettingOutput

### ReportTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArns
- **Type**: typing.Optional[typing.List[str]]

### NumberOfFrameworks
- **Type**: typing.Optional[int]

### Accounts
- **Type**: typing.Optional[typing.List[str]]

### OrganizationUnits
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]


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


# RestoreJobCreator

### RestoreTestingPlanArn
- **Type**: typing.Optional[str]


# RestoreJobSummary

### Region
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ABORTED', 'AGGREGATE_ALL', 'ANY', 'COMPLETED', 'CREATED', 'FAILED', 'PENDING', 'RUNNING']]

### ResourceType
- **Type**: typing.Optional[str]

### Count
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# RestoreJobsListMember

### AccountId
- **Type**: typing.Optional[str]

### RestoreJobId
- **Type**: typing.Optional[str]

### RecoveryPointArn
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### CompletionDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### StatusMessage
- **Type**: typing.Optional[str]

### PercentDone
- **Type**: typing.Optional[str]

### BackupSizeInBytes
- **Type**: typing.Optional[int]

### IamRoleArn
- **Type**: typing.Optional[str]

### ExpectedCompletionTimeMinutes
- **Type**: typing.Optional[int]

### CreatedResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### RecoveryPointCreationDate
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreJobCreator]

### ValidationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCESSFUL', 'TIMED_OUT', 'VALIDATING']]

### ValidationStatusMessage
- **Type**: typing.Optional[str]

### DeletionStatus
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'SUCCESSFUL']]

### DeletionStatusMessage
- **Type**: typing.Optional[str]


# RestoreTestingPlanForCreate

### RecoveryPointSelection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingRecoveryPointSelection, aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingRecoveryPointSelectionOutput]
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingPlanForGet

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RecoveryPointSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingRecoveryPointSelectionOutput'>
- **Required**: Yes

### RestoreTestingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### LastExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingPlanForList

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RestoreTestingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### LastExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingPlanForUpdate

### RecoveryPointSelection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingRecoveryPointSelection, aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingRecoveryPointSelectionOutput, NoneType]

### ScheduleExpression
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingRecoveryPointSelection

### Algorithm
- **Type**: typing.Optional[typing.Literal['LATEST_WITHIN_WINDOW', 'RANDOM_WITHIN_WINDOW']]

### ExcludeVaults
- **Type**: typing.Optional[typing.List[str]]

### IncludeVaults
- **Type**: typing.Optional[typing.List[str]]

### RecoveryPointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CONTINUOUS', 'SNAPSHOT']]]

### SelectionWindowDays
- **Type**: typing.Optional[int]


# RestoreTestingRecoveryPointSelectionOutput

### Algorithm
- **Type**: typing.Optional[typing.Literal['LATEST_WITHIN_WINDOW', 'RANDOM_WITHIN_WINDOW']]

### ExcludeVaults
- **Type**: typing.Optional[typing.List[str]]

### IncludeVaults
- **Type**: typing.Optional[typing.List[str]]

### RecoveryPointTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CONTINUOUS', 'SNAPSHOT']]]

### SelectionWindowDays
- **Type**: typing.Optional[int]


# RestoreTestingSelectionForCreate

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ProtectedResourceConditions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResourceConditions, aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResourceConditionsOutput, NoneType]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingSelectionForGet

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### ProtectedResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ProtectedResourceConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResourceConditionsOutput]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingSelectionForList

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProtectedResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingSelectionForUpdate

### IamRoleArn
- **Type**: typing.Optional[str]

### ProtectedResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ProtectedResourceConditions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResourceConditions, aws_resource_validator.pydantic_models.backup.backup_classes.ProtectedResourceConditionsOutput, NoneType]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# StartBackupJobInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]

### StartWindowMinutes
- **Type**: typing.Optional[int]

### CompleteWindowMinutes
- **Type**: typing.Optional[int]

### Lifecycle
- **Type**: <class 'NoneType'>

### RecoveryPointTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### Index
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StartBackupJobOutput

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IsParent
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# StartCopyJobInput

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceBackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationBackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: <class 'NoneType'>


# StartCopyJobOutput

### CopyJobId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IsParent
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# StartReportJobInput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]


# StartReportJobOutput

### ReportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# StartRestoreJobInput

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### IamRoleArn
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### CopySourceTagsToRestoredResource
- **Type**: typing.Optional[bool]


# StartRestoreJobOutput

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# StopBackupJobInput

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBackupPlanInput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.BackupPlanInput'>
- **Required**: Yes


# UpdateBackupPlanOutput

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup.backup_classes.AdvancedBackupSettingOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFrameworkInput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkDescription
- **Type**: typing.Optional[str]

### FrameworkControls
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.FrameworkControl, aws_resource_validator.pydantic_models.backup.backup_classes.FrameworkControlOutput]]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# UpdateFrameworkOutput

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGlobalSettingsInput

### GlobalSettings
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateRecoveryPointIndexSettingsInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Index
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### IamRoleArn
- **Type**: typing.Optional[str]


# UpdateRecoveryPointIndexSettingsOutput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### IndexStatus
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']
- **Required**: Yes

### Index
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecoveryPointLifecycleInput

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: <class 'NoneType'>


# UpdateRecoveryPointLifecycleOutput

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.Lifecycle'>
- **Required**: Yes

### CalculatedLifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.CalculatedLifecycle'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRegionSettingsInput

### ResourceTypeOptInPreference
- **Type**: typing.Optional[typing.Dict[str, bool]]

### ResourceTypeManagementPreference
- **Type**: typing.Optional[typing.Dict[str, bool]]


# UpdateReportPlanInput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportDeliveryChannel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ReportDeliveryChannel, aws_resource_validator.pydantic_models.backup.backup_classes.ReportDeliveryChannelOutput, NoneType]

### ReportSetting
- **Type**: typing.Union[aws_resource_validator.pydantic_models.backup.backup_classes.ReportSetting, aws_resource_validator.pydantic_models.backup.backup_classes.ReportSettingOutput, NoneType]

### IdempotencyToken
- **Type**: typing.Optional[str]


# UpdateReportPlanOutput

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRestoreTestingPlanInput

### RestoreTestingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingPlanForUpdate'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRestoreTestingPlanOutput

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RestoreTestingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRestoreTestingSelectionInput

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.RestoreTestingSelectionForUpdate'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRestoreTestingSelectionOutput

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RestoreTestingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup.backup_classes.ResponseMetadata'>
- **Required**: Yes


