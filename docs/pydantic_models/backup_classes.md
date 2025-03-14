# Backup Classes

# AdvancedBackupSettingOutputTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# AdvancedBackupSettingTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### BackupOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdvancedBackupSettingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BackupJobSummaryTypeDef

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


# BackupJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointCreatorTypeDef]

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


# BackupPlanInputTypeDef

### BackupPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.BackupRuleInputTypeDef]
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingUnionTypeDef]]


# BackupPlanTemplatesListMemberTypeDef

### BackupPlanTemplateId
- **Type**: typing.Optional[str]

### BackupPlanTemplateName
- **Type**: typing.Optional[str]


# BackupPlanTypeDef

### BackupPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupRuleTypeDef]
- **Required**: Yes

### AdvancedBackupSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingOutputTypeDef]]


# BackupPlansListMemberTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingOutputTypeDef]]


# BackupRuleInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]

### RecoveryPointTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CopyActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.CopyActionTypeDef]]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### IndexActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.IndexActionUnionTypeDef]]


# BackupRuleTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]

### RecoveryPointTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### RuleId
- **Type**: typing.Optional[str]

### CopyActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.CopyActionTypeDef]]

### EnableContinuousBackup
- **Type**: typing.Optional[bool]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### IndexActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.IndexActionOutputTypeDef]]


# BackupSelectionOutputTypeDef

### SelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.List[str]]

### ListOfTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.ConditionTypeDef]]

### NotResources
- **Type**: typing.Optional[typing.List[str]]

### Conditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ConditionsOutputTypeDef]


# BackupSelectionTypeDef

### SelectionName
- **Type**: <class 'str'>
- **Required**: Yes

### IamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### ListOfTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ConditionTypeDef]]

### NotResources
- **Type**: typing.Optional[typing.Sequence[str]]

### Conditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ConditionsTypeDef]


# BackupSelectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BackupSelectionsListMemberTypeDef

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


# BackupVaultListMemberTypeDef

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

# CalculatedLifecycleTypeDef

### MoveToColdStorageAt
- **Type**: typing.Optional[datetime.datetime]

### DeleteAt
- **Type**: typing.Optional[datetime.datetime]


# CancelLegalHoldInputTypeDef

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### CancelDescription
- **Type**: <class 'str'>
- **Required**: Yes

### RetainRecordInDays
- **Type**: typing.Optional[int]


# ConditionParameterTypeDef

### ConditionKey
- **Type**: typing.Optional[str]

### ConditionValue
- **Type**: typing.Optional[str]


# ConditionTypeDef

### ConditionType
- **Type**: typing.Literal['STRINGEQUALS']
- **Required**: Yes

### ConditionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ConditionValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConditionsOutputTypeDef

### StringEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]

### StringNotEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]

### StringLike
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]

### StringNotLike
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]


# ConditionsTypeDef

### StringEquals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]

### StringNotEquals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]

### StringLike
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]

### StringNotLike
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ConditionParameterTypeDef]]


# ControlInputParameterTypeDef

### ParameterName
- **Type**: typing.Optional[str]

### ParameterValue
- **Type**: typing.Optional[str]


# ControlScopeOutputTypeDef

### ComplianceResourceIds
- **Type**: typing.Optional[typing.List[str]]

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ControlScopeTypeDef

### ComplianceResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ControlScopeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyActionTypeDef

### DestinationBackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]


# CopyJobSummaryTypeDef

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


# CopyJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointCreatorTypeDef]

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


# CreateBackupPlanInputTypeDef

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupPlanInputTypeDef'>
- **Required**: Yes

### BackupPlanTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateBackupPlanOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackupSelectionInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupSelectionUnionTypeDef'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateBackupSelectionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackupVaultInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateBackupVaultOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFrameworkInputTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkControls
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.FrameworkControlUnionTypeDef]
- **Required**: Yes

### FrameworkDescription
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]

### FrameworkTags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFrameworkOutputTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLegalHoldInputTypeDef

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]

### RecoveryPointSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointSelectionUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLegalHoldOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RecoveryPointSelectionOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLogicallyAirGappedBackupVaultInputTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateLogicallyAirGappedBackupVaultOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReportPlanInputTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportDeliveryChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ReportDeliveryChannelUnionTypeDef'>
- **Required**: Yes

### ReportSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ReportSettingUnionTypeDef'>
- **Required**: Yes

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportPlanTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# CreateReportPlanOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRestoreTestingPlanInputTypeDef

### RestoreTestingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingPlanForCreateTypeDef'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRestoreTestingPlanOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRestoreTestingSelectionInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingSelectionForCreateTypeDef'>
- **Required**: Yes

