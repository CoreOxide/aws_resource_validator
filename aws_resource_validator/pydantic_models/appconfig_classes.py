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

class DeletionProtectionSettingsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    ProtectionPeriodInMinutes: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActionInvocationTypeDef(BaseValidatorModel):
    ExtensionIdentifier: Optional[str] = None
    ActionName: Optional[str] = None
    Uri: Optional[str] = None
    RoleArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    InvocationId: Optional[str] = None


class ActionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Uri: Optional[str] = None
    RoleArn: Optional[str] = None


class ApplicationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class AppliedExtensionTypeDef(BaseValidatorModel):
    ExtensionId: Optional[str] = None
    ExtensionAssociationId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Parameters: Optional[Dict[str, str]] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateDeploymentStrategyRequestTypeDef(BaseValidatorModel):
    Name: str
    DeploymentDurationInMinutes: int
    GrowthFactor: float
    Description: Optional[str] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    ReplicateTo: Optional[ReplicateToType] = None
    Tags: Optional[Mapping[str, str]] = None


class MonitorTypeDef(BaseValidatorModel):
    AlarmArn: str
    AlarmRoleArn: Optional[str] = None


class CreateExtensionAssociationRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    ResourceIdentifier: str
    ExtensionVersionNumber: Optional[int] = None
    Parameters: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class DeleteConfigurationProfileRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    DeletionProtectionCheck: Optional[DeletionProtectionCheckType] = None


class DeleteDeploymentStrategyRequestTypeDef(BaseValidatorModel):
    DeploymentStrategyId: str


class DeleteEnvironmentRequestTypeDef(BaseValidatorModel):
    EnvironmentId: str
    ApplicationId: str
    DeletionProtectionCheck: Optional[DeletionProtectionCheckType] = None


class DeleteExtensionAssociationRequestTypeDef(BaseValidatorModel):
    ExtensionAssociationId: str


class DeleteExtensionRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None


class DeleteHostedConfigurationVersionRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int


class DeploymentStrategyTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    GrowthFactor: Optional[float] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    ReplicateTo: Optional[ReplicateToType] = None


class DeploymentSummaryTypeDef(BaseValidatorModel):
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


class ExtensionAssociationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ExtensionArn: Optional[str] = None
    ResourceArn: Optional[str] = None


class ExtensionSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None


class GetApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class GetConfigurationProfileRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str


class GetConfigurationRequestTypeDef(BaseValidatorModel):
    Application: str
    Environment: str
    Configuration: str
    ClientId: str
    ClientConfigurationVersion: Optional[str] = None


class GetDeploymentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int


class GetDeploymentStrategyRequestTypeDef(BaseValidatorModel):
    DeploymentStrategyId: str


class GetEnvironmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str


class GetExtensionAssociationRequestTypeDef(BaseValidatorModel):
    ExtensionAssociationId: str


class GetExtensionRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None


class GetHostedConfigurationVersionRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int


class HostedConfigurationVersionSummaryTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ConfigurationProfileId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Description: Optional[str] = None
    ContentType: Optional[str] = None
    VersionLabel: Optional[str] = None
    KmsKeyArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDeploymentStrategiesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDeploymentsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEnvironmentsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListExtensionAssociationsRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListExtensionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Name: Optional[str] = None


class ListHostedConfigurationVersionsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VersionLabel: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class StartDeploymentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyIdentifier: Optional[str] = None
    DynamicExtensionParameters: Optional[Mapping[str, str]] = None


class StopDeploymentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int
    AllowRevert: Optional[bool] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateDeploymentStrategyRequestTypeDef(BaseValidatorModel):
    DeploymentStrategyId: str
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthFactor: Optional[float] = None
    GrowthType: Optional[GrowthTypeType] = None


class UpdateExtensionAssociationRequestTypeDef(BaseValidatorModel):
    ExtensionAssociationId: str
    Parameters: Optional[Mapping[str, str]] = None


class ValidateConfigurationRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str


class UpdateAccountSettingsRequestTypeDef(BaseValidatorModel):
    DeletionProtection: Optional[DeletionProtectionSettingsTypeDef] = None


