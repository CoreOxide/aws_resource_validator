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
from aws_resource_validator.pydantic_models.cloudformation_constants import *

class AccountGateResultTypeDef(BaseValidatorModel):
    Status: Optional[AccountGateStatusType] = None
    StatusReason: Optional[str] = None

class AccountLimitTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[int] = None

class LoggingConfigTypeDef(BaseValidatorModel):
    LogRoleArn: str
    LogGroupName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AutoDeploymentTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    RetainStacksOnAccountRemoval: Optional[bool] = None

class TypeConfigurationIdentifierTypeDef(BaseValidatorModel):
    TypeArn: Optional[str] = None
    TypeConfigurationAlias: Optional[str] = None
    TypeConfigurationArn: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    TypeName: Optional[str] = None

class TypeConfigurationDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Alias: Optional[str] = None
    Configuration: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    TypeArn: Optional[str] = None
    TypeName: Optional[str] = None
    IsDefaultConfiguration: Optional[bool] = None

class CancelUpdateStackInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    ClientRequestToken: Optional[str] = None

class CancelUpdateStackInputStackCancelUpdateTypeDef(BaseValidatorModel):
    ClientRequestToken: Optional[str] = None

class ChangeSetHookResourceTargetDetailsTypeDef(BaseValidatorModel):
    LogicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceAction: Optional[ChangeActionType] = None

class ChangeSetSummaryTypeDef(BaseValidatorModel):
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

class ContinueUpdateRollbackInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    RoleARN: Optional[str] = None
    ResourcesToSkip: Optional[Sequence[str]] = None
    ClientRequestToken: Optional[str] = None

