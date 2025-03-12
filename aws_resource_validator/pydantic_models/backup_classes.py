from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class AdvancedBackupSettingOutputTypeDef(BaseValidatorModel):
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


class IndexActionOutputTypeDef(BaseValidatorModel):
    ResourceTypes: Optional[List[str]] = None


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
    VaultType: Optional[VaultTypeType] = None
    VaultState: Optional[VaultStateType] = None
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


class CancelLegalHoldInputTypeDef(BaseValidatorModel):
    LegalHoldId: str
    CancelDescription: str
    RetainRecordInDays: Optional[int] = None


class ConditionParameterTypeDef(BaseValidatorModel):
    ConditionKey: Optional[str] = None
    ConditionValue: Optional[str] = None


class ControlInputParameterTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class ControlScopeOutputTypeDef(BaseValidatorModel):
    ComplianceResourceIds: Optional[List[str]] = None
    ComplianceResourceTypes: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


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


class CreateBackupVaultInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultTags: Optional[Mapping[str, str]] = None
    EncryptionKeyArn: Optional[str] = None
    CreatorRequestId: Optional[str] = None


class CreateLogicallyAirGappedBackupVaultInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    MinRetentionDays: int
    MaxRetentionDays: int
    BackupVaultTags: Optional[Mapping[str, str]] = None
    CreatorRequestId: Optional[str] = None


class DateRangeOutputTypeDef(BaseValidatorModel):
    FromDate: datetime
    ToDate: datetime


class DeleteBackupPlanInputTypeDef(BaseValidatorModel):
    BackupPlanId: str


class DeleteBackupSelectionInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    SelectionId: str


class DeleteBackupVaultAccessPolicyInputTypeDef(BaseValidatorModel):
    BackupVaultName: str


class DeleteBackupVaultInputTypeDef(BaseValidatorModel):
    BackupVaultName: str


class DeleteBackupVaultLockConfigurationInputTypeDef(BaseValidatorModel):
    BackupVaultName: str


class DeleteBackupVaultNotificationsInputTypeDef(BaseValidatorModel):
    BackupVaultName: str


class DeleteFrameworkInputTypeDef(BaseValidatorModel):
    FrameworkName: str


class DeleteRecoveryPointInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class DeleteReportPlanInputTypeDef(BaseValidatorModel):
    ReportPlanName: str


class DeleteRestoreTestingPlanInputTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str


class DeleteRestoreTestingSelectionInputTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str


class DescribeBackupJobInputTypeDef(BaseValidatorModel):
    BackupJobId: str


class DescribeBackupVaultInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None


class DescribeCopyJobInputTypeDef(BaseValidatorModel):
    CopyJobId: str


class DescribeFrameworkInputTypeDef(BaseValidatorModel):
    FrameworkName: str


class DescribeProtectedResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str


class DescribeRecoveryPointInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None


class DescribeReportJobInputTypeDef(BaseValidatorModel):
    ReportJobId: str


class DescribeReportPlanInputTypeDef(BaseValidatorModel):
    ReportPlanName: str


class DescribeRestoreJobInputTypeDef(BaseValidatorModel):
    RestoreJobId: str


class RestoreJobCreatorTypeDef(BaseValidatorModel):
    RestoreTestingPlanArn: Optional[str] = None


class DisassociateRecoveryPointFromParentInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class DisassociateRecoveryPointInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class ExportBackupPlanTemplateInputTypeDef(BaseValidatorModel):
    BackupPlanId: str


class FrameworkTypeDef(BaseValidatorModel):
    FrameworkName: Optional[str] = None
    FrameworkArn: Optional[str] = None
    FrameworkDescription: Optional[str] = None
    NumberOfControls: Optional[int] = None
    CreationTime: Optional[datetime] = None
    DeploymentStatus: Optional[str] = None


class GetBackupPlanFromJSONInputTypeDef(BaseValidatorModel):
    BackupPlanTemplateJson: str


class GetBackupPlanFromTemplateInputTypeDef(BaseValidatorModel):
    BackupPlanTemplateId: str


class GetBackupPlanInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    VersionId: Optional[str] = None


class GetBackupSelectionInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    SelectionId: str


class GetBackupVaultAccessPolicyInputTypeDef(BaseValidatorModel):
    BackupVaultName: str


class GetBackupVaultNotificationsInputTypeDef(BaseValidatorModel):
    BackupVaultName: str


class GetLegalHoldInputTypeDef(BaseValidatorModel):
    LegalHoldId: str


class GetRecoveryPointIndexDetailsInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class GetRecoveryPointRestoreMetadataInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None


class GetRestoreJobMetadataInputTypeDef(BaseValidatorModel):
    RestoreJobId: str


class GetRestoreTestingInferredMetadataInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None


class GetRestoreTestingPlanInputTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str


class GetRestoreTestingSelectionInputTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str


class IndexActionTypeDef(BaseValidatorModel):
    ResourceTypes: Optional[Sequence[str]] = None


class IndexedRecoveryPointTypeDef(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    IamRoleArn: Optional[str] = None
    BackupCreationDate: Optional[datetime] = None
    ResourceType: Optional[str] = None
    IndexCreationDate: Optional[datetime] = None
    IndexStatus: Optional[IndexStatusType] = None
    IndexStatusMessage: Optional[str] = None
    BackupVaultArn: Optional[str] = None


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


class ListBackupJobSummariesInputTypeDef(BaseValidatorModel):
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


class ListBackupPlanTemplatesInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBackupPlanVersionsInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBackupPlansInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeDeleted: Optional[bool] = None


class ListBackupSelectionsInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBackupVaultsInputTypeDef(BaseValidatorModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCopyJobSummariesInputTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFrameworksInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLegalHoldsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProtectedResourcesByBackupVaultInputTypeDef(BaseValidatorModel):
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


class ListProtectedResourcesInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRecoveryPointsByLegalHoldInputTypeDef(BaseValidatorModel):
    LegalHoldId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RecoveryPointMemberTypeDef(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    BackupVaultName: Optional[str] = None


class ListRecoveryPointsByResourceInputTypeDef(BaseValidatorModel):
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
    IndexStatus: Optional[IndexStatusType] = None
    IndexStatusMessage: Optional[str] = None


class ListReportPlansInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRestoreJobSummariesInputTypeDef(BaseValidatorModel):
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


class ListRestoreTestingPlansInputTypeDef(BaseValidatorModel):
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


class ListRestoreTestingSelectionsInputTypeDef(BaseValidatorModel):
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


class ListTagsInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PutBackupVaultAccessPolicyInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    Policy: Optional[str] = None


class PutBackupVaultLockConfigurationInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    MinRetentionDays: Optional[int] = None
    MaxRetentionDays: Optional[int] = None
    ChangeableForDays: Optional[int] = None


class PutBackupVaultNotificationsInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    SNSTopicArn: str
    BackupVaultEvents: Sequence[BackupVaultEventType]


class PutRestoreValidationResultInputTypeDef(BaseValidatorModel):
    RestoreJobId: str
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: Optional[str] = None


class ReportDeliveryChannelOutputTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    Formats: Optional[List[str]] = None


class ReportDeliveryChannelTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    Formats: Optional[Sequence[str]] = None


class ReportDestinationTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Keys: Optional[List[str]] = None


class ReportSettingOutputTypeDef(BaseValidatorModel):
    ReportTemplate: str
    FrameworkArns: Optional[List[str]] = None
    NumberOfFrameworks: Optional[int] = None
    Accounts: Optional[List[str]] = None
    OrganizationUnits: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class ReportSettingTypeDef(BaseValidatorModel):
    ReportTemplate: str
    FrameworkArns: Optional[Sequence[str]] = None
    NumberOfFrameworks: Optional[int] = None
    Accounts: Optional[Sequence[str]] = None
    OrganizationUnits: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None


class RestoreTestingRecoveryPointSelectionOutputTypeDef(BaseValidatorModel):
    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithmType] = None
    ExcludeVaults: Optional[List[str]] = None
    IncludeVaults: Optional[List[str]] = None
    RecoveryPointTypes: Optional[List[RestoreTestingRecoveryPointTypeType]] = None
    SelectionWindowDays: Optional[int] = None


class RestoreTestingRecoveryPointSelectionTypeDef(BaseValidatorModel):
    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithmType] = None
    ExcludeVaults: Optional[Sequence[str]] = None
    IncludeVaults: Optional[Sequence[str]] = None
    RecoveryPointTypes: Optional[Sequence[RestoreTestingRecoveryPointTypeType]] = None
    SelectionWindowDays: Optional[int] = None


class StartReportJobInputTypeDef(BaseValidatorModel):
    ReportPlanName: str
    IdempotencyToken: Optional[str] = None


class StartRestoreJobInputTypeDef(BaseValidatorModel):
    RecoveryPointArn: str
    Metadata: Mapping[str, str]
    IamRoleArn: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    ResourceType: Optional[str] = None
    CopySourceTagsToRestoredResource: Optional[bool] = None


class StopBackupJobInputTypeDef(BaseValidatorModel):
    BackupJobId: str


class TagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeyList: Sequence[str]


class UpdateGlobalSettingsInputTypeDef(BaseValidatorModel):
    GlobalSettings: Optional[Mapping[str, str]] = None


class UpdateRecoveryPointIndexSettingsInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    Index: IndexType
    IamRoleArn: Optional[str] = None


class UpdateRegionSettingsInputTypeDef(BaseValidatorModel):
    ResourceTypeOptInPreference: Optional[Mapping[str, bool]] = None
    ResourceTypeManagementPreference: Optional[Mapping[str, bool]] = None


class BackupPlansListMemberTypeDef(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    DeletionDate: Optional[datetime] = None
    VersionId: Optional[str] = None
    BackupPlanName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingOutputTypeDef]] = None


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


class StartBackupJobInputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    ResourceArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompleteWindowMinutes: Optional[int] = None
    Lifecycle: Optional[LifecycleTypeDef] = None
    RecoveryPointTags: Optional[Mapping[str, str]] = None
    BackupOptions: Optional[Mapping[str, str]] = None
    Index: Optional[IndexType] = None


class StartCopyJobInputTypeDef(BaseValidatorModel):
    RecoveryPointArn: str
    SourceBackupVaultName: str
    DestinationBackupVaultArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    Lifecycle: Optional[LifecycleTypeDef] = None


class UpdateRecoveryPointLifecycleInputTypeDef(BaseValidatorModel):
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
    IndexStatus: Optional[IndexStatusType] = None
    IndexStatusMessage: Optional[str] = None


class ConditionsOutputTypeDef(BaseValidatorModel):
    StringEquals: Optional[List[ConditionParameterTypeDef]] = None
    StringNotEquals: Optional[List[ConditionParameterTypeDef]] = None
    StringLike: Optional[List[ConditionParameterTypeDef]] = None
    StringNotLike: Optional[List[ConditionParameterTypeDef]] = None


class ConditionsTypeDef(BaseValidatorModel):
    StringEquals: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringNotEquals: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringLike: Optional[Sequence[ConditionParameterTypeDef]] = None
    StringNotLike: Optional[Sequence[ConditionParameterTypeDef]] = None


class FrameworkControlOutputTypeDef(BaseValidatorModel):
    ControlName: str
    ControlInputParameters: Optional[List[ControlInputParameterTypeDef]] = None
    ControlScope: Optional[ControlScopeOutputTypeDef] = None


class CreateBackupPlanOutputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingOutputTypeDef]
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
    VaultState: VaultStateType
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
    IndexStatus: IndexStatusType
    IndexStatusMessage: str
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


