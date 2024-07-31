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
from aws_resource_validator.pydantic_models.ssm_constants import *

class AccountSharingInfoTypeDef(BaseModel):
    AccountId: Optional[str] = None
    SharedDocumentVersion: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AlarmTypeDef(BaseModel):
    Name: str

class AlarmStateInformationTypeDef(BaseModel):
    Name: str
    State: ExternalAlarmStateType

class AssociateOpsItemRelatedItemRequestRequestTypeDef(BaseModel):
    OpsItemId: str
    AssociationType: str
    ResourceType: str
    ResourceUri: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociationOverviewTypeDef(BaseModel):
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    AssociationStatusAggregatedCount: Optional[Dict[str, int]] = None

class AssociationStatusOutputTypeDef(BaseModel):
    Date: datetime
    Name: AssociationStatusNameType
    Message: str
    AdditionalInfo: Optional[str] = None

class TargetOutputTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None

class AssociationExecutionFilterTypeDef(BaseModel):
    Key: AssociationExecutionFilterKeyType
    Value: str
    Type: AssociationFilterOperatorTypeType

class OutputSourceTypeDef(BaseModel):
    OutputSourceId: Optional[str] = None
    OutputSourceType: Optional[str] = None

class AssociationExecutionTargetsFilterTypeDef(BaseModel):
    Key: AssociationExecutionTargetsFilterKeyType
    Value: str

class AssociationFilterTypeDef(BaseModel):
    key: AssociationFilterKeyType
    value: str

class AttachmentContentTypeDef(BaseModel):
    Name: Optional[str] = None
    Size: Optional[int] = None
    Hash: Optional[str] = None
    HashType: Optional[Literal["Sha256"]] = None
    Url: Optional[str] = None

class AttachmentInformationTypeDef(BaseModel):
    Name: Optional[str] = None

class AttachmentsSourceTypeDef(BaseModel):
    Key: Optional[AttachmentsSourceKeyType] = None
    Values: Optional[Sequence[str]] = None
    Name: Optional[str] = None

class AutomationExecutionFilterTypeDef(BaseModel):
    Key: AutomationExecutionFilterKeyType
    Values: Sequence[str]

class ResolvedTargetsTypeDef(BaseModel):
    ParameterValues: Optional[List[str]] = None
    Truncated: Optional[bool] = None

class ProgressCountersTypeDef(BaseModel):
    TotalSteps: Optional[int] = None
    SuccessSteps: Optional[int] = None
    FailedSteps: Optional[int] = None
    CancelledSteps: Optional[int] = None
    TimedOutSteps: Optional[int] = None

class PatchSourceTypeDef(BaseModel):
    Name: str
    Products: Sequence[str]
    Configuration: str

class CancelCommandRequestRequestTypeDef(BaseModel):
    CommandId: str
    InstanceIds: Optional[Sequence[str]] = None

class CancelMaintenanceWindowExecutionRequestRequestTypeDef(BaseModel):
    WindowExecutionId: str

class CloudWatchOutputConfigTypeDef(BaseModel):
    CloudWatchLogGroupName: Optional[str] = None
    CloudWatchOutputEnabled: Optional[bool] = None

class CommandFilterTypeDef(BaseModel):
    key: CommandFilterKeyType
    value: str

class CommandPluginTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[CommandPluginStatusType] = None
    StatusDetails: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseStartDateTime: Optional[datetime] = None
    ResponseFinishDateTime: Optional[datetime] = None
    Output: Optional[str] = None
    StandardOutputUrl: Optional[str] = None
    StandardErrorUrl: Optional[str] = None
    OutputS3Region: Optional[str] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None

