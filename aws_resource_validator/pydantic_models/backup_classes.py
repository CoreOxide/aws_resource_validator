from datetime import datetime
from pydantic import BaseModel
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

class AdvancedBackupSettingPaginatorTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    BackupOptions: Optional[Dict[str, str]] = None

class AdvancedBackupSettingTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    BackupOptions: Optional[Mapping[str, str]] = None

class BackupJobSummaryTypeDef(BaseModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[BackupJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class RecoveryPointCreatorTypeDef(BaseModel):
    BackupPlanId: Optional[str] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None

class BackupPlanTemplatesListMemberTypeDef(BaseModel):
    BackupPlanTemplateId: Optional[str] = None
    BackupPlanTemplateName: Optional[str] = None

class LifecycleTypeDef(BaseModel):
    MoveToColdStorageAfterDays: Optional[int] = None
    DeleteAfterDays: Optional[int] = None
    OptInToArchiveForSupportedResources: Optional[bool] = None

class ConditionTypeDef(BaseModel):
    ConditionType: Literal["STRINGEQUALS"]
    ConditionKey: str
    ConditionValue: str

class BackupSelectionsListMemberTypeDef(BaseModel):
    SelectionId: Optional[str] = None
    SelectionName: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None
    IamRoleArn: Optional[str] = None

class BackupVaultListMemberTypeDef(BaseModel):
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

class CalculatedLifecycleTypeDef(BaseModel):
    MoveToColdStorageAt: Optional[datetime] = None
    DeleteAt: Optional[datetime] = None

class CancelLegalHoldInputRequestTypeDef(BaseModel):
    LegalHoldId: str
    CancelDescription: str
    RetainRecordInDays: Optional[int] = None

class ConditionParameterTypeDef(BaseModel):
    ConditionKey: Optional[str] = None
    ConditionValue: Optional[str] = None

class ControlInputParameterTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class ControlScopeTypeDef(BaseModel):
    ComplianceResourceIds: Optional[Sequence[str]] = None
    ComplianceResourceTypes: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class CopyJobSummaryTypeDef(BaseModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateBackupVaultInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultTags: Optional[Mapping[str, str]] = None
    EncryptionKeyArn: Optional[str] = None
    CreatorRequestId: Optional[str] = None

class CreateLogicallyAirGappedBackupVaultInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    MinRetentionDays: int
    MaxRetentionDays: int
    BackupVaultTags: Optional[Mapping[str, str]] = None
    CreatorRequestId: Optional[str] = None

class ReportDeliveryChannelTypeDef(BaseModel):
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    Formats: Optional[Sequence[str]] = None

class ReportSettingTypeDef(BaseModel):
    ReportTemplate: str
    FrameworkArns: Optional[Sequence[str]] = None
    NumberOfFrameworks: Optional[int] = None
    Accounts: Optional[Sequence[str]] = None
    OrganizationUnits: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None

class DeleteBackupPlanInputRequestTypeDef(BaseModel):
    BackupPlanId: str

class DeleteBackupSelectionInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    SelectionId: str

class DeleteBackupVaultAccessPolicyInputRequestTypeDef(BaseModel):
    BackupVaultName: str

class DeleteBackupVaultInputRequestTypeDef(BaseModel):
    BackupVaultName: str

class DeleteBackupVaultLockConfigurationInputRequestTypeDef(BaseModel):
    BackupVaultName: str

class DeleteBackupVaultNotificationsInputRequestTypeDef(BaseModel):
    BackupVaultName: str

class DeleteFrameworkInputRequestTypeDef(BaseModel):
    FrameworkName: str

class DeleteRecoveryPointInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str

class DeleteReportPlanInputRequestTypeDef(BaseModel):
    ReportPlanName: str

class DeleteRestoreTestingPlanInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str

class DeleteRestoreTestingSelectionInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str

class DescribeBackupJobInputRequestTypeDef(BaseModel):
    BackupJobId: str

class DescribeBackupVaultInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None

class DescribeCopyJobInputRequestTypeDef(BaseModel):
    CopyJobId: str

class DescribeFrameworkInputRequestTypeDef(BaseModel):
    FrameworkName: str

class DescribeProtectedResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str

class DescribeRecoveryPointInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None

class DescribeReportJobInputRequestTypeDef(BaseModel):
    ReportJobId: str

class DescribeReportPlanInputRequestTypeDef(BaseModel):
    ReportPlanName: str

class DescribeRestoreJobInputRequestTypeDef(BaseModel):
    RestoreJobId: str

class RestoreJobCreatorTypeDef(BaseModel):
    RestoreTestingPlanArn: Optional[str] = None

class DisassociateRecoveryPointFromParentInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str

class DisassociateRecoveryPointInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str

class ExportBackupPlanTemplateInputRequestTypeDef(BaseModel):
    BackupPlanId: str

class FrameworkTypeDef(BaseModel):
    FrameworkName: Optional[str] = None
    FrameworkArn: Optional[str] = None
    FrameworkDescription: Optional[str] = None
    NumberOfControls: Optional[int] = None
    CreationTime: Optional[datetime] = None
    DeploymentStatus: Optional[str] = None

class GetBackupPlanFromJSONInputRequestTypeDef(BaseModel):
    BackupPlanTemplateJson: str

class GetBackupPlanFromTemplateInputRequestTypeDef(BaseModel):
    BackupPlanTemplateId: str

class GetBackupPlanInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    VersionId: Optional[str] = None

class GetBackupSelectionInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    SelectionId: str

class GetBackupVaultAccessPolicyInputRequestTypeDef(BaseModel):
    BackupVaultName: str

class GetBackupVaultNotificationsInputRequestTypeDef(BaseModel):
    BackupVaultName: str

class GetLegalHoldInputRequestTypeDef(BaseModel):
    LegalHoldId: str

class GetRecoveryPointRestoreMetadataInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None

class GetRestoreJobMetadataInputRequestTypeDef(BaseModel):
    RestoreJobId: str

class GetRestoreTestingInferredMetadataInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None

class GetRestoreTestingPlanInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str

class GetRestoreTestingSelectionInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str

class KeyValueTypeDef(BaseModel):
    Key: str
    Value: str

class LegalHoldTypeDef(BaseModel):
    Title: Optional[str] = None
    Status: Optional[LegalHoldStatusType] = None
    Description: Optional[str] = None
    LegalHoldId: Optional[str] = None
    LegalHoldArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CancellationDate: Optional[datetime] = None

class ListBackupJobSummariesInputRequestTypeDef(BaseModel):
    AccountId: Optional[str] = None
    State: Optional[BackupJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBackupPlanTemplatesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBackupPlanVersionsInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBackupPlansInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeDeleted: Optional[bool] = None

class ListBackupSelectionsInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBackupVaultsInputRequestTypeDef(BaseModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCopyJobSummariesInputRequestTypeDef(BaseModel):
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFrameworksInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListLegalHoldsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProtectedResourcesByBackupVaultInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProtectedResourceTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    LastBackupTime: Optional[datetime] = None
    ResourceName: Optional[str] = None
    LastBackupVaultArn: Optional[str] = None
    LastRecoveryPointArn: Optional[str] = None

class ListProtectedResourcesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRecoveryPointsByLegalHoldInputRequestTypeDef(BaseModel):
    LegalHoldId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RecoveryPointMemberTypeDef(BaseModel):
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    BackupVaultName: Optional[str] = None

class ListRecoveryPointsByResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ManagedByAWSBackupOnly: Optional[bool] = None

class RecoveryPointByResourceTypeDef(BaseModel):
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

class ListReportPlansInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRestoreJobSummariesInputRequestTypeDef(BaseModel):
    AccountId: Optional[str] = None
    State: Optional[RestoreJobStateType] = None
    ResourceType: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RestoreJobSummaryTypeDef(BaseModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[RestoreJobStateType] = None
    ResourceType: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ListRestoreTestingPlansInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RestoreTestingPlanForListTypeDef(BaseModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    LastExecutionTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class ListRestoreTestingSelectionsInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RestoreTestingSelectionForListTypeDef(BaseModel):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ValidationWindowHours: Optional[int] = None

class ListTagsInputRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PutBackupVaultAccessPolicyInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    Policy: Optional[str] = None

class PutBackupVaultLockConfigurationInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    MinRetentionDays: Optional[int] = None
    MaxRetentionDays: Optional[int] = None
    ChangeableForDays: Optional[int] = None

class PutBackupVaultNotificationsInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    SNSTopicArn: str
    BackupVaultEvents: Sequence[BackupVaultEventType]

class PutRestoreValidationResultInputRequestTypeDef(BaseModel):
    RestoreJobId: str
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: Optional[str] = None

class ReportDestinationTypeDef(BaseModel):
    S3BucketName: Optional[str] = None
    S3Keys: Optional[List[str]] = None

class RestoreTestingRecoveryPointSelectionTypeDef(BaseModel):
    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithmType] = None
    ExcludeVaults: Optional[Sequence[str]] = None
    IncludeVaults: Optional[Sequence[str]] = None
    RecoveryPointTypes: Optional[Sequence[RestoreTestingRecoveryPointTypeType]] = None
    SelectionWindowDays: Optional[int] = None

class StartReportJobInputRequestTypeDef(BaseModel):
    ReportPlanName: str
    IdempotencyToken: Optional[str] = None

class StartRestoreJobInputRequestTypeDef(BaseModel):
    RecoveryPointArn: str
    Metadata: Mapping[str, str]
    IamRoleArn: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    ResourceType: Optional[str] = None
    CopySourceTagsToRestoredResource: Optional[bool] = None

class StopBackupJobInputRequestTypeDef(BaseModel):
    BackupJobId: str

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeyList: Sequence[str]

class UpdateGlobalSettingsInputRequestTypeDef(BaseModel):
    GlobalSettings: Optional[Mapping[str, str]] = None

class UpdateRegionSettingsInputRequestTypeDef(BaseModel):
    ResourceTypeOptInPreference: Optional[Mapping[str, bool]] = None
    ResourceTypeManagementPreference: Optional[Mapping[str, bool]] = None

class BackupPlansListMemberPaginatorTypeDef(BaseModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    DeletionDate: Optional[datetime] = None
    VersionId: Optional[str] = None
    BackupPlanName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingPaginatorTypeDef]] = None

class BackupPlansListMemberTypeDef(BaseModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    DeletionDate: Optional[datetime] = None
    VersionId: Optional[str] = None
    BackupPlanName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingTypeDef]] = None

class BackupJobTypeDef(BaseModel):
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

class CopyJobTypeDef(BaseModel):
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

class CopyActionTypeDef(BaseModel):
    DestinationBackupVaultArn: str
    Lifecycle: Optional[LifecycleTypeDef] = None

class StartBackupJobInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    ResourceArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompleteWindowMinutes: Optional[int] = None
    Lifecycle: Optional[LifecycleTypeDef] = None
    RecoveryPointTags: Optional[Mapping[str, str]] = None
    BackupOptions: Optional[Mapping[str, str]] = None

class StartCopyJobInputRequestTypeDef(BaseModel):
    RecoveryPointArn: str
    SourceBackupVaultName: str
    DestinationBackupVaultArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    Lifecycle: Optional[LifecycleTypeDef] = None

class UpdateRecoveryPointLifecycleInputRequestTypeDef(BaseModel):
    BackupVaultName: str
    RecoveryPointArn: str
    Lifecycle: Optional[LifecycleTypeDef] = None

class RecoveryPointByBackupVaultTypeDef(BaseModel):
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

class ConditionsTypeDef(BaseModel):
    StringEquals: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringNotEquals: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringLike: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringNotLike: Optional[Sequence[ConditionParameterTypeDef]] = None

class FrameworkControlTypeDef(BaseModel):
    ControlName: str
    ControlInputParameters: Optional[Sequence[ControlInputParameterTypeDef]] = None
    ControlScope: Optional[ControlScopeTypeDef] = None

class CreateBackupPlanOutputTypeDef(BaseModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupSelectionOutputTypeDef(BaseModel):
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupVaultOutputTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFrameworkOutputTypeDef(BaseModel):
    FrameworkName: str
    FrameworkArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLogicallyAirGappedBackupVaultOutputTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    VaultState: VaultStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportPlanOutputTypeDef(BaseModel):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingPlanOutputTypeDef(BaseModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingSelectionOutputTypeDef(BaseModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupPlanOutputTypeDef(BaseModel):
    BackupPlanId: str
    BackupPlanArn: str
    DeletionDate: datetime
    VersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupJobOutputTypeDef(BaseModel):
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

class DescribeBackupVaultOutputTypeDef(BaseModel):
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

class DescribeGlobalSettingsOutputTypeDef(BaseModel):
    GlobalSettings: Dict[str, str]
    LastUpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProtectedResourceOutputTypeDef(BaseModel):
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

class DescribeRecoveryPointOutputTypeDef(BaseModel):
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

class DescribeRegionSettingsOutputTypeDef(BaseModel):
    ResourceTypeOptInPreference: Dict[str, bool]
    ResourceTypeManagementPreference: Dict[str, bool]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportBackupPlanTemplateOutputTypeDef(BaseModel):
    BackupPlanTemplateJson: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupVaultAccessPolicyOutputTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupVaultNotificationsOutputTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultArn: str
    SNSTopicArn: str
    BackupVaultEvents: List[BackupVaultEventType]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryPointRestoreMetadataOutputTypeDef(BaseModel):
    BackupVaultArn: str
    RecoveryPointArn: str
    RestoreMetadata: Dict[str, str]
    ResourceType: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRestoreJobMetadataOutputTypeDef(BaseModel):
    RestoreJobId: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRestoreTestingInferredMetadataOutputTypeDef(BaseModel):
    InferredMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSupportedResourceTypesOutputTypeDef(BaseModel):
    ResourceTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobSummariesOutputTypeDef(BaseModel):
    BackupJobSummaries: List[BackupJobSummaryTypeDef]
    AggregationPeriod: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlanTemplatesOutputTypeDef(BaseModel):
    NextToken: str
    BackupPlanTemplatesList: List[BackupPlanTemplatesListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupSelectionsOutputTypeDef(BaseModel):
    NextToken: str
    BackupSelectionsList: List[BackupSelectionsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupVaultsOutputTypeDef(BaseModel):
    BackupVaultList: List[BackupVaultListMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCopyJobSummariesOutputTypeDef(BaseModel):
    CopyJobSummaries: List[CopyJobSummaryTypeDef]
    AggregationPeriod: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsOutputTypeDef(BaseModel):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartBackupJobOutputTypeDef(BaseModel):
    BackupJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartCopyJobOutputTypeDef(BaseModel):
    CopyJobId: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartReportJobOutputTypeDef(BaseModel):
    ReportJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartRestoreJobOutputTypeDef(BaseModel):
    RestoreJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackupPlanOutputTypeDef(BaseModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFrameworkOutputTypeDef(BaseModel):
    FrameworkName: str
    FrameworkArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecoveryPointLifecycleOutputTypeDef(BaseModel):
    BackupVaultArn: str
    RecoveryPointArn: str
    Lifecycle: LifecycleTypeDef
    CalculatedLifecycle: CalculatedLifecycleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportPlanOutputTypeDef(BaseModel):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingPlanOutputTypeDef(BaseModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingSelectionOutputTypeDef(BaseModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReportPlanInputRequestTypeDef(BaseModel):
    ReportPlanName: str
    ReportDeliveryChannel: ReportDeliveryChannelTypeDef
    ReportSetting: ReportSettingTypeDef
    ReportPlanDescription: Optional[str] = None
    ReportPlanTags: Optional[Mapping[str, str]] = None
    IdempotencyToken: Optional[str] = None

class ReportPlanTypeDef(BaseModel):
    ReportPlanArn: Optional[str] = None
    ReportPlanName: Optional[str] = None
    ReportPlanDescription: Optional[str] = None
    ReportSetting: Optional[ReportSettingTypeDef] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelTypeDef] = None
    DeploymentStatus: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAttemptedExecutionTime: Optional[datetime] = None
    LastSuccessfulExecutionTime: Optional[datetime] = None

class UpdateReportPlanInputRequestTypeDef(BaseModel):
    ReportPlanName: str
    ReportPlanDescription: Optional[str] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelTypeDef] = None
    ReportSetting: Optional[ReportSettingTypeDef] = None
    IdempotencyToken: Optional[str] = None

class DateRangeTypeDef(BaseModel):
    FromDate: TimestampTypeDef
    ToDate: TimestampTypeDef

class ListBackupJobsInputRequestTypeDef(BaseModel):
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

class ListCopyJobsInputRequestTypeDef(BaseModel):
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

class ListRecoveryPointsByBackupVaultInputRequestTypeDef(BaseModel):
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

class ListReportJobsInputRequestTypeDef(BaseModel):
    ByReportPlanName: Optional[str] = None
    ByCreationBefore: Optional[TimestampTypeDef] = None
    ByCreationAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRestoreJobsByProtectedResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    ByStatus: Optional[RestoreJobStatusType] = None
    ByRecoveryPointCreationDateAfter: Optional[TimestampTypeDef] = None
    ByRecoveryPointCreationDateBefore: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRestoreJobsInputRequestTypeDef(BaseModel):
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

class DescribeRestoreJobOutputTypeDef(BaseModel):
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

class RestoreJobsListMemberTypeDef(BaseModel):
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

class ListFrameworksOutputTypeDef(BaseModel):
    Frameworks: List[FrameworkTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectedResourceConditionsTypeDef(BaseModel):
    StringEquals: Optional[Sequence[KeyValueTypeDef]] = None
    StringNotEquals: Optional[Sequence[KeyValueTypeDef]] = None

class ListLegalHoldsOutputTypeDef(BaseModel):
    NextToken: str
    LegalHolds: List[LegalHoldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobsInputListBackupJobsPaginateTypeDef(BaseModel):
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

class ListBackupPlanTemplatesInputListBackupPlanTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupPlanVersionsInputListBackupPlanVersionsPaginateTypeDef(BaseModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupPlansInputListBackupPlansPaginateTypeDef(BaseModel):
    IncludeDeleted: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupSelectionsInputListBackupSelectionsPaginateTypeDef(BaseModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBackupVaultsInputListBackupVaultsPaginateTypeDef(BaseModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCopyJobsInputListCopyJobsPaginateTypeDef(BaseModel):
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

class ListLegalHoldsInputListLegalHoldsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedResourcesByBackupVaultInputListProtectedResourcesByBackupVaultPaginateTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedResourcesInputListProtectedResourcesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsByBackupVaultInputListRecoveryPointsByBackupVaultPaginateTypeDef(BaseModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    ByResourceArn: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByBackupPlanId: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByParentRecoveryPointArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsByLegalHoldInputListRecoveryPointsByLegalHoldPaginateTypeDef(BaseModel):
    LegalHoldId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryPointsByResourceInputListRecoveryPointsByResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    ManagedByAWSBackupOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRestoreJobsInputListRestoreJobsPaginateTypeDef(BaseModel):
    ByAccountId: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[RestoreJobStatusType] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByRestoreTestingPlanArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRestoreTestingPlansInputListRestoreTestingPlansPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRestoreTestingSelectionsInputListRestoreTestingSelectionsPaginateTypeDef(BaseModel):
    RestoreTestingPlanName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedResourcesByBackupVaultOutputTypeDef(BaseModel):
    Results: List[ProtectedResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectedResourcesOutputTypeDef(BaseModel):
    Results: List[ProtectedResourceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsByLegalHoldOutputTypeDef(BaseModel):
    RecoveryPoints: List[RecoveryPointMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryPointsByResourceOutputTypeDef(BaseModel):
    NextToken: str
    RecoveryPoints: List[RecoveryPointByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreJobSummariesOutputTypeDef(BaseModel):
    RestoreJobSummaries: List[RestoreJobSummaryTypeDef]
    AggregationPeriod: str
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreTestingPlansOutputTypeDef(BaseModel):
    NextToken: str
    RestoreTestingPlans: List[RestoreTestingPlanForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreTestingSelectionsOutputTypeDef(BaseModel):
    NextToken: str
    RestoreTestingSelections: List[RestoreTestingSelectionForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReportJobTypeDef(BaseModel):
    ReportJobId: Optional[str] = None
    ReportPlanArn: Optional[str] = None
    ReportTemplate: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    ReportDestination: Optional[ReportDestinationTypeDef] = None

class RestoreTestingPlanForCreateTypeDef(BaseModel):
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionTypeDef
    RestoreTestingPlanName: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class RestoreTestingPlanForGetTypeDef(BaseModel):
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

class RestoreTestingPlanForUpdateTypeDef(BaseModel):
    RecoveryPointSelection: Optional[RestoreTestingRecoveryPointSelectionTypeDef] = None
    ScheduleExpression: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

class ListBackupPlanVersionsOutputPaginatorTypeDef(BaseModel):
    NextToken: str
    BackupPlanVersionsList: List[BackupPlansListMemberPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlansOutputPaginatorTypeDef(BaseModel):
    NextToken: str
    BackupPlansList: List[BackupPlansListMemberPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlanVersionsOutputTypeDef(BaseModel):
    NextToken: str
    BackupPlanVersionsList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupPlansOutputTypeDef(BaseModel):
    NextToken: str
    BackupPlansList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupJobsOutputTypeDef(BaseModel):
    BackupJobs: List[BackupJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCopyJobOutputTypeDef(BaseModel):
    CopyJob: CopyJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCopyJobsOutputTypeDef(BaseModel):
    CopyJobs: List[CopyJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BackupRuleInputTypeDef(BaseModel):
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

class BackupRuleTypeDef(BaseModel):
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

class ListRecoveryPointsByBackupVaultOutputTypeDef(BaseModel):
    NextToken: str
    RecoveryPoints: List[RecoveryPointByBackupVaultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BackupSelectionTypeDef(BaseModel):
    SelectionName: str
    IamRoleArn: str
    Resources: Optional[Sequence[str]] = None
    ListOfTags: Optional[Sequence[ConditionTypeDef]] = None
    NotResources: Optional[Sequence[str]] = None
    Conditions: Optional[ConditionsTypeDef] = None

class CreateFrameworkInputRequestTypeDef(BaseModel):
    FrameworkName: str
    FrameworkControls: Sequence[FrameworkControlTypeDef]
    FrameworkDescription: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    FrameworkTags: Optional[Mapping[str, str]] = None

class DescribeFrameworkOutputTypeDef(BaseModel):
    FrameworkName: str
    FrameworkArn: str
    FrameworkDescription: str
    FrameworkControls: List[FrameworkControlTypeDef]
    CreationTime: datetime
    DeploymentStatus: str
    FrameworkStatus: str
    IdempotencyToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFrameworkInputRequestTypeDef(BaseModel):
    FrameworkName: str
    FrameworkDescription: Optional[str] = None
    FrameworkControls: Optional[Sequence[FrameworkControlTypeDef]] = None
    IdempotencyToken: Optional[str] = None

class DescribeReportPlanOutputTypeDef(BaseModel):
    ReportPlan: ReportPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportPlansOutputTypeDef(BaseModel):
    ReportPlans: List[ReportPlanTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecoveryPointSelectionTypeDef(BaseModel):
    VaultNames: Optional[Sequence[str]] = None
    ResourceIdentifiers: Optional[Sequence[str]] = None
    DateRange: Optional[DateRangeTypeDef] = None

class ListRestoreJobsByProtectedResourceOutputTypeDef(BaseModel):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRestoreJobsOutputTypeDef(BaseModel):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTestingSelectionForCreateTypeDef(BaseModel):
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingSelectionName: str
    ProtectedResourceArns: Optional[Sequence[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsTypeDef] = None
    RestoreMetadataOverrides: Optional[Mapping[str, str]] = None
    ValidationWindowHours: Optional[int] = None

class RestoreTestingSelectionForGetTypeDef(BaseModel):
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

class RestoreTestingSelectionForUpdateTypeDef(BaseModel):
    IamRoleArn: Optional[str] = None
    ProtectedResourceArns: Optional[Sequence[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsTypeDef] = None
    RestoreMetadataOverrides: Optional[Mapping[str, str]] = None
    ValidationWindowHours: Optional[int] = None

class DescribeReportJobOutputTypeDef(BaseModel):
    ReportJob: ReportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReportJobsOutputTypeDef(BaseModel):
    ReportJobs: List[ReportJobTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreTestingPlanInputRequestTypeDef(BaseModel):
    RestoreTestingPlan: RestoreTestingPlanForCreateTypeDef
    CreatorRequestId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class GetRestoreTestingPlanOutputTypeDef(BaseModel):
    RestoreTestingPlan: RestoreTestingPlanForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingPlanInputRequestTypeDef(BaseModel):
    RestoreTestingPlan: RestoreTestingPlanForUpdateTypeDef
    RestoreTestingPlanName: str

class BackupPlanInputTypeDef(BaseModel):
    BackupPlanName: str
    Rules: Sequence[BackupRuleInputTypeDef]
    AdvancedBackupSettings: Optional[Sequence[AdvancedBackupSettingTypeDef]] = None

class BackupPlanTypeDef(BaseModel):
    BackupPlanName: str
    Rules: List[BackupRuleTypeDef]
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingTypeDef]] = None

class CreateBackupSelectionInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    BackupSelection: BackupSelectionTypeDef
    CreatorRequestId: Optional[str] = None

class GetBackupSelectionOutputTypeDef(BaseModel):
    BackupSelection: BackupSelectionTypeDef
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLegalHoldInputRequestTypeDef(BaseModel):
    Title: str
    Description: str
    IdempotencyToken: Optional[str] = None
    RecoveryPointSelection: Optional[RecoveryPointSelectionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateLegalHoldOutputTypeDef(BaseModel):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    RecoveryPointSelection: RecoveryPointSelectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLegalHoldOutputTypeDef(BaseModel):
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

class CreateRestoreTestingSelectionInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForCreateTypeDef
    CreatorRequestId: Optional[str] = None

class GetRestoreTestingSelectionOutputTypeDef(BaseModel):
    RestoreTestingSelection: RestoreTestingSelectionForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRestoreTestingSelectionInputRequestTypeDef(BaseModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForUpdateTypeDef
    RestoreTestingSelectionName: str

class CreateBackupPlanInputRequestTypeDef(BaseModel):
    BackupPlan: BackupPlanInputTypeDef
    BackupPlanTags: Optional[Mapping[str, str]] = None
    CreatorRequestId: Optional[str] = None

class UpdateBackupPlanInputRequestTypeDef(BaseModel):
    BackupPlanId: str
    BackupPlan: BackupPlanInputTypeDef

class GetBackupPlanFromJSONOutputTypeDef(BaseModel):
    BackupPlan: BackupPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupPlanFromTemplateOutputTypeDef(BaseModel):
    BackupPlanDocument: BackupPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackupPlanOutputTypeDef(BaseModel):
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

