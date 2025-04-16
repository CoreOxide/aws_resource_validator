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
from aws_resource_validator.pydantic_models.ssm_constants import *

class AccountSharingInfo(BaseValidatorModel):
    AccountId: Optional[str] = None
    SharedDocumentVersion: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class Alarm(BaseValidatorModel):
    Name: str


class AlarmStateInformation(BaseValidatorModel):
    Name: str
    State: ExternalAlarmStateType


class AssociateOpsItemRelatedItemRequest(BaseValidatorModel):
    OpsItemId: str
    AssociationType: str
    ResourceType: str
    ResourceUri: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociationOverview(BaseValidatorModel):
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    AssociationStatusAggregatedCount: Optional[Dict[str, int]] = None


class AssociationStatusOutput(BaseValidatorModel):
    Date: datetime
    Name: AssociationStatusNameType
    Message: str
    AdditionalInfo: Optional[str] = None


class TargetOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class OutputSource(BaseValidatorModel):
    OutputSourceId: Optional[str] = None
    OutputSourceType: Optional[str] = None


class AssociationExecutionTargetsFilter(BaseValidatorModel):
    Key: AssociationExecutionTargetsFilterKeyType
    Value: str


class AssociationFilter(BaseValidatorModel):
    key: AssociationFilterKeyType
    value: str


class AttachmentContent(BaseValidatorModel):
    Name: Optional[str] = None
    Size: Optional[int] = None
    Hash: Optional[str] = None
    HashType: Optional[Literal["Sha256"]] = None
    Url: Optional[str] = None


class AttachmentInformation(BaseValidatorModel):
    Name: Optional[str] = None


class AttachmentsSource(BaseValidatorModel):
    Key: Optional[AttachmentsSourceKeyType] = None
    Values: Optional[Sequence[str]] = None
    Name: Optional[str] = None


class AutomationExecutionFilter(BaseValidatorModel):
    Key: AutomationExecutionFilterKeyType
    Values: Sequence[str]


class ResolvedTargets(BaseValidatorModel):
    ParameterValues: Optional[List[str]] = None
    Truncated: Optional[bool] = None


class TargetPreview(BaseValidatorModel):
    Count: Optional[int] = None
    TargetType: Optional[str] = None


class ProgressCounters(BaseValidatorModel):
    TotalSteps: Optional[int] = None
    SuccessSteps: Optional[int] = None
    FailedSteps: Optional[int] = None
    CancelledSteps: Optional[int] = None
    TimedOutSteps: Optional[int] = None


class CancelCommandRequest(BaseValidatorModel):
    CommandId: str
    InstanceIds: Optional[Sequence[str]] = None


class CancelMaintenanceWindowExecutionRequest(BaseValidatorModel):
    WindowExecutionId: str


class CloudWatchOutputConfig(BaseValidatorModel):
    CloudWatchLogGroupName: Optional[str] = None
    CloudWatchOutputEnabled: Optional[bool] = None


class CommandFilter(BaseValidatorModel):
    key: CommandFilterKeyType
    value: str


class CommandPlugin(BaseValidatorModel):
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


