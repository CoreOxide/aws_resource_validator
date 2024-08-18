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
from aws_resource_validator.pydantic_models.elasticbeanstalk_constants import *

class AbortEnvironmentUpdateMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class LatencyTypeDef(BaseValidatorModel):
    P999: Optional[float] = None
    P99: Optional[float] = None
    P95: Optional[float] = None
    P90: Optional[float] = None
    P85: Optional[float] = None
    P75: Optional[float] = None
    P50: Optional[float] = None
    P10: Optional[float] = None

class StatusCodesTypeDef(BaseValidatorModel):
    Status2xx: Optional[int] = None
    Status3xx: Optional[int] = None
    Status4xx: Optional[int] = None
    Status5xx: Optional[int] = None

class S3LocationTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class SourceBuildInformationTypeDef(BaseValidatorModel):
    SourceType: SourceTypeType
    SourceRepository: SourceRepositoryType
    SourceLocation: str

class MaxAgeRuleTypeDef(BaseValidatorModel):
    Enabled: bool
    MaxAgeInDays: Optional[int] = None
    DeleteSourceFromS3: Optional[bool] = None

class MaxCountRuleTypeDef(BaseValidatorModel):
    Enabled: bool
    MaxCount: Optional[int] = None
    DeleteSourceFromS3: Optional[bool] = None

class ApplyEnvironmentManagedActionRequestRequestTypeDef(BaseValidatorModel):
    ActionId: str
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None

class AssociateEnvironmentOperationsRoleMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentName: str
    OperationsRole: str

class AutoScalingGroupTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class BuildConfigurationTypeDef(BaseValidatorModel):
    CodeBuildServiceRole: str
    Image: str
    ArtifactName: Optional[str] = None
    ComputeType: Optional[ComputeTypeType] = None
    TimeoutInMinutes: Optional[int] = None

class BuilderTypeDef(BaseValidatorModel):
    ARN: Optional[str] = None

class CPUUtilizationTypeDef(BaseValidatorModel):
    User: Optional[float] = None
    Nice: Optional[float] = None
    System: Optional[float] = None
    Idle: Optional[float] = None
    IOWait: Optional[float] = None
    IRQ: Optional[float] = None
    SoftIRQ: Optional[float] = None
    Privileged: Optional[float] = None

class CheckDNSAvailabilityMessageRequestTypeDef(BaseValidatorModel):
    CNAMEPrefix: str

class ComposeEnvironmentsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    GroupName: Optional[str] = None
    VersionLabels: Optional[Sequence[str]] = None

class OptionRestrictionRegexTypeDef(BaseValidatorModel):
    Pattern: Optional[str] = None
    Label: Optional[str] = None

class ConfigurationOptionSettingTypeDef(BaseValidatorModel):
    ResourceName: Optional[str] = None
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None
    Value: Optional[str] = None

class ValidationMessageTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Severity: Optional[ValidationSeverityType] = None
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class SourceConfigurationTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    TemplateName: Optional[str] = None

class EnvironmentTierTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Version: Optional[str] = None

class OptionSpecificationTypeDef(BaseValidatorModel):
    ResourceName: Optional[str] = None
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None

class PlatformSummaryTypeDef(BaseValidatorModel):
    PlatformArn: Optional[str] = None
    PlatformOwner: Optional[str] = None
    PlatformStatus: Optional[PlatformStatusType] = None
    PlatformCategory: Optional[str] = None
    OperatingSystemName: Optional[str] = None
    OperatingSystemVersion: Optional[str] = None
    SupportedTierList: Optional[List[str]] = None
    SupportedAddonList: Optional[List[str]] = None
    PlatformLifecycleState: Optional[str] = None
    PlatformVersion: Optional[str] = None
    PlatformBranchName: Optional[str] = None
    PlatformBranchLifecycleState: Optional[str] = None

class CustomAmiTypeDef(BaseValidatorModel):
    VirtualizationType: Optional[str] = None
    ImageId: Optional[str] = None

class DeleteApplicationMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    TerminateEnvByForce: Optional[bool] = None

class DeleteApplicationVersionMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    VersionLabel: str
    DeleteSourceBundle: Optional[bool] = None

class DeleteConfigurationTemplateMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    TemplateName: str

class DeleteEnvironmentConfigurationMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    EnvironmentName: str

class DeletePlatformVersionRequestRequestTypeDef(BaseValidatorModel):
    PlatformArn: Optional[str] = None

class DeploymentTypeDef(BaseValidatorModel):
    VersionLabel: Optional[str] = None
    DeploymentId: Optional[int] = None
    Status: Optional[str] = None
    DeploymentTime: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeApplicationVersionsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabels: Optional[Sequence[str]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeApplicationsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationNames: Optional[Sequence[str]] = None

class DescribeConfigurationSettingsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None

class DescribeEnvironmentHealthRequestRequestTypeDef(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    AttributeNames: Optional[Sequence[EnvironmentHealthAttributeType]] = None

class InstanceHealthSummaryTypeDef(BaseValidatorModel):
    NoData: Optional[int] = None
    Unknown: Optional[int] = None
    Pending: Optional[int] = None
    Ok: Optional[int] = None
    Info: Optional[int] = None
    Warning: Optional[int] = None
    Degraded: Optional[int] = None
    Severe: Optional[int] = None

class DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None

class ManagedActionHistoryItemTypeDef(BaseValidatorModel):
    ActionId: Optional[str] = None
    ActionType: Optional[ActionTypeType] = None
    ActionDescription: Optional[str] = None
    FailureType: Optional[FailureTypeType] = None
    Status: Optional[ActionHistoryStatusType] = None
    FailureDescription: Optional[str] = None
    ExecutedTime: Optional[datetime] = None
    FinishedTime: Optional[datetime] = None

class DescribeEnvironmentManagedActionsRequestRequestTypeDef(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    Status: Optional[ActionStatusType] = None

class ManagedActionTypeDef(BaseValidatorModel):
    ActionId: Optional[str] = None
    ActionDescription: Optional[str] = None
    ActionType: Optional[ActionTypeType] = None
    Status: Optional[ActionStatusType] = None
    WindowStartTime: Optional[datetime] = None

class DescribeEnvironmentResourcesMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeInstancesHealthRequestRequestTypeDef(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    AttributeNames: Optional[Sequence[InstancesHealthAttributeType]] = None
    NextToken: Optional[str] = None

class DescribePlatformVersionRequestRequestTypeDef(BaseValidatorModel):
    PlatformArn: Optional[str] = None

class DisassociateEnvironmentOperationsRoleMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentName: str

class EnvironmentLinkTypeDef(BaseValidatorModel):
    LinkName: Optional[str] = None
    EnvironmentName: Optional[str] = None

class EnvironmentInfoDescriptionTypeDef(BaseValidatorModel):
    InfoType: Optional[EnvironmentInfoTypeType] = None
    Ec2InstanceId: Optional[str] = None
    SampleTimestamp: Optional[datetime] = None
    Message: Optional[str] = None

class InstanceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class LaunchConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class LaunchTemplateTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class LoadBalancerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class QueueTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    URL: Optional[str] = None

class TriggerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class EventDescriptionTypeDef(BaseValidatorModel):
    EventDate: Optional[datetime] = None
    Message: Optional[str] = None
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PlatformArn: Optional[str] = None
    RequestId: Optional[str] = None
    Severity: Optional[EventSeverityType] = None

class SolutionStackDescriptionTypeDef(BaseValidatorModel):
    SolutionStackName: Optional[str] = None
    PermittedFileTypes: Optional[List[str]] = None

class SearchFilterTypeDef(BaseValidatorModel):
    Attribute: Optional[str] = None
    Operator: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class PlatformBranchSummaryTypeDef(BaseValidatorModel):
    PlatformName: Optional[str] = None
    BranchName: Optional[str] = None
    LifecycleState: Optional[str] = None
    BranchOrder: Optional[int] = None
    SupportedTierList: Optional[List[str]] = None

class PlatformFilterTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Operator: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class ListTagsForResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListenerTypeDef(BaseValidatorModel):
    Protocol: Optional[str] = None
    Port: Optional[int] = None

class PlatformFrameworkTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class PlatformProgrammingLanguageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None

class RebuildEnvironmentMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

class RequestEnvironmentInfoMessageRequestTypeDef(BaseValidatorModel):
    InfoType: EnvironmentInfoTypeType
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

class ResourceQuotaTypeDef(BaseValidatorModel):
    Maximum: Optional[int] = None

class RestartAppServerMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

class RetrieveEnvironmentInfoMessageRequestTypeDef(BaseValidatorModel):
    InfoType: EnvironmentInfoTypeType
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

class SwapEnvironmentCNAMEsMessageRequestTypeDef(BaseValidatorModel):
    SourceEnvironmentId: Optional[str] = None
    SourceEnvironmentName: Optional[str] = None
    DestinationEnvironmentId: Optional[str] = None
    DestinationEnvironmentName: Optional[str] = None

class TerminateEnvironmentMessageRequestTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    TerminateResources: Optional[bool] = None
    ForceTerminate: Optional[bool] = None

class UpdateApplicationMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    Description: Optional[str] = None

class UpdateApplicationVersionMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    VersionLabel: str
    Description: Optional[str] = None

class ApplyEnvironmentManagedActionResultTypeDef(BaseValidatorModel):
    ActionId: str
    ActionDescription: str
    ActionType: ActionTypeType
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDNSAvailabilityResultMessageTypeDef(BaseValidatorModel):
    Available: bool
    FullyQualifiedCNAME: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageLocationResultMessageTypeDef(BaseValidatorModel):
    S3Bucket: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationMetricsTypeDef(BaseValidatorModel):
    Duration: Optional[int] = None
    RequestCount: Optional[int] = None
    StatusCodes: Optional[StatusCodesTypeDef] = None
    Latency: Optional[LatencyTypeDef] = None

class ApplicationVersionDescriptionTypeDef(BaseValidatorModel):
    ApplicationVersionArn: Optional[str] = None
    ApplicationName: Optional[str] = None
    Description: Optional[str] = None
    VersionLabel: Optional[str] = None
    SourceBuildInformation: Optional[SourceBuildInformationTypeDef] = None
    BuildArn: Optional[str] = None
    SourceBundle: Optional[S3LocationTypeDef] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    Status: Optional[ApplicationVersionStatusType] = None

class ApplicationVersionLifecycleConfigTypeDef(BaseValidatorModel):
    MaxCountRule: Optional[MaxCountRuleTypeDef] = None
    MaxAgeRule: Optional[MaxAgeRuleTypeDef] = None

class SystemStatusTypeDef(BaseValidatorModel):
    CPUUtilization: Optional[CPUUtilizationTypeDef] = None
    LoadAverage: Optional[List[float]] = None

class ConfigurationOptionDescriptionTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    Name: Optional[str] = None
    DefaultValue: Optional[str] = None
    ChangeSeverity: Optional[str] = None
    UserDefined: Optional[bool] = None
    ValueType: Optional[ConfigurationOptionValueTypeType] = None
    ValueOptions: Optional[List[str]] = None
    MinValue: Optional[int] = None
    MaxValue: Optional[int] = None
    MaxLength: Optional[int] = None
    Regex: Optional[OptionRestrictionRegexTypeDef] = None

class ConfigurationSettingsDescriptionResponseTypeDef(BaseValidatorModel):
    SolutionStackName: str
    PlatformArn: str
    ApplicationName: str
    TemplateName: str
    Description: str
    EnvironmentName: str
    DeploymentStatus: ConfigurationDeploymentStatusType
    DateCreated: datetime
    DateUpdated: datetime
    OptionSettings: List[ConfigurationOptionSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationSettingsDescriptionTypeDef(BaseValidatorModel):
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    ApplicationName: Optional[str] = None
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    EnvironmentName: Optional[str] = None
    DeploymentStatus: Optional[ConfigurationDeploymentStatusType] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    OptionSettings: Optional[List[ConfigurationOptionSettingTypeDef]] = None

class ValidateConfigurationSettingsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    OptionSettings: Sequence[ConfigurationOptionSettingTypeDef]
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None

class ConfigurationSettingsValidationMessagesTypeDef(BaseValidatorModel):
    Messages: List[ValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationVersionMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    VersionLabel: str
    Description: Optional[str] = None
    SourceBuildInformation: Optional[SourceBuildInformationTypeDef] = None
    SourceBundle: Optional[S3LocationTypeDef] = None
    BuildConfiguration: Optional[BuildConfigurationTypeDef] = None
    AutoCreateApplication: Optional[bool] = None
    Process: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreatePlatformVersionRequestRequestTypeDef(BaseValidatorModel):
    PlatformName: str
    PlatformVersion: str
    PlatformDefinitionBundle: S3LocationTypeDef
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[Sequence[ConfigurationOptionSettingTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ResourceTagsDescriptionMessageTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTagsForResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagsToAdd: Optional[Sequence[TagTypeDef]] = None
    TagsToRemove: Optional[Sequence[str]] = None

class CreateConfigurationTemplateMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    TemplateName: str
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    EnvironmentId: Optional[str] = None
    Description: Optional[str] = None
    OptionSettings: Optional[Sequence[ConfigurationOptionSettingTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEnvironmentMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    EnvironmentName: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    CNAMEPrefix: Optional[str] = None
    Tier: Optional[EnvironmentTierTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    OptionSettings: Optional[Sequence[ConfigurationOptionSettingTypeDef]] = None
    OptionsToRemove: Optional[Sequence[OptionSpecificationTypeDef]] = None
    OperationsRole: Optional[str] = None

class DescribeConfigurationOptionsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    Options: Optional[Sequence[OptionSpecificationTypeDef]] = None

class UpdateConfigurationTemplateMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    TemplateName: str
    Description: Optional[str] = None
    OptionSettings: Optional[Sequence[ConfigurationOptionSettingTypeDef]] = None
    OptionsToRemove: Optional[Sequence[OptionSpecificationTypeDef]] = None

class UpdateEnvironmentMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    Tier: Optional[EnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    OptionSettings: Optional[Sequence[ConfigurationOptionSettingTypeDef]] = None
    OptionsToRemove: Optional[Sequence[OptionSpecificationTypeDef]] = None

class CreatePlatformVersionResultTypeDef(BaseValidatorModel):
    PlatformSummary: PlatformSummaryTypeDef
    Builder: BuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePlatformVersionResultTypeDef(BaseValidatorModel):
    PlatformSummary: PlatformSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlatformVersionsResultTypeDef(BaseValidatorModel):
    PlatformSummaryList: List[PlatformSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeApplicationVersionsMessageDescribeApplicationVersionsPaginateTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabels: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEnvironmentManagedActionHistoryRequestDescribeEnvironmentManagedActionHistoryPaginateTypeDef(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEnvironmentManagedActionHistoryResultTypeDef(BaseValidatorModel):
    ManagedActionHistoryItems: List[ManagedActionHistoryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEnvironmentManagedActionsResultTypeDef(BaseValidatorModel):
    ManagedActions: List[ManagedActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentsMessageDescribeEnvironmentsPaginateTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[Sequence[str]] = None
    EnvironmentNames: Optional[Sequence[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEnvironmentsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[Sequence[str]] = None
    EnvironmentNames: Optional[Sequence[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PlatformArn: Optional[str] = None
    RequestId: Optional[str] = None
    Severity: Optional[EventSeverityType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PlatformArn: Optional[str] = None
    RequestId: Optional[str] = None
    Severity: Optional[EventSeverityType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeEnvironmentsMessageEnvironmentExistsWaitTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[Sequence[str]] = None
    EnvironmentNames: Optional[Sequence[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEnvironmentsMessageEnvironmentTerminatedWaitTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[Sequence[str]] = None
    EnvironmentNames: Optional[Sequence[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEnvironmentsMessageEnvironmentUpdatedWaitTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[Sequence[str]] = None
    EnvironmentNames: Optional[Sequence[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class RetrieveEnvironmentInfoResultMessageTypeDef(BaseValidatorModel):
    EnvironmentInfo: List[EnvironmentInfoDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentResourceDescriptionTypeDef(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    AutoScalingGroups: Optional[List[AutoScalingGroupTypeDef]] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    LaunchConfigurations: Optional[List[LaunchConfigurationTypeDef]] = None
    LaunchTemplates: Optional[List[LaunchTemplateTypeDef]] = None
    LoadBalancers: Optional[List[LoadBalancerTypeDef]] = None
    Triggers: Optional[List[TriggerTypeDef]] = None
    Queues: Optional[List[QueueTypeDef]] = None

class EventDescriptionsMessageTypeDef(BaseValidatorModel):
    Events: List[EventDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAvailableSolutionStacksResultMessageTypeDef(BaseValidatorModel):
    SolutionStacks: List[str]
    SolutionStackDetails: List[SolutionStackDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlatformBranchesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[SearchFilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class ListPlatformBranchesResultTypeDef(BaseValidatorModel):
    PlatformBranchSummaryList: List[PlatformBranchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPlatformVersionsRequestListPlatformVersionsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PlatformFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlatformVersionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[PlatformFilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None

class LoadBalancerDescriptionTypeDef(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    Domain: Optional[str] = None
    Listeners: Optional[List[ListenerTypeDef]] = None

class PlatformDescriptionTypeDef(BaseValidatorModel):
    PlatformArn: Optional[str] = None
    PlatformOwner: Optional[str] = None
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformStatus: Optional[PlatformStatusType] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    PlatformCategory: Optional[str] = None
    Description: Optional[str] = None
    Maintainer: Optional[str] = None
    OperatingSystemName: Optional[str] = None
    OperatingSystemVersion: Optional[str] = None
    ProgrammingLanguages: Optional[List[PlatformProgrammingLanguageTypeDef]] = None
    Frameworks: Optional[List[PlatformFrameworkTypeDef]] = None
    CustomAmiList: Optional[List[CustomAmiTypeDef]] = None
    SupportedTierList: Optional[List[str]] = None
    SupportedAddonList: Optional[List[str]] = None
    PlatformLifecycleState: Optional[str] = None
    PlatformBranchName: Optional[str] = None
    PlatformBranchLifecycleState: Optional[str] = None

class ResourceQuotasTypeDef(BaseValidatorModel):
    ApplicationQuota: Optional[ResourceQuotaTypeDef] = None
    ApplicationVersionQuota: Optional[ResourceQuotaTypeDef] = None
    EnvironmentQuota: Optional[ResourceQuotaTypeDef] = None
    ConfigurationTemplateQuota: Optional[ResourceQuotaTypeDef] = None
    CustomPlatformQuota: Optional[ResourceQuotaTypeDef] = None

class DescribeEnvironmentHealthResultTypeDef(BaseValidatorModel):
    EnvironmentName: str
    HealthStatus: str
    Status: EnvironmentHealthType
    Color: str
    Causes: List[str]
    ApplicationMetrics: ApplicationMetricsTypeDef
    InstancesHealth: InstanceHealthSummaryTypeDef
    RefreshedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationVersionDescriptionMessageTypeDef(BaseValidatorModel):
    ApplicationVersion: ApplicationVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationVersionDescriptionsMessageTypeDef(BaseValidatorModel):
    ApplicationVersions: List[ApplicationVersionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ApplicationResourceLifecycleConfigTypeDef(BaseValidatorModel):
    ServiceRole: Optional[str] = None
    VersionLifecycleConfig: Optional[ApplicationVersionLifecycleConfigTypeDef] = None

class SingleInstanceHealthTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    HealthStatus: Optional[str] = None
    Color: Optional[str] = None
    Causes: Optional[List[str]] = None
    LaunchedAt: Optional[datetime] = None
    ApplicationMetrics: Optional[ApplicationMetricsTypeDef] = None
    System: Optional[SystemStatusTypeDef] = None
    Deployment: Optional[DeploymentTypeDef] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[str] = None

class ConfigurationOptionsDescriptionTypeDef(BaseValidatorModel):
    SolutionStackName: str
    PlatformArn: str
    Options: List[ConfigurationOptionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationSettingsDescriptionsTypeDef(BaseValidatorModel):
    ConfigurationSettings: List[ConfigurationSettingsDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentResourceDescriptionsMessageTypeDef(BaseValidatorModel):
    EnvironmentResources: EnvironmentResourceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentResourcesDescriptionTypeDef(BaseValidatorModel):
    LoadBalancer: Optional[LoadBalancerDescriptionTypeDef] = None

class DescribePlatformVersionResultTypeDef(BaseValidatorModel):
    PlatformDescription: PlatformDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResultTypeDef(BaseValidatorModel):
    ResourceQuotas: ResourceQuotasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationDescriptionTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    ApplicationName: Optional[str] = None
    Description: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    Versions: Optional[List[str]] = None
    ConfigurationTemplates: Optional[List[str]] = None
    ResourceLifecycleConfig: Optional[ApplicationResourceLifecycleConfigTypeDef] = None

class ApplicationResourceLifecycleDescriptionMessageTypeDef(BaseValidatorModel):
    ApplicationName: str
    ResourceLifecycleConfig: ApplicationResourceLifecycleConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    Description: Optional[str] = None
    ResourceLifecycleConfig: Optional[ApplicationResourceLifecycleConfigTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateApplicationResourceLifecycleMessageRequestTypeDef(BaseValidatorModel):
    ApplicationName: str
    ResourceLifecycleConfig: ApplicationResourceLifecycleConfigTypeDef

class DescribeInstancesHealthResultTypeDef(BaseValidatorModel):
    InstanceHealthList: List[SingleInstanceHealthTypeDef]
    RefreshedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EnvironmentDescriptionResponseTypeDef(BaseValidatorModel):
    EnvironmentName: str
    EnvironmentId: str
    ApplicationName: str
    VersionLabel: str
    SolutionStackName: str
    PlatformArn: str
    TemplateName: str
    Description: str
    EndpointURL: str
    CNAME: str
    DateCreated: datetime
    DateUpdated: datetime
    Status: EnvironmentStatusType
    AbortableOperationInProgress: bool
    Health: EnvironmentHealthType
    HealthStatus: EnvironmentHealthStatusType
    Resources: EnvironmentResourcesDescriptionTypeDef
    Tier: EnvironmentTierTypeDef
    EnvironmentLinks: List[EnvironmentLinkTypeDef]
    EnvironmentArn: str
    OperationsRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentDescriptionTypeDef(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    EndpointURL: Optional[str] = None
    CNAME: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    Status: Optional[EnvironmentStatusType] = None
    AbortableOperationInProgress: Optional[bool] = None
    Health: Optional[EnvironmentHealthType] = None
    HealthStatus: Optional[EnvironmentHealthStatusType] = None
    Resources: Optional[EnvironmentResourcesDescriptionTypeDef] = None
    Tier: Optional[EnvironmentTierTypeDef] = None
    EnvironmentLinks: Optional[List[EnvironmentLinkTypeDef]] = None
    EnvironmentArn: Optional[str] = None
    OperationsRole: Optional[str] = None

class ApplicationDescriptionMessageTypeDef(BaseValidatorModel):
    Application: ApplicationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationDescriptionsMessageTypeDef(BaseValidatorModel):
    Applications: List[ApplicationDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentDescriptionsMessageTypeDef(BaseValidatorModel):
    Environments: List[EnvironmentDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

