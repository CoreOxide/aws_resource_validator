from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.backup_constants import *

class AdvancedBackupSettingPaginatorTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    BackupOptions: Optional[Dict[str, str]] = None

class AdvancedBackupSettingTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    BackupOptions: Optional[Mapping[str, str]] = None

class BackupJobSummaryTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[BackupJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class RecoveryPointCreatorTypeDef(BaseValidatorModel):
    BackupPlanId: Optional[str] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None

class BackupPlanTemplatesListMemberTypeDef(BaseValidatorModel):
    BackupPlanTemplateId: Optional[str] = None
    BackupPlanTemplateName: Optional[str] = None

class LifecycleTypeDef(BaseValidatorModel):
    MoveToColdStorageAfterDays: Optional[int] = None
    DeleteAfterDays: Optional[int] = None
    OptInToArchiveForSupportedResources: Optional[bool] = None

class ConditionTypeDef(BaseValidatorModel):
    ConditionType: Literal["STRINGEQUALS"]
    ConditionKey: str
    ConditionValue: str

class BackupSelectionsListMemberTypeDef(BaseValidatorModel):
    SelectionId: Optional[str] = None
    SelectionName: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None
    IamRoleArn: Optional[str] = None

class BackupVaultListMemberTypeDef(BaseValidatorModel):
    BackupVaultName: Optional[str] = None
    BackupVaultArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    EncryptionKeyArn: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    NumberOfRecoveryPoints: Optional[int] = None
    Locked: Optional[bool] = None
    MinRetentionDays: Optional[int] = None
    MaxRetentionDays: Optional[int] = None
    LockDate: Optional[datetime] = None

class CalculatedLifecycleTypeDef(BaseValidatorModel):
    MoveToColdStorageAt: Optional[datetime] = None
    DeleteAt: Optional[datetime] = None

class CancelLegalHoldInputRequestTypeDef(BaseValidatorModel):
    LegalHoldId: str
    CancelDescription: str
    RetainRecordInDays: Optional[int] = None

class ConditionParameterTypeDef(BaseValidatorModel):
    ConditionKey: Optional[str] = None
    ConditionValue: Optional[str] = None

class ControlInputParameterTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class ControlScopeTypeDef(BaseValidatorModel):
    ComplianceResourceIds: Optional[Sequence[str]] = None
    ComplianceResourceTypes: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class CopyJobSummaryTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateBackupVaultInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultTags: Optional[Mapping[str, str]] = None
    EncryptionKeyArn: Optional[str] = None
    CreatorRequestId: Optional[str] = None

class CreateLogicallyAirGappedBackupVaultInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    MinRetentionDays: int
    MaxRetentionDays: int
    BackupVaultTags: Optional[Mapping[str, str]] = None
    CreatorRequestId: Optional[str] = None

class ReportDeliveryChannelTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    Formats: Optional[Sequence[str]] = None

class ReportSettingTypeDef(BaseValidatorModel):
    ReportTemplate: str
    FrameworkArns: Optional[Sequence[str]] = None
    NumberOfFrameworks: Optional[int] = None
    Accounts: Optional[Sequence[str]] = None
    OrganizationUnits: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None

class DeleteBackupPlanInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str

class DeleteBackupSelectionInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    SelectionId: str

class DeleteBackupVaultAccessPolicyInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str

class DeleteBackupVaultInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str

class DeleteBackupVaultLockConfigurationInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str

class DeleteBackupVaultNotificationsInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str

class DeleteFrameworkInputRequestTypeDef(BaseValidatorModel):
    FrameworkName: str

class DeleteRecoveryPointInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str

class DeleteReportPlanInputRequestTypeDef(BaseValidatorModel):
    ReportPlanName: str

class DeleteRestoreTestingPlanInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str

class DeleteRestoreTestingSelectionInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str

class DescribeBackupJobInputRequestTypeDef(BaseValidatorModel):
    BackupJobId: str

class DescribeBackupVaultInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None

class DescribeCopyJobInputRequestTypeDef(BaseValidatorModel):
    CopyJobId: str

class DescribeFrameworkInputRequestTypeDef(BaseValidatorModel):
    FrameworkName: str

class DescribeProtectedResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DescribeRecoveryPointInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None

class DescribeReportJobInputRequestTypeDef(BaseValidatorModel):
    ReportJobId: str

class DescribeReportPlanInputRequestTypeDef(BaseValidatorModel):
    ReportPlanName: str

class DescribeRestoreJobInputRequestTypeDef(BaseValidatorModel):
    RestoreJobId: str

class RestoreJobCreatorTypeDef(BaseValidatorModel):
    RestoreTestingPlanArn: Optional[str] = None

class DisassociateRecoveryPointFromParentInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str

class DisassociateRecoveryPointInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str

class ExportBackupPlanTemplateInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str

class FrameworkTypeDef(BaseValidatorModel):
    FrameworkName: Optional[str] = None
    FrameworkArn: Optional[str] = None
    FrameworkDescription: Optional[str] = None
    NumberOfControls: Optional[int] = None
    CreationTime: Optional[datetime] = None
    DeploymentStatus: Optional[str] = None

class GetBackupPlanFromJSONInputRequestTypeDef(BaseValidatorModel):
    BackupPlanTemplateJson: str

class GetBackupPlanFromTemplateInputRequestTypeDef(BaseValidatorModel):
    BackupPlanTemplateId: str

class GetBackupPlanInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    VersionId: Optional[str] = None

class GetBackupSelectionInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    SelectionId: str

class GetBackupVaultAccessPolicyInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str

class GetBackupVaultNotificationsInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str

class GetLegalHoldInputRequestTypeDef(BaseValidatorModel):
    LegalHoldId: str

class GetRecoveryPointRestoreMetadataInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None

class GetRestoreJobMetadataInputRequestTypeDef(BaseValidatorModel):
    RestoreJobId: str

class GetRestoreTestingInferredMetadataInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None

class GetRestoreTestingPlanInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str

class GetRestoreTestingSelectionInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str

class KeyValueTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class LegalHoldTypeDef(BaseValidatorModel):
    Title: Optional[str] = None
    Status: Optional[LegalHoldStatusType] = None
    Description: Optional[str] = None
    LegalHoldId: Optional[str] = None
    LegalHoldArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CancellationDate: Optional[datetime] = None

class ListBackupJobSummariesInputRequestTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[BackupJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBackupPlanTemplatesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBackupPlanVersionsInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBackupPlansInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeDeleted: Optional[bool] = None

class ListBackupSelectionsInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBackupVaultsInputRequestTypeDef(BaseValidatorModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCopyJobSummariesInputRequestTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFrameworksInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLegalHoldsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProtectedResourcesByBackupVaultInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProtectedResourceTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    LastBackupTime: Optional[datetime] = None
    ResourceName: Optional[str] = None
    LastBackupVaultArn: Optional[str] = None
    LastRecoveryPointArn: Optional[str] = None

class ListProtectedResourcesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRecoveryPointsByLegalHoldInputRequestTypeDef(BaseValidatorModel):
    LegalHoldId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RecoveryPointMemberTypeDef(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    BackupVaultName: Optional[str] = None

class ListRecoveryPointsByResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ManagedByAWSBackupOnly: Optional[bool] = None

class RecoveryPointByResourceTypeDef(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    Status: Optional[RecoveryPointStatusType] = None
    StatusMessage: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    BackupSizeBytes: Optional[int] = None
    BackupVaultName: Optional[str] = None
    IsParent: Optional[bool] = None
    ParentRecoveryPointArn: Optional[str] = None
    ResourceName: Optional[str] = None
    VaultType: Optional[VaultTypeType] = None

class ListReportPlansInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRestoreJobSummariesInputRequestTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[RestoreJobStateType] = None
    ResourceType: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RestoreJobSummaryTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[RestoreJobStateType] = None
    ResourceType: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ListRestoreTestingPlansInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RestoreTestingPlanForListTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    LastExecutionTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class ListRestoreTestingSelectionsInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RestoreTestingSelectionForListTypeDef(BaseValidatorModel):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ValidationWindowHours: Optional[int] = None

class ListTagsInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PutBackupVaultAccessPolicyInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    Policy: Optional[str] = None

class PutBackupVaultLockConfigurationInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    MinRetentionDays: Optional[int] = None
    MaxRetentionDays: Optional[int] = None
    ChangeableForDays: Optional[int] = None

class PutBackupVaultNotificationsInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    SNSTopicArn: str
    BackupVaultEvents: Sequence[BackupVaultEventType]

class PutRestoreValidationResultInputRequestTypeDef(BaseValidatorModel):
    RestoreJobId: str
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: Optional[str] = None

class ReportDestinationTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Keys: Optional[List[str]] = None

class RestoreTestingRecoveryPointSelectionTypeDef(BaseValidatorModel):
    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithmType] = None
    ExcludeVaults: Optional[Sequence[str]] = None
    IncludeVaults: Optional[Sequence[str]] = None
    RecoveryPointTypes: Optional[Sequence[RestoreTestingRecoveryPointTypeType]] = None
    SelectionWindowDays: Optional[int] = None

class StartReportJobInputRequestTypeDef(BaseValidatorModel):
    ReportPlanName: str
    IdempotencyToken: Optional[str] = None

class StartRestoreJobInputRequestTypeDef(BaseValidatorModel):
    RecoveryPointArn: str
    Metadata: Mapping[str, str]
    IamRoleArn: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    ResourceType: Optional[str] = None
    CopySourceTagsToRestoredResource: Optional[bool] = None

class StopBackupJobInputRequestTypeDef(BaseValidatorModel):
    BackupJobId: str

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeyList: Sequence[str]

class UpdateGlobalSettingsInputRequestTypeDef(BaseValidatorModel):
    GlobalSettings: Optional[Mapping[str, str]] = None

class UpdateRegionSettingsInputRequestTypeDef(BaseValidatorModel):
    ResourceTypeOptInPreference: Optional[Mapping[str, bool]] = None
    ResourceTypeManagementPreference: Optional[Mapping[str, bool]] = None

class BackupPlansListMemberPaginatorTypeDef(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    DeletionDate: Optional[datetime] = None
    VersionId: Optional[str] = None
    BackupPlanName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingPaginatorTypeDef]] = None

class BackupPlansListMemberTypeDef(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    DeletionDate: Optional[datetime] = None
    VersionId: Optional[str] = None
    BackupPlanName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingTypeDef]] = None

class BackupJobTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    BackupJobId: Optional[str] = None
    BackupVaultName: Optional[str] = None
    BackupVaultArn: Optional[str] = None
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    State: Optional[BackupJobStateType] = None
    StatusMessage: Optional[str] = None
    PercentDone: Optional[str] = None
    BackupSizeInBytes: Optional[int] = None
    IamRoleArn: Optional[str] = None
    CreatedBy: Optional[RecoveryPointCreatorTypeDef] = None
    ExpectedCompletionDate: Optional[datetime] = None
    StartBy: Optional[datetime] = None
    ResourceType: Optional[str] = None
    BytesTransferred: Optional[int] = None
    BackupOptions: Optional[Dict[str, str]] = None
    BackupType: Optional[str] = None
    ParentJobId: Optional[str] = None
    IsParent: Optional[bool] = None
    ResourceName: Optional[str] = None
    InitiationDate: Optional[datetime] = None
    MessageCategory: Optional[str] = None

class CopyJobTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    CopyJobId: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    SourceRecoveryPointArn: Optional[str] = None
    DestinationBackupVaultArn: Optional[str] = None
    DestinationRecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    State: Optional[CopyJobStateType] = None
    StatusMessage: Optional[str] = None
    BackupSizeInBytes: Optional[int] = None
    IamRoleArn: Optional[str] = None
    CreatedBy: Optional[RecoveryPointCreatorTypeDef] = None
    ResourceType: Optional[str] = None
    ParentJobId: Optional[str] = None
    IsParent: Optional[bool] = None
    CompositeMemberIdentifier: Optional[str] = None
    NumberOfChildJobs: Optional[int] = None
    ChildJobsInState: Optional[Dict[CopyJobStateType, int]] = None
    ResourceName: Optional[str] = None
    MessageCategory: Optional[str] = None

class CopyActionTypeDef(BaseValidatorModel):
    DestinationBackupVaultArn: str
    Lifecycle: Optional[LifecycleTypeDef] = None

class StartBackupJobInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    ResourceArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompleteWindowMinutes: Optional[int] = None
    Lifecycle: Optional[LifecycleTypeDef] = None
    RecoveryPointTags: Optional[Mapping[str, str]] = None
    BackupOptions: Optional[Mapping[str, str]] = None

class StartCopyJobInputRequestTypeDef(BaseValidatorModel):
    RecoveryPointArn: str
    SourceBackupVaultName: str
    DestinationBackupVaultArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    Lifecycle: Optional[LifecycleTypeDef] = None

class UpdateRecoveryPointLifecycleInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    Lifecycle: Optional[LifecycleTypeDef] = None

class RecoveryPointByBackupVaultTypeDef(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    BackupVaultArn: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    CreatedBy: Optional[RecoveryPointCreatorTypeDef] = None
    IamRoleArn: Optional[str] = None
    Status: Optional[RecoveryPointStatusType] = None
    StatusMessage: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    BackupSizeInBytes: Optional[int] = None
    CalculatedLifecycle: Optional[CalculatedLifecycleTypeDef] = None
    Lifecycle: Optional[LifecycleTypeDef] = None
    EncryptionKeyArn: Optional[str] = None
    IsEncrypted: Optional[bool] = None
    LastRestoreTime: Optional[datetime] = None
    ParentRecoveryPointArn: Optional[str] = None
    CompositeMemberIdentifier: Optional[str] = None
    IsParent: Optional[bool] = None
    ResourceName: Optional[str] = None
    VaultType: Optional[VaultTypeType] = None

class ConditionsTypeDef(BaseValidatorModel):
    StringEquals: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringNotEquals: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringLike: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringNotLike: Optional[Sequence[ConditionParameterTypeDef]] = None

class FrameworkControlTypeDef(BaseValidatorModel):
    ControlName: str
    ControlInputParameters: Optional[Sequence[ControlInputParameterTypeDef]] = None
    ControlScope: Optional[ControlScopeTypeDef] = None

class CreateBackupPlanOutputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupSelectionOutputTypeDef(BaseValidatorModel):
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupVaultOutputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFrameworkOutputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLogicallyAirGappedBackupVaultOutputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    VaultState: VaultStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportPlanOutputTypeDef(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingPlanOutputTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingSelectionOutputTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupPlanOutputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    DeletionDate: datetime
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupJobOutputTypeDef(BaseValidatorModel):
    AccountId: str
    BackupJobId: str
    BackupVaultName: str
    BackupVaultArn: str
    RecoveryPointArn: str
    ResourceArn: str
    CreationDate: datetime
    CompletionDate: datetime
    State: BackupJobStateType
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    CreatedBy: RecoveryPointCreatorTypeDef
    ResourceType: str
    BytesTransferred: int
    ExpectedCompletionDate: datetime
    StartBy: datetime
    BackupOptions: Dict[str, str]
    BackupType: str
    ParentJobId: str
    IsParent: bool
    NumberOfChildJobs: int
    ChildJobsInState: Dict[BackupJobStateType, int]
    ResourceName: str
    InitiationDate: datetime
    MessageCategory: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupVaultOutputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    VaultType: VaultTypeType
    EncryptionKeyArn: str
    CreationDate: datetime
    CreatorRequestId: str
    NumberOfRecoveryPoints: int
    Locked: bool
    MinRetentionDays: int
    MaxRetentionDays: int
    LockDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalSettingsOutputTypeDef(BaseValidatorModel):
    GlobalSettings: Dict[str, str]
    LastUpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProtectedResourceOutputTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceType: str
    LastBackupTime: datetime
    ResourceName: str
    LastBackupVaultArn: str
    LastRecoveryPointArn: str
    LatestRestoreExecutionTimeMinutes: int
    LatestRestoreJobCreationDate: datetime
    LatestRestoreRecoveryPointCreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecoveryPointOutputTypeDef(BaseValidatorModel):
    RecoveryPointArn: str
    BackupVaultName: str
    BackupVaultArn: str
    SourceBackupVaultArn: str
    ResourceArn: str
    ResourceType: str
    CreatedBy: RecoveryPointCreatorTypeDef
    IamRoleArn: str
    Status: RecoveryPointStatusType
    StatusMessage: str
    CreationDate: datetime
    CompletionDate: datetime
    BackupSizeInBytes: int
    CalculatedLifecycle: CalculatedLifecycleTypeDef
    Lifecycle: LifecycleTypeDef
    EncryptionKeyArn: str
    IsEncrypted: bool
    StorageClass: StorageClassType
    LastRestoreTime: datetime
    ParentRecoveryPointArn: str
    CompositeMemberIdentifier: str
    IsParent: bool
    ResourceName: str
    VaultType: VaultTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegionSettingsOutputTypeDef(BaseValidatorModel):
    ResourceTypeOptInPreference: Dict[str, bool]
    ResourceTypeManagementPreference: Dict[str, bool]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportBackupPlanTemplateOutputTypeDef(BaseValidatorModel):
    BackupPlanTemplateJson: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupVaultAccessPolicyOutputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupVaultNotificationsOutputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    SNSTopicArn: str
    BackupVaultEvents: List[BackupVaultEventType]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryPointRestoreMetadataOutputTypeDef(BaseValidatorModel):
    BackupVaultArn: str
    RecoveryPointArn: str
    RestoreMetadata: Dict[str, str]
    ResourceType: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRestoreJobMetadataOutputTypeDef(BaseValidatorModel):
    RestoreJobId: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRestoreTestingInferredMetadataOutputTypeDef(BaseValidatorModel):
    InferredMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSupportedResourceTypesOutputTypeDef(BaseValidatorModel):
    ResourceTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobSummariesOutputTypeDef(BaseValidatorModel):
    BackupJobSummaries: List[BackupJobSummaryTypeDef]
    AggregationPeriod: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlanTemplatesOutputTypeDef(BaseValidatorModel):
    NextToken: str
    BackupPlanTemplatesList: List[BackupPlanTemplatesListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupSelectionsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    BackupSelectionsList: List[BackupSelectionsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupVaultsOutputTypeDef(BaseValidatorModel):
    BackupVaultList: List[BackupVaultListMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCopyJobSummariesOutputTypeDef(BaseValidatorModel):
    CopyJobSummaries: List[CopyJobSummaryTypeDef]
    AggregationPeriod: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartBackupJobOutputTypeDef(BaseValidatorModel):
    BackupJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartCopyJobOutputTypeDef(BaseValidatorModel):
    CopyJobId: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartReportJobOutputTypeDef(BaseValidatorModel):
    ReportJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRestoreJobOutputTypeDef(BaseValidatorModel):
    RestoreJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackupPlanOutputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFrameworkOutputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecoveryPointLifecycleOutputTypeDef(BaseValidatorModel):
    BackupVaultArn: str
    RecoveryPointArn: str
    Lifecycle: LifecycleTypeDef
    CalculatedLifecycle: CalculatedLifecycleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportPlanOutputTypeDef(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingPlanOutputTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingSelectionOutputTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportPlanInputRequestTypeDef(BaseValidatorModel):
    ReportPlanName: str
    ReportDeliveryChannel: ReportDeliveryChannelTypeDef
    ReportSetting: ReportSettingTypeDef
    ReportPlanDescription: Optional[str] = None
    ReportPlanTags: Optional[Mapping[str, str]] = None
    IdempotencyToken: Optional[str] = None

class ReportPlanTypeDef(BaseValidatorModel):
    ReportPlanArn: Optional[str] = None
    ReportPlanName: Optional[str] = None
    ReportPlanDescription: Optional[str] = None
    ReportSetting: Optional[ReportSettingTypeDef] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelTypeDef] = None
    DeploymentStatus: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAttemptedExecutionTime: Optional[datetime] = None
    LastSuccessfulExecutionTime: Optional[datetime] = None

class UpdateReportPlanInputRequestTypeDef(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanDescription: Optional[str] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelTypeDef] = None
    ReportSetting: Optional[ReportSettingTypeDef] = None
    IdempotencyToken: Optional[str] = None

class DateRangeTypeDef(BaseValidatorModel):
    FromDate: TimestampTypeDef
    ToDate: TimestampTypeDef

class ListBackupJobsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByResourceArn: Optional[str] = None
    ByState: Optional[BackupJobStateType] = None
    ByBackupVaultName: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByResourceType: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None

class ListCopyJobsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByResourceArn: Optional[str] = None
    ByState: Optional[CopyJobStateType] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByResourceType: Optional[str] = None
    ByDestinationVaultArn: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None

class ListRecoveryPointsByBackupVaultInputRequestTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByResourceArn: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByBackupPlanId: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByParentRecoveryPointArn: Optional[str] = None

class ListReportJobsInputRequestTypeDef(BaseValidatorModel):
    ByReportPlanName: Optional[str] = None
    ByCreationBefore: Optional[TimestampTypeDef] = None
    ByCreationAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRestoreJobsByProtectedResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ByStatus: Optional[RestoreJobStatusType] = None
    ByRecoveryPointCreationDateAfter: Optional[TimestampTypeDef] = None
    ByRecoveryPointCreationDateBefore: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRestoreJobsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByAccountId: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[RestoreJobStatusType] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByRestoreTestingPlanArn: Optional[str] = None

class DescribeRestoreJobOutputTypeDef(BaseValidatorModel):
    AccountId: str
    RestoreJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    CompletionDate: datetime
    Status: RestoreJobStatusType
    StatusMessage: str
    PercentDone: str
    BackupSizeInBytes: int
    IamRoleArn: str
    ExpectedCompletionTimeMinutes: int
    CreatedResourceArn: str
    ResourceType: str
    RecoveryPointCreationDate: datetime
    CreatedBy: RestoreJobCreatorTypeDef
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: str
    DeletionStatus: RestoreDeletionStatusType
    DeletionStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreJobsListMemberTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    RestoreJobId: Optional[str] = None
    RecoveryPointArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    Status: Optional[RestoreJobStatusType] = None
    StatusMessage: Optional[str] = None
    PercentDone: Optional[str] = None
    BackupSizeInBytes: Optional[int] = None
    IamRoleArn: Optional[str] = None
    ExpectedCompletionTimeMinutes: Optional[int] = None
    CreatedResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    RecoveryPointCreationDate: Optional[datetime] = None
    CreatedBy: Optional[RestoreJobCreatorTypeDef] = None
    ValidationStatus: Optional[RestoreValidationStatusType] = None
    ValidationStatusMessage: Optional[str] = None
    DeletionStatus: Optional[RestoreDeletionStatusType] = None
    DeletionStatusMessage: Optional[str] = None

class ListFrameworksOutputTypeDef(BaseValidatorModel):
    Frameworks: List[FrameworkTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectedResourceConditionsTypeDef(BaseValidatorModel):
    StringEquals: Optional[Sequence[KeyValueTypeDef]] = None
    StringNotEquals: Optional[Sequence[KeyValueTypeDef]] = None

class ListLegalHoldsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    LegalHolds: List[LegalHoldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobsInputListBackupJobsPaginateTypeDef(BaseValidatorModel):
    ByResourceArn: Optional[str] = None
    ByState: Optional[BackupJobStateType] = None
    ByBackupVaultName: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByResourceType: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef(BaseValidatorModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupPlansInputListBackupPlansPaginateTypeDef(BaseValidatorModel):
    IncludeDeleted: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef(BaseValidatorModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupVaultsInputListBackupVaultsPaginateTypeDef(BaseValidatorModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCopyJobsInputListCopyJobsPaginateTypeDef(BaseValidatorModel):
    ByResourceArn: Optional[str] = None
    ByState: Optional[CopyJobStateType] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByResourceType: Optional[str] = None
    ByDestinationVaultArn: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLegalHoldsInputListLegalHoldsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedResourcesByBackupVaultInputListProtectedResourcesByBackupVaultPaginateTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    ByResourceArn: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByBackupPlanId: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByParentRecoveryPointArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef(BaseValidatorModel):
    LegalHoldId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    ManagedByAWSBackupOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRestoreJobsInputListRestoreJobsPaginateTypeDef(BaseValidatorModel):
    ByAccountId: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[RestoreJobStatusType] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByRestoreTestingPlanArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRestoreTestingPlansInputListRestoreTestingPlansPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRestoreTestingSelectionsInputListRestoreTestingSelectionsPaginateTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedResourcesByBackupVaultOutputTypeDef(BaseValidatorModel):
    Results: List[ProtectedResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectedResourcesOutputTypeDef(BaseValidatorModel):
    Results: List[ProtectedResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsByLegalHoldOutputTypeDef(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsByResourceOutputTypeDef(BaseValidatorModel):
    NextToken: str
    RecoveryPoints: List[RecoveryPointByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreJobSummariesOutputTypeDef(BaseValidatorModel):
    RestoreJobSummaries: List[RestoreJobSummaryTypeDef]
    AggregationPeriod: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreTestingPlansOutputTypeDef(BaseValidatorModel):
    NextToken: str
    RestoreTestingPlans: List[RestoreTestingPlanForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreTestingSelectionsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    RestoreTestingSelections: List[RestoreTestingSelectionForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReportJobTypeDef(BaseValidatorModel):
    ReportJobId: Optional[str] = None
    ReportPlanArn: Optional[str] = None
    ReportTemplate: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    ReportDestination: Optional[ReportDestinationTypeDef] = None

class RestoreTestingPlanForCreateTypeDef(BaseValidatorModel):
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionTypeDef
    RestoreTestingPlanName: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class RestoreTestingPlanForGetTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionTypeDef
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    CreatorRequestId: Optional[str] = None
    LastExecutionTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class RestoreTestingPlanForUpdateTypeDef(BaseValidatorModel):
    RecoveryPointSelection: Optional[RestoreTestingRecoveryPointSelectionTypeDef] = None
    ScheduleExpression: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class ListBackupPlanVersionsOutputPaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    BackupPlanVersionsList: List[BackupPlansListMemberPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlansOutputPaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    BackupPlansList: List[BackupPlansListMemberPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlanVersionsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    BackupPlanVersionsList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlansOutputTypeDef(BaseValidatorModel):
    NextToken: str
    BackupPlansList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobsOutputTypeDef(BaseValidatorModel):
    BackupJobs: List[BackupJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCopyJobOutputTypeDef(BaseValidatorModel):
    CopyJob: CopyJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCopyJobsOutputTypeDef(BaseValidatorModel):
    CopyJobs: List[CopyJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BackupRuleInputTypeDef(BaseValidatorModel):
    RuleName: str
    TargetBackupVaultName: str
    ScheduleExpression: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompletionWindowMinutes: Optional[int] = None
    Lifecycle: Optional[LifecycleTypeDef] = None
    RecoveryPointTags: Optional[Mapping[str, str]] = None
    CopyActions: Optional[Sequence[CopyActionTypeDef]] = None
    EnableContinuousBackup: Optional[bool] = None
    ScheduleExpressionTimezone: Optional[str] = None

class BackupRuleTypeDef(BaseValidatorModel):
    RuleName: str
    TargetBackupVaultName: str
    ScheduleExpression: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompletionWindowMinutes: Optional[int] = None
    Lifecycle: Optional[LifecycleTypeDef] = None
    RecoveryPointTags: Optional[Dict[str, str]] = None
    RuleId: Optional[str] = None
    CopyActions: Optional[List[CopyActionTypeDef]] = None
    EnableContinuousBackup: Optional[bool] = None
    ScheduleExpressionTimezone: Optional[str] = None

class ListRecoveryPointsByBackupVaultOutputTypeDef(BaseValidatorModel):
    NextToken: str
    RecoveryPoints: List[RecoveryPointByBackupVaultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BackupSelectionTypeDef(BaseValidatorModel):
    SelectionName: str
    IamRoleArn: str
    Resources: Optional[Sequence[str]] = None
    ListOfTags: Optional[Sequence[ConditionTypeDef]] = None
    NotResources: Optional[Sequence[str]] = None
    Conditions: Optional[ConditionsTypeDef] = None

class CreateFrameworkInputRequestTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkControls: Sequence[FrameworkControlTypeDef]
    FrameworkDescription: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    FrameworkTags: Optional[Mapping[str, str]] = None

class DescribeFrameworkOutputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    FrameworkDescription: str
    FrameworkControls: List[FrameworkControlTypeDef]
    CreationTime: datetime
    DeploymentStatus: str
    FrameworkStatus: str
    IdempotencyToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFrameworkInputRequestTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkDescription: Optional[str] = None
    FrameworkControls: Optional[Sequence[FrameworkControlTypeDef]] = None
    IdempotencyToken: Optional[str] = None

class DescribeReportPlanOutputTypeDef(BaseValidatorModel):
    ReportPlan: ReportPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportPlansOutputTypeDef(BaseValidatorModel):
    ReportPlans: List[ReportPlanTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecoveryPointSelectionTypeDef(BaseValidatorModel):
    VaultNames: Optional[Sequence[str]] = None
    ResourceIdentifiers: Optional[Sequence[str]] = None
    DateRange: Optional[DateRangeTypeDef] = None

class ListRestoreJobsByProtectedResourceOutputTypeDef(BaseValidatorModel):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreJobsOutputTypeDef(BaseValidatorModel):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTestingSelectionForCreateTypeDef(BaseValidatorModel):
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingSelectionName: str
    ProtectedResourceArns: Optional[Sequence[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsTypeDef] = None
    RestoreMetadataOverrides: Optional[Mapping[str, str]] = None
    ValidationWindowHours: Optional[int] = None

class RestoreTestingSelectionForGetTypeDef(BaseValidatorModel):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    CreatorRequestId: Optional[str] = None
    ProtectedResourceArns: Optional[List[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsTypeDef] = None
    RestoreMetadataOverrides: Optional[Dict[str, str]] = None
    ValidationWindowHours: Optional[int] = None

class RestoreTestingSelectionForUpdateTypeDef(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    ProtectedResourceArns: Optional[Sequence[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsTypeDef] = None
    RestoreMetadataOverrides: Optional[Mapping[str, str]] = None
    ValidationWindowHours: Optional[int] = None

class DescribeReportJobOutputTypeDef(BaseValidatorModel):
    ReportJob: ReportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportJobsOutputTypeDef(BaseValidatorModel):
    ReportJobs: List[ReportJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingPlanInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForCreateTypeDef
    CreatorRequestId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetRestoreTestingPlanOutputTypeDef(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingPlanInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForUpdateTypeDef
    RestoreTestingPlanName: str

class BackupPlanInputTypeDef(BaseValidatorModel):
    BackupPlanName: str
    Rules: Sequence[BackupRuleInputTypeDef]
    AdvancedBackupSettings: Optional[Sequence[AdvancedBackupSettingTypeDef]] = None

class BackupPlanTypeDef(BaseValidatorModel):
    BackupPlanName: str
    Rules: List[BackupRuleTypeDef]
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingTypeDef]] = None

class CreateBackupSelectionInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupSelection: BackupSelectionTypeDef
    CreatorRequestId: Optional[str] = None

class GetBackupSelectionOutputTypeDef(BaseValidatorModel):
    BackupSelection: BackupSelectionTypeDef
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLegalHoldInputRequestTypeDef(BaseValidatorModel):
    Title: str
    Description: str
    IdempotencyToken: Optional[str] = None
    RecoveryPointSelection: Optional[RecoveryPointSelectionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateLegalHoldOutputTypeDef(BaseValidatorModel):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    RecoveryPointSelection: RecoveryPointSelectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLegalHoldOutputTypeDef(BaseValidatorModel):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    CancelDescription: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    CancellationDate: datetime
    RetainRecordUntil: datetime
    RecoveryPointSelection: RecoveryPointSelectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingSelectionInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForCreateTypeDef
    CreatorRequestId: Optional[str] = None

class GetRestoreTestingSelectionOutputTypeDef(BaseValidatorModel):
    RestoreTestingSelection: RestoreTestingSelectionForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingSelectionInputRequestTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForUpdateTypeDef
    RestoreTestingSelectionName: str

class CreateBackupPlanInputRequestTypeDef(BaseValidatorModel):
    BackupPlan: BackupPlanInputTypeDef
    BackupPlanTags: Optional[Mapping[str, str]] = None
    CreatorRequestId: Optional[str] = None

class UpdateBackupPlanInputRequestTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupPlan: BackupPlanInputTypeDef

class GetBackupPlanFromJSONOutputTypeDef(BaseValidatorModel):
    BackupPlan: BackupPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupPlanFromTemplateOutputTypeDef(BaseValidatorModel):
    BackupPlanDocument: BackupPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupPlanOutputTypeDef(BaseValidatorModel):
    BackupPlan: BackupPlanTypeDef
    BackupPlanId: str
    BackupPlanArn: str
    VersionId: str
    CreatorRequestId: str
    CreationDate: datetime
    DeletionDate: datetime
    LastExecutionDate: datetime
    AdvancedBackupSettings: List[AdvancedBackupSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

