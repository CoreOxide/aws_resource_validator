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
from aws_resource_validator.pydantic_models.greengrass_constants import *

class AssociateRoleToGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    RoleArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateServiceRoleToAccountRequestRequestTypeDef(BaseValidatorModel):
    RoleArn: str

class BulkDeploymentMetricsTypeDef(BaseValidatorModel):
    InvalidInputRecords: Optional[int] = None
    RecordsProcessed: Optional[int] = None
    RetryAttempts: Optional[int] = None

class ErrorDetailTypeDef(BaseValidatorModel):
    DetailedErrorCode: Optional[str] = None
    DetailedErrorMessage: Optional[str] = None

class BulkDeploymentTypeDef(BaseValidatorModel):
    BulkDeploymentArn: Optional[str] = None
    BulkDeploymentId: Optional[str] = None
    CreatedAt: Optional[str] = None

class ConnectivityInfoTypeDef(BaseValidatorModel):
    HostAddress: Optional[str] = None
    Id: Optional[str] = None
    Metadata: Optional[str] = None
    PortNumber: Optional[int] = None

class ConnectorTypeDef(BaseValidatorModel):
    ConnectorArn: str
    Id: str
    Parameters: Optional[Mapping[str, str]] = None

class CoreTypeDef(BaseValidatorModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None

class CreateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    DeploymentType: DeploymentTypeType
    GroupId: str
    AmznClientToken: Optional[str] = None
    DeploymentId: Optional[str] = None
    GroupVersionId: Optional[str] = None

class DeviceTypeDef(BaseValidatorModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None

class CreateGroupCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None

class GroupVersionTypeDef(BaseValidatorModel):
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None

class CreateGroupVersionRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None

class LoggerTypeDef(BaseValidatorModel):
    Component: LoggerComponentType
    Id: str
    Level: LoggerLevelType
    Type: LoggerTypeType
    Space: Optional[int] = None

class CreateSoftwareUpdateJobRequestRequestTypeDef(BaseValidatorModel):
    S3UrlSignerRole: str
    SoftwareToUpdate: SoftwareToUpdateType
    UpdateTargets: Sequence[str]
    UpdateTargetsArchitecture: UpdateTargetsArchitectureType
    UpdateTargetsOperatingSystem: UpdateTargetsOperatingSystemType
    AmznClientToken: Optional[str] = None
    UpdateAgentLogLevel: Optional[UpdateAgentLogLevelType] = None

class SubscriptionTypeDef(BaseValidatorModel):
    Id: str
    Source: str
    Subject: str
    Target: str

class DefinitionInformationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedTimestamp: Optional[str] = None
    LatestVersion: Optional[str] = None
    LatestVersionArn: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class DeleteConnectorDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str

class DeleteCoreDefinitionRequestRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str

class DeleteDeviceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str

class DeleteFunctionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str

class DeleteLoggerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str

class DeleteResourceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str

class DeleteSubscriptionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str

class DeploymentTypeDef(BaseValidatorModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    GroupArn: Optional[str] = None

class DisassociateRoleFromGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str

class ResourceAccessPolicyTypeDef(BaseValidatorModel):
    ResourceId: str
    Permission: Optional[PermissionType] = None

class FunctionRunAsConfigTypeDef(BaseValidatorModel):
    Gid: Optional[int] = None
    Uid: Optional[int] = None

class GetAssociatedRoleRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str

class GetBulkDeploymentStatusRequestRequestTypeDef(BaseValidatorModel):
    BulkDeploymentId: str

class GetConnectivityInfoRequestRequestTypeDef(BaseValidatorModel):
    ThingName: str

class GetConnectorDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str

class GetConnectorDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    ConnectorDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetCoreDefinitionRequestRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str

class GetCoreDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    CoreDefinitionVersionId: str

class GetDeploymentStatusRequestRequestTypeDef(BaseValidatorModel):
    DeploymentId: str
    GroupId: str

class GetDeviceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str

class GetDeviceDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    DeviceDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetFunctionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str

class GetFunctionDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    FunctionDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetGroupCertificateAuthorityRequestRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityId: str
    GroupId: str

class GetGroupCertificateConfigurationRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str

class GetGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str

class GetGroupVersionRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    GroupVersionId: str

class GetLoggerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str

class GetLoggerDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    LoggerDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetResourceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str

class GetResourceDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    ResourceDefinitionVersionId: str

class GetSubscriptionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str

class GetSubscriptionDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    SubscriptionDefinitionVersionId: str
    NextToken: Optional[str] = None

class GetThingRuntimeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ThingName: str

class GroupCertificateAuthorityPropertiesTypeDef(BaseValidatorModel):
    GroupCertificateAuthorityArn: Optional[str] = None
    GroupCertificateAuthorityId: Optional[str] = None

class GroupInformationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedTimestamp: Optional[str] = None
    LatestVersion: Optional[str] = None
    LatestVersionArn: Optional[str] = None
    Name: Optional[str] = None

class GroupOwnerSettingTypeDef(BaseValidatorModel):
    AutoAddGroupOwner: Optional[bool] = None
    GroupOwner: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBulkDeploymentDetailedReportsRequestRequestTypeDef(BaseValidatorModel):
    BulkDeploymentId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListBulkDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListConnectorDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class VersionInformationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    Version: Optional[str] = None

class ListConnectorDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListCoreDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListCoreDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListDeviceDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListDeviceDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListFunctionDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListFunctionDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListGroupCertificateAuthoritiesRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str

class ListGroupVersionsRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListLoggerDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListLoggerDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListResourceDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListResourceDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListSubscriptionDefinitionVersionsRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListSubscriptionDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ResetDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    Force: Optional[bool] = None

class SecretsManagerSecretResourceDataTypeDef(BaseValidatorModel):
    ARN: Optional[str] = None
    AdditionalStagingLabelsToDownload: Optional[Sequence[str]] = None

class ResourceDownloadOwnerSettingTypeDef(BaseValidatorModel):
    GroupOwner: str
    GroupPermission: PermissionType

class TelemetryConfigurationTypeDef(BaseValidatorModel):
    Telemetry: TelemetryType
    ConfigurationSyncStatus: Optional[ConfigurationSyncStatusType] = None

class StartBulkDeploymentRequestRequestTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    InputFileUri: str
    AmznClientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class StopBulkDeploymentRequestRequestTypeDef(BaseValidatorModel):
    BulkDeploymentId: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    tags: Optional[Mapping[str, str]] = None

class TelemetryConfigurationUpdateTypeDef(BaseValidatorModel):
    Telemetry: TelemetryType

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectorDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    Name: Optional[str] = None

class UpdateCoreDefinitionRequestRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    Name: Optional[str] = None

class UpdateDeviceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    Name: Optional[str] = None

class UpdateFunctionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    Name: Optional[str] = None

class UpdateGroupCertificateConfigurationRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    CertificateExpiryInMilliseconds: Optional[str] = None

class UpdateGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    Name: Optional[str] = None

class UpdateLoggerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    Name: Optional[str] = None

class UpdateResourceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    Name: Optional[str] = None

class UpdateSubscriptionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    Name: Optional[str] = None

class AssociateRoleToGroupResponseTypeDef(BaseValidatorModel):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateServiceRoleToAccountResponseTypeDef(BaseValidatorModel):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseValidatorModel):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    GroupCertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSoftwareUpdateJobResponseTypeDef(BaseValidatorModel):
    IotJobArn: str
    IotJobId: str
    PlatformSoftwareVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateRoleFromGroupResponseTypeDef(BaseValidatorModel):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateServiceRoleFromAccountResponseTypeDef(BaseValidatorModel):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedRoleResponseTypeDef(BaseValidatorModel):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupCertificateAuthorityResponseTypeDef(BaseValidatorModel):
    GroupCertificateAuthorityArn: str
    GroupCertificateAuthorityId: str
    PemEncodedCertificate: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupCertificateConfigurationResponseTypeDef(BaseValidatorModel):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggerDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceRoleForAccountResponseTypeDef(BaseValidatorModel):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionDefinitionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetDeploymentsResponseTypeDef(BaseValidatorModel):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBulkDeploymentResponseTypeDef(BaseValidatorModel):
    BulkDeploymentArn: str
    BulkDeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoResponseTypeDef(BaseValidatorModel):
    Message: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupCertificateConfigurationResponseTypeDef(BaseValidatorModel):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BulkDeploymentResultTypeDef(BaseValidatorModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    ErrorDetails: Optional[List[ErrorDetailTypeDef]] = None
    ErrorMessage: Optional[str] = None
    GroupArn: Optional[str] = None

class GetBulkDeploymentStatusResponseTypeDef(BaseValidatorModel):
    BulkDeploymentMetrics: BulkDeploymentMetricsTypeDef
    BulkDeploymentStatus: BulkDeploymentStatusType
    CreatedAt: str
    ErrorDetails: List[ErrorDetailTypeDef]
    ErrorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentStatusResponseTypeDef(BaseValidatorModel):
    DeploymentStatus: str
    DeploymentType: DeploymentTypeType
    ErrorDetails: List[ErrorDetailTypeDef]
    ErrorMessage: str
    UpdatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBulkDeploymentsResponseTypeDef(BaseValidatorModel):
    BulkDeployments: List[BulkDeploymentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectivityInfoResponseTypeDef(BaseValidatorModel):
    ConnectivityInfo: List[ConnectivityInfoTypeDef]
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoRequestRequestTypeDef(BaseValidatorModel):
    ThingName: str
    ConnectivityInfo: Optional[Sequence[ConnectivityInfoTypeDef]] = None

class ConnectorDefinitionVersionTypeDef(BaseValidatorModel):
    Connectors: Optional[Sequence[ConnectorTypeDef]] = None

class CreateConnectorDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    AmznClientToken: Optional[str] = None
    Connectors: Optional[Sequence[ConnectorTypeDef]] = None

class CoreDefinitionVersionTypeDef(BaseValidatorModel):
    Cores: Optional[Sequence[CoreTypeDef]] = None

class CreateCoreDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    AmznClientToken: Optional[str] = None
    Cores: Optional[Sequence[CoreTypeDef]] = None

class CreateDeviceDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Devices: Optional[Sequence[DeviceTypeDef]] = None

class DeviceDefinitionVersionTypeDef(BaseValidatorModel):
    Devices: Optional[Sequence[DeviceTypeDef]] = None

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[GroupVersionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class GetGroupVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: GroupVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    AmznClientToken: Optional[str] = None
    Loggers: Optional[Sequence[LoggerTypeDef]] = None

class LoggerDefinitionVersionTypeDef(BaseValidatorModel):
    Loggers: Optional[Sequence[LoggerTypeDef]] = None

class CreateSubscriptionDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    AmznClientToken: Optional[str] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None

class SubscriptionDefinitionVersionTypeDef(BaseValidatorModel):
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None

class ListConnectorDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggerDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsResponseTypeDef(BaseValidatorModel):
    Deployments: List[DeploymentTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionDefaultExecutionConfigTypeDef(BaseValidatorModel):
    IsolationMode: Optional[FunctionIsolationModeType] = None
    RunAs: Optional[FunctionRunAsConfigTypeDef] = None

class FunctionExecutionConfigTypeDef(BaseValidatorModel):
    IsolationMode: Optional[FunctionIsolationModeType] = None
    RunAs: Optional[FunctionRunAsConfigTypeDef] = None

class ListGroupCertificateAuthoritiesResponseTypeDef(BaseValidatorModel):
    GroupCertificateAuthorities: List[GroupCertificateAuthorityPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupInformationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LocalDeviceResourceDataTypeDef(BaseValidatorModel):
    GroupOwnerSetting: Optional[GroupOwnerSettingTypeDef] = None
    SourcePath: Optional[str] = None

class LocalVolumeResourceDataTypeDef(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    GroupOwnerSetting: Optional[GroupOwnerSettingTypeDef] = None
    SourcePath: Optional[str] = None

class ListBulkDeploymentsRequestListBulkDeploymentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorDefinitionVersionsRequestListConnectorDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorDefinitionsRequestListConnectorDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreDefinitionVersionsRequestListCoreDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreDefinitionsRequestListCoreDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseValidatorModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceDefinitionVersionsRequestListDeviceDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceDefinitionsRequestListDeviceDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionDefinitionVersionsRequestListFunctionDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFunctionDefinitionsRequestListFunctionDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupVersionsRequestListGroupVersionsPaginateTypeDef(BaseValidatorModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLoggerDefinitionVersionsRequestListLoggerDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLoggerDefinitionsRequestListLoggerDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDefinitionVersionsRequestListResourceDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceDefinitionsRequestListResourceDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionDefinitionVersionsRequestListSubscriptionDefinitionVersionsPaginateTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionDefinitionsRequestListSubscriptionDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggerDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class S3MachineLearningModelResourceDataTypeDef(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    OwnerSetting: Optional[ResourceDownloadOwnerSettingTypeDef] = None
    S3Uri: Optional[str] = None

class SageMakerMachineLearningModelResourceDataTypeDef(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    OwnerSetting: Optional[ResourceDownloadOwnerSettingTypeDef] = None
    SageMakerJobArn: Optional[str] = None

class RuntimeConfigurationTypeDef(BaseValidatorModel):
    TelemetryConfiguration: Optional[TelemetryConfigurationTypeDef] = None

class UpdateThingRuntimeConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ThingName: str
    TelemetryConfiguration: Optional[TelemetryConfigurationUpdateTypeDef] = None

class ListBulkDeploymentDetailedReportsResponseTypeDef(BaseValidatorModel):
    Deployments: List[BulkDeploymentResultTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ConnectorDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetConnectorDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: ConnectorDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[CoreDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetCoreDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: CoreDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeviceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[DeviceDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetDeviceDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: DeviceDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[LoggerDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetLoggerDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: LoggerDefinitionVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[SubscriptionDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetSubscriptionDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: SubscriptionDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionDefaultConfigTypeDef(BaseValidatorModel):
    Execution: Optional[FunctionDefaultExecutionConfigTypeDef] = None

class FunctionConfigurationEnvironmentTypeDef(BaseValidatorModel):
    AccessSysfs: Optional[bool] = None
    Execution: Optional[FunctionExecutionConfigTypeDef] = None
    ResourceAccessPolicies: Optional[Sequence[ResourceAccessPolicyTypeDef]] = None
    Variables: Optional[Mapping[str, str]] = None

class ResourceDataContainerTypeDef(BaseValidatorModel):
    LocalDeviceResourceData: Optional[LocalDeviceResourceDataTypeDef] = None
    LocalVolumeResourceData: Optional[LocalVolumeResourceDataTypeDef] = None
    S3MachineLearningModelResourceData: Optional[       S3MachineLearningModelResourceDataTypeDef     ] = None
    SageMakerMachineLearningModelResourceData: Optional[       SageMakerMachineLearningModelResourceDataTypeDef     ] = None
    SecretsManagerSecretResourceData: Optional[SecretsManagerSecretResourceDataTypeDef] = None

class GetThingRuntimeConfigurationResponseTypeDef(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationTypeDef(BaseValidatorModel):
    EncodingType: Optional[EncodingTypeType] = None
    Environment: Optional[FunctionConfigurationEnvironmentTypeDef] = None
    ExecArgs: Optional[str] = None
    Executable: Optional[str] = None
    MemorySize: Optional[int] = None
    Pinned: Optional[bool] = None
    Timeout: Optional[int] = None
    FunctionRuntimeOverride: Optional[str] = None

class ResourceTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerTypeDef

class FunctionTypeDef(BaseValidatorModel):
    Id: str
    FunctionArn: Optional[str] = None
    FunctionConfiguration: Optional[FunctionConfigurationTypeDef] = None

class CreateResourceDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Resources: Optional[Sequence[ResourceTypeDef]] = None

class ResourceDefinitionVersionTypeDef(BaseValidatorModel):
    Resources: Optional[Sequence[ResourceTypeDef]] = None

class CreateFunctionDefinitionVersionRequestRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    AmznClientToken: Optional[str] = None
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[Sequence[FunctionTypeDef]] = None

class FunctionDefinitionVersionTypeDef(BaseValidatorModel):
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[Sequence[FunctionTypeDef]] = None

class CreateResourceDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ResourceDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetResourceDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: ResourceDefinitionVersionTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionDefinitionRequestRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[FunctionDefinitionVersionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetFunctionDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: FunctionDefinitionVersionTypeDef
    Id: str
    NextToken: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef

