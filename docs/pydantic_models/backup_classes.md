# backup_classes

# AdvancedBackupSettingPaginatorTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### BackupOptions
- **Type**: typing.Optional[typing.Dict[str, str]]


# AdvancedBackupSettingTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### BackupOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingTypeDef]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingTypeDef]]


# BackupPlansListMemberPaginatorTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingPaginatorTypeDef]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingTypeDef]]


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


# CancelLegalHoldInputRequestTypeDef

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


# ControlScopeTypeDef

### ComplianceResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


# CreateBackupPlanInputRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackupSelectionInputRequestTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupSelectionTypeDef'>
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


# CreateBackupVaultInputRequestTypeDef

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


# CreateFrameworkInputRequestTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkControls
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.FrameworkControlTypeDef]
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


# CreateLegalHoldInputRequestTypeDef

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IdempotencyToken
- **Type**: typing.Optional[str]

### RecoveryPointSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointSelectionTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RecoveryPointSelectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLogicallyAirGappedBackupVaultInputRequestTypeDef

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


# CreateReportPlanInputRequestTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportDeliveryChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ReportDeliveryChannelTypeDef'>
- **Required**: Yes

### ReportSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ReportSettingTypeDef'>
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


# CreateRestoreTestingPlanInputRequestTypeDef

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


# CreateRestoreTestingSelectionInputRequestTypeDef

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


# DateRangeTypeDef

### FromDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToDate
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DeleteBackupPlanInputRequestTypeDef

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


# DeleteBackupSelectionInputRequestTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultAccessPolicyInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultLockConfigurationInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackupVaultNotificationsInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFrameworkInputRequestTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryPointInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReportPlanInputRequestTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestoreTestingPlanInputRequestTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRestoreTestingSelectionInputRequestTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelectionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBackupJobInputRequestTypeDef

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


# DescribeBackupVaultInputRequestTypeDef

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


# DescribeCopyJobInputRequestTypeDef

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


# DescribeFrameworkInputRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.FrameworkControlTypeDef]
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


# DescribeProtectedResourceInputRequestTypeDef

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


# DescribeRecoveryPointInputRequestTypeDef

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


# DescribeReportJobInputRequestTypeDef

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


# DescribeReportPlanInputRequestTypeDef

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


# DescribeRestoreJobInputRequestTypeDef

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


# DisassociateRecoveryPointFromParentInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateRecoveryPointInputRequestTypeDef

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


# ExportBackupPlanTemplateInputRequestTypeDef

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


# FrameworkControlTypeDef

### ControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ControlInputParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.ControlInputParameterTypeDef]]

### ControlScope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ControlScopeTypeDef]


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


# GetBackupPlanFromJSONInputRequestTypeDef

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


# GetBackupPlanFromTemplateInputRequestTypeDef

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


# GetBackupPlanInputRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackupSelectionInputRequestTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackupSelectionOutputTypeDef

### BackupSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.BackupSelectionTypeDef'>
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


# GetBackupVaultAccessPolicyInputRequestTypeDef

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


# GetBackupVaultNotificationsInputRequestTypeDef

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


# GetLegalHoldInputRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RecoveryPointSelectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecoveryPointRestoreMetadataInputRequestTypeDef

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


# GetRestoreJobMetadataInputRequestTypeDef

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


# GetRestoreTestingInferredMetadataInputRequestTypeDef

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


# GetRestoreTestingPlanInputRequestTypeDef

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


# GetRestoreTestingSelectionInputRequestTypeDef

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


# ListBackupJobSummariesInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupJobsInputListBackupJobsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupJobsInputRequestTypeDef

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


# ListBackupJobsOutputTypeDef

### BackupJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupJobTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupPlanTemplatesInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupPlanTemplatesOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanTemplatesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlanTemplatesListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupPlanVersionsInputRequestTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupPlanVersionsOutputPaginatorTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanVersionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlansListMemberPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupPlanVersionsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlanVersionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlansListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupPlansInputListBackupPlansPaginateTypeDef

### IncludeDeleted
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupPlansInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeDeleted
- **Type**: typing.Optional[bool]


# ListBackupPlansOutputPaginatorTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlansList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlansListMemberPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupPlansOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPlansList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupPlansListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupSelectionsInputRequestTypeDef

### BackupPlanId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListBackupSelectionsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BackupSelectionsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.BackupSelectionsListMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackupVaultsInputListBackupVaultsPaginateTypeDef

### ByVaultType
- **Type**: typing.Optional[typing.Literal['BACKUP_VAULT', 'LOGICALLY_AIR_GAPPED_BACKUP_VAULT']]

### ByShared
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListBackupVaultsInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCopyJobSummariesInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCopyJobsInputListCopyJobsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListCopyJobsInputRequestTypeDef

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


# ListCopyJobsOutputTypeDef

### CopyJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.CopyJobTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFrameworksInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFrameworksOutputTypeDef

### Frameworks
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.FrameworkTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLegalHoldsInputListLegalHoldsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListLegalHoldsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLegalHoldsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### LegalHolds
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.LegalHoldTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProtectedResourcesByBackupVaultInputListProtectedResourcesByBackupVaultPaginateTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListProtectedResourcesByBackupVaultInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListProtectedResourcesInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProtectedResourcesOutputTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsByBackupVaultInputRequestTypeDef

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


# ListRecoveryPointsByBackupVaultOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointByBackupVaultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef

### LegalHoldId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsByLegalHoldInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedByAWSBackupOnly
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRecoveryPointsByResourceInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RecoveryPointByResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportJobsInputRequestTypeDef

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


# ListReportJobsOutputTypeDef

### ReportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ReportJobTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReportPlansInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReportPlansOutputTypeDef

### ReportPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.ReportPlanTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRestoreJobSummariesInputRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRestoreJobsByProtectedResourceInputRequestTypeDef

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


# ListRestoreJobsByProtectedResourceOutputTypeDef

### RestoreJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreJobsListMemberTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRestoreJobsInputListRestoreJobsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreJobsInputRequestTypeDef

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


# ListRestoreJobsOutputTypeDef

### RestoreJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreJobsListMemberTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRestoreTestingPlansInputListRestoreTestingPlansPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreTestingPlansInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingPlansOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingPlans
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreTestingPlanForListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRestoreTestingSelectionsInputListRestoreTestingSelectionsPaginateTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.PaginatorConfigTypeDef]


# ListRestoreTestingSelectionsInputRequestTypeDef

### RestoreTestingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRestoreTestingSelectionsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RestoreTestingSelections
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.RestoreTestingSelectionForListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsOutputTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProtectedResourceConditionsTypeDef

### StringEquals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.KeyValueTypeDef]]

### StringNotEquals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.KeyValueTypeDef]]


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


# PutBackupVaultAccessPolicyInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: typing.Optional[str]


# PutBackupVaultLockConfigurationInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### MinRetentionDays
- **Type**: typing.Optional[int]

### MaxRetentionDays
- **Type**: typing.Optional[int]

### ChangeableForDays
- **Type**: typing.Optional[int]


# PutBackupVaultNotificationsInputRequestTypeDef

### BackupVaultName
- **Type**: <class 'str'>
- **Required**: Yes

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### BackupVaultEvents
- **Type**: typing.Sequence[typing.Literal['BACKUP_JOB_COMPLETED', 'BACKUP_JOB_EXPIRED', 'BACKUP_JOB_FAILED', 'BACKUP_JOB_STARTED', 'BACKUP_JOB_SUCCESSFUL', 'BACKUP_PLAN_CREATED', 'BACKUP_PLAN_MODIFIED', 'COPY_JOB_FAILED', 'COPY_JOB_STARTED', 'COPY_JOB_SUCCESSFUL', 'RECOVERY_POINT_MODIFIED', 'RESTORE_JOB_COMPLETED', 'RESTORE_JOB_FAILED', 'RESTORE_JOB_STARTED', 'RESTORE_JOB_SUCCESSFUL', 'S3_BACKUP_OBJECT_FAILED', 'S3_RESTORE_OBJECT_FAILED']]
- **Required**: Yes


# PutRestoreValidationResultInputRequestTypeDef

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


# RecoveryPointSelectionTypeDef

### VaultNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### DateRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.DateRangeTypeDef]


# ReportDeliveryChannelTypeDef

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]

### Formats
- **Type**: typing.Optional[typing.Sequence[str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportSettingTypeDef]

### ReportDeliveryChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportDeliveryChannelTypeDef]

### DeploymentStatus
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastAttemptedExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulExecutionTime
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingRecoveryPointSelectionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.RestoreTestingRecoveryPointSelectionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.RestoreTestingRecoveryPointSelectionTypeDef]

### ScheduleExpression
- **Type**: typing.Optional[str]

### ScheduleExpressionTimezone
- **Type**: typing.Optional[str]

### StartWindowHours
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceConditionsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceConditionsTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ProtectedResourceConditionsTypeDef]

### RestoreMetadataOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ValidationWindowHours
- **Type**: typing.Optional[int]


# StartBackupJobInputRequestTypeDef

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


# StartCopyJobInputRequestTypeDef

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


# StartReportJobInputRequestTypeDef

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


# StartRestoreJobInputRequestTypeDef

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


# StopBackupJobInputRequestTypeDef

### BackupJobId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBackupPlanInputRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.backup_classes.AdvancedBackupSettingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.backup_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFrameworkInputRequestTypeDef

### FrameworkName
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkDescription
- **Type**: typing.Optional[str]

### FrameworkControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.backup_classes.FrameworkControlTypeDef]]

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


# UpdateGlobalSettingsInputRequestTypeDef

### GlobalSettings
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateRecoveryPointLifecycleInputRequestTypeDef

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


# UpdateRegionSettingsInputRequestTypeDef

### ResourceTypeOptInPreference
- **Type**: typing.Optional[typing.Mapping[str, bool]]

### ResourceTypeManagementPreference
- **Type**: typing.Optional[typing.Mapping[str, bool]]


# UpdateReportPlanInputRequestTypeDef

### ReportPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ReportPlanDescription
- **Type**: typing.Optional[str]

### ReportDeliveryChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportDeliveryChannelTypeDef]

### ReportSetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.backup_classes.ReportSettingTypeDef]

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


# UpdateRestoreTestingPlanInputRequestTypeDef

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


# UpdateRestoreTestingSelectionInputRequestTypeDef

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