class ParameterTypeDef(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    ParameterValue: Optional[str] = None
    UsePreviousValue: Optional[bool] = None
    ResolvedValue: Optional[str] = None

class ResourceToImportTypeDef(BaseValidatorModel):
    ResourceType: str
    LogicalResourceId: str
    ResourceIdentifier: Mapping[str, str]

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResourceDefinitionTypeDef(BaseValidatorModel):
    ResourceType: str
    ResourceIdentifier: Mapping[str, str]
    LogicalResourceId: Optional[str] = None

class TemplateConfigurationTypeDef(BaseValidatorModel):
    DeletionPolicy: Optional[GeneratedTemplateDeletionPolicyType] = None
    UpdateReplacePolicy: Optional[GeneratedTemplateUpdateReplacePolicyType] = None

class DeploymentTargetsTypeDef(BaseValidatorModel):
    Accounts: Optional[Sequence[str]] = None
    AccountsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    AccountFilterType: Optional[AccountFilterTypeType] = None

class StackSetOperationPreferencesTypeDef(BaseValidatorModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[Sequence[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None

class ManagedExecutionTypeDef(BaseValidatorModel):
    Active: Optional[bool] = None

class DeactivateTypeInputRequestTypeDef(BaseValidatorModel):
    TypeName: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    Arn: Optional[str] = None

class DeleteChangeSetInputRequestTypeDef(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None

class DeleteGeneratedTemplateInputRequestTypeDef(BaseValidatorModel):
    GeneratedTemplateName: str

class DeleteStackInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    RetainResources: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DeletionMode: Optional[DeletionModeType] = None

class DeleteStackInputStackDeleteTypeDef(BaseValidatorModel):
    RetainResources: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DeletionMode: Optional[DeletionModeType] = None

class DeleteStackSetInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None

class DeploymentTargetsOutputTypeDef(BaseValidatorModel):
    Accounts: Optional[List[str]] = None
    AccountsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    AccountFilterType: Optional[AccountFilterTypeType] = None

class DeregisterTypeInputRequestTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccountLimitsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class DescribeChangeSetHooksInputRequestTypeDef(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    LogicalResourceId: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeChangeSetInputRequestTypeDef(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None

class DescribeGeneratedTemplateInputRequestTypeDef(BaseValidatorModel):
    GeneratedTemplateName: str

class TemplateProgressTypeDef(BaseValidatorModel):
    ResourcesSucceeded: Optional[int] = None
    ResourcesFailed: Optional[int] = None
    ResourcesProcessing: Optional[int] = None
    ResourcesPending: Optional[int] = None

class DescribeOrganizationsAccessInputRequestTypeDef(BaseValidatorModel):
    CallAs: Optional[CallAsType] = None

class DescribePublisherInputRequestTypeDef(BaseValidatorModel):
    PublisherId: Optional[str] = None

class DescribeResourceScanInputRequestTypeDef(BaseValidatorModel):
    ResourceScanId: str

class DescribeStackDriftDetectionStatusInputRequestTypeDef(BaseValidatorModel):
    StackDriftDetectionId: str

class DescribeStackEventsInputRequestTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None

class StackEventTypeDef(BaseValidatorModel):
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
    HookInvocationPoint: Optional[Literal["PRE_PROVISION"]] = None
    HookFailureMode: Optional[HookFailureModeType] = None
    DetailedStatus: Optional[DetailedStatusType] = None

class DescribeStackInstanceInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    CallAs: Optional[CallAsType] = None

class DescribeStackResourceDriftsInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    StackResourceDriftStatusFilters: Optional[Sequence[StackResourceDriftStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeStackResourceInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str

class DescribeStackResourcesInputRequestTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None

class DescribeStackSetInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None

class DescribeStackSetOperationInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None

class DescribeStacksInputRequestTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None

class DescribeTypeInputRequestTypeDef(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    Arn: Optional[str] = None
    VersionId: Optional[str] = None
    PublisherId: Optional[str] = None
    PublicVersionNumber: Optional[str] = None

class RequiredActivatedTypeTypeDef(BaseValidatorModel):
    TypeNameAlias: Optional[str] = None
    OriginalTypeName: Optional[str] = None
    PublisherId: Optional[str] = None
    SupportedMajorVersions: Optional[List[int]] = None

class DescribeTypeRegistrationInputRequestTypeDef(BaseValidatorModel):
    RegistrationToken: str

class DetectStackDriftInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    LogicalResourceIds: Optional[Sequence[str]] = None

class DetectStackResourceDriftInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str

class ExecuteChangeSetInputRequestTypeDef(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DisableRollback: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None

class ExportTypeDef(BaseValidatorModel):
    ExportingStackId: Optional[str] = None
    Name: Optional[str] = None
    Value: Optional[str] = None

class GetGeneratedTemplateInputRequestTypeDef(BaseValidatorModel):
    GeneratedTemplateName: str
    Format: Optional[TemplateFormatType] = None

class GetStackPolicyInputRequestTypeDef(BaseValidatorModel):
    StackName: str

class GetTemplateInputRequestTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    ChangeSetName: Optional[str] = None
    TemplateStage: Optional[TemplateStageType] = None

class TemplateSummaryConfigTypeDef(BaseValidatorModel):
    TreatUnrecognizedResourceTypesAsWarnings: Optional[bool] = None

class ResourceIdentifierSummaryTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    LogicalResourceIds: Optional[List[str]] = None
    ResourceIdentifiers: Optional[List[str]] = None

class WarningsTypeDef(BaseValidatorModel):
    UnrecognizedResourceTypes: Optional[List[str]] = None

class ListChangeSetsInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    NextToken: Optional[str] = None

class ListExportsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class ListGeneratedTemplatesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TemplateSummaryTypeDef(BaseValidatorModel):
    GeneratedTemplateId: Optional[str] = None
    GeneratedTemplateName: Optional[str] = None
    Status: Optional[GeneratedTemplateStatusType] = None
    StatusReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    NumberOfResources: Optional[int] = None

class ListImportsInputRequestTypeDef(BaseValidatorModel):
    ExportName: str
    NextToken: Optional[str] = None

class ScannedResourceIdentifierTypeDef(BaseValidatorModel):
    ResourceType: str
    ResourceIdentifier: Mapping[str, str]

class ScannedResourceTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceIdentifier: Optional[Dict[str, str]] = None
    ManagedByStack: Optional[bool] = None

class ListResourceScanResourcesInputRequestTypeDef(BaseValidatorModel):
    ResourceScanId: str
    ResourceIdentifier: Optional[str] = None
    ResourceTypePrefix: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourceScansInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResourceScanSummaryTypeDef(BaseValidatorModel):
    ResourceScanId: Optional[str] = None
    Status: Optional[ResourceScanStatusType] = None
    StatusReason: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    PercentageCompleted: Optional[float] = None

class ListStackInstanceResourceDriftsInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    OperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StackInstanceResourceDriftStatuses: Optional[Sequence[StackResourceDriftStatusType]] = None
    CallAs: Optional[CallAsType] = None

class StackInstanceFilterTypeDef(BaseValidatorModel):
    Name: Optional[StackInstanceFilterNameType] = None
    Values: Optional[str] = None

class ListStackResourcesInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    NextToken: Optional[str] = None

class ListStackSetAutoDeploymentTargetsInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None

class StackSetAutoDeploymentTargetSummaryTypeDef(BaseValidatorModel):
    OrganizationalUnitId: Optional[str] = None
    Regions: Optional[List[str]] = None

class OperationResultFilterTypeDef(BaseValidatorModel):
    Name: Optional[Literal["OPERATION_RESULT_STATUS"]] = None
    Values: Optional[str] = None

class ListStackSetOperationsInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None

class ListStackSetsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[StackSetStatusType] = None
    CallAs: Optional[CallAsType] = None

class ListStacksInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    StackStatusFilter: Optional[Sequence[StackStatusType]] = None

class ListTypeRegistrationsInputRequestTypeDef(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    TypeArn: Optional[str] = None
    RegistrationStatusFilter: Optional[RegistrationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTypeVersionsInputRequestTypeDef(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    Arn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    PublisherId: Optional[str] = None

class TypeVersionSummaryTypeDef(BaseValidatorModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    Arn: Optional[str] = None
    TimeCreated: Optional[datetime] = None
    Description: Optional[str] = None
    PublicVersionNumber: Optional[str] = None

class TypeFiltersTypeDef(BaseValidatorModel):
    Category: Optional[CategoryType] = None
    PublisherId: Optional[str] = None
    TypeNamePrefix: Optional[str] = None

class TypeSummaryTypeDef(BaseValidatorModel):
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

class ModuleInfoTypeDef(BaseValidatorModel):
    TypeHierarchy: Optional[str] = None
    LogicalIdHierarchy: Optional[str] = None

class OutputTypeDef(BaseValidatorModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None
    ExportName: Optional[str] = None

class ParameterConstraintsTypeDef(BaseValidatorModel):
    AllowedValues: Optional[List[str]] = None

class PhysicalResourceIdContextKeyValuePairTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class PropertyDifferenceTypeDef(BaseValidatorModel):
    PropertyPath: str
    ExpectedValue: str
    ActualValue: str
    DifferenceType: DifferenceTypeType

class PublishTypeInputRequestTypeDef(BaseValidatorModel):
    Type: Optional[ThirdPartyTypeType] = None
    Arn: Optional[str] = None
    TypeName: Optional[str] = None
    PublicVersionNumber: Optional[str] = None

class RecordHandlerProgressInputRequestTypeDef(BaseValidatorModel):
    BearerToken: str
    OperationStatus: OperationStatusType
    CurrentOperationStatus: Optional[OperationStatusType] = None
    StatusMessage: Optional[str] = None
    ErrorCode: Optional[HandlerErrorCodeType] = None
    ResourceModel: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class RegisterPublisherInputRequestTypeDef(BaseValidatorModel):
    AcceptTermsAndConditions: Optional[bool] = None
    ConnectionArn: Optional[str] = None

class ResourceTargetDefinitionTypeDef(BaseValidatorModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None
    Path: Optional[str] = None
    BeforeValue: Optional[str] = None
    AfterValue: Optional[str] = None
    AttributeChangeType: Optional[AttributeChangeTypeType] = None

class RollbackTriggerTypeDef(BaseValidatorModel):
    Arn: str
    Type: str

class RollbackStackInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None

class SetStackPolicyInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None

class SetTypeConfigurationInputRequestTypeDef(BaseValidatorModel):
    Configuration: str
    TypeArn: Optional[str] = None
    ConfigurationAlias: Optional[str] = None
    TypeName: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None

class SetTypeDefaultVersionInputRequestTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None

class SignalResourceInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    LogicalResourceId: str
    UniqueId: str
    Status: ResourceSignalStatusType

class StackDriftInformationSummaryTypeDef(BaseValidatorModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackDriftInformationTypeDef(BaseValidatorModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackInstanceComprehensiveStatusTypeDef(BaseValidatorModel):
    DetailedStatus: Optional[StackInstanceDetailedStatusType] = None

class StackResourceDriftInformationTypeDef(BaseValidatorModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackResourceDriftInformationSummaryTypeDef(BaseValidatorModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackSetDriftDetectionDetailsTypeDef(BaseValidatorModel):
    DriftStatus: Optional[StackSetDriftStatusType] = None
    DriftDetectionStatus: Optional[StackSetDriftDetectionStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    TotalStackInstancesCount: Optional[int] = None
    DriftedStackInstancesCount: Optional[int] = None
    InSyncStackInstancesCount: Optional[int] = None
    InProgressStackInstancesCount: Optional[int] = None
    FailedStackInstancesCount: Optional[int] = None

class StackSetOperationPreferencesExtraOutputTypeDef(BaseValidatorModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[List[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None

class StackSetOperationPreferencesOutputTypeDef(BaseValidatorModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[List[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None

class StackSetOperationStatusDetailsTypeDef(BaseValidatorModel):
    FailedStackInstancesCount: Optional[int] = None

class StartResourceScanInputRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: Optional[str] = None

class StopStackSetOperationInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None

class TemplateParameterTypeDef(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    NoEcho: Optional[bool] = None
    Description: Optional[str] = None

class TestTypeInputRequestTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None
    LogDeliveryBucket: Optional[str] = None

class UpdateTerminationProtectionInputRequestTypeDef(BaseValidatorModel):
    EnableTerminationProtection: bool
    StackName: str

class ValidateTemplateInputRequestTypeDef(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None

class WarningPropertyTypeDef(BaseValidatorModel):
    PropertyPath: Optional[str] = None
    Required: Optional[bool] = None
    Description: Optional[str] = None

class StackSetOperationResultSummaryTypeDef(BaseValidatorModel):
    Account: Optional[str] = None
    Region: Optional[str] = None
    Status: Optional[StackSetOperationResultStatusType] = None
    StatusReason: Optional[str] = None
    AccountGateResult: Optional[AccountGateResultTypeDef] = None
    OrganizationalUnitId: Optional[str] = None

class ActivateTypeInputRequestTypeDef(BaseValidatorModel):
    Type: Optional[ThirdPartyTypeType] = None
    PublicTypeArn: Optional[str] = None
    PublisherId: Optional[str] = None
    TypeName: Optional[str] = None
    TypeNameAlias: Optional[str] = None
    AutoUpdate: Optional[bool] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    VersionBump: Optional[VersionBumpType] = None
    MajorVersion: Optional[int] = None

class RegisterTypeInputRequestTypeDef(BaseValidatorModel):
    TypeName: str
    SchemaHandlerPackage: str
    Type: Optional[RegistryTypeType] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class ActivateTypeOutputTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChangeSetOutputTypeDef(BaseValidatorModel):
    Id: str
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGeneratedTemplateOutputTypeDef(BaseValidatorModel):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackInstancesOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackOutputTypeDef(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackSetOutputTypeDef(BaseValidatorModel):
    StackSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStackInstancesOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountLimitsOutputTypeDef(BaseValidatorModel):
    AccountLimits: List[AccountLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrganizationsAccessOutputTypeDef(BaseValidatorModel):
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePublisherOutputTypeDef(BaseValidatorModel):
    PublisherId: str
    PublisherStatus: PublisherStatusType
    IdentityProvider: IdentityProviderType
    PublisherProfile: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceScanOutputTypeDef(BaseValidatorModel):
    ResourceScanId: str
    Status: ResourceScanStatusType
    StatusReason: str
    StartTime: datetime
    EndTime: datetime
    PercentageCompleted: float
    ResourceTypes: List[str]
    ResourcesScanned: int
    ResourcesRead: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackDriftDetectionStatusOutputTypeDef(BaseValidatorModel):
    StackId: str
    StackDriftDetectionId: str
    StackDriftStatus: StackDriftStatusType
    DetectionStatus: StackDriftDetectionStatusType
    DetectionStatusReason: str
    DriftedStackResourceCount: int
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTypeRegistrationOutputTypeDef(BaseValidatorModel):
    ProgressStatus: RegistrationStatusType
    Description: str
    TypeArn: str
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectStackDriftOutputTypeDef(BaseValidatorModel):
    StackDriftDetectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectStackSetDriftOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EstimateTemplateCostOutputTypeDef(BaseValidatorModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeneratedTemplateOutputTypeDef(BaseValidatorModel):
    Status: GeneratedTemplateStatusType
    TemplateBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStackPolicyOutputTypeDef(BaseValidatorModel):
    StackPolicyBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateOutputTypeDef(BaseValidatorModel):
    TemplateBody: Dict[str, Any]
    StagesAvailable: List["TemplateStageType"]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportStacksToStackSetOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportsOutputTypeDef(BaseValidatorModel):
    Imports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTypeRegistrationsOutputTypeDef(BaseValidatorModel):
    RegistrationTokenList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModuleInfoResponseTypeDef(BaseValidatorModel):
    TypeHierarchy: str
    LogicalIdHierarchy: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishTypeOutputTypeDef(BaseValidatorModel):
    PublicTypeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterPublisherOutputTypeDef(BaseValidatorModel):
    PublisherId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTypeOutputTypeDef(BaseValidatorModel):
    RegistrationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackStackOutputTypeDef(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetTypeConfigurationOutputTypeDef(BaseValidatorModel):
    ConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StackDriftInformationResponseTypeDef(BaseValidatorModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StackResourceDriftInformationResponseTypeDef(BaseValidatorModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StackResourceDriftInformationSummaryResponseTypeDef(BaseValidatorModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceScanOutputTypeDef(BaseValidatorModel):
    ResourceScanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestTypeOutputTypeDef(BaseValidatorModel):
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeneratedTemplateOutputTypeDef(BaseValidatorModel):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackInstancesOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackOutputTypeDef(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackSetOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTerminationProtectionOutputTypeDef(BaseValidatorModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDescribeTypeConfigurationsErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    TypeConfigurationIdentifier: Optional[TypeConfigurationIdentifierTypeDef] = None

class BatchDescribeTypeConfigurationsInputRequestTypeDef(BaseValidatorModel):
    TypeConfigurationIdentifiers: Sequence[TypeConfigurationIdentifierTypeDef]

class ChangeSetHookTargetDetailsTypeDef(BaseValidatorModel):
    TargetType: Optional[Literal["RESOURCE"]] = None
    ResourceTargetDetails: Optional[ChangeSetHookResourceTargetDetailsTypeDef] = None

class ListChangeSetsOutputTypeDef(BaseValidatorModel):
    Summaries: List[ChangeSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EstimateTemplateCostInputRequestTypeDef(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class CreateGeneratedTemplateInputRequestTypeDef(BaseValidatorModel):
    GeneratedTemplateName: str
    Resources: Optional[Sequence[ResourceDefinitionTypeDef]] = None
    StackName: Optional[str] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None

class UpdateGeneratedTemplateInputRequestTypeDef(BaseValidatorModel):
    GeneratedTemplateName: str
    NewGeneratedTemplateName: Optional[str] = None
    AddResources: Optional[Sequence[ResourceDefinitionTypeDef]] = None
    RemoveResources: Optional[Sequence[str]] = None
    RefreshAllResources: Optional[bool] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None

class CreateStackInstancesInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    Regions: Sequence[str]
    Accounts: Optional[Sequence[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    ParameterOverrides: Optional[Sequence[ParameterTypeDef]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class DeleteStackInstancesInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    Regions: Sequence[str]
    RetainStacks: bool
    Accounts: Optional[Sequence[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class DetectStackSetDriftInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class ImportStacksToStackSetInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    StackIds: Optional[Sequence[str]] = None
    StackIdsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class UpdateStackInstancesInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    Regions: Sequence[str]
    Accounts: Optional[Sequence[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    ParameterOverrides: Optional[Sequence[ParameterTypeDef]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class CreateStackSetInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    Description: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    StackId: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    PermissionModel: Optional[PermissionModelsType] = None
    AutoDeployment: Optional[AutoDeploymentTypeDef] = None
    CallAs: Optional[CallAsType] = None
    ClientRequestToken: Optional[str] = None
    ManagedExecution: Optional[ManagedExecutionTypeDef] = None

class StackSetSummaryTypeDef(BaseValidatorModel):
    StackSetName: Optional[str] = None
    StackSetId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[StackSetStatusType] = None
    AutoDeployment: Optional[AutoDeploymentTypeDef] = None
    PermissionModel: Optional[PermissionModelsType] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    ManagedExecution: Optional[ManagedExecutionTypeDef] = None

class UpdateStackSetInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    Description: Optional[str] = None
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    PermissionModel: Optional[PermissionModelsType] = None
    AutoDeployment: Optional[AutoDeploymentTypeDef] = None
    OperationId: Optional[str] = None
    Accounts: Optional[Sequence[str]] = None
    Regions: Optional[Sequence[str]] = None
    CallAs: Optional[CallAsType] = None
    ManagedExecution: Optional[ManagedExecutionTypeDef] = None

class DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeChangeSetInputDescribeChangeSetPaginateTypeDef(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStackEventsInputDescribeStackEventsPaginateTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStacksInputDescribeStacksPaginateTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChangeSetsInputListChangeSetsPaginateTypeDef(BaseValidatorModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportsInputListExportsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGeneratedTemplatesInputListGeneratedTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportsInputListImportsPaginateTypeDef(BaseValidatorModel):
    ExportName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceScanResourcesInputListResourceScanResourcesPaginateTypeDef(BaseValidatorModel):
    ResourceScanId: str
    ResourceIdentifier: Optional[str] = None
    ResourceTypePrefix: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceScansInputListResourceScansPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackResourcesInputListStackResourcesPaginateTypeDef(BaseValidatorModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackSetOperationsInputListStackSetOperationsPaginateTypeDef(BaseValidatorModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackSetsInputListStackSetsPaginateTypeDef(BaseValidatorModel):
    Status: Optional[StackSetStatusType] = None
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStacksInputListStacksPaginateTypeDef(BaseValidatorModel):
    StackStatusFilter: Optional[Sequence[StackStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeChangeSetInputChangeSetCreateCompleteWaitTypeDef(BaseValidatorModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackCreateCompleteWaitTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackDeleteCompleteWaitTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackExistsWaitTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackImportCompleteWaitTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackRollbackCompleteWaitTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackUpdateCompleteWaitTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTypeRegistrationInputTypeRegistrationCompleteWaitTypeDef(BaseValidatorModel):
    RegistrationToken: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStackEventsOutputTypeDef(BaseValidatorModel):
    StackEvents: List[StackEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTypeOutputTypeDef(BaseValidatorModel):
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
    LoggingConfig: LoggingConfigTypeDef
    RequiredActivatedTypes: List[RequiredActivatedTypeTypeDef]
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListExportsOutputTypeDef(BaseValidatorModel):
    Exports: List[ExportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTemplateSummaryInputRequestTypeDef(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    StackName: Optional[str] = None
    StackSetName: Optional[str] = None
    CallAs: Optional[CallAsType] = None
    TemplateSummaryConfig: Optional[TemplateSummaryConfigTypeDef] = None

class ListGeneratedTemplatesOutputTypeDef(BaseValidatorModel):
    Summaries: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceScanRelatedResourcesInputListResourceScanRelatedResourcesPaginateTypeDef(BaseValidatorModel):
    ResourceScanId: str
    Resources: Sequence[ScannedResourceIdentifierTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceScanRelatedResourcesInputRequestTypeDef(BaseValidatorModel):
    ResourceScanId: str
    Resources: Sequence[ScannedResourceIdentifierTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourceScanRelatedResourcesOutputTypeDef(BaseValidatorModel):
    RelatedResources: List[ScannedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceScanResourcesOutputTypeDef(BaseValidatorModel):
    Resources: List[ScannedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceScansOutputTypeDef(BaseValidatorModel):
    ResourceScanSummaries: List[ResourceScanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStackInstancesInputListStackInstancesPaginateTypeDef(BaseValidatorModel):
    StackSetName: str
    Filters: Optional[Sequence[StackInstanceFilterTypeDef]] = None
    StackInstanceAccount: Optional[str] = None
    StackInstanceRegion: Optional[str] = None
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackInstancesInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[StackInstanceFilterTypeDef]] = None
    StackInstanceAccount: Optional[str] = None
    StackInstanceRegion: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class ListStackSetAutoDeploymentTargetsOutputTypeDef(BaseValidatorModel):
    Summaries: List[StackSetAutoDeploymentTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStackSetOperationResultsInputListStackSetOperationResultsPaginateTypeDef(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None
    Filters: Optional[Sequence[OperationResultFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackSetOperationResultsInputRequestTypeDef(BaseValidatorModel):
    StackSetName: str
    OperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None
    Filters: Optional[Sequence[OperationResultFilterTypeDef]] = None

class ListTypeVersionsOutputTypeDef(BaseValidatorModel):
    TypeVersionSummaries: List[TypeVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTypesInputListTypesPaginateTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    Type: Optional[RegistryTypeType] = None
    Filters: Optional[TypeFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypesInputRequestTypeDef(BaseValidatorModel):
    Visibility: Optional[VisibilityType] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    Type: Optional[RegistryTypeType] = None
    Filters: Optional[TypeFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTypesOutputTypeDef(BaseValidatorModel):
    TypeSummaries: List[TypeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ParameterDeclarationTypeDef(BaseValidatorModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    ParameterType: Optional[str] = None
    NoEcho: Optional[bool] = None
    Description: Optional[str] = None
    ParameterConstraints: Optional[ParameterConstraintsTypeDef] = None

class StackInstanceResourceDriftsSummaryTypeDef(BaseValidatorModel):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: Optional[str] = None
    PhysicalResourceIdContext: Optional[       List[PhysicalResourceIdContextKeyValuePairTypeDef]     ] = None
    PropertyDifferences: Optional[List[PropertyDifferenceTypeDef]] = None

class StackResourceDriftTypeDef(BaseValidatorModel):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: Optional[str] = None
    PhysicalResourceIdContext: Optional[       List[PhysicalResourceIdContextKeyValuePairTypeDef]     ] = None
    ExpectedProperties: Optional[str] = None
    ActualProperties: Optional[str] = None
    PropertyDifferences: Optional[List[PropertyDifferenceTypeDef]] = None
    ModuleInfo: Optional[ModuleInfoTypeDef] = None

class ResourceChangeDetailTypeDef(BaseValidatorModel):
    Target: Optional[ResourceTargetDefinitionTypeDef] = None
    Evaluation: Optional[EvaluationTypeType] = None
    ChangeSource: Optional[ChangeSourceType] = None
    CausingEntity: Optional[str] = None

class RollbackConfigurationExtraOutputTypeDef(BaseValidatorModel):
    RollbackTriggers: Optional[List[RollbackTriggerTypeDef]] = None
    MonitoringTimeInMinutes: Optional[int] = None

class RollbackConfigurationOutputTypeDef(BaseValidatorModel):
    RollbackTriggers: Optional[List[RollbackTriggerTypeDef]] = None
    MonitoringTimeInMinutes: Optional[int] = None

class RollbackConfigurationResponseTypeDef(BaseValidatorModel):
    RollbackTriggers: List[RollbackTriggerTypeDef]
    MonitoringTimeInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackConfigurationTypeDef(BaseValidatorModel):
    RollbackTriggers: Optional[Sequence[RollbackTriggerTypeDef]] = None
    MonitoringTimeInMinutes: Optional[int] = None

class StackSummaryTypeDef(BaseValidatorModel):
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
    DriftInformation: Optional[StackDriftInformationSummaryTypeDef] = None

class StackInstanceSummaryTypeDef(BaseValidatorModel):
    StackSetId: Optional[str] = None
    Region: Optional[str] = None
    Account: Optional[str] = None
    StackId: Optional[str] = None
    Status: Optional[StackInstanceStatusType] = None
    StatusReason: Optional[str] = None
    StackInstanceStatus: Optional[StackInstanceComprehensiveStatusTypeDef] = None
    OrganizationalUnitId: Optional[str] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    LastOperationId: Optional[str] = None

class StackInstanceTypeDef(BaseValidatorModel):
    StackSetId: Optional[str] = None
    Region: Optional[str] = None
    Account: Optional[str] = None
    StackId: Optional[str] = None
    ParameterOverrides: Optional[List[ParameterTypeDef]] = None
    Status: Optional[StackInstanceStatusType] = None
    StackInstanceStatus: Optional[StackInstanceComprehensiveStatusTypeDef] = None
    StatusReason: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    LastOperationId: Optional[str] = None

class StackResourceDetailTypeDef(BaseValidatorModel):
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
    DriftInformation: Optional[StackResourceDriftInformationTypeDef] = None
    ModuleInfo: Optional[ModuleInfoTypeDef] = None

class StackResourceTypeDef(BaseValidatorModel):
    LogicalResourceId: str
    ResourceType: str
    Timestamp: datetime
    ResourceStatus: ResourceStatusType
    StackName: Optional[str] = None
    StackId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceStatusReason: Optional[str] = None
    Description: Optional[str] = None
    DriftInformation: Optional[StackResourceDriftInformationTypeDef] = None
    ModuleInfo: Optional[ModuleInfoTypeDef] = None

class StackResourceSummaryTypeDef(BaseValidatorModel):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatusType
    PhysicalResourceId: Optional[str] = None
    ResourceStatusReason: Optional[str] = None
    DriftInformation: Optional[StackResourceDriftInformationSummaryTypeDef] = None
    ModuleInfo: Optional[ModuleInfoTypeDef] = None

class StackSetTypeDef(BaseValidatorModel):
    StackSetName: Optional[str] = None
    StackSetId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[StackSetStatusType] = None
    TemplateBody: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None
    Capabilities: Optional[List[CapabilityType]] = None
    Tags: Optional[List[TagTypeDef]] = None
    StackSetARN: Optional[str] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    StackSetDriftDetectionDetails: Optional[StackSetDriftDetectionDetailsTypeDef] = None
    AutoDeployment: Optional[AutoDeploymentTypeDef] = None
    PermissionModel: Optional[PermissionModelsType] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    ManagedExecution: Optional[ManagedExecutionTypeDef] = None
    Regions: Optional[List[str]] = None

class StackSetOperationSummaryTypeDef(BaseValidatorModel):
    OperationId: Optional[str] = None
    Action: Optional[StackSetOperationActionType] = None
    Status: Optional[StackSetOperationStatusType] = None
    CreationTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    StatusReason: Optional[str] = None
    StatusDetails: Optional[StackSetOperationStatusDetailsTypeDef] = None
    OperationPreferences: Optional[StackSetOperationPreferencesOutputTypeDef] = None

class StackSetOperationTypeDef(BaseValidatorModel):
    OperationId: Optional[str] = None
    StackSetId: Optional[str] = None
    Action: Optional[StackSetOperationActionType] = None
    Status: Optional[StackSetOperationStatusType] = None
    OperationPreferences: Optional[StackSetOperationPreferencesOutputTypeDef] = None
    RetainStacks: Optional[bool] = None
    AdministrationRoleARN: Optional[str] = None
    ExecutionRoleName: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    DeploymentTargets: Optional[DeploymentTargetsOutputTypeDef] = None
    StackSetDriftDetectionDetails: Optional[StackSetDriftDetectionDetailsTypeDef] = None
    StatusReason: Optional[str] = None
    StatusDetails: Optional[StackSetOperationStatusDetailsTypeDef] = None

class ValidateTemplateOutputTypeDef(BaseValidatorModel):
    Parameters: List[TemplateParameterTypeDef]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    DeclaredTransforms: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class WarningDetailTypeDef(BaseValidatorModel):
    Type: Optional[WarningTypeType] = None
    Properties: Optional[List[WarningPropertyTypeDef]] = None

class ListStackSetOperationResultsOutputTypeDef(BaseValidatorModel):
    Summaries: List[StackSetOperationResultSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchDescribeTypeConfigurationsOutputTypeDef(BaseValidatorModel):
    Errors: List[BatchDescribeTypeConfigurationsErrorTypeDef]
    UnprocessedTypeConfigurations: List[TypeConfigurationIdentifierTypeDef]
    TypeConfigurations: List[TypeConfigurationDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeSetHookTypeDef(BaseValidatorModel):
    InvocationPoint: Optional[Literal["PRE_PROVISION"]] = None
    FailureMode: Optional[HookFailureModeType] = None
    TypeName: Optional[str] = None
    TypeVersionId: Optional[str] = None
    TypeConfigurationVersionId: Optional[str] = None
    TargetDetails: Optional[ChangeSetHookTargetDetailsTypeDef] = None

class ListStackSetsOutputTypeDef(BaseValidatorModel):
    Summaries: List[StackSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTemplateSummaryOutputTypeDef(BaseValidatorModel):
    Parameters: List[ParameterDeclarationTypeDef]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    ResourceTypes: List[str]
    Version: str
    Metadata: str
    DeclaredTransforms: List[str]
    ResourceIdentifierSummaries: List[ResourceIdentifierSummaryTypeDef]
    Warnings: WarningsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackInstanceResourceDriftsOutputTypeDef(BaseValidatorModel):
    Summaries: List[StackInstanceResourceDriftsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackResourceDriftsOutputTypeDef(BaseValidatorModel):
    StackResourceDrifts: List[StackResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetectStackResourceDriftOutputTypeDef(BaseValidatorModel):
    StackResourceDrift: StackResourceDriftTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceChangeTypeDef(BaseValidatorModel):
    PolicyAction: Optional[PolicyActionType] = None
    Action: Optional[ChangeActionType] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    Replacement: Optional[ReplacementType] = None
    Scope: Optional[List[ResourceAttributeType]] = None
    Details: Optional[List[ResourceChangeDetailTypeDef]] = None
    ChangeSetId: Optional[str] = None
    ModuleInfo: Optional[ModuleInfoTypeDef] = None
    BeforeContext: Optional[str] = None
    AfterContext: Optional[str] = None

class StackTypeDef(BaseValidatorModel):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatusType
    StackId: Optional[str] = None
    ChangeSetId: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None
    DeletionTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    RollbackConfiguration: Optional[RollbackConfigurationOutputTypeDef] = None
    StackStatusReason: Optional[str] = None
    DisableRollback: Optional[bool] = None
    NotificationARNs: Optional[List[str]] = None
    TimeoutInMinutes: Optional[int] = None
    Capabilities: Optional[List[CapabilityType]] = None
    Outputs: Optional[List[OutputTypeDef]] = None
    RoleARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    EnableTerminationProtection: Optional[bool] = None
    ParentId: Optional[str] = None
    RootId: Optional[str] = None
    DriftInformation: Optional[StackDriftInformationTypeDef] = None
    RetainExceptOnCreate: Optional[bool] = None
    DeletionMode: Optional[DeletionModeType] = None
    DetailedStatus: Optional[DetailedStatusType] = None

class CreateChangeSetInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    ChangeSetName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    RollbackConfiguration: Optional[RollbackConfigurationTypeDef] = None
    NotificationARNs: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    ChangeSetType: Optional[ChangeSetTypeType] = None
    ResourcesToImport: Optional[Sequence[ResourceToImportTypeDef]] = None
    IncludeNestedStacks: Optional[bool] = None
    OnStackFailure: Optional[OnStackFailureType] = None
    ImportExistingResources: Optional[bool] = None

class CreateStackInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    DisableRollback: Optional[bool] = None
    RollbackConfiguration: Optional[RollbackConfigurationTypeDef] = None
    TimeoutInMinutes: Optional[int] = None
    NotificationARNs: Optional[Sequence[str]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    OnFailure: Optional[OnFailureType] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    EnableTerminationProtection: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None

class CreateStackInputServiceResourceCreateStackTypeDef(BaseValidatorModel):
    StackName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    DisableRollback: Optional[bool] = None
    RollbackConfiguration: Optional[RollbackConfigurationTypeDef] = None
    TimeoutInMinutes: Optional[int] = None
    NotificationARNs: Optional[Sequence[str]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    OnFailure: Optional[OnFailureType] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None
    EnableTerminationProtection: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None

class UpdateStackInputRequestTypeDef(BaseValidatorModel):
    StackName: str
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    StackPolicyDuringUpdateBody: Optional[str] = None
    StackPolicyDuringUpdateURL: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    RollbackConfiguration: Optional[RollbackConfigurationTypeDef] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    NotificationARNs: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DisableRollback: Optional[bool] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None

class UpdateStackInputStackUpdateTypeDef(BaseValidatorModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    UsePreviousTemplate: Optional[bool] = None
    StackPolicyDuringUpdateBody: Optional[str] = None
    StackPolicyDuringUpdateURL: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None
    Capabilities: Optional[Sequence[CapabilityType]] = None
    ResourceTypes: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    RollbackConfiguration: Optional[RollbackConfigurationTypeDef] = None
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None
    NotificationARNs: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DisableRollback: Optional[bool] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None

class ListStacksOutputTypeDef(BaseValidatorModel):
    StackSummaries: List[StackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStackInstancesOutputTypeDef(BaseValidatorModel):
    Summaries: List[StackInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackInstanceOutputTypeDef(BaseValidatorModel):
    StackInstance: StackInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackResourceOutputTypeDef(BaseValidatorModel):
    StackResourceDetail: StackResourceDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackResourcesOutputTypeDef(BaseValidatorModel):
    StackResources: List[StackResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackResourcesOutputTypeDef(BaseValidatorModel):
    StackResourceSummaries: List[StackResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackSetOutputTypeDef(BaseValidatorModel):
    StackSet: StackSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackSetOperationsOutputTypeDef(BaseValidatorModel):
    Summaries: List[StackSetOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackSetOperationOutputTypeDef(BaseValidatorModel):
    StackSetOperation: StackSetOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDetailTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    LogicalResourceId: Optional[str] = None
    ResourceIdentifier: Optional[Dict[str, str]] = None
    ResourceStatus: Optional[GeneratedTemplateResourceStatusType] = None
    ResourceStatusReason: Optional[str] = None
    Warnings: Optional[List[WarningDetailTypeDef]] = None

class DescribeChangeSetHooksOutputTypeDef(BaseValidatorModel):
    ChangeSetId: str
    ChangeSetName: str
    Hooks: List[ChangeSetHookTypeDef]
    Status: ChangeSetHooksStatusType
    StackId: str
    StackName: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ChangeTypeDef(BaseValidatorModel):
    Type: Optional[Literal["Resource"]] = None
    HookInvocationCount: Optional[int] = None
    ResourceChange: Optional[ResourceChangeTypeDef] = None

class DescribeStacksOutputTypeDef(BaseValidatorModel):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeGeneratedTemplateOutputTypeDef(BaseValidatorModel):
    GeneratedTemplateId: str
    GeneratedTemplateName: str
    Resources: List[ResourceDetailTypeDef]
    Status: GeneratedTemplateStatusType
    StatusReason: str
    CreationTime: datetime
    LastUpdatedTime: datetime
    Progress: TemplateProgressTypeDef
    StackId: str
    TemplateConfiguration: TemplateConfigurationTypeDef
    TotalWarnings: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChangeSetOutputTypeDef(BaseValidatorModel):
    ChangeSetName: str
    ChangeSetId: str
    StackId: str
    StackName: str
    Description: str
    Parameters: List[ParameterTypeDef]
    CreationTime: datetime
    ExecutionStatus: ExecutionStatusType
    Status: ChangeSetStatusType
    StatusReason: str
    NotificationARNs: List[str]
    RollbackConfiguration: RollbackConfigurationOutputTypeDef
    Capabilities: List[CapabilityType]
    Tags: List[TagTypeDef]
    Changes: List[ChangeTypeDef]
    IncludeNestedStacks: bool
    ParentChangeSetId: str
    RootChangeSetId: str
    OnStackFailure: OnStackFailureType
    ImportExistingResources: bool
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