class AccountSettingsTypeDef(BaseValidatorModel):
    DeletionProtection: DeletionProtectionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApplicationResponseTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class ConfigurationTypeDef(BaseValidatorModel):
    Content: StreamingBody
    ConfigurationVersion: str
    ContentType: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentStrategyResponseTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthTypeType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    ReplicateTo: ReplicateToType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExtensionAssociationTypeDef(BaseValidatorModel):
    Id: str
    ExtensionArn: str
    ResourceArn: str
    Arn: str
    Parameters: Dict[str, str]
    ExtensionVersionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class HostedConfigurationVersionTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int
    Description: str
    Content: StreamingBody
    ContentType: str
    VersionLabel: str
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceTagsTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentEventTypeDef(BaseValidatorModel):
    EventType: Optional[DeploymentEventTypeType] = None
    TriggeredBy: Optional[TriggeredByType] = None
    Description: Optional[str] = None
    ActionInvocations: Optional[List[ActionInvocationTypeDef]] = None
    OccurredAt: Optional[datetime] = None


class ApplicationsTypeDef(BaseValidatorModel):
    Items: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class CreateHostedConfigurationVersionRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Content: BlobTypeDef
    ContentType: str
    Description: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    VersionLabel: Optional[str] = None


class ConfigurationProfileSummaryTypeDef(BaseValidatorModel):
    pass


class ConfigurationProfilesTypeDef(BaseValidatorModel):
    Items: List[ConfigurationProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ValidatorTypeDef(BaseValidatorModel):
    pass


class UpdateConfigurationProfileRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RetrievalRoleArn: Optional[str] = None
    Validators: Optional[Sequence[ValidatorTypeDef]] = None
    KmsKeyIdentifier: Optional[str] = None


class CreateEnvironmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Name: str
    Description: Optional[str] = None
    Monitors: Optional[Sequence[MonitorTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None


class EnvironmentResponseTypeDef(BaseValidatorModel):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    State: EnvironmentStateType
    Monitors: List[MonitorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EnvironmentTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[EnvironmentStateType] = None
    Monitors: Optional[List[MonitorTypeDef]] = None


class UpdateEnvironmentRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Monitors: Optional[Sequence[MonitorTypeDef]] = None


class ParameterTypeDef(BaseValidatorModel):
    pass


class CreateExtensionRequestTypeDef(BaseValidatorModel):
    Name: str
    Actions: Mapping[ActionPointType, Sequence[ActionTypeDef]]
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, ParameterTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    LatestVersionNumber: Optional[int] = None


class ExtensionTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    VersionNumber: int
    Arn: str
    Description: str
    Actions: Dict[ActionPointType, List[ActionTypeDef]]
    Parameters: Dict[str, ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateExtensionRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    Description: Optional[str] = None
    Actions: Optional[Mapping[ActionPointType, Sequence[ActionTypeDef]]] = None
    Parameters: Optional[Mapping[str, ParameterTypeDef]] = None
    VersionNumber: Optional[int] = None


class DeploymentStrategiesTypeDef(BaseValidatorModel):
    Items: List[DeploymentStrategyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DeploymentsTypeDef(BaseValidatorModel):
    Items: List[DeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExtensionAssociationsTypeDef(BaseValidatorModel):
    Items: List[ExtensionAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExtensionsTypeDef(BaseValidatorModel):
    Items: List[ExtensionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class HostedConfigurationVersionsTypeDef(BaseValidatorModel):
    Items: List[HostedConfigurationVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeploymentStrategiesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeploymentsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExtensionAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExtensionsRequestPaginateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHostedConfigurationVersionsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionLabel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DeploymentTypeDef(BaseValidatorModel):
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
    EventLog: List[DeploymentEventTypeDef]
    PercentageComplete: float
    StartedAt: datetime
    CompletedAt: datetime
    AppliedExtensions: List[AppliedExtensionTypeDef]
    KmsKeyArn: str
    KmsKeyIdentifier: str
    VersionLabel: str
    ResponseMetadata: ResponseMetadataTypeDef


class EnvironmentsTypeDef(BaseValidatorModel):
    Items: List[EnvironmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


