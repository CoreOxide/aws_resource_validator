from datetime import datetime

from botocore.response import StreamingBody

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
from aws_resource_validator.pydantic_models.appconfig_constants import *

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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ApplicationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None

class AppliedExtensionTypeDef(BaseValidatorModel):
    ExtensionId: Optional[str] = None
    ExtensionAssociationId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Parameters: Optional[Dict[str, str]] = None

class ConfigurationProfileSummaryTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    LocationUri: Optional[str] = None
    ValidatorTypes: Optional[List[ValidatorTypeType]] = None
    Type: Optional[str] = None

class ValidatorTypeDef(BaseValidatorModel):
    Type: ValidatorTypeType
    Content: str

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateDeploymentStrategyRequestRequestTypeDef(BaseValidatorModel):
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

class CreateExtensionAssociationRequestRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    ResourceIdentifier: str
    ExtensionVersionNumber: Optional[int] = None
    Parameters: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None

class ParameterTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Required: Optional[bool] = None
    Dynamic: Optional[bool] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class DeleteConfigurationProfileRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str

class DeleteDeploymentStrategyRequestRequestTypeDef(BaseValidatorModel):
    DeploymentStrategyId: str

class DeleteEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str

class DeleteExtensionAssociationRequestRequestTypeDef(BaseValidatorModel):
    ExtensionAssociationId: str

class DeleteExtensionRequestRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None

class DeleteHostedConfigurationVersionRequestRequestTypeDef(BaseValidatorModel):
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

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class GetConfigurationProfileRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str

class GetConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Application: str
    Environment: str
    Configuration: str
    ClientId: str
    ClientConfigurationVersion: Optional[str] = None

class GetDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int

class GetDeploymentStrategyRequestRequestTypeDef(BaseValidatorModel):
    DeploymentStrategyId: str

class GetEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str

class GetExtensionAssociationRequestRequestTypeDef(BaseValidatorModel):
    ExtensionAssociationId: str

class GetExtensionRequestRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    VersionNumber: Optional[int] = None

class GetHostedConfigurationVersionRequestRequestTypeDef(BaseValidatorModel):
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

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationProfilesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Type: Optional[str] = None

class ListDeploymentStrategiesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListExtensionAssociationsRequestRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListExtensionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Name: Optional[str] = None

class ListHostedConfigurationVersionsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VersionLabel: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class StartDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    KmsKeyIdentifier: Optional[str] = None
    DynamicExtensionParameters: Optional[Mapping[str, str]] = None

class StopDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    DeploymentNumber: int

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateDeploymentStrategyRequestRequestTypeDef(BaseValidatorModel):
    DeploymentStrategyId: str
    Description: Optional[str] = None
    DeploymentDurationInMinutes: Optional[int] = None
    FinalBakeTimeInMinutes: Optional[int] = None
    GrowthFactor: Optional[float] = None
    GrowthType: Optional[GrowthTypeType] = None

class UpdateExtensionAssociationRequestRequestTypeDef(BaseValidatorModel):
    ExtensionAssociationId: str
    Parameters: Optional[Mapping[str, str]] = None

class ValidateConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    ConfigurationVersion: str

class DeploymentEventTypeDef(BaseValidatorModel):
    EventType: Optional[DeploymentEventTypeType] = None
    TriggeredBy: Optional[TriggeredByType] = None
    Description: Optional[str] = None
    ActionInvocations: Optional[List[ActionInvocationTypeDef]] = None
    OccurredAt: Optional[datetime] = None

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

class ApplicationsTypeDef(BaseValidatorModel):
    Items: List[ApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostedConfigurationVersionRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Content: BlobTypeDef
    ContentType: str
    Description: Optional[str] = None
    LatestVersionNumber: Optional[int] = None
    VersionLabel: Optional[str] = None

class ConfigurationProfilesTypeDef(BaseValidatorModel):
    Items: List[ConfigurationProfileSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationProfileTypeDef(BaseValidatorModel):
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

class CreateConfigurationProfileRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Name: str
    LocationUri: str
    Description: Optional[str] = None
    RetrievalRoleArn: Optional[str] = None
    Validators: Optional[Sequence[ValidatorTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    Type: Optional[str] = None
    KmsKeyIdentifier: Optional[str] = None

class UpdateConfigurationProfileRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ConfigurationProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    RetrievalRoleArn: Optional[str] = None
    Validators: Optional[Sequence[ValidatorTypeDef]] = None
    KmsKeyIdentifier: Optional[str] = None

class CreateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Monitors: Optional[Sequence[MonitorTypeDef]] = None

class CreateExtensionRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateExtensionRequestRequestTypeDef(BaseValidatorModel):
    ExtensionIdentifier: str
    Description: Optional[str] = None
    Actions: Optional[Mapping[ActionPointType, Sequence[ActionTypeDef]]] = None
    Parameters: Optional[Mapping[str, ParameterTypeDef]] = None
    VersionNumber: Optional[int] = None

class DeploymentStrategiesTypeDef(BaseValidatorModel):
    Items: List[DeploymentStrategyTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentsTypeDef(BaseValidatorModel):
    Items: List[DeploymentSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionAssociationsTypeDef(BaseValidatorModel):
    Items: List[ExtensionAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExtensionsTypeDef(BaseValidatorModel):
    Items: List[ExtensionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class HostedConfigurationVersionsTypeDef(BaseValidatorModel):
    Items: List[HostedConfigurationVersionSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationProfilesRequestListConfigurationProfilesPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    Type: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentStrategiesRequestListDeploymentStrategiesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    EnvironmentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExtensionAssociationsRequestListExtensionAssociationsPaginateTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    ExtensionIdentifier: Optional[str] = None
    ExtensionVersionNumber: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExtensionsRequestListExtensionsPaginateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHostedConfigurationVersionsRequestListHostedConfigurationVersionsPaginateTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