### CreatorRequestId
- **Type**: typing.Optional[str]


# CreateRestoreTestingSelectionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DateRangeOutputTypeDef

### FromDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ToDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DateRangeTypeDef

### FromDate
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef'>
- **Required**: Yes

### ToDate
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef'>
- **Required**: Yes


# DeleteBackupPlanInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupPlanOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackupSelectionInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultAccessPolicyInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultLockConfigurationInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultNotificationsInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFrameworkInputTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryPointInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportPlanInputTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestoreTestingPlanInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestoreTestingSelectionInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBackupJobInputTypeDef

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBackupJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RecoveryPointCreatorTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBackupVaultInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# DescribeBackupVaultOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCopyJobInputTypeDef

### CopyJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCopyJobOutputTypeDef

### CopyJob
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.CopyJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFrameworkInputTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFrameworkOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.FrameworkControlOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGlobalSettingsOutputTypeDef

### GlobalSettings
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProtectedResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProtectedResourceOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecoveryPointInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# DescribeRecoveryPointOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RecoveryPointCreatorTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.CalculatedLifecycleTypeDef'>
- **Required**: Yes

### Lifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRegionSettingsOutputTypeDef

### ResourceTypeOptInPreference
- **Type**: typing.Dict[str, bool]
- **Required**: Yes

### ResourceTypeManagementPreference
- **Type**: typing.Dict[str, bool]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReportJobInputTypeDef

### ReportJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReportJobOutputTypeDef

### ReportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ReportJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReportPlanInputTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReportPlanOutputTypeDef

### ReportPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ReportPlanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRestoreJobInputTypeDef

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRestoreJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreJobCreatorTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateRecoveryPointFromParentInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRecoveryPointInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportBackupPlanTemplateInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportBackupPlanTemplateOutputTypeDef

### BackupPlanTemplateJson
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FrameworkControlOutputTypeDef

### ControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ControlInputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.ControlInputParameterTypeDef]]

### ControlScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ControlScopeOutputTypeDef]


# FrameworkControlTypeDef

### ControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ControlInputParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ControlInputParameterTypeDef]]

### ControlScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ControlScopeUnionTypeDef]


# FrameworkControlUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FrameworkTypeDef

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


# GetBackupPlanFromJSONInputTypeDef

### BackupPlanTemplateJson
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupPlanFromJSONOutputTypeDef

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupPlanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackupPlanFromTemplateInputTypeDef

### BackupPlanTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupPlanFromTemplateOutputTypeDef

### BackupPlanDocument
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupPlanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackupPlanInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# GetBackupPlanOutputTypeDef

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupPlanTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackupSelectionInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupSelectionOutputTypeDef

### BackupSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupSelectionOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackupVaultAccessPolicyInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupVaultAccessPolicyOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackupVaultNotificationsInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupVaultNotificationsOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLegalHoldInputTypeDef

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLegalHoldOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RecoveryPointSelectionOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecoveryPointIndexDetailsInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecoveryPointIndexDetailsOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecoveryPointRestoreMetadataInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# GetRecoveryPointRestoreMetadataOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRestoreJobMetadataInputTypeDef

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestoreJobMetadataOutputTypeDef

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRestoreTestingInferredMetadataInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]


# GetRestoreTestingInferredMetadataOutputTypeDef

### InferredMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRestoreTestingPlanInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestoreTestingPlanOutputTypeDef

### RestoreTestingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingPlanForGetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRestoreTestingSelectionInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRestoreTestingSelectionOutputTypeDef

### RestoreTestingSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingSelectionForGetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSupportedResourceTypesOutputTypeDef

### ResourceTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IndexActionOutputTypeDef

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]


# IndexActionTypeDef

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# IndexActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IndexedRecoveryPointTypeDef

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


# KeyValueTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# LegalHoldTypeDef

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


# LifecycleTypeDef

### MoveToColdStorageAfterDays
- **Type**: typing.Optional[int]

### DeleteAfterDays
- **Type**: typing.Optional[int]

### OptInToArchiveForSupportedResources
- **Type**: typing.Optional[bool]


# ListBackupJobSummariesInputTypeDef

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


# ListBackupJobSummariesOutputTypeDef

### BackupJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupJobSummaryTypeDef]
- **Required**: Yes

### AggregationPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupJobsInputPaginateTypeDef

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['ABORTED', 'ABORTING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'PARTIAL', 'PENDING', 'RUNNING']]

### ByBackupVaultName
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByResourceType
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCompleteBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupJobsInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByResourceType
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCompleteBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]


