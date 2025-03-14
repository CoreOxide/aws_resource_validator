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

class AccountSharingInfoTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    SharedDocumentVersion: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class AlarmTypeDef(BaseValidatorModel):
    Name: str


class AlarmStateInformationTypeDef(BaseValidatorModel):
    Name: str
    State: ExternalAlarmStateType


class AssociateOpsItemRelatedItemRequestTypeDef(BaseValidatorModel):
    OpsItemId: str
    AssociationType: str
    ResourceType: str
    ResourceUri: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociationOverviewTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    AssociationStatusAggregatedCount: Optional[Dict[str, int]] = None


class AssociationStatusOutputTypeDef(BaseValidatorModel):
    Date: datetime
    Name: AssociationStatusNameType
    Message: str
    AdditionalInfo: Optional[str] = None


class TargetOutputTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class OutputSourceTypeDef(BaseValidatorModel):
    OutputSourceId: Optional[str] = None
    OutputSourceType: Optional[str] = None


class AssociationExecutionTargetsFilterTypeDef(BaseValidatorModel):
    Key: AssociationExecutionTargetsFilterKeyType
    Value: str


class AssociationFilterTypeDef(BaseValidatorModel):
    key: AssociationFilterKeyType
    value: str


class AttachmentContentTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Size: Optional[int] = None
    Hash: Optional[str] = None
    HashType: Optional[Literal["Sha256"]] = None
    Url: Optional[str] = None


class AttachmentInformationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class AttachmentsSourceTypeDef(BaseValidatorModel):
    Key: Optional[AttachmentsSourceKeyType] = None
    Values: Optional[Sequence[str]] = None
    Name: Optional[str] = None


class AutomationExecutionFilterTypeDef(BaseValidatorModel):
    Key: AutomationExecutionFilterKeyType
    Values: Sequence[str]


class ResolvedTargetsTypeDef(BaseValidatorModel):
    ParameterValues: Optional[List[str]] = None
    Truncated: Optional[bool] = None


class TargetPreviewTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    TargetType: Optional[str] = None


class ProgressCountersTypeDef(BaseValidatorModel):
    TotalSteps: Optional[int] = None
    SuccessSteps: Optional[int] = None
    FailedSteps: Optional[int] = None
    CancelledSteps: Optional[int] = None
    TimedOutSteps: Optional[int] = None


class CancelCommandRequestTypeDef(BaseValidatorModel):
    CommandId: str
    InstanceIds: Optional[Sequence[str]] = None


class CancelMaintenanceWindowExecutionRequestTypeDef(BaseValidatorModel):
    WindowExecutionId: str


class CloudWatchOutputConfigTypeDef(BaseValidatorModel):
    CloudWatchLogGroupName: Optional[str] = None
    CloudWatchOutputEnabled: Optional[bool] = None


class CommandFilterTypeDef(BaseValidatorModel):
    key: CommandFilterKeyType
    value: str


class CommandPluginTypeDef(BaseValidatorModel):
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


