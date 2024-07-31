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
from aws_resource_validator.pydantic_models.cloudformation_constants import *

class AccountGateResultTypeDef(BaseModel):
    Status: Optional[AccountGateStatusType] = None
    StatusReason: Optional[str] = None

class AccountLimitTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[int] = None

class LoggingConfigTypeDef(BaseModel):
    LogRoleArn: str
    LogGroupName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AutoDeploymentTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    RetainStacksOnAccountRemoval: Optional[bool] = None

class TypeConfigurationIdentifierTypeDef(BaseModel):
    TypeArn: Optional[str] = None
    TypeConfigurationAlias: Optional[str] = None
    TypeConfigurationArn: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    TypeName: Optional[str] = None

class TypeConfigurationDetailsTypeDef(BaseModel):
    Arn: Optional[str] = None
    Alias: Optional[str] = None
    Configuration: Optional[str] = None
    LastUpdated: Optional[datetime] = None
    TypeArn: Optional[str] = None
    TypeName: Optional[str] = None
    IsDefaultConfiguration: Optional[bool] = None

class CancelUpdateStackInputRequestTypeDef(BaseModel):
    StackName: str
    ClientRequestToken: Optional[str] = None

class CancelUpdateStackInputStackCancelUpdateTypeDef(BaseModel):
    ClientRequestToken: Optional[str] = None

class ChangeSetHookResourceTargetDetailsTypeDef(BaseModel):
    LogicalResourceId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceAction: Optional[ChangeActionType] = None

class ChangeSetSummaryTypeDef(BaseModel):
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

class ContinueUpdateRollbackInputRequestTypeDef(BaseModel):
    StackName: str
    RoleARN: Optional[str] = None
    ResourcesToSkip: Optional[Sequence[str]] = None
    ClientRequestToken: Optional[str] = None

class ParameterTypeDef(BaseModel):
    ParameterKey: Optional[str] = None
    ParameterValue: Optional[str] = None
    UsePreviousValue: Optional[bool] = None
    ResolvedValue: Optional[str] = None

class ResourceToImportTypeDef(BaseModel):
    ResourceType: str
    LogicalResourceId: str
    ResourceIdentifier: Mapping[str, str]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResourceDefinitionTypeDef(BaseModel):
    ResourceType: str
    ResourceIdentifier: Mapping[str, str]
    LogicalResourceId: Optional[str] = None

class TemplateConfigurationTypeDef(BaseModel):
    DeletionPolicy: Optional[GeneratedTemplateDeletionPolicyType] = None
    UpdateReplacePolicy: Optional[GeneratedTemplateUpdateReplacePolicyType] = None

class DeploymentTargetsTypeDef(BaseModel):
    Accounts: Optional[Sequence[str]] = None
    AccountsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    AccountFilterType: Optional[AccountFilterTypeType] = None