# ListBackupJobsOutputTypeDef

### BackupJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupPlanTemplatesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupPlanTemplatesInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupPlanTemplatesOutputTypeDef

### BackupPlanTemplatesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlanTemplatesListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupPlanVersionsInputPaginateTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupPlanVersionsInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupPlanVersionsOutputTypeDef

### BackupPlanVersionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlansListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupPlansInputPaginateTypeDef

### IncludeDeleted
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupPlansInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeDeleted
- **Type**: typing.Optional[bool]


# ListBackupPlansOutputTypeDef

### BackupPlansList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlansListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupSelectionsInputPaginateTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupSelectionsInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupSelectionsOutputTypeDef

### BackupSelectionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupSelectionsListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBackupVaultsInputPaginateTypeDef

### ByVaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### ByShared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupVaultsInputTypeDef

### ByVaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### ByShared
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupVaultsOutputTypeDef

### BackupVaultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupVaultListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCopyJobSummariesInputTypeDef

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


# ListCopyJobSummariesOutputTypeDef

### CopyJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.CopyJobSummaryTypeDef]
- **Required**: Yes

### AggregationPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCopyJobsInputPaginateTypeDef

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PARTIAL', 'RUNNING']]

### ByCreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByResourceType
- **Type**: typing.Optional[str]

### ByDestinationVaultArn
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCompleteAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListCopyJobsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ByResourceArn
- **Type**: typing.Optional[str]

### ByState
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PARTIAL', 'RUNNING']]

### ByCreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByResourceType
- **Type**: typing.Optional[str]

### ByDestinationVaultArn
- **Type**: typing.Optional[str]

### ByAccountId
- **Type**: typing.Optional[str]

### ByCompleteBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCompleteAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByParentJobId
- **Type**: typing.Optional[str]

### ByMessageCategory
- **Type**: typing.Optional[str]


# ListCopyJobsOutputTypeDef

### CopyJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.CopyJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFrameworksInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFrameworksOutputTypeDef

### Frameworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.FrameworkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndexedRecoveryPointsInputPaginateTypeDef

### SourceResourceArn
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ResourceType
- **Type**: typing.Optional[str]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListIndexedRecoveryPointsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SourceResourceArn
- **Type**: typing.Optional[str]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ResourceType
- **Type**: typing.Optional[str]

### IndexStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'FAILED', 'PENDING']]


# ListIndexedRecoveryPointsOutputTypeDef

### IndexedRecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.IndexedRecoveryPointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLegalHoldsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListLegalHoldsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLegalHoldsOutputTypeDef

### LegalHolds
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.LegalHoldTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectedResourcesByBackupVaultInputPaginateTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListProtectedResourcesByBackupVaultInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectedResourcesByBackupVaultOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProtectedResourcesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListProtectedResourcesInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectedResourcesOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsByBackupVaultInputPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByParentRecoveryPointArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsByBackupVaultInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByParentRecoveryPointArn
- **Type**: typing.Optional[str]


# ListRecoveryPointsByBackupVaultOutputTypeDef

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointByBackupVaultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsByLegalHoldInputPaginateTypeDef

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsByLegalHoldInputTypeDef

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRecoveryPointsByLegalHoldOutputTypeDef

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryPointsByResourceInputPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedByAWSBackupOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsByResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ManagedByAWSBackupOnly
- **Type**: typing.Optional[bool]


# ListRecoveryPointsByResourceOutputTypeDef

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointByResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReportJobsInputTypeDef

### ByReportPlanName
- **Type**: typing.Optional[str]

### ByCreationBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreationAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByStatus
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReportJobsOutputTypeDef

### ReportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ReportJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReportPlansInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReportPlansOutputTypeDef

### ReportPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ReportPlanTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobSummariesInputTypeDef

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


# ListRestoreJobSummariesOutputTypeDef

### RestoreJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreJobSummaryTypeDef]
- **Required**: Yes

### AggregationPeriod
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobsByProtectedResourceInputPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByRecoveryPointCreationDateAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByRecoveryPointCreationDateBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreJobsByProtectedResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByRecoveryPointCreationDateAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByRecoveryPointCreationDateBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRestoreJobsByProtectedResourceOutputTypeDef

### RestoreJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreJobsListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreJobsInputPaginateTypeDef

### ByAccountId
- **Type**: typing.Optional[str]

### ByResourceType
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByCompleteBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCompleteAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByRestoreTestingPlanArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreJobsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ByAccountId
- **Type**: typing.Optional[str]

