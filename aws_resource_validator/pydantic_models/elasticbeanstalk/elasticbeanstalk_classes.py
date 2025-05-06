from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.elasticbeanstalk.elasticbeanstalk_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbortEnvironmentUpdateMessage(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Latency(BaseValidatorModel):
    P999: Optional[float] = None
    P99: Optional[float] = None
    P95: Optional[float] = None
    P90: Optional[float] = None
    P85: Optional[float] = None
    P75: Optional[float] = None
    P50: Optional[float] = None
    P10: Optional[float] = None


class StatusCodes(BaseValidatorModel):
    Status2xx: Optional[int] = None
    Status3xx: Optional[int] = None
    Status4xx: Optional[int] = None
    Status5xx: Optional[int] = None


class S3Location(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None


class SourceBuildInformation(BaseValidatorModel):
    SourceType: SourceTypeType
    SourceRepository: SourceRepositoryType
    SourceLocation: str


class MaxAgeRule(BaseValidatorModel):
    Enabled: bool
    MaxAgeInDays: Optional[int] = None
    DeleteSourceFromS3: Optional[bool] = None


class MaxCountRule(BaseValidatorModel):
    Enabled: bool
    MaxCount: Optional[int] = None
    DeleteSourceFromS3: Optional[bool] = None


class ApplyEnvironmentManagedActionRequest(BaseValidatorModel):
    ActionId: str
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None


class AssociateEnvironmentOperationsRoleMessage(BaseValidatorModel):
    EnvironmentName: str
    OperationsRole: str


class AutoScalingGroup(BaseValidatorModel):
    Name: Optional[str] = None


class BuildConfiguration(BaseValidatorModel):
    CodeBuildServiceRole: str
    Image: str
    ArtifactName: Optional[str] = None
    ComputeType: Optional[ComputeTypeType] = None
    TimeoutInMinutes: Optional[int] = None


class Builder(BaseValidatorModel):
    ARN: Optional[str] = None


class CPUUtilization(BaseValidatorModel):
    User: Optional[float] = None
    Nice: Optional[float] = None
    System: Optional[float] = None
    Idle: Optional[float] = None
    IOWait: Optional[float] = None
    IRQ: Optional[float] = None
    SoftIRQ: Optional[float] = None
    Privileged: Optional[float] = None


class CheckDNSAvailabilityMessage(BaseValidatorModel):
    CNAMEPrefix: str


class ComposeEnvironmentsMessage(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    GroupName: Optional[str] = None
    VersionLabels: Optional[List[str]] = None


class OptionRestrictionRegex(BaseValidatorModel):
    Pattern: Optional[str] = None
    Label: Optional[str] = None


class ConfigurationOptionSetting(BaseValidatorModel):
    ResourceName: Optional[str] = None
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None
    Value: Optional[str] = None


class ValidationMessage(BaseValidatorModel):
    Message: Optional[str] = None
    Severity: Optional[ValidationSeverityType] = None
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class SourceConfiguration(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    TemplateName: Optional[str] = None


class EnvironmentTier(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Version: Optional[str] = None


class OptionSpecification(BaseValidatorModel):
    ResourceName: Optional[str] = None
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None


class PlatformSummary(BaseValidatorModel):
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


class CustomAmi(BaseValidatorModel):
    VirtualizationType: Optional[str] = None
    ImageId: Optional[str] = None


class DeleteApplicationMessage(BaseValidatorModel):
    ApplicationName: str
    TerminateEnvByForce: Optional[bool] = None


class DeleteApplicationVersionMessage(BaseValidatorModel):
    ApplicationName: str
    VersionLabel: str
    DeleteSourceBundle: Optional[bool] = None


class DeleteConfigurationTemplateMessage(BaseValidatorModel):
    ApplicationName: str
    TemplateName: str


class DeleteEnvironmentConfigurationMessage(BaseValidatorModel):
    ApplicationName: str
    EnvironmentName: str


class DeletePlatformVersionRequest(BaseValidatorModel):
    PlatformArn: Optional[str] = None


class Deployment(BaseValidatorModel):
    VersionLabel: Optional[str] = None
    DeploymentId: Optional[int] = None
    Status: Optional[str] = None
    DeploymentTime: Optional[datetime] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeApplicationVersionsMessage(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabels: Optional[List[str]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeApplicationsMessage(BaseValidatorModel):
    ApplicationNames: Optional[List[str]] = None


class DescribeConfigurationSettingsMessage(BaseValidatorModel):
    ApplicationName: str
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None


class DescribeEnvironmentHealthRequest(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    AttributeNames: Optional[List[EnvironmentHealthAttributeType]] = None


class InstanceHealthSummary(BaseValidatorModel):
    NoData: Optional[int] = None
    Unknown: Optional[int] = None
    Pending: Optional[int] = None
    Ok: Optional[int] = None
    Info: Optional[int] = None
    Warning: Optional[int] = None
    Degraded: Optional[int] = None
    Severe: Optional[int] = None


class DescribeEnvironmentManagedActionHistoryRequest(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxItems: Optional[int] = None


class ManagedActionHistoryItem(BaseValidatorModel):
    ActionId: Optional[str] = None
    ActionType: Optional[ActionTypeType] = None
    ActionDescription: Optional[str] = None
    FailureType: Optional[FailureTypeType] = None
    Status: Optional[ActionHistoryStatusType] = None
    FailureDescription: Optional[str] = None
    ExecutedTime: Optional[datetime] = None
    FinishedTime: Optional[datetime] = None


class DescribeEnvironmentManagedActionsRequest(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    Status: Optional[ActionStatusType] = None


class ManagedAction(BaseValidatorModel):
    ActionId: Optional[str] = None
    ActionDescription: Optional[str] = None
    ActionType: Optional[ActionTypeType] = None
    Status: Optional[ActionStatusType] = None
    WindowStartTime: Optional[datetime] = None


class DescribeEnvironmentResourcesMessage(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None

Timestamp = Union[datetime, str]


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeInstancesHealthRequest(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    AttributeNames: Optional[List[InstancesHealthAttributeType]] = None
    NextToken: Optional[str] = None


class DescribePlatformVersionRequest(BaseValidatorModel):
    PlatformArn: Optional[str] = None


class DisassociateEnvironmentOperationsRoleMessage(BaseValidatorModel):
    EnvironmentName: str


class EnvironmentLink(BaseValidatorModel):
    LinkName: Optional[str] = None
    EnvironmentName: Optional[str] = None


class EnvironmentInfoDescription(BaseValidatorModel):
    InfoType: Optional[EnvironmentInfoTypeType] = None
    Ec2InstanceId: Optional[str] = None
    SampleTimestamp: Optional[datetime] = None
    Message: Optional[str] = None


class Instance(BaseValidatorModel):
    Id: Optional[str] = None


class LaunchConfiguration(BaseValidatorModel):
    Name: Optional[str] = None


class LaunchTemplate(BaseValidatorModel):
    Id: Optional[str] = None


class LoadBalancer(BaseValidatorModel):
    Name: Optional[str] = None


class Queue(BaseValidatorModel):
    Name: Optional[str] = None
    URL: Optional[str] = None


class Trigger(BaseValidatorModel):
    Name: Optional[str] = None


class EventDescription(BaseValidatorModel):
    EventDate: Optional[datetime] = None
    Message: Optional[str] = None
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PlatformArn: Optional[str] = None
    RequestId: Optional[str] = None
    Severity: Optional[EventSeverityType] = None


class SolutionStackDescription(BaseValidatorModel):
    SolutionStackName: Optional[str] = None
    PermittedFileTypes: Optional[List[str]] = None


class SearchFilter(BaseValidatorModel):
    Attribute: Optional[str] = None
    Operator: Optional[str] = None
    Values: Optional[List[str]] = None


class PlatformBranchSummary(BaseValidatorModel):
    PlatformName: Optional[str] = None
    BranchName: Optional[str] = None
    LifecycleState: Optional[str] = None
    BranchOrder: Optional[int] = None
    SupportedTierList: Optional[List[str]] = None


class PlatformFilter(BaseValidatorModel):
    Type: Optional[str] = None
    Operator: Optional[str] = None
    Values: Optional[List[str]] = None


class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceArn: str


class Listener(BaseValidatorModel):
    Protocol: Optional[str] = None
    Port: Optional[int] = None


class PlatformFramework(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class PlatformProgrammingLanguage(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None


class RebuildEnvironmentMessage(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None


class RequestEnvironmentInfoMessage(BaseValidatorModel):
    InfoType: EnvironmentInfoTypeType
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None


class ResourceQuota(BaseValidatorModel):
    Maximum: Optional[int] = None


class RestartAppServerMessage(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None


class RetrieveEnvironmentInfoMessage(BaseValidatorModel):
    InfoType: EnvironmentInfoTypeType
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None


class SwapEnvironmentCNAMEsMessage(BaseValidatorModel):
    SourceEnvironmentId: Optional[str] = None
    SourceEnvironmentName: Optional[str] = None
    DestinationEnvironmentId: Optional[str] = None
    DestinationEnvironmentName: Optional[str] = None


class TerminateEnvironmentMessage(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    TerminateResources: Optional[bool] = None
    ForceTerminate: Optional[bool] = None


class UpdateApplicationMessage(BaseValidatorModel):
    ApplicationName: str
    Description: Optional[str] = None


class UpdateApplicationVersionMessage(BaseValidatorModel):
    ApplicationName: str
    VersionLabel: str
    Description: Optional[str] = None


class ApplyEnvironmentManagedActionResult(BaseValidatorModel):
    ActionId: str
    ActionDescription: str
    ActionType: ActionTypeType
    Status: str
    ResponseMetadata: ResponseMetadata


class CheckDNSAvailabilityResultMessage(BaseValidatorModel):
    Available: bool
    FullyQualifiedCNAME: str
    ResponseMetadata: ResponseMetadata


class CreateStorageLocationResultMessage(BaseValidatorModel):
    S3Bucket: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ApplicationMetrics(BaseValidatorModel):
    Duration: Optional[int] = None
    RequestCount: Optional[int] = None
    StatusCodes: Optional[StatusCodes] = None
    Latency: Optional[Latency] = None


class ApplicationVersionDescription(BaseValidatorModel):
    ApplicationVersionArn: Optional[str] = None
    ApplicationName: Optional[str] = None
    Description: Optional[str] = None
    VersionLabel: Optional[str] = None
    SourceBuildInformation: Optional[SourceBuildInformation] = None
    BuildArn: Optional[str] = None
    SourceBundle: Optional[S3Location] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    Status: Optional[ApplicationVersionStatusType] = None


class ApplicationVersionLifecycleConfig(BaseValidatorModel):
    MaxCountRule: Optional[MaxCountRule] = None
    MaxAgeRule: Optional[MaxAgeRule] = None


class SystemStatus(BaseValidatorModel):
    CPUUtilization: Optional[CPUUtilization] = None
    LoadAverage: Optional[List[float]] = None


class ConfigurationOptionDescription(BaseValidatorModel):
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
    Regex: Optional[OptionRestrictionRegex] = None


class ConfigurationSettingsDescriptionResponse(BaseValidatorModel):
    SolutionStackName: str
    PlatformArn: str
    ApplicationName: str
    TemplateName: str
    Description: str
    EnvironmentName: str
    DeploymentStatus: ConfigurationDeploymentStatusType
    DateCreated: datetime
    DateUpdated: datetime
    OptionSettings: List[ConfigurationOptionSetting]
    ResponseMetadata: ResponseMetadata


class ConfigurationSettingsDescription(BaseValidatorModel):
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    ApplicationName: Optional[str] = None
    TemplateName: Optional[str] = None
    Description: Optional[str] = None
    EnvironmentName: Optional[str] = None
    DeploymentStatus: Optional[ConfigurationDeploymentStatusType] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    OptionSettings: Optional[List[ConfigurationOptionSetting]] = None


class ValidateConfigurationSettingsMessage(BaseValidatorModel):
    ApplicationName: str
    OptionSettings: List[ConfigurationOptionSetting]
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None


class ConfigurationSettingsValidationMessages(BaseValidatorModel):
    Messages: List[ValidationMessage]
    ResponseMetadata: ResponseMetadata


class CreateApplicationVersionMessage(BaseValidatorModel):
    ApplicationName: str
    VersionLabel: str
    Description: Optional[str] = None
    SourceBuildInformation: Optional[SourceBuildInformation] = None
    SourceBundle: Optional[S3Location] = None
    BuildConfiguration: Optional[BuildConfiguration] = None
    AutoCreateApplication: Optional[bool] = None
    Process: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class CreatePlatformVersionRequest(BaseValidatorModel):
    PlatformName: str
    PlatformVersion: str
    PlatformDefinitionBundle: S3Location
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[ConfigurationOptionSetting]] = None
    Tags: Optional[List[Tag]] = None


class ResourceTagsDescriptionMessage(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateTagsForResourceMessage(BaseValidatorModel):
    ResourceArn: str
    TagsToAdd: Optional[List[Tag]] = None
    TagsToRemove: Optional[List[str]] = None


class CreateConfigurationTemplateMessage(BaseValidatorModel):
    ApplicationName: str
    TemplateName: str
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    SourceConfiguration: Optional[SourceConfiguration] = None
    EnvironmentId: Optional[str] = None
    Description: Optional[str] = None
    OptionSettings: Optional[List[ConfigurationOptionSetting]] = None
    Tags: Optional[List[Tag]] = None


class CreateEnvironmentMessage(BaseValidatorModel):
    ApplicationName: str
    EnvironmentName: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    CNAMEPrefix: Optional[str] = None
    Tier: Optional[EnvironmentTier] = None
    Tags: Optional[List[Tag]] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    OptionSettings: Optional[List[ConfigurationOptionSetting]] = None
    OptionsToRemove: Optional[List[OptionSpecification]] = None
    OperationsRole: Optional[str] = None


class DescribeConfigurationOptionsMessage(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentName: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    Options: Optional[List[OptionSpecification]] = None


class UpdateConfigurationTemplateMessage(BaseValidatorModel):
    ApplicationName: str
    TemplateName: str
    Description: Optional[str] = None
    OptionSettings: Optional[List[ConfigurationOptionSetting]] = None
    OptionsToRemove: Optional[List[OptionSpecification]] = None


class UpdateEnvironmentMessage(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    Tier: Optional[EnvironmentTier] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    SolutionStackName: Optional[str] = None
    PlatformArn: Optional[str] = None
    OptionSettings: Optional[List[ConfigurationOptionSetting]] = None
    OptionsToRemove: Optional[List[OptionSpecification]] = None


class CreatePlatformVersionResult(BaseValidatorModel):
    PlatformSummary: PlatformSummary
    Builder: Builder
    ResponseMetadata: ResponseMetadata


class DeletePlatformVersionResult(BaseValidatorModel):
    PlatformSummary: PlatformSummary
    ResponseMetadata: ResponseMetadata


class ListPlatformVersionsResult(BaseValidatorModel):
    PlatformSummaryList: List[PlatformSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeApplicationVersionsMessagePaginate(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabels: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEnvironmentManagedActionHistoryRequestPaginate(BaseValidatorModel):
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEnvironmentManagedActionHistoryResult(BaseValidatorModel):
    ManagedActionHistoryItems: List[ManagedActionHistoryItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEnvironmentManagedActionsResult(BaseValidatorModel):
    ManagedActions: List[ManagedAction]
    ResponseMetadata: ResponseMetadata


class DescribeEnvironmentsMessagePaginate(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[List[str]] = None
    EnvironmentNames: Optional[List[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEnvironmentsMessage(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[List[str]] = None
    EnvironmentNames: Optional[List[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PlatformArn: Optional[str] = None
    RequestId: Optional[str] = None
    Severity: Optional[EventSeverityType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsMessage(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    TemplateName: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentName: Optional[str] = None
    PlatformArn: Optional[str] = None
    RequestId: Optional[str] = None
    Severity: Optional[EventSeverityType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeEnvironmentsMessageWaitExtraExtra(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[List[str]] = None
    EnvironmentNames: Optional[List[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEnvironmentsMessageWaitExtra(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[List[str]] = None
    EnvironmentNames: Optional[List[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEnvironmentsMessageWait(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    VersionLabel: Optional[str] = None
    EnvironmentIds: Optional[List[str]] = None
    EnvironmentNames: Optional[List[str]] = None
    IncludeDeleted: Optional[bool] = None
    IncludedDeletedBackTo: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class RetrieveEnvironmentInfoResultMessage(BaseValidatorModel):
    EnvironmentInfo: List[EnvironmentInfoDescription]
    ResponseMetadata: ResponseMetadata


class EnvironmentResourceDescription(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    AutoScalingGroups: Optional[List[AutoScalingGroup]] = None
    Instances: Optional[List[Instance]] = None
    LaunchConfigurations: Optional[List[LaunchConfiguration]] = None
    LaunchTemplates: Optional[List[LaunchTemplate]] = None
    LoadBalancers: Optional[List[LoadBalancer]] = None
    Triggers: Optional[List[Trigger]] = None
    Queues: Optional[List[Queue]] = None


class EventDescriptionsMessage(BaseValidatorModel):
    Events: List[EventDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAvailableSolutionStacksResultMessage(BaseValidatorModel):
    SolutionStacks: List[str]
    SolutionStackDetails: List[SolutionStackDescription]
    ResponseMetadata: ResponseMetadata


class ListPlatformBranchesRequest(BaseValidatorModel):
    Filters: Optional[List[SearchFilter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class ListPlatformBranchesResult(BaseValidatorModel):
    PlatformBranchSummaryList: List[PlatformBranchSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPlatformVersionsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[PlatformFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPlatformVersionsRequest(BaseValidatorModel):
    Filters: Optional[List[PlatformFilter]] = None
    MaxRecords: Optional[int] = None
    NextToken: Optional[str] = None


class LoadBalancerDescription(BaseValidatorModel):
    LoadBalancerName: Optional[str] = None
    Domain: Optional[str] = None
    Listeners: Optional[List[Listener]] = None


class PlatformDescription(BaseValidatorModel):
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
    ProgrammingLanguages: Optional[List[PlatformProgrammingLanguage]] = None
    Frameworks: Optional[List[PlatformFramework]] = None
    CustomAmiList: Optional[List[CustomAmi]] = None
    SupportedTierList: Optional[List[str]] = None
    SupportedAddonList: Optional[List[str]] = None
    PlatformLifecycleState: Optional[str] = None
    PlatformBranchName: Optional[str] = None
    PlatformBranchLifecycleState: Optional[str] = None


class ResourceQuotas(BaseValidatorModel):
    ApplicationQuota: Optional[ResourceQuota] = None
    ApplicationVersionQuota: Optional[ResourceQuota] = None
    EnvironmentQuota: Optional[ResourceQuota] = None
    ConfigurationTemplateQuota: Optional[ResourceQuota] = None
    CustomPlatformQuota: Optional[ResourceQuota] = None


class DescribeEnvironmentHealthResult(BaseValidatorModel):
    EnvironmentName: str
    HealthStatus: str
    Status: EnvironmentHealthType
    Color: str
    Causes: List[str]
    ApplicationMetrics: ApplicationMetrics
    InstancesHealth: InstanceHealthSummary
    RefreshedAt: datetime
    ResponseMetadata: ResponseMetadata


class ApplicationVersionDescriptionMessage(BaseValidatorModel):
    ApplicationVersion: ApplicationVersionDescription
    ResponseMetadata: ResponseMetadata


class ApplicationVersionDescriptionsMessage(BaseValidatorModel):
    ApplicationVersions: List[ApplicationVersionDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ApplicationResourceLifecycleConfig(BaseValidatorModel):
    ServiceRole: Optional[str] = None
    VersionLifecycleConfig: Optional[ApplicationVersionLifecycleConfig] = None


class SingleInstanceHealth(BaseValidatorModel):
    InstanceId: Optional[str] = None
    HealthStatus: Optional[str] = None
    Color: Optional[str] = None
    Causes: Optional[List[str]] = None
    LaunchedAt: Optional[datetime] = None
    ApplicationMetrics: Optional[ApplicationMetrics] = None
    System: Optional[SystemStatus] = None
    Deployment: Optional[Deployment] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[str] = None


class ConfigurationOptionsDescription(BaseValidatorModel):
    SolutionStackName: str
    PlatformArn: str
    Options: List[ConfigurationOptionDescription]
    ResponseMetadata: ResponseMetadata


class ConfigurationSettingsDescriptions(BaseValidatorModel):
    ConfigurationSettings: List[ConfigurationSettingsDescription]
    ResponseMetadata: ResponseMetadata


class EnvironmentResourceDescriptionsMessage(BaseValidatorModel):
    EnvironmentResources: EnvironmentResourceDescription
    ResponseMetadata: ResponseMetadata


class EnvironmentResourcesDescription(BaseValidatorModel):
    LoadBalancer: Optional[LoadBalancerDescription] = None


class DescribePlatformVersionResult(BaseValidatorModel):
    PlatformDescription: PlatformDescription
    ResponseMetadata: ResponseMetadata


class DescribeAccountAttributesResult(BaseValidatorModel):
    ResourceQuotas: ResourceQuotas
    ResponseMetadata: ResponseMetadata


class ApplicationDescription(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    ApplicationName: Optional[str] = None
    Description: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateUpdated: Optional[datetime] = None
    Versions: Optional[List[str]] = None
    ConfigurationTemplates: Optional[List[str]] = None
    ResourceLifecycleConfig: Optional[ApplicationResourceLifecycleConfig] = None


class ApplicationResourceLifecycleDescriptionMessage(BaseValidatorModel):
    ApplicationName: str
    ResourceLifecycleConfig: ApplicationResourceLifecycleConfig
    ResponseMetadata: ResponseMetadata


class CreateApplicationMessage(BaseValidatorModel):
    ApplicationName: str
    Description: Optional[str] = None
    ResourceLifecycleConfig: Optional[ApplicationResourceLifecycleConfig] = None
    Tags: Optional[List[Tag]] = None


class UpdateApplicationResourceLifecycleMessage(BaseValidatorModel):
    ApplicationName: str
    ResourceLifecycleConfig: ApplicationResourceLifecycleConfig


class DescribeInstancesHealthResult(BaseValidatorModel):
    InstanceHealthList: List[SingleInstanceHealth]
    RefreshedAt: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EnvironmentDescriptionResponse(BaseValidatorModel):
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
    Resources: EnvironmentResourcesDescription
    Tier: EnvironmentTier
    EnvironmentLinks: List[EnvironmentLink]
    EnvironmentArn: str
    OperationsRole: str
    ResponseMetadata: ResponseMetadata


class EnvironmentDescription(BaseValidatorModel):
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
    Resources: Optional[EnvironmentResourcesDescription] = None
    Tier: Optional[EnvironmentTier] = None
    EnvironmentLinks: Optional[List[EnvironmentLink]] = None
    EnvironmentArn: Optional[str] = None
    OperationsRole: Optional[str] = None


class ApplicationDescriptionMessage(BaseValidatorModel):
    Application: ApplicationDescription
    ResponseMetadata: ResponseMetadata


class ApplicationDescriptionsMessage(BaseValidatorModel):
    Applications: List[ApplicationDescription]
    ResponseMetadata: ResponseMetadata


class EnvironmentDescriptionsMessage(BaseValidatorModel):
    Environments: List[EnvironmentDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None