class GetRecoveryPointIndexDetailsOutputTypeDef(BaseValidatorModel):
    RecoveryPointArn: str
    BackupVaultArn: str
    SourceResourceArn: str
    IndexCreationDate: datetime
    IndexDeletionDate: datetime
    IndexCompletionDate: datetime
    IndexStatus: IndexStatusType
    IndexStatusMessage: str
    TotalItemsIndexed: int
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBackupPlanTemplatesOutputTypeDef(BaseValidatorModel):
    BackupPlanTemplatesList: List[BackupPlanTemplatesListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBackupSelectionsOutputTypeDef(BaseValidatorModel):
    BackupSelectionsList: List[BackupSelectionsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBackupVaultsOutputTypeDef(BaseValidatorModel):
    BackupVaultList: List[BackupVaultListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCopyJobSummariesOutputTypeDef(BaseValidatorModel):
    CopyJobSummaries: List[CopyJobSummaryTypeDef]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    AdvancedBackupSettings: List[AdvancedBackupSettingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFrameworkOutputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRecoveryPointIndexSettingsOutputTypeDef(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    IndexStatus: IndexStatusType
    Index: IndexType
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


class RecoveryPointSelectionOutputTypeDef(BaseValidatorModel):
    VaultNames: Optional[List[str]] = None
    ResourceIdentifiers: Optional[List[str]] = None
    DateRange: Optional[DateRangeOutputTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DateRangeTypeDef(BaseValidatorModel):
    FromDate: TimestampTypeDef
    ToDate: TimestampTypeDef


class ListBackupJobsInputTypeDef(BaseValidatorModel):
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


class ListCopyJobsInputTypeDef(BaseValidatorModel):
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


class ListIndexedRecoveryPointsInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SourceResourceArn: Optional[str] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    ResourceType: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None


class ListRecoveryPointsByBackupVaultInputTypeDef(BaseValidatorModel):
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


class ListReportJobsInputTypeDef(BaseValidatorModel):
    ByReportPlanName: Optional[str] = None
    ByCreationBefore: Optional[TimestampTypeDef] = None
    ByCreationAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRestoreJobsByProtectedResourceInputTypeDef(BaseValidatorModel):
    ResourceArn: str
    ByStatus: Optional[RestoreJobStatusType] = None
    ByRecoveryPointCreationDateAfter: Optional[TimestampTypeDef] = None
    ByRecoveryPointCreationDateBefore: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRestoreJobsInputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIndexedRecoveryPointsOutputTypeDef(BaseValidatorModel):
    IndexedRecoveryPoints: List[IndexedRecoveryPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ProtectedResourceConditionsOutputTypeDef(BaseValidatorModel):
    StringEquals: Optional[List[KeyValueTypeDef]] = None
    StringNotEquals: Optional[List[KeyValueTypeDef]] = None


class ProtectedResourceConditionsTypeDef(BaseValidatorModel):
    StringEquals: Optional[Sequence[KeyValueTypeDef]] = None
    StringNotEquals: Optional[Sequence[KeyValueTypeDef]] = None


class ListLegalHoldsOutputTypeDef(BaseValidatorModel):
    LegalHolds: List[LegalHoldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBackupJobsInputPaginateTypeDef(BaseValidatorModel):
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


class ListBackupPlanTemplatesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBackupPlanVersionsInputPaginateTypeDef(BaseValidatorModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBackupPlansInputPaginateTypeDef(BaseValidatorModel):
    IncludeDeleted: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBackupSelectionsInputPaginateTypeDef(BaseValidatorModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBackupVaultsInputPaginateTypeDef(BaseValidatorModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCopyJobsInputPaginateTypeDef(BaseValidatorModel):
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


class ListIndexedRecoveryPointsInputPaginateTypeDef(BaseValidatorModel):
    SourceResourceArn: Optional[str] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    ResourceType: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLegalHoldsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProtectedResourcesByBackupVaultInputPaginateTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProtectedResourcesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecoveryPointsByBackupVaultInputPaginateTypeDef(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    ByResourceArn: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByBackupPlanId: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByParentRecoveryPointArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecoveryPointsByLegalHoldInputPaginateTypeDef(BaseValidatorModel):
    LegalHoldId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecoveryPointsByResourceInputPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    ManagedByAWSBackupOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRestoreJobsByProtectedResourceInputPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    ByStatus: Optional[RestoreJobStatusType] = None
    ByRecoveryPointCreationDateAfter: Optional[TimestampTypeDef] = None
    ByRecoveryPointCreationDateBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRestoreJobsInputPaginateTypeDef(BaseValidatorModel):
    ByAccountId: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByCreatedBefore: Optional[TimestampTypeDef] = None
    ByCreatedAfter: Optional[TimestampTypeDef] = None
    ByStatus: Optional[RestoreJobStatusType] = None
    ByCompleteBefore: Optional[TimestampTypeDef] = None
    ByCompleteAfter: Optional[TimestampTypeDef] = None
    ByRestoreTestingPlanArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRestoreTestingPlansInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRestoreTestingSelectionsInputPaginateTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProtectedResourcesByBackupVaultOutputTypeDef(BaseValidatorModel):
    Results: List[ProtectedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProtectedResourcesOutputTypeDef(BaseValidatorModel):
    Results: List[ProtectedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRecoveryPointsByLegalHoldOutputTypeDef(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRecoveryPointsByResourceOutputTypeDef(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRestoreJobSummariesOutputTypeDef(BaseValidatorModel):
    RestoreJobSummaries: List[RestoreJobSummaryTypeDef]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRestoreTestingPlansOutputTypeDef(BaseValidatorModel):
    RestoreTestingPlans: List[RestoreTestingPlanForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRestoreTestingSelectionsOutputTypeDef(BaseValidatorModel):
    RestoreTestingSelections: List[RestoreTestingSelectionForListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ReportJobTypeDef(BaseValidatorModel):
    ReportJobId: Optional[str] = None
    ReportPlanArn: Optional[str] = None
    ReportTemplate: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    ReportDestination: Optional[ReportDestinationTypeDef] = None


class ReportPlanTypeDef(BaseValidatorModel):
    ReportPlanArn: Optional[str] = None
    ReportPlanName: Optional[str] = None
    ReportPlanDescription: Optional[str] = None
    ReportSetting: Optional[ReportSettingOutputTypeDef] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelOutputTypeDef] = None
    DeploymentStatus: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAttemptedExecutionTime: Optional[datetime] = None
    LastSuccessfulExecutionTime: Optional[datetime] = None


class RestoreTestingPlanForGetTypeDef(BaseValidatorModel):
    CreationTime: datetime
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionOutputTypeDef
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    CreatorRequestId: Optional[str] = None
    LastExecutionTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None


class ListBackupPlanVersionsOutputTypeDef(BaseValidatorModel):
    BackupPlanVersionsList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBackupPlansOutputTypeDef(BaseValidatorModel):
    BackupPlansList: List[BackupPlansListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListBackupJobsOutputTypeDef(BaseValidatorModel):
    BackupJobs: List[BackupJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeCopyJobOutputTypeDef(BaseValidatorModel):
    CopyJob: CopyJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCopyJobsOutputTypeDef(BaseValidatorModel):
    CopyJobs: List[CopyJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    IndexActions: Optional[List[IndexActionOutputTypeDef]] = None


class ListRecoveryPointsByBackupVaultOutputTypeDef(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointByBackupVaultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BackupSelectionOutputTypeDef(BaseValidatorModel):
    SelectionName: str
    IamRoleArn: str
    Resources: Optional[List[str]] = None
    ListOfTags: Optional[List[ConditionTypeDef]] = None
    NotResources: Optional[List[str]] = None
    Conditions: Optional[ConditionsOutputTypeDef] = None


class BackupSelectionTypeDef(BaseValidatorModel):
    SelectionName: str
    IamRoleArn: str
    Resources: Optional[Sequence[str]] = None
    ListOfTags: Optional[Sequence[ConditionTypeDef]] = None
    NotResources: Optional[Sequence[str]] = None
    Conditions: Optional[ConditionsTypeDef] = None


class DescribeFrameworkOutputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    FrameworkDescription: str
    FrameworkControls: List[FrameworkControlOutputTypeDef]
    CreationTime: datetime
    DeploymentStatus: str
    FrameworkStatus: str
    IdempotencyToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ControlScopeUnionTypeDef(BaseValidatorModel):
    pass


class FrameworkControlTypeDef(BaseValidatorModel):
    ControlName: str
    ControlInputParameters: Optional[Sequence[ControlInputParameterTypeDef]] = None
    ControlScope: Optional[ControlScopeUnionTypeDef] = None


class CreateLegalHoldOutputTypeDef(BaseValidatorModel):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    RecoveryPointSelection: RecoveryPointSelectionOutputTypeDef
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
    RecoveryPointSelection: RecoveryPointSelectionOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RecoveryPointSelectionTypeDef(BaseValidatorModel):
    VaultNames: Optional[Sequence[str]] = None
    ResourceIdentifiers: Optional[Sequence[str]] = None
    DateRange: Optional[DateRangeTypeDef] = None


class ListRestoreJobsByProtectedResourceOutputTypeDef(BaseValidatorModel):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRestoreJobsOutputTypeDef(BaseValidatorModel):
    RestoreJobs: List[RestoreJobsListMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IndexActionUnionTypeDef(BaseValidatorModel):
    pass


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
    IndexActions: Optional[Sequence[IndexActionUnionTypeDef]] = None


class RestoreTestingSelectionForGetTypeDef(BaseValidatorModel):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    CreatorRequestId: Optional[str] = None
    ProtectedResourceArns: Optional[List[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsOutputTypeDef] = None
    RestoreMetadataOverrides: Optional[Dict[str, str]] = None
    ValidationWindowHours: Optional[int] = None


class DescribeReportJobOutputTypeDef(BaseValidatorModel):
    ReportJob: ReportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListReportJobsOutputTypeDef(BaseValidatorModel):
    ReportJobs: List[ReportJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeReportPlanOutputTypeDef(BaseValidatorModel):
    ReportPlan: ReportPlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListReportPlansOutputTypeDef(BaseValidatorModel):
    ReportPlans: List[ReportPlanTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ReportDeliveryChannelUnionTypeDef(BaseValidatorModel):
    pass


class ReportSettingUnionTypeDef(BaseValidatorModel):
    pass


class CreateReportPlanInputTypeDef(BaseValidatorModel):
    ReportPlanName: str
    ReportDeliveryChannel: ReportDeliveryChannelUnionTypeDef
    ReportSetting: ReportSettingUnionTypeDef
    ReportPlanDescription: Optional[str] = None
    ReportPlanTags: Optional[Mapping[str, str]] = None
    IdempotencyToken: Optional[str] = None


class UpdateReportPlanInputTypeDef(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanDescription: Optional[str] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelUnionTypeDef] = None
    ReportSetting: Optional[ReportSettingUnionTypeDef] = None
    IdempotencyToken: Optional[str] = None


class GetRestoreTestingPlanOutputTypeDef(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreTestingRecoveryPointSelectionUnionTypeDef(BaseValidatorModel):
    pass


class RestoreTestingPlanForCreateTypeDef(BaseValidatorModel):
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionUnionTypeDef
    RestoreTestingPlanName: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None


class RestoreTestingPlanForUpdateTypeDef(BaseValidatorModel):
    RecoveryPointSelection: Optional[RestoreTestingRecoveryPointSelectionUnionTypeDef] = None
    ScheduleExpression: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None


class BackupPlanTypeDef(BaseValidatorModel):
    BackupPlanName: str
    Rules: List[BackupRuleTypeDef]
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingOutputTypeDef]] = None


class GetBackupSelectionOutputTypeDef(BaseValidatorModel):
    BackupSelection: BackupSelectionOutputTypeDef
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AdvancedBackupSettingUnionTypeDef(BaseValidatorModel):
    pass


class BackupPlanInputTypeDef(BaseValidatorModel):
    BackupPlanName: str
    Rules: Sequence[BackupRuleInputTypeDef]
    AdvancedBackupSettings: Optional[Sequence[AdvancedBackupSettingUnionTypeDef]] = None


class GetRestoreTestingSelectionOutputTypeDef(BaseValidatorModel):
    RestoreTestingSelection: RestoreTestingSelectionForGetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ProtectedResourceConditionsUnionTypeDef(BaseValidatorModel):
    pass


class RestoreTestingSelectionForCreateTypeDef(BaseValidatorModel):
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingSelectionName: str
    ProtectedResourceArns: Optional[Sequence[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsUnionTypeDef] = None
    RestoreMetadataOverrides: Optional[Mapping[str, str]] = None
    ValidationWindowHours: Optional[int] = None


class RestoreTestingSelectionForUpdateTypeDef(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    ProtectedResourceArns: Optional[Sequence[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsUnionTypeDef] = None
    RestoreMetadataOverrides: Optional[Mapping[str, str]] = None
    ValidationWindowHours: Optional[int] = None


class CreateRestoreTestingPlanInputTypeDef(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForCreateTypeDef
    CreatorRequestId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateRestoreTestingPlanInputTypeDef(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForUpdateTypeDef
    RestoreTestingPlanName: str


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
    AdvancedBackupSettings: List[AdvancedBackupSettingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BackupSelectionUnionTypeDef(BaseValidatorModel):
    pass


class CreateBackupSelectionInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupSelection: BackupSelectionUnionTypeDef
    CreatorRequestId: Optional[str] = None


class FrameworkControlUnionTypeDef(BaseValidatorModel):
    pass


class CreateFrameworkInputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkControls: Sequence[FrameworkControlUnionTypeDef]
    FrameworkDescription: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    FrameworkTags: Optional[Mapping[str, str]] = None


class UpdateFrameworkInputTypeDef(BaseValidatorModel):
    FrameworkName: str
    FrameworkDescription: Optional[str] = None
    FrameworkControls: Optional[Sequence[FrameworkControlUnionTypeDef]] = None
    IdempotencyToken: Optional[str] = None


class RecoveryPointSelectionUnionTypeDef(BaseValidatorModel):
    pass


class CreateLegalHoldInputTypeDef(BaseValidatorModel):
    Title: str
    Description: str
    IdempotencyToken: Optional[str] = None
    RecoveryPointSelection: Optional[RecoveryPointSelectionUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateBackupPlanInputTypeDef(BaseValidatorModel):
    BackupPlan: BackupPlanInputTypeDef
    BackupPlanTags: Optional[Mapping[str, str]] = None
    CreatorRequestId: Optional[str] = None


class UpdateBackupPlanInputTypeDef(BaseValidatorModel):
    BackupPlanId: str
    BackupPlan: BackupPlanInputTypeDef


class CreateRestoreTestingSelectionInputTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForCreateTypeDef
    CreatorRequestId: Optional[str] = None


class UpdateRestoreTestingSelectionInputTypeDef(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForUpdateTypeDef
    RestoreTestingSelectionName: str