class NotificationConfigOutputTypeDef(BaseModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[List[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None

class ComplianceExecutionSummaryExtraOutputTypeDef(BaseModel):
    ExecutionTime: datetime
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None

class ComplianceExecutionSummaryOutputTypeDef(BaseModel):
    ExecutionTime: datetime
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None

class ComplianceItemEntryTypeDef(BaseModel):
    Severity: ComplianceSeverityType
    Status: ComplianceStatusType
    Id: Optional[str] = None
    Title: Optional[str] = None
    Details: Optional[Mapping[str, str]] = None

class ComplianceStringFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    Type: Optional[ComplianceQueryOperatorTypeType] = None

class SeveritySummaryTypeDef(BaseModel):
    CriticalCount: Optional[int] = None
    HighCount: Optional[int] = None
    MediumCount: Optional[int] = None
    LowCount: Optional[int] = None
    InformationalCount: Optional[int] = None
    UnspecifiedCount: Optional[int] = None

class RegistrationMetadataItemTypeDef(BaseModel):
    Key: str
    Value: str

class TargetTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DocumentRequiresTypeDef(BaseModel):
    Name: str
    Version: Optional[str] = None
    RequireType: Optional[str] = None
    VersionName: Optional[str] = None

class OpsItemDataValueTypeDef(BaseModel):
    Value: Optional[str] = None
    Type: Optional[OpsItemDataTypeType] = None

class OpsItemNotificationTypeDef(BaseModel):
    Arn: Optional[str] = None

class RelatedOpsItemTypeDef(BaseModel):
    OpsItemId: str

class MetadataValueTypeDef(BaseModel):
    Value: Optional[str] = None

class DeleteActivationRequestRequestTypeDef(BaseModel):
    ActivationId: str

class DeleteAssociationRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None

class DeleteDocumentRequestRequestTypeDef(BaseModel):
    Name: str
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None
    Force: Optional[bool] = None

class DeleteInventoryRequestRequestTypeDef(BaseModel):
    TypeName: str
    SchemaDeleteOption: Optional[InventorySchemaDeleteOptionType] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DeleteMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str

class DeleteOpsItemRequestRequestTypeDef(BaseModel):
    OpsItemId: str

class DeleteOpsMetadataRequestRequestTypeDef(BaseModel):
    OpsMetadataArn: str

class DeleteParameterRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteParametersRequestRequestTypeDef(BaseModel):
    Names: Sequence[str]

class DeletePatchBaselineRequestRequestTypeDef(BaseModel):
    BaselineId: str

class DeleteResourceDataSyncRequestRequestTypeDef(BaseModel):
    SyncName: str
    SyncType: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    PolicyId: str
    PolicyHash: str

class DeregisterManagedInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef(BaseModel):
    BaselineId: str
    PatchGroup: str

class DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str
    WindowTargetId: str
    Safe: Optional[bool] = None

class DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str
    WindowTaskId: str

class DescribeActivationsFilterTypeDef(BaseModel):
    FilterKey: Optional[DescribeActivationsFilterKeysType] = None
    FilterValues: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAssociationRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None

class StepExecutionFilterTypeDef(BaseModel):
    Key: StepExecutionFilterKeyType
    Values: Sequence[str]

class PatchOrchestratorFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class PatchTypeDef(BaseModel):
    Id: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    ContentUrl: Optional[str] = None
    Vendor: Optional[str] = None
    ProductFamily: Optional[str] = None
    Product: Optional[str] = None
    Classification: Optional[str] = None
    MsrcSeverity: Optional[str] = None
    KbNumber: Optional[str] = None
    MsrcNumber: Optional[str] = None
    Language: Optional[str] = None
    AdvisoryIds: Optional[List[str]] = None
    BugzillaIds: Optional[List[str]] = None
    CVEIds: Optional[List[str]] = None
    Name: Optional[str] = None
    Epoch: Optional[int] = None
    Version: Optional[str] = None
    Release: Optional[str] = None
    Arch: Optional[str] = None
    Severity: Optional[str] = None
    Repository: Optional[str] = None

class DescribeDocumentPermissionRequestRequestTypeDef(BaseModel):
    Name: str
    PermissionType: Literal["Share"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDocumentRequestRequestTypeDef(BaseModel):
    Name: str
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None

class DescribeEffectiveInstanceAssociationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class InstanceAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    InstanceId: Optional[str] = None
    Content: Optional[str] = None
    AssociationVersion: Optional[str] = None

class DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef(BaseModel):
    BaselineId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceAssociationsStatusRequestRequestTypeDef(BaseModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class InstanceInformationFilterTypeDef(BaseModel):
    key: InstanceInformationFilterKeyType
    valueSet: Sequence[str]

class InstanceInformationStringFilterTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]

class InstancePatchStateFilterTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]
    Type: InstancePatchStateOperatorTypeType

class InstancePatchStateTypeDef(BaseModel):
    InstanceId: str
    PatchGroup: str
    BaselineId: str
    OperationStartTime: datetime
    OperationEndTime: datetime
    Operation: PatchOperationTypeType
    SnapshotId: Optional[str] = None
    InstallOverrideList: Optional[str] = None
    OwnerInformation: Optional[str] = None
    InstalledCount: Optional[int] = None
    InstalledOtherCount: Optional[int] = None
    InstalledPendingRebootCount: Optional[int] = None
    InstalledRejectedCount: Optional[int] = None
    MissingCount: Optional[int] = None
    FailedCount: Optional[int] = None
    UnreportedNotApplicableCount: Optional[int] = None
    NotApplicableCount: Optional[int] = None
    LastNoRebootInstallOperationTime: Optional[datetime] = None
    RebootOption: Optional[RebootOptionType] = None
    CriticalNonCompliantCount: Optional[int] = None
    SecurityNonCompliantCount: Optional[int] = None
    OtherNonCompliantCount: Optional[int] = None

class DescribeInstancePatchStatesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PatchComplianceDataTypeDef(BaseModel):
    Title: str
    KBId: str
    Classification: str
    Severity: str
    State: PatchComplianceDataStateType
    InstalledTime: datetime
    CVEIds: Optional[str] = None

class InstancePropertyFilterTypeDef(BaseModel):
    key: InstancePropertyFilterKeyType
    valueSet: Sequence[str]

class InstancePropertyStringFilterTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]
    Operator: Optional[InstancePropertyFilterOperatorType] = None

class DescribeInventoryDeletionsRequestRequestTypeDef(BaseModel):
    DeletionId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MaintenanceWindowFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class MaintenanceWindowExecutionTaskInvocationIdentityTypeDef(BaseModel):
    WindowExecutionId: Optional[str] = None
    TaskExecutionId: Optional[str] = None
    InvocationId: Optional[str] = None
    ExecutionId: Optional[str] = None
    TaskType: Optional[MaintenanceWindowTaskTypeType] = None
    Parameters: Optional[str] = None
    Status: Optional[MaintenanceWindowExecutionStatusType] = None
    StatusDetails: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    OwnerInformation: Optional[str] = None
    WindowTargetId: Optional[str] = None

class MaintenanceWindowExecutionTypeDef(BaseModel):
    WindowId: Optional[str] = None
    WindowExecutionId: Optional[str] = None
    Status: Optional[MaintenanceWindowExecutionStatusType] = None
    StatusDetails: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ScheduledWindowExecutionTypeDef(BaseModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None
    ExecutionTime: Optional[str] = None

class MaintenanceWindowIdentityForTargetTypeDef(BaseModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None

class MaintenanceWindowIdentityTypeDef(BaseModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Enabled: Optional[bool] = None
    Duration: Optional[int] = None
    Cutoff: Optional[int] = None
    Schedule: Optional[str] = None
    ScheduleTimezone: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    EndDate: Optional[str] = None
    StartDate: Optional[str] = None
    NextExecutionTime: Optional[str] = None

class OpsItemFilterTypeDef(BaseModel):
    Key: OpsItemFilterKeyType
    Values: Sequence[str]
    Operator: OpsItemFilterOperatorType

class ParameterStringFilterTypeDef(BaseModel):
    Key: str
    Option: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class ParametersFilterTypeDef(BaseModel):
    Key: ParametersFilterKeyType
    Values: Sequence[str]

class PatchBaselineIdentityTypeDef(BaseModel):
    BaselineId: Optional[str] = None
    BaselineName: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    BaselineDescription: Optional[str] = None
    DefaultBaseline: Optional[bool] = None

class DescribePatchGroupStateRequestRequestTypeDef(BaseModel):
    PatchGroup: str

class DescribePatchPropertiesRequestRequestTypeDef(BaseModel):
    OperatingSystem: OperatingSystemType
    Property: PatchPropertyType
    PatchSet: Optional[PatchSetType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SessionFilterTypeDef(BaseModel):
    key: SessionFilterKeyType
    value: str

class DisassociateOpsItemRelatedItemRequestRequestTypeDef(BaseModel):
    OpsItemId: str
    AssociationId: str

class DocumentDefaultVersionDescriptionTypeDef(BaseModel):
    Name: Optional[str] = None
    DefaultVersion: Optional[str] = None
    DefaultVersionName: Optional[str] = None

class DocumentParameterTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[DocumentParameterTypeType] = None
    Description: Optional[str] = None
    DefaultValue: Optional[str] = None

class ReviewInformationTypeDef(BaseModel):
    ReviewedTime: Optional[datetime] = None
    Status: Optional[ReviewStatusType] = None
    Reviewer: Optional[str] = None

class DocumentFilterTypeDef(BaseModel):
    key: DocumentFilterKeyType
    value: str

class DocumentKeyValuesFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DocumentReviewCommentSourceTypeDef(BaseModel):
    Type: Optional[Literal["Comment"]] = None
    Content: Optional[str] = None

class DocumentVersionInfoTypeDef(BaseModel):
    Name: Optional[str] = None
    DisplayName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    IsDefaultVersion: Optional[bool] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    Status: Optional[DocumentStatusType] = None
    StatusInformation: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None

class PatchStatusTypeDef(BaseModel):
    DeploymentStatus: Optional[PatchDeploymentStatusType] = None
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovalDate: Optional[datetime] = None

class FailureDetailsTypeDef(BaseModel):
    FailureStage: Optional[str] = None
    FailureType: Optional[str] = None
    Details: Optional[Dict[str, List[str]]] = None

class GetAutomationExecutionRequestRequestTypeDef(BaseModel):
    AutomationExecutionId: str

class GetCalendarStateRequestRequestTypeDef(BaseModel):
    CalendarNames: Sequence[str]
    AtTime: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetCommandInvocationRequestRequestTypeDef(BaseModel):
    CommandId: str
    InstanceId: str
    PluginName: Optional[str] = None

class GetConnectionStatusRequestRequestTypeDef(BaseModel):
    Target: str

class GetDefaultPatchBaselineRequestRequestTypeDef(BaseModel):
    OperatingSystem: Optional[OperatingSystemType] = None

class GetDocumentRequestRequestTypeDef(BaseModel):
    Name: str
    VersionName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None

class InventoryFilterTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]
    Type: Optional[InventoryQueryOperatorTypeType] = None

class ResultAttributeTypeDef(BaseModel):
    TypeName: str

class GetInventorySchemaRequestRequestTypeDef(BaseModel):
    TypeName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Aggregator: Optional[bool] = None
    SubType: Optional[bool] = None

class GetMaintenanceWindowExecutionRequestRequestTypeDef(BaseModel):
    WindowExecutionId: str

class GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef(BaseModel):
    WindowExecutionId: str
    TaskId: str
    InvocationId: str

class GetMaintenanceWindowExecutionTaskRequestRequestTypeDef(BaseModel):
    WindowExecutionId: str
    TaskId: str

class MaintenanceWindowTaskParameterValueExpressionOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class GetMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str

class GetMaintenanceWindowTaskRequestRequestTypeDef(BaseModel):
    WindowId: str
    WindowTaskId: str

class LoggingInfoTypeDef(BaseModel):
    S3BucketName: str
    S3Region: str
    S3KeyPrefix: Optional[str] = None

class GetOpsItemRequestRequestTypeDef(BaseModel):
    OpsItemId: str
    OpsItemArn: Optional[str] = None

class GetOpsMetadataRequestRequestTypeDef(BaseModel):
    OpsMetadataArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class OpsFilterTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]
    Type: Optional[OpsFilterOperatorTypeType] = None

class OpsResultAttributeTypeDef(BaseModel):
    TypeName: str

class GetParameterHistoryRequestRequestTypeDef(BaseModel):
    Name: str
    WithDecryption: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetParameterRequestRequestTypeDef(BaseModel):
    Name: str
    WithDecryption: Optional[bool] = None

class ParameterTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[ParameterTypeType] = None
    Value: Optional[str] = None
    Version: Optional[int] = None
    Selector: Optional[str] = None
    SourceResult: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    ARN: Optional[str] = None
    DataType: Optional[str] = None

class GetParametersRequestRequestTypeDef(BaseModel):
    Names: Sequence[str]
    WithDecryption: Optional[bool] = None

class GetPatchBaselineForPatchGroupRequestRequestTypeDef(BaseModel):
    PatchGroup: str
    OperatingSystem: Optional[OperatingSystemType] = None

class GetPatchBaselineRequestRequestTypeDef(BaseModel):
    BaselineId: str

class PatchSourceOutputTypeDef(BaseModel):
    Name: str
    Products: List[str]
    Configuration: str

class GetResourcePoliciesRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetResourcePoliciesResponseEntryTypeDef(BaseModel):
    PolicyId: Optional[str] = None
    PolicyHash: Optional[str] = None
    Policy: Optional[str] = None

class GetServiceSettingRequestRequestTypeDef(BaseModel):
    SettingId: str

class ServiceSettingTypeDef(BaseModel):
    SettingId: Optional[str] = None
    SettingValue: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    ARN: Optional[str] = None
    Status: Optional[str] = None

class InstanceAggregatedAssociationOverviewTypeDef(BaseModel):
    DetailedStatus: Optional[str] = None
    InstanceAssociationStatusAggregatedCount: Optional[Dict[str, int]] = None

class S3OutputLocationTypeDef(BaseModel):
    OutputS3Region: Optional[str] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None

class S3OutputUrlTypeDef(BaseModel):
    OutputUrl: Optional[str] = None

class InventoryDeletionSummaryItemTypeDef(BaseModel):
    Version: Optional[str] = None
    Count: Optional[int] = None
    RemainingCount: Optional[int] = None

class InventoryItemAttributeTypeDef(BaseModel):
    Name: str
    DataType: InventoryAttributeDataTypeType

class InventoryItemTypeDef(BaseModel):
    TypeName: str
    SchemaVersion: str
    CaptureTime: str
    ContentHash: Optional[str] = None
    Content: Optional[Sequence[Mapping[str, str]]] = None
    Context: Optional[Mapping[str, str]] = None

class InventoryResultItemTypeDef(BaseModel):
    TypeName: str
    SchemaVersion: str
    Content: List[Dict[str, str]]
    CaptureTime: Optional[str] = None
    ContentHash: Optional[str] = None

class LabelParameterVersionRequestRequestTypeDef(BaseModel):
    Name: str
    Labels: Sequence[str]
    ParameterVersion: Optional[int] = None

class ListAssociationVersionsRequestRequestTypeDef(BaseModel):
    AssociationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDocumentMetadataHistoryRequestRequestTypeDef(BaseModel):
    Name: str
    Metadata: Literal["DocumentReviews"]
    DocumentVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDocumentVersionsRequestRequestTypeDef(BaseModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class OpsItemEventFilterTypeDef(BaseModel):
    Key: Literal["OpsItemId"]
    Values: Sequence[str]
    Operator: Literal["Equal"]

class OpsItemRelatedItemsFilterTypeDef(BaseModel):
    Key: OpsItemRelatedItemsFilterKeyType
    Values: Sequence[str]
    Operator: Literal["Equal"]

class OpsMetadataFilterTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]

class OpsMetadataTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    OpsMetadataArn: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    CreationDate: Optional[datetime] = None

class ListResourceDataSyncRequestRequestTypeDef(BaseModel):
    SyncType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str

class MaintenanceWindowAutomationParametersOutputTypeDef(BaseModel):
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None

class MaintenanceWindowAutomationParametersTypeDef(BaseModel):
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None

class MaintenanceWindowLambdaParametersOutputTypeDef(BaseModel):
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[bytes] = None

class NotificationConfigTypeDef(BaseModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[Sequence[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None

class MaintenanceWindowStepFunctionsParametersTypeDef(BaseModel):
    Input: Optional[str] = None
    Name: Optional[str] = None

class MaintenanceWindowTaskParameterValueExpressionExtraOutputTypeDef(BaseModel):
    Values: Optional[List[str]] = None

class MaintenanceWindowTaskParameterValueExpressionTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None

class ModifyDocumentPermissionRequestRequestTypeDef(BaseModel):
    Name: str
    PermissionType: Literal["Share"]
    AccountIdsToAdd: Optional[Sequence[str]] = None
    AccountIdsToRemove: Optional[Sequence[str]] = None
    SharedDocumentVersion: Optional[str] = None

class NotificationConfigExtraOutputTypeDef(BaseModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[List[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None

class OpsEntityItemTypeDef(BaseModel):
    CaptureTime: Optional[str] = None
    Content: Optional[List[Dict[str, str]]] = None

class OpsItemIdentityTypeDef(BaseModel):
    Arn: Optional[str] = None

class ParameterInlinePolicyTypeDef(BaseModel):
    PolicyText: Optional[str] = None
    PolicyType: Optional[str] = None
    PolicyStatus: Optional[str] = None

class ParentStepDetailsTypeDef(BaseModel):
    StepExecutionId: Optional[str] = None
    StepName: Optional[str] = None
    Action: Optional[str] = None
    Iteration: Optional[int] = None
    IteratorValue: Optional[str] = None

class PatchFilterOutputTypeDef(BaseModel):
    Key: PatchFilterKeyType
    Values: List[str]

class PatchFilterTypeDef(BaseModel):
    Key: PatchFilterKeyType
    Values: Sequence[str]

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str
    PolicyId: Optional[str] = None
    PolicyHash: Optional[str] = None

class RegisterDefaultPatchBaselineRequestRequestTypeDef(BaseModel):
    BaselineId: str

class RegisterPatchBaselineForPatchGroupRequestRequestTypeDef(BaseModel):
    BaselineId: str
    PatchGroup: str

class RemoveTagsFromResourceRequestRequestTypeDef(BaseModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str
    TagKeys: Sequence[str]

class ResetServiceSettingRequestRequestTypeDef(BaseModel):
    SettingId: str

class ResourceDataSyncOrganizationalUnitTypeDef(BaseModel):
    OrganizationalUnitId: Optional[str] = None

class ResourceDataSyncDestinationDataSharingTypeDef(BaseModel):
    DestinationDataSharingType: Optional[str] = None

class ResumeSessionRequestRequestTypeDef(BaseModel):
    SessionId: str

class TargetExtraOutputTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None

class SendAutomationSignalRequestRequestTypeDef(BaseModel):
    AutomationExecutionId: str
    SignalType: SignalTypeType
    Payload: Optional[Mapping[str, Sequence[str]]] = None

class SessionManagerOutputUrlTypeDef(BaseModel):
    S3OutputUrl: Optional[str] = None
    CloudWatchOutputUrl: Optional[str] = None

class StartAssociationsOnceRequestRequestTypeDef(BaseModel):
    AssociationIds: Sequence[str]

class StartSessionRequestRequestTypeDef(BaseModel):
    Target: str
    DocumentName: Optional[str] = None
    Reason: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None

class StopAutomationExecutionRequestRequestTypeDef(BaseModel):
    AutomationExecutionId: str
    Type: Optional[StopTypeType] = None

class TerminateSessionRequestRequestTypeDef(BaseModel):
    SessionId: str

class UnlabelParameterVersionRequestRequestTypeDef(BaseModel):
    Name: str
    ParameterVersion: int
    Labels: Sequence[str]

class UpdateDocumentDefaultVersionRequestRequestTypeDef(BaseModel):
    Name: str
    DocumentVersion: str

class UpdateMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    Schedule: Optional[str] = None
    ScheduleTimezone: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    Cutoff: Optional[int] = None
    AllowUnassociatedTargets: Optional[bool] = None
    Enabled: Optional[bool] = None
    Replace: Optional[bool] = None

class UpdateManagedInstanceRoleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IamRole: str

class UpdateServiceSettingRequestRequestTypeDef(BaseModel):
    SettingId: str
    SettingValue: str

class ActivationTypeDef(BaseModel):
    ActivationId: Optional[str] = None
    Description: Optional[str] = None
    DefaultInstanceName: Optional[str] = None
    IamRole: Optional[str] = None
    RegistrationLimit: Optional[int] = None
    RegistrationsCount: Optional[int] = None
    ExpirationDate: Optional[datetime] = None
    Expired: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class AddTagsToResourceRequestRequestTypeDef(BaseModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateMaintenanceWindowRequestRequestTypeDef(BaseModel):
    Name: str
    Schedule: str
    Duration: int
    Cutoff: int
    AllowUnassociatedTargets: bool
    Description: Optional[str] = None
    StartDate: Optional[str] = None
    EndDate: Optional[str] = None
    ScheduleTimezone: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutParameterRequestRequestTypeDef(BaseModel):
    Name: str
    Value: str
    Description: Optional[str] = None
    Type: Optional[ParameterTypeType] = None
    KeyId: Optional[str] = None
    Overwrite: Optional[bool] = None
    AllowedPattern: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Tier: Optional[ParameterTierType] = None
    Policies: Optional[str] = None
    DataType: Optional[str] = None

class AlarmConfigurationExtraOutputTypeDef(BaseModel):
    Alarms: List[AlarmTypeDef]
    IgnorePollAlarmFailure: Optional[bool] = None

class AlarmConfigurationOutputTypeDef(BaseModel):
    Alarms: List[AlarmTypeDef]
    IgnorePollAlarmFailure: Optional[bool] = None

class AlarmConfigurationTypeDef(BaseModel):
    Alarms: Sequence[AlarmTypeDef]
    IgnorePollAlarmFailure: Optional[bool] = None

class AssociateOpsItemRelatedItemResponseTypeDef(BaseModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMaintenanceWindowExecutionResultTypeDef(BaseModel):
    WindowExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateActivationResultTypeDef(BaseModel):
    ActivationId: str
    ActivationCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMaintenanceWindowResultTypeDef(BaseModel):
    WindowId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOpsItemResponseTypeDef(BaseModel):
    OpsItemId: str
    OpsItemArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOpsMetadataResultTypeDef(BaseModel):
    OpsMetadataArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePatchBaselineResultTypeDef(BaseModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMaintenanceWindowResultTypeDef(BaseModel):
    WindowId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteParametersResultTypeDef(BaseModel):
    DeletedParameters: List[str]
    InvalidParameters: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePatchBaselineResultTypeDef(BaseModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterPatchBaselineForPatchGroupResultTypeDef(BaseModel):
    BaselineId: str
    PatchGroup: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTargetFromMaintenanceWindowResultTypeDef(BaseModel):
    WindowId: str
    WindowTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTaskFromMaintenanceWindowResultTypeDef(BaseModel):
    WindowId: str
    WindowTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDocumentPermissionResponseTypeDef(BaseModel):
    AccountIds: List[str]
    AccountSharingInfoList: List[AccountSharingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePatchGroupStateResultTypeDef(BaseModel):
    Instances: int
    InstancesWithInstalledPatches: int
    InstancesWithInstalledOtherPatches: int
    InstancesWithInstalledPendingRebootPatches: int
    InstancesWithInstalledRejectedPatches: int
    InstancesWithMissingPatches: int
    InstancesWithFailedPatches: int
    InstancesWithNotApplicablePatches: int
    InstancesWithUnreportedNotApplicablePatches: int
    InstancesWithCriticalNonCompliantPatches: int
    InstancesWithSecurityNonCompliantPatches: int
    InstancesWithOtherNonCompliantPatches: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePatchPropertiesResultTypeDef(BaseModel):
    Properties: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCalendarStateResponseTypeDef(BaseModel):
    State: CalendarStateType
    AtTime: str
    NextTransitionTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionStatusResponseTypeDef(BaseModel):
    Target: str
    Status: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultPatchBaselineResultTypeDef(BaseModel):
    BaselineId: str
    OperatingSystem: OperatingSystemType
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeployablePatchSnapshotForInstanceResultTypeDef(BaseModel):
    InstanceId: str
    SnapshotId: str
    SnapshotDownloadUrl: str
    Product: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMaintenanceWindowExecutionResultTypeDef(BaseModel):
    WindowExecutionId: str
    TaskIds: List[str]
    Status: MaintenanceWindowExecutionStatusType
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetMaintenanceWindowExecutionTaskInvocationResultTypeDef(BaseModel):
    WindowExecutionId: str
    TaskExecutionId: str
    InvocationId: str
    ExecutionId: str
    TaskType: MaintenanceWindowTaskTypeType
    Parameters: str
    Status: MaintenanceWindowExecutionStatusType
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    OwnerInformation: str
    WindowTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMaintenanceWindowResultTypeDef(BaseModel):
    WindowId: str
    Name: str
    Description: str
    StartDate: str
    EndDate: str
    Schedule: str
    ScheduleTimezone: str
    ScheduleOffset: int
    NextExecutionTime: str
    Duration: int
    Cutoff: int
    AllowUnassociatedTargets: bool
    Enabled: bool
    CreatedDate: datetime
    ModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPatchBaselineForPatchGroupResultTypeDef(BaseModel):
    BaselineId: str
    PatchGroup: str
    OperatingSystem: OperatingSystemType
    ResponseMetadata: ResponseMetadataTypeDef

class LabelParameterVersionResultTypeDef(BaseModel):
    InvalidLabels: List[str]
    ParameterVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListInventoryEntriesResultTypeDef(BaseModel):
    TypeName: str
    InstanceId: str
    SchemaVersion: str
    CaptureTime: str
    Entries: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResultTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutInventoryResultTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutParameterResultTypeDef(BaseModel):
    Version: int
    Tier: ParameterTierType
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    PolicyId: str
    PolicyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDefaultPatchBaselineResultTypeDef(BaseModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterPatchBaselineForPatchGroupResultTypeDef(BaseModel):
    BaselineId: str
    PatchGroup: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTargetWithMaintenanceWindowResultTypeDef(BaseModel):
    WindowTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTaskWithMaintenanceWindowResultTypeDef(BaseModel):
    WindowTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeSessionResponseTypeDef(BaseModel):
    SessionId: str
    TokenValue: str
    StreamUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAutomationExecutionResultTypeDef(BaseModel):
    AutomationExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartChangeRequestExecutionResultTypeDef(BaseModel):
    AutomationExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSessionResponseTypeDef(BaseModel):
    SessionId: str
    TokenValue: str
    StreamUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateSessionResponseTypeDef(BaseModel):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UnlabelParameterVersionResultTypeDef(BaseModel):
    RemovedLabels: List[str]
    InvalidLabels: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMaintenanceWindowResultTypeDef(BaseModel):
    WindowId: str
    Name: str
    Description: str
    StartDate: str
    EndDate: str
    Schedule: str
    ScheduleTimezone: str
    ScheduleOffset: int
    Duration: int
    Cutoff: int
    AllowUnassociatedTargets: bool
    Enabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOpsMetadataResultTypeDef(BaseModel):
    OpsMetadataArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociationTypeDef(BaseModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    LastExecutionDate: Optional[datetime] = None
    Overview: Optional[AssociationOverviewTypeDef] = None
    ScheduleExpression: Optional[str] = None
    AssociationName: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None

class MaintenanceWindowTargetTypeDef(BaseModel):
    WindowId: Optional[str] = None
    WindowTargetId: Optional[str] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateMaintenanceWindowTargetResultTypeDef(BaseModel):
    WindowId: str
    WindowTargetId: str
    Targets: List[TargetOutputTypeDef]
    OwnerInformation: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAssociationExecutionsRequestRequestTypeDef(BaseModel):
    AssociationId: str
    Filters: Optional[Sequence[AssociationExecutionFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class AssociationExecutionTargetTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    ExecutionId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    OutputSource: Optional[OutputSourceTypeDef] = None

class DescribeAssociationExecutionTargetsRequestRequestTypeDef(BaseModel):
    AssociationId: str
    ExecutionId: str
    Filters: Optional[Sequence[AssociationExecutionTargetsFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAssociationsRequestRequestTypeDef(BaseModel):
    AssociationFilterList: Optional[Sequence[AssociationFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class AssociationStatusTypeDef(BaseModel):
    Date: TimestampTypeDef
    Name: AssociationStatusNameType
    Message: str
    AdditionalInfo: Optional[str] = None

class ComplianceExecutionSummaryTypeDef(BaseModel):
    ExecutionTime: TimestampTypeDef
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None

class UpdateDocumentRequestRequestTypeDef(BaseModel):
    Content: str
    Name: str
    Attachments: Optional[Sequence[AttachmentsSourceTypeDef]] = None
    DisplayName: Optional[str] = None
    VersionName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None

class DescribeAutomationExecutionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[AutomationExecutionFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MaintenanceWindowLambdaParametersTypeDef(BaseModel):
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None

class GetCommandInvocationResultTypeDef(BaseModel):
    CommandId: str
    InstanceId: str
    Comment: str
    DocumentName: str
    DocumentVersion: str
    PluginName: str
    ResponseCode: int
    ExecutionStartDateTime: str
    ExecutionElapsedTime: str
    ExecutionEndDateTime: str
    Status: CommandInvocationStatusType
    StatusDetails: str
    StandardOutputContent: str
    StandardOutputUrl: str
    StandardErrorContent: str
    StandardErrorUrl: str
    CloudWatchOutputConfig: CloudWatchOutputConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommandInvocationsRequestRequestTypeDef(BaseModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None
    Details: Optional[bool] = None

class ListCommandsRequestRequestTypeDef(BaseModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None

class CommandInvocationTypeDef(BaseModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceName: Optional[str] = None
    Comment: Optional[str] = None
    DocumentName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    RequestedDateTime: Optional[datetime] = None
    Status: Optional[CommandInvocationStatusType] = None
    StatusDetails: Optional[str] = None
    TraceOutput: Optional[str] = None
    StandardOutputUrl: Optional[str] = None
    StandardErrorUrl: Optional[str] = None
    CommandPlugins: Optional[List[CommandPluginTypeDef]] = None
    ServiceRole: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigOutputTypeDef] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfigTypeDef] = None

class MaintenanceWindowRunCommandParametersOutputTypeDef(BaseModel):
    Comment: Optional[str] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfigTypeDef] = None
    DocumentHash: Optional[str] = None
    DocumentHashType: Optional[DocumentHashTypeType] = None
    DocumentVersion: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigOutputTypeDef] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    ServiceRoleArn: Optional[str] = None
    TimeoutSeconds: Optional[int] = None

class ComplianceItemTypeDef(BaseModel):
    ComplianceType: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Id: Optional[str] = None
    Title: Optional[str] = None
    Status: Optional[ComplianceStatusType] = None
    Severity: Optional[ComplianceSeverityType] = None
    ExecutionSummary: Optional[ComplianceExecutionSummaryOutputTypeDef] = None
    Details: Optional[Dict[str, str]] = None

class ListComplianceItemsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    ResourceIds: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListComplianceSummariesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourceComplianceSummariesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class CompliantSummaryTypeDef(BaseModel):
    CompliantCount: Optional[int] = None
    SeveritySummary: Optional[SeveritySummaryTypeDef] = None

class NonCompliantSummaryTypeDef(BaseModel):
    NonCompliantCount: Optional[int] = None
    SeveritySummary: Optional[SeveritySummaryTypeDef] = None

class CreateActivationRequestRequestTypeDef(BaseModel):
    IamRole: str
    Description: Optional[str] = None
    DefaultInstanceName: Optional[str] = None
    RegistrationLimit: Optional[int] = None
    ExpirationDate: Optional[TimestampTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    RegistrationMetadata: Optional[Sequence[RegistrationMetadataItemTypeDef]] = None

class CreateDocumentRequestRequestTypeDef(BaseModel):
    Content: str
    Name: str
    Requires: Optional[Sequence[DocumentRequiresTypeDef]] = None
    Attachments: Optional[Sequence[AttachmentsSourceTypeDef]] = None
    DisplayName: Optional[str] = None
    VersionName: Optional[str] = None
    DocumentType: Optional[DocumentTypeType] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DocumentIdentifierTypeDef(BaseModel):
    Name: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    DisplayName: Optional[str] = None
    Owner: Optional[str] = None
    VersionName: Optional[str] = None
    PlatformTypes: Optional[List[PlatformTypeType]] = None
    DocumentVersion: Optional[str] = None
    DocumentType: Optional[DocumentTypeType] = None
    SchemaVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    Requires: Optional[List[DocumentRequiresTypeDef]] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Author: Optional[str] = None

class GetDocumentResultTypeDef(BaseModel):
    Name: str
    CreatedDate: datetime
    DisplayName: str
    VersionName: str
    DocumentVersion: str
    Status: DocumentStatusType
    StatusInformation: str
    Content: str
    DocumentType: DocumentTypeType
    DocumentFormat: DocumentFormatType
    Requires: List[DocumentRequiresTypeDef]
    AttachmentsContent: List[AttachmentContentTypeDef]
    ReviewStatus: ReviewStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class OpsItemSummaryTypeDef(BaseModel):
    CreatedBy: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    Priority: Optional[int] = None
    Source: Optional[str] = None
    Status: Optional[OpsItemStatusType] = None
    OpsItemId: Optional[str] = None
    Title: Optional[str] = None
    OperationalData: Optional[Dict[str, OpsItemDataValueTypeDef]] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    OpsItemType: Optional[str] = None
    ActualStartTime: Optional[datetime] = None
    ActualEndTime: Optional[datetime] = None
    PlannedStartTime: Optional[datetime] = None
    PlannedEndTime: Optional[datetime] = None

class CreateOpsItemRequestRequestTypeDef(BaseModel):
    Description: str
    Source: str
    Title: str
    OpsItemType: Optional[str] = None
    OperationalData: Optional[Mapping[str, OpsItemDataValueTypeDef]] = None
    Notifications: Optional[Sequence[OpsItemNotificationTypeDef]] = None
    Priority: Optional[int] = None
    RelatedOpsItems: Optional[Sequence[RelatedOpsItemTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    ActualStartTime: Optional[TimestampTypeDef] = None
    ActualEndTime: Optional[TimestampTypeDef] = None
    PlannedStartTime: Optional[TimestampTypeDef] = None
    PlannedEndTime: Optional[TimestampTypeDef] = None
    AccountId: Optional[str] = None

class OpsItemTypeDef(BaseModel):
    CreatedBy: Optional[str] = None
    OpsItemType: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Description: Optional[str] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    Notifications: Optional[List[OpsItemNotificationTypeDef]] = None
    Priority: Optional[int] = None
    RelatedOpsItems: Optional[List[RelatedOpsItemTypeDef]] = None
    Status: Optional[OpsItemStatusType] = None
    OpsItemId: Optional[str] = None
    Version: Optional[str] = None
    Title: Optional[str] = None
    Source: Optional[str] = None
    OperationalData: Optional[Dict[str, OpsItemDataValueTypeDef]] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    ActualStartTime: Optional[datetime] = None
    ActualEndTime: Optional[datetime] = None
    PlannedStartTime: Optional[datetime] = None
    PlannedEndTime: Optional[datetime] = None
    OpsItemArn: Optional[str] = None

class UpdateOpsItemRequestRequestTypeDef(BaseModel):
    OpsItemId: str
    Description: Optional[str] = None
    OperationalData: Optional[Mapping[str, OpsItemDataValueTypeDef]] = None
    OperationalDataToDelete: Optional[Sequence[str]] = None
    Notifications: Optional[Sequence[OpsItemNotificationTypeDef]] = None
    Priority: Optional[int] = None
    RelatedOpsItems: Optional[Sequence[RelatedOpsItemTypeDef]] = None
    Status: Optional[OpsItemStatusType] = None
    Title: Optional[str] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    ActualStartTime: Optional[TimestampTypeDef] = None
    ActualEndTime: Optional[TimestampTypeDef] = None
    PlannedStartTime: Optional[TimestampTypeDef] = None
    PlannedEndTime: Optional[TimestampTypeDef] = None
    OpsItemArn: Optional[str] = None

class CreateOpsMetadataRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Metadata: Optional[Mapping[str, MetadataValueTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetOpsMetadataResultTypeDef(BaseModel):
    ResourceId: str
    Metadata: Dict[str, MetadataValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateOpsMetadataRequestRequestTypeDef(BaseModel):
    OpsMetadataArn: str
    MetadataToUpdate: Optional[Mapping[str, MetadataValueTypeDef]] = None
    KeysToDelete: Optional[Sequence[str]] = None

class DescribeActivationsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[DescribeActivationsFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeActivationsRequestDescribeActivationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[DescribeActivationsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAssociationExecutionTargetsRequestDescribeAssociationExecutionTargetsPaginateTypeDef(BaseModel):
    AssociationId: str
    ExecutionId: str
    Filters: Optional[Sequence[AssociationExecutionTargetsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAssociationExecutionsRequestDescribeAssociationExecutionsPaginateTypeDef(BaseModel):
    AssociationId: str
    Filters: Optional[Sequence[AssociationExecutionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAutomationExecutionsRequestDescribeAutomationExecutionsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[AutomationExecutionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEffectiveInstanceAssociationsRequestDescribeEffectiveInstanceAssociationsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEffectivePatchesForPatchBaselineRequestDescribeEffectivePatchesForPatchBaselinePaginateTypeDef(BaseModel):
    BaselineId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceAssociationsStatusRequestDescribeInstanceAssociationsStatusPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancePatchStatesRequestDescribeInstancePatchStatesPaginateTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInventoryDeletionsRequestDescribeInventoryDeletionsPaginateTypeDef(BaseModel):
    DeletionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePatchPropertiesRequestDescribePatchPropertiesPaginateTypeDef(BaseModel):
    OperatingSystem: OperatingSystemType
    Property: PatchPropertyType
    PatchSet: Optional[PatchSetType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInventorySchemaRequestGetInventorySchemaPaginateTypeDef(BaseModel):
    TypeName: Optional[str] = None
    Aggregator: Optional[bool] = None
    SubType: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetParameterHistoryRequestGetParameterHistoryPaginateTypeDef(BaseModel):
    Name: str
    WithDecryption: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociationVersionsRequestListAssociationVersionsPaginateTypeDef(BaseModel):
    AssociationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociationsRequestListAssociationsPaginateTypeDef(BaseModel):
    AssociationFilterList: Optional[Sequence[AssociationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCommandInvocationsRequestListCommandInvocationsPaginateTypeDef(BaseModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None
    Details: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCommandsRequestListCommandsPaginateTypeDef(BaseModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComplianceItemsRequestListComplianceItemsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    ResourceIds: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComplianceSummariesRequestListComplianceSummariesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentVersionsRequestListDocumentVersionsPaginateTypeDef(BaseModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceComplianceSummariesRequestListResourceComplianceSummariesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDataSyncRequestListResourceDataSyncPaginateTypeDef(BaseModel):
    SyncType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAutomationStepExecutionsRequestDescribeAutomationStepExecutionsPaginateTypeDef(BaseModel):
    AutomationExecutionId: str
    Filters: Optional[Sequence[StepExecutionFilterTypeDef]] = None
    ReverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAutomationStepExecutionsRequestRequestTypeDef(BaseModel):
    AutomationExecutionId: str
    Filters: Optional[Sequence[StepExecutionFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ReverseOrder: Optional[bool] = None

class DescribeAvailablePatchesRequestDescribeAvailablePatchesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAvailablePatchesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstancePatchesRequestDescribeInstancePatchesPaginateTypeDef(BaseModel):
    InstanceId: str
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancePatchesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribePatchBaselinesRequestDescribePatchBaselinesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePatchBaselinesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePatchGroupsRequestDescribePatchGroupsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePatchGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    NextToken: Optional[str] = None

class DescribeAvailablePatchesResultTypeDef(BaseModel):
    Patches: List[PatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEffectiveInstanceAssociationsResultTypeDef(BaseModel):
    Associations: List[InstanceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceInformationRequestDescribeInstanceInformationPaginateTypeDef(BaseModel):
    InstanceInformationFilterList: Optional[Sequence[InstanceInformationFilterTypeDef]] = None
    Filters: Optional[Sequence[InstanceInformationStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceInformationRequestRequestTypeDef(BaseModel):
    InstanceInformationFilterList: Optional[Sequence[InstanceInformationFilterTypeDef]] = None
    Filters: Optional[Sequence[InstanceInformationStringFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstancePatchStatesForPatchGroupRequestDescribeInstancePatchStatesForPatchGroupPaginateTypeDef(BaseModel):
    PatchGroup: str
    Filters: Optional[Sequence[InstancePatchStateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef(BaseModel):
    PatchGroup: str
    Filters: Optional[Sequence[InstancePatchStateFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeInstancePatchStatesForPatchGroupResultTypeDef(BaseModel):
    InstancePatchStates: List[InstancePatchStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancePatchStatesResultTypeDef(BaseModel):
    InstancePatchStates: List[InstancePatchStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancePatchesResultTypeDef(BaseModel):
    Patches: List[PatchComplianceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancePropertiesRequestDescribeInstancePropertiesPaginateTypeDef(BaseModel):
    InstancePropertyFilterList: Optional[Sequence[InstancePropertyFilterTypeDef]] = None
    FiltersWithOperator: Optional[Sequence[InstancePropertyStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancePropertiesRequestRequestTypeDef(BaseModel):
    InstancePropertyFilterList: Optional[Sequence[InstancePropertyFilterTypeDef]] = None
    FiltersWithOperator: Optional[Sequence[InstancePropertyStringFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowExecutionTaskInvocationsRequestDescribeMaintenanceWindowExecutionTaskInvocationsPaginateTypeDef(BaseModel):
    WindowExecutionId: str
    TaskId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef(BaseModel):
    WindowExecutionId: str
    TaskId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowExecutionTasksRequestDescribeMaintenanceWindowExecutionTasksPaginateTypeDef(BaseModel):
    WindowExecutionId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef(BaseModel):
    WindowExecutionId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowExecutionsRequestDescribeMaintenanceWindowExecutionsPaginateTypeDef(BaseModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowExecutionsRequestRequestTypeDef(BaseModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowTargetsRequestDescribeMaintenanceWindowTargetsPaginateTypeDef(BaseModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowTargetsRequestRequestTypeDef(BaseModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowTasksRequestDescribeMaintenanceWindowTasksPaginateTypeDef(BaseModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowTasksRequestRequestTypeDef(BaseModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowsRequestDescribeMaintenanceWindowsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef(BaseModel):
    WindowExecutionTaskInvocationIdentities: List[       MaintenanceWindowExecutionTaskInvocationIdentityTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowExecutionsResultTypeDef(BaseModel):
    WindowExecutions: List[MaintenanceWindowExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowScheduleResultTypeDef(BaseModel):
    ScheduledWindowExecutions: List[ScheduledWindowExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowsForTargetResultTypeDef(BaseModel):
    WindowIdentities: List[MaintenanceWindowIdentityForTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowsResultTypeDef(BaseModel):
    WindowIdentities: List[MaintenanceWindowIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOpsItemsRequestDescribeOpsItemsPaginateTypeDef(BaseModel):
    OpsItemFilters: Optional[Sequence[OpsItemFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOpsItemsRequestRequestTypeDef(BaseModel):
    OpsItemFilters: Optional[Sequence[OpsItemFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetParametersByPathRequestGetParametersByPathPaginateTypeDef(BaseModel):
    Path: str
    Recursive: Optional[bool] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    WithDecryption: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetParametersByPathRequestRequestTypeDef(BaseModel):
    Path: str
    Recursive: Optional[bool] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    WithDecryption: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeParametersRequestDescribeParametersPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ParametersFilterTypeDef]] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    Shared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParametersRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ParametersFilterTypeDef]] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Shared: Optional[bool] = None

class DescribePatchBaselinesResultTypeDef(BaseModel):
    BaselineIdentities: List[PatchBaselineIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PatchGroupPatchBaselineMappingTypeDef(BaseModel):
    PatchGroup: Optional[str] = None
    BaselineIdentity: Optional[PatchBaselineIdentityTypeDef] = None

class DescribeSessionsRequestDescribeSessionsPaginateTypeDef(BaseModel):
    State: SessionStateType
    Filters: Optional[Sequence[SessionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSessionsRequestRequestTypeDef(BaseModel):
    State: SessionStateType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[SessionFilterTypeDef]] = None

class UpdateDocumentDefaultVersionResultTypeDef(BaseModel):
    Description: DocumentDefaultVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentDescriptionTypeDef(BaseModel):
    Sha1: Optional[str] = None
    Hash: Optional[str] = None
    HashType: Optional[DocumentHashTypeType] = None
    Name: Optional[str] = None
    DisplayName: Optional[str] = None
    VersionName: Optional[str] = None
    Owner: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Status: Optional[DocumentStatusType] = None
    StatusInformation: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[List[DocumentParameterTypeDef]] = None
    PlatformTypes: Optional[List[PlatformTypeType]] = None
    DocumentType: Optional[DocumentTypeType] = None
    SchemaVersion: Optional[str] = None
    LatestVersion: Optional[str] = None
    DefaultVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    AttachmentsInformation: Optional[List[AttachmentInformationTypeDef]] = None
    Requires: Optional[List[DocumentRequiresTypeDef]] = None
    Author: Optional[str] = None
    ReviewInformation: Optional[List[ReviewInformationTypeDef]] = None
    ApprovedVersion: Optional[str] = None
    PendingReviewVersion: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Category: Optional[List[str]] = None
    CategoryEnum: Optional[List[str]] = None

class ListDocumentsRequestListDocumentsPaginateTypeDef(BaseModel):
    DocumentFilterList: Optional[Sequence[DocumentFilterTypeDef]] = None
    Filters: Optional[Sequence[DocumentKeyValuesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentsRequestRequestTypeDef(BaseModel):
    DocumentFilterList: Optional[Sequence[DocumentFilterTypeDef]] = None
    Filters: Optional[Sequence[DocumentKeyValuesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DocumentReviewerResponseSourceTypeDef(BaseModel):
    CreateTime: Optional[datetime] = None
    UpdatedTime: Optional[datetime] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Comment: Optional[List[DocumentReviewCommentSourceTypeDef]] = None
    Reviewer: Optional[str] = None

class DocumentReviewsTypeDef(BaseModel):
    Action: DocumentReviewActionType
    Comment: Optional[Sequence[DocumentReviewCommentSourceTypeDef]] = None

class ListDocumentVersionsResultTypeDef(BaseModel):
    DocumentVersions: List[DocumentVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EffectivePatchTypeDef(BaseModel):
    Patch: Optional[PatchTypeDef] = None
    PatchStatus: Optional[PatchStatusTypeDef] = None

class GetCommandInvocationRequestCommandExecutedWaitTypeDef(BaseModel):
    CommandId: str
    InstanceId: str
    PluginName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class InventoryGroupTypeDef(BaseModel):
    Name: str
    Filters: Sequence[InventoryFilterTypeDef]

class ListInventoryEntriesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    TypeName: str
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetInventoryRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    Aggregators: Optional[Sequence["InventoryAggregatorTypeDef"]] = None
    ResultAttributes: Optional[Sequence[ResultAttributeTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class OpsAggregatorTypeDef(BaseModel):
    AggregatorType: Optional[str] = None
    TypeName: Optional[str] = None
    AttributeName: Optional[str] = None
    Values: Optional[Mapping[str, str]] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence[Dict[str, Any]]] = None

class GetOpsSummaryRequestRequestTypeDef(BaseModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence["OpsAggregatorTypeDef"]] = None
    ResultAttributes: Optional[Sequence[OpsResultAttributeTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetParameterResultTypeDef(BaseModel):
    Parameter: ParameterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersByPathResultTypeDef(BaseModel):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetParametersResultTypeDef(BaseModel):
    Parameters: List[ParameterTypeDef]
    InvalidParameters: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePoliciesResponseTypeDef(BaseModel):
    Policies: List[GetResourcePoliciesResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetServiceSettingResultTypeDef(BaseModel):
    ServiceSetting: ServiceSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetServiceSettingResultTypeDef(BaseModel):
    ServiceSetting: ServiceSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceInformationTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    PingStatus: Optional[PingStatusType] = None
    LastPingDateTime: Optional[datetime] = None
    AgentVersion: Optional[str] = None
    IsLatestVersion: Optional[bool] = None
    PlatformType: Optional[PlatformTypeType] = None
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    ActivationId: Optional[str] = None
    IamRole: Optional[str] = None
    RegistrationDate: Optional[datetime] = None
    ResourceType: Optional[ResourceTypeType] = None
    Name: Optional[str] = None
    IPAddress: Optional[str] = None
    ComputerName: Optional[str] = None
    AssociationStatus: Optional[str] = None
    LastAssociationExecutionDate: Optional[datetime] = None
    LastSuccessfulAssociationExecutionDate: Optional[datetime] = None
    AssociationOverview: Optional[InstanceAggregatedAssociationOverviewTypeDef] = None
    SourceId: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None

class InstancePropertyTypeDef(BaseModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceRole: Optional[str] = None
    KeyName: Optional[str] = None
    InstanceState: Optional[str] = None
    Architecture: Optional[str] = None
    IPAddress: Optional[str] = None
    LaunchTime: Optional[datetime] = None
    PingStatus: Optional[PingStatusType] = None
    LastPingDateTime: Optional[datetime] = None
    AgentVersion: Optional[str] = None
    PlatformType: Optional[PlatformTypeType] = None
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    ActivationId: Optional[str] = None
    IamRole: Optional[str] = None
    RegistrationDate: Optional[datetime] = None
    ResourceType: Optional[str] = None
    ComputerName: Optional[str] = None
    AssociationStatus: Optional[str] = None
    LastAssociationExecutionDate: Optional[datetime] = None
    LastSuccessfulAssociationExecutionDate: Optional[datetime] = None
    AssociationOverview: Optional[InstanceAggregatedAssociationOverviewTypeDef] = None
    SourceId: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None

class InstanceAssociationOutputLocationTypeDef(BaseModel):
    S3Location: Optional[S3OutputLocationTypeDef] = None

class InstanceAssociationOutputUrlTypeDef(BaseModel):
    S3OutputUrl: Optional[S3OutputUrlTypeDef] = None

class InventoryDeletionSummaryTypeDef(BaseModel):
    TotalCount: Optional[int] = None
    RemainingCount: Optional[int] = None
    SummaryItems: Optional[List[InventoryDeletionSummaryItemTypeDef]] = None

class InventoryItemSchemaTypeDef(BaseModel):
    TypeName: str
    Attributes: List[InventoryItemAttributeTypeDef]
    Version: Optional[str] = None
    DisplayName: Optional[str] = None

class PutInventoryRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Items: Sequence[InventoryItemTypeDef]

class InventoryResultEntityTypeDef(BaseModel):
    Id: Optional[str] = None
    Data: Optional[Dict[str, InventoryResultItemTypeDef]] = None

class ListOpsItemEventsRequestListOpsItemEventsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[OpsItemEventFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOpsItemEventsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[OpsItemEventFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOpsItemRelatedItemsRequestListOpsItemRelatedItemsPaginateTypeDef(BaseModel):
    OpsItemId: Optional[str] = None
    Filters: Optional[Sequence[OpsItemRelatedItemsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOpsItemRelatedItemsRequestRequestTypeDef(BaseModel):
    OpsItemId: Optional[str] = None
    Filters: Optional[Sequence[OpsItemRelatedItemsFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOpsMetadataRequestListOpsMetadataPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[OpsMetadataFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOpsMetadataRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[OpsMetadataFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOpsMetadataResultTypeDef(BaseModel):
    OpsMetadataList: List[OpsMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MaintenanceWindowRunCommandParametersTypeDef(BaseModel):
    Comment: Optional[str] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfigTypeDef] = None
    DocumentHash: Optional[str] = None
    DocumentHashType: Optional[DocumentHashTypeType] = None
    DocumentVersion: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigTypeDef] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    ServiceRoleArn: Optional[str] = None
    TimeoutSeconds: Optional[int] = None

class OpsEntityTypeDef(BaseModel):
    Id: Optional[str] = None
    Data: Optional[Dict[str, OpsEntityItemTypeDef]] = None

class OpsItemEventSummaryTypeDef(BaseModel):
    OpsItemId: Optional[str] = None
    EventId: Optional[str] = None
    Source: Optional[str] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None
    CreatedBy: Optional[OpsItemIdentityTypeDef] = None
    CreatedTime: Optional[datetime] = None

class OpsItemRelatedItemSummaryTypeDef(BaseModel):
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ResourceType: Optional[str] = None
    AssociationType: Optional[str] = None
    ResourceUri: Optional[str] = None
    CreatedBy: Optional[OpsItemIdentityTypeDef] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedBy: Optional[OpsItemIdentityTypeDef] = None
    LastModifiedTime: Optional[datetime] = None

class ParameterHistoryTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[ParameterTypeType] = None
    KeyId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    Description: Optional[str] = None
    Value: Optional[str] = None
    AllowedPattern: Optional[str] = None
    Version: Optional[int] = None
    Labels: Optional[List[str]] = None
    Tier: Optional[ParameterTierType] = None
    Policies: Optional[List[ParameterInlinePolicyTypeDef]] = None
    DataType: Optional[str] = None

class ParameterMetadataTypeDef(BaseModel):
    Name: Optional[str] = None
    ARN: Optional[str] = None
    Type: Optional[ParameterTypeType] = None
    KeyId: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    Description: Optional[str] = None
    AllowedPattern: Optional[str] = None
    Version: Optional[int] = None
    Tier: Optional[ParameterTierType] = None
    Policies: Optional[List[ParameterInlinePolicyTypeDef]] = None
    DataType: Optional[str] = None

class PatchFilterGroupOutputTypeDef(BaseModel):
    PatchFilters: List[PatchFilterOutputTypeDef]

class PatchFilterGroupTypeDef(BaseModel):
    PatchFilters: Sequence[PatchFilterTypeDef]

class ResourceDataSyncAwsOrganizationsSourceOutputTypeDef(BaseModel):
    OrganizationSourceType: str
    OrganizationalUnits: Optional[List[ResourceDataSyncOrganizationalUnitTypeDef]] = None

class ResourceDataSyncAwsOrganizationsSourceTypeDef(BaseModel):
    OrganizationSourceType: str
    OrganizationalUnits: Optional[Sequence[ResourceDataSyncOrganizationalUnitTypeDef]] = None

class ResourceDataSyncS3DestinationTypeDef(BaseModel):
    BucketName: str
    SyncFormat: Literal["JsonSerDe"]
    Region: str
    Prefix: Optional[str] = None
    AWSKMSKeyARN: Optional[str] = None
    DestinationDataSharing: Optional[ResourceDataSyncDestinationDataSharingTypeDef] = None

class SessionTypeDef(BaseModel):
    SessionId: Optional[str] = None
    Target: Optional[str] = None
    Status: Optional[SessionStatusType] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    DocumentName: Optional[str] = None
    Owner: Optional[str] = None
    Reason: Optional[str] = None
    Details: Optional[str] = None
    OutputUrl: Optional[SessionManagerOutputUrlTypeDef] = None
    MaxSessionDuration: Optional[str] = None

class DescribeActivationsResultTypeDef(BaseModel):
    ActivationList: List[ActivationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TargetLocationExtraOutputTypeDef(BaseModel):
    Accounts: Optional[List[str]] = None
    Regions: Optional[List[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationExtraOutputTypeDef] = None

class AssociationExecutionTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    ExecutionId: Optional[str] = None
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastExecutionDate: Optional[datetime] = None
    ResourceCountByStatus: Optional[str] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None

class CommandTypeDef(BaseModel):
    CommandId: Optional[str] = None
    DocumentName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Comment: Optional[str] = None
    ExpiresAfter: Optional[datetime] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    InstanceIds: Optional[List[str]] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    RequestedDateTime: Optional[datetime] = None
    Status: Optional[CommandStatusType] = None
    StatusDetails: Optional[str] = None
    OutputS3Region: Optional[str] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetCount: Optional[int] = None
    CompletedCount: Optional[int] = None
    ErrorCount: Optional[int] = None
    DeliveryTimedOutCount: Optional[int] = None
    ServiceRole: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigOutputTypeDef] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfigTypeDef] = None
    TimeoutSeconds: Optional[int] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None

class GetMaintenanceWindowExecutionTaskResultTypeDef(BaseModel):
    WindowExecutionId: str
    TaskExecutionId: str
    TaskArn: str
    ServiceRole: str
    Type: MaintenanceWindowTaskTypeType
    TaskParameters: List[       Dict[str, MaintenanceWindowTaskParameterValueExpressionOutputTypeDef]
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    Status: MaintenanceWindowExecutionStatusType
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    AlarmConfiguration: AlarmConfigurationOutputTypeDef
    TriggeredAlarms: List[AlarmStateInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MaintenanceWindowExecutionTaskIdentityTypeDef(BaseModel):
    WindowExecutionId: Optional[str] = None
    TaskExecutionId: Optional[str] = None
    Status: Optional[MaintenanceWindowExecutionStatusType] = None
    StatusDetails: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TaskArn: Optional[str] = None
    TaskType: Optional[MaintenanceWindowTaskTypeType] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None

class MaintenanceWindowTaskTypeDef(BaseModel):
    WindowId: Optional[str] = None
    WindowTaskId: Optional[str] = None
    TaskArn: Optional[str] = None
    Type: Optional[MaintenanceWindowTaskTypeType] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TaskParameters: Optional[       Dict[str, MaintenanceWindowTaskParameterValueExpressionOutputTypeDef] = None
    Priority: Optional[int] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    ServiceRoleArn: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None

class TargetLocationOutputTypeDef(BaseModel):
    Accounts: Optional[List[str]] = None
    Regions: Optional[List[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None

class TargetLocationTypeDef(BaseModel):
    Accounts: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class ListAssociationsResultTypeDef(BaseModel):
    Associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowTargetsResultTypeDef(BaseModel):
    Targets: List[MaintenanceWindowTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAssociationExecutionTargetsResultTypeDef(BaseModel):
    AssociationExecutionTargets: List[AssociationExecutionTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateAssociationStatusRequestRequestTypeDef(BaseModel):
    Name: str
    InstanceId: str
    AssociationStatus: AssociationStatusTypeDef

class PutComplianceItemsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    ResourceType: str
    ComplianceType: str
    ExecutionSummary: ComplianceExecutionSummaryTypeDef
    Items: Sequence[ComplianceItemEntryTypeDef]
    ItemContentHash: Optional[str] = None
    UploadType: Optional[ComplianceUploadTypeType] = None

class ListCommandInvocationsResultTypeDef(BaseModel):
    CommandInvocations: List[CommandInvocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MaintenanceWindowTaskInvocationParametersOutputTypeDef(BaseModel):
    RunCommand: Optional[MaintenanceWindowRunCommandParametersOutputTypeDef] = None
    Automation: Optional[MaintenanceWindowAutomationParametersOutputTypeDef] = None
    StepFunctions: Optional[MaintenanceWindowStepFunctionsParametersTypeDef] = None
    Lambda: Optional[MaintenanceWindowLambdaParametersOutputTypeDef] = None

class ListComplianceItemsResultTypeDef(BaseModel):
    ComplianceItems: List[ComplianceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ComplianceSummaryItemTypeDef(BaseModel):
    ComplianceType: Optional[str] = None
    CompliantSummary: Optional[CompliantSummaryTypeDef] = None
    NonCompliantSummary: Optional[NonCompliantSummaryTypeDef] = None

class ResourceComplianceSummaryItemTypeDef(BaseModel):
    ComplianceType: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ComplianceStatusType] = None
    OverallSeverity: Optional[ComplianceSeverityType] = None
    ExecutionSummary: Optional[ComplianceExecutionSummaryOutputTypeDef] = None
    CompliantSummary: Optional[CompliantSummaryTypeDef] = None
    NonCompliantSummary: Optional[NonCompliantSummaryTypeDef] = None

class ListDocumentsResultTypeDef(BaseModel):
    DocumentIdentifiers: List[DocumentIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOpsItemsResponseTypeDef(BaseModel):
    OpsItemSummaries: List[OpsItemSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetOpsItemResponseTypeDef(BaseModel):
    OpsItem: OpsItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePatchGroupsResultTypeDef(BaseModel):
    Mappings: List[PatchGroupPatchBaselineMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDocumentResultTypeDef(BaseModel):
    DocumentDescription: DocumentDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDocumentResultTypeDef(BaseModel):
    Document: DocumentDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDocumentResultTypeDef(BaseModel):
    DocumentDescription: DocumentDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentMetadataResponseInfoTypeDef(BaseModel):
    ReviewerResponse: Optional[List[DocumentReviewerResponseSourceTypeDef]] = None

class UpdateDocumentMetadataRequestRequestTypeDef(BaseModel):
    Name: str
    DocumentReviews: DocumentReviewsTypeDef
    DocumentVersion: Optional[str] = None

class DescribeEffectivePatchesForPatchBaselineResultTypeDef(BaseModel):
    EffectivePatches: List[EffectivePatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InventoryAggregatorTypeDef(BaseModel):
    Expression: Optional[str] = None
    Aggregators: Optional[Sequence[Dict[str, Any]]] = None
    Groups: Optional[Sequence[InventoryGroupTypeDef]] = None

class GetOpsSummaryRequestGetOpsSummaryPaginateTypeDef(BaseModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence[OpsAggregatorTypeDef]] = None
    ResultAttributes: Optional[Sequence[OpsResultAttributeTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceInformationResultTypeDef(BaseModel):
    InstanceInformationList: List[InstanceInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancePropertiesResultTypeDef(BaseModel):
    InstanceProperties: List[InstancePropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceAssociationStatusInfoTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    Name: Optional[str] = None
    DocumentVersion: Optional[str] = None
    AssociationVersion: Optional[str] = None
    InstanceId: Optional[str] = None
    ExecutionDate: Optional[datetime] = None
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    ExecutionSummary: Optional[str] = None
    ErrorCode: Optional[str] = None
    OutputUrl: Optional[InstanceAssociationOutputUrlTypeDef] = None
    AssociationName: Optional[str] = None

class DeleteInventoryResultTypeDef(BaseModel):
    DeletionId: str
    TypeName: str
    DeletionSummary: InventoryDeletionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InventoryDeletionStatusItemTypeDef(BaseModel):
    DeletionId: Optional[str] = None
    TypeName: Optional[str] = None
    DeletionStartTime: Optional[datetime] = None
    LastStatus: Optional[InventoryDeletionStatusType] = None
    LastStatusMessage: Optional[str] = None
    DeletionSummary: Optional[InventoryDeletionSummaryTypeDef] = None
    LastStatusUpdateTime: Optional[datetime] = None

class GetInventorySchemaResultTypeDef(BaseModel):
    Schemas: List[InventoryItemSchemaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetInventoryResultTypeDef(BaseModel):
    Entities: List[InventoryResultEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MaintenanceWindowTaskInvocationParametersTypeDef(BaseModel):
    RunCommand: Optional[MaintenanceWindowRunCommandParametersTypeDef] = None
    Automation: Optional[MaintenanceWindowAutomationParametersTypeDef] = None
    StepFunctions: Optional[MaintenanceWindowStepFunctionsParametersTypeDef] = None
    Lambda: Optional[MaintenanceWindowLambdaParametersTypeDef] = None

class GetOpsSummaryResultTypeDef(BaseModel):
    Entities: List[OpsEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOpsItemEventsResponseTypeDef(BaseModel):
    Summaries: List[OpsItemEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOpsItemRelatedItemsResponseTypeDef(BaseModel):
    Summaries: List[OpsItemRelatedItemSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetParameterHistoryResultTypeDef(BaseModel):
    Parameters: List[ParameterHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeParametersResultTypeDef(BaseModel):
    Parameters: List[ParameterMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PatchRuleOutputTypeDef(BaseModel):
    PatchFilterGroup: PatchFilterGroupOutputTypeDef
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApproveAfterDays: Optional[int] = None
    ApproveUntilDate: Optional[str] = None
    EnableNonSecurity: Optional[bool] = None

class PatchRuleTypeDef(BaseModel):
    PatchFilterGroup: PatchFilterGroupTypeDef
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApproveAfterDays: Optional[int] = None
    ApproveUntilDate: Optional[str] = None
    EnableNonSecurity: Optional[bool] = None

class ResourceDataSyncSourceWithStateTypeDef(BaseModel):
    SourceType: Optional[str] = None
    AwsOrganizationsSource: Optional[ResourceDataSyncAwsOrganizationsSourceOutputTypeDef] = None
    SourceRegions: Optional[List[str]] = None
    IncludeFutureRegions: Optional[bool] = None
    State: Optional[str] = None
    EnableAllOpsDataSources: Optional[bool] = None

class ResourceDataSyncSourceTypeDef(BaseModel):
    SourceType: str
    SourceRegions: Sequence[str]
    AwsOrganizationsSource: Optional[ResourceDataSyncAwsOrganizationsSourceTypeDef] = None
    IncludeFutureRegions: Optional[bool] = None
    EnableAllOpsDataSources: Optional[bool] = None

class DescribeMaintenanceWindowScheduleRequestRequestTypeDef(BaseModel):
    WindowId: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowsForTargetRequestDescribeMaintenanceWindowsForTargetPaginateTypeDef(BaseModel):
    Targets: Sequence[TargetUnionTypeDef]
    ResourceType: MaintenanceWindowResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMaintenanceWindowsForTargetRequestRequestTypeDef(BaseModel):
    Targets: Sequence[TargetUnionTypeDef]
    ResourceType: MaintenanceWindowResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RegisterTargetWithMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str
    ResourceType: MaintenanceWindowResourceTypeType
    Targets: Sequence[TargetUnionTypeDef]
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None

class SendCommandRequestRequestTypeDef(BaseModel):
    DocumentName: str
    InstanceIds: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    DocumentVersion: Optional[str] = None
    DocumentHash: Optional[str] = None
    DocumentHashType: Optional[DocumentHashTypeType] = None
    TimeoutSeconds: Optional[int] = None
    Comment: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    OutputS3Region: Optional[str] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    ServiceRoleArn: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigTypeDef] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfigTypeDef] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class UpdateMaintenanceWindowTargetRequestRequestTypeDef(BaseModel):
    WindowId: str
    WindowTargetId: str
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Replace: Optional[bool] = None

class DescribeSessionsResponseTypeDef(BaseModel):
    Sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RunbookExtraOutputTypeDef(BaseModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[List[TargetExtraOutputTypeDef]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[List[TargetLocationExtraOutputTypeDef]] = None

class DescribeAssociationExecutionsResultTypeDef(BaseModel):
    AssociationExecutions: List[AssociationExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCommandsResultTypeDef(BaseModel):
    Commands: List[CommandTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SendCommandResultTypeDef(BaseModel):
    Command: CommandTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMaintenanceWindowExecutionTasksResultTypeDef(BaseModel):
    WindowExecutionTaskIdentities: List[MaintenanceWindowExecutionTaskIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMaintenanceWindowTasksResultTypeDef(BaseModel):
    Tasks: List[MaintenanceWindowTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociationDescriptionTypeDef(BaseModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    Date: Optional[datetime] = None
    LastUpdateAssociationDate: Optional[datetime] = None
    Status: Optional[AssociationStatusOutputTypeDef] = None
    Overview: Optional[AssociationOverviewTypeDef] = None
    DocumentVersion: Optional[str] = None
    AutomationTargetParameterName: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    AssociationId: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    LastExecutionDate: Optional[datetime] = None
    LastSuccessfulExecutionDate: Optional[datetime] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[List[str]] = None
    TargetLocations: Optional[List[TargetLocationOutputTypeDef]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None

class AssociationVersionInfoTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Name: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[List[str]] = None
    TargetLocations: Optional[List[TargetLocationOutputTypeDef]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None

class CreateAssociationBatchRequestEntryOutputTypeDef(BaseModel):
    Name: str
    InstanceId: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    AutomationTargetParameterName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[List[str]] = None
    TargetLocations: Optional[List[TargetLocationOutputTypeDef]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None

class RunbookOutputTypeDef(BaseModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[List[TargetLocationOutputTypeDef]] = None

class StepExecutionTypeDef(BaseModel):
    StepName: Optional[str] = None
    Action: Optional[str] = None
    TimeoutSeconds: Optional[int] = None
    OnFailure: Optional[str] = None
    MaxAttempts: Optional[int] = None
    ExecutionStartTime: Optional[datetime] = None
    ExecutionEndTime: Optional[datetime] = None
    StepStatus: Optional[AutomationExecutionStatusType] = None
    ResponseCode: Optional[str] = None
    Inputs: Optional[Dict[str, str]] = None
    Outputs: Optional[Dict[str, List[str]]] = None
    Response: Optional[str] = None
    FailureMessage: Optional[str] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    StepExecutionId: Optional[str] = None
    OverriddenParameters: Optional[Dict[str, List[str]]] = None
    IsEnd: Optional[bool] = None
    NextStep: Optional[str] = None
    IsCritical: Optional[bool] = None
    ValidNextSteps: Optional[List[str]] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TargetLocation: Optional[TargetLocationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None
    ParentStepDetails: Optional[ParentStepDetailsTypeDef] = None

class CreateAssociationBatchRequestEntryTypeDef(BaseModel):
    Name: str
    InstanceId: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    AutomationTargetParameterName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[Sequence[TargetTypeDef]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[Sequence[str]] = None
    TargetLocations: Optional[Sequence[TargetLocationTypeDef]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class RunbookTypeDef(BaseModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetTypeDef]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[Sequence[TargetLocationTypeDef]] = None

class GetMaintenanceWindowTaskResultTypeDef(BaseModel):
    WindowId: str
    WindowTaskId: str
    Targets: List[TargetOutputTypeDef]
    TaskArn: str
    ServiceRoleArn: str
    TaskType: MaintenanceWindowTaskTypeType
    TaskParameters: Dict[str, MaintenanceWindowTaskParameterValueExpressionOutputTypeDef]
    TaskInvocationParameters: MaintenanceWindowTaskInvocationParametersOutputTypeDef
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    LoggingInfo: LoggingInfoTypeDef
    Name: str
    Description: str
    CutoffBehavior: MaintenanceWindowTaskCutoffBehaviorType
    AlarmConfiguration: AlarmConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMaintenanceWindowTaskResultTypeDef(BaseModel):
    WindowId: str
    WindowTaskId: str
    Targets: List[TargetOutputTypeDef]
    TaskArn: str
    ServiceRoleArn: str
    TaskParameters: Dict[str, MaintenanceWindowTaskParameterValueExpressionOutputTypeDef]
    TaskInvocationParameters: MaintenanceWindowTaskInvocationParametersOutputTypeDef
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    LoggingInfo: LoggingInfoTypeDef
    Name: str
    Description: str
    CutoffBehavior: MaintenanceWindowTaskCutoffBehaviorType
    AlarmConfiguration: AlarmConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListComplianceSummariesResultTypeDef(BaseModel):
    ComplianceSummaryItems: List[ComplianceSummaryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceComplianceSummariesResultTypeDef(BaseModel):
    ResourceComplianceSummaryItems: List[ResourceComplianceSummaryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDocumentMetadataHistoryResponseTypeDef(BaseModel):
    Name: str
    DocumentVersion: str
    Author: str
    Metadata: DocumentMetadataResponseInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetInventoryRequestGetInventoryPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    Aggregators: Optional[Sequence[InventoryAggregatorTypeDef]] = None
    ResultAttributes: Optional[Sequence[ResultAttributeTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceAssociationsStatusResultTypeDef(BaseModel):
    InstanceAssociationStatusInfos: List[InstanceAssociationStatusInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInventoryDeletionsResultTypeDef(BaseModel):
    InventoryDeletions: List[InventoryDeletionStatusItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterTaskWithMaintenanceWindowRequestRequestTypeDef(BaseModel):
    WindowId: str
    TaskArn: str
    TaskType: MaintenanceWindowTaskTypeType
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ServiceRoleArn: Optional[str] = None
    TaskParameters: Optional[       Mapping[str, MaintenanceWindowTaskParameterValueExpressionUnionTypeDef] = None
    TaskInvocationParameters: Optional[MaintenanceWindowTaskInvocationParametersTypeDef] = None
    Priority: Optional[int] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class UpdateMaintenanceWindowTaskRequestRequestTypeDef(BaseModel):
    WindowId: str
    WindowTaskId: str
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    TaskArn: Optional[str] = None
    ServiceRoleArn: Optional[str] = None
    TaskParameters: Optional[       Mapping[str, MaintenanceWindowTaskParameterValueExpressionUnionTypeDef] = None
    TaskInvocationParameters: Optional[MaintenanceWindowTaskInvocationParametersTypeDef] = None
    Priority: Optional[int] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Replace: Optional[bool] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class PatchRuleGroupOutputTypeDef(BaseModel):
    PatchRules: List[PatchRuleOutputTypeDef]

class PatchRuleGroupTypeDef(BaseModel):
    PatchRules: Sequence[PatchRuleTypeDef]

class ResourceDataSyncItemTypeDef(BaseModel):
    SyncName: Optional[str] = None
    SyncType: Optional[str] = None
    SyncSource: Optional[ResourceDataSyncSourceWithStateTypeDef] = None
    S3Destination: Optional[ResourceDataSyncS3DestinationTypeDef] = None
    LastSyncTime: Optional[datetime] = None
    LastSuccessfulSyncTime: Optional[datetime] = None
    SyncLastModifiedTime: Optional[datetime] = None
    LastStatus: Optional[LastResourceDataSyncStatusType] = None
    SyncCreatedTime: Optional[datetime] = None
    LastSyncStatusMessage: Optional[str] = None

class CreateResourceDataSyncRequestRequestTypeDef(BaseModel):
    SyncName: str
    S3Destination: Optional[ResourceDataSyncS3DestinationTypeDef] = None
    SyncType: Optional[str] = None
    SyncSource: Optional[ResourceDataSyncSourceTypeDef] = None

class UpdateResourceDataSyncRequestRequestTypeDef(BaseModel):
    SyncName: str
    SyncType: str
    SyncSource: ResourceDataSyncSourceTypeDef

class CreateAssociationResultTypeDef(BaseModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAssociationResultTypeDef(BaseModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssociationResultTypeDef(BaseModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAssociationStatusResultTypeDef(BaseModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociationVersionsResultTypeDef(BaseModel):
    AssociationVersions: List[AssociationVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailedCreateAssociationTypeDef(BaseModel):
    Entry: Optional[CreateAssociationBatchRequestEntryOutputTypeDef] = None
    Message: Optional[str] = None
    Fault: Optional[FaultType] = None

class AutomationExecutionMetadataTypeDef(BaseModel):
    AutomationExecutionId: Optional[str] = None
    DocumentName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    AutomationExecutionStatus: Optional[AutomationExecutionStatusType] = None
    ExecutionStartTime: Optional[datetime] = None
    ExecutionEndTime: Optional[datetime] = None
    ExecutedBy: Optional[str] = None
    LogFile: Optional[str] = None
    Outputs: Optional[Dict[str, List[str]]] = None
    Mode: Optional[ExecutionModeType] = None
    ParentAutomationExecutionId: Optional[str] = None
    CurrentStepName: Optional[str] = None
    CurrentAction: Optional[str] = None
    FailureMessage: Optional[str] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    ResolvedTargets: Optional[ResolvedTargetsTypeDef] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    Target: Optional[str] = None
    AutomationType: Optional[AutomationTypeType] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None
    AutomationSubtype: Optional[Literal["ChangeRequest"]] = None
    ScheduledTime: Optional[datetime] = None
    Runbooks: Optional[List[RunbookOutputTypeDef]] = None
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ChangeRequestName: Optional[str] = None

class AutomationExecutionTypeDef(BaseModel):
    AutomationExecutionId: Optional[str] = None
    DocumentName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    ExecutionStartTime: Optional[datetime] = None
    ExecutionEndTime: Optional[datetime] = None
    AutomationExecutionStatus: Optional[AutomationExecutionStatusType] = None
    StepExecutions: Optional[List[StepExecutionTypeDef]] = None
    StepExecutionsTruncated: Optional[bool] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    Outputs: Optional[Dict[str, List[str]]] = None
    FailureMessage: Optional[str] = None
    Mode: Optional[ExecutionModeType] = None
    ParentAutomationExecutionId: Optional[str] = None
    ExecutedBy: Optional[str] = None
    CurrentStepName: Optional[str] = None
    CurrentAction: Optional[str] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    ResolvedTargets: Optional[ResolvedTargetsTypeDef] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    Target: Optional[str] = None
    TargetLocations: Optional[List[TargetLocationOutputTypeDef]] = None
    ProgressCounters: Optional[ProgressCountersTypeDef] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    TriggeredAlarms: Optional[List[AlarmStateInformationTypeDef]] = None
    AutomationSubtype: Optional[Literal["ChangeRequest"]] = None
    ScheduledTime: Optional[datetime] = None
    Runbooks: Optional[List[RunbookOutputTypeDef]] = None
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ChangeRequestName: Optional[str] = None
    Variables: Optional[Dict[str, List[str]]] = None

class DescribeAutomationStepExecutionsResultTypeDef(BaseModel):
    StepExecutions: List[StepExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateAssociationRequestRequestTypeDef(BaseModel):
    Name: str
    DocumentVersion: Optional[str] = None
    InstanceId: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    AssociationName: Optional[str] = None
    AutomationTargetParameterName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[Sequence[str]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnionTypeDef]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class StartAutomationExecutionRequestRequestTypeDef(BaseModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    ClientToken: Optional[str] = None
    Mode: Optional[ExecutionModeType] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[Sequence[TargetLocationUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class UpdateAssociationRequestRequestTypeDef(BaseModel):
    AssociationId: str
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    DocumentVersion: Optional[str] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    Name: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    AssociationName: Optional[str] = None
    AssociationVersion: Optional[str] = None
    AutomationTargetParameterName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[Sequence[str]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnionTypeDef]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class GetPatchBaselineResultTypeDef(BaseModel):
    BaselineId: str
    Name: str
    OperatingSystem: OperatingSystemType
    GlobalFilters: PatchFilterGroupOutputTypeDef
    ApprovalRules: PatchRuleGroupOutputTypeDef
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevelType
    ApprovedPatchesEnableNonSecurity: bool
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchActionType
    PatchGroups: List[str]
    CreatedDate: datetime
    ModifiedDate: datetime
    Description: str
    Sources: List[PatchSourceOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePatchBaselineResultTypeDef(BaseModel):
    BaselineId: str
    Name: str
    OperatingSystem: OperatingSystemType
    GlobalFilters: PatchFilterGroupOutputTypeDef
    ApprovalRules: PatchRuleGroupOutputTypeDef
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevelType
    ApprovedPatchesEnableNonSecurity: bool
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchActionType
    CreatedDate: datetime
    ModifiedDate: datetime
    Description: str
    Sources: List[PatchSourceOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BaselineOverrideTypeDef(BaseModel):
    OperatingSystem: Optional[OperatingSystemType] = None
    GlobalFilters: Optional[PatchFilterGroupTypeDef] = None
    ApprovalRules: Optional[PatchRuleGroupTypeDef] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    Sources: Optional[Sequence[PatchSourceTypeDef]] = None

class CreatePatchBaselineRequestRequestTypeDef(BaseModel):
    Name: str
    OperatingSystem: Optional[OperatingSystemType] = None
    GlobalFilters: Optional[PatchFilterGroupTypeDef] = None
    ApprovalRules: Optional[PatchRuleGroupTypeDef] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    Description: Optional[str] = None
    Sources: Optional[Sequence[PatchSourceUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdatePatchBaselineRequestRequestTypeDef(BaseModel):
    BaselineId: str
    Name: Optional[str] = None
    GlobalFilters: Optional[PatchFilterGroupTypeDef] = None
    ApprovalRules: Optional[PatchRuleGroupTypeDef] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    Description: Optional[str] = None
    Sources: Optional[Sequence[PatchSourceUnionTypeDef]] = None
    Replace: Optional[bool] = None

class ListResourceDataSyncResultTypeDef(BaseModel):
    ResourceDataSyncItems: List[ResourceDataSyncItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateAssociationBatchResultTypeDef(BaseModel):
    Successful: List[AssociationDescriptionTypeDef]
    Failed: List[FailedCreateAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAutomationExecutionsResultTypeDef(BaseModel):
    AutomationExecutionMetadataList: List[AutomationExecutionMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetAutomationExecutionResultTypeDef(BaseModel):
    AutomationExecution: AutomationExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssociationBatchRequestRequestTypeDef(BaseModel):
    Entries: Sequence[CreateAssociationBatchRequestEntryUnionTypeDef]

class StartChangeRequestExecutionRequestRequestTypeDef(BaseModel):
    DocumentName: str
    Runbooks: Sequence[RunbookUnionTypeDef]
    ScheduledTime: Optional[TimestampTypeDef] = None
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    ChangeRequestName: Optional[str] = None
    ClientToken: Optional[str] = None
    AutoApprove: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ScheduledEndTime: Optional[TimestampTypeDef] = None
    ChangeDetails: Optional[str] = None

class GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    SnapshotId: str
    BaselineOverride: Optional[BaselineOverrideTypeDef] = None

