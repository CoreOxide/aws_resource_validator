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
from aws_resource_validator.pydantic_models.appconfig_constants import *

class DeletionProtectionSettings(BaseValidatorModel):
    Enabled: Optional[bool] = None
    ProtectionPeriodInMinutes: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActionInvocation(BaseValidatorModel):
    ExtensionIdentifier: Optional[str] = None
    ActionName: Optional[str] = None
    Uri: Optional[str] = None
    RoleArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    InvocationId: Optional[str] = None


class Action(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Uri: Optional[str] = None
    RoleArn: Optional[str] = None


class Application(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class AppliedExtension(BaseValidatorModel):
    ExtensionId: Optional[str] = None
    ExtensionAssociationId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Parameters: Optional[Dict[str, str]] = None


class CreateApplicationRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateDeploymentStrategyRequest(BaseValidatorModel):
    Name: str
    DeploymentDurationInMinutes: int
    GrowthFactor: float
    Description: Optional[str] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    ReplicateTo: Optional[ReplicateToType] = None
    Tags: Optional[Mapping[str, str]] = None


class Monitor(BaseValidatorModel):
    AlarmArn: str
    AlarmRoleArn: Optional[str] = None


class CreateExtensionAssociationRequest(BaseValidatorModel):
    ExtensionIdentifier: str
    ResourceIdentifier: str
    ExtensionVersionNumber: Optional[int] = None
    Parameters: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteApplicationRequest(BaseValidatorModel):
    ApplicationId: str


class DeleteConfigurationProfileRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    DeletionProtectionCheck: Optional[DeletionProtectionCheckType] = None


class DeleteDeploymentStrategyRequest(BaseValidatorModel):
    DeploymentStrategyId: str


class DeleteEnvironmentRequest(BaseValidatorModel):
    EnvironmentId: str
    ApplicationId: str
    DeletionProtectionCheck: Optional[DeletionProtectionCheckType] = None


class DeleteExtensionAssociationRequest(BaseValidatorModel):
    ExtensionAssociationId: str


class DeleteExtensionRequest(BaseValidatorModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None


class DeleteHostedConfigurationVersionRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int


class DeploymentStrategy(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    GrowthFactor: Optional[float] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    ReplicateTo: Optional[ReplicateToType] = None


class DeploymentSummary(BaseValidatorModel):
    DeploymentNumber: Optional[int] = None
    ConfigurationName: Optional[str] = None
    ConfigurationVersion: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    GrowthFactor: Optional[float] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    State: Optional[DeploymentStateType] = None
    PercentageComplete: Optional[float] = None
    StartedAt: Optional[datetime] = None
    CompletedAt: Optional[datetime] = None
    VersionLabel: Optional[str] = None


class ExtensionAssociationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    ExtensionArn: Optional[str] = None
    ResourceArn: Optional[str] = None


class ExtensionSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None


class GetApplicationRequest(BaseValidatorModel):
    ApplicationId: str


class GetConfigurationProfileRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str


class GetConfigurationRequest(BaseValidatorModel):
    Application: str
    Environment: str
    Configuration: str
    ClientId: str
    ClientConfigurationVersion: Optional[str] = None


class GetDeploymentRequest(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int


class GetDeploymentStrategyRequest(BaseValidatorModel):
    DeploymentStrategyId: str


class GetEnvironmentRequest(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str


class GetExtensionAssociationRequest(BaseValidatorModel):
    ExtensionAssociationId: str


class GetExtensionRequest(BaseValidatorModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None


class GetHostedConfigurationVersionRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int


class HostedConfigurationVersionSummary(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ConfigurationProfileId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Description: Optional[str] = None
    ContentType: Optional[str] = None
    VersionLabel: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDeploymentStrategiesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDeploymentsRequest(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEnvironmentsRequest(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListExtensionAssociationsRequest(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListExtensionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Name: Optional[str] = None


class ListHostedConfigurationVersionsRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VersionLabel: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class StartDeploymentRequest(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyIdentifier: Optional[str] = None
    DynamicExtensionParameters: Optional[Mapping[str, str]] = None


class StopDeploymentRequest(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int
    AllowRevert: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateApplicationRequest(BaseValidatorModel):
    ApplicationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateDeploymentStrategyRequest(BaseValidatorModel):
    DeploymentStrategyId: str
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthFactor: Optional[float] = None
    GrowthType: Optional[GrowthTypeType] = None


class UpdateExtensionAssociationRequest(BaseValidatorModel):
    ExtensionAssociationId: str
    Parameters: Optional[Mapping[str, str]] = None


class ValidateConfigurationRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str


class UpdateAccountSettingsRequest(BaseValidatorModel):
    DeletionProtection: Optional[DeletionProtectionSettings] = None


class AccountSettings(BaseValidatorModel):
    DeletionProtection: DeletionProtectionSettings
    ResponseMetadata: ResponseMetadata


class ApplicationResponse(BaseValidatorModel):
    Id: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadata


class Configuration(BaseValidatorModel):
    Content: StreamingBody
    ConfigurationVersion: str
    ContentType: str
    ResponseMetadata: ResponseMetadata


class DeploymentStrategyResponse(BaseValidatorModel):
    Id: str
    Name: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthTypeType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    ReplicateTo: ReplicateToType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExtensionAssociation(BaseValidatorModel):
    Id: str
    ExtensionArn: str
    ResourceArn: str
    Arn: str
    Parameters: Dict[str, str]
    ExtensionVersionNumber: int
    ResponseMetadata: ResponseMetadata


class HostedConfigurationVersion(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int
    Description: str
    Content: StreamingBody
    ContentType: str
    VersionLabel: str
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class ResourceTags(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeploymentEvent(BaseValidatorModel):
    EventType: Optional[DeploymentEventTypeType] = None
    TriggeredBy: Optional[TriggeredByType] = None
    Description: Optional[str] = None
    ActionInvocations: Optional[List[ActionInvocation]] = None
    OccurredAt: Optional[datetime] = None


class Applications(BaseValidatorModel):
    Items: List[Application]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class CreateHostedConfigurationVersionRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Content: Blob
    ContentType: str
    Description: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    VersionLabel: Optional[str] = None


class ConfigurationProfileSummary(BaseValidatorModel):
    pass


class ConfigurationProfiles(BaseValidatorModel):
    Items: List[ConfigurationProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Validator(BaseValidatorModel):
    pass


class UpdateConfigurationProfileRequest(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RetrievalRoleArn: Optional[str] = None
    Validators: Optional[Sequence[Validator]] = None
    KmsKeyIdentifier: Optional[str] = None


class CreateEnvironmentRequest(BaseValidatorModel):
    ApplicationId: str
    Name: str
    Description: Optional[str] = None
    Monitors: Optional[Sequence[Monitor]] = None
    Tags: Optional[Mapping[str, str]] = None


class EnvironmentResponse(BaseValidatorModel):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    State: EnvironmentStateType
    Monitors: List[Monitor]
    ResponseMetadata: ResponseMetadata


class Environment(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[EnvironmentStateType] = None
    Monitors: Optional[List[Monitor]] = None


class UpdateEnvironmentRequest(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Monitors: Optional[Sequence[Monitor]] = None


class Parameter(BaseValidatorModel):
    pass


class CreateExtensionRequest(BaseValidatorModel):
    Name: str
    Actions: Mapping[ActionPointType, Sequence[Action]]
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, Parameter]] = None
    Tags: Optional[Mapping[str, str]] = None
    LatestVersionNumber: Optional[int] = None


class Extension(BaseValidatorModel):
    Id: str
    Name: str
    VersionNumber: int
    Arn: str
    Description: str
    Actions: Dict[ActionPointType, List[Action]]
    Parameters: Dict[str, Parameter]
    ResponseMetadata: ResponseMetadata


class UpdateExtensionRequest(BaseValidatorModel):
    ExtensionIdentifier: str
    Description: Optional[str] = None
    Actions: Optional[Mapping[ActionPointType, Sequence[Action]]] = None
    Parameters: Optional[Mapping[str, Parameter]] = None
    VersionNumber: Optional[int] = None


class DeploymentStrategies(BaseValidatorModel):
    Items: List[DeploymentStrategy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Deployments(BaseValidatorModel):
    Items: List[DeploymentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExtensionAssociations(BaseValidatorModel):
    Items: List[ExtensionAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Extensions(BaseValidatorModel):
    Items: List[ExtensionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HostedConfigurationVersions(BaseValidatorModel):
    Items: List[HostedConfigurationVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentStrategiesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsRequestPaginate(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExtensionAssociationsRequestPaginate(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExtensionsRequestPaginate(BaseValidatorModel):
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHostedConfigurationVersionsRequestPaginate(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionLabel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class Deployment(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    DeploymentNumber: int
    ConfigurationName: str
    ConfigurationLocationUri: str
    ConfigurationVersion: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthTypeType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    State: DeploymentStateType
    EventLog: List[DeploymentEvent]
    PercentageComplete: float
    StartedAt: datetime
    CompletedAt: datetime
    AppliedExtensions: List[AppliedExtension]
    KmsKeyArn: str
    KmsKeyIdentifier: str
    VersionLabel: str
    ResponseMetadata: ResponseMetadata


class Environments(BaseValidatorModel):
    Items: List[Environment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


