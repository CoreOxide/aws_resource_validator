from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudformation.cloudformation_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountGateResult(BaseValidatorModel):
    Status: Optional[AccountGateStatusType] = None
    StatusReason: Optional[str] = None


class AccountLimit(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[int] = None


class LoggingConfig(BaseValidatorModel):
    LogRoleArn: str
    LogGroupName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AutoDeployment(BaseValidatorModel):
    Enabled: Optional[bool] = None
    RetainStacksOnAccountRemoval: Optional[bool] = None


class TypeConfigurationIdentifier(BaseValidatorModel):
    TypeArn: Optional[str] = None
    TypeConfigurationAlias: Optional[str] = None
    TypeConfigurationArn: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    TypeName: Optional[str] = None


class TypeConfigurationDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Alias: Optional[str] = None
    Configuration: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    TypeArn: Optional[str] = None
    TypeName: Optional[str] = None
    IsDefaultConfiguration: Optional[bool] = None


class CancelUpdateStackInputStackCancelUpdate(BaseValidatorModel):
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'cancel_update_stack' function.
class CancelUpdateStackInput(BaseValidatorModel):
    StackName: str
    ClientRequestToken: Optional[str] = None


class ChangeSetHookResourceTargetDetails(BaseValidatorModel):
    LogicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceAction: Optional[ChangeActionType] = None


class ChangeSetSummary(BaseValidatorModel):
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    ChangeSetId: Optional[str] = None
    ChangeSetName: Optional[str] = None
    ExecutionStatus: Optional[ExecutionStatusType] = None
    Status: Optional[ChangeSetStatusType] = None
    StatusReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Description: Optional[str] = None
    IncludeNestedStacks: Optional[bool] = None
    ParentChangeSetId: Optional[str] = None
    RootChangeSetId: Optional[str] = None
    ImportExistingResources: Optional[bool] = None


class ContinueUpdateRollbackInput(BaseValidatorModel):
    StackName: str
    RoleARN: Optional[str] = None
    ResourcesToSkip: Optional[List[str]] = None
    ClientRequestToken: Optional[str] = None


class Parameter(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    ParameterValue: Optional[str] = None
    UsePreviousValue: Optional[bool] = None
    ResolvedValue: Optional[str] = None


class ResourceToImport(BaseValidatorModel):
    ResourceType: str
    LogicalResourceId: str
    ResourceIdentifier: Dict[str, str]


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResourceDefinition(BaseValidatorModel):
    ResourceType: str
    ResourceIdentifier: Dict[str, str]
    LogicalResourceId: Optional[str] = None


class TemplateConfiguration(BaseValidatorModel):
    DeletionPolicy: Optional[GeneratedTemplateDeletionPolicyType] = None
    UpdateReplacePolicy: Optional[GeneratedTemplateUpdateReplacePolicyType] = None


class StackDefinition(BaseValidatorModel):
    StackName: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None


class ManagedExecution(BaseValidatorModel):
    Active: Optional[bool] = None


class DeactivateTypeInput(BaseValidatorModel):
    TypeName: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    Arn: Optional[str] = None


class DeleteChangeSetInput(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None


# This class is the input for the 'delete_generated_template' function.
class DeleteGeneratedTemplateInput(BaseValidatorModel):
    GeneratedTemplateName: str


class DeleteStackInputStackDelete(BaseValidatorModel):
    RetainResources: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DeletionMode: Optional[DeletionModeType] = None


# This class is the input for the 'delete_stack' function.
class DeleteStackInput(BaseValidatorModel):
    StackName: str
    RetainResources: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DeletionMode: Optional[DeletionModeType] = None


class DeleteStackSetInput(BaseValidatorModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None


class DeploymentTargetsOutput(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    AccountsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    AccountFilterType: Optional[AccountFilterTypeType] = None


class DeploymentTargets(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    AccountsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    AccountFilterType: Optional[AccountFilterTypeType] = None


class DeregisterTypeInput(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_account_limits' function.
class DescribeAccountLimitsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'describe_change_set_hooks' function.
class DescribeChangeSetHooksInput(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    LogicalResourceId: Optional[str] = None


# This class is the input for the 'describe_change_set' function.
class DescribeChangeSetInput(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_generated_template' function.
class DescribeGeneratedTemplateInput(BaseValidatorModel):
    GeneratedTemplateName: str


class TemplateProgress(BaseValidatorModel):
    ResourcesSucceeded: Optional[int] = None
    ResourcesFailed: Optional[int] = None
    ResourcesProcessing: Optional[int] = None
    ResourcesPending: Optional[int] = None


# This class is the input for the 'describe_organizations_access' function.
class DescribeOrganizationsAccessInput(BaseValidatorModel):
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'describe_publisher' function.
class DescribePublisherInput(BaseValidatorModel):
    PublisherId: Optional[str] = None


# This class is the input for the 'describe_resource_scan' function.
class DescribeResourceScanInput(BaseValidatorModel):
    ResourceScanId: str


# This class is the input for the 'describe_stack_drift_detection_status' function.
class DescribeStackDriftDetectionStatusInput(BaseValidatorModel):
    StackDriftDetectionId: str


# This class is the input for the 'describe_stack_events' function.
class DescribeStackEventsInput(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None


class StackEvent(BaseValidatorModel):
    StackId: str
    EventId: str
    StackName: str
    Timestamp: datetime
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceStatus: Optional[ResourceStatusType] = None
    ResourceStatusReason: Optional[str] = None
    ResourceProperties: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    HookType: Optional[str] = None
    HookStatus: Optional[HookStatusType] = None
    HookStatusReason: Optional[str] = None
    HookInvocationPoint: Optional[Literal['PRE_PROVISION']] = None
    HookFailureMode: Optional[HookFailureModeType] = None
    DetailedStatus: Optional[DetailedStatusType] = None


# This class is the input for the 'describe_stack_instance' function.
class DescribeStackInstanceInput(BaseValidatorModel):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'describe_stack_refactor' function.
class DescribeStackRefactorInput(BaseValidatorModel):
    StackRefactorId: str


# This class is the input for the 'describe_stack_resource_drifts' function.
class DescribeStackResourceDriftsInput(BaseValidatorModel):
    StackName: str
    StackResourceDriftStatusFilters: Optional[List[StackResourceDriftStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_stack_resource' function.
class DescribeStackResourceInput(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str


# This class is the input for the 'describe_stack_resources' function.
class DescribeStackResourcesInput(BaseValidatorModel):
    StackName: Optional[str] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None


# This class is the input for the 'describe_stack_set' function.
class DescribeStackSetInput(BaseValidatorModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'describe_stack_set_operation' function.
class DescribeStackSetOperationInput(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'describe_stacks' function.
class DescribeStacksInput(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_type' function.
class DescribeTypeInput(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    Arn: Optional[str] = None
    VersionId: Optional[str] = None
    PublisherId: Optional[str] = None
    PublicVersionNumber: Optional[str] = None


class RequiredActivatedType(BaseValidatorModel):
    TypeNameAlias: Optional[str] = None
    OriginalTypeName: Optional[str] = None
    PublisherId: Optional[str] = None
    SupportedMajorVersions: Optional[List[int]] = None


# This class is the input for the 'describe_type_registration' function.
class DescribeTypeRegistrationInput(BaseValidatorModel):
    RegistrationToken: str


# This class is the input for the 'detect_stack_drift' function.
class DetectStackDriftInput(BaseValidatorModel):
    StackName: str
    LogicalResourceIds: Optional[List[str]] = None


# This class is the input for the 'detect_stack_resource_drift' function.
class DetectStackResourceDriftInput(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str


class ExecuteChangeSetInput(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DisableRollback: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None


# This class is the input for the 'execute_stack_refactor' function.
class ExecuteStackRefactorInput(BaseValidatorModel):
    StackRefactorId: str


class Export(BaseValidatorModel):
    ExportingStackId: Optional[str] = None
    Name: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'get_generated_template' function.
class GetGeneratedTemplateInput(BaseValidatorModel):
    GeneratedTemplateName: str
    Format: Optional[TemplateFormatType] = None


# This class is the input for the 'get_stack_policy' function.
class GetStackPolicyInput(BaseValidatorModel):
    StackName: str


# This class is the input for the 'get_template' function.
class GetTemplateInput(BaseValidatorModel):
    StackName: Optional[str] = None
    ChangeSetName: Optional[str] = None
    TemplateStage: Optional[TemplateStageType] = None


class TemplateSummaryConfig(BaseValidatorModel):
    TreatUnrecognizedResourceTypesAsWarnings: Optional[bool] = None


class ResourceIdentifierSummary(BaseValidatorModel):
    ResourceType: Optional[str] = None
    LogicalResourceIds: Optional[List[str]] = None
    ResourceIdentifiers: Optional[List[str]] = None


class Warnings(BaseValidatorModel):
    UnrecognizedResourceTypes: Optional[List[str]] = None


class HookResultSummary(BaseValidatorModel):
    InvocationPoint: Optional[Literal['PRE_PROVISION']] = None
    FailureMode: Optional[HookFailureModeType] = None
    TypeName: Optional[str] = None
    TypeVersionId: Optional[str] = None
    TypeConfigurationVersionId: Optional[str] = None
    Status: Optional[HookStatusType] = None
    HookStatusReason: Optional[str] = None


# This class is the input for the 'list_change_sets' function.
class ListChangeSetsInput(BaseValidatorModel):
    StackName: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_exports' function.
class ListExportsInput(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_generated_templates' function.
class ListGeneratedTemplatesInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TemplateSummary(BaseValidatorModel):
    GeneratedTemplateId: Optional[str] = None
    GeneratedTemplateName: Optional[str] = None
    Status: Optional[GeneratedTemplateStatusType] = None
    StatusReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    NumberOfResources: Optional[int] = None


# This class is the input for the 'list_hook_results' function.
class ListHookResultsInput(BaseValidatorModel):
    TargetType: ListHookResultsTargetTypeType
    TargetId: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_imports' function.
class ListImportsInput(BaseValidatorModel):
    ExportName: str
    NextToken: Optional[str] = None


class ScannedResourceIdentifier(BaseValidatorModel):
    ResourceType: str
    ResourceIdentifier: Dict[str, str]


class ScannedResource(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceIdentifier: Optional[Dict[str, str]] = None
    ManagedByStack: Optional[bool] = None


# This class is the input for the 'list_resource_scan_resources' function.
class ListResourceScanResourcesInput(BaseValidatorModel):
    ResourceScanId: str
    ResourceIdentifier: Optional[str] = None
    ResourceTypePrefix: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_resource_scans' function.
class ListResourceScansInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceScanSummary(BaseValidatorModel):
    ResourceScanId: Optional[str] = None
    Status: Optional[ResourceScanStatusType] = None
    StatusReason: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    PercentageCompleted: Optional[float] = None


# This class is the input for the 'list_stack_instance_resource_drifts' function.
class ListStackInstanceResourceDriftsInput(BaseValidatorModel):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    OperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StackInstanceResourceDriftStatuses: Optional[List[StackResourceDriftStatusType]] = None
    CallAs: Optional[CallAsType] = None


class StackInstanceFilter(BaseValidatorModel):
    Name: Optional[StackInstanceFilterNameType] = None
    Values: Optional[str] = None


# This class is the input for the 'list_stack_refactor_actions' function.
class ListStackRefactorActionsInput(BaseValidatorModel):
    StackRefactorId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_stack_refactors' function.
class ListStackRefactorsInput(BaseValidatorModel):
    ExecutionStatusFilter: Optional[List[StackRefactorExecutionStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StackRefactorSummary(BaseValidatorModel):
    StackRefactorId: Optional[str] = None
    Description: Optional[str] = None
    ExecutionStatus: Optional[StackRefactorExecutionStatusType] = None
    ExecutionStatusReason: Optional[str] = None
    Status: Optional[StackRefactorStatusType] = None
    StatusReason: Optional[str] = None


# This class is the input for the 'list_stack_resources' function.
class ListStackResourcesInput(BaseValidatorModel):
    StackName: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_stack_set_auto_deployment_targets' function.
class ListStackSetAutoDeploymentTargetsInput(BaseValidatorModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None


class StackSetAutoDeploymentTargetSummary(BaseValidatorModel):
    OrganizationalUnitId: Optional[str] = None
    Regions: Optional[List[str]] = None


class OperationResultFilter(BaseValidatorModel):
    Name: Optional[Literal['OPERATION_RESULT_STATUS']] = None
    Values: Optional[str] = None


# This class is the input for the 'list_stack_set_operations' function.
class ListStackSetOperationsInput(BaseValidatorModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'list_stack_sets' function.
class ListStackSetsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[StackSetStatusType] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'list_stacks' function.
class ListStacksInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    StackStatusFilter: Optional[List[StackStatusType]] = None


# This class is the input for the 'list_type_registrations' function.
class ListTypeRegistrationsInput(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    TypeArn: Optional[str] = None
    RegistrationStatusFilter: Optional[RegistrationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_type_versions' function.
class ListTypeVersionsInput(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    Arn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    PublisherId: Optional[str] = None


class TypeVersionSummary(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    Arn: Optional[str] = None
    TimeCreated: Optional[datetime] = None
    Description: Optional[str] = None
    PublicVersionNumber: Optional[str] = None


class TypeFilters(BaseValidatorModel):
    Category: Optional[CategoryType] = None
    PublisherId: Optional[str] = None
    TypeNamePrefix: Optional[str] = None


class TypeSummary(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    TypeArn: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    Description: Optional[str] = None
    PublisherId: Optional[str] = None
    OriginalTypeName: Optional[str] = None
    PublicVersionNumber: Optional[str] = None
    LatestPublicVersion: Optional[str] = None
    PublisherIdentity: Optional[IdentityProviderType] = None
    PublisherName: Optional[str] = None
    IsActivated: Optional[bool] = None


class ModuleInfo(BaseValidatorModel):
    TypeHierarchy: Optional[str] = None
    LogicalIdHierarchy: Optional[str] = None


class Output(BaseValidatorModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None
    ExportName: Optional[str] = None


class ParameterConstraints(BaseValidatorModel):
    AllowedValues: Optional[List[str]] = None


class PhysicalResourceIdContextKeyValuePair(BaseValidatorModel):
    Key: str
    Value: str


class PropertyDifference(BaseValidatorModel):
    PropertyPath: str
    ExpectedValue: str
    ActualValue: str
    DifferenceType: DifferenceTypeType


# This class is the input for the 'publish_type' function.
class PublishTypeInput(BaseValidatorModel):
    Type: Optional[ThirdPartyTypeType] = None
    Arn: Optional[str] = None
    TypeName: Optional[str] = None
    PublicVersionNumber: Optional[str] = None


class RecordHandlerProgressInput(BaseValidatorModel):
    BearerToken: str
    OperationStatus: OperationStatusType
    CurrentOperationStatus: Optional[OperationStatusType] = None
    StatusMessage: Optional[str] = None
    ErrorCode: Optional[HandlerErrorCodeType] = None
    ResourceModel: Optional[str] = None
    ClientRequestToken: Optional[str] = None


# This class is the input for the 'register_publisher' function.
class RegisterPublisherInput(BaseValidatorModel):
    AcceptTermsAndConditions: Optional[bool] = None
    ConnectionArn: Optional[str] = None


class ResourceTargetDefinition(BaseValidatorModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None
    Path: Optional[str] = None
    BeforeValue: Optional[str] = None
    AfterValue: Optional[str] = None
    AttributeChangeType: Optional[AttributeChangeTypeType] = None


class ResourceLocation(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str


class RollbackTrigger(BaseValidatorModel):
    Arn: str
    Type: str


# This class is the input for the 'rollback_stack' function.
class RollbackStackInput(BaseValidatorModel):
    StackName: str
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None


# This class is the input for the 'set_stack_policy' function.
class SetStackPolicyInput(BaseValidatorModel):
    StackName: str
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None


# This class is the input for the 'set_type_configuration' function.
class SetTypeConfigurationInput(BaseValidatorModel):
    Configuration: str
    TypeArn: Optional[str] = None
    ConfigurationAlias: Optional[str] = None
    TypeName: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None


class SetaultVersionInput(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None


# This class is the input for the 'signal_resource' function.
class SignalResourceInput(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str
    UniqueId: str
    Status: ResourceSignalStatusType


class StackDriftInformationSummary(BaseValidatorModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None


class StackDriftInformation(BaseValidatorModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None


class StackInstanceComprehensiveStatus(BaseValidatorModel):
    DetailedStatus: Optional[StackInstanceDetailedStatusType] = None


class StackResourceDriftInformation(BaseValidatorModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None


class StackResourceDriftInformationSummary(BaseValidatorModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None


class StackSetDriftDetectionDetails(BaseValidatorModel):
    DriftStatus: Optional[StackSetDriftStatusType] = None
    DriftDetectionStatus: Optional[StackSetDriftDetectionStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    TotalStackInstancesCount: Optional[int] = None
    DriftedStackInstancesCount: Optional[int] = None
    InSyncStackInstancesCount: Optional[int] = None
    InProgressStackInstancesCount: Optional[int] = None
    FailedStackInstancesCount: Optional[int] = None


class StackSetOperationPreferencesOutput(BaseValidatorModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[List[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None


class StackSetOperationPreferences(BaseValidatorModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[List[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None


class StackSetOperationStatusDetails(BaseValidatorModel):
    FailedStackInstancesCount: Optional[int] = None


# This class is the input for the 'start_resource_scan' function.
class StartResourceScanInput(BaseValidatorModel):
    ClientRequestToken: Optional[str] = None


class StopStackSetOperationInput(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None


class TemplateParameter(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    NoEcho: Optional[bool] = None
    Description: Optional[str] = None


# This class is the input for the 'test_type' function.
class TestTypeInput(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None
    LogDeliveryBucket: Optional[str] = None


# This class is the input for the 'update_termination_protection' function.
class UpdateTerminationProtectionInput(BaseValidatorModel):
    EnableTerminationProtection: bool
    StackName: str


# This class is the input for the 'validate_template' function.
class ValidateTemplateInput(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None


class WarningProperty(BaseValidatorModel):
    PropertyPath: Optional[str] = None
    Required: Optional[bool] = None
    Description: Optional[str] = None


class StackSetOperationResultSummary(BaseValidatorModel):
    Account: Optional[str] = None
    Region: Optional[str] = None
    Status: Optional[StackSetOperationResultStatusType] = None
    StatusReason: Optional[str] = None
    AccountGateResult: Optional[AccountGateResult] = None
    OrganizationalUnitId: Optional[str] = None


# This class is the input for the 'activate_type' function.
class ActivateTypeInput(BaseValidatorModel):
    Type: Optional[ThirdPartyTypeType] = None
    PublicTypeArn: Optional[str] = None
    PublisherId: Optional[str] = None
    TypeName: Optional[str] = None
    TypeNameAlias: Optional[str] = None
    AutoUpdate: Optional[bool] = None
    LoggingConfig: Optional[LoggingConfig] = None
    ExecutionRoleArn: Optional[str] = None
    VersionBump: Optional[VersionBumpType] = None
    MajorVersion: Optional[int] = None


# This class is the input for the 'register_type' function.
class RegisterTypeInput(BaseValidatorModel):
    TypeName: str
    SchemaHandlerPackage: str
    Type: Optional[RegistryTypeType] = None
    LoggingConfig: Optional[LoggingConfig] = None
    ExecutionRoleArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None


# This class is the output for the 'activate_type' function.
class ActivateTypeOutput(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_change_set' function.
class CreateChangeSetOutput(BaseValidatorModel):
    Id: str
    StackId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_generated_template' function.
class CreateGeneratedTemplateOutput(BaseValidatorModel):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stack_instances' function.
class CreateStackInstancesOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stack' function.
class CreateStackOutput(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stack_refactor' function.
class CreateStackRefactorOutput(BaseValidatorModel):
    StackRefactorId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stack_set' function.
class CreateStackSetOutput(BaseValidatorModel):
    StackSetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_stack_instances' function.
class DeleteStackInstancesOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_account_limits' function.
class DescribeAccountLimitsOutput(BaseValidatorModel):
    AccountLimits: List[AccountLimit]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_organizations_access' function.
class DescribeOrganizationsAccessOutput(BaseValidatorModel):
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_publisher' function.
class DescribePublisherOutput(BaseValidatorModel):
    PublisherId: str
    PublisherStatus: PublisherStatusType
    IdentityProvider: IdentityProviderType
    PublisherProfile: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resource_scan' function.
class DescribeResourceScanOutput(BaseValidatorModel):
    ResourceScanId: str
    Status: ResourceScanStatusType
    StatusReason: str
    StartTime: datetime
    EndTime: datetime
    PercentageCompleted: float
    ResourceTypes: List[str]
    ResourcesScanned: int
    ResourcesRead: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stack_drift_detection_status' function.
class DescribeStackDriftDetectionStatusOutput(BaseValidatorModel):
    StackId: str
    StackDriftDetectionId: str
    StackDriftStatus: StackDriftStatusType
    DetectionStatus: StackDriftDetectionStatusType
    DetectionStatusReason: str
    DriftedStackResourceCount: int
    Timestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stack_refactor' function.
class DescribeStackRefactorOutput(BaseValidatorModel):
    Description: str
    StackRefactorId: str
    StackIds: List[str]
    ExecutionStatus: StackRefactorExecutionStatusType
    ExecutionStatusReason: str
    Status: StackRefactorStatusType
    StatusReason: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_type_registration' function.
class DescribeTypeRegistrationOutput(BaseValidatorModel):
    ProgressStatus: RegistrationStatusType
    Description: str
    TypeArn: str
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_stack_drift' function.
class DetectStackDriftOutput(BaseValidatorModel):
    StackDriftDetectionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detect_stack_set_drift' function.
class DetectStackSetDriftOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'signal_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'estimate_template_cost' function.
class EstimateTemplateCostOutput(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_generated_template' function.
class GetGeneratedTemplateOutput(BaseValidatorModel):
    Status: GeneratedTemplateStatusType
    TemplateBody: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_stack_policy' function.
class GetStackPolicyOutput(BaseValidatorModel):
    StackPolicyBody: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_template' function.
class GetTemplateOutput(BaseValidatorModel):
    TemplateBody: Dict[str, Any]
    StagesAvailable: List[TemplateStageType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_stacks_to_stack_set' function.
class ImportStacksToStackSetOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_imports' function.
class ListImportsOutput(BaseValidatorModel):
    Imports: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_type_registrations' function.
class ListTypeRegistrationsOutput(BaseValidatorModel):
    RegistrationTokenList: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'publish_type' function.
class PublishTypeOutput(BaseValidatorModel):
    PublicTypeArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_publisher' function.
class RegisterPublisherOutput(BaseValidatorModel):
    PublisherId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_type' function.
class RegisterTypeOutput(BaseValidatorModel):
    RegistrationToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rollback_stack' function.
class RollbackStackOutput(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_type_configuration' function.
class SetTypeConfigurationOutput(BaseValidatorModel):
    ConfigurationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_resource_scan' function.
class StartResourceScanOutput(BaseValidatorModel):
    ResourceScanId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_type' function.
class TestTypeOutput(BaseValidatorModel):
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_generated_template' function.
class UpdateGeneratedTemplateOutput(BaseValidatorModel):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_stack_instances' function.
class UpdateStackInstancesOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_stack' function.
class UpdateStackOutput(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_stack_set' function.
class UpdateStackSetOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_termination_protection' function.
class UpdateTerminationProtectionOutput(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadata


class BatchDescribeTypeConfigurationsError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    TypeConfigurationIdentifier: Optional[TypeConfigurationIdentifier] = None


# This class is the input for the 'batch_describe_type_configurations' function.
class BatchDescribeTypeConfigurationsInput(BaseValidatorModel):
    TypeConfigurationIdentifiers: List[TypeConfigurationIdentifier]


class ChangeSetHookTargetDetails(BaseValidatorModel):
    TargetType: Optional[Literal['RESOURCE']] = None
    ResourceTargetDetails: Optional[ChangeSetHookResourceTargetDetails] = None


# This class is the output for the 'list_change_sets' function.
class ListChangeSetsOutput(BaseValidatorModel):
    Summaries: List[ChangeSetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'estimate_template_cost' function.
class EstimateTemplateCostInput(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None


# This class is the input for the 'create_generated_template' function.
class CreateGeneratedTemplateInput(BaseValidatorModel):
    GeneratedTemplateName: str
    Resources: Optional[List[ResourceDefinition]] = None
    StackName: Optional[str] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None


# This class is the input for the 'update_generated_template' function.
class UpdateGeneratedTemplateInput(BaseValidatorModel):
    GeneratedTemplateName: str
    NewGeneratedTemplateName: Optional[str] = None
    AddResources: Optional[List[ResourceDefinition]] = None
    RemoveResources: Optional[List[str]] = None
    RefreshAllResources: Optional[bool] = None
    TemplateConfiguration: Optional[TemplateConfiguration] = None


# This class is the input for the 'create_stack_set' function.
class CreateStackSetInput(BaseValidatorModel):
    StackSetName: str
    Description: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    StackId: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    Tags: Optional[List[Tag]] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    PermissionModel: Optional[PermissionModelsType] = None
    AutoDeployment: Optional[AutoDeployment] = None
    CallAs: Optional[CallAsType] = None
    ClientRequestToken: Optional[str] = None
    ManagedExecution: Optional[ManagedExecution] = None


class StackSetSummary(BaseValidatorModel):
    StackSetName: Optional[str] = None
    StackSetId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[StackSetStatusType] = None
    AutoDeployment: Optional[AutoDeployment] = None
    PermissionModel: Optional[PermissionModelsType] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    ManagedExecution: Optional[ManagedExecution] = None

DeploymentTargetsUnion = Union[DeploymentTargets, DeploymentTargetsOutput]


class DescribeAccountLimitsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeChangeSetInputPaginate(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStackEventsInputPaginate(BaseValidatorModel):
    StackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStacksInputPaginate(BaseValidatorModel):
    StackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListChangeSetsInputPaginate(BaseValidatorModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExportsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGeneratedTemplatesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportsInputPaginate(BaseValidatorModel):
    ExportName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceScanResourcesInputPaginate(BaseValidatorModel):
    ResourceScanId: str
    ResourceIdentifier: Optional[str] = None
    ResourceTypePrefix: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceScansInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStackRefactorActionsInputPaginate(BaseValidatorModel):
    StackRefactorId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStackRefactorsInputPaginate(BaseValidatorModel):
    ExecutionStatusFilter: Optional[List[StackRefactorExecutionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStackResourcesInputPaginate(BaseValidatorModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStackSetOperationsInputPaginate(BaseValidatorModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStackSetsInputPaginate(BaseValidatorModel):
    Status: Optional[StackSetStatusType] = None
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStacksInputPaginate(BaseValidatorModel):
    StackStatusFilter: Optional[List[StackStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeChangeSetInputWait(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStackRefactorInputWaitExtra(BaseValidatorModel):
    StackRefactorId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStackRefactorInputWait(BaseValidatorModel):
    StackRefactorId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStacksInputWaitExtraExtraExtraExtraExtra(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStacksInputWaitExtraExtraExtraExtra(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStacksInputWaitExtraExtraExtra(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStacksInputWaitExtraExtra(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStacksInputWaitExtra(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStacksInputWait(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTypeRegistrationInputWait(BaseValidatorModel):
    RegistrationToken: str
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_stack_events' function.
class DescribeStackEventsOutput(BaseValidatorModel):
    StackEvents: List[StackEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_type' function.
class DescribeTypeOutput(BaseValidatorModel):
    Arn: str
    Type: RegistryTypeType
    TypeName: str
    DefaultVersionId: str
    IsDefaultVersion: bool
    TypeTestsStatus: TypeTestsStatusType
    TypeTestsStatusDescription: str
    Description: str
    Schema: str
    ProvisioningType: ProvisioningTypeType
    DeprecatedStatus: DeprecatedStatusType
    LoggingConfig: LoggingConfig
    RequiredActivatedTypes: List[RequiredActivatedType]
    ExecutionRoleArn: str
    Visibility: VisibilityType
    SourceUrl: str
    DocumentationUrl: str
    LastUpdated: datetime
    TimeCreated: datetime
    ConfigurationSchema: str
    PublisherId: str
    OriginalTypeName: str
    OriginalTypeArn: str
    PublicVersionNumber: str
    LatestPublicVersion: str
    IsActivated: bool
    AutoUpdate: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_exports' function.
class ListExportsOutput(BaseValidatorModel):
    Exports: List[Export]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'get_template_summary' function.
class GetTemplateSummaryInput(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    StackName: Optional[str] = None
    StackSetName: Optional[str] = None
    CallAs: Optional[CallAsType] = None
    TemplateSummaryConfig: Optional[TemplateSummaryConfig] = None


# This class is the output for the 'list_hook_results' function.
class ListHookResultsOutput(BaseValidatorModel):
    TargetType: ListHookResultsTargetTypeType
    TargetId: str
    HookResults: List[HookResultSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_generated_templates' function.
class ListGeneratedTemplatesOutput(BaseValidatorModel):
    Summaries: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceScanRelatedResourcesInputPaginate(BaseValidatorModel):
    ResourceScanId: str
    Resources: List[ScannedResourceIdentifier]
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_resource_scan_related_resources' function.
class ListResourceScanRelatedResourcesInput(BaseValidatorModel):
    ResourceScanId: str
    Resources: List[ScannedResourceIdentifier]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_resource_scan_related_resources' function.
class ListResourceScanRelatedResourcesOutput(BaseValidatorModel):
    RelatedResources: List[ScannedResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_resource_scan_resources' function.
class ListResourceScanResourcesOutput(BaseValidatorModel):
    Resources: List[ScannedResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_resource_scans' function.
class ListResourceScansOutput(BaseValidatorModel):
    ResourceScanSummaries: List[ResourceScanSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStackInstancesInputPaginate(BaseValidatorModel):
    StackSetName: str
    Filters: Optional[List[StackInstanceFilter]] = None
    StackInstanceAccount: Optional[str] = None
    StackInstanceRegion: Optional[str] = None
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_stack_instances' function.
class ListStackInstancesInput(BaseValidatorModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[StackInstanceFilter]] = None
    StackInstanceAccount: Optional[str] = None
    StackInstanceRegion: Optional[str] = None
    CallAs: Optional[CallAsType] = None


# This class is the output for the 'list_stack_refactors' function.
class ListStackRefactorsOutput(BaseValidatorModel):
    StackRefactorSummaries: List[StackRefactorSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_stack_set_auto_deployment_targets' function.
class ListStackSetAutoDeploymentTargetsOutput(BaseValidatorModel):
    Summaries: List[StackSetAutoDeploymentTargetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStackSetOperationResultsInputPaginate(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None
    Filters: Optional[List[OperationResultFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_stack_set_operation_results' function.
class ListStackSetOperationResultsInput(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None
    Filters: Optional[List[OperationResultFilter]] = None


# This class is the output for the 'list_type_versions' function.
class ListTypeVersionsOutput(BaseValidatorModel):
    TypeVersionSummaries: List[TypeVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTypesInputPaginate(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    Type: Optional[RegistryTypeType] = None
    Filters: Optional[TypeFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_types' function.
class ListTypesInput(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    Type: Optional[RegistryTypeType] = None
    Filters: Optional[TypeFilters] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_types' function.
class ListTypesOutput(BaseValidatorModel):
    TypeSummaries: List[TypeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ParameterDeclaration(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    ParameterType: Optional[str] = None
    NoEcho: Optional[bool] = None
    Description: Optional[str] = None
    ParameterConstraints: Optional[ParameterConstraints] = None


class StackInstanceResourceDriftsSummary(BaseValidatorModel):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: Optional[str] = None
    PhysicalResourceIdContext: Optional[List[PhysicalResourceIdContextKeyValuePair]] = None
    PropertyDifferences: Optional[List[PropertyDifference]] = None


class StackResourceDrift(BaseValidatorModel):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: Optional[str] = None
    PhysicalResourceIdContext: Optional[List[PhysicalResourceIdContextKeyValuePair]] = None
    ExpectedProperties: Optional[str] = None
    ActualProperties: Optional[str] = None
    PropertyDifferences: Optional[List[PropertyDifference]] = None
    ModuleInfo: Optional[ModuleInfo] = None


class ResourceChangeDetail(BaseValidatorModel):
    Target: Optional[ResourceTargetDefinition] = None
    Evaluation: Optional[EvaluationTypeType] = None
    ChangeSource: Optional[ChangeSourceType] = None
    CausingEntity: Optional[str] = None


class ResourceMapping(BaseValidatorModel):
    Source: ResourceLocation
    Destination: ResourceLocation


class RollbackConfigurationOutput(BaseValidatorModel):
    RollbackTriggers: Optional[List[RollbackTrigger]] = None
    MonitoringTimeInMinutes: Optional[int] = None


class RollbackConfiguration(BaseValidatorModel):
    RollbackTriggers: Optional[List[RollbackTrigger]] = None
    MonitoringTimeInMinutes: Optional[int] = None


class StackSummary(BaseValidatorModel):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatusType
    StackId: Optional[str] = None
    TemplateDescription: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None
    DeletionTime: Optional[datetime] = None
    StackStatusReason: Optional[str] = None
    ParentId: Optional[str] = None
    RootId: Optional[str] = None
    DriftInformation: Optional[StackDriftInformationSummary] = None


class StackInstanceSummary(BaseValidatorModel):
    StackSetId: Optional[str] = None
    Region: Optional[str] = None
    Account: Optional[str] = None
    StackId: Optional[str] = None
    Status: Optional[StackInstanceStatusType] = None
    StatusReason: Optional[str] = None
    StackInstanceStatus: Optional[StackInstanceComprehensiveStatus] = None
    OrganizationalUnitId: Optional[str] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    LastOperationId: Optional[str] = None


class StackInstance(BaseValidatorModel):
    StackSetId: Optional[str] = None
    Region: Optional[str] = None
    Account: Optional[str] = None
    StackId: Optional[str] = None
    ParameterOverrides: Optional[List[Parameter]] = None
    Status: Optional[StackInstanceStatusType] = None
    StackInstanceStatus: Optional[StackInstanceComprehensiveStatus] = None
    StatusReason: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    LastOperationId: Optional[str] = None


class StackResourceDetail(BaseValidatorModel):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatusType
    StackName: Optional[str] = None
    StackId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceStatusReason: Optional[str] = None
    Description: Optional[str] = None
    Metadata: Optional[str] = None
    DriftInformation: Optional[StackResourceDriftInformation] = None
    ModuleInfo: Optional[ModuleInfo] = None


class StackResource(BaseValidatorModel):
    LogicalResourceId: str
    ResourceType: str
    Timestamp: datetime
    ResourceStatus: ResourceStatusType
    StackName: Optional[str] = None
    StackId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceStatusReason: Optional[str] = None
    Description: Optional[str] = None
    DriftInformation: Optional[StackResourceDriftInformation] = None
    ModuleInfo: Optional[ModuleInfo] = None


class StackResourceSummary(BaseValidatorModel):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatusType
    PhysicalResourceId: Optional[str] = None
    ResourceStatusReason: Optional[str] = None
    DriftInformation: Optional[StackResourceDriftInformationSummary] = None
    ModuleInfo: Optional[ModuleInfo] = None


class StackSet(BaseValidatorModel):
    StackSetName: Optional[str] = None
    StackSetId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[StackSetStatusType] = None
    TemplateBody: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    Tags: Optional[List[Tag]] = None
    StackSetARN: Optional[str] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    StackSetDriftDetectionDetails: Optional[StackSetDriftDetectionDetails] = None
    AutoDeployment: Optional[AutoDeployment] = None
    PermissionModel: Optional[PermissionModelsType] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    ManagedExecution: Optional[ManagedExecution] = None
    Regions: Optional[List[str]] = None

StackSetOperationPreferencesUnion = Union[StackSetOperationPreferences, StackSetOperationPreferencesOutput]


class StackSetOperationSummary(BaseValidatorModel):
    OperationId: Optional[str] = None
    Action: Optional[StackSetOperationActionType] = None
    Status: Optional[StackSetOperationStatusType] = None
    CreationTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    StatusReason: Optional[str] = None
    StatusDetails: Optional[StackSetOperationStatusDetails] = None
    OperationPreferences: Optional[StackSetOperationPreferencesOutput] = None


class StackSetOperation(BaseValidatorModel):
    OperationId: Optional[str] = None
    StackSetId: Optional[str] = None
    Action: Optional[StackSetOperationActionType] = None
    Status: Optional[StackSetOperationStatusType] = None
    OperationPreferences: Optional[StackSetOperationPreferencesOutput] = None
    RetainStacks: Optional[bool] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    DeploymentTargets: Optional[DeploymentTargetsOutput] = None
    StackSetDriftDetectionDetails: Optional[StackSetDriftDetectionDetails] = None
    StatusReason: Optional[str] = None
    StatusDetails: Optional[StackSetOperationStatusDetails] = None


# This class is the output for the 'validate_template' function.
class ValidateTemplateOutput(BaseValidatorModel):
    Parameters: List[TemplateParameter]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    DeclaredTransforms: List[str]
    ResponseMetadata: ResponseMetadata


class WarningDetail(BaseValidatorModel):
    Type: Optional[WarningTypeType] = None
    Properties: Optional[List[WarningProperty]] = None


# This class is the output for the 'list_stack_set_operation_results' function.
class ListStackSetOperationResultsOutput(BaseValidatorModel):
    Summaries: List[StackSetOperationResultSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_describe_type_configurations' function.
class BatchDescribeTypeConfigurationsOutput(BaseValidatorModel):
    Errors: List[BatchDescribeTypeConfigurationsError]
    UnprocessedTypeConfigurations: List[TypeConfigurationIdentifier]
    TypeConfigurations: List[TypeConfigurationDetails]
    ResponseMetadata: ResponseMetadata


class ChangeSetHook(BaseValidatorModel):
    InvocationPoint: Optional[Literal['PRE_PROVISION']] = None
    FailureMode: Optional[HookFailureModeType] = None
    TypeName: Optional[str] = None
    TypeVersionId: Optional[str] = None
    TypeConfigurationVersionId: Optional[str] = None
    TargetDetails: Optional[ChangeSetHookTargetDetails] = None


# This class is the output for the 'list_stack_sets' function.
class ListStackSetsOutput(BaseValidatorModel):
    Summaries: List[StackSetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_template_summary' function.
class GetTemplateSummaryOutput(BaseValidatorModel):
    Parameters: List[ParameterDeclaration]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    ResourceTypes: List[str]
    Version: str
    Metadata: str
    DeclaredTransforms: List[str]
    ResourceIdentifierSummaries: List[ResourceIdentifierSummary]
    Warnings: Warnings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_stack_instance_resource_drifts' function.
class ListStackInstanceResourceDriftsOutput(BaseValidatorModel):
    Summaries: List[StackInstanceResourceDriftsSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_stack_resource_drifts' function.
class DescribeStackResourceDriftsOutput(BaseValidatorModel):
    StackResourceDrifts: List[StackResourceDrift]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'detect_stack_resource_drift' function.
class DetectStackResourceDriftOutput(BaseValidatorModel):
    StackResourceDrift: StackResourceDrift
    ResponseMetadata: ResponseMetadata


class ResourceChange(BaseValidatorModel):
    PolicyAction: Optional[PolicyActionType] = None
    Action: Optional[ChangeActionType] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Replacement: Optional[ReplacementType] = None
    Scope: Optional[List[ResourceAttributeType]] = None
    Details: Optional[List[ResourceChangeDetail]] = None
    ChangeSetId: Optional[str] = None
    ModuleInfo: Optional[ModuleInfo] = None
    BeforeContext: Optional[str] = None
    AfterContext: Optional[str] = None


# This class is the input for the 'create_stack_refactor' function.
class CreateStackRefactorInput(BaseValidatorModel):
    StackDefinitions: List[StackDefinition]
    Description: Optional[str] = None
    EnableStackCreation: Optional[bool] = None
    ResourceMappings: Optional[List[ResourceMapping]] = None


class StackRefactorAction(BaseValidatorModel):
    Action: Optional[StackRefactorActionTypeType] = None
    Entity: Optional[StackRefactorActionEntityType] = None
    PhysicalResourceId: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    Description: Optional[str] = None
    Detection: Optional[StackRefactorDetectionType] = None
    DetectionReason: Optional[str] = None
    TagResources: Optional[List[Tag]] = None
    UntagResources: Optional[List[str]] = None
    ResourceMapping: Optional[ResourceMapping] = None


class Stack(BaseValidatorModel):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatusType
    StackId: Optional[str] = None
    ChangeSetId: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    DeletionTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    RollbackConfiguration: Optional[RollbackConfigurationOutput] = None
    StackStatusReason: Optional[str] = None
    DisableRollback: Optional[bool] = None
    NotificationARNs: Optional[List[str]] = None
    TimeoutInMinutes: Optional[int] = None
    Capabilities: Optional[List[CapabilityType]] = None
    Outputs: Optional[List[Output]] = None
    RoleARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    EnableTerminationProtection: Optional[bool] = None
    ParentId: Optional[str] = None
    RootId: Optional[str] = None
    DriftInformation: Optional[StackDriftInformation] = None
    RetainExceptOnCreate: Optional[bool] = None
    DeletionMode: Optional[DeletionModeType] = None
    DetailedStatus: Optional[DetailedStatusType] = None

RollbackConfigurationUnion = Union[RollbackConfiguration, RollbackConfigurationOutput]


# This class is the output for the 'list_stacks' function.
class ListStacksOutput(BaseValidatorModel):
    StackSummaries: List[StackSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_stack_instances' function.
class ListStackInstancesOutput(BaseValidatorModel):
    Summaries: List[StackInstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_stack_instance' function.
class DescribeStackInstanceOutput(BaseValidatorModel):
    StackInstance: StackInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stack_resource' function.
class DescribeStackResourceOutput(BaseValidatorModel):
    StackResourceDetail: StackResourceDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stack_resources' function.
class DescribeStackResourcesOutput(BaseValidatorModel):
    StackResources: List[StackResource]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_stack_resources' function.
class ListStackResourcesOutput(BaseValidatorModel):
    StackResourceSummaries: List[StackResourceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_stack_set' function.
class DescribeStackSetOutput(BaseValidatorModel):
    StackSet: StackSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_stack_instances' function.
class CreateStackInstancesInput(BaseValidatorModel):
    StackSetName: str
    Regions: List[str]
    Accounts: Optional[List[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsUnion] = None
    ParameterOverrides: Optional[List[Parameter]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesUnion] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'delete_stack_instances' function.
class DeleteStackInstancesInput(BaseValidatorModel):
    StackSetName: str
    Regions: List[str]
    RetainStacks: bool
    Accounts: Optional[List[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsUnion] = None
    OperationPreferences: Optional[StackSetOperationPreferencesUnion] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'detect_stack_set_drift' function.
class DetectStackSetDriftInput(BaseValidatorModel):
    StackSetName: str
    OperationPreferences: Optional[StackSetOperationPreferencesUnion] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'import_stacks_to_stack_set' function.
class ImportStacksToStackSetInput(BaseValidatorModel):
    StackSetName: str
    StackIds: Optional[List[str]] = None
    StackIdsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesUnion] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'update_stack_instances' function.
class UpdateStackInstancesInput(BaseValidatorModel):
    StackSetName: str
    Regions: List[str]
    Accounts: Optional[List[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsUnion] = None
    ParameterOverrides: Optional[List[Parameter]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesUnion] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None


# This class is the input for the 'update_stack_set' function.
class UpdateStackSetInput(BaseValidatorModel):
    StackSetName: str
    Description: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    Parameters: Optional[List[Parameter]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    Tags: Optional[List[Tag]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesUnion] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    DeploymentTargets: Optional[DeploymentTargetsUnion] = None
    PermissionModel: Optional[PermissionModelsType] = None
    AutoDeployment: Optional[AutoDeployment] = None
    OperationId: Optional[str] = None
    Accounts: Optional[List[str]] = None
    Regions: Optional[List[str]] = None
    CallAs: Optional[CallAsType] = None
    ManagedExecution: Optional[ManagedExecution] = None


# This class is the output for the 'list_stack_set_operations' function.
class ListStackSetOperationsOutput(BaseValidatorModel):
    Summaries: List[StackSetOperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_stack_set_operation' function.
class DescribeStackSetOperationOutput(BaseValidatorModel):
    StackSetOperation: StackSetOperation
    ResponseMetadata: ResponseMetadata


class ResourceDetail(BaseValidatorModel):
    ResourceType: Optional[str] = None
    LogicalResourceId: Optional[str] = None
    ResourceIdentifier: Optional[Dict[str, str]] = None
    ResourceStatus: Optional[GeneratedTemplateResourceStatusType] = None
    ResourceStatusReason: Optional[str] = None
    Warnings: Optional[List[WarningDetail]] = None


# This class is the output for the 'describe_change_set_hooks' function.
class DescribeChangeSetHooksOutput(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetName: str
    Hooks: List[ChangeSetHook]
    Status: ChangeSetHooksStatusType
    StackId: str
    StackName: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Change(BaseValidatorModel):
    Type: Optional[Literal['Resource']] = None
    HookInvocationCount: Optional[int] = None
    ResourceChange: Optional[ResourceChange] = None


# This class is the output for the 'list_stack_refactor_actions' function.
class ListStackRefactorActionsOutput(BaseValidatorModel):
    StackRefactorActions: List[StackRefactorAction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_stacks' function.
class DescribeStacksOutput(BaseValidatorModel):
    Stacks: List[Stack]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_change_set' function.
class CreateChangeSetInput(BaseValidatorModel):
    StackName: str
    ChangeSetName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    Parameters: Optional[List[Parameter]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    ResourceTypes: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    RollbackConfiguration: Optional[RollbackConfigurationUnion] = None
    NotificationARNs: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    ChangeSetType: Optional[ChangeSetTypeType] = None
    ResourcesToImport: Optional[List[ResourceToImport]] = None
    IncludeNestedStacks: Optional[bool] = None
    OnStackFailure: Optional[OnStackFailureType] = None
    ImportExistingResources: Optional[bool] = None


class CreateStackInputServiceResourceCreateStack(BaseValidatorModel):
    StackName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    DisableRollback: Optional[bool] = None
    RollbackConfiguration: Optional[RollbackConfigurationUnion] = None
    TimeoutInMinutes: Optional[int] = None
    NotificationARNs: Optional[List[str]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    ResourceTypes: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    OnFailure: Optional[OnFailureType] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None
    EnableTerminationProtection: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None


# This class is the input for the 'create_stack' function.
class CreateStackInput(BaseValidatorModel):
    StackName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    DisableRollback: Optional[bool] = None
    RollbackConfiguration: Optional[RollbackConfigurationUnion] = None
    TimeoutInMinutes: Optional[int] = None
    NotificationARNs: Optional[List[str]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    ResourceTypes: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    OnFailure: Optional[OnFailureType] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ClientRequestToken: Optional[str] = None
    EnableTerminationProtection: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None


class UpdateStackInputStackUpdate(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    StackPolicyDuringUpdateBody: Optional[str] = None
    StackPolicyDuringUpdateURL: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    ResourceTypes: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    RollbackConfiguration: Optional[RollbackConfigurationUnion] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    NotificationARNs: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    DisableRollback: Optional[bool] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None


# This class is the input for the 'update_stack' function.
class UpdateStackInput(BaseValidatorModel):
    StackName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    StackPolicyDuringUpdateBody: Optional[str] = None
    StackPolicyDuringUpdateURL: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    ResourceTypes: Optional[List[str]] = None
    RoleARN: Optional[str] = None
    RollbackConfiguration: Optional[RollbackConfigurationUnion] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    NotificationARNs: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    DisableRollback: Optional[bool] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None


# This class is the output for the 'describe_generated_template' function.
class DescribeGeneratedTemplateOutput(BaseValidatorModel):
    GeneratedTemplateId: str
    GeneratedTemplateName: str
    Resources: List[ResourceDetail]
    Status: GeneratedTemplateStatusType
    StatusReason: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    Progress: TemplateProgress
    StackId: str
    TemplateConfiguration: TemplateConfiguration
    TotalWarnings: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_change_set' function.
class DescribeChangeSetOutput(BaseValidatorModel):
    ChangeSetName: str
    ChangeSetId: str
    StackId: str
    StackName: str
    Description: str
    Parameters: List[Parameter]
    CreationTime: datetime
    ExecutionStatus: ExecutionStatusType
    Status: ChangeSetStatusType
    StatusReason: str
    NotificationARNs: List[str]
    RollbackConfiguration: RollbackConfigurationOutput
    Capabilities: List[CapabilityType]
    Tags: List[Tag]
    Changes: List[Change]
    IncludeNestedStacks: bool
    ParentChangeSetId: str
    RootChangeSetId: str
    OnStackFailure: OnStackFailureType
    ImportExistingResources: bool
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None