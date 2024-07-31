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
from aws_resource_validator.pydantic_models.appconfig_constants import *

class ActionInvocationTypeDef(BaseModel):
    ExtensionIdentifier: Optional[str] = None
    ActionName: Optional[str] = None
    Uri: Optional[str] = None
    RoleArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    InvocationId: Optional[str] = None

class ActionTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Uri: Optional[str] = None
    RoleArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ApplicationTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None

class AppliedExtensionTypeDef(BaseModel):
    ExtensionId: Optional[str] = None
    ExtensionAssociationId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Parameters: Optional[Dict[str, str]] = None

class ConfigurationProfileSummaryTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    LocationUri: Optional[str] = None
    ValidatorTypes: Optional[List[ValidatorTypeType]] = None
    Type: Optional[str] = None

class ValidatorTypeDef(BaseModel):
    Type: ValidatorTypeType
    Content: str

class CreateApplicationRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateDeploymentStrategyRequestRequestTypeDef(BaseModel):
    Name: str
    DeploymentDurationInMinutes: int
    GrowthFactor: float
    Description: Optional[str] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    ReplicateTo: Optional[ReplicateToType] = None
    Tags: Optional[Mapping[str, str]] = None

class MonitorTypeDef(BaseModel):
    AlarmArn: str
    AlarmRoleArn: Optional[str] = None

class CreateExtensionAssociationRequestRequestTypeDef(BaseModel):
    ExtensionIdentifier: str
    ResourceIdentifier: str
    ExtensionVersionNumber: Optional[int] = None
    Parameters: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None

class ParameterTypeDef(BaseModel):
    Description: Optional[str] = None
    Required: Optional[bool] = None
    Dynamic: Optional[bool] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class DeleteConfigurationProfileRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str

class DeleteDeploymentStrategyRequestRequestTypeDef(BaseModel):
    DeploymentStrategyId: str

class DeleteEnvironmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str

class DeleteExtensionAssociationRequestRequestTypeDef(BaseModel):
    ExtensionAssociationId: str