class StackSetOperationPreferencesTypeDef(BaseModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[Sequence[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None

class ManagedExecutionTypeDef(BaseModel):
    Active: Optional[bool] = None

class DeactivateTypeInputRequestTypeDef(BaseModel):
    TypeName: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    Arn: Optional[str] = None

class DeleteChangeSetInputRequestTypeDef(BaseModel):
    ChangeSetName: str
    StackName: Optional[str] = None

class DeleteGeneratedTemplateInputRequestTypeDef(BaseModel):
    GeneratedTemplateName: str

class DeleteStackInputRequestTypeDef(BaseModel):
    StackName: str
    RetainResources: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DeletionMode: Optional[DeletionModeType] = None

class DeleteStackInputStackDeleteTypeDef(BaseModel):
    RetainResources: Optional[Sequence[str]] = None
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DeletionMode: Optional[DeletionModeType] = None

class DeleteStackSetInputRequestTypeDef(BaseModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None

class DeploymentTargetsOutputTypeDef(BaseModel):
    Accounts: Optional[List[str]] = None
    AccountsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[List[str]] = None
    AccountFilterType: Optional[AccountFilterTypeType] = None

class DeregisterTypeInputRequestTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccountLimitsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class DescribeChangeSetHooksInputRequestTypeDef(BaseModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    LogicalResourceId: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeChangeSetInputRequestTypeDef(BaseModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None

class DescribeGeneratedTemplateInputRequestTypeDef(BaseModel):
    GeneratedTemplateName: str

class TemplateProgressTypeDef(BaseModel):
    ResourcesSucceeded: Optional[int] = None
    ResourcesFailed: Optional[int] = None
    ResourcesProcessing: Optional[int] = None
    ResourcesPending: Optional[int] = None

class DescribeOrganizationsAccessInputRequestTypeDef(BaseModel):
    CallAs: Optional[CallAsType] = None

class DescribePublisherInputRequestTypeDef(BaseModel):
    PublisherId: Optional[str] = None

class DescribeResourceScanInputRequestTypeDef(BaseModel):
    ResourceScanId: str

class DescribeStackDriftDetectionStatusInputRequestTypeDef(BaseModel):
    StackDriftDetectionId: str

class DescribeStackEventsInputRequestTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None

class StackEventTypeDef(BaseModel):
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

class DescribeStackInstanceInputRequestTypeDef(BaseModel):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    CallAs: Optional[CallAsType] = None

class DescribeStackResourceDriftsInputRequestTypeDef(BaseModel):
    StackName: str
    StackResourceDriftStatusFilters: Optional[Sequence[StackResourceDriftStatusType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeStackResourceInputRequestTypeDef(BaseModel):
    StackName: str
    LogicalResourceId: str

class DescribeStackResourcesInputRequestTypeDef(BaseModel):
    StackName: Optional[str] = None
    LogicalResourceId: Optional[str] = None
    PhysicalResourceId: Optional[str] = None

class DescribeStackSetInputRequestTypeDef(BaseModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None

class DescribeStackSetOperationInputRequestTypeDef(BaseModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None

class DescribeStacksInputRequestTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None

class DescribeTypeInputRequestTypeDef(BaseModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    Arn: Optional[str] = None
    VersionId: Optional[str] = None
    PublisherId: Optional[str] = None
    PublicVersionNumber: Optional[str] = None

class RequiredActivatedTypeTypeDef(BaseModel):
    TypeNameAlias: Optional[str] = None
    OriginalTypeName: Optional[str] = None
    PublisherId: Optional[str] = None
    SupportedMajorVersions: Optional[List[int]] = None

class DescribeTypeRegistrationInputRequestTypeDef(BaseModel):
    RegistrationToken: str

class DetectStackDriftInputRequestTypeDef(BaseModel):
    StackName: str
    LogicalResourceIds: Optional[Sequence[str]] = None

class DetectStackResourceDriftInputRequestTypeDef(BaseModel):
    StackName: str
    LogicalResourceId: str

class ExecuteChangeSetInputRequestTypeDef(BaseModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    DisableRollback: Optional[bool] = None
    RetainExceptOnCreate: Optional[bool] = None

class ExportTypeDef(BaseModel):
    ExportingStackId: Optional[str] = None
    Name: Optional[str] = None
    Value: Optional[str] = None

class GetGeneratedTemplateInputRequestTypeDef(BaseModel):
    GeneratedTemplateName: str
    Format: Optional[TemplateFormatType] = None

class GetStackPolicyInputRequestTypeDef(BaseModel):
    StackName: str

class GetTemplateInputRequestTypeDef(BaseModel):
    StackName: Optional[str] = None
    ChangeSetName: Optional[str] = None
    TemplateStage: Optional[TemplateStageType] = None

class TemplateSummaryConfigTypeDef(BaseModel):
    TreatUnrecognizedResourceTypesAsWarnings: Optional[bool] = None

class ResourceIdentifierSummaryTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    LogicalResourceIds: Optional[List[str]] = None
    ResourceIdentifiers: Optional[List[str]] = None

class WarningsTypeDef(BaseModel):
    UnrecognizedResourceTypes: Optional[List[str]] = None

class ListChangeSetsInputRequestTypeDef(BaseModel):
    StackName: str
    NextToken: Optional[str] = None

class ListExportsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class ListGeneratedTemplatesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TemplateSummaryTypeDef(BaseModel):
    GeneratedTemplateId: Optional[str] = None
    GeneratedTemplateName: Optional[str] = None
    Status: Optional[GeneratedTemplateStatusType] = None
    StatusReason: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    NumberOfResources: Optional[int] = None

class ListImportsInputRequestTypeDef(BaseModel):
    ExportName: str
    NextToken: Optional[str] = None

class ScannedResourceIdentifierTypeDef(BaseModel):
    ResourceType: str
    ResourceIdentifier: Mapping[str, str]

class ScannedResourceTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceIdentifier: Optional[Dict[str, str]] = None
    ManagedByStack: Optional[bool] = None

class ListResourceScanResourcesInputRequestTypeDef(BaseModel):
    ResourceScanId: str
    ResourceIdentifier: Optional[str] = None
    ResourceTypePrefix: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourceScansInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ResourceScanSummaryTypeDef(BaseModel):
    ResourceScanId: Optional[str] = None
    Status: Optional[ResourceScanStatusType] = None
    StatusReason: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    PercentageCompleted: Optional[float] = None

class ListStackInstanceResourceDriftsInputRequestTypeDef(BaseModel):
    StackSetName: str
    StackInstanceAccount: str
    StackInstanceRegion: str
    OperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StackInstanceResourceDriftStatuses: Optional[Sequence[StackResourceDriftStatusType]] = None
    CallAs: Optional[CallAsType] = None

class StackInstanceFilterTypeDef(BaseModel):
    Name: Optional[StackInstanceFilterNameType] = None
    Values: Optional[str] = None

class ListStackResourcesInputRequestTypeDef(BaseModel):
    StackName: str
    NextToken: Optional[str] = None

class ListStackSetAutoDeploymentTargetsInputRequestTypeDef(BaseModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None

class StackSetAutoDeploymentTargetSummaryTypeDef(BaseModel):
    OrganizationalUnitId: Optional[str] = None
    Regions: Optional[List[str]] = None

class OperationResultFilterTypeDef(BaseModel):
    Name: Optional[Literal["OPERATION_RESULT_STATUS"]] = None
    Values: Optional[str] = None

class ListStackSetOperationsInputRequestTypeDef(BaseModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None

class ListStackSetsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[StackSetStatusType] = None
    CallAs: Optional[CallAsType] = None

class ListStacksInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    StackStatusFilter: Optional[Sequence[StackStatusType]] = None

class ListTypeRegistrationsInputRequestTypeDef(BaseModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    TypeArn: Optional[str] = None
    RegistrationStatusFilter: Optional[RegistrationStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTypeVersionsInputRequestTypeDef(BaseModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    Arn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    PublisherId: Optional[str] = None

class TypeVersionSummaryTypeDef(BaseModel):
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    Arn: Optional[str] = None
    TimeCreated: Optional[datetime] = None
    Description: Optional[str] = None
    PublicVersionNumber: Optional[str] = None

class TypeFiltersTypeDef(BaseModel):
    Category: Optional[CategoryType] = None
    PublisherId: Optional[str] = None
    TypeNamePrefix: Optional[str] = None

class TypeSummaryTypeDef(BaseModel):
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

class ModuleInfoTypeDef(BaseModel):
    TypeHierarchy: Optional[str] = None
    LogicalIdHierarchy: Optional[str] = None

class OutputTypeDef(BaseModel):
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None
    Description: Optional[str] = None
    ExportName: Optional[str] = None

class ParameterConstraintsTypeDef(BaseModel):
    AllowedValues: Optional[List[str]] = None

class PhysicalResourceIdContextKeyValuePairTypeDef(BaseModel):
    Key: str
    Value: str

class PropertyDifferenceTypeDef(BaseModel):
    PropertyPath: str
    ExpectedValue: str
    ActualValue: str
    DifferenceType: DifferenceTypeType

class PublishTypeInputRequestTypeDef(BaseModel):
    Type: Optional[ThirdPartyTypeType] = None
    Arn: Optional[str] = None
    TypeName: Optional[str] = None
    PublicVersionNumber: Optional[str] = None

class RecordHandlerProgressInputRequestTypeDef(BaseModel):
    BearerToken: str
    OperationStatus: OperationStatusType
    CurrentOperationStatus: Optional[OperationStatusType] = None
    StatusMessage: Optional[str] = None
    ErrorCode: Optional[HandlerErrorCodeType] = None
    ResourceModel: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class RegisterPublisherInputRequestTypeDef(BaseModel):
    AcceptTermsAndConditions: Optional[bool] = None
    ConnectionArn: Optional[str] = None

class ResourceTargetDefinitionTypeDef(BaseModel):
    Attribute: Optional[ResourceAttributeType] = None
    Name: Optional[str] = None
    RequiresRecreation: Optional[RequiresRecreationType] = None
    Path: Optional[str] = None
    BeforeValue: Optional[str] = None
    AfterValue: Optional[str] = None
    AttributeChangeType: Optional[AttributeChangeTypeType] = None

class RollbackTriggerTypeDef(BaseModel):
    Arn: str
    Type: str

class RollbackStackInputRequestTypeDef(BaseModel):
    StackName: str
    RoleARN: Optional[str] = None
    ClientRequestToken: Optional[str] = None
    RetainExceptOnCreate: Optional[bool] = None

class SetStackPolicyInputRequestTypeDef(BaseModel):
    StackName: str
    StackPolicyBody: Optional[str] = None
    StackPolicyURL: Optional[str] = None

class SetTypeConfigurationInputRequestTypeDef(BaseModel):
    Configuration: str
    TypeArn: Optional[str] = None
    ConfigurationAlias: Optional[str] = None
    TypeName: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None

class SetTypeDefaultVersionInputRequestTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[RegistryTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None

class SignalResourceInputRequestTypeDef(BaseModel):
    StackName: str
    LogicalResourceId: str
    UniqueId: str
    Status: ResourceSignalStatusType

class StackDriftInformationSummaryTypeDef(BaseModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackDriftInformationTypeDef(BaseModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackInstanceComprehensiveStatusTypeDef(BaseModel):
    DetailedStatus: Optional[StackInstanceDetailedStatusType] = None

class StackResourceDriftInformationTypeDef(BaseModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackResourceDriftInformationSummaryTypeDef(BaseModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: Optional[datetime] = None

class StackSetDriftDetectionDetailsTypeDef(BaseModel):
    DriftStatus: Optional[StackSetDriftStatusType] = None
    DriftDetectionStatus: Optional[StackSetDriftDetectionStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    TotalStackInstancesCount: Optional[int] = None
    DriftedStackInstancesCount: Optional[int] = None
    InSyncStackInstancesCount: Optional[int] = None
    InProgressStackInstancesCount: Optional[int] = None
    FailedStackInstancesCount: Optional[int] = None

class StackSetOperationPreferencesExtraOutputTypeDef(BaseModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[List[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None

class StackSetOperationPreferencesOutputTypeDef(BaseModel):
    RegionConcurrencyType: Optional[RegionConcurrencyTypeType] = None
    RegionOrder: Optional[List[str]] = None
    FailureToleranceCount: Optional[int] = None
    FailureTolerancePercentage: Optional[int] = None
    MaxConcurrentCount: Optional[int] = None
    MaxConcurrentPercentage: Optional[int] = None
    ConcurrencyMode: Optional[ConcurrencyModeType] = None

class StackSetOperationStatusDetailsTypeDef(BaseModel):
    FailedStackInstancesCount: Optional[int] = None

class StartResourceScanInputRequestTypeDef(BaseModel):
    ClientRequestToken: Optional[str] = None

class StopStackSetOperationInputRequestTypeDef(BaseModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None

class TemplateParameterTypeDef(BaseModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    NoEcho: Optional[bool] = None
    Description: Optional[str] = None

class TestTypeInputRequestTypeDef(BaseModel):
    Arn: Optional[str] = None
    Type: Optional[ThirdPartyTypeType] = None
    TypeName: Optional[str] = None
    VersionId: Optional[str] = None
    LogDeliveryBucket: Optional[str] = None

class UpdateTerminationProtectionInputRequestTypeDef(BaseModel):
    EnableTerminationProtection: bool
    StackName: str

class ValidateTemplateInputRequestTypeDef(BaseModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None

class WarningPropertyTypeDef(BaseModel):
    PropertyPath: Optional[str] = None
    Required: Optional[bool] = None
    Description: Optional[str] = None

class StackSetOperationResultSummaryTypeDef(BaseModel):
    Account: Optional[str] = None
    Region: Optional[str] = None
    Status: Optional[StackSetOperationResultStatusType] = None
    StatusReason: Optional[str] = None
    AccountGateResult: Optional[AccountGateResultTypeDef] = None
    OrganizationalUnitId: Optional[str] = None

class ActivateTypeInputRequestTypeDef(BaseModel):
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

class RegisterTypeInputRequestTypeDef(BaseModel):
    TypeName: str
    SchemaHandlerPackage: str
    Type: Optional[RegistryTypeType] = None
    LoggingConfig: Optional[LoggingConfigTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    ClientRequestToken: Optional[str] = None

class ActivateTypeOutputTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChangeSetOutputTypeDef(BaseModel):
    Id: str
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGeneratedTemplateOutputTypeDef(BaseModel):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackInstancesOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackOutputTypeDef(BaseModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackSetOutputTypeDef(BaseModel):
    StackSetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteStackInstancesOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountLimitsOutputTypeDef(BaseModel):
    AccountLimits: List[AccountLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrganizationsAccessOutputTypeDef(BaseModel):
    Status: OrganizationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePublisherOutputTypeDef(BaseModel):
    PublisherId: str
    PublisherStatus: PublisherStatusType
    IdentityProvider: IdentityProviderType
    PublisherProfile: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceScanOutputTypeDef(BaseModel):
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

class DescribeStackDriftDetectionStatusOutputTypeDef(BaseModel):
    StackId: str
    StackDriftDetectionId: str
    StackDriftStatus: StackDriftStatusType
    DetectionStatus: StackDriftDetectionStatusType
    DetectionStatusReason: str
    DriftedStackResourceCount: int
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTypeRegistrationOutputTypeDef(BaseModel):
    ProgressStatus: RegistrationStatusType
    Description: str
    TypeArn: str
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectStackDriftOutputTypeDef(BaseModel):
    StackDriftDetectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectStackSetDriftOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EstimateTemplateCostOutputTypeDef(BaseModel):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeneratedTemplateOutputTypeDef(BaseModel):
    Status: GeneratedTemplateStatusType
    TemplateBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetStackPolicyOutputTypeDef(BaseModel):
    StackPolicyBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateOutputTypeDef(BaseModel):
    TemplateBody: Dict[str, Any]
    StagesAvailable: List["TemplateStageType"]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportStacksToStackSetOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportsOutputTypeDef(BaseModel):
    Imports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTypeRegistrationsOutputTypeDef(BaseModel):
    RegistrationTokenList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModuleInfoResponseTypeDef(BaseModel):
    TypeHierarchy: str
    LogicalIdHierarchy: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishTypeOutputTypeDef(BaseModel):
    PublicTypeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterPublisherOutputTypeDef(BaseModel):
    PublisherId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTypeOutputTypeDef(BaseModel):
    RegistrationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackStackOutputTypeDef(BaseModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetTypeConfigurationOutputTypeDef(BaseModel):
    ConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StackDriftInformationResponseTypeDef(BaseModel):
    StackDriftStatus: StackDriftStatusType
    LastCheckTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StackResourceDriftInformationResponseTypeDef(BaseModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StackResourceDriftInformationSummaryResponseTypeDef(BaseModel):
    StackResourceDriftStatus: StackResourceDriftStatusType
    LastCheckTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceScanOutputTypeDef(BaseModel):
    ResourceScanId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestTypeOutputTypeDef(BaseModel):
    TypeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeneratedTemplateOutputTypeDef(BaseModel):
    GeneratedTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackInstancesOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackOutputTypeDef(BaseModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackSetOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTerminationProtectionOutputTypeDef(BaseModel):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDescribeTypeConfigurationsErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    TypeConfigurationIdentifier: Optional[TypeConfigurationIdentifierTypeDef] = None

class BatchDescribeTypeConfigurationsInputRequestTypeDef(BaseModel):
    TypeConfigurationIdentifiers: Sequence[TypeConfigurationIdentifierTypeDef]

class ChangeSetHookTargetDetailsTypeDef(BaseModel):
    TargetType: Optional[Literal["RESOURCE"]] = None
    ResourceTargetDetails: Optional[ChangeSetHookResourceTargetDetailsTypeDef] = None

class ListChangeSetsOutputTypeDef(BaseModel):
    Summaries: List[ChangeSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EstimateTemplateCostInputRequestTypeDef(BaseModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class CreateGeneratedTemplateInputRequestTypeDef(BaseModel):
    GeneratedTemplateName: str
    Resources: Optional[Sequence[ResourceDefinitionTypeDef]] = None
    StackName: Optional[str] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None

class UpdateGeneratedTemplateInputRequestTypeDef(BaseModel):
    GeneratedTemplateName: str
    NewGeneratedTemplateName: Optional[str] = None
    AddResources: Optional[Sequence[ResourceDefinitionTypeDef]] = None
    RemoveResources: Optional[Sequence[str]] = None
    RefreshAllResources: Optional[bool] = None
    TemplateConfiguration: Optional[TemplateConfigurationTypeDef] = None

class CreateStackInstancesInputRequestTypeDef(BaseModel):
    StackSetName: str
    Regions: Sequence[str]
    Accounts: Optional[Sequence[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    ParameterOverrides: Optional[Sequence[ParameterTypeDef]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class DeleteStackInstancesInputRequestTypeDef(BaseModel):
    StackSetName: str
    Regions: Sequence[str]
    RetainStacks: bool
    Accounts: Optional[Sequence[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class DetectStackSetDriftInputRequestTypeDef(BaseModel):
    StackSetName: str
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class ImportStacksToStackSetInputRequestTypeDef(BaseModel):
    StackSetName: str
    StackIds: Optional[Sequence[str]] = None
    StackIdsUrl: Optional[str] = None
    OrganizationalUnitIds: Optional[Sequence[str]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class UpdateStackInstancesInputRequestTypeDef(BaseModel):
    StackSetName: str
    Regions: Sequence[str]
    Accounts: Optional[Sequence[str]] = None
    DeploymentTargets: Optional[DeploymentTargetsTypeDef] = None
    ParameterOverrides: Optional[Sequence[ParameterTypeDef]] = None
    OperationPreferences: Optional[StackSetOperationPreferencesTypeDef] = None
    OperationId: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class CreateStackSetInputRequestTypeDef(BaseModel):
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

class StackSetSummaryTypeDef(BaseModel):
    StackSetName: Optional[str] = None
    StackSetId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[StackSetStatusType] = None
    AutoDeployment: Optional[AutoDeploymentTypeDef] = None
    PermissionModel: Optional[PermissionModelsType] = None
    DriftStatus: Optional[StackDriftStatusType] = None
    LastDriftCheckTimestamp: Optional[datetime] = None
    ManagedExecution: Optional[ManagedExecutionTypeDef] = None

class UpdateStackSetInputRequestTypeDef(BaseModel):
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

class DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeChangeSetInputDescribeChangeSetPaginateTypeDef(BaseModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStackEventsInputDescribeStackEventsPaginateTypeDef(BaseModel):
    StackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStacksInputDescribeStacksPaginateTypeDef(BaseModel):
    StackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChangeSetsInputListChangeSetsPaginateTypeDef(BaseModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportsInputListExportsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGeneratedTemplatesInputListGeneratedTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportsInputListImportsPaginateTypeDef(BaseModel):
    ExportName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceScanResourcesInputListResourceScanResourcesPaginateTypeDef(BaseModel):
    ResourceScanId: str
    ResourceIdentifier: Optional[str] = None
    ResourceTypePrefix: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceScansInputListResourceScansPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackResourcesInputListStackResourcesPaginateTypeDef(BaseModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackSetOperationsInputListStackSetOperationsPaginateTypeDef(BaseModel):
    StackSetName: str
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackSetsInputListStackSetsPaginateTypeDef(BaseModel):
    Status: Optional[StackSetStatusType] = None
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStacksInputListStacksPaginateTypeDef(BaseModel):
    StackStatusFilter: Optional[Sequence[StackStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeChangeSetInputChangeSetCreateCompleteWaitTypeDef(BaseModel):
    ChangeSetName: str
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    IncludePropertyValues: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackCreateCompleteWaitTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackDeleteCompleteWaitTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackExistsWaitTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackImportCompleteWaitTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackRollbackCompleteWaitTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStacksInputStackUpdateCompleteWaitTypeDef(BaseModel):
    StackName: Optional[str] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTypeRegistrationInputTypeRegistrationCompleteWaitTypeDef(BaseModel):
    RegistrationToken: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStackEventsOutputTypeDef(BaseModel):
    StackEvents: List[StackEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTypeOutputTypeDef(BaseModel):
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

class ListExportsOutputTypeDef(BaseModel):
    Exports: List[ExportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTemplateSummaryInputRequestTypeDef(BaseModel):
    TemplateBody: Optional[str] = None
    TemplateURL: Optional[str] = None
    StackName: Optional[str] = None
    StackSetName: Optional[str] = None
    CallAs: Optional[CallAsType] = None
    TemplateSummaryConfig: Optional[TemplateSummaryConfigTypeDef] = None

class ListGeneratedTemplatesOutputTypeDef(BaseModel):
    Summaries: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceScanRelatedResourcesInputListResourceScanRelatedResourcesPaginateTypeDef(BaseModel):
    ResourceScanId: str
    Resources: Sequence[ScannedResourceIdentifierTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceScanRelatedResourcesInputRequestTypeDef(BaseModel):
    ResourceScanId: str
    Resources: Sequence[ScannedResourceIdentifierTypeDef]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListResourceScanRelatedResourcesOutputTypeDef(BaseModel):
    RelatedResources: List[ScannedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceScanResourcesOutputTypeDef(BaseModel):
    Resources: List[ScannedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListResourceScansOutputTypeDef(BaseModel):
    ResourceScanSummaries: List[ResourceScanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStackInstancesInputListStackInstancesPaginateTypeDef(BaseModel):
    StackSetName: str
    Filters: Optional[Sequence[StackInstanceFilterTypeDef]] = None
    StackInstanceAccount: Optional[str] = None
    StackInstanceRegion: Optional[str] = None
    CallAs: Optional[CallAsType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackInstancesInputRequestTypeDef(BaseModel):
    StackSetName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[StackInstanceFilterTypeDef]] = None
    StackInstanceAccount: Optional[str] = None
    StackInstanceRegion: Optional[str] = None
    CallAs: Optional[CallAsType] = None

class ListStackSetAutoDeploymentTargetsOutputTypeDef(BaseModel):
    Summaries: List[StackSetAutoDeploymentTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStackSetOperationResultsInputListStackSetOperationResultsPaginateTypeDef(BaseModel):
    StackSetName: str
    OperationId: str
    CallAs: Optional[CallAsType] = None
    Filters: Optional[Sequence[OperationResultFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStackSetOperationResultsInputRequestTypeDef(BaseModel):
    StackSetName: str
    OperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    CallAs: Optional[CallAsType] = None
    Filters: Optional[Sequence[OperationResultFilterTypeDef]] = None

class ListTypeVersionsOutputTypeDef(BaseModel):
    TypeVersionSummaries: List[TypeVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTypesInputListTypesPaginateTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    Type: Optional[RegistryTypeType] = None
    Filters: Optional[TypeFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTypesInputRequestTypeDef(BaseModel):
    Visibility: Optional[VisibilityType] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None
    DeprecatedStatus: Optional[DeprecatedStatusType] = None
    Type: Optional[RegistryTypeType] = None
    Filters: Optional[TypeFiltersTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTypesOutputTypeDef(BaseModel):
    TypeSummaries: List[TypeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ParameterDeclarationTypeDef(BaseModel):
    ParameterKey: Optional[str] = None
    DefaultValue: Optional[str] = None
    ParameterType: Optional[str] = None
    NoEcho: Optional[bool] = None
    Description: Optional[str] = None
    ParameterConstraints: Optional[ParameterConstraintsTypeDef] = None

class StackInstanceResourceDriftsSummaryTypeDef(BaseModel):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatusType
    Timestamp: datetime
    PhysicalResourceId: Optional[str] = None
    PhysicalResourceIdContext: Optional[       List[PhysicalResourceIdContextKeyValuePairTypeDef]     ] = None
    PropertyDifferences: Optional[List[PropertyDifferenceTypeDef]] = None

class StackResourceDriftTypeDef(BaseModel):
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

class ResourceChangeDetailTypeDef(BaseModel):
    Target: Optional[ResourceTargetDefinitionTypeDef] = None
    Evaluation: Optional[EvaluationTypeType] = None
    ChangeSource: Optional[ChangeSourceType] = None
    CausingEntity: Optional[str] = None

class RollbackConfigurationExtraOutputTypeDef(BaseModel):
    RollbackTriggers: Optional[List[RollbackTriggerTypeDef]] = None
    MonitoringTimeInMinutes: Optional[int] = None

class RollbackConfigurationOutputTypeDef(BaseModel):
    RollbackTriggers: Optional[List[RollbackTriggerTypeDef]] = None
    MonitoringTimeInMinutes: Optional[int] = None

class RollbackConfigurationResponseTypeDef(BaseModel):
    RollbackTriggers: List[RollbackTriggerTypeDef]
    MonitoringTimeInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackConfigurationTypeDef(BaseModel):
    RollbackTriggers: Optional[Sequence[RollbackTriggerTypeDef]] = None
    MonitoringTimeInMinutes: Optional[int] = None

class StackSummaryTypeDef(BaseModel):
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

class StackInstanceSummaryTypeDef(BaseModel):
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

class StackInstanceTypeDef(BaseModel):
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

class StackResourceDetailTypeDef(BaseModel):
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

class StackResourceTypeDef(BaseModel):
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

class StackResourceSummaryTypeDef(BaseModel):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatusType
    PhysicalResourceId: Optional[str] = None
    ResourceStatusReason: Optional[str] = None
    DriftInformation: Optional[StackResourceDriftInformationSummaryTypeDef] = None
    ModuleInfo: Optional[ModuleInfoTypeDef] = None

class StackSetTypeDef(BaseModel):
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

class StackSetOperationSummaryTypeDef(BaseModel):
    OperationId: Optional[str] = None
    Action: Optional[StackSetOperationActionType] = None
    Status: Optional[StackSetOperationStatusType] = None
    CreationTimestamp: Optional[datetime] = None
    EndTimestamp: Optional[datetime] = None
    StatusReason: Optional[str] = None
    StatusDetails: Optional[StackSetOperationStatusDetailsTypeDef] = None
    OperationPreferences: Optional[StackSetOperationPreferencesOutputTypeDef] = None

class StackSetOperationTypeDef(BaseModel):
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

class ValidateTemplateOutputTypeDef(BaseModel):
    Parameters: List[TemplateParameterTypeDef]
    Description: str
    Capabilities: List[CapabilityType]
    CapabilitiesReason: str
    DeclaredTransforms: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class WarningDetailTypeDef(BaseModel):
    Type: Optional[WarningTypeType] = None
    Properties: Optional[List[WarningPropertyTypeDef]] = None

class ListStackSetOperationResultsOutputTypeDef(BaseModel):
    Summaries: List[StackSetOperationResultSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchDescribeTypeConfigurationsOutputTypeDef(BaseModel):
    Errors: List[BatchDescribeTypeConfigurationsErrorTypeDef]
    UnprocessedTypeConfigurations: List[TypeConfigurationIdentifierTypeDef]
    TypeConfigurations: List[TypeConfigurationDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeSetHookTypeDef(BaseModel):
    InvocationPoint: Optional[Literal["PRE_PROVISION"]] = None
    FailureMode: Optional[HookFailureModeType] = None
    TypeName: Optional[str] = None
    TypeVersionId: Optional[str] = None
    TypeConfigurationVersionId: Optional[str] = None
    TargetDetails: Optional[ChangeSetHookTargetDetailsTypeDef] = None

class ListStackSetsOutputTypeDef(BaseModel):
    Summaries: List[StackSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTemplateSummaryOutputTypeDef(BaseModel):
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

class ListStackInstanceResourceDriftsOutputTypeDef(BaseModel):
    Summaries: List[StackInstanceResourceDriftsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackResourceDriftsOutputTypeDef(BaseModel):
    StackResourceDrifts: List[StackResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetectStackResourceDriftOutputTypeDef(BaseModel):
    StackResourceDrift: StackResourceDriftTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceChangeTypeDef(BaseModel):
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

class StackTypeDef(BaseModel):
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

class CreateChangeSetInputRequestTypeDef(BaseModel):
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

class CreateStackInputRequestTypeDef(BaseModel):
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

class CreateStackInputServiceResourceCreateStackTypeDef(BaseModel):
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

class UpdateStackInputRequestTypeDef(BaseModel):
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

class UpdateStackInputStackUpdateTypeDef(BaseModel):
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

class ListStacksOutputTypeDef(BaseModel):
    StackSummaries: List[StackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStackInstancesOutputTypeDef(BaseModel):
    Summaries: List[StackInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackInstanceOutputTypeDef(BaseModel):
    StackInstance: StackInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackResourceOutputTypeDef(BaseModel):
    StackResourceDetail: StackResourceDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackResourcesOutputTypeDef(BaseModel):
    StackResources: List[StackResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackResourcesOutputTypeDef(BaseModel):
    StackResourceSummaries: List[StackResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackSetOutputTypeDef(BaseModel):
    StackSet: StackSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStackSetOperationsOutputTypeDef(BaseModel):
    Summaries: List[StackSetOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStackSetOperationOutputTypeDef(BaseModel):
    StackSetOperation: StackSetOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceDetailTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    LogicalResourceId: Optional[str] = None
    ResourceIdentifier: Optional[Dict[str, str]] = None
    ResourceStatus: Optional[GeneratedTemplateResourceStatusType] = None
    ResourceStatusReason: Optional[str] = None
    Warnings: Optional[List[WarningDetailTypeDef]] = None

class DescribeChangeSetHooksOutputTypeDef(BaseModel):
    ChangeSetId: str
    ChangeSetName: str
    Hooks: List[ChangeSetHookTypeDef]
    Status: ChangeSetHooksStatusType
    StackId: str
    StackName: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ChangeTypeDef(BaseModel):
    Type: Optional[Literal["Resource"]] = None
    HookInvocationCount: Optional[int] = None
    ResourceChange: Optional[ResourceChangeTypeDef] = None

class DescribeStacksOutputTypeDef(BaseModel):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeGeneratedTemplateOutputTypeDef(BaseModel):
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

class DescribeChangeSetOutputTypeDef(BaseModel):
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

