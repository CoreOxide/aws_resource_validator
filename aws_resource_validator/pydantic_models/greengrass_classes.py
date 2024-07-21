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
from aws_resource_validator.pydantic_models.greengrass_constants import *

class AssociateRoleToGroupRequestRequestTypeDef(BaseModel):
    GroupId: str
    RoleArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateServiceRoleToAccountRequestRequestTypeDef(BaseModel):
    RoleArn: str

class BulkDeploymentMetricsTypeDef(BaseModel):
    InvalidInputRecords: Optional[int] = None
    RecordsProcessed: Optional[int] = None
    RetryAttempts: Optional[int] = None

class ErrorDetailTypeDef(BaseModel):
    DetailedErrorCode: Optional[str] = None
    DetailedErrorMessage: Optional[str] = None

class BulkDeploymentTypeDef(BaseModel):
    BulkDeploymentArn: Optional[str] = None
    BulkDeploymentId: Optional[str] = None
    CreatedAt: Optional[str] = None

class ConnectivityInfoTypeDef(BaseModel):
    HostAddress: Optional[str] = None
    Id: Optional[str] = None
    Metadata: Optional[str] = None
    PortNumber: Optional[int] = None

class ConnectorTypeDef(BaseModel):
    ConnectorArn: str
    Id: str
    Parameters: Optional[Mapping[str, str]] = None