class NotificationConfigOutputTypeDef(BaseValidatorModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[List[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None


class ComplianceExecutionSummaryOutputTypeDef(BaseValidatorModel):
    ExecutionTime: datetime
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None


class ComplianceItemEntryTypeDef(BaseValidatorModel):
    Severity: ComplianceSeverityType
    Status: ComplianceStatusType
    Id: Optional[str] = None
    Title: Optional[str] = None
    Details: Optional[Mapping[str, str]] = None


class SeveritySummaryTypeDef(BaseValidatorModel):
    CriticalCount: Optional[int] = None
    HighCount: Optional[int] = None
    MediumCount: Optional[int] = None
    LowCount: Optional[int] = None
    InformationalCount: Optional[int] = None
    UnspecifiedCount: Optional[int] = None


class RegistrationMetadataItemTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class DocumentRequiresTypeDef(BaseValidatorModel):
    Name: str
    Version: Optional[str] = None
    RequireType: Optional[str] = None
    VersionName: Optional[str] = None


class OpsItemNotificationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class RelatedOpsItemTypeDef(BaseValidatorModel):
    OpsItemId: str


class MetadataValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None


class DeleteActivationRequestTypeDef(BaseValidatorModel):
    ActivationId: str


class DeleteAssociationRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None


class DeleteDocumentRequestTypeDef(BaseValidatorModel):
    Name: str
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None
    Force: Optional[bool] = None


class DeleteInventoryRequestTypeDef(BaseValidatorModel):
    TypeName: str
    SchemaDeleteOption: Optional[InventorySchemaDeleteOptionType] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


class DeleteMaintenanceWindowRequestTypeDef(BaseValidatorModel):
    WindowId: str


class DeleteOpsItemRequestTypeDef(BaseValidatorModel):
    OpsItemId: str


class DeleteOpsMetadataRequestTypeDef(BaseValidatorModel):
    OpsMetadataArn: str


class DeleteParameterRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteParametersRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]


class DeletePatchBaselineRequestTypeDef(BaseValidatorModel):
    BaselineId: str


class DeleteResourceDataSyncRequestTypeDef(BaseValidatorModel):
    SyncName: str
    SyncType: Optional[str] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    PolicyId: str
    PolicyHash: str


class DeregisterManagedInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class DeregisterPatchBaselineForPatchGroupRequestTypeDef(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str


class DeregisterTargetFromMaintenanceWindowRequestTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    Safe: Optional[bool] = None


class DeregisterTaskFromMaintenanceWindowRequestTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str


class DescribeActivationsFilterTypeDef(BaseValidatorModel):
    FilterKey: Optional[DescribeActivationsFilterKeysType] = None
    FilterValues: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAssociationRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    InstanceId: Optional[str] = None
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None


class StepExecutionFilterTypeDef(BaseValidatorModel):
    Key: StepExecutionFilterKeyType
    Values: Sequence[str]


class PatchOrchestratorFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class PatchTypeDef(BaseValidatorModel):
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


class DescribeDocumentPermissionRequestTypeDef(BaseValidatorModel):
    Name: str
    PermissionType: Literal["Share"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDocumentRequestTypeDef(BaseValidatorModel):
    Name: str
    DocumentVersion: Optional[str] = None
    VersionName: Optional[str] = None


class DescribeEffectiveInstanceAssociationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstanceAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    InstanceId: Optional[str] = None
    Content: Optional[str] = None
    AssociationVersion: Optional[str] = None


class DescribeEffectivePatchesForPatchBaselineRequestTypeDef(BaseValidatorModel):
    BaselineId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceAssociationsStatusRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstanceInformationFilterTypeDef(BaseValidatorModel):
    key: InstanceInformationFilterKeyType
    valueSet: Sequence[str]


class InstanceInformationStringFilterTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class InstancePatchStateTypeDef(BaseValidatorModel):
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


class DescribeInstancePatchStatesRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PatchComplianceDataTypeDef(BaseValidatorModel):
    Title: str
    KBId: str
    Classification: str
    Severity: str
    State: PatchComplianceDataStateType
    InstalledTime: datetime
    CVEIds: Optional[str] = None


class InstancePropertyFilterTypeDef(BaseValidatorModel):
    key: InstancePropertyFilterKeyType
    valueSet: Sequence[str]


class InstancePropertyStringFilterTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]
    Operator: Optional[InstancePropertyFilterOperatorType] = None


class DescribeInventoryDeletionsRequestTypeDef(BaseValidatorModel):
    DeletionId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MaintenanceWindowFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class MaintenanceWindowExecutionTaskInvocationIdentityTypeDef(BaseValidatorModel):
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


class MaintenanceWindowExecutionTypeDef(BaseValidatorModel):
    WindowId: Optional[str] = None
    WindowExecutionId: Optional[str] = None
    Status: Optional[MaintenanceWindowExecutionStatusType] = None
    StatusDetails: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ScheduledWindowExecutionTypeDef(BaseValidatorModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None
    ExecutionTime: Optional[str] = None


class MaintenanceWindowIdentityForTargetTypeDef(BaseValidatorModel):
    WindowId: Optional[str] = None
    Name: Optional[str] = None


class MaintenanceWindowIdentityTypeDef(BaseValidatorModel):
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


class OpsItemFilterTypeDef(BaseValidatorModel):
    Key: OpsItemFilterKeyType
    Values: Sequence[str]
    Operator: OpsItemFilterOperatorType


class ParameterStringFilterTypeDef(BaseValidatorModel):
    Key: str
    Option: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class ParametersFilterTypeDef(BaseValidatorModel):
    Key: ParametersFilterKeyType
    Values: Sequence[str]


class PatchBaselineIdentityTypeDef(BaseValidatorModel):
    BaselineId: Optional[str] = None
    BaselineName: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemType] = None
    BaselineDescription: Optional[str] = None
    DefaultBaseline: Optional[bool] = None


class DescribePatchGroupStateRequestTypeDef(BaseValidatorModel):
    PatchGroup: str


class DescribePatchPropertiesRequestTypeDef(BaseValidatorModel):
    OperatingSystem: OperatingSystemType
    Property: PatchPropertyType
    PatchSet: Optional[PatchSetType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SessionFilterTypeDef(BaseValidatorModel):
    key: SessionFilterKeyType
    value: str


class DisassociateOpsItemRelatedItemRequestTypeDef(BaseValidatorModel):
    OpsItemId: str
    AssociationId: str


class DocumentDefaultVersionDescriptionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultVersion: Optional[str] = None
    DefaultVersionName: Optional[str] = None


class ReviewInformationTypeDef(BaseValidatorModel):
    ReviewedTime: Optional[datetime] = None
    Status: Optional[ReviewStatusType] = None
    Reviewer: Optional[str] = None


class DocumentFilterTypeDef(BaseValidatorModel):
    key: DocumentFilterKeyType
    value: str


class DocumentKeyValuesFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class DocumentVersionInfoTypeDef(BaseValidatorModel):
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


class PatchStatusTypeDef(BaseValidatorModel):
    DeploymentStatus: Optional[PatchDeploymentStatusType] = None
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovalDate: Optional[datetime] = None


class FailureDetailsTypeDef(BaseValidatorModel):
    FailureStage: Optional[str] = None
    FailureType: Optional[str] = None
    Details: Optional[Dict[str, List[str]]] = None


class GetAutomationExecutionRequestTypeDef(BaseValidatorModel):
    AutomationExecutionId: str


class GetCalendarStateRequestTypeDef(BaseValidatorModel):
    CalendarNames: Sequence[str]
    AtTime: Optional[str] = None


class GetCommandInvocationRequestTypeDef(BaseValidatorModel):
    CommandId: str
    InstanceId: str
    PluginName: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetConnectionStatusRequestTypeDef(BaseValidatorModel):
    Target: str


class GetDefaultPatchBaselineRequestTypeDef(BaseValidatorModel):
    OperatingSystem: Optional[OperatingSystemType] = None


class GetDocumentRequestTypeDef(BaseValidatorModel):
    Name: str
    VersionName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None


class GetExecutionPreviewRequestTypeDef(BaseValidatorModel):
    ExecutionPreviewId: str


class ResultAttributeTypeDef(BaseValidatorModel):
    TypeName: str


class GetInventorySchemaRequestTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Aggregator: Optional[bool] = None
    SubType: Optional[bool] = None


class GetMaintenanceWindowExecutionRequestTypeDef(BaseValidatorModel):
    WindowExecutionId: str


class GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str
    InvocationId: str


class GetMaintenanceWindowExecutionTaskRequestTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str


class MaintenanceWindowTaskParameterValueExpressionOutputTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None


class GetMaintenanceWindowRequestTypeDef(BaseValidatorModel):
    WindowId: str


class GetMaintenanceWindowTaskRequestTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str


class LoggingInfoTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3Region: str
    S3KeyPrefix: Optional[str] = None


class GetOpsItemRequestTypeDef(BaseValidatorModel):
    OpsItemId: str
    OpsItemArn: Optional[str] = None


class GetOpsMetadataRequestTypeDef(BaseValidatorModel):
    OpsMetadataArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class OpsResultAttributeTypeDef(BaseValidatorModel):
    TypeName: str


class GetParameterHistoryRequestTypeDef(BaseValidatorModel):
    Name: str
    WithDecryption: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetParameterRequestTypeDef(BaseValidatorModel):
    Name: str
    WithDecryption: Optional[bool] = None


class GetParametersRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]
    WithDecryption: Optional[bool] = None


class GetPatchBaselineForPatchGroupRequestTypeDef(BaseValidatorModel):
    PatchGroup: str
    OperatingSystem: Optional[OperatingSystemType] = None


class GetPatchBaselineRequestTypeDef(BaseValidatorModel):
    BaselineId: str


class PatchSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Products: List[str]
    Configuration: str


class GetResourcePoliciesRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetResourcePoliciesResponseEntryTypeDef(BaseValidatorModel):
    PolicyId: Optional[str] = None
    PolicyHash: Optional[str] = None
    Policy: Optional[str] = None


class GetServiceSettingRequestTypeDef(BaseValidatorModel):
    SettingId: str


class ServiceSettingTypeDef(BaseValidatorModel):
    SettingId: Optional[str] = None
    SettingValue: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    ARN: Optional[str] = None
    Status: Optional[str] = None


class InstanceAggregatedAssociationOverviewTypeDef(BaseValidatorModel):
    DetailedStatus: Optional[str] = None
    InstanceAssociationStatusAggregatedCount: Optional[Dict[str, int]] = None


class S3OutputLocationTypeDef(BaseValidatorModel):
    OutputS3Region: Optional[str] = None
    OutputS3BucketName: Optional[str] = None
    OutputS3KeyPrefix: Optional[str] = None


class S3OutputUrlTypeDef(BaseValidatorModel):
    OutputUrl: Optional[str] = None


class InstanceInfoTypeDef(BaseValidatorModel):
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


class InventoryDeletionSummaryItemTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    Count: Optional[int] = None
    RemainingCount: Optional[int] = None


class InventoryItemAttributeTypeDef(BaseValidatorModel):
    Name: str
    DataType: InventoryAttributeDataTypeType


class InventoryItemTypeDef(BaseValidatorModel):
    TypeName: str
    SchemaVersion: str
    CaptureTime: str
    ContentHash: Optional[str] = None
    Content: Optional[Sequence[Mapping[str, str]]] = None
    Context: Optional[Mapping[str, str]] = None


class InventoryResultItemTypeDef(BaseValidatorModel):
    TypeName: str
    SchemaVersion: str
    Content: List[Dict[str, str]]
    CaptureTime: Optional[str] = None
    ContentHash: Optional[str] = None


class LabelParameterVersionRequestTypeDef(BaseValidatorModel):
    Name: str
    Labels: Sequence[str]
    ParameterVersion: Optional[int] = None


class ListAssociationVersionsRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDocumentMetadataHistoryRequestTypeDef(BaseValidatorModel):
    Name: str
    Metadata: Literal["DocumentReviews"]
    DocumentVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDocumentVersionsRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NodeAggregatorPaginatorTypeDef(BaseValidatorModel):
    AggregatorType: Literal["Count"]
    TypeName: Literal["Instance"]
    AttributeName: NodeAttributeNameType
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class NodeAggregatorTypeDef(BaseValidatorModel):
    AggregatorType: Literal["Count"]
    TypeName: Literal["Instance"]
    AttributeName: NodeAttributeNameType
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class OpsItemEventFilterTypeDef(BaseValidatorModel):
    Key: Literal["OpsItemId"]
    Values: Sequence[str]
    Operator: Literal["Equal"]


class OpsItemRelatedItemsFilterTypeDef(BaseValidatorModel):
    Key: OpsItemRelatedItemsFilterKeyType
    Values: Sequence[str]
    Operator: Literal["Equal"]


class OpsMetadataFilterTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class OpsMetadataTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    OpsMetadataArn: Optional[str] = None
    LastModifiedDate: Optional[datetime] = None
    LastModifiedUser: Optional[str] = None
    CreationDate: Optional[datetime] = None


class ListResourceDataSyncRequestTypeDef(BaseValidatorModel):
    SyncType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str


class MaintenanceWindowAutomationParametersOutputTypeDef(BaseValidatorModel):
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None


class MaintenanceWindowAutomationParametersTypeDef(BaseValidatorModel):
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None


class MaintenanceWindowLambdaParametersOutputTypeDef(BaseValidatorModel):
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[bytes] = None


class NotificationConfigTypeDef(BaseValidatorModel):
    NotificationArn: Optional[str] = None
    NotificationEvents: Optional[Sequence[NotificationEventType]] = None
    NotificationType: Optional[NotificationTypeType] = None


class MaintenanceWindowStepFunctionsParametersTypeDef(BaseValidatorModel):
    Input: Optional[str] = None
    Name: Optional[str] = None


class MaintenanceWindowTaskParameterValueExpressionTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None


class ModifyDocumentPermissionRequestTypeDef(BaseValidatorModel):
    Name: str
    PermissionType: Literal["Share"]
    AccountIdsToAdd: Optional[Sequence[str]] = None
    AccountIdsToRemove: Optional[Sequence[str]] = None
    SharedDocumentVersion: Optional[str] = None


class NodeOwnerInfoTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    OrganizationalUnitPath: Optional[str] = None


class OpsEntityItemTypeDef(BaseValidatorModel):
    CaptureTime: Optional[str] = None
    Content: Optional[List[Dict[str, str]]] = None


class OpsItemIdentityTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class ParameterInlinePolicyTypeDef(BaseValidatorModel):
    PolicyText: Optional[str] = None
    PolicyType: Optional[str] = None
    PolicyStatus: Optional[str] = None


class ParentStepDetailsTypeDef(BaseValidatorModel):
    StepExecutionId: Optional[str] = None
    StepName: Optional[str] = None
    Action: Optional[str] = None
    Iteration: Optional[int] = None
    IteratorValue: Optional[str] = None


class PatchFilterOutputTypeDef(BaseValidatorModel):
    Key: PatchFilterKeyType
    Values: List[str]


class PatchFilterTypeDef(BaseValidatorModel):
    Key: PatchFilterKeyType
    Values: Sequence[str]


class PatchSourceTypeDef(BaseValidatorModel):
    Name: str
    Products: Sequence[str]
    Configuration: str


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    PolicyId: Optional[str] = None
    PolicyHash: Optional[str] = None


class RegisterDefaultPatchBaselineRequestTypeDef(BaseValidatorModel):
    BaselineId: str


class RegisterPatchBaselineForPatchGroupRequestTypeDef(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str


class RemoveTagsFromResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str
    TagKeys: Sequence[str]


class ResetServiceSettingRequestTypeDef(BaseValidatorModel):
    SettingId: str


class ResourceDataSyncOrganizationalUnitTypeDef(BaseValidatorModel):
    OrganizationalUnitId: Optional[str] = None


class ResourceDataSyncDestinationDataSharingTypeDef(BaseValidatorModel):
    DestinationDataSharingType: Optional[str] = None


class ResumeSessionRequestTypeDef(BaseValidatorModel):
    SessionId: str


class SendAutomationSignalRequestTypeDef(BaseValidatorModel):
    AutomationExecutionId: str
    SignalType: SignalTypeType
    Payload: Optional[Mapping[str, Sequence[str]]] = None


class SessionManagerOutputUrlTypeDef(BaseValidatorModel):
    S3OutputUrl: Optional[str] = None
    CloudWatchOutputUrl: Optional[str] = None


class StartAssociationsOnceRequestTypeDef(BaseValidatorModel):
    AssociationIds: Sequence[str]


class StartSessionRequestTypeDef(BaseValidatorModel):
    Target: str
    DocumentName: Optional[str] = None
    Reason: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None


class TargetTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class TerminateSessionRequestTypeDef(BaseValidatorModel):
    SessionId: str


class UnlabelParameterVersionRequestTypeDef(BaseValidatorModel):
    Name: str
    ParameterVersion: int
    Labels: Sequence[str]


class UpdateDocumentDefaultVersionRequestTypeDef(BaseValidatorModel):
    Name: str
    DocumentVersion: str


class UpdateMaintenanceWindowRequestTypeDef(BaseValidatorModel):
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


class UpdateManagedInstanceRoleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IamRole: str


class UpdateServiceSettingRequestTypeDef(BaseValidatorModel):
    SettingId: str
    SettingValue: str


class ActivationTypeDef(BaseValidatorModel):
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


class AddTagsToResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeForTaggingType
    ResourceId: str
    Tags: Sequence[TagTypeDef]


class CreateMaintenanceWindowRequestTypeDef(BaseValidatorModel):
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


class AlarmConfigurationOutputTypeDef(BaseValidatorModel):
    Alarms: List[AlarmTypeDef]
    IgnorePollAlarmFailure: Optional[bool] = None


class AlarmConfigurationTypeDef(BaseValidatorModel):
    Alarms: Sequence[AlarmTypeDef]
    IgnorePollAlarmFailure: Optional[bool] = None


class AssociateOpsItemRelatedItemResponseTypeDef(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelMaintenanceWindowExecutionResultTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateActivationResultTypeDef(BaseValidatorModel):
    ActivationId: str
    ActivationCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMaintenanceWindowResultTypeDef(BaseValidatorModel):
    WindowId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOpsItemResponseTypeDef(BaseValidatorModel):
    OpsItemId: str
    OpsItemArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOpsMetadataResultTypeDef(BaseValidatorModel):
    OpsMetadataArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePatchBaselineResultTypeDef(BaseValidatorModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMaintenanceWindowResultTypeDef(BaseValidatorModel):
    WindowId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteParametersResultTypeDef(BaseValidatorModel):
    DeletedParameters: List[str]
    InvalidParameters: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePatchBaselineResultTypeDef(BaseValidatorModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterPatchBaselineForPatchGroupResultTypeDef(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterTargetFromMaintenanceWindowResultTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterTaskFromMaintenanceWindowResultTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDocumentPermissionResponseTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    AccountSharingInfoList: List[AccountSharingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribePatchGroupStateResultTypeDef(BaseValidatorModel):
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


class DescribePatchPropertiesResultTypeDef(BaseValidatorModel):
    Properties: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetCalendarStateResponseTypeDef(BaseValidatorModel):
    State: CalendarStateType
    AtTime: str
    NextTransitionTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetConnectionStatusResponseTypeDef(BaseValidatorModel):
    Target: str
    Status: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetDefaultPatchBaselineResultTypeDef(BaseValidatorModel):
    BaselineId: str
    OperatingSystem: OperatingSystemType
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeployablePatchSnapshotForInstanceResultTypeDef(BaseValidatorModel):
    InstanceId: str
    SnapshotId: str
    SnapshotDownloadUrl: str
    Product: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMaintenanceWindowExecutionResultTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    TaskIds: List[str]
    Status: MaintenanceWindowExecutionStatusType
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetMaintenanceWindowExecutionTaskInvocationResultTypeDef(BaseValidatorModel):
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


class GetMaintenanceWindowResultTypeDef(BaseValidatorModel):
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


class GetPatchBaselineForPatchGroupResultTypeDef(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str
    OperatingSystem: OperatingSystemType
    ResponseMetadata: ResponseMetadataTypeDef


class LabelParameterVersionResultTypeDef(BaseValidatorModel):
    InvalidLabels: List[str]
    ParameterVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListInventoryEntriesResultTypeDef(BaseValidatorModel):
    TypeName: str
    InstanceId: str
    SchemaVersion: str
    CaptureTime: str
    Entries: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListNodesSummaryResultTypeDef(BaseValidatorModel):
    Summary: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutInventoryResultTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutParameterResultTypeDef(BaseValidatorModel):
    Version: int
    Tier: ParameterTierType
    ResponseMetadata: ResponseMetadataTypeDef


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyId: str
    PolicyHash: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterDefaultPatchBaselineResultTypeDef(BaseValidatorModel):
    BaselineId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterPatchBaselineForPatchGroupResultTypeDef(BaseValidatorModel):
    BaselineId: str
    PatchGroup: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterTargetWithMaintenanceWindowResultTypeDef(BaseValidatorModel):
    WindowTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterTaskWithMaintenanceWindowResultTypeDef(BaseValidatorModel):
    WindowTaskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResumeSessionResponseTypeDef(BaseValidatorModel):
    SessionId: str
    TokenValue: str
    StreamUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartAutomationExecutionResultTypeDef(BaseValidatorModel):
    AutomationExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartChangeRequestExecutionResultTypeDef(BaseValidatorModel):
    AutomationExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartExecutionPreviewResponseTypeDef(BaseValidatorModel):
    ExecutionPreviewId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartSessionResponseTypeDef(BaseValidatorModel):
    SessionId: str
    TokenValue: str
    StreamUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class TerminateSessionResponseTypeDef(BaseValidatorModel):
    SessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UnlabelParameterVersionResultTypeDef(BaseValidatorModel):
    RemovedLabels: List[str]
    InvalidLabels: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMaintenanceWindowResultTypeDef(BaseValidatorModel):
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


class UpdateOpsMetadataResultTypeDef(BaseValidatorModel):
    OpsMetadataArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociationTypeDef(BaseValidatorModel):
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


class MaintenanceWindowTargetTypeDef(BaseValidatorModel):
    WindowId: Optional[str] = None
    WindowTargetId: Optional[str] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateMaintenanceWindowTargetResultTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    Targets: List[TargetOutputTypeDef]
    OwnerInformation: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociationExecutionFilterTypeDef(BaseValidatorModel):
    pass


class DescribeAssociationExecutionsRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    Filters: Optional[Sequence[AssociationExecutionFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AssociationExecutionTargetTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    AssociationVersion: Optional[str] = None
    ExecutionId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Status: Optional[str] = None
    DetailedStatus: Optional[str] = None
    LastExecutionDate: Optional[datetime] = None
    OutputSource: Optional[OutputSourceTypeDef] = None


class DescribeAssociationExecutionTargetsRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    ExecutionId: str
    Filters: Optional[Sequence[AssociationExecutionTargetsFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAssociationsRequestTypeDef(BaseValidatorModel):
    AssociationFilterList: Optional[Sequence[AssociationFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class AssociationStatusTypeDef(BaseValidatorModel):
    Date: TimestampTypeDef
    Name: AssociationStatusNameType
    Message: str
    AdditionalInfo: Optional[str] = None


class ComplianceExecutionSummaryTypeDef(BaseValidatorModel):
    ExecutionTime: TimestampTypeDef
    ExecutionId: Optional[str] = None
    ExecutionType: Optional[str] = None


class UpdateDocumentRequestTypeDef(BaseValidatorModel):
    Content: str
    Name: str
    Attachments: Optional[Sequence[AttachmentsSourceTypeDef]] = None
    DisplayName: Optional[str] = None
    VersionName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    DocumentFormat: Optional[DocumentFormatType] = None
    TargetType: Optional[str] = None


class DescribeAutomationExecutionsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[AutomationExecutionFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class AutomationExecutionPreviewTypeDef(BaseValidatorModel):
    StepPreviews: Optional[Dict[ImpactTypeType, int]] = None
    Regions: Optional[List[str]] = None
    TargetPreviews: Optional[List[TargetPreviewTypeDef]] = None
    TotalAccounts: Optional[int] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class MaintenanceWindowLambdaParametersTypeDef(BaseValidatorModel):
    ClientContext: Optional[str] = None
    Qualifier: Optional[str] = None
    Payload: Optional[BlobTypeDef] = None


class GetCommandInvocationResultTypeDef(BaseValidatorModel):
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


class ListCommandInvocationsRequestTypeDef(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None
    Details: Optional[bool] = None


class ListCommandsRequestTypeDef(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None


class CommandInvocationTypeDef(BaseValidatorModel):
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


class MaintenanceWindowRunCommandParametersOutputTypeDef(BaseValidatorModel):
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


class ComplianceItemTypeDef(BaseValidatorModel):
    ComplianceType: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Id: Optional[str] = None
    Title: Optional[str] = None
    Status: Optional[ComplianceStatusType] = None
    Severity: Optional[ComplianceSeverityType] = None
    ExecutionSummary: Optional[ComplianceExecutionSummaryOutputTypeDef] = None
    Details: Optional[Dict[str, str]] = None


class ComplianceStringFilterTypeDef(BaseValidatorModel):
    pass


class ListComplianceItemsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    ResourceIds: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListComplianceSummariesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListResourceComplianceSummariesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class CompliantSummaryTypeDef(BaseValidatorModel):
    CompliantCount: Optional[int] = None
    SeveritySummary: Optional[SeveritySummaryTypeDef] = None


class NonCompliantSummaryTypeDef(BaseValidatorModel):
    NonCompliantCount: Optional[int] = None
    SeveritySummary: Optional[SeveritySummaryTypeDef] = None


class CreateActivationRequestTypeDef(BaseValidatorModel):
    IamRole: str
    Description: Optional[str] = None
    DefaultInstanceName: Optional[str] = None
    RegistrationLimit: Optional[int] = None
    ExpirationDate: Optional[TimestampTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    RegistrationMetadata: Optional[Sequence[RegistrationMetadataItemTypeDef]] = None


class CreateDocumentRequestTypeDef(BaseValidatorModel):
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


class DocumentIdentifierTypeDef(BaseValidatorModel):
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


class GetDocumentResultTypeDef(BaseValidatorModel):
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


class OpsItemDataValueTypeDef(BaseValidatorModel):
    pass


class OpsItemSummaryTypeDef(BaseValidatorModel):
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


class CreateOpsItemRequestTypeDef(BaseValidatorModel):
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


class OpsItemTypeDef(BaseValidatorModel):
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


class UpdateOpsItemRequestTypeDef(BaseValidatorModel):
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


class CreateOpsMetadataRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Metadata: Optional[Mapping[str, MetadataValueTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class GetOpsMetadataResultTypeDef(BaseValidatorModel):
    ResourceId: str
    Metadata: Dict[str, MetadataValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateOpsMetadataRequestTypeDef(BaseValidatorModel):
    OpsMetadataArn: str
    MetadataToUpdate: Optional[Mapping[str, MetadataValueTypeDef]] = None
    KeysToDelete: Optional[Sequence[str]] = None


class DescribeActivationsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[DescribeActivationsFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeActivationsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[DescribeActivationsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAssociationExecutionTargetsRequestPaginateTypeDef(BaseValidatorModel):
    AssociationId: str
    ExecutionId: str
    Filters: Optional[Sequence[AssociationExecutionTargetsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAssociationExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    AssociationId: str
    Filters: Optional[Sequence[AssociationExecutionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAutomationExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[AutomationExecutionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef(BaseValidatorModel):
    BaselineId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstanceAssociationsStatusRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstancePatchStatesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInventoryDeletionsRequestPaginateTypeDef(BaseValidatorModel):
    DeletionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePatchPropertiesRequestPaginateTypeDef(BaseValidatorModel):
    OperatingSystem: OperatingSystemType
    Property: PatchPropertyType
    PatchSet: Optional[PatchSetType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetInventorySchemaRequestPaginateTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    Aggregator: Optional[bool] = None
    SubType: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetParameterHistoryRequestPaginateTypeDef(BaseValidatorModel):
    Name: str
    WithDecryption: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourcePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociationVersionsRequestPaginateTypeDef(BaseValidatorModel):
    AssociationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    AssociationFilterList: Optional[Sequence[AssociationFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCommandInvocationsRequestPaginateTypeDef(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None
    Details: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCommandsRequestPaginateTypeDef(BaseValidatorModel):
    CommandId: Optional[str] = None
    InstanceId: Optional[str] = None
    Filters: Optional[Sequence[CommandFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComplianceItemsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    ResourceIds: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComplianceSummariesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDocumentVersionsRequestPaginateTypeDef(BaseValidatorModel):
    Name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceComplianceSummariesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ComplianceStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceDataSyncRequestPaginateTypeDef(BaseValidatorModel):
    SyncType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAutomationStepExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    AutomationExecutionId: str
    Filters: Optional[Sequence[StepExecutionFilterTypeDef]] = None
    ReverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAutomationStepExecutionsRequestTypeDef(BaseValidatorModel):
    AutomationExecutionId: str
    Filters: Optional[Sequence[StepExecutionFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ReverseOrder: Optional[bool] = None


class DescribeAvailablePatchesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAvailablePatchesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstancePatchesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstancePatchesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribePatchBaselinesRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePatchBaselinesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePatchGroupsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePatchGroupsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    NextToken: Optional[str] = None


class DescribeAvailablePatchesResultTypeDef(BaseValidatorModel):
    Patches: List[PatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeEffectiveInstanceAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[InstanceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInstanceInformationRequestPaginateTypeDef(BaseValidatorModel):
    InstanceInformationFilterList: Optional[Sequence[InstanceInformationFilterTypeDef]] = None
    Filters: Optional[Sequence[InstanceInformationStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstanceInformationRequestTypeDef(BaseValidatorModel):
    InstanceInformationFilterList: Optional[Sequence[InstanceInformationFilterTypeDef]] = None
    Filters: Optional[Sequence[InstanceInformationStringFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstancePatchStateFilterTypeDef(BaseValidatorModel):
    pass


class DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef(BaseValidatorModel):
    PatchGroup: str
    Filters: Optional[Sequence[InstancePatchStateFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstancePatchStatesForPatchGroupRequestTypeDef(BaseValidatorModel):
    PatchGroup: str
    Filters: Optional[Sequence[InstancePatchStateFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInstancePatchStatesForPatchGroupResultTypeDef(BaseValidatorModel):
    InstancePatchStates: List[InstancePatchStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInstancePatchStatesResultTypeDef(BaseValidatorModel):
    InstancePatchStates: List[InstancePatchStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInstancePatchesResultTypeDef(BaseValidatorModel):
    Patches: List[PatchComplianceDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInstancePropertiesRequestPaginateTypeDef(BaseValidatorModel):
    InstancePropertyFilterList: Optional[Sequence[InstancePropertyFilterTypeDef]] = None
    FiltersWithOperator: Optional[Sequence[InstancePropertyStringFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeInstancePropertiesRequestTypeDef(BaseValidatorModel):
    InstancePropertyFilterList: Optional[Sequence[InstancePropertyFilterTypeDef]] = None
    FiltersWithOperator: Optional[Sequence[InstancePropertyStringFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    TaskId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowExecutionTasksRequestTypeDef(BaseValidatorModel):
    WindowExecutionId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowExecutionsRequestTypeDef(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowTargetsRequestPaginateTypeDef(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowTargetsRequestTypeDef(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowTasksRequestPaginateTypeDef(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowTasksRequestTypeDef(BaseValidatorModel):
    WindowId: str
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[MaintenanceWindowFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef(BaseValidatorModel):
    WindowExecutionTaskInvocationIdentities: List[ MaintenanceWindowExecutionTaskInvocationIdentityTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowExecutionsResultTypeDef(BaseValidatorModel):
    WindowExecutions: List[MaintenanceWindowExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowScheduleResultTypeDef(BaseValidatorModel):
    ScheduledWindowExecutions: List[ScheduledWindowExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsForTargetResultTypeDef(BaseValidatorModel):
    WindowIdentities: List[MaintenanceWindowIdentityForTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsResultTypeDef(BaseValidatorModel):
    WindowIdentities: List[MaintenanceWindowIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeOpsItemsRequestPaginateTypeDef(BaseValidatorModel):
    OpsItemFilters: Optional[Sequence[OpsItemFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOpsItemsRequestTypeDef(BaseValidatorModel):
    OpsItemFilters: Optional[Sequence[OpsItemFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetParametersByPathRequestPaginateTypeDef(BaseValidatorModel):
    Path: str
    Recursive: Optional[bool] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    WithDecryption: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetParametersByPathRequestTypeDef(BaseValidatorModel):
    Path: str
    Recursive: Optional[bool] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    WithDecryption: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeParametersRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ParametersFilterTypeDef]] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    Shared: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeParametersRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ParametersFilterTypeDef]] = None
    ParameterFilters: Optional[Sequence[ParameterStringFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Shared: Optional[bool] = None


class DescribePatchBaselinesResultTypeDef(BaseValidatorModel):
    BaselineIdentities: List[PatchBaselineIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PatchGroupPatchBaselineMappingTypeDef(BaseValidatorModel):
    PatchGroup: Optional[str] = None
    BaselineIdentity: Optional[PatchBaselineIdentityTypeDef] = None


class DescribeSessionsRequestPaginateTypeDef(BaseValidatorModel):
    State: SessionStateType
    Filters: Optional[Sequence[SessionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSessionsRequestTypeDef(BaseValidatorModel):
    State: SessionStateType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[SessionFilterTypeDef]] = None


class UpdateDocumentDefaultVersionResultTypeDef(BaseValidatorModel):
    Description: DocumentDefaultVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DocumentParameterTypeDef(BaseValidatorModel):
    pass


class DocumentDescriptionTypeDef(BaseValidatorModel):
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


class ListDocumentsRequestPaginateTypeDef(BaseValidatorModel):
    DocumentFilterList: Optional[Sequence[DocumentFilterTypeDef]] = None
    Filters: Optional[Sequence[DocumentKeyValuesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDocumentsRequestTypeDef(BaseValidatorModel):
    DocumentFilterList: Optional[Sequence[DocumentFilterTypeDef]] = None
    Filters: Optional[Sequence[DocumentKeyValuesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DocumentReviewCommentSourceTypeDef(BaseValidatorModel):
    pass


class DocumentReviewerResponseSourceTypeDef(BaseValidatorModel):
    CreateTime: Optional[datetime] = None
    UpdatedTime: Optional[datetime] = None
    ReviewStatus: Optional[ReviewStatusType] = None
    Comment: Optional[List[DocumentReviewCommentSourceTypeDef]] = None
    Reviewer: Optional[str] = None


class DocumentReviewsTypeDef(BaseValidatorModel):
    Action: DocumentReviewActionType
    Comment: Optional[Sequence[DocumentReviewCommentSourceTypeDef]] = None


class ListDocumentVersionsResultTypeDef(BaseValidatorModel):
    DocumentVersions: List[DocumentVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EffectivePatchTypeDef(BaseValidatorModel):
    Patch: Optional[PatchTypeDef] = None
    PatchStatus: Optional[PatchStatusTypeDef] = None


class GetCommandInvocationRequestWaitTypeDef(BaseValidatorModel):
    CommandId: str
    InstanceId: str
    PluginName: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class InventoryFilterTypeDef(BaseValidatorModel):
    pass


class InventoryGroupTypeDef(BaseValidatorModel):
    Name: str
    Filters: Sequence[InventoryFilterTypeDef]


class ListInventoryEntriesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TypeName: str
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OpsFilterTypeDef(BaseValidatorModel):
    pass


class OpsAggregatorPaginatorTypeDef(BaseValidatorModel):
    AggregatorType: Optional[str] = None
    TypeName: Optional[str] = None
    AttributeName: Optional[str] = None
    Values: Optional[Mapping[str, str]] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class OpsAggregatorTypeDef(BaseValidatorModel):
    AggregatorType: Optional[str] = None
    TypeName: Optional[str] = None
    AttributeName: Optional[str] = None
    Values: Optional[Mapping[str, str]] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None


class ParameterTypeDef(BaseValidatorModel):
    pass


class GetParameterResultTypeDef(BaseValidatorModel):
    Parameter: ParameterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetParametersByPathResultTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetParametersResultTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    InvalidParameters: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePoliciesResponseTypeDef(BaseValidatorModel):
    Policies: List[GetResourcePoliciesResponseEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetServiceSettingResultTypeDef(BaseValidatorModel):
    ServiceSetting: ServiceSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResetServiceSettingResultTypeDef(BaseValidatorModel):
    ServiceSetting: ServiceSettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InstanceInformationTypeDef(BaseValidatorModel):
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


class InstancePropertyTypeDef(BaseValidatorModel):
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


class InstanceAssociationOutputLocationTypeDef(BaseValidatorModel):
    S3Location: Optional[S3OutputLocationTypeDef] = None


class InstanceAssociationOutputUrlTypeDef(BaseValidatorModel):
    S3OutputUrl: Optional[S3OutputUrlTypeDef] = None


class NodeTypeTypeDef(BaseValidatorModel):
    Instance: Optional[InstanceInfoTypeDef] = None


class InventoryDeletionSummaryTypeDef(BaseValidatorModel):
    TotalCount: Optional[int] = None
    RemainingCount: Optional[int] = None
    SummaryItems: Optional[List[InventoryDeletionSummaryItemTypeDef]] = None


class InventoryItemSchemaTypeDef(BaseValidatorModel):
    TypeName: str
    Attributes: List[InventoryItemAttributeTypeDef]
    Version: Optional[str] = None
    DisplayName: Optional[str] = None


class PutInventoryRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Items: Sequence[InventoryItemTypeDef]


class InventoryResultEntityTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Data: Optional[Dict[str, InventoryResultItemTypeDef]] = None


class NodeFilterTypeDef(BaseValidatorModel):
    pass


class ListNodesRequestPaginateTypeDef(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNodesRequestTypeDef(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListNodesSummaryRequestPaginateTypeDef(BaseValidatorModel):
    Aggregators: Sequence[NodeAggregatorPaginatorTypeDef]
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNodesSummaryRequestTypeDef(BaseValidatorModel):
    Aggregators: Sequence[NodeAggregatorTypeDef]
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[NodeFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOpsItemEventsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[OpsItemEventFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOpsItemEventsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[OpsItemEventFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOpsItemRelatedItemsRequestPaginateTypeDef(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    Filters: Optional[Sequence[OpsItemRelatedItemsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOpsItemRelatedItemsRequestTypeDef(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    Filters: Optional[Sequence[OpsItemRelatedItemsFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOpsMetadataRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[OpsMetadataFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOpsMetadataRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[OpsMetadataFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOpsMetadataResultTypeDef(BaseValidatorModel):
    OpsMetadataList: List[OpsMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MaintenanceWindowRunCommandParametersTypeDef(BaseValidatorModel):
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


class OpsEntityTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Data: Optional[Dict[str, OpsEntityItemTypeDef]] = None


class OpsItemEventSummaryTypeDef(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    EventId: Optional[str] = None
    Source: Optional[str] = None
    DetailType: Optional[str] = None
    Detail: Optional[str] = None
    CreatedBy: Optional[OpsItemIdentityTypeDef] = None
    CreatedTime: Optional[datetime] = None


class OpsItemRelatedItemSummaryTypeDef(BaseValidatorModel):
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ResourceType: Optional[str] = None
    AssociationType: Optional[str] = None
    ResourceUri: Optional[str] = None
    CreatedBy: Optional[OpsItemIdentityTypeDef] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedBy: Optional[OpsItemIdentityTypeDef] = None
    LastModifiedTime: Optional[datetime] = None


class PatchFilterGroupOutputTypeDef(BaseValidatorModel):
    PatchFilters: List[PatchFilterOutputTypeDef]


class ResourceDataSyncAwsOrganizationsSourceOutputTypeDef(BaseValidatorModel):
    OrganizationSourceType: str
    OrganizationalUnits: Optional[List[ResourceDataSyncOrganizationalUnitTypeDef]] = None


class ResourceDataSyncAwsOrganizationsSourceTypeDef(BaseValidatorModel):
    OrganizationSourceType: str
    OrganizationalUnits: Optional[Sequence[ResourceDataSyncOrganizationalUnitTypeDef]] = None


class ResourceDataSyncS3DestinationTypeDef(BaseValidatorModel):
    BucketName: str
    SyncFormat: Literal["JsonSerDe"]
    Region: str
    Prefix: Optional[str] = None
    AWSKMSKeyARN: Optional[str] = None
    DestinationDataSharing: Optional[ResourceDataSyncDestinationDataSharingTypeDef] = None


class SessionTypeDef(BaseValidatorModel):
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


class DescribeActivationsResultTypeDef(BaseValidatorModel):
    ActivationList: List[ActivationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociationExecutionTypeDef(BaseValidatorModel):
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


class CommandTypeDef(BaseValidatorModel):
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


class MaintenanceWindowExecutionTaskIdentityTypeDef(BaseValidatorModel):
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


class TargetLocationOutputTypeDef(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    Regions: Optional[List[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    IncludeChildOrganizationUnits: Optional[bool] = None
    ExcludeAccounts: Optional[List[str]] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TargetsMaxConcurrency: Optional[str] = None
    TargetsMaxErrors: Optional[str] = None


class ListAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowTargetsResultTypeDef(BaseValidatorModel):
    Targets: List[MaintenanceWindowTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeAssociationExecutionTargetsResultTypeDef(BaseValidatorModel):
    AssociationExecutionTargets: List[AssociationExecutionTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExecutionPreviewTypeDef(BaseValidatorModel):
    Automation: Optional[AutomationExecutionPreviewTypeDef] = None


class ListCommandInvocationsResultTypeDef(BaseValidatorModel):
    CommandInvocations: List[CommandInvocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MaintenanceWindowTaskInvocationParametersOutputTypeDef(BaseValidatorModel):
    RunCommand: Optional[MaintenanceWindowRunCommandParametersOutputTypeDef] = None
    Automation: Optional[MaintenanceWindowAutomationParametersOutputTypeDef] = None
    StepFunctions: Optional[MaintenanceWindowStepFunctionsParametersTypeDef] = None
    Lambda: Optional[MaintenanceWindowLambdaParametersOutputTypeDef] = None


class ListComplianceItemsResultTypeDef(BaseValidatorModel):
    ComplianceItems: List[ComplianceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ComplianceSummaryItemTypeDef(BaseValidatorModel):
    ComplianceType: Optional[str] = None
    CompliantSummary: Optional[CompliantSummaryTypeDef] = None
    NonCompliantSummary: Optional[NonCompliantSummaryTypeDef] = None


class ResourceComplianceSummaryItemTypeDef(BaseValidatorModel):
    ComplianceType: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Status: Optional[ComplianceStatusType] = None
    OverallSeverity: Optional[ComplianceSeverityType] = None
    ExecutionSummary: Optional[ComplianceExecutionSummaryOutputTypeDef] = None
    CompliantSummary: Optional[CompliantSummaryTypeDef] = None
    NonCompliantSummary: Optional[NonCompliantSummaryTypeDef] = None


class ListDocumentsResultTypeDef(BaseValidatorModel):
    DocumentIdentifiers: List[DocumentIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeOpsItemsResponseTypeDef(BaseValidatorModel):
    OpsItemSummaries: List[OpsItemSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetOpsItemResponseTypeDef(BaseValidatorModel):
    OpsItem: OpsItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePatchGroupsResultTypeDef(BaseValidatorModel):
    Mappings: List[PatchGroupPatchBaselineMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateDocumentResultTypeDef(BaseValidatorModel):
    DocumentDescription: DocumentDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDocumentResultTypeDef(BaseValidatorModel):
    Document: DocumentDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDocumentResultTypeDef(BaseValidatorModel):
    DocumentDescription: DocumentDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DocumentMetadataResponseInfoTypeDef(BaseValidatorModel):
    ReviewerResponse: Optional[List[DocumentReviewerResponseSourceTypeDef]] = None


class UpdateDocumentMetadataRequestTypeDef(BaseValidatorModel):
    Name: str
    DocumentReviews: DocumentReviewsTypeDef
    DocumentVersion: Optional[str] = None


class DescribeEffectivePatchesForPatchBaselineResultTypeDef(BaseValidatorModel):
    EffectivePatches: List[EffectivePatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InventoryAggregatorPaginatorTypeDef(BaseValidatorModel):
    Expression: Optional[str] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None
    Groups: Optional[Sequence[InventoryGroupTypeDef]] = None


class InventoryAggregatorTypeDef(BaseValidatorModel):
    Expression: Optional[str] = None
    Aggregators: Optional[Sequence[Mapping[str, Any]]] = None
    Groups: Optional[Sequence[InventoryGroupTypeDef]] = None


class GetOpsSummaryRequestPaginateTypeDef(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence[OpsAggregatorPaginatorTypeDef]] = None
    ResultAttributes: Optional[Sequence[OpsResultAttributeTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetOpsSummaryRequestTypeDef(BaseValidatorModel):
    SyncName: Optional[str] = None
    Filters: Optional[Sequence[OpsFilterTypeDef]] = None
    Aggregators: Optional[Sequence[OpsAggregatorTypeDef]] = None
    ResultAttributes: Optional[Sequence[OpsResultAttributeTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInstanceInformationResultTypeDef(BaseValidatorModel):
    InstanceInformationList: List[InstanceInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInstancePropertiesResultTypeDef(BaseValidatorModel):
    InstanceProperties: List[InstancePropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InstanceAssociationStatusInfoTypeDef(BaseValidatorModel):
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


class NodeTypeDef(BaseValidatorModel):
    CaptureTime: Optional[datetime] = None
    Id: Optional[str] = None
    Owner: Optional[NodeOwnerInfoTypeDef] = None
    Region: Optional[str] = None
    NodeType: Optional[NodeTypeTypeDef] = None


class DeleteInventoryResultTypeDef(BaseValidatorModel):
    DeletionId: str
    TypeName: str
    DeletionSummary: InventoryDeletionSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InventoryDeletionStatusItemTypeDef(BaseValidatorModel):
    DeletionId: Optional[str] = None
    TypeName: Optional[str] = None
    DeletionStartTime: Optional[datetime] = None
    LastStatus: Optional[InventoryDeletionStatusType] = None
    LastStatusMessage: Optional[str] = None
    DeletionSummary: Optional[InventoryDeletionSummaryTypeDef] = None
    LastStatusUpdateTime: Optional[datetime] = None


class GetInventorySchemaResultTypeDef(BaseValidatorModel):
    Schemas: List[InventoryItemSchemaTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetInventoryResultTypeDef(BaseValidatorModel):
    Entities: List[InventoryResultEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MaintenanceWindowTaskInvocationParametersTypeDef(BaseValidatorModel):
    RunCommand: Optional[MaintenanceWindowRunCommandParametersTypeDef] = None
    Automation: Optional[MaintenanceWindowAutomationParametersTypeDef] = None
    StepFunctions: Optional[MaintenanceWindowStepFunctionsParametersTypeDef] = None
    Lambda: Optional[MaintenanceWindowLambdaParametersTypeDef] = None


class GetOpsSummaryResultTypeDef(BaseValidatorModel):
    Entities: List[OpsEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListOpsItemEventsResponseTypeDef(BaseValidatorModel):
    Summaries: List[OpsItemEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListOpsItemRelatedItemsResponseTypeDef(BaseValidatorModel):
    Summaries: List[OpsItemRelatedItemSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ParameterHistoryTypeDef(BaseValidatorModel):
    pass


class GetParameterHistoryResultTypeDef(BaseValidatorModel):
    Parameters: List[ParameterHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ParameterMetadataTypeDef(BaseValidatorModel):
    pass


class DescribeParametersResultTypeDef(BaseValidatorModel):
    Parameters: List[ParameterMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PatchRuleOutputTypeDef(BaseValidatorModel):
    PatchFilterGroup: PatchFilterGroupOutputTypeDef
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApproveAfterDays: Optional[int] = None
    ApproveUntilDate: Optional[str] = None
    EnableNonSecurity: Optional[bool] = None


class PatchFilterUnionTypeDef(BaseValidatorModel):
    pass


class PatchFilterGroupTypeDef(BaseValidatorModel):
    PatchFilters: Sequence[PatchFilterUnionTypeDef]


class ResourceDataSyncSourceWithStateTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    AwsOrganizationsSource: Optional[ResourceDataSyncAwsOrganizationsSourceOutputTypeDef] = None
    SourceRegions: Optional[List[str]] = None
    IncludeFutureRegions: Optional[bool] = None
    State: Optional[str] = None
    EnableAllOpsDataSources: Optional[bool] = None


class DescribeSessionsResponseTypeDef(BaseValidatorModel):
    Sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TargetUnionTypeDef(BaseValidatorModel):
    pass


class DescribeMaintenanceWindowScheduleRequestPaginateTypeDef(BaseValidatorModel):
    WindowId: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowScheduleRequestTypeDef(BaseValidatorModel):
    WindowId: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ResourceType: Optional[MaintenanceWindowResourceTypeType] = None
    Filters: Optional[Sequence[PatchOrchestratorFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef(BaseValidatorModel):
    Targets: Sequence[TargetUnionTypeDef]
    ResourceType: MaintenanceWindowResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMaintenanceWindowsForTargetRequestTypeDef(BaseValidatorModel):
    Targets: Sequence[TargetUnionTypeDef]
    ResourceType: MaintenanceWindowResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RegisterTargetWithMaintenanceWindowRequestTypeDef(BaseValidatorModel):
    WindowId: str
    ResourceType: MaintenanceWindowResourceTypeType
    Targets: Sequence[TargetUnionTypeDef]
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdateMaintenanceWindowTargetRequestTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTargetId: str
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    OwnerInformation: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Replace: Optional[bool] = None


class DescribeAssociationExecutionsResultTypeDef(BaseValidatorModel):
    AssociationExecutions: List[AssociationExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCommandsResultTypeDef(BaseValidatorModel):
    Commands: List[CommandTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SendCommandResultTypeDef(BaseValidatorModel):
    Command: CommandTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMaintenanceWindowExecutionTasksResultTypeDef(BaseValidatorModel):
    WindowExecutionTaskIdentities: List[MaintenanceWindowExecutionTaskIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MaintenanceWindowTaskTypeDef(BaseValidatorModel):
    pass


class DescribeMaintenanceWindowTasksResultTypeDef(BaseValidatorModel):
    Tasks: List[MaintenanceWindowTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociationDescriptionTypeDef(BaseValidatorModel):
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


class AssociationVersionInfoTypeDef(BaseValidatorModel):
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


class CreateAssociationBatchRequestEntryOutputTypeDef(BaseValidatorModel):
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


class RunbookOutputTypeDef(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Dict[str, List[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[List[TargetOutputTypeDef]] = None
    TargetMaps: Optional[List[Dict[str, List[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[List[TargetLocationOutputTypeDef]] = None


class StepExecutionTypeDef(BaseValidatorModel):
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


class AlarmConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class NotificationConfigUnionTypeDef(BaseValidatorModel):
    pass


class SendCommandRequestTypeDef(BaseValidatorModel):
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
    NotificationConfig: Optional[NotificationConfigUnionTypeDef] = None
    CloudWatchOutputConfig: Optional[CloudWatchOutputConfigTypeDef] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None


class TargetLocationTypeDef(BaseValidatorModel):
    Accounts: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None
    TargetLocationMaxConcurrency: Optional[str] = None
    TargetLocationMaxErrors: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    TargetLocationAlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None
    IncludeChildOrganizationUnits: Optional[bool] = None
    ExcludeAccounts: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    TargetsMaxConcurrency: Optional[str] = None
    TargetsMaxErrors: Optional[str] = None


class AssociationStatusUnionTypeDef(BaseValidatorModel):
    pass


class UpdateAssociationStatusRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceId: str
    AssociationStatus: AssociationStatusUnionTypeDef


class ComplianceExecutionSummaryUnionTypeDef(BaseValidatorModel):
    pass


class PutComplianceItemsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: str
    ComplianceType: str
    ExecutionSummary: ComplianceExecutionSummaryUnionTypeDef
    Items: Sequence[ComplianceItemEntryTypeDef]
    ItemContentHash: Optional[str] = None
    UploadType: Optional[ComplianceUploadTypeType] = None


class GetExecutionPreviewResponseTypeDef(BaseValidatorModel):
    ExecutionPreviewId: str
    EndedAt: datetime
    Status: ExecutionPreviewStatusType
    StatusMessage: str
    ExecutionPreview: ExecutionPreviewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMaintenanceWindowTaskResultTypeDef(BaseValidatorModel):
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


class UpdateMaintenanceWindowTaskResultTypeDef(BaseValidatorModel):
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


class ListComplianceSummariesResultTypeDef(BaseValidatorModel):
    ComplianceSummaryItems: List[ComplianceSummaryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceComplianceSummariesResultTypeDef(BaseValidatorModel):
    ResourceComplianceSummaryItems: List[ResourceComplianceSummaryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDocumentMetadataHistoryResponseTypeDef(BaseValidatorModel):
    Name: str
    DocumentVersion: str
    Author: str
    Metadata: DocumentMetadataResponseInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetInventoryRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    Aggregators: Optional[Sequence[InventoryAggregatorPaginatorTypeDef]] = None
    ResultAttributes: Optional[Sequence[ResultAttributeTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetInventoryRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[InventoryFilterTypeDef]] = None
    Aggregators: Optional[Sequence[InventoryAggregatorTypeDef]] = None
    ResultAttributes: Optional[Sequence[ResultAttributeTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInstanceAssociationsStatusResultTypeDef(BaseValidatorModel):
    InstanceAssociationStatusInfos: List[InstanceAssociationStatusInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListNodesResultTypeDef(BaseValidatorModel):
    Nodes: List[NodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInventoryDeletionsResultTypeDef(BaseValidatorModel):
    InventoryDeletions: List[InventoryDeletionStatusItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PatchRuleGroupOutputTypeDef(BaseValidatorModel):
    PatchRules: List[PatchRuleOutputTypeDef]


class ResourceDataSyncItemTypeDef(BaseValidatorModel):
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


class ResourceDataSyncAwsOrganizationsSourceUnionTypeDef(BaseValidatorModel):
    pass


class ResourceDataSyncSourceTypeDef(BaseValidatorModel):
    SourceType: str
    SourceRegions: Sequence[str]
    AwsOrganizationsSource: Optional[ResourceDataSyncAwsOrganizationsSourceUnionTypeDef] = None
    IncludeFutureRegions: Optional[bool] = None
    EnableAllOpsDataSources: Optional[bool] = None


class CreateAssociationResultTypeDef(BaseValidatorModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAssociationResultTypeDef(BaseValidatorModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssociationResultTypeDef(BaseValidatorModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssociationStatusResultTypeDef(BaseValidatorModel):
    AssociationDescription: AssociationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssociationVersionsResultTypeDef(BaseValidatorModel):
    AssociationVersions: List[AssociationVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FailedCreateAssociationTypeDef(BaseValidatorModel):
    Entry: Optional[CreateAssociationBatchRequestEntryOutputTypeDef] = None
    Message: Optional[str] = None
    Fault: Optional[FaultType] = None


class AutomationExecutionMetadataTypeDef(BaseValidatorModel):
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
    TargetLocationsURL: Optional[str] = None
    AutomationSubtype: Optional[Literal["ChangeRequest"]] = None
    ScheduledTime: Optional[datetime] = None
    Runbooks: Optional[List[RunbookOutputTypeDef]] = None
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ChangeRequestName: Optional[str] = None


class AutomationExecutionTypeDef(BaseValidatorModel):
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
    TargetLocationsURL: Optional[str] = None
    AutomationSubtype: Optional[Literal["ChangeRequest"]] = None
    ScheduledTime: Optional[datetime] = None
    Runbooks: Optional[List[RunbookOutputTypeDef]] = None
    OpsItemId: Optional[str] = None
    AssociationId: Optional[str] = None
    ChangeRequestName: Optional[str] = None
    Variables: Optional[Dict[str, List[str]]] = None


class DescribeAutomationStepExecutionsResultTypeDef(BaseValidatorModel):
    StepExecutions: List[StepExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MaintenanceWindowTaskParameterValueExpressionUnionTypeDef(BaseValidatorModel):
    pass


class MaintenanceWindowTaskInvocationParametersUnionTypeDef(BaseValidatorModel):
    pass


class RegisterTaskWithMaintenanceWindowRequestTypeDef(BaseValidatorModel):
    WindowId: str
    TaskArn: str
    TaskType: MaintenanceWindowTaskTypeType
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ServiceRoleArn: Optional[str] = None
    TaskParameters: Optional[ Mapping[str, MaintenanceWindowTaskParameterValueExpressionUnionTypeDef] ] = None
    TaskInvocationParameters: Optional[MaintenanceWindowTaskInvocationParametersUnionTypeDef] = None
    Priority: Optional[int] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None


class UpdateMaintenanceWindowTaskRequestTypeDef(BaseValidatorModel):
    WindowId: str
    WindowTaskId: str
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    TaskArn: Optional[str] = None
    ServiceRoleArn: Optional[str] = None
    TaskParameters: Optional[ Mapping[str, MaintenanceWindowTaskParameterValueExpressionUnionTypeDef] ] = None
    TaskInvocationParameters: Optional[MaintenanceWindowTaskInvocationParametersUnionTypeDef] = None
    Priority: Optional[int] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    LoggingInfo: Optional[LoggingInfoTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Replace: Optional[bool] = None
    CutoffBehavior: Optional[MaintenanceWindowTaskCutoffBehaviorType] = None
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None


class GetPatchBaselineResultTypeDef(BaseValidatorModel):
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


class UpdatePatchBaselineResultTypeDef(BaseValidatorModel):
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


class PatchFilterGroupUnionTypeDef(BaseValidatorModel):
    pass


class PatchRuleTypeDef(BaseValidatorModel):
    PatchFilterGroup: PatchFilterGroupUnionTypeDef
    ComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApproveAfterDays: Optional[int] = None
    ApproveUntilDate: Optional[str] = None
    EnableNonSecurity: Optional[bool] = None


class ListResourceDataSyncResultTypeDef(BaseValidatorModel):
    ResourceDataSyncItems: List[ResourceDataSyncItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateResourceDataSyncRequestTypeDef(BaseValidatorModel):
    SyncName: str
    S3Destination: Optional[ResourceDataSyncS3DestinationTypeDef] = None
    SyncType: Optional[str] = None
    SyncSource: Optional[ResourceDataSyncSourceTypeDef] = None


class UpdateResourceDataSyncRequestTypeDef(BaseValidatorModel):
    SyncName: str
    SyncType: str
    SyncSource: ResourceDataSyncSourceTypeDef


class CreateAssociationBatchResultTypeDef(BaseValidatorModel):
    Successful: List[AssociationDescriptionTypeDef]
    Failed: List[FailedCreateAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAutomationExecutionsResultTypeDef(BaseValidatorModel):
    AutomationExecutionMetadataList: List[AutomationExecutionMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetAutomationExecutionResultTypeDef(BaseValidatorModel):
    AutomationExecution: AutomationExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TargetLocationUnionTypeDef(BaseValidatorModel):
    pass


class AutomationExecutionInputsTypeDef(BaseValidatorModel):
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    TargetLocations: Optional[Sequence[TargetLocationUnionTypeDef]] = None
    TargetLocationsURL: Optional[str] = None


class CreateAssociationBatchRequestEntryTypeDef(BaseValidatorModel):
    Name: str
    InstanceId: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    AutomationTargetParameterName: Optional[str] = None
    DocumentVersion: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    ScheduleExpression: Optional[str] = None
    OutputLocation: Optional[InstanceAssociationOutputLocationTypeDef] = None
    AssociationName: Optional[str] = None
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
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None


class CreateAssociationRequestTypeDef(BaseValidatorModel):
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
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None


class RunbookTypeDef(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, Sequence[str]]] = None
    TargetParameterName: Optional[str] = None
    Targets: Optional[Sequence[TargetUnionTypeDef]] = None
    TargetMaps: Optional[Sequence[Mapping[str, Sequence[str]]]] = None
    MaxConcurrency: Optional[str] = None
    MaxErrors: Optional[str] = None
    TargetLocations: Optional[Sequence[TargetLocationUnionTypeDef]] = None


class StartAutomationExecutionRequestTypeDef(BaseValidatorModel):
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
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None
    TargetLocationsURL: Optional[str] = None


class UpdateAssociationRequestTypeDef(BaseValidatorModel):
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
    AlarmConfiguration: Optional[AlarmConfigurationUnionTypeDef] = None


class ExecutionInputsTypeDef(BaseValidatorModel):
    Automation: Optional[AutomationExecutionInputsTypeDef] = None


class PatchRuleUnionTypeDef(BaseValidatorModel):
    pass


class PatchRuleGroupTypeDef(BaseValidatorModel):
    PatchRules: Sequence[PatchRuleUnionTypeDef]


class StartExecutionPreviewRequestTypeDef(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None
    ExecutionInputs: Optional[ExecutionInputsTypeDef] = None


class CreateAssociationBatchRequestEntryUnionTypeDef(BaseValidatorModel):
    pass


class CreateAssociationBatchRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[CreateAssociationBatchRequestEntryUnionTypeDef]


class RunbookUnionTypeDef(BaseValidatorModel):
    pass


class StartChangeRequestExecutionRequestTypeDef(BaseValidatorModel):
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


class PatchRuleGroupUnionTypeDef(BaseValidatorModel):
    pass


class PatchSourceUnionTypeDef(BaseValidatorModel):
    pass


class BaselineOverrideTypeDef(BaseValidatorModel):
    OperatingSystem: Optional[OperatingSystemType] = None
    GlobalFilters: Optional[PatchFilterGroupUnionTypeDef] = None
    ApprovalRules: Optional[PatchRuleGroupUnionTypeDef] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    Sources: Optional[Sequence[PatchSourceUnionTypeDef]] = None


class CreatePatchBaselineRequestTypeDef(BaseValidatorModel):
    Name: str
    OperatingSystem: Optional[OperatingSystemType] = None
    GlobalFilters: Optional[PatchFilterGroupUnionTypeDef] = None
    ApprovalRules: Optional[PatchRuleGroupUnionTypeDef] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    Description: Optional[str] = None
    Sources: Optional[Sequence[PatchSourceUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdatePatchBaselineRequestTypeDef(BaseValidatorModel):
    BaselineId: str
    Name: Optional[str] = None
    GlobalFilters: Optional[PatchFilterGroupUnionTypeDef] = None
    ApprovalRules: Optional[PatchRuleGroupUnionTypeDef] = None
    ApprovedPatches: Optional[Sequence[str]] = None
    ApprovedPatchesComplianceLevel: Optional[PatchComplianceLevelType] = None
    ApprovedPatchesEnableNonSecurity: Optional[bool] = None
    RejectedPatches: Optional[Sequence[str]] = None
    RejectedPatchesAction: Optional[PatchActionType] = None
    Description: Optional[str] = None
    Sources: Optional[Sequence[PatchSourceUnionTypeDef]] = None
    Replace: Optional[bool] = None


class GetDeployablePatchSnapshotForInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SnapshotId: str
    BaselineOverride: Optional[BaselineOverrideTypeDef] = None