class DeleteExtensionRequestRequestTypeDef(BaseModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None

class DeleteHostedConfigurationVersionRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int

class DeploymentStrategyTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    GrowthType: Optional[GrowthTypeType] = None
    GrowthFactor: Optional[float] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    ReplicateTo: Optional[ReplicateToType] = None

class DeploymentSummaryTypeDef(BaseModel):
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

class ExtensionAssociationSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    ExtensionArn: Optional[str] = None
    ResourceArn: Optional[str] = None

class ExtensionSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    VersionNumber: Optional[int] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None

class GetApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class GetConfigurationProfileRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str

class GetConfigurationRequestRequestTypeDef(BaseModel):
    Application: str
    Environment: str
    Configuration: str
    ClientId: str
    ClientConfigurationVersion: Optional[str] = None

class GetDeploymentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int

class GetDeploymentStrategyRequestRequestTypeDef(BaseModel):
    DeploymentStrategyId: str

class GetEnvironmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str

class GetExtensionAssociationRequestRequestTypeDef(BaseModel):
    ExtensionAssociationId: str

class GetExtensionRequestRequestTypeDef(BaseModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None

class GetHostedConfigurationVersionRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int

class HostedConfigurationVersionSummaryTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ConfigurationProfileId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Description: Optional[str] = None
    ContentType: Optional[str] = None
    VersionLabel: Optional[str] = None
    KmsKeyArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationProfilesRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Type: Optional[str] = None

class ListDeploymentStrategiesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEnvironmentsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListExtensionAssociationsRequestRequestTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListExtensionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Name: Optional[str] = None

class ListHostedConfigurationVersionsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VersionLabel: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class StartDeploymentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyIdentifier: Optional[str] = None
    DynamicExtensionParameters: Optional[Mapping[str, str]] = None

class StopDeploymentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateDeploymentStrategyRequestRequestTypeDef(BaseModel):
    DeploymentStrategyId: str
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthFactor: Optional[float] = None
    GrowthType: Optional[GrowthTypeType] = None

class UpdateExtensionAssociationRequestRequestTypeDef(BaseModel):
    ExtensionAssociationId: str
    Parameters: Optional[Mapping[str, str]] = None

class ValidateConfigurationRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str

class DeploymentEventTypeDef(BaseModel):
    EventType: Optional[DeploymentEventTypeType] = None
    TriggeredBy: Optional[TriggeredByType] = None
    Description: Optional[str] = None
    ActionInvocations: Optional[List[ActionInvocationTypeDef]] = None
    OccurredAt: Optional[datetime] = None

class ApplicationResponseTypeDef(BaseModel):
    Id: str
    Name: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationTypeDef(BaseModel):
    Content: StreamingBody
    ConfigurationVersion: str
    ContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentStrategyResponseTypeDef(BaseModel):
    Id: str
    Name: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthTypeType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    ReplicateTo: ReplicateToType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionAssociationTypeDef(BaseModel):
    Id: str
    ExtensionArn: str
    ResourceArn: str
    Arn: str
    Parameters: Dict[str, str]
    ExtensionVersionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef

class HostedConfigurationVersionTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int
    Description: str
    Content: StreamingBody
    ContentType: str
    VersionLabel: str
    KmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTagsTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationsTypeDef(BaseModel):
    Items: List[ApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostedConfigurationVersionRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Content: BlobTypeDef
    ContentType: str
    Description: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    VersionLabel: Optional[str] = None

class ConfigurationProfilesTypeDef(BaseModel):
    Items: List[ConfigurationProfileSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationProfileTypeDef(BaseModel):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    LocationUri: str
    RetrievalRoleArn: str
    Validators: List[ValidatorTypeDef]
    Type: str
    KmsKeyArn: str
    KmsKeyIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationProfileRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    Name: str
    LocationUri: str
    Description: Optional[str] = None
    RetrievalRoleArn: Optional[str] = None
    Validators: Optional[Sequence[ValidatorTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    Type: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None

class UpdateConfigurationProfileRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RetrievalRoleArn: Optional[str] = None
    Validators: Optional[Sequence[ValidatorTypeDef]] = None
    KmsKeyIdentifier: Optional[str] = None

class CreateEnvironmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    Name: str
    Description: Optional[str] = None
    Monitors: Optional[Sequence[MonitorTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None

class EnvironmentResponseTypeDef(BaseModel):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    State: EnvironmentStateType
    Monitors: List[MonitorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[EnvironmentStateType] = None
    Monitors: Optional[List[MonitorTypeDef]] = None

class UpdateEnvironmentRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Monitors: Optional[Sequence[MonitorTypeDef]] = None

class CreateExtensionRequestRequestTypeDef(BaseModel):
    Name: str
    Actions: Mapping[ActionPointType, Sequence[ActionTypeDef]]
    Description: Optional[str] = None
    Parameters: Optional[Mapping[str, ParameterTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    LatestVersionNumber: Optional[int] = None

class ExtensionTypeDef(BaseModel):
    Id: str
    Name: str
    VersionNumber: int
    Arn: str
    Description: str
    Actions: Dict[ActionPointType, List[ActionTypeDef]]
    Parameters: Dict[str, ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExtensionRequestRequestTypeDef(BaseModel):
    ExtensionIdentifier: str
    Description: Optional[str] = None
    Actions: Optional[Mapping[ActionPointType, Sequence[ActionTypeDef]]] = None
    Parameters: Optional[Mapping[str, ParameterTypeDef]] = None
    VersionNumber: Optional[int] = None

class DeploymentStrategiesTypeDef(BaseModel):
    Items: List[DeploymentStrategyTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentsTypeDef(BaseModel):
    Items: List[DeploymentSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionAssociationsTypeDef(BaseModel):
    Items: List[ExtensionAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionsTypeDef(BaseModel):
    Items: List[ExtensionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class HostedConfigurationVersionsTypeDef(BaseModel):
    Items: List[HostedConfigurationVersionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationProfilesRequestListConfigurationProfilesPaginateTypeDef(BaseModel):
    ApplicationId: str
    Type: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentStrategiesRequestListDeploymentStrategiesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseModel):
    ApplicationId: str
    EnvironmentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExtensionAssociationsRequestListExtensionAssociationsPaginateTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExtensionsRequestListExtensionsPaginateTypeDef(BaseModel):
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHostedConfigurationVersionsRequestListHostedConfigurationVersionsPaginateTypeDef(BaseModel):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionLabel: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DeploymentTypeDef(BaseModel):
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

class EnvironmentsTypeDef(BaseModel):
    Items: List[EnvironmentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