class CoreTypeDef(BaseModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    DeploymentType: DeploymentTypeType
    GroupId: str
    AmznClientToken: Optional[str] = None
    DeploymentId: Optional[str] = None
    GroupVersionId: Optional[str] = None

class DeviceTypeDef(BaseModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None

class CreateGroupCertificateAuthorityRequestRequestTypeDef(BaseModel):
    GroupId: str
    AmznClientToken: Optional[str] = None

class GroupVersionTypeDef(BaseModel):
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None

class CreateGroupVersionRequestRequestTypeDef(BaseModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None

class LoggerTypeDef(BaseModel):
    Component: LoggerComponentType
    Id: str
    Level: LoggerLevelType
    Type: LoggerTypeType
    Space: Optional[int] = None

class CreateSoftwareUpdateJobRequestRequestTypeDef(BaseModel):
    S3UrlSignerRole: str
    SoftwareToUpdate: SoftwareToUpdateType
    UpdateTargets: Sequence[str]
    UpdateTargetsArchitecture: UpdateTargetsArchitectureType
    UpdateTargetsOperatingSystem: UpdateTargetsOperatingSystemType
    AmznClientToken: Optional[str] = None
    UpdateAgentLogLevel: Optional[UpdateAgentLogLevelType] = None

class SubscriptionTypeDef(BaseModel):
    Id: str
    Source: str
    Subject: str
    Target: str

class DefinitionInformationTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedTimestamp: Optional[str] = None
    LatestVersion: Optional[str] = None
    LatestVersionArn: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class DeleteConnectorDefinitionRequestRequestTypeDef(BaseModel):
    ConnectorDefinitionId: str

class DeleteCoreDefinitionRequestRequestTypeDef(BaseModel):
    CoreDefinitionId: str

class DeleteDeviceDefinitionRequestRequestTypeDef(BaseModel):
    DeviceDefinitionId: str

class DeleteFunctionDefinitionRequestRequestTypeDef(BaseModel):
    FunctionDefinitionId: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    GroupId: str

class DeleteLoggerDefinitionRequestRequestTypeDef(BaseModel):
    LoggerDefinitionId: str

class DeleteResourceDefinitionRequestRequestTypeDef(BaseModel):
    ResourceDefinitionId: str

class DeleteSubscriptionDefinitionRequestRequestTypeDef(BaseModel):
    SubscriptionDefinitionId: str

class DeploymentTypeDef(BaseModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    GroupArn: Optional[str] = None

class DisassociateRoleFromGroupRequestRequestTypeDef(BaseModel):
    GroupId: str

class ResourceAccessPolicyTypeDef(BaseModel):
    ResourceId: str
    Permission: Optional[PermissionType] = None

class FunctionRunAsConfigTypeDef(BaseModel):
    Gid: Optional[int] = None
    Uid: Optional[int] = None

class GetAssociatedRoleRequestRequestTypeDef(BaseModel):
    GroupId: str

class GetBulkDeploymentStatusRequestRequestTypeDef(BaseModel):
    BulkDeploymentId: str

class GetConnectivityInfoRequestRequestTypeDef(BaseModel):
    ThingName: str

class GetConnectorDefinitionRequestRequestTypeDef(BaseModel):
    ConnectorDefinitionId: str

class GetConnectorDefinitionVersionRequestRequestTypeDef(BaseModel):
    ConnectorDefinitionId: str
    ConnectorDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetCoreDefinitionRequestRequestTypeDef(BaseModel):
    CoreDefinitionId: str

class GetCoreDefinitionVersionRequestRequestTypeDef(BaseModel):
    CoreDefinitionId: str
    CoreDefinitionVersionId: str

class GetDeploymentStatusRequestRequestTypeDef(BaseModel):
    DeploymentId: str
    GroupId: str

class GetDeviceDefinitionRequestRequestTypeDef(BaseModel):
    DeviceDefinitionId: str

class GetDeviceDefinitionVersionRequestRequestTypeDef(BaseModel):
    DeviceDefinitionId: str
    DeviceDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetFunctionDefinitionRequestRequestTypeDef(BaseModel):
    FunctionDefinitionId: str

class GetFunctionDefinitionVersionRequestRequestTypeDef(BaseModel):
    FunctionDefinitionId: str
    FunctionDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetGroupCertificateAuthorityRequestRequestTypeDef(BaseModel):
    CertificateAuthorityId: str
    GroupId: str

class GetGroupCertificateConfigurationRequestRequestTypeDef(BaseModel):
    GroupId: str

class GetGroupRequestRequestTypeDef(BaseModel):
    GroupId: str

class GetGroupVersionRequestRequestTypeDef(BaseModel):
    GroupId: str
    GroupVersionId: str

class GetLoggerDefinitionRequestRequestTypeDef(BaseModel):
    LoggerDefinitionId: str

class GetLoggerDefinitionVersionRequestRequestTypeDef(BaseModel):
    LoggerDefinitionId: str
    LoggerDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetResourceDefinitionRequestRequestTypeDef(BaseModel):
    ResourceDefinitionId: str

class GetResourceDefinitionVersionRequestRequestTypeDef(BaseModel):
    ResourceDefinitionId: str
    ResourceDefinitionVersionId: str

class GetSubscriptionDefinitionRequestRequestTypeDef(BaseModel):
    SubscriptionDefinitionId: str

class GetSubscriptionDefinitionVersionRequestRequestTypeDef(BaseModel):
    SubscriptionDefinitionId: str
    SubscriptionDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetThingRuntimeConfigurationRequestRequestTypeDef(BaseModel):
    ThingName: str

class GroupCertificateAuthorityPropertiesTypeDef(BaseModel):
    GroupCertificateAuthorityArn: Optional[str] = None
    GroupCertificateAuthorityId: Optional[str] = None

class GroupInformationTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedTimestamp: Optional[str] = None
    LatestVersion: Optional[str] = None
    LatestVersionArn: Optional[str] = None
    Name: Optional[str] = None

class GroupOwnerSettingTypeDef(BaseModel):
    AutoAddGroupOwner: Optional[bool] = None
    GroupOwner: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBulkDeploymentDetailedReportsRequestRequestTypeDef(BaseModel):
    BulkDeploymentId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListBulkDeploymentsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListConnectorDefinitionVersionsRequestRequestTypeDef(BaseModel):
    ConnectorDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class VersionInformationTypeDef(BaseModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    Version: Optional[str] = None

class ListConnectorDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListCoreDefinitionVersionsRequestRequestTypeDef(BaseModel):
    CoreDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListCoreDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListDeviceDefinitionVersionsRequestRequestTypeDef(BaseModel):
    DeviceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListDeviceDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListFunctionDefinitionVersionsRequestRequestTypeDef(BaseModel):
    FunctionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListFunctionDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListGroupCertificateAuthoritiesRequestRequestTypeDef(BaseModel):
    GroupId: str

class ListGroupVersionsRequestRequestTypeDef(BaseModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListLoggerDefinitionVersionsRequestRequestTypeDef(BaseModel):
    LoggerDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListLoggerDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListResourceDefinitionVersionsRequestRequestTypeDef(BaseModel):
    ResourceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListResourceDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListSubscriptionDefinitionVersionsRequestRequestTypeDef(BaseModel):
    SubscriptionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListSubscriptionDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ResetDeploymentsRequestRequestTypeDef(BaseModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    Force: Optional[bool] = None

class SecretsManagerSecretResourceDataTypeDef(BaseModel):
    ARN: Optional[str] = None
    AdditionalStagingLabelsToDownload: Optional[Sequence[str]] = None

class ResourceDownloadOwnerSettingTypeDef(BaseModel):
    GroupOwner: str
    GroupPermission: PermissionType

class TelemetryConfigurationTypeDef(BaseModel):
    Telemetry: TelemetryType
    ConfigurationSyncStatus: Optional[ConfigurationSyncStatusType] = None

class StartBulkDeploymentRequestRequestTypeDef(BaseModel):
    ExecutionRoleArn: str
    InputFileUri: str
    AmznClientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StopBulkDeploymentRequestRequestTypeDef(BaseModel):
    BulkDeploymentId: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    tags: Optional[Mapping[str, str]] = None

class TelemetryConfigurationUpdateTypeDef(BaseModel):
    Telemetry: TelemetryType

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectorDefinitionRequestRequestTypeDef(BaseModel):
    ConnectorDefinitionId: str
    Name: Optional[str] = None

class UpdateCoreDefinitionRequestRequestTypeDef(BaseModel):
    CoreDefinitionId: str
    Name: Optional[str] = None

class UpdateDeviceDefinitionRequestRequestTypeDef(BaseModel):
    DeviceDefinitionId: str
    Name: Optional[str] = None

class UpdateFunctionDefinitionRequestRequestTypeDef(BaseModel):
    FunctionDefinitionId: str
    Name: Optional[str] = None

class UpdateGroupCertificateConfigurationRequestRequestTypeDef(BaseModel):
    GroupId: str
    CertificateExpiryInMilliseconds: Optional[str] = None

class UpdateGroupRequestRequestTypeDef(BaseModel):
    GroupId: str
    Name: Optional[str] = None

class UpdateLoggerDefinitionRequestRequestTypeDef(BaseModel):
    LoggerDefinitionId: str
    Name: Optional[str] = None

class UpdateResourceDefinitionRequestRequestTypeDef(BaseModel):
    ResourceDefinitionId: str
    Name: Optional[str] = None

class UpdateSubscriptionDefinitionRequestRequestTypeDef(BaseModel):
    SubscriptionDefinitionId: str
    Name: Optional[str] = None

class AssociateRoleToGroupResponseTypeDef(BaseModel):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateServiceRoleToAccountResponseTypeDef(BaseModel):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseModel):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupCertificateAuthorityResponseTypeDef(BaseModel):
    GroupCertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSoftwareUpdateJobResponseTypeDef(BaseModel):
    IotJobArn: str
    IotJobId: str
    PlatformSoftwareVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateRoleFromGroupResponseTypeDef(BaseModel):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateServiceRoleFromAccountResponseTypeDef(BaseModel):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedRoleResponseTypeDef(BaseModel):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupCertificateAuthorityResponseTypeDef(BaseModel):
    GroupCertificateAuthorityArn: str
    GroupCertificateAuthorityId: str
    PemEncodedCertificate: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupCertificateConfigurationResponseTypeDef(BaseModel):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggerDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceRoleForAccountResponseTypeDef(BaseModel):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionDefinitionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetDeploymentsResponseTypeDef(BaseModel):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBulkDeploymentResponseTypeDef(BaseModel):
    BulkDeploymentArn: str
    BulkDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoResponseTypeDef(BaseModel):
    Message: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupCertificateConfigurationResponseTypeDef(BaseModel):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BulkDeploymentResultTypeDef(BaseModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    ErrorDetails: Optional[List[ErrorDetailTypeDef]] = None
    ErrorMessage: Optional[str] = None
    GroupArn: Optional[str] = None

class GetBulkDeploymentStatusResponseTypeDef(BaseModel):
    BulkDeploymentMetrics: BulkDeploymentMetricsTypeDef
    BulkDeploymentStatus: BulkDeploymentStatusType
    CreatedAt: str
    ErrorDetails: List[ErrorDetailTypeDef]
    ErrorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentStatusResponseTypeDef(BaseModel):
    DeploymentStatus: str
    DeploymentType: DeploymentTypeType
    ErrorDetails: List[ErrorDetailTypeDef]
    ErrorMessage: str
    UpdatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBulkDeploymentsResponseTypeDef(BaseModel):
    BulkDeployments: List[BulkDeploymentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectivityInfoResponseTypeDef(BaseModel):
    ConnectivityInfo: List[ConnectivityInfoTypeDef]
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoRequestRequestTypeDef(BaseModel):
    ThingName: str
    ConnectivityInfo: Optional[Sequence[ConnectivityInfoTypeDef]] = None

class ConnectorDefinitionVersionTypeDef(BaseModel):
    Connectors: Optional[Sequence[ConnectorTypeDef]] = None

class CreateConnectorDefinitionVersionRequestRequestTypeDef(BaseModel):
    ConnectorDefinitionId: str
    AmznClientToken: Optional[str] = None
    Connectors: Optional[Sequence[ConnectorTypeDef]] = None

class CoreDefinitionVersionTypeDef(BaseModel):
    Cores: Optional[Sequence[CoreTypeDef]] = None

class CreateCoreDefinitionVersionRequestRequestTypeDef(BaseModel):
    CoreDefinitionId: str
    AmznClientToken: Optional[str] = None
    Cores: Optional[Sequence[CoreTypeDef]] = None

class CreateDeviceDefinitionVersionRequestRequestTypeDef(BaseModel):
    DeviceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Devices: Optional[Sequence[DeviceTypeDef]] = None

class DeviceDefinitionVersionTypeDef(BaseModel):
    Devices: Optional[Sequence[DeviceTypeDef]] = None

class CreateGroupRequestRequestTypeDef(BaseModel):
    Name: str
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[GroupVersionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetGroupVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: GroupVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionVersionRequestRequestTypeDef(BaseModel):
    LoggerDefinitionId: str
    AmznClientToken: Optional[str] = None
    Loggers: Optional[Sequence[LoggerTypeDef]] = None

class LoggerDefinitionVersionTypeDef(BaseModel):
    Loggers: Optional[Sequence[LoggerTypeDef]] = None

class CreateSubscriptionDefinitionVersionRequestRequestTypeDef(BaseModel):
    SubscriptionDefinitionId: str
    AmznClientToken: Optional[str] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None

class SubscriptionDefinitionVersionTypeDef(BaseModel):
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None

class ListConnectorDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggerDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionDefinitionsResponseTypeDef(BaseModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsResponseTypeDef(BaseModel):
    Deployments: List[DeploymentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionDefaultExecutionConfigTypeDef(BaseModel):
    IsolationMode: Optional[FunctionIsolationModeType] = None
    RunAs: Optional[FunctionRunAsConfigTypeDef] = None

class FunctionExecutionConfigTypeDef(BaseModel):
    IsolationMode: Optional[FunctionIsolationModeType] = None
    RunAs: Optional[FunctionRunAsConfigTypeDef] = None

class ListGroupCertificateAuthoritiesResponseTypeDef(BaseModel):
    GroupCertificateAuthorities: List[GroupCertificateAuthorityPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LocalDeviceResourceDataTypeDef(BaseModel):
    GroupOwnerSetting: Optional[GroupOwnerSettingTypeDef] = None
    SourcePath: Optional[str] = None

class LocalVolumeResourceDataTypeDef(BaseModel):
    DestinationPath: Optional[str] = None
    GroupOwnerSetting: Optional[GroupOwnerSettingTypeDef] = None
    SourcePath: Optional[str] = None

class ListBulkDeploymentsRequestListBulkDeploymentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateTypeDef(BaseModel):
    ConnectorDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateTypeDef(BaseModel):
    CoreDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreDefinitionsRequestListCoreDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateTypeDef(BaseModel):
    DeviceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateTypeDef(BaseModel):
    FunctionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupVersionsRequestListGroupVersionsPaginateTypeDef(BaseModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateTypeDef(BaseModel):
    LoggerDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateTypeDef(BaseModel):
    ResourceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDefinitionsRequestListResourceDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateTypeDef(BaseModel):
    SubscriptionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggerDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionDefinitionVersionsResponseTypeDef(BaseModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class S3MachineLearningModelResourceDataTypeDef(BaseModel):
    DestinationPath: Optional[str] = None
    OwnerSetting: Optional[ResourceDownloadOwnerSettingTypeDef] = None
    S3Uri: Optional[str] = None

class SageMakerMachineLearningModelResourceDataTypeDef(BaseModel):
    DestinationPath: Optional[str] = None
    OwnerSetting: Optional[ResourceDownloadOwnerSettingTypeDef] = None
    SageMakerJobArn: Optional[str] = None

class RuntimeConfigurationTypeDef(BaseModel):
    TelemetryConfiguration: Optional[TelemetryConfigurationTypeDef] = None

class UpdateThingRuntimeConfigurationRequestRequestTypeDef(BaseModel):
    ThingName: str
    TelemetryConfiguration: Optional[TelemetryConfigurationUpdateTypeDef] = None

class ListBulkDeploymentDetailedReportsResponseTypeDef(BaseModel):
    Deployments: List[BulkDeploymentResultTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ConnectorDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetConnectorDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: ConnectorDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[CoreDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetCoreDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: CoreDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[DeviceDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetDeviceDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: DeviceDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[LoggerDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetLoggerDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: LoggerDefinitionVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[SubscriptionDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetSubscriptionDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: SubscriptionDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionDefaultConfigTypeDef(BaseModel):
    Execution: Optional[FunctionDefaultExecutionConfigTypeDef] = None

class FunctionConfigurationEnvironmentTypeDef(BaseModel):
    AccessSysfs: Optional[bool] = None
    Execution: Optional[FunctionExecutionConfigTypeDef] = None
    ResourceAccessPolicies: Optional[Sequence[ResourceAccessPolicyTypeDef]] = None
    Variables: Optional[Mapping[str, str]] = None

class ResourceDataContainerTypeDef(BaseModel):
    LocalDeviceResourceData: Optional[LocalDeviceResourceDataTypeDef] = None
    LocalVolumeResourceData: Optional[LocalVolumeResourceDataTypeDef] = None
    S3MachineLearningModelResourceData: Optional[       S3MachineLearningModelResourceDataTypeDef     ] = None
    SageMakerMachineLearningModelResourceData: Optional[       SageMakerMachineLearningModelResourceDataTypeDef     ] = None
    SecretsManagerSecretResourceData: Optional[SecretsManagerSecretResourceDataTypeDef] = None

class GetThingRuntimeConfigurationResponseTypeDef(BaseModel):
    RuntimeConfiguration: RuntimeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationTypeDef(BaseModel):
    EncodingType: Optional[EncodingTypeType] = None
    Environment: Optional[FunctionConfigurationEnvironmentTypeDef] = None
    ExecArgs: Optional[str] = None
    Executable: Optional[str] = None
    MemorySize: Optional[int] = None
    Pinned: Optional[bool] = None
    Timeout: Optional[int] = None
    FunctionRuntimeOverride: Optional[str] = None

class ResourceTypeDef(BaseModel):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerTypeDef

class FunctionTypeDef(BaseModel):
    Id: str
    FunctionArn: Optional[str] = None
    FunctionConfiguration: Optional[FunctionConfigurationTypeDef] = None

class CreateResourceDefinitionVersionRequestRequestTypeDef(BaseModel):
    ResourceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Resources: Optional[Sequence[ResourceTypeDef]] = None

class ResourceDefinitionVersionTypeDef(BaseModel):
    Resources: Optional[Sequence[ResourceTypeDef]] = None

class CreateFunctionDefinitionVersionRequestRequestTypeDef(BaseModel):
    FunctionDefinitionId: str
    AmznClientToken: Optional[str] = None
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[Sequence[FunctionTypeDef]] = None

class FunctionDefinitionVersionTypeDef(BaseModel):
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[Sequence[FunctionTypeDef]] = None

class CreateResourceDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ResourceDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetResourceDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: ResourceDefinitionVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionRequestRequestTypeDef(BaseModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[FunctionDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetFunctionDefinitionVersionResponseTypeDef(BaseModel):
    Arn: str
    CreationTimestamp: str
    Definition: FunctionDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