class NotificationConfigOutput(BaseValidatorModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[List[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None


class ComplianceExecutionSummaryOutput(BaseValidatorModel):
    ExecutionTime: datetime
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None


class ComplianceItemEntry(BaseValidatorModel):
    Severity: ComplianceSeverityType
    Status: ComplianceStatusType
    Id: Optional[str] = None
    Title: Optional[str] = None
    Details: Optional[Mapping[str, str]] = None


class SeveritySummary(BaseValidatorModel):
    CriticalCount: Optional[int] = None
    HighCount: Optional[int] = None
    MediumCount: Optional[int] = None
    LowCount: Optional[int] = None
    InformationalCount: Optional[int] = None
    UnspecifiedCount: Optional[int] = None


class RegistrationMetadataItem(BaseValidatorModel):
    Key: str
    Value: str


class DocumentRequires(BaseValidatorModel):
    Name: str
    Version: Optional[str] = None
    RequireType: Optional[str] = None
    VersionName: Optional[str] = None


class OpsItemNotification(BaseValidatorModel):
    Arn: Optional[str] = None


class RelatedOpsItem(BaseValidatorModel):
    OpsItemId: str


class MetadataValue(BaseValidatorModel):
    Value: Optional[str] = None


class DeleteActivationRequest(BaseValidatorModel):
    ActivationId: str


class DeleteAssociationRequest(BaseValidatorModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None


class DeleteDocumentRequest(BaseValidatorModel):
    Name: str
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None
    Force: Optional[bool] = None


class DeleteInventoryRequest(BaseValidatorModel):
    TypeName: str
    SchemaDeleteOption: Optional[InventorySchemaDeleteOptionType] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


class DeleteMaintenanceWindowRequest(BaseValidatorModel):
    WindowId: str


class DeleteOpsItemRequest(BaseValidatorModel):
    OpsItemId: str


class DeleteOpsMetadataRequest(BaseValidatorModel):
    OpsMetadataArn: str


class DeleteParameterRequest(BaseValidatorModel):
    Name: str


class DeleteParametersRequest(BaseValidatorModel):
    Names: Sequence[str]


class DeletePatchBaselineRequest(BaseValidatorModel):
    BaselineId: str


class DeleteResourceDataSyncRequest(BaseValidatorModel):
    SyncName: str
    SyncType: Optional[str] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    PolicyId: str
    PolicyHash: str


class DeregisterManagedInstanceRequest(BaseValidatorModel):
    InstanceId: str


class DeregisterPatchBaselineForPatchGroupRequest(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str


class DeregisterTargetFromMaintenanceWindowRequest(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    Safe: Optional[bool] = None


class DeregisterTaskFromMaintenanceWindowRequest(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str


class DescribeActivationsFilter(BaseValidatorModel):
    FilterKey: Optional[DescribeActivationsFilterKeysType] = None
    FilterValues: Optional[Sequence[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAssociationRequest(BaseValidatorModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None


class StepExecutionFilter(BaseValidatorModel):
    Key: StepExecutionFilterKeyType
    Values: Sequence[str]


class PatchOrchestratorFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class Patch(BaseValidatorModel):
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


class DescribeDocumentPermissionRequest(BaseValidatorModel):
    Name: str
    PermissionType: Literal["Share"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDocumentRequest(BaseValidatorModel):
    Name: str
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None


class DescribeEffectiveInstanceAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstanceAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    InstanceId: Optional[str] = None
    Content: Optional[str] = None
    AssociationVersion: Optional[str] = None


class DescribeEffectivePatchesForPatchBaselineRequest(BaseValidatorModel):
    BaselineId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceAssociationsStatusRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstanceInformationFilter(BaseValidatorModel):
    key: InstanceInformationFilterKeyType
    valueSet: Sequence[str]


class InstanceInformationStringFilter(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class InstancePatchState(BaseValidatorModel):
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


class DescribeInstancePatchStatesRequest(BaseValidatorModel):
    InstanceIds: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PatchComplianceData(BaseValidatorModel):
    Title: str
    KBId: str
    Classification: str
    Severity: str
    State: PatchComplianceDataStateType
    InstalledTime: datetime
    CVEIds: Optional[str] = None


class InstancePropertyFilter(BaseValidatorModel):
    key: InstancePropertyFilterKeyType
    valueSet: Sequence[str]


class InstancePropertyStringFilter(BaseValidatorModel):
    Key: str
    Values: Sequence[str]
    Operator: Optional[InstancePropertyFilterOperatorType] = None


class DescribeInventoryDeletionsRequest(BaseValidatorModel):
    DeletionId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MaintenanceWindowFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class MaintenanceWindowExecutionTaskInvocationIdentity(BaseValidatorModel):
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


class MaintenanceWindowExecution(BaseValidatorModel):
    WindowId: Optional[str] = None
    WindowExecutionId: Optional[str] = None
    Status: Optional[MaintenanceWindowExecutionStatusType] = None
    StatusDetails: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ScheduledWindowExecution(BaseValidatorModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None
    ExecutionTime: Optional[str] = None


class MaintenanceWindowIdentityForTarget(BaseValidatorModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None


class MaintenanceWindowIdentity(BaseValidatorModel):
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


class OpsItemFilter(BaseValidatorModel):
    Key: OpsItemFilterKeyType
    Values: Sequence[str]
    Operator: OpsItemFilterOperatorType


class ParameterStringFilter(BaseValidatorModel):
    Key: str
    Option: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class ParametersFilter(BaseValidatorModel):
    Key: ParametersFilterKeyType
    Values: Sequence[str]


class PatchBaselineIdentity(BaseValidatorModel):
    BaselineId: Optional[str] = None
    BaselineName: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    BaselineDescription: Optional[str] = None
    DefaultBaseline: Optional[bool] = None


class DescribePatchGroupStateRequest(BaseValidatorModel):
    PatchGroup: str


class DescribePatchPropertiesRequest(BaseValidatorModel):
    OperatingSystem: OperatingSystemType
    Property: PatchPropertyType
    PatchSet: Optional[PatchSetType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SessionFilter(BaseValidatorModel):
    key: SessionFilterKeyType
    value: str


class DisassociateOpsItemRelatedItemRequest(BaseValidatorModel):
    OpsItemId: str
    AssociationId: str


class DocumentDefaultVersionDescription(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultVersion: Optional[str] = None
    DefaultVersionName: Optional[str] = None


class ReviewInformation(BaseValidatorModel):
    ReviewedTime: Optional[datetime] = None
    Status: Optional[ReviewStatusType] = None
    Reviewer: Optional[str] = None


class DocumentFilter(BaseValidatorModel):
    key: DocumentFilterKeyType
    value: str


class DocumentKeyValuesFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class DocumentVersionInfo(BaseValidatorModel):
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


class PatchStatus(BaseValidatorModel):
    DeploymentStatus: Optional[PatchDeploymentStatusType] = None
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovalDate: Optional[datetime] = None


class FailureDetails(BaseValidatorModel):
    FailureStage: Optional[str] = None
    FailureType: Optional[str] = None
    Details: Optional[Dict[str, List[str]]] = None


class GetAutomationExecutionRequest(BaseValidatorModel):
    AutomationExecutionId: str


class GetCalendarStateRequest(BaseValidatorModel):
    CalendarNames: Sequence[str]
    AtTime: Optional[str] = None


class GetCommandInvocationRequest(BaseValidatorModel):
    CommandId: str
    InstanceId: str
    PluginName: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetConnectionStatusRequest(BaseValidatorModel):
    Target: str


class GetDefaultPatchBaselineRequest(BaseValidatorModel):
    OperatingSystem: Optional[OperatingSystemType] = None


class GetDocumentRequest(BaseValidatorModel):
    Name: str
    VersionName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None


class GetExecutionPreviewRequest(BaseValidatorModel):
    ExecutionPreviewId: str


class ResultAttribute(BaseValidatorModel):
    TypeName: str


class GetInventorySchemaRequest(BaseValidatorModel):
    TypeName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Aggregator: Optional[bool] = None
    SubType: Optional[bool] = None


class GetMaintenanceWindowExecutionRequest(BaseValidatorModel):
    WindowExecutionId: str


class GetMaintenanceWindowExecutionTaskInvocationRequest(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str
    InvocationId: str


class GetMaintenanceWindowExecutionTaskRequest(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str


class MaintenanceWindowTaskParameterValueExpressionOutput(BaseValidatorModel):
    Values: Optional[List[str]] = None


class GetMaintenanceWindowRequest(BaseValidatorModel):
    WindowId: str


class GetMaintenanceWindowTaskRequest(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str


class LoggingInfo(BaseValidatorModel):
    S3BucketName: str
    S3Region: str
    S3KeyPrefix: Optional[str] = None


class GetOpsItemRequest(BaseValidatorModel):
    OpsItemId: str
    OpsItemArn: Optional[str] = None


class GetOpsMetadataRequest(BaseValidatorModel):
    OpsMetadataArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OpsResultAttribute(BaseValidatorModel):
    TypeName: str


class GetParameterHistoryRequest(BaseValidatorModel):
    Name: str
    WithDecryption: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetParameterRequest(BaseValidatorModel):
    Name: str
    WithDecryption: Optional[bool] = None


class GetParametersRequest(BaseValidatorModel):
    Names: Sequence[str]
    WithDecryption: Optional[bool] = None


class GetPatchBaselineForPatchGroupRequest(BaseValidatorModel):
    PatchGroup: str
    OperatingSystem: Optional[OperatingSystemType] = None


class GetPatchBaselineRequest(BaseValidatorModel):
    BaselineId: str


class PatchSourceOutput(BaseValidatorModel):
    Name: str
    Products: List[str]
    Configuration: str


class GetResourcePoliciesRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetResourcePoliciesResponseEntry(BaseValidatorModel):
    PolicyId: Optional[str] = None
    PolicyHash: Optional[str] = None
    Policy: Optional[str] = None


class GetServiceSettingRequest(BaseValidatorModel):
    SettingId: str


class ServiceSetting(BaseValidatorModel):
    SettingId: Optional[str] = None
    SettingValue: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    ARN: Optional[str] = None
    Status: Optional[str] = None


class InstanceAggregatedAssociationOverview(BaseValidatorModel):
    DetailedStatus: Optional[str] = None
    InstanceAssociationStatusAggregatedCount: Optional[Dict[str, int]] = None


class S3OutputLocation(BaseValidatorModel):
    OutputS3Region: Optional[str] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None


class S3OutputUrl(BaseValidatorModel):
    OutputUrl: Optional[str] = None


class InstanceInfo(BaseValidatorModel):
    AgentType: Optional[str] = None
    AgentVersion: Optional[str] = None
    ComputerName: Optional[str] = None
    InstanceStatus: Optional[str] = None
    IpAddress: Optional[str] = None
    ManagedStatus: Optional[ManagedStatusType] = None
    PlatformType: Optional[PlatformTypeType] = None
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None


class InventoryDeletionSummaryItem(BaseValidatorModel):
    Version: Optional[str] = None
    Count: Optional[int] = None
    RemainingCount: Optional[int] = None


class InventoryItemAttribute(BaseValidatorModel):
    Name: str
    DataType: InventoryAttributeDataTypeType


class InventoryItem(BaseValidatorModel):
    TypeName: str
    SchemaVersion: str
    CaptureTime: str
    ContentHash: Optional[str] = None
    Content: Optional[Sequence[Mapping[str, str]]] = None
    Context: Optional[Mapping[str, str]] = None


class InventoryResultItem(BaseValidatorModel):
    TypeName: str
    SchemaVersion: str
    Content: List[Dict[str, str]]
    CaptureTime: Optional[str] = None
    ContentHash: Optional[str] = None


class LabelParameterVersionRequest(BaseValidatorModel):
    Name: str
    Labels: Sequence[str]
    ParameterVersion: Optional[int] = None


class ListAssociationVersionsRequest(BaseValidatorModel):
    AssociationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDocumentMetadataHistoryRequest(BaseValidatorModel):
    Name: str
    Metadata: Literal["DocumentReviews"]
    DocumentVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentVersionsRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NodeAggregatorPaginator(BaseValidatorModel):
    AggregatorType: Literal["Count"]
    TypeName: Literal["Instance"]
    AttributeName: NodeAttributeNameType
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class NodeAggregator(BaseValidatorModel):
    AggregatorType: Literal["Count"]
    TypeName: Literal["Instance"]
    AttributeName: NodeAttributeNameType
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class OpsItemEventFilter(BaseValidatorModel):
    Key: Literal["OpsItemId"]
    Values: Sequence[str]
    Operator: Literal["Equal"]


class OpsItemRelatedItemsFilter(BaseValidatorModel):
    Key: OpsItemRelatedItemsFilterKeyType
    Values: Sequence[str]
    Operator: Literal["Equal"]


class OpsMetadataFilter(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class OpsMetadata(BaseValidatorModel):
    ResourceId: Optional[str] = None
    OpsMetadataArn: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    CreationDate: Optional[datetime] = None


class ListResourceDataSyncRequest(BaseValidatorModel):
    SyncType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str


class MaintenanceWindowAutomationParametersOutput(BaseValidatorModel):
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None


class MaintenanceWindowAutomationParameters(BaseValidatorModel):
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None


class MaintenanceWindowLambdaParametersOutput(BaseValidatorModel):
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[bytes] = None


class NotificationConfig(BaseValidatorModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[Sequence[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None


class MaintenanceWindowStepFunctionsParameters(BaseValidatorModel):
    Input: Optional[str] = None
    Name: Optional[str] = None


class MaintenanceWindowTaskParameterValueExpression(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class ModifyDocumentPermissionRequest(BaseValidatorModel):
    Name: str
    PermissionType: Literal["Share"]
    AccountIdsToAdd: Optional[Sequence[str]] = None
    AccountIdsToRemove: Optional[Sequence[str]] = None
    SharedDocumentVersion: Optional[str] = None


class NodeOwnerInfo(BaseValidatorModel):
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    OrganizationalUnitPath: Optional[str] = None


class OpsEntityItem(BaseValidatorModel):
    CaptureTime: Optional[str] = None
    Content: Optional[List[Dict[str, str]]] = None


class OpsItemIdentity(BaseValidatorModel):
    Arn: Optional[str] = None


class ParameterInlinePolicy(BaseValidatorModel):
    PolicyText: Optional[str] = None
    PolicyType: Optional[str] = None
    PolicyStatus: Optional[str] = None


class ParentStepDetails(BaseValidatorModel):
    StepExecutionId: Optional[str] = None
    StepName: Optional[str] = None
    Action: Optional[str] = None
    Iteration: Optional[int] = None
    IteratorValue: Optional[str] = None


class PatchFilterOutput(BaseValidatorModel):
    Key: PatchFilterKeyType
    Values: List[str]


class PatchFilter(BaseValidatorModel):
    Key: PatchFilterKeyType
    Values: Sequence[str]


class PatchSource(BaseValidatorModel):
    Name: str
    Products: Sequence[str]
    Configuration: str


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    PolicyId: Optional[str] = None
    PolicyHash: Optional[str] = None


class RegisterDefaultPatchBaselineRequest(BaseValidatorModel):
    BaselineId: str


class RegisterPatchBaselineForPatchGroupRequest(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str


class RemoveTagsFromResourceRequest(BaseValidatorModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str
    TagKeys: Sequence[str]


class ResetServiceSettingRequest(BaseValidatorModel):
    SettingId: str


class ResourceDataSyncOrganizationalUnit(BaseValidatorModel):
    OrganizationalUnitId: Optional[str] = None


class ResourceDataSyncDestinationDataSharing(BaseValidatorModel):
    DestinationDataSharingType: Optional[str] = None


class ResumeSessionRequest(BaseValidatorModel):
    SessionId: str


class SendAutomationSignalRequest(BaseValidatorModel):
    AutomationExecutionId: str
    SignalType: SignalTypeType
    Payload: Optional[Mapping[str, Sequence[str]]] = None


class SessionManagerOutputUrl(BaseValidatorModel):
    S3OutputUrl: Optional[str] = None
    CloudWatchOutputUrl: Optional[str] = None


class StartAssociationsOnceRequest(BaseValidatorModel):
    AssociationIds: Sequence[str]


class StartSessionRequest(BaseValidatorModel):
    Target: str
    DocumentName: Optional[str] = None
    Reason: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None


class Target(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class TerminateSessionRequest(BaseValidatorModel):
    SessionId: str


class UnlabelParameterVersionRequest(BaseValidatorModel):
    Name: str
    ParameterVersion: int
    Labels: Sequence[str]


class UpdateDocumentDefaultVersionRequest(BaseValidatorModel):
    Name: str
    DocumentVersion: str


class UpdateMaintenanceWindowRequest(BaseValidatorModel):
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


class UpdateManagedInstanceRoleRequest(BaseValidatorModel):
    InstanceId: str
    IamRole: str


class UpdateServiceSettingRequest(BaseValidatorModel):
    SettingId: str
    SettingValue: str


class Activation(BaseValidatorModel):
    ActivationId: Optional[str] = None
    Description: Optional[str] = None
    DefaultInstanceName: Optional[str] = None
    IamRole: Optional[str] = None
    RegistrationLimit: Optional[int] = None
    RegistrationsCount: Optional[int] = None
    ExpirationDate: Optional[datetime] = None
    Expired: Optional[bool] = None
    CreatedDate: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class AddTagsToResourceRequest(BaseValidatorModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str
    Tags: Sequence[Tag]


class CreateMaintenanceWindowRequest(BaseValidatorModel):
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
    Tags: Optional[Sequence[Tag]] = None


class AlarmConfigurationOutput(BaseValidatorModel):
    Alarms: List[Alarm]
    IgnorePollAlarmFailure: Optional[bool] = None


class AlarmConfiguration(BaseValidatorModel):
    Alarms: Sequence[Alarm]
    IgnorePollAlarmFailure: Optional[bool] = None


class AssociateOpsItemRelatedItemResponse(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadata


class CancelMaintenanceWindowExecutionResult(BaseValidatorModel):
    WindowExecutionId: str
    ResponseMetadata: ResponseMetadata


class CreateActivationResult(BaseValidatorModel):
    ActivationId: str
    ActivationCode: str
    ResponseMetadata: ResponseMetadata


class CreateMaintenanceWindowResult(BaseValidatorModel):
    WindowId: str
    ResponseMetadata: ResponseMetadata


class CreateOpsItemResponse(BaseValidatorModel):
    OpsItemId: str
    OpsItemArn: str
    ResponseMetadata: ResponseMetadata


class CreateOpsMetadataResult(BaseValidatorModel):
    OpsMetadataArn: str
    ResponseMetadata: ResponseMetadata


class CreatePatchBaselineResult(BaseValidatorModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadata


class DeleteMaintenanceWindowResult(BaseValidatorModel):
    WindowId: str
    ResponseMetadata: ResponseMetadata


class DeleteParametersResult(BaseValidatorModel):
    DeletedParameters: List[str]
    InvalidParameters: List[str]
    ResponseMetadata: ResponseMetadata


class DeletePatchBaselineResult(BaseValidatorModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadata


class DeregisterPatchBaselineForPatchGroupResult(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str
    ResponseMetadata: ResponseMetadata


class DeregisterTargetFromMaintenanceWindowResult(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    ResponseMetadata: ResponseMetadata


class DeregisterTaskFromMaintenanceWindowResult(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str
    ResponseMetadata: ResponseMetadata


class DescribeDocumentPermissionResponse(BaseValidatorModel):
    AccountIds: List[str]
    AccountSharingInfoList: List[AccountSharingInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePatchGroupStateResult(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class DescribePatchPropertiesResult(BaseValidatorModel):
    Properties: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCalendarStateResponse(BaseValidatorModel):
    State: CalendarStateType
    AtTime: str
    NextTransitionTime: str
    ResponseMetadata: ResponseMetadata


class GetConnectionStatusResponse(BaseValidatorModel):
    Target: str
    Status: ConnectionStatusType
    ResponseMetadata: ResponseMetadata


class GetDefaultPatchBaselineResult(BaseValidatorModel):
    BaselineId: str
    OperatingSystem: OperatingSystemType
    ResponseMetadata: ResponseMetadata


class GetDeployablePatchSnapshotForInstanceResult(BaseValidatorModel):
    InstanceId: str
    SnapshotId: str
    SnapshotDownloadUrl: str
    Product: str
    ResponseMetadata: ResponseMetadata


class GetMaintenanceWindowExecutionResult(BaseValidatorModel):
    WindowExecutionId: str
    TaskIds: List[str]
    Status: MaintenanceWindowExecutionStatusType
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadata


class GetMaintenanceWindowExecutionTaskInvocationResult(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class GetMaintenanceWindowResult(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class GetPatchBaselineForPatchGroupResult(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str
    OperatingSystem: OperatingSystemType
    ResponseMetadata: ResponseMetadata


class LabelParameterVersionResult(BaseValidatorModel):
    InvalidLabels: List[str]
    ParameterVersion: int
    ResponseMetadata: ResponseMetadata


class ListInventoryEntriesResult(BaseValidatorModel):
    TypeName: str
    InstanceId: str
    SchemaVersion: str
    CaptureTime: str
    Entries: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNodesSummaryResult(BaseValidatorModel):
    Summary: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResult(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class PutInventoryResult(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class PutParameterResult(BaseValidatorModel):
    Version: int
    Tier: ParameterTierType
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyResponse(BaseValidatorModel):
    PolicyId: str
    PolicyHash: str
    ResponseMetadata: ResponseMetadata


class RegisterDefaultPatchBaselineResult(BaseValidatorModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadata


class RegisterPatchBaselineForPatchGroupResult(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str
    ResponseMetadata: ResponseMetadata


class RegisterTargetWithMaintenanceWindowResult(BaseValidatorModel):
    WindowTargetId: str
    ResponseMetadata: ResponseMetadata


class RegisterTaskWithMaintenanceWindowResult(BaseValidatorModel):
    WindowTaskId: str
    ResponseMetadata: ResponseMetadata


class ResumeSessionResponse(BaseValidatorModel):
    SessionId: str
    TokenValue: str
    StreamUrl: str
    ResponseMetadata: ResponseMetadata


class StartAutomationExecutionResult(BaseValidatorModel):
    AutomationExecutionId: str
    ResponseMetadata: ResponseMetadata


class StartChangeRequestExecutionResult(BaseValidatorModel):
    AutomationExecutionId: str
    ResponseMetadata: ResponseMetadata


class StartExecutionPreviewResponse(BaseValidatorModel):
    ExecutionPreviewId: str
    ResponseMetadata: ResponseMetadata


class StartSessionResponse(BaseValidatorModel):
    SessionId: str
    TokenValue: str
    StreamUrl: str
    ResponseMetadata: ResponseMetadata


class TerminateSessionResponse(BaseValidatorModel):
    SessionId: str
    ResponseMetadata: ResponseMetadata


class UnlabelParameterVersionResult(BaseValidatorModel):
    RemovedLabels: List[str]
    InvalidLabels: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateMaintenanceWindowResult(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class UpdateOpsMetadataResult(BaseValidatorModel):
    OpsMetadataArn: str
    ResponseMetadata: ResponseMetadata


class Association(BaseValidatorModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[List[TargetOutput]] = None
    LastExecutionDate: Optional[datetime] = None
    Overview: Optional[AssociationOverview] = None
    ScheduleExpression: Optional[str] = None
    AssociationName: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None


class MaintenanceWindowTarget(BaseValidatorModel):
    WindowId: Optional[str] = None
    WindowTargetId: Optional[str] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Targets: Optional[List[TargetOutput]] = None
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateMaintenanceWindowTargetResult(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    Targets: List[TargetOutput]
    OwnerInformation: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadata


class AssociationExecutionFilter(BaseValidatorModel):
    pass


class DescribeAssociationExecutionsRequest(BaseValidatorModel):
    AssociationId: str
    Filters: Optional[Sequence[AssociationExecutionFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AssociationExecutionTarget(BaseValidatorModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    ExecutionId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    OutputSource: Optional[OutputSource] = None


class DescribeAssociationExecutionTargetsRequest(BaseValidatorModel):
    AssociationId: str
    ExecutionId: str
    Filters: Optional[Sequence[AssociationExecutionTargetsFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAssociationsRequest(BaseValidatorModel):
    AssociationFilterList: Optional[Sequence[AssociationFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class AssociationStatus(BaseValidatorModel):
    Date: Timestamp
    Name: AssociationStatusNameType
    Message: str
    AdditionalInfo: Optional[str] = None


class ComplianceExecutionSummary(BaseValidatorModel):
    ExecutionTime: Timestamp
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None


class UpdateDocumentRequest(BaseValidatorModel):
    Content: str
    Name: str
    Attachments: Optional[Sequence[AttachmentsSource]] = None
    DisplayName: Optional[str] = None
    VersionName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None


class DescribeAutomationExecutionsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[AutomationExecutionFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AutomationExecutionPreview(BaseValidatorModel):
    StepPreviews: Optional[Dict[ImpactTypeType, int]] = None
    Regions: Optional[List[str]] = None
    TargetPreviews: Optional[List[TargetPreview]] = None
    TotalAccounts: Optional[int] = None


class Blob(BaseValidatorModel):
    pass


class MaintenanceWindowLambdaParameters(BaseValidatorModel):
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[Blob] = None


class GetCommandInvocationResult(BaseValidatorModel):
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
    CloudWatchOutputConfig: CloudWatchOutputConfig
    ResponseMetadata: ResponseMetadata


class ListCommandInvocationsRequest(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[CommandFilter]] = None
    Details: Optional[bool] = None


class ListCommandsRequest(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[CommandFilter]] = None


class CommandInvocation(BaseValidatorModel):
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
    CommandPlugins: Optional[List[CommandPlugin]] = None
    ServiceRole: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigOutput] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfig] = None


class MaintenanceWindowRunCommandParametersOutput(BaseValidatorModel):
    Comment: Optional[str] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfig] = None
    DocumentHash: Optional[str] = None
    DocumentHashType: Optional[DocumentHashTypeType] = None
    DocumentVersion: Optional[str] = None
    NotificationConfig: Optional[NotificationConfigOutput] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    ServiceRoleArn: Optional[str] = None
    TimeoutSeconds: Optional[int] = None


class ComplianceItem(BaseValidatorModel):
    ComplianceType: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Id: Optional[str] = None
    Title: Optional[str] = None
    Status: Optional[ComplianceStatusType] = None
    Severity: Optional[ComplianceSeverityType] = None
    ExecutionSummary: Optional[ComplianceExecutionSummaryOutput] = None
    Details: Optional[Dict[str, str]] = None


class ComplianceStringFilter(BaseValidatorModel):
    pass


class ListComplianceItemsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilter]] = None
    ResourceIds: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListComplianceSummariesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListResourceComplianceSummariesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CompliantSummary(BaseValidatorModel):
    CompliantCount: Optional[int] = None
    SeveritySummary: Optional[SeveritySummary] = None


class NonCompliantSummary(BaseValidatorModel):
    NonCompliantCount: Optional[int] = None
    SeveritySummary: Optional[SeveritySummary] = None


class CreateActivationRequest(BaseValidatorModel):
    IamRole: str
    Description: Optional[str] = None
    DefaultInstanceName: Optional[str] = None
    RegistrationLimit: Optional[int] = None
    ExpirationDate: Optional[Timestamp] = None
    Tags: Optional[Sequence[Tag]] = None
    RegistrationMetadata: Optional[Sequence[RegistrationMetadataItem]] = None


class CreateDocumentRequest(BaseValidatorModel):
    Content: str
    Name: str
    Requires: Optional[Sequence[DocumentRequires]] = None
    Attachments: Optional[Sequence[AttachmentsSource]] = None
    DisplayName: Optional[str] = None
    VersionName: Optional[str] = None
    DocumentType: Optional[DocumentTypeType] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class DocumentIdentifier(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None
    Requires: Optional[List[DocumentRequires]] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Author: Optional[str] = None


class GetDocumentResult(BaseValidatorModel):
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
    Requires: List[DocumentRequires]
    AttachmentsContent: List[AttachmentContent]
    ReviewStatus: ReviewStatusType
    ResponseMetadata: ResponseMetadata


class OpsItemDataValue(BaseValidatorModel):
    pass


class OpsItemSummary(BaseValidatorModel):
    CreatedBy: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    Priority: Optional[int] = None
    Source: Optional[str] = None
    Status: Optional[OpsItemStatusType] = None
    OpsItemId: Optional[str] = None
    Title: Optional[str] = None
    OperationalData: Optional[Dict[str, OpsItemDataValue]] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    OpsItemType: Optional[str] = None
    ActualStartTime: Optional[datetime] = None
    ActualEndTime: Optional[datetime] = None
    PlannedStartTime: Optional[datetime] = None
    PlannedEndTime: Optional[datetime] = None


class CreateOpsItemRequest(BaseValidatorModel):
    Description: str
    Source: str
    Title: str
    OpsItemType: Optional[str] = None
    OperationalData: Optional[Mapping[str, OpsItemDataValue]] = None
    Notifications: Optional[Sequence[OpsItemNotification]] = None
    Priority: Optional[int] = None
    RelatedOpsItems: Optional[Sequence[RelatedOpsItem]] = None
    Tags: Optional[Sequence[Tag]] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    ActualStartTime: Optional[Timestamp] = None
    ActualEndTime: Optional[Timestamp] = None
    PlannedStartTime: Optional[Timestamp] = None
    PlannedEndTime: Optional[Timestamp] = None
    AccountId: Optional[str] = None


class OpsItem(BaseValidatorModel):
    CreatedBy: Optional[str] = None
    OpsItemType: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    Description: Optional[str] = None
    LastModifiedBy: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    Notifications: Optional[List[OpsItemNotification]] = None
    Priority: Optional[int] = None
    RelatedOpsItems: Optional[List[RelatedOpsItem]] = None
    Status: Optional[OpsItemStatusType] = None
    OpsItemId: Optional[str] = None
    Version: Optional[str] = None
    Title: Optional[str] = None
    Source: Optional[str] = None
    OperationalData: Optional[Dict[str, OpsItemDataValue]] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    ActualStartTime: Optional[datetime] = None
    ActualEndTime: Optional[datetime] = None
    PlannedStartTime: Optional[datetime] = None
    PlannedEndTime: Optional[datetime] = None
    OpsItemArn: Optional[str] = None


class UpdateOpsItemRequest(BaseValidatorModel):
    OpsItemId: str
    Description: Optional[str] = None
    OperationalData: Optional[Mapping[str, OpsItemDataValue]] = None
    OperationalDataToDelete: Optional[Sequence[str]] = None
    Notifications: Optional[Sequence[OpsItemNotification]] = None
    Priority: Optional[int] = None
    RelatedOpsItems: Optional[Sequence[RelatedOpsItem]] = None
    Status: Optional[OpsItemStatusType] = None
    Title: Optional[str] = None
    Category: Optional[str] = None
    Severity: Optional[str] = None
    ActualStartTime: Optional[Timestamp] = None
    ActualEndTime: Optional[Timestamp] = None
    PlannedStartTime: Optional[Timestamp] = None
    PlannedEndTime: Optional[Timestamp] = None
    OpsItemArn: Optional[str] = None


class CreateOpsMetadataRequest(BaseValidatorModel):
    ResourceId: str
    Metadata: Optional[Mapping[str, MetadataValue]] = None
    Tags: Optional[Sequence[Tag]] = None


class GetOpsMetadataResult(BaseValidatorModel):
    ResourceId: str
    Metadata: Dict[str, MetadataValue]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateOpsMetadataRequest(BaseValidatorModel):
    OpsMetadataArn: str
    MetadataToUpdate: Optional[Mapping[str, MetadataValue]] = None
    KeysToDelete: Optional[Sequence[str]] = None


class DescribeActivationsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[DescribeActivationsFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeActivationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[DescribeActivationsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAssociationExecutionTargetsRequestPaginate(BaseValidatorModel):
    AssociationId: str
    ExecutionId: str
    Filters: Optional[Sequence[AssociationExecutionTargetsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAssociationExecutionsRequestPaginate(BaseValidatorModel):
    AssociationId: str
    Filters: Optional[Sequence[AssociationExecutionFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAutomationExecutionsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[AutomationExecutionFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEffectiveInstanceAssociationsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEffectivePatchesForPatchBaselineRequestPaginate(BaseValidatorModel):
    BaselineId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstanceAssociationsStatusRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstancePatchStatesRequestPaginate(BaseValidatorModel):
    InstanceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInventoryDeletionsRequestPaginate(BaseValidatorModel):
    DeletionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePatchPropertiesRequestPaginate(BaseValidatorModel):
    OperatingSystem: OperatingSystemType
    Property: PatchPropertyType
    PatchSet: Optional[PatchSetType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInventorySchemaRequestPaginate(BaseValidatorModel):
    TypeName: Optional[str] = None
    Aggregator: Optional[bool] = None
    SubType: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetParameterHistoryRequestPaginate(BaseValidatorModel):
    Name: str
    WithDecryption: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourcePoliciesRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociationVersionsRequestPaginate(BaseValidatorModel):
    AssociationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociationsRequestPaginate(BaseValidatorModel):
    AssociationFilterList: Optional[Sequence[AssociationFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCommandInvocationsRequestPaginate(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    Filters: Optional[Sequence[CommandFilter]] = None
    Details: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCommandsRequestPaginate(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    Filters: Optional[Sequence[CommandFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComplianceItemsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilter]] = None
    ResourceIds: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComplianceSummariesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDocumentVersionsRequestPaginate(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceComplianceSummariesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceDataSyncRequestPaginate(BaseValidatorModel):
    SyncType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAutomationStepExecutionsRequestPaginate(BaseValidatorModel):
    AutomationExecutionId: str
    Filters: Optional[Sequence[StepExecutionFilter]] = None
    ReverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAutomationStepExecutionsRequest(BaseValidatorModel):
    AutomationExecutionId: str
    Filters: Optional[Sequence[StepExecutionFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ReverseOrder: Optional[bool] = None


class DescribeAvailablePatchesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAvailablePatchesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstancePatchesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstancePatchesRequest(BaseValidatorModel):
    InstanceId: str
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribePatchBaselinesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePatchBaselinesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePatchGroupsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePatchGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    NextToken: Optional[str] = None


class DescribeAvailablePatchesResult(BaseValidatorModel):
    Patches: List[Patch]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEffectiveInstanceAssociationsResult(BaseValidatorModel):
    Associations: List[InstanceAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInstanceInformationRequestPaginate(BaseValidatorModel):
    InstanceInformationFilterList: Optional[Sequence[InstanceInformationFilter]] = None
    Filters: Optional[Sequence[InstanceInformationStringFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstanceInformationRequest(BaseValidatorModel):
    InstanceInformationFilterList: Optional[Sequence[InstanceInformationFilter]] = None
    Filters: Optional[Sequence[InstanceInformationStringFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstancePatchStateFilter(BaseValidatorModel):
    pass


class DescribeInstancePatchStatesForPatchGroupRequestPaginate(BaseValidatorModel):
    PatchGroup: str
    Filters: Optional[Sequence[InstancePatchStateFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstancePatchStatesForPatchGroupRequest(BaseValidatorModel):
    PatchGroup: str
    Filters: Optional[Sequence[InstancePatchStateFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInstancePatchStatesForPatchGroupResult(BaseValidatorModel):
    InstancePatchStates: List[InstancePatchState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInstancePatchStatesResult(BaseValidatorModel):
    InstancePatchStates: List[InstancePatchState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInstancePatchesResult(BaseValidatorModel):
    Patches: List[PatchComplianceData]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInstancePropertiesRequestPaginate(BaseValidatorModel):
    InstancePropertyFilterList: Optional[Sequence[InstancePropertyFilter]] = None
    FiltersWithOperator: Optional[Sequence[InstancePropertyStringFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInstancePropertiesRequest(BaseValidatorModel):
    InstancePropertyFilterList: Optional[Sequence[InstancePropertyFilter]] = None
    FiltersWithOperator: Optional[Sequence[InstancePropertyStringFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginate(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowExecutionTaskInvocationsRequest(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionTasksRequestPaginate(BaseValidatorModel):
    WindowExecutionId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowExecutionTasksRequest(BaseValidatorModel):
    WindowExecutionId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionsRequestPaginate(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowExecutionsRequest(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowTargetsRequestPaginate(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowTargetsRequest(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowTasksRequestPaginate(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowTasksRequest(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[MaintenanceWindowFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionTaskInvocationsResult(BaseValidatorModel):
    WindowExecutionTaskInvocationIdentities: List[ MaintenanceWindowExecutionTaskInvocationIdentity ]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionsResult(BaseValidatorModel):
    WindowExecutions: List[MaintenanceWindowExecution]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowScheduleResult(BaseValidatorModel):
    ScheduledWindowExecutions: List[ScheduledWindowExecution]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsForTargetResult(BaseValidatorModel):
    WindowIdentities: List[MaintenanceWindowIdentityForTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsResult(BaseValidatorModel):
    WindowIdentities: List[MaintenanceWindowIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOpsItemsRequestPaginate(BaseValidatorModel):
    OpsItemFilters: Optional[Sequence[OpsItemFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOpsItemsRequest(BaseValidatorModel):
    OpsItemFilters: Optional[Sequence[OpsItemFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetParametersByPathRequestPaginate(BaseValidatorModel):
    Path: str
    Recursive: Optional[bool] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilter]] = None
    WithDecryption: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetParametersByPathRequest(BaseValidatorModel):
    Path: str
    Recursive: Optional[bool] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilter]] = None
    WithDecryption: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeParametersRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ParametersFilter]] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilter]] = None
    Shared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeParametersRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ParametersFilter]] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Shared: Optional[bool] = None


class DescribePatchBaselinesResult(BaseValidatorModel):
    BaselineIdentities: List[PatchBaselineIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PatchGroupPatchBaselineMapping(BaseValidatorModel):
    PatchGroup: Optional[str] = None
    BaselineIdentity: Optional[PatchBaselineIdentity] = None


class DescribeSessionsRequestPaginate(BaseValidatorModel):
    State: SessionStateType
    Filters: Optional[Sequence[SessionFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSessionsRequest(BaseValidatorModel):
    State: SessionStateType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[SessionFilter]] = None


class UpdateDocumentDefaultVersionResult(BaseValidatorModel):
    Description: DocumentDefaultVersionDescription
    ResponseMetadata: ResponseMetadata


class DocumentParameter(BaseValidatorModel):
    pass


class DocumentDescription(BaseValidatorModel):
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
    Parameters: Optional[List[DocumentParameter]] = None
    PlatformTypes: Optional[List[PlatformTypeType]] = None
    DocumentType: Optional[DocumentTypeType] = None
    SchemaVersion: Optional[str] = None
    LatestVersion: Optional[str] = None
    DefaultVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    AttachmentsInformation: Optional[List[AttachmentInformation]] = None
    Requires: Optional[List[DocumentRequires]] = None
    Author: Optional[str] = None
    ReviewInformation: Optional[List[ReviewInformation]] = None
    ApprovedVersion: Optional[str] = None
    PendingReviewVersion: Optional[str] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Category: Optional[List[str]] = None
    CategoryEnum: Optional[List[str]] = None


class ListDocumentsRequestPaginate(BaseValidatorModel):
    DocumentFilterList: Optional[Sequence[DocumentFilter]] = None
    Filters: Optional[Sequence[DocumentKeyValuesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDocumentsRequest(BaseValidatorModel):
    DocumentFilterList: Optional[Sequence[DocumentFilter]] = None
    Filters: Optional[Sequence[DocumentKeyValuesFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DocumentReviewCommentSource(BaseValidatorModel):
    pass


class DocumentReviewerResponseSource(BaseValidatorModel):
    CreateTime: Optional[datetime] = None
    UpdatedTime: Optional[datetime] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Comment: Optional[List[DocumentReviewCommentSource]] = None
    Reviewer: Optional[str] = None


class DocumentReviews(BaseValidatorModel):
    Action: DocumentReviewActionType
    Comment: Optional[Sequence[DocumentReviewCommentSource]] = None


class ListDocumentVersionsResult(BaseValidatorModel):
    DocumentVersions: List[DocumentVersionInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EffectivePatch(BaseValidatorModel):
    Patch: Optional[Patch] = None
    PatchStatus: Optional[PatchStatus] = None


class GetCommandInvocationRequestWait(BaseValidatorModel):
    CommandId: str
    InstanceId: str
    PluginName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class InventoryFilter(BaseValidatorModel):
    pass


class InventoryGroup(BaseValidatorModel):
    Name: str
    Filters: Sequence[InventoryFilter]


class ListInventoryEntriesRequest(BaseValidatorModel):
    InstanceId: str
    TypeName: str
    Filters: Optional[Sequence[InventoryFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OpsFilter(BaseValidatorModel):
    pass


class OpsAggregatorPaginator(BaseValidatorModel):
    AggregatorType: Optional[str] = None
    TypeName: Optional[str] = None
    AttributeName: Optional[str] = None
    Values: Optional[Mapping[str, str]] = None
    Filters: Optional[Sequence[OpsFilter]] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class OpsAggregator(BaseValidatorModel):
    AggregatorType: Optional[str] = None
    TypeName: Optional[str] = None
    AttributeName: Optional[str] = None
    Values: Optional[Mapping[str, str]] = None
    Filters: Optional[Sequence[OpsFilter]] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class Parameter(BaseValidatorModel):
    pass


class GetParameterResult(BaseValidatorModel):
    Parameter: Parameter
    ResponseMetadata: ResponseMetadata


class GetParametersByPathResult(BaseValidatorModel):
    Parameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetParametersResult(BaseValidatorModel):
    Parameters: List[Parameter]
    InvalidParameters: List[str]
    ResponseMetadata: ResponseMetadata


class GetResourcePoliciesResponse(BaseValidatorModel):
    Policies: List[GetResourcePoliciesResponseEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetServiceSettingResult(BaseValidatorModel):
    ServiceSetting: ServiceSetting
    ResponseMetadata: ResponseMetadata


class ResetServiceSettingResult(BaseValidatorModel):
    ServiceSetting: ServiceSetting
    ResponseMetadata: ResponseMetadata


class InstanceInformation(BaseValidatorModel):
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
    AssociationOverview: Optional[InstanceAggregatedAssociationOverview] = None
    SourceId: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None


class InstanceProperty(BaseValidatorModel):
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
    AssociationOverview: Optional[InstanceAggregatedAssociationOverview] = None
    SourceId: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None


class InstanceAssociationOutputLocation(BaseValidatorModel):
    S3Location: Optional[S3OutputLocation] = None


class InstanceAssociationOutputUrl(BaseValidatorModel):
    S3OutputUrl: Optional[S3OutputUrl] = None


class NodeType(BaseValidatorModel):
    Instance: Optional[InstanceInfo] = None


class InventoryDeletionSummary(BaseValidatorModel):
    TotalCount: Optional[int] = None
    RemainingCount: Optional[int] = None
    SummaryItems: Optional[List[InventoryDeletionSummaryItem]] = None


class InventoryItemSchema(BaseValidatorModel):
    TypeName: str
    Attributes: List[InventoryItemAttribute]
    Version: Optional[str] = None
    DisplayName: Optional[str] = None


class PutInventoryRequest(BaseValidatorModel):
    InstanceId: str
    Items: Sequence[InventoryItem]


class InventoryResultEntity(BaseValidatorModel):
    Id: Optional[str] = None
    Data: Optional[Dict[str, InventoryResultItem]] = None


class NodeFilter(BaseValidatorModel):
    pass


class ListNodesRequestPaginate(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNodesRequest(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListNodesSummaryRequestPaginate(BaseValidatorModel):
    Aggregators: Sequence[NodeAggregatorPaginator]
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNodesSummaryRequest(BaseValidatorModel):
    Aggregators: Sequence[NodeAggregator]
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOpsItemEventsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[OpsItemEventFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOpsItemEventsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[OpsItemEventFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOpsItemRelatedItemsRequestPaginate(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    Filters: Optional[Sequence[OpsItemRelatedItemsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOpsItemRelatedItemsRequest(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    Filters: Optional[Sequence[OpsItemRelatedItemsFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOpsMetadataRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[OpsMetadataFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOpsMetadataRequest(BaseValidatorModel):
    Filters: Optional[Sequence[OpsMetadataFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOpsMetadataResult(BaseValidatorModel):
    OpsMetadataList: List[OpsMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MaintenanceWindowRunCommandParameters(BaseValidatorModel):
    Comment: Optional[str] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfig] = None
    DocumentHash: Optional[str] = None
    DocumentHashType: Optional[DocumentHashTypeType] = None
    DocumentVersion: Optional[str] = None
    NotificationConfig: Optional[NotificationConfig] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    ServiceRoleArn: Optional[str] = None
    TimeoutSeconds: Optional[int] = None


class OpsEntity(BaseValidatorModel):
    Id: Optional[str] = None
    Data: Optional[Dict[str, OpsEntityItem]] = None


class OpsItemEventSummary(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    EventId: Optional[str] = None
    Source: Optional[str] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None
    CreatedBy: Optional[OpsItemIdentity] = None
    CreatedTime: Optional[datetime] = None


class OpsItemRelatedItemSummary(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ResourceType: Optional[str] = None
    AssociationType: Optional[str] = None
    ResourceUri: Optional[str] = None
    CreatedBy: Optional[OpsItemIdentity] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedBy: Optional[OpsItemIdentity] = None
    LastModifiedTime: Optional[datetime] = None


class PatchFilterGroupOutput(BaseValidatorModel):
    PatchFilters: List[PatchFilterOutput]


class ResourceDataSyncAwsOrganizationsSourceOutput(BaseValidatorModel):
    OrganizationSourceType: str
    OrganizationalUnits: Optional[List[ResourceDataSyncOrganizationalUnit]] = None


class ResourceDataSyncAwsOrganizationsSource(BaseValidatorModel):
    OrganizationSourceType: str
    OrganizationalUnits: Optional[Sequence[ResourceDataSyncOrganizationalUnit]] = None


class ResourceDataSyncS3Destination(BaseValidatorModel):
    BucketName: str
    SyncFormat: Literal["JsonSerDe"]
    Region: str
    Prefix: Optional[str] = None
    AWSKMSKeyARN: Optional[str] = None
    DestinationDataSharing: Optional[ResourceDataSyncDestinationDataSharing] = None


class Session(BaseValidatorModel):
    SessionId: Optional[str] = None
    Target: Optional[str] = None
    Status: Optional[SessionStatusType] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    DocumentName: Optional[str] = None
    Owner: Optional[str] = None
    Reason: Optional[str] = None
    Details: Optional[str] = None
    OutputUrl: Optional[SessionManagerOutputUrl] = None
    MaxSessionDuration: Optional[str] = None


class DescribeActivationsResult(BaseValidatorModel):
    ActivationList: List[Activation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociationExecution(BaseValidatorModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    ExecutionId: Optional[str] = None
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastExecutionDate: Optional[datetime] = None
    ResourceCountByStatus: Optional[str] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None


class Command(BaseValidatorModel):
    CommandId: Optional[str] = None
    DocumentName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Comment: Optional[str] = None
    ExpiresAfter: Optional[datetime] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    InstanceIds: Optional[List[str]] = None
    Targets: Optional[List[TargetOutput]] = None
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
    NotificationConfig: Optional[NotificationConfigOutput] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfig] = None
    TimeoutSeconds: Optional[int] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None


class MaintenanceWindowExecutionTaskIdentity(BaseValidatorModel):
    WindowExecutionId: Optional[str] = None
    TaskExecutionId: Optional[str] = None
    Status: Optional[MaintenanceWindowExecutionStatusType] = None
    StatusDetails: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    TaskArn: Optional[str] = None
    TaskType: Optional[MaintenanceWindowTaskTypeType] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None


class TargetLocationOutput(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    Regions: Optional[List[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    IncludeChildOrganizationUnits: Optional[bool] = None
    ExcludeAccounts: Optional[List[str]] = None
    Targets: Optional[List[TargetOutput]] = None
    TargetsMaxConcurrency: Optional[str] = None
    TargetsMaxErrors: Optional[str] = None


class ListAssociationsResult(BaseValidatorModel):
    Associations: List[Association]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowTargetsResult(BaseValidatorModel):
    Targets: List[MaintenanceWindowTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAssociationExecutionTargetsResult(BaseValidatorModel):
    AssociationExecutionTargets: List[AssociationExecutionTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExecutionPreview(BaseValidatorModel):
    Automation: Optional[AutomationExecutionPreview] = None


class ListCommandInvocationsResult(BaseValidatorModel):
    CommandInvocations: List[CommandInvocation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MaintenanceWindowTaskInvocationParametersOutput(BaseValidatorModel):
    RunCommand: Optional[MaintenanceWindowRunCommandParametersOutput] = None
    Automation: Optional[MaintenanceWindowAutomationParametersOutput] = None
    StepFunctions: Optional[MaintenanceWindowStepFunctionsParameters] = None
    Lambda: Optional[MaintenanceWindowLambdaParametersOutput] = None


class ListComplianceItemsResult(BaseValidatorModel):
    ComplianceItems: List[ComplianceItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ComplianceSummaryItem(BaseValidatorModel):
    ComplianceType: Optional[str] = None
    CompliantSummary: Optional[CompliantSummary] = None
    NonCompliantSummary: Optional[NonCompliantSummary] = None


class ResourceComplianceSummaryItem(BaseValidatorModel):
    ComplianceType: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ComplianceStatusType] = None
    OverallSeverity: Optional[ComplianceSeverityType] = None
    ExecutionSummary: Optional[ComplianceExecutionSummaryOutput] = None
    CompliantSummary: Optional[CompliantSummary] = None
    NonCompliantSummary: Optional[NonCompliantSummary] = None


class ListDocumentsResult(BaseValidatorModel):
    DocumentIdentifiers: List[DocumentIdentifier]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOpsItemsResponse(BaseValidatorModel):
    OpsItemSummaries: List[OpsItemSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetOpsItemResponse(BaseValidatorModel):
    OpsItem: OpsItem
    ResponseMetadata: ResponseMetadata


class DescribePatchGroupsResult(BaseValidatorModel):
    Mappings: List[PatchGroupPatchBaselineMapping]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateDocumentResult(BaseValidatorModel):
    DocumentDescription: DocumentDescription
    ResponseMetadata: ResponseMetadata


class DescribeDocumentResult(BaseValidatorModel):
    Document: DocumentDescription
    ResponseMetadata: ResponseMetadata


class UpdateDocumentResult(BaseValidatorModel):
    DocumentDescription: DocumentDescription
    ResponseMetadata: ResponseMetadata


class DocumentMetadataResponseInfo(BaseValidatorModel):
    ReviewerResponse: Optional[List[DocumentReviewerResponseSource]] = None


class UpdateDocumentMetadataRequest(BaseValidatorModel):
    Name: str
    DocumentReviews: DocumentReviews
    DocumentVersion: Optional[str] = None


class DescribeEffectivePatchesForPatchBaselineResult(BaseValidatorModel):
    EffectivePatches: List[EffectivePatch]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InventoryAggregatorPaginator(BaseValidatorModel):
    Expression: Optional[str] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None
    Groups: Optional[Sequence[InventoryGroup]] = None


class InventoryAggregator(BaseValidatorModel):
    Expression: Optional[str] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None
    Groups: Optional[Sequence[InventoryGroup]] = None


class GetOpsSummaryRequestPaginate(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[OpsFilter]] = None
    Aggregators: Optional[Sequence[OpsAggregatorPaginator]] = None
    ResultAttributes: Optional[Sequence[OpsResultAttribute]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetOpsSummaryRequest(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[OpsFilter]] = None
    Aggregators: Optional[Sequence[OpsAggregator]] = None
    ResultAttributes: Optional[Sequence[OpsResultAttribute]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInstanceInformationResult(BaseValidatorModel):
    InstanceInformationList: List[InstanceInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInstancePropertiesResult(BaseValidatorModel):
    InstanceProperties: List[InstanceProperty]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceAssociationStatusInfo(BaseValidatorModel):
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
    OutputUrl: Optional[InstanceAssociationOutputUrl] = None
    AssociationName: Optional[str] = None


class Node(BaseValidatorModel):
    CaptureTime: Optional[datetime] = None
    Id: Optional[str] = None
    Owner: Optional[NodeOwnerInfo] = None
    Region: Optional[str] = None
    NodeType: Optional[NodeType] = None


class DeleteInventoryResult(BaseValidatorModel):
    DeletionId: str
    TypeName: str
    DeletionSummary: InventoryDeletionSummary
    ResponseMetadata: ResponseMetadata


class InventoryDeletionStatusItem(BaseValidatorModel):
    DeletionId: Optional[str] = None
    TypeName: Optional[str] = None
    DeletionStartTime: Optional[datetime] = None
    LastStatus: Optional[InventoryDeletionStatusType] = None
    LastStatusMessage: Optional[str] = None
    DeletionSummary: Optional[InventoryDeletionSummary] = None
    LastStatusUpdateTime: Optional[datetime] = None


class GetInventorySchemaResult(BaseValidatorModel):
    Schemas: List[InventoryItemSchema]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetInventoryResult(BaseValidatorModel):
    Entities: List[InventoryResultEntity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MaintenanceWindowTaskInvocationParameters(BaseValidatorModel):
    RunCommand: Optional[MaintenanceWindowRunCommandParameters] = None
    Automation: Optional[MaintenanceWindowAutomationParameters] = None
    StepFunctions: Optional[MaintenanceWindowStepFunctionsParameters] = None
    Lambda: Optional[MaintenanceWindowLambdaParameters] = None


class GetOpsSummaryResult(BaseValidatorModel):
    Entities: List[OpsEntity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOpsItemEventsResponse(BaseValidatorModel):
    Summaries: List[OpsItemEventSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOpsItemRelatedItemsResponse(BaseValidatorModel):
    Summaries: List[OpsItemRelatedItemSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ParameterHistory(BaseValidatorModel):
    pass


class GetParameterHistoryResult(BaseValidatorModel):
    Parameters: List[ParameterHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ParameterMetadata(BaseValidatorModel):
    pass


class DescribeParametersResult(BaseValidatorModel):
    Parameters: List[ParameterMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PatchRuleOutput(BaseValidatorModel):
    PatchFilterGroup: PatchFilterGroupOutput
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApproveAfterDays: Optional[int] = None
    ApproveUntilDate: Optional[str] = None
    EnableNonSecurity: Optional[bool] = None


class PatchFilterUnion(BaseValidatorModel):
    pass


class PatchFilterGroup(BaseValidatorModel):
    PatchFilters: Sequence[PatchFilterUnion]


class ResourceDataSyncSourceWithState(BaseValidatorModel):
    SourceType: Optional[str] = None
    AwsOrganizationsSource: Optional[ResourceDataSyncAwsOrganizationsSourceOutput] = None
    SourceRegions: Optional[List[str]] = None
    IncludeFutureRegions: Optional[bool] = None
    State: Optional[str] = None
    EnableAllOpsDataSources: Optional[bool] = None


class DescribeSessionsResponse(BaseValidatorModel):
    Sessions: List[Session]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TargetUnion(BaseValidatorModel):
    pass


class DescribeMaintenanceWindowScheduleRequestPaginate(BaseValidatorModel):
    WindowId: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowScheduleRequest(BaseValidatorModel):
    WindowId: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Filters: Optional[Sequence[PatchOrchestratorFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsForTargetRequestPaginate(BaseValidatorModel):
    Targets: Sequence[TargetUnion]
    ResourceType: MaintenanceWindowResourceTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMaintenanceWindowsForTargetRequest(BaseValidatorModel):
    Targets: Sequence[TargetUnion]
    ResourceType: MaintenanceWindowResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RegisterTargetWithMaintenanceWindowRequest(BaseValidatorModel):
    WindowId: str
    ResourceType: MaintenanceWindowResourceTypeType
    Targets: Sequence[TargetUnion]
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdateMaintenanceWindowTargetRequest(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    Targets: Optional[Sequence[TargetUnion]] = None
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Replace: Optional[bool] = None


class DescribeAssociationExecutionsResult(BaseValidatorModel):
    AssociationExecutions: List[AssociationExecution]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCommandsResult(BaseValidatorModel):
    Commands: List[Command]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SendCommandResult(BaseValidatorModel):
    Command: Command
    ResponseMetadata: ResponseMetadata


class DescribeMaintenanceWindowExecutionTasksResult(BaseValidatorModel):
    WindowExecutionTaskIdentities: List[MaintenanceWindowExecutionTaskIdentity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MaintenanceWindowTask(BaseValidatorModel):
    pass


class DescribeMaintenanceWindowTasksResult(BaseValidatorModel):
    Tasks: List[MaintenanceWindowTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociationDescription(BaseValidatorModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    Date: Optional[datetime] = None
    LastUpdateAssociationDate: Optional[datetime] = None
    Status: Optional[AssociationStatusOutput] = None
    Overview: Optional[AssociationOverview] = None
    DocumentVersion: Optional[str] = None
    AutomationTargetParameterName: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    AssociationId: Optional[str] = None
    Targets: Optional[List[TargetOutput]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocation] = None
    LastExecutionDate: Optional[datetime] = None
    LastSuccessfulExecutionDate: Optional[datetime] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[List[str]] = None
    TargetLocations: Optional[List[TargetLocationOutput]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None


class AssociationVersionInfo(BaseValidatorModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Name: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    Targets: Optional[List[TargetOutput]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocation] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[List[str]] = None
    TargetLocations: Optional[List[TargetLocationOutput]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None


class CreateAssociationBatchRequestEntryOutput(BaseValidatorModel):
    Name: str
    InstanceId: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    AutomationTargetParameterName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[List[TargetOutput]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocation] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[List[str]] = None
    TargetLocations: Optional[List[TargetLocationOutput]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None


class RunbookOutput(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[List[TargetOutput]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[List[TargetLocationOutput]] = None


class StepExecution(BaseValidatorModel):
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
    FailureDetails: Optional[FailureDetails] = None
    StepExecutionId: Optional[str] = None
    OverriddenParameters: Optional[Dict[str, List[str]]] = None
    IsEnd: Optional[bool] = None
    NextStep: Optional[str] = None
    IsCritical: Optional[bool] = None
    ValidNextSteps: Optional[List[str]] = None
    Targets: Optional[List[TargetOutput]] = None
    TargetLocation: Optional[TargetLocationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None
    ParentStepDetails: Optional[ParentStepDetails] = None


class AlarmConfigurationUnion(BaseValidatorModel):
    pass


class NotificationConfigUnion(BaseValidatorModel):
    pass


class SendCommandRequest(BaseValidatorModel):
    DocumentName: str
    InstanceIds: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[TargetUnion]] = None
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
    NotificationConfig: Optional[NotificationConfigUnion] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfig] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class TargetLocation(BaseValidatorModel):
    Accounts: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationUnion] = None
    IncludeChildOrganizationUnits: Optional[bool] = None
    ExcludeAccounts: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    TargetsMaxConcurrency: Optional[str] = None
    TargetsMaxErrors: Optional[str] = None


class AssociationStatusUnion(BaseValidatorModel):
    pass


class UpdateAssociationStatusRequest(BaseValidatorModel):
    Name: str
    InstanceId: str
    AssociationStatus: AssociationStatusUnion


class ComplianceExecutionSummaryUnion(BaseValidatorModel):
    pass


class PutComplianceItemsRequest(BaseValidatorModel):
    ResourceId: str
    ResourceType: str
    ComplianceType: str
    ExecutionSummary: ComplianceExecutionSummaryUnion
    Items: Sequence[ComplianceItemEntry]
    ItemContentHash: Optional[str] = None
    UploadType: Optional[ComplianceUploadTypeType] = None


class GetExecutionPreviewResponse(BaseValidatorModel):
    ExecutionPreviewId: str
    EndedAt: datetime
    Status: ExecutionPreviewStatusType
    StatusMessage: str
    ExecutionPreview: ExecutionPreview
    ResponseMetadata: ResponseMetadata


class GetMaintenanceWindowTaskResult(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str
    Targets: List[TargetOutput]
    TaskArn: str
    ServiceRoleArn: str
    TaskType: MaintenanceWindowTaskTypeType
    TaskParameters: Dict[str, MaintenanceWindowTaskParameterValueExpressionOutput]
    TaskInvocationParameters: MaintenanceWindowTaskInvocationParametersOutput
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    LoggingInfo: LoggingInfo
    Name: str
    Description: str
    CutoffBehavior: MaintenanceWindowTaskCutoffBehaviorType
    AlarmConfiguration: AlarmConfigurationOutput
    ResponseMetadata: ResponseMetadata


class UpdateMaintenanceWindowTaskResult(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str
    Targets: List[TargetOutput]
    TaskArn: str
    ServiceRoleArn: str
    TaskParameters: Dict[str, MaintenanceWindowTaskParameterValueExpressionOutput]
    TaskInvocationParameters: MaintenanceWindowTaskInvocationParametersOutput
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    LoggingInfo: LoggingInfo
    Name: str
    Description: str
    CutoffBehavior: MaintenanceWindowTaskCutoffBehaviorType
    AlarmConfiguration: AlarmConfigurationOutput
    ResponseMetadata: ResponseMetadata


class ListComplianceSummariesResult(BaseValidatorModel):
    ComplianceSummaryItems: List[ComplianceSummaryItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceComplianceSummariesResult(BaseValidatorModel):
    ResourceComplianceSummaryItems: List[ResourceComplianceSummaryItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDocumentMetadataHistoryResponse(BaseValidatorModel):
    Name: str
    DocumentVersion: str
    Author: str
    Metadata: DocumentMetadataResponseInfo
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetInventoryRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[InventoryFilter]] = None
    Aggregators: Optional[Sequence[InventoryAggregatorPaginator]] = None
    ResultAttributes: Optional[Sequence[ResultAttribute]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInventoryRequest(BaseValidatorModel):
    Filters: Optional[Sequence[InventoryFilter]] = None
    Aggregators: Optional[Sequence[InventoryAggregator]] = None
    ResultAttributes: Optional[Sequence[ResultAttribute]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInstanceAssociationsStatusResult(BaseValidatorModel):
    InstanceAssociationStatusInfos: List[InstanceAssociationStatusInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNodesResult(BaseValidatorModel):
    Nodes: List[Node]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInventoryDeletionsResult(BaseValidatorModel):
    InventoryDeletions: List[InventoryDeletionStatusItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PatchRuleGroupOutput(BaseValidatorModel):
    PatchRules: List[PatchRuleOutput]


class ResourceDataSyncItem(BaseValidatorModel):
    SyncName: Optional[str] = None
    SyncType: Optional[str] = None
    SyncSource: Optional[ResourceDataSyncSourceWithState] = None
    S3Destination: Optional[ResourceDataSyncS3Destination] = None
    LastSyncTime: Optional[datetime] = None
    LastSuccessfulSyncTime: Optional[datetime] = None
    SyncLastModifiedTime: Optional[datetime] = None
    LastStatus: Optional[LastResourceDataSyncStatusType] = None
    SyncCreatedTime: Optional[datetime] = None
    LastSyncStatusMessage: Optional[str] = None


class ResourceDataSyncAwsOrganizationsSourceUnion(BaseValidatorModel):
    pass


class ResourceDataSyncSource(BaseValidatorModel):
    SourceType: str
    SourceRegions: Sequence[str]
    AwsOrganizationsSource: Optional[ResourceDataSyncAwsOrganizationsSourceUnion] = None
    IncludeFutureRegions: Optional[bool] = None
    EnableAllOpsDataSources: Optional[bool] = None


class CreateAssociationResult(BaseValidatorModel):
    AssociationDescription: AssociationDescription
    ResponseMetadata: ResponseMetadata


class DescribeAssociationResult(BaseValidatorModel):
    AssociationDescription: AssociationDescription
    ResponseMetadata: ResponseMetadata


class UpdateAssociationResult(BaseValidatorModel):
    AssociationDescription: AssociationDescription
    ResponseMetadata: ResponseMetadata


class UpdateAssociationStatusResult(BaseValidatorModel):
    AssociationDescription: AssociationDescription
    ResponseMetadata: ResponseMetadata


class ListAssociationVersionsResult(BaseValidatorModel):
    AssociationVersions: List[AssociationVersionInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FailedCreateAssociation(BaseValidatorModel):
    Entry: Optional[CreateAssociationBatchRequestEntryOutput] = None
    Message: Optional[str] = None
    Fault: Optional[FaultType] = None


class AutomationExecutionMetadata(BaseValidatorModel):
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
    Targets: Optional[List[TargetOutput]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    ResolvedTargets: Optional[ResolvedTargets] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    Target: Optional[str] = None
    AutomationType: Optional[AutomationTypeType] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None
    TargetLocationsURL: Optional[str] = None
    AutomationSubtype: Optional[Literal["ChangeRequest"]] = None
    ScheduledTime: Optional[datetime] = None
    Runbooks: Optional[List[RunbookOutput]] = None
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ChangeRequestName: Optional[str] = None


class AutomationExecution(BaseValidatorModel):
    AutomationExecutionId: Optional[str] = None
    DocumentName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    ExecutionStartTime: Optional[datetime] = None
    ExecutionEndTime: Optional[datetime] = None
    AutomationExecutionStatus: Optional[AutomationExecutionStatusType] = None
    StepExecutions: Optional[List[StepExecution]] = None
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
    Targets: Optional[List[TargetOutput]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    ResolvedTargets: Optional[ResolvedTargets] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    Target: Optional[str] = None
    TargetLocations: Optional[List[TargetLocationOutput]] = None
    ProgressCounters: Optional[ProgressCounters] = None
    AlarmConfiguration: Optional[AlarmConfigurationOutput] = None
    TriggeredAlarms: Optional[List[AlarmStateInformation]] = None
    TargetLocationsURL: Optional[str] = None
    AutomationSubtype: Optional[Literal["ChangeRequest"]] = None
    ScheduledTime: Optional[datetime] = None
    Runbooks: Optional[List[RunbookOutput]] = None
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ChangeRequestName: Optional[str] = None
    Variables: Optional[Dict[str, List[str]]] = None


class DescribeAutomationStepExecutionsResult(BaseValidatorModel):
    StepExecutions: List[StepExecution]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MaintenanceWindowTaskParameterValueExpressionUnion(BaseValidatorModel):
    pass


class MaintenanceWindowTaskInvocationParametersUnion(BaseValidatorModel):
    pass


class RegisterTaskWithMaintenanceWindowRequest(BaseValidatorModel):
    WindowId: str
    TaskArn: str
    TaskType: MaintenanceWindowTaskTypeType
    Targets: Optional[Sequence[TargetUnion]] = None
    ServiceRoleArn: Optional[str] = None
    TaskParameters: Optional[ Mapping[str, MaintenanceWindowTaskParameterValueExpressionUnion] ] = None
    TaskInvocationParameters: Optional[MaintenanceWindowTaskInvocationParametersUnion] = None
    Priority: Optional[int] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    LoggingInfo: Optional[LoggingInfo] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class UpdateMaintenanceWindowTaskRequest(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str
    Targets: Optional[Sequence[TargetUnion]] = None
    TaskArn: Optional[str] = None
    ServiceRoleArn: Optional[str] = None
    TaskParameters: Optional[ Mapping[str, MaintenanceWindowTaskParameterValueExpressionUnion] ] = None
    TaskInvocationParameters: Optional[MaintenanceWindowTaskInvocationParametersUnion] = None
    Priority: Optional[int] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    LoggingInfo: Optional[LoggingInfo] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Replace: Optional[bool] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class GetPatchBaselineResult(BaseValidatorModel):
    BaselineId: str
    Name: str
    OperatingSystem: OperatingSystemType
    GlobalFilters: PatchFilterGroupOutput
    ApprovalRules: PatchRuleGroupOutput
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevelType
    ApprovedPatchesEnableNonSecurity: bool
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchActionType
    PatchGroups: List[str]
    CreatedDate: datetime
    ModifiedDate: datetime
    Description: str
    Sources: List[PatchSourceOutput]
    ResponseMetadata: ResponseMetadata


class UpdatePatchBaselineResult(BaseValidatorModel):
    BaselineId: str
    Name: str
    OperatingSystem: OperatingSystemType
    GlobalFilters: PatchFilterGroupOutput
    ApprovalRules: PatchRuleGroupOutput
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevelType
    ApprovedPatchesEnableNonSecurity: bool
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchActionType
    CreatedDate: datetime
    ModifiedDate: datetime
    Description: str
    Sources: List[PatchSourceOutput]
    ResponseMetadata: ResponseMetadata


class PatchFilterGroupUnion(BaseValidatorModel):
    pass


class PatchRule(BaseValidatorModel):
    PatchFilterGroup: PatchFilterGroupUnion
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApproveAfterDays: Optional[int] = None
    ApproveUntilDate: Optional[str] = None
    EnableNonSecurity: Optional[bool] = None


class ListResourceDataSyncResult(BaseValidatorModel):
    ResourceDataSyncItems: List[ResourceDataSyncItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateResourceDataSyncRequest(BaseValidatorModel):
    SyncName: str
    S3Destination: Optional[ResourceDataSyncS3Destination] = None
    SyncType: Optional[str] = None
    SyncSource: Optional[ResourceDataSyncSource] = None


class UpdateResourceDataSyncRequest(BaseValidatorModel):
    SyncName: str
    SyncType: str
    SyncSource: ResourceDataSyncSource


class CreateAssociationBatchResult(BaseValidatorModel):
    Successful: List[AssociationDescription]
    Failed: List[FailedCreateAssociation]
    ResponseMetadata: ResponseMetadata


class DescribeAutomationExecutionsResult(BaseValidatorModel):
    AutomationExecutionMetadataList: List[AutomationExecutionMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetAutomationExecutionResult(BaseValidatorModel):
    AutomationExecution: AutomationExecution
    ResponseMetadata: ResponseMetadata


class TargetLocationUnion(BaseValidatorModel):
    pass


class AutomationExecutionInputs(BaseValidatorModel):
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnion]] = None
    TargetLocationsURL: Optional[str] = None


class CreateAssociationBatchRequestEntry(BaseValidatorModel):
    Name: str
    InstanceId: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    AutomationTargetParameterName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocation] = None
    AssociationName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[Sequence[str]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnion]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class CreateAssociationRequest(BaseValidatorModel):
    Name: str
    DocumentVersion: Optional[str] = None
    InstanceId: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocation] = None
    AssociationName: Optional[str] = None
    AutomationTargetParameterName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[Sequence[str]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnion]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    Tags: Optional[Sequence[Tag]] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class Runbook(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[Sequence[TargetLocationUnion]] = None


class StartAutomationExecutionRequest(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    ClientToken: Optional[str] = None
    Mode: Optional[ExecutionModeType] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[Sequence[TargetLocationUnion]] = None
    Tags: Optional[Sequence[Tag]] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None
    TargetLocationsURL: Optional[str] = None


class UpdateAssociationRequest(BaseValidatorModel):
    AssociationId: str
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    DocumentVersion: Optional[str] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocation] = None
    Name: Optional[str] = None
    Targets: Optional[Sequence[TargetUnion]] = None
    AssociationName: Optional[str] = None
    AssociationVersion: Optional[str] = None
    AutomationTargetParameterName: Optional[str] = None
    MaxErrors: Optional[str] = None
    MaxConcurrency: Optional[str] = None
    ComplianceSeverity: Optional[AssociationComplianceSeverityType] = None
    SyncCompliance: Optional[AssociationSyncComplianceType] = None
    ApplyOnlyAtCronInterval: Optional[bool] = None
    CalendarNames: Optional[Sequence[str]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnion]] = None
    ScheduleOffset: Optional[int] = None
    Duration: Optional[int] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class ExecutionInputs(BaseValidatorModel):
    Automation: Optional[AutomationExecutionInputs] = None


class PatchRuleUnion(BaseValidatorModel):
    pass


class PatchRuleGroup(BaseValidatorModel):
    PatchRules: Sequence[PatchRuleUnion]


class StartExecutionPreviewRequest(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    ExecutionInputs: Optional[ExecutionInputs] = None


class CreateAssociationBatchRequestEntryUnion(BaseValidatorModel):
    pass


class CreateAssociationBatchRequest(BaseValidatorModel):
    Entries: Sequence[CreateAssociationBatchRequestEntryUnion]


class RunbookUnion(BaseValidatorModel):
    pass


class StartChangeRequestExecutionRequest(BaseValidatorModel):
    DocumentName: str
    Runbooks: Sequence[RunbookUnion]
    ScheduledTime: Optional[Timestamp] = None
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    ChangeRequestName: Optional[str] = None
    ClientToken: Optional[str] = None
    AutoApprove: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None
    ScheduledEndTime: Optional[Timestamp] = None
    ChangeDetails: Optional[str] = None


class PatchRuleGroupUnion(BaseValidatorModel):
    pass


class PatchSourceUnion(BaseValidatorModel):
    pass


class BaselineOverride(BaseValidatorModel):
    OperatingSystem: Optional[OperatingSystemType] = None
    GlobalFilters: Optional[PatchFilterGroupUnion] = None
    ApprovalRules: Optional[PatchRuleGroupUnion] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    Sources: Optional[Sequence[PatchSourceUnion]] = None


class CreatePatchBaselineRequest(BaseValidatorModel):
    Name: str
    OperatingSystem: Optional[OperatingSystemType] = None
    GlobalFilters: Optional[PatchFilterGroupUnion] = None
    ApprovalRules: Optional[PatchRuleGroupUnion] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    Description: Optional[str] = None
    Sources: Optional[Sequence[PatchSourceUnion]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class UpdatePatchBaselineRequest(BaseValidatorModel):
    BaselineId: str
    Name: Optional[str] = None
    GlobalFilters: Optional[PatchFilterGroupUnion] = None
    ApprovalRules: Optional[PatchRuleGroupUnion] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    Description: Optional[str] = None
    Sources: Optional[Sequence[PatchSourceUnion]] = None
    Replace: Optional[bool] = None


class GetDeployablePatchSnapshotForInstanceRequest(BaseValidatorModel):
    InstanceId: str
    SnapshotId: str
    BaselineOverride: Optional[BaselineOverride] = None