### ByResourceType
- **Type**: typing.Optional[str]

### ByCreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByStatus
- **Type**: typing.Optional[typing.Literal['ABORTED', 'COMPLETED', 'FAILED', 'PENDING', 'RUNNING']]

### ByCompleteBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByCompleteAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.TimestampTypeDef]

### ByRestoreTestingPlanArn
- **Type**: typing.Optional[str]


# ListRestoreJobsOutputTypeDef

### RestoreJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreJobsListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingPlansInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreTestingPlansInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingPlansOutputTypeDef

### RestoreTestingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreTestingPlanForListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingSelectionsInputPaginateTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreTestingSelectionsInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingSelectionsOutputTypeDef

### RestoreTestingSelections
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreTestingSelectionForListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProtectedResourceConditionsOutputTypeDef

### StringEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.KeyValueTypeDef]]

### StringNotEquals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.KeyValueTypeDef]]


# ProtectedResourceConditionsTypeDef

### StringEquals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.KeyValueTypeDef]]

### StringNotEquals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.KeyValueTypeDef]]


# ProtectedResourceConditionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProtectedResourceTypeDef

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


# PutBackupVaultAccessPolicyInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: typing.Optional[str]


# PutBackupVaultLockConfigurationInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### MinRetentionDays
- **Type**: typing.Optional[int]

### MaxRetentionDays
- **Type**: typing.Optional[int]

### ChangeableForDays
- **Type**: typing.Optional[int]


# PutBackupVaultNotificationsInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultEvents
- **Type**: typing.Sequence[typing.Literal['BACKUP_JOB_COMPLETED', 'BACKUP_JOB_EXPIRED', 'BACKUP_JOB_FAILED', 'BACKUP_JOB_STARTED', 'BACKUP_JOB_SUCCESSFUL', 'BACKUP_PLAN_CREATED', 'BACKUP_PLAN_MODIFIED', 'COPY_JOB_FAILED', 'COPY_JOB_STARTED', 'COPY_JOB_SUCCESSFUL', 'RECOVERY_POINT_MODIFIED', 'RESTORE_JOB_COMPLETED', 'RESTORE_JOB_FAILED', 'RESTORE_JOB_STARTED', 'RESTORE_JOB_SUCCESSFUL', 'S3_BACKUP_OBJECT_FAILED', 'S3_RESTORE_OBJECT_FAILED']]
- **Required**: Yes


# PutRestoreValidationResultInputTypeDef

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationStatus
- **Type**: typing.Literal['FAILED', 'SUCCESSFUL', 'TIMED_OUT', 'VALIDATING']
- **Required**: Yes

### ValidationStatusMessage
- **Type**: typing.Optional[str]


# RecoveryPointByBackupVaultTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointCreatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.CalculatedLifecycleTypeDef]

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]

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


# RecoveryPointByResourceTypeDef

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


# RecoveryPointCreatorTypeDef

### BackupPlanId
- **Type**: typing.Optional[str]

### BackupPlanArn
- **Type**: typing.Optional[str]

### BackupPlanVersion
- **Type**: typing.Optional[str]

### BackupRuleId
- **Type**: typing.Optional[str]


# RecoveryPointMemberTypeDef

### RecoveryPointArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### BackupVaultName
- **Type**: typing.Optional[str]


# RecoveryPointSelectionOutputTypeDef

### VaultNames
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.DateRangeOutputTypeDef]


# RecoveryPointSelectionTypeDef

### VaultNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.DateRangeTypeDef]


# RecoveryPointSelectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportDeliveryChannelOutputTypeDef

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]

### Formats
- **Type**: typing.Optional[typing.List[str]]


# ReportDeliveryChannelTypeDef

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]

### Formats
- **Type**: typing.Optional[typing.Sequence[str]]


# ReportDeliveryChannelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReportDestinationTypeDef

### S3BucketName
- **Type**: typing.Optional[str]

### S3Keys
- **Type**: typing.Optional[typing.List[str]]


# ReportJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportDestinationTypeDef]


# ReportPlanTypeDef

### ReportPlanArn
- **Type**: typing.Optional[str]

### ReportPlanName
- **Type**: typing.Optional[str]

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportSettingOutputTypeDef]

### ReportDeliveryChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportDeliveryChannelOutputTypeDef]

### DeploymentStatus
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastAttemptedExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulExecutionTime
- **Type**: typing.Optional[datetime.datetime]


# ReportSettingOutputTypeDef

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


# ReportSettingTypeDef

### ReportTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkArns
- **Type**: typing.Optional[typing.Sequence[str]]

