from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.backup.backup_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AdvancedBackupSettingOutput(BaseValidatorModel):
    ResourceType: Optional[str] = None
    BackupOptions: Optional[Dict[str, str]] = None


class AdvancedBackupSetting(BaseValidatorModel):
    ResourceType: Optional[str] = None
    BackupOptions: Optional[Dict[str, str]] = None


class BackupJobSummary(BaseValidatorModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[BackupJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class RecoveryPointCreator(BaseValidatorModel):
    BackupPlanId: Optional[str] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None


class BackupPlanTemplatesListMember(BaseValidatorModel):
    BackupPlanTemplateId: Optional[str] = None
    BackupPlanTemplateName: Optional[str] = None


class Lifecycle(BaseValidatorModel):
    MoveToColdStorageAfterDays: Optional[int] = None
    DeleteAfterDays: Optional[int] = None
    OptInToArchiveForSupportedResources: Optional[bool] = None


class IndexActionOutput(BaseValidatorModel):
    ResourceTypes: Optional[List[str]] = None


class Condition(BaseValidatorModel):
    ConditionType: Literal['STRINGEQUALS']
    ConditionKey: str
    ConditionValue: str


class BackupSelectionsListMember(BaseValidatorModel):
    SelectionId: Optional[str] = None
    SelectionName: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CreatorRequestId: Optional[str] = None
    IamRoleArn: Optional[str] = None


class BackupVaultListMember(BaseValidatorModel):
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


class CalculatedLifecycle(BaseValidatorModel):
    MoveToColdStorageAt: Optional[datetime] = None
    DeleteAt: Optional[datetime] = None


class CancelLegalHoldInput(BaseValidatorModel):
    LegalHoldId: str
    CancelDescription: str
    RetainRecordInDays: Optional[int] = None


class ConditionParameter(BaseValidatorModel):
    ConditionKey: Optional[str] = None
    ConditionValue: Optional[str] = None


class ControlInputParameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class ControlScopeOutput(BaseValidatorModel):
    ComplianceResourceIds: Optional[List[str]] = None
    ComplianceResourceTypes: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


class ControlScope(BaseValidatorModel):
    ComplianceResourceIds: Optional[List[str]] = None
    ComplianceResourceTypes: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


class CopyJobSummary(BaseValidatorModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateBackupVaultInput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultTags: Optional[Dict[str, str]] = None
    EncryptionKeyArn: Optional[str] = None
    CreatorRequestId: Optional[str] = None


class CreateLogicallyAirGappedBackupVaultInput(BaseValidatorModel):
    BackupVaultName: str
    MinRetentionDays: int
    MaxRetentionDays: int
    BackupVaultTags: Optional[Dict[str, str]] = None
    CreatorRequestId: Optional[str] = None


class DateRangeOutput(BaseValidatorModel):
    FromDate: datetime
    ToDate: datetime

Timestamp = Union[datetime, str]


class DeleteBackupPlanInput(BaseValidatorModel):
    BackupPlanId: str


class DeleteBackupSelectionInput(BaseValidatorModel):
    BackupPlanId: str
    SelectionId: str


class DeleteBackupVaultAccessPolicyInput(BaseValidatorModel):
    BackupVaultName: str


class DeleteBackupVaultInput(BaseValidatorModel):
    BackupVaultName: str


class DeleteBackupVaultLockConfigurationInput(BaseValidatorModel):
    BackupVaultName: str


class DeleteBackupVaultNotificationsInput(BaseValidatorModel):
    BackupVaultName: str


class DeleteFrameworkInput(BaseValidatorModel):
    FrameworkName: str


class DeleteRecoveryPointInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class DeleteReportPlanInput(BaseValidatorModel):
    ReportPlanName: str


class DeleteRestoreTestingPlanInput(BaseValidatorModel):
    RestoreTestingPlanName: str


class DeleteRestoreTestingSelectionInput(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str


class DescribeBackupJobInput(BaseValidatorModel):
    BackupJobId: str


class DescribeBackupVaultInput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None


class DescribeCopyJobInput(BaseValidatorModel):
    CopyJobId: str


class DescribeFrameworkInput(BaseValidatorModel):
    FrameworkName: str


class DescribeProtectedResourceInput(BaseValidatorModel):
    ResourceArn: str


class DescribeRecoveryPointInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None


class DescribeReportJobInput(BaseValidatorModel):
    ReportJobId: str


class DescribeReportPlanInput(BaseValidatorModel):
    ReportPlanName: str


class DescribeRestoreJobInput(BaseValidatorModel):
    RestoreJobId: str


class RestoreJobCreator(BaseValidatorModel):
    RestoreTestingPlanArn: Optional[str] = None


class DisassociateRecoveryPointFromParentInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class DisassociateRecoveryPointInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class ExportBackupPlanTemplateInput(BaseValidatorModel):
    BackupPlanId: str


class Framework(BaseValidatorModel):
    FrameworkName: Optional[str] = None
    FrameworkArn: Optional[str] = None
    FrameworkDescription: Optional[str] = None
    NumberOfControls: Optional[int] = None
    CreationTime: Optional[datetime] = None
    DeploymentStatus: Optional[str] = None


class GetBackupPlanFromJSONInput(BaseValidatorModel):
    BackupPlanTemplateJson: str


class GetBackupPlanFromTemplateInput(BaseValidatorModel):
    BackupPlanTemplateId: str


class GetBackupPlanInput(BaseValidatorModel):
    BackupPlanId: str
    VersionId: Optional[str] = None


class GetBackupSelectionInput(BaseValidatorModel):
    BackupPlanId: str
    SelectionId: str


class GetBackupVaultAccessPolicyInput(BaseValidatorModel):
    BackupVaultName: str


class GetBackupVaultNotificationsInput(BaseValidatorModel):
    BackupVaultName: str


class GetLegalHoldInput(BaseValidatorModel):
    LegalHoldId: str


class GetRecoveryPointIndexDetailsInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str


class GetRecoveryPointRestoreMetadataInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None


class GetRestoreJobMetadataInput(BaseValidatorModel):
    RestoreJobId: str


class GetRestoreTestingInferredMetadataInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    BackupVaultAccountId: Optional[str] = None


class GetRestoreTestingPlanInput(BaseValidatorModel):
    RestoreTestingPlanName: str


class GetRestoreTestingSelectionInput(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str


class IndexAction(BaseValidatorModel):
    ResourceTypes: Optional[List[str]] = None


class IndexedRecoveryPoint(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    SourceResourceArn: Optional[str] = None
    IamRoleArn: Optional[str] = None
    BackupCreationDate: Optional[datetime] = None
    ResourceType: Optional[str] = None
    IndexCreationDate: Optional[datetime] = None
    IndexStatus: Optional[IndexStatusType] = None
    IndexStatusMessage: Optional[str] = None
    BackupVaultArn: Optional[str] = None


class KeyValue(BaseValidatorModel):
    Key: str
    Value: str


class LegalHold(BaseValidatorModel):
    Title: Optional[str] = None
    Status: Optional[LegalHoldStatusType] = None
    Description: Optional[str] = None
    LegalHoldId: Optional[str] = None
    LegalHoldArn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CancellationDate: Optional[datetime] = None


class ListBackupJobSummariesInput(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[BackupJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBackupPlanTemplatesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBackupPlanVersionsInput(BaseValidatorModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBackupPlansInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeDeleted: Optional[bool] = None


class ListBackupSelectionsInput(BaseValidatorModel):
    BackupPlanId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBackupVaultsInput(BaseValidatorModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCopyJobSummariesInput(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[CopyJobStatusType] = None
    ResourceType: Optional[str] = None
    MessageCategory: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFrameworksInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListLegalHoldsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProtectedResourcesByBackupVaultInput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProtectedResource(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    LastBackupTime: Optional[datetime] = None
    ResourceName: Optional[str] = None
    LastBackupVaultArn: Optional[str] = None
    LastRecoveryPointArn: Optional[str] = None


class ListProtectedResourcesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRecoveryPointsByLegalHoldInput(BaseValidatorModel):
    LegalHoldId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RecoveryPointMember(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    BackupVaultName: Optional[str] = None


class ListRecoveryPointsByResourceInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ManagedByAWSBackupOnly: Optional[bool] = None


class RecoveryPointByResource(BaseValidatorModel):
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


class ListReportPlansInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRestoreJobSummariesInput(BaseValidatorModel):
    AccountId: Optional[str] = None
    State: Optional[RestoreJobStateType] = None
    ResourceType: Optional[str] = None
    AggregationPeriod: Optional[AggregationPeriodType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RestoreJobSummary(BaseValidatorModel):
    Region: Optional[str] = None
    AccountId: Optional[str] = None
    State: Optional[RestoreJobStateType] = None
    ResourceType: Optional[str] = None
    Count: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ListRestoreTestingPlansInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RestoreTestingPlanForList(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    LastExecutionTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None


class ListRestoreTestingSelectionsInput(BaseValidatorModel):
    RestoreTestingPlanName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RestoreTestingSelectionForList(BaseValidatorModel):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ValidationWindowHours: Optional[int] = None


class ListTagsInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PutBackupVaultAccessPolicyInput(BaseValidatorModel):
    BackupVaultName: str
    Policy: Optional[str] = None


class PutBackupVaultLockConfigurationInput(BaseValidatorModel):
    BackupVaultName: str
    MinRetentionDays: Optional[int] = None
    MaxRetentionDays: Optional[int] = None
    ChangeableForDays: Optional[int] = None


class PutBackupVaultNotificationsInput(BaseValidatorModel):
    BackupVaultName: str
    SNSTopicArn: str
    BackupVaultEvents: List[BackupVaultEventType]


class PutRestoreValidationResultInput(BaseValidatorModel):
    RestoreJobId: str
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: Optional[str] = None


class ReportDeliveryChannelOutput(BaseValidatorModel):
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    Formats: Optional[List[str]] = None


class ReportDeliveryChannel(BaseValidatorModel):
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    Formats: Optional[List[str]] = None


class ReportDestination(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Keys: Optional[List[str]] = None


class ReportSettingOutput(BaseValidatorModel):
    ReportTemplate: str
    FrameworkArns: Optional[List[str]] = None
    NumberOfFrameworks: Optional[int] = None
    Accounts: Optional[List[str]] = None
    OrganizationUnits: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class ReportSetting(BaseValidatorModel):
    ReportTemplate: str
    FrameworkArns: Optional[List[str]] = None
    NumberOfFrameworks: Optional[int] = None
    Accounts: Optional[List[str]] = None
    OrganizationUnits: Optional[List[str]] = None
    Regions: Optional[List[str]] = None


class RestoreTestingRecoveryPointSelectionOutput(BaseValidatorModel):
    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithmType] = None
    ExcludeVaults: Optional[List[str]] = None
    IncludeVaults: Optional[List[str]] = None
    RecoveryPointTypes: Optional[List[RestoreTestingRecoveryPointTypeType]] = None
    SelectionWindowDays: Optional[int] = None


class RestoreTestingRecoveryPointSelection(BaseValidatorModel):
    Algorithm: Optional[RestoreTestingRecoveryPointSelectionAlgorithmType] = None
    ExcludeVaults: Optional[List[str]] = None
    IncludeVaults: Optional[List[str]] = None
    RecoveryPointTypes: Optional[List[RestoreTestingRecoveryPointTypeType]] = None
    SelectionWindowDays: Optional[int] = None


class StartReportJobInput(BaseValidatorModel):
    ReportPlanName: str
    IdempotencyToken: Optional[str] = None


class StartRestoreJobInput(BaseValidatorModel):
    RecoveryPointArn: str
    Metadata: Dict[str, str]
    IamRoleArn: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    ResourceType: Optional[str] = None
    CopySourceTagsToRestoredResource: Optional[bool] = None


class StopBackupJobInput(BaseValidatorModel):
    BackupJobId: str


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeyList: List[str]


class UpdateGlobalSettingsInput(BaseValidatorModel):
    GlobalSettings: Optional[Dict[str, str]] = None


class UpdateRecoveryPointIndexSettingsInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    Index: IndexType
    IamRoleArn: Optional[str] = None


class UpdateRegionSettingsInput(BaseValidatorModel):
    ResourceTypeOptInPreference: Optional[Dict[str, bool]] = None
    ResourceTypeManagementPreference: Optional[Dict[str, bool]] = None


class BackupPlansListMember(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    DeletionDate: Optional[datetime] = None
    VersionId: Optional[str] = None
    BackupPlanName: Optional[str] = None
    CreatorRequestId: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingOutput]] = None

AdvancedBackupSettingUnion = Union[AdvancedBackupSetting, AdvancedBackupSettingOutput]


class BackupJob(BaseValidatorModel):
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
    CreatedBy: Optional[RecoveryPointCreator] = None
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


class CopyJob(BaseValidatorModel):
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
    CreatedBy: Optional[RecoveryPointCreator] = None
    ResourceType: Optional[str] = None
    ParentJobId: Optional[str] = None
    IsParent: Optional[bool] = None
    CompositeMemberIdentifier: Optional[str] = None
    NumberOfChildJobs: Optional[int] = None
    ChildJobsInState: Optional[Dict[CopyJobStateType, int]] = None
    ResourceName: Optional[str] = None
    MessageCategory: Optional[str] = None


class CopyAction(BaseValidatorModel):
    DestinationBackupVaultArn: str
    Lifecycle: Optional[Lifecycle] = None


class StartBackupJobInput(BaseValidatorModel):
    BackupVaultName: str
    ResourceArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompleteWindowMinutes: Optional[int] = None
    Lifecycle: Optional[Lifecycle] = None
    RecoveryPointTags: Optional[Dict[str, str]] = None
    BackupOptions: Optional[Dict[str, str]] = None
    Index: Optional[IndexType] = None


class StartCopyJobInput(BaseValidatorModel):
    RecoveryPointArn: str
    SourceBackupVaultName: str
    DestinationBackupVaultArn: str
    IamRoleArn: str
    IdempotencyToken: Optional[str] = None
    Lifecycle: Optional[Lifecycle] = None


class UpdateRecoveryPointLifecycleInput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    Lifecycle: Optional[Lifecycle] = None


class RecoveryPointByBackupVault(BaseValidatorModel):
    RecoveryPointArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    BackupVaultArn: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    CreatedBy: Optional[RecoveryPointCreator] = None
    IamRoleArn: Optional[str] = None
    Status: Optional[RecoveryPointStatusType] = None
    StatusMessage: Optional[str] = None
    CreationDate: Optional[datetime] = None
    CompletionDate: Optional[datetime] = None
    BackupSizeInBytes: Optional[int] = None
    CalculatedLifecycle: Optional[CalculatedLifecycle] = None
    Lifecycle: Optional[Lifecycle] = None
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


class ConditionsOutput(BaseValidatorModel):
    StringEquals: Optional[List[ConditionParameter]] = None
    StringNotEquals: Optional[List[ConditionParameter]] = None
    StringLike: Optional[List[ConditionParameter]] = None
    StringNotLike: Optional[List[ConditionParameter]] = None


class Conditions(BaseValidatorModel):
    StringEquals: Optional[List[ConditionParameter]] = None
    StringNotEquals: Optional[List[ConditionParameter]] = None
    StringLike: Optional[List[ConditionParameter]] = None
    StringNotLike: Optional[List[ConditionParameter]] = None


class FrameworkControlOutput(BaseValidatorModel):
    ControlName: str
    ControlInputParameters: Optional[List[ControlInputParameter]] = None
    ControlScope: Optional[ControlScopeOutput] = None

ControlScopeUnion = Union[ControlScope, ControlScopeOutput]


class CreateBackupPlanOutput(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingOutput]
    ResponseMetadata: ResponseMetadata


class CreateBackupSelectionOutput(BaseValidatorModel):
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadata


class CreateBackupVaultOutput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    ResponseMetadata: ResponseMetadata


class CreateFrameworkOutput(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    ResponseMetadata: ResponseMetadata


class CreateLogicallyAirGappedBackupVaultOutput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    CreationDate: datetime
    VaultState: VaultStateType
    ResponseMetadata: ResponseMetadata


class CreateReportPlanOutput(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateRestoreTestingPlanOutput(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ResponseMetadata: ResponseMetadata


class CreateRestoreTestingSelectionOutput(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    ResponseMetadata: ResponseMetadata


class DeleteBackupPlanOutput(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    DeletionDate: datetime
    VersionId: str
    ResponseMetadata: ResponseMetadata


class DescribeBackupJobOutput(BaseValidatorModel):
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
    CreatedBy: RecoveryPointCreator
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
    ResponseMetadata: ResponseMetadata


class DescribeBackupVaultOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class DescribeGlobalSettingsOutput(BaseValidatorModel):
    GlobalSettings: Dict[str, str]
    LastUpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribeProtectedResourceOutput(BaseValidatorModel):
    ResourceArn: str
    ResourceType: str
    LastBackupTime: datetime
    ResourceName: str
    LastBackupVaultArn: str
    LastRecoveryPointArn: str
    LatestRestoreExecutionTimeMinutes: int
    LatestRestoreJobCreationDate: datetime
    LatestRestoreRecoveryPointCreationDate: datetime
    ResponseMetadata: ResponseMetadata


class DescribeRecoveryPointOutput(BaseValidatorModel):
    RecoveryPointArn: str
    BackupVaultName: str
    BackupVaultArn: str
    SourceBackupVaultArn: str
    ResourceArn: str
    ResourceType: str
    CreatedBy: RecoveryPointCreator
    IamRoleArn: str
    Status: RecoveryPointStatusType
    StatusMessage: str
    CreationDate: datetime
    CompletionDate: datetime
    BackupSizeInBytes: int
    CalculatedLifecycle: CalculatedLifecycle
    Lifecycle: Lifecycle
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
    ResponseMetadata: ResponseMetadata


class DescribeRegionSettingsOutput(BaseValidatorModel):
    ResourceTypeOptInPreference: Dict[str, bool]
    ResourceTypeManagementPreference: Dict[str, bool]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExportBackupPlanTemplateOutput(BaseValidatorModel):
    BackupPlanTemplateJson: str
    ResponseMetadata: ResponseMetadata


class GetBackupVaultAccessPolicyOutput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetBackupVaultNotificationsOutput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultArn: str
    SNSTopicArn: str
    BackupVaultEvents: List[BackupVaultEventType]
    ResponseMetadata: ResponseMetadata


class GetRecoveryPointIndexDetailsOutput(BaseValidatorModel):
    RecoveryPointArn: str
    BackupVaultArn: str
    SourceResourceArn: str
    IndexCreationDate: datetime
    IndexDeletionDate: datetime
    IndexCompletionDate: datetime
    IndexStatus: IndexStatusType
    IndexStatusMessage: str
    TotalItemsIndexed: int
    ResponseMetadata: ResponseMetadata


class GetRecoveryPointRestoreMetadataOutput(BaseValidatorModel):
    BackupVaultArn: str
    RecoveryPointArn: str
    RestoreMetadata: Dict[str, str]
    ResourceType: str
    ResponseMetadata: ResponseMetadata


class GetRestoreJobMetadataOutput(BaseValidatorModel):
    RestoreJobId: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetRestoreTestingInferredMetadataOutput(BaseValidatorModel):
    InferredMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSupportedResourceTypesOutput(BaseValidatorModel):
    ResourceTypes: List[str]
    ResponseMetadata: ResponseMetadata


class ListBackupJobSummariesOutput(BaseValidatorModel):
    BackupJobSummaries: List[BackupJobSummary]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBackupPlanTemplatesOutput(BaseValidatorModel):
    BackupPlanTemplatesList: List[BackupPlanTemplatesListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBackupSelectionsOutput(BaseValidatorModel):
    BackupSelectionsList: List[BackupSelectionsListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBackupVaultsOutput(BaseValidatorModel):
    BackupVaultList: List[BackupVaultListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCopyJobSummariesOutput(BaseValidatorModel):
    CopyJobSummaries: List[CopyJobSummary]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartBackupJobOutput(BaseValidatorModel):
    BackupJobId: str
    RecoveryPointArn: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadata


class StartCopyJobOutput(BaseValidatorModel):
    CopyJobId: str
    CreationDate: datetime
    IsParent: bool
    ResponseMetadata: ResponseMetadata


class StartReportJobOutput(BaseValidatorModel):
    ReportJobId: str
    ResponseMetadata: ResponseMetadata


class StartRestoreJobOutput(BaseValidatorModel):
    RestoreJobId: str
    ResponseMetadata: ResponseMetadata


class UpdateBackupPlanOutput(BaseValidatorModel):
    BackupPlanId: str
    BackupPlanArn: str
    CreationDate: datetime
    VersionId: str
    AdvancedBackupSettings: List[AdvancedBackupSettingOutput]
    ResponseMetadata: ResponseMetadata


class UpdateFrameworkOutput(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateRecoveryPointIndexSettingsOutput(BaseValidatorModel):
    BackupVaultName: str
    RecoveryPointArn: str
    IndexStatus: IndexStatusType
    Index: IndexType
    ResponseMetadata: ResponseMetadata


class UpdateRecoveryPointLifecycleOutput(BaseValidatorModel):
    BackupVaultArn: str
    RecoveryPointArn: str
    Lifecycle: Lifecycle
    CalculatedLifecycle: CalculatedLifecycle
    ResponseMetadata: ResponseMetadata


class UpdateReportPlanOutput(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanArn: str
    CreationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateRestoreTestingPlanOutput(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateRestoreTestingSelectionOutput(BaseValidatorModel):
    CreationTime: datetime
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class RecoveryPointSelectionOutput(BaseValidatorModel):
    VaultNames: Optional[List[str]] = None
    ResourceIdentifiers: Optional[List[str]] = None
    DateRange: Optional[DateRangeOutput] = None


class DateRange(BaseValidatorModel):
    FromDate: Timestamp
    ToDate: Timestamp


class ListBackupJobsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByResourceArn: Optional[str] = None
    ByState: Optional[BackupJobStateType] = None
    ByBackupVaultName: Optional[str] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByResourceType: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteAfter: Optional[Timestamp] = None
    ByCompleteBefore: Optional[Timestamp] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None


class ListCopyJobsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByResourceArn: Optional[str] = None
    ByState: Optional[CopyJobStateType] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByResourceType: Optional[str] = None
    ByDestinationVaultArn: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteBefore: Optional[Timestamp] = None
    ByCompleteAfter: Optional[Timestamp] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None


class ListIndexedRecoveryPointsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SourceResourceArn: Optional[str] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None
    ResourceType: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None


class ListRecoveryPointsByBackupVaultInput(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByResourceArn: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByBackupPlanId: Optional[str] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByParentRecoveryPointArn: Optional[str] = None


class ListReportJobsInput(BaseValidatorModel):
    ByReportPlanName: Optional[str] = None
    ByCreationBefore: Optional[Timestamp] = None
    ByCreationAfter: Optional[Timestamp] = None
    ByStatus: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRestoreJobsByProtectedResourceInput(BaseValidatorModel):
    ResourceArn: str
    ByStatus: Optional[RestoreJobStatusType] = None
    ByRecoveryPointCreationDateAfter: Optional[Timestamp] = None
    ByRecoveryPointCreationDateBefore: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRestoreJobsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ByAccountId: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByStatus: Optional[RestoreJobStatusType] = None
    ByCompleteBefore: Optional[Timestamp] = None
    ByCompleteAfter: Optional[Timestamp] = None
    ByRestoreTestingPlanArn: Optional[str] = None


class DescribeRestoreJobOutput(BaseValidatorModel):
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
    CreatedBy: RestoreJobCreator
    ValidationStatus: RestoreValidationStatusType
    ValidationStatusMessage: str
    DeletionStatus: RestoreDeletionStatusType
    DeletionStatusMessage: str
    ResponseMetadata: ResponseMetadata


class RestoreJobsListMember(BaseValidatorModel):
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
    CreatedBy: Optional[RestoreJobCreator] = None
    ValidationStatus: Optional[RestoreValidationStatusType] = None
    ValidationStatusMessage: Optional[str] = None
    DeletionStatus: Optional[RestoreDeletionStatusType] = None
    DeletionStatusMessage: Optional[str] = None


class ListFrameworksOutput(BaseValidatorModel):
    Frameworks: List[Framework]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

IndexActionUnion = Union[IndexAction, IndexActionOutput]


class ListIndexedRecoveryPointsOutput(BaseValidatorModel):
    IndexedRecoveryPoints: List[IndexedRecoveryPoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ProtectedResourceConditionsOutput(BaseValidatorModel):
    StringEquals: Optional[List[KeyValue]] = None
    StringNotEquals: Optional[List[KeyValue]] = None


class ProtectedResourceConditions(BaseValidatorModel):
    StringEquals: Optional[List[KeyValue]] = None
    StringNotEquals: Optional[List[KeyValue]] = None


class ListLegalHoldsOutput(BaseValidatorModel):
    LegalHolds: List[LegalHold]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBackupJobsInputPaginate(BaseValidatorModel):
    ByResourceArn: Optional[str] = None
    ByState: Optional[BackupJobStateType] = None
    ByBackupVaultName: Optional[str] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByResourceType: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteAfter: Optional[Timestamp] = None
    ByCompleteBefore: Optional[Timestamp] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBackupPlanTemplatesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBackupPlanVersionsInputPaginate(BaseValidatorModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBackupPlansInputPaginate(BaseValidatorModel):
    IncludeDeleted: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBackupSelectionsInputPaginate(BaseValidatorModel):
    BackupPlanId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBackupVaultsInputPaginate(BaseValidatorModel):
    ByVaultType: Optional[VaultTypeType] = None
    ByShared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCopyJobsInputPaginate(BaseValidatorModel):
    ByResourceArn: Optional[str] = None
    ByState: Optional[CopyJobStateType] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByResourceType: Optional[str] = None
    ByDestinationVaultArn: Optional[str] = None
    ByAccountId: Optional[str] = None
    ByCompleteBefore: Optional[Timestamp] = None
    ByCompleteAfter: Optional[Timestamp] = None
    ByParentJobId: Optional[str] = None
    ByMessageCategory: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIndexedRecoveryPointsInputPaginate(BaseValidatorModel):
    SourceResourceArn: Optional[str] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None
    ResourceType: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLegalHoldsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtectedResourcesByBackupVaultInputPaginate(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtectedResourcesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecoveryPointsByBackupVaultInputPaginate(BaseValidatorModel):
    BackupVaultName: str
    BackupVaultAccountId: Optional[str] = None
    ByResourceArn: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByBackupPlanId: Optional[str] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByParentRecoveryPointArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecoveryPointsByLegalHoldInputPaginate(BaseValidatorModel):
    LegalHoldId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecoveryPointsByResourceInputPaginate(BaseValidatorModel):
    ResourceArn: str
    ManagedByAWSBackupOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRestoreJobsByProtectedResourceInputPaginate(BaseValidatorModel):
    ResourceArn: str
    ByStatus: Optional[RestoreJobStatusType] = None
    ByRecoveryPointCreationDateAfter: Optional[Timestamp] = None
    ByRecoveryPointCreationDateBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRestoreJobsInputPaginate(BaseValidatorModel):
    ByAccountId: Optional[str] = None
    ByResourceType: Optional[str] = None
    ByCreatedBefore: Optional[Timestamp] = None
    ByCreatedAfter: Optional[Timestamp] = None
    ByStatus: Optional[RestoreJobStatusType] = None
    ByCompleteBefore: Optional[Timestamp] = None
    ByCompleteAfter: Optional[Timestamp] = None
    ByRestoreTestingPlanArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRestoreTestingPlansInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRestoreTestingSelectionsInputPaginate(BaseValidatorModel):
    RestoreTestingPlanName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtectedResourcesByBackupVaultOutput(BaseValidatorModel):
    Results: List[ProtectedResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProtectedResourcesOutput(BaseValidatorModel):
    Results: List[ProtectedResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRecoveryPointsByLegalHoldOutput(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRecoveryPointsByResourceOutput(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointByResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRestoreJobSummariesOutput(BaseValidatorModel):
    RestoreJobSummaries: List[RestoreJobSummary]
    AggregationPeriod: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRestoreTestingPlansOutput(BaseValidatorModel):
    RestoreTestingPlans: List[RestoreTestingPlanForList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRestoreTestingSelectionsOutput(BaseValidatorModel):
    RestoreTestingSelections: List[RestoreTestingSelectionForList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ReportDeliveryChannelUnion = Union[ReportDeliveryChannel, ReportDeliveryChannelOutput]


class ReportJob(BaseValidatorModel):
    ReportJobId: Optional[str] = None
    ReportPlanArn: Optional[str] = None
    ReportTemplate: Optional[str] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    ReportDestination: Optional[ReportDestination] = None


class ReportPlan(BaseValidatorModel):
    ReportPlanArn: Optional[str] = None
    ReportPlanName: Optional[str] = None
    ReportPlanDescription: Optional[str] = None
    ReportSetting: Optional[ReportSettingOutput] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelOutput] = None
    DeploymentStatus: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAttemptedExecutionTime: Optional[datetime] = None
    LastSuccessfulExecutionTime: Optional[datetime] = None

ReportSettingUnion = Union[ReportSetting, ReportSettingOutput]


class RestoreTestingPlanForGet(BaseValidatorModel):
    CreationTime: datetime
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionOutput
    RestoreTestingPlanArn: str
    RestoreTestingPlanName: str
    ScheduleExpression: str
    CreatorRequestId: Optional[str] = None
    LastExecutionTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None

RestoreTestingRecoveryPointSelectionUnion = Union[RestoreTestingRecoveryPointSelection, RestoreTestingRecoveryPointSelectionOutput]


class ListBackupPlanVersionsOutput(BaseValidatorModel):
    BackupPlanVersionsList: List[BackupPlansListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBackupPlansOutput(BaseValidatorModel):
    BackupPlansList: List[BackupPlansListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBackupJobsOutput(BaseValidatorModel):
    BackupJobs: List[BackupJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeCopyJobOutput(BaseValidatorModel):
    CopyJob: CopyJob
    ResponseMetadata: ResponseMetadata


class ListCopyJobsOutput(BaseValidatorModel):
    CopyJobs: List[CopyJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BackupRule(BaseValidatorModel):
    RuleName: str
    TargetBackupVaultName: str
    ScheduleExpression: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompletionWindowMinutes: Optional[int] = None
    Lifecycle: Optional[Lifecycle] = None
    RecoveryPointTags: Optional[Dict[str, str]] = None
    RuleId: Optional[str] = None
    CopyActions: Optional[List[CopyAction]] = None
    EnableContinuousBackup: Optional[bool] = None
    ScheduleExpressionTimezone: Optional[str] = None
    IndexActions: Optional[List[IndexActionOutput]] = None


class ListRecoveryPointsByBackupVaultOutput(BaseValidatorModel):
    RecoveryPoints: List[RecoveryPointByBackupVault]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BackupSelectionOutput(BaseValidatorModel):
    SelectionName: str
    IamRoleArn: str
    Resources: Optional[List[str]] = None
    ListOfTags: Optional[List[Condition]] = None
    NotResources: Optional[List[str]] = None
    Conditions: Optional[ConditionsOutput] = None


class BackupSelection(BaseValidatorModel):
    SelectionName: str
    IamRoleArn: str
    Resources: Optional[List[str]] = None
    ListOfTags: Optional[List[Condition]] = None
    NotResources: Optional[List[str]] = None
    Conditions: Optional[Conditions] = None


class DescribeFrameworkOutput(BaseValidatorModel):
    FrameworkName: str
    FrameworkArn: str
    FrameworkDescription: str
    FrameworkControls: List[FrameworkControlOutput]
    CreationTime: datetime
    DeploymentStatus: str
    FrameworkStatus: str
    IdempotencyToken: str
    ResponseMetadata: ResponseMetadata


class FrameworkControl(BaseValidatorModel):
    ControlName: str
    ControlInputParameters: Optional[List[ControlInputParameter]] = None
    ControlScope: Optional[ControlScopeUnion] = None


class CreateLegalHoldOutput(BaseValidatorModel):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    RecoveryPointSelection: RecoveryPointSelectionOutput
    ResponseMetadata: ResponseMetadata


class GetLegalHoldOutput(BaseValidatorModel):
    Title: str
    Status: LegalHoldStatusType
    Description: str
    CancelDescription: str
    LegalHoldId: str
    LegalHoldArn: str
    CreationDate: datetime
    CancellationDate: datetime
    RetainRecordUntil: datetime
    RecoveryPointSelection: RecoveryPointSelectionOutput
    ResponseMetadata: ResponseMetadata


class RecoveryPointSelection(BaseValidatorModel):
    VaultNames: Optional[List[str]] = None
    ResourceIdentifiers: Optional[List[str]] = None
    DateRange: Optional[DateRange] = None


class ListRestoreJobsByProtectedResourceOutput(BaseValidatorModel):
    RestoreJobs: List[RestoreJobsListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRestoreJobsOutput(BaseValidatorModel):
    RestoreJobs: List[RestoreJobsListMember]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BackupRuleInput(BaseValidatorModel):
    RuleName: str
    TargetBackupVaultName: str
    ScheduleExpression: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    CompletionWindowMinutes: Optional[int] = None
    Lifecycle: Optional[Lifecycle] = None
    RecoveryPointTags: Optional[Dict[str, str]] = None
    CopyActions: Optional[List[CopyAction]] = None
    EnableContinuousBackup: Optional[bool] = None
    ScheduleExpressionTimezone: Optional[str] = None
    IndexActions: Optional[List[IndexActionUnion]] = None


class RestoreTestingSelectionForGet(BaseValidatorModel):
    CreationTime: datetime
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingPlanName: str
    RestoreTestingSelectionName: str
    CreatorRequestId: Optional[str] = None
    ProtectedResourceArns: Optional[List[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsOutput] = None
    RestoreMetadataOverrides: Optional[Dict[str, str]] = None
    ValidationWindowHours: Optional[int] = None

ProtectedResourceConditionsUnion = Union[ProtectedResourceConditions, ProtectedResourceConditionsOutput]


class DescribeReportJobOutput(BaseValidatorModel):
    ReportJob: ReportJob
    ResponseMetadata: ResponseMetadata


class ListReportJobsOutput(BaseValidatorModel):
    ReportJobs: List[ReportJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeReportPlanOutput(BaseValidatorModel):
    ReportPlan: ReportPlan
    ResponseMetadata: ResponseMetadata


class ListReportPlansOutput(BaseValidatorModel):
    ReportPlans: List[ReportPlan]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateReportPlanInput(BaseValidatorModel):
    ReportPlanName: str
    ReportDeliveryChannel: ReportDeliveryChannelUnion
    ReportSetting: ReportSettingUnion
    ReportPlanDescription: Optional[str] = None
    ReportPlanTags: Optional[Dict[str, str]] = None
    IdempotencyToken: Optional[str] = None


class UpdateReportPlanInput(BaseValidatorModel):
    ReportPlanName: str
    ReportPlanDescription: Optional[str] = None
    ReportDeliveryChannel: Optional[ReportDeliveryChannelUnion] = None
    ReportSetting: Optional[ReportSettingUnion] = None
    IdempotencyToken: Optional[str] = None


class GetRestoreTestingPlanOutput(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForGet
    ResponseMetadata: ResponseMetadata


class RestoreTestingPlanForCreate(BaseValidatorModel):
    RecoveryPointSelection: RestoreTestingRecoveryPointSelectionUnion
    RestoreTestingPlanName: str
    ScheduleExpression: str
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None


class RestoreTestingPlanForUpdate(BaseValidatorModel):
    RecoveryPointSelection: Optional[RestoreTestingRecoveryPointSelectionUnion] = None
    ScheduleExpression: Optional[str] = None
    ScheduleExpressionTimezone: Optional[str] = None
    StartWindowHours: Optional[int] = None


class BackupPlan(BaseValidatorModel):
    BackupPlanName: str
    Rules: List[BackupRule]
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingOutput]] = None


class GetBackupSelectionOutput(BaseValidatorModel):
    BackupSelection: BackupSelectionOutput
    SelectionId: str
    BackupPlanId: str
    CreationDate: datetime
    CreatorRequestId: str
    ResponseMetadata: ResponseMetadata

BackupSelectionUnion = Union[BackupSelection, BackupSelectionOutput]

FrameworkControlUnion = Union[FrameworkControl, FrameworkControlOutput]

RecoveryPointSelectionUnion = Union[RecoveryPointSelection, RecoveryPointSelectionOutput]


class BackupPlanInput(BaseValidatorModel):
    BackupPlanName: str
    Rules: List[BackupRuleInput]
    AdvancedBackupSettings: Optional[List[AdvancedBackupSettingUnion]] = None


class GetRestoreTestingSelectionOutput(BaseValidatorModel):
    RestoreTestingSelection: RestoreTestingSelectionForGet
    ResponseMetadata: ResponseMetadata


class RestoreTestingSelectionForCreate(BaseValidatorModel):
    IamRoleArn: str
    ProtectedResourceType: str
    RestoreTestingSelectionName: str
    ProtectedResourceArns: Optional[List[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsUnion] = None
    RestoreMetadataOverrides: Optional[Dict[str, str]] = None
    ValidationWindowHours: Optional[int] = None


class RestoreTestingSelectionForUpdate(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    ProtectedResourceArns: Optional[List[str]] = None
    ProtectedResourceConditions: Optional[ProtectedResourceConditionsUnion] = None
    RestoreMetadataOverrides: Optional[Dict[str, str]] = None
    ValidationWindowHours: Optional[int] = None


class CreateRestoreTestingPlanInput(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForCreate
    CreatorRequestId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateRestoreTestingPlanInput(BaseValidatorModel):
    RestoreTestingPlan: RestoreTestingPlanForUpdate
    RestoreTestingPlanName: str


class GetBackupPlanFromJSONOutput(BaseValidatorModel):
    BackupPlan: BackupPlan
    ResponseMetadata: ResponseMetadata


class GetBackupPlanFromTemplateOutput(BaseValidatorModel):
    BackupPlanDocument: BackupPlan
    ResponseMetadata: ResponseMetadata


class GetBackupPlanOutput(BaseValidatorModel):
    BackupPlan: BackupPlan
    BackupPlanId: str
    BackupPlanArn: str
    VersionId: str
    CreatorRequestId: str
    CreationDate: datetime
    DeletionDate: datetime
    LastExecutionDate: datetime
    AdvancedBackupSettings: List[AdvancedBackupSettingOutput]
    ResponseMetadata: ResponseMetadata


class CreateBackupSelectionInput(BaseValidatorModel):
    BackupPlanId: str
    BackupSelection: BackupSelectionUnion
    CreatorRequestId: Optional[str] = None


class CreateFrameworkInput(BaseValidatorModel):
    FrameworkName: str
    FrameworkControls: List[FrameworkControlUnion]
    FrameworkDescription: Optional[str] = None
    IdempotencyToken: Optional[str] = None
    FrameworkTags: Optional[Dict[str, str]] = None


class UpdateFrameworkInput(BaseValidatorModel):
    FrameworkName: str
    FrameworkDescription: Optional[str] = None
    FrameworkControls: Optional[List[FrameworkControlUnion]] = None
    IdempotencyToken: Optional[str] = None


class CreateLegalHoldInput(BaseValidatorModel):
    Title: str
    Description: str
    IdempotencyToken: Optional[str] = None
    RecoveryPointSelection: Optional[RecoveryPointSelectionUnion] = None
    Tags: Optional[Dict[str, str]] = None


class CreateBackupPlanInput(BaseValidatorModel):
    BackupPlan: BackupPlanInput
    BackupPlanTags: Optional[Dict[str, str]] = None
    CreatorRequestId: Optional[str] = None


class UpdateBackupPlanInput(BaseValidatorModel):
    BackupPlanId: str
    BackupPlan: BackupPlanInput


class CreateRestoreTestingSelectionInput(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForCreate
    CreatorRequestId: Optional[str] = None


class UpdateRestoreTestingSelectionInput(BaseValidatorModel):
    RestoreTestingPlanName: str
    RestoreTestingSelection: RestoreTestingSelectionForUpdate
    RestoreTestingSelectionName: str