### NumberOfFrameworks
- **Type**: typing.Optional[int]

### Accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationUnits
- **Type**: typing.Optional[typing.Sequence[str]]

### Regions
- **Type**: typing.Optional[typing.Sequence[str]]


# ReportSettingUnionTypeDef

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


# RestoreJobCreatorTypeDef

### RestoreTestingPlanArn
- **Type**: typing.Optional[str]


# RestoreJobSummaryTypeDef

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


# RestoreJobsListMemberTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RestoreJobCreatorTypeDef]

### ValidationStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUCCESSFUL', 'TIMED_OUT', 'VALIDATING']]

### ValidationStatusMessage
- **Type**: typing.Optional[str]

### DeletionStatus
- **Type**: typing.Optional[typing.Literal['DELETING', 'FAILED', 'SUCCESSFUL']]

### DeletionStatusMessage
- **Type**: typing.Optional[str]


# RestoreTestingPlanForCreateTypeDef

### RecoveryPointSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingRecoveryPointSelectionUnionTypeDef'>
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


# RestoreTestingPlanForGetTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RecoveryPointSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingRecoveryPointSelectionOutputTypeDef'>
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


# RestoreTestingPlanForListTypeDef

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


# RestoreTestingPlanForUpdateTypeDef

### RecoveryPointSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RestoreTestingRecoveryPointSelectionUnionTypeDef]

### ScheduleExpression
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingRecoveryPointSelectionOutputTypeDef

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


# RestoreTestingRecoveryPointSelectionTypeDef

### Algorithm
- **Type**: typing.Optional[typing.Literal['LATEST_WITHIN_WINDOW', 'RANDOM_WITHIN_WINDOW']]

### ExcludeVaults
- **Type**: typing.Optional[typing.Sequence[str]]

### IncludeVaults
- **Type**: typing.Optional[typing.Sequence[str]]

### RecoveryPointTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTINUOUS', 'SNAPSHOT']]]

### SelectionWindowDays
- **Type**: typing.Optional[int]


# RestoreTestingRecoveryPointSelectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RestoreTestingSelectionForCreateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### ProtectedResourceConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceConditionsUnionTypeDef]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingSelectionForGetTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceConditionsOutputTypeDef]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# RestoreTestingSelectionForListTypeDef

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


# RestoreTestingSelectionForUpdateTypeDef

### IamRoleArn
- **Type**: typing.Optional[str]

### ProtectedResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ProtectedResourceConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceConditionsUnionTypeDef]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# StartBackupJobInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]

### RecoveryPointTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### BackupOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Index
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StartBackupJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartCopyJobInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]


# StartCopyJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartReportJobInputTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]


# StartReportJobOutputTypeDef

### ReportJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRestoreJobInputTypeDef

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### IamRoleArn
- **Type**: typing.Optional[str]

### IdempotencyToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### CopySourceTagsToRestoredResource
- **Type**: typing.Optional[bool]


# StartRestoreJobOutputTypeDef

### RestoreJobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopBackupJobInputTypeDef

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBackupPlanInputTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupPlanInputTypeDef'>
- **Required**: Yes


# UpdateBackupPlanOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFrameworkInputTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkDescription
- **Type**: typing.Optional[str]

### FrameworkControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.FrameworkControlUnionTypeDef]]

### IdempotencyToken
- **Type**: typing.Optional[str]


# UpdateFrameworkOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlobalSettingsInputTypeDef

### GlobalSettings
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateRecoveryPointIndexSettingsInputTypeDef

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


# UpdateRecoveryPointIndexSettingsOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecoveryPointLifecycleInputTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef]


# UpdateRecoveryPointLifecycleOutputTypeDef

### BackupVaultArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.LifecycleTypeDef'>
- **Required**: Yes

### CalculatedLifecycle
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.CalculatedLifecycleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRegionSettingsInputTypeDef

### ResourceTypeOptInPreference
- **Type**: typing.Optional[typing.Mapping[str, bool]]

### ResourceTypeManagementPreference
- **Type**: typing.Optional[typing.Mapping[str, bool]]


# UpdateReportPlanInputTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportDeliveryChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportDeliveryChannelUnionTypeDef]

### ReportSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportSettingUnionTypeDef]

### IdempotencyToken
- **Type**: typing.Optional[str]


# UpdateReportPlanOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRestoreTestingPlanInputTypeDef

### RestoreTestingPlan
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingPlanForUpdateTypeDef'>
- **Required**: Yes

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRestoreTestingPlanOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRestoreTestingSelectionInputTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingSelectionForUpdateTypeDef'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRestoreTestingSelectionOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


