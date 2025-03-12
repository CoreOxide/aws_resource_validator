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
from aws_resource_validator.pydantic_models.greengrass_constants import *

class AssociateRoleToGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str
    RoleArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateServiceRoleToAccountRequestTypeDef(BaseValidatorModel):
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


class ConnectorOutputTypeDef(BaseValidatorModel):
    ConnectorArn: str
    Id: str
    Parameters: Optional[Dict[str, str]] = None


class ConnectorTypeDef(BaseValidatorModel):
    ConnectorArn: str
    Id: str
    Parameters: Optional[Mapping[str, str]] = None


class CoreTypeDef(BaseValidatorModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None


class CreateDeploymentRequestTypeDef(BaseValidatorModel):
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


class CreateGroupCertificateAuthorityRequestTypeDef(BaseValidatorModel):
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


class CreateGroupVersionRequestTypeDef(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None


class CreateSoftwareUpdateJobRequestTypeDef(BaseValidatorModel):
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


class DeleteConnectorDefinitionRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str


class DeleteCoreDefinitionRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str


class DeleteDeviceDefinitionRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str


class DeleteFunctionDefinitionRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str


class DeleteLoggerDefinitionRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str


class DeleteResourceDefinitionRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str


class DeleteSubscriptionDefinitionRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str


class DeploymentTypeDef(BaseValidatorModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    GroupArn: Optional[str] = None


class DisassociateRoleFromGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str


class ResourceAccessPolicyTypeDef(BaseValidatorModel):
    ResourceId: str
    Permission: Optional[PermissionType] = None


class FunctionRunAsConfigTypeDef(BaseValidatorModel):
    Gid: Optional[int] = None
    Uid: Optional[int] = None


class GetAssociatedRoleRequestTypeDef(BaseValidatorModel):
    GroupId: str


class GetBulkDeploymentStatusRequestTypeDef(BaseValidatorModel):
    BulkDeploymentId: str


class GetConnectivityInfoRequestTypeDef(BaseValidatorModel):
    ThingName: str


class GetConnectorDefinitionRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str


class GetConnectorDefinitionVersionRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    ConnectorDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetCoreDefinitionRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str


class GetCoreDefinitionVersionRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    CoreDefinitionVersionId: str


class GetDeploymentStatusRequestTypeDef(BaseValidatorModel):
    DeploymentId: str
    GroupId: str


class GetDeviceDefinitionRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str


class GetDeviceDefinitionVersionRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    DeviceDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetFunctionDefinitionRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str


class GetFunctionDefinitionVersionRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    FunctionDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetGroupCertificateAuthorityRequestTypeDef(BaseValidatorModel):
    CertificateAuthorityId: str
    GroupId: str


class GetGroupCertificateConfigurationRequestTypeDef(BaseValidatorModel):
    GroupId: str


class GetGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str


class GetGroupVersionRequestTypeDef(BaseValidatorModel):
    GroupId: str
    GroupVersionId: str


class GetLoggerDefinitionRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str


class GetLoggerDefinitionVersionRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    LoggerDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetResourceDefinitionRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str


class GetResourceDefinitionVersionRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    ResourceDefinitionVersionId: str


class GetSubscriptionDefinitionRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str


class GetSubscriptionDefinitionVersionRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    SubscriptionDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetThingRuntimeConfigurationRequestTypeDef(BaseValidatorModel):
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


class ListBulkDeploymentDetailedReportsRequestTypeDef(BaseValidatorModel):
    BulkDeploymentId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListBulkDeploymentsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListConnectorDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class VersionInformationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    Version: Optional[str] = None


class ListConnectorDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListCoreDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListCoreDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListDeploymentsRequestTypeDef(BaseValidatorModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListDeviceDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListDeviceDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListFunctionDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListFunctionDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListGroupCertificateAuthoritiesRequestTypeDef(BaseValidatorModel):
    GroupId: str


class ListGroupVersionsRequestTypeDef(BaseValidatorModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListLoggerDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListLoggerDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListResourceDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListResourceDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionVersionsRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ResetDeploymentsRequestTypeDef(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    Force: Optional[bool] = None


class SecretsManagerSecretResourceDataOutputTypeDef(BaseValidatorModel):
    ARN: Optional[str] = None
    AdditionalStagingLabelsToDownload: Optional[List[str]] = None


class ResourceDownloadOwnerSettingTypeDef(BaseValidatorModel):
    GroupOwner: str
    GroupPermission: PermissionType


class TelemetryConfigurationTypeDef(BaseValidatorModel):
    Telemetry: TelemetryType
    ConfigurationSyncStatus: Optional[ConfigurationSyncStatusType] = None


class SecretsManagerSecretResourceDataTypeDef(BaseValidatorModel):
    ARN: Optional[str] = None
    AdditionalStagingLabelsToDownload: Optional[Sequence[str]] = None


class StartBulkDeploymentRequestTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    InputFileUri: str
    AmznClientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StopBulkDeploymentRequestTypeDef(BaseValidatorModel):
    BulkDeploymentId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    tags: Optional[Mapping[str, str]] = None


class TelemetryConfigurationUpdateTypeDef(BaseValidatorModel):
    Telemetry: TelemetryType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateConnectorDefinitionRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    Name: Optional[str] = None


class UpdateCoreDefinitionRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    Name: Optional[str] = None


class UpdateDeviceDefinitionRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    Name: Optional[str] = None


class UpdateFunctionDefinitionRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    Name: Optional[str] = None


class UpdateGroupCertificateConfigurationRequestTypeDef(BaseValidatorModel):
    GroupId: str
    CertificateExpiryInMilliseconds: Optional[str] = None


class UpdateGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str
    Name: Optional[str] = None


class UpdateLoggerDefinitionRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    Name: Optional[str] = None


class UpdateResourceDefinitionRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    Name: Optional[str] = None


class UpdateSubscriptionDefinitionRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetConnectivityInfoResponseTypeDef(BaseValidatorModel):
    ConnectivityInfo: List[ConnectivityInfoTypeDef]
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConnectivityInfoRequestTypeDef(BaseValidatorModel):
    ThingName: str
    ConnectivityInfo: Optional[Sequence[ConnectivityInfoTypeDef]] = None


class ConnectorDefinitionVersionOutputTypeDef(BaseValidatorModel):
    Connectors: Optional[List[ConnectorOutputTypeDef]] = None


class ConnectorDefinitionVersionTypeDef(BaseValidatorModel):
    Connectors: Optional[Sequence[ConnectorTypeDef]] = None


class CoreDefinitionVersionOutputTypeDef(BaseValidatorModel):
    Cores: Optional[List[CoreTypeDef]] = None


class CoreDefinitionVersionTypeDef(BaseValidatorModel):
    Cores: Optional[Sequence[CoreTypeDef]] = None


class CreateCoreDefinitionVersionRequestTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    AmznClientToken: Optional[str] = None
    Cores: Optional[Sequence[CoreTypeDef]] = None


class CreateDeviceDefinitionVersionRequestTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Devices: Optional[Sequence[DeviceTypeDef]] = None


class DeviceDefinitionVersionOutputTypeDef(BaseValidatorModel):
    Devices: Optional[List[DeviceTypeDef]] = None


class DeviceDefinitionVersionTypeDef(BaseValidatorModel):
    Devices: Optional[Sequence[DeviceTypeDef]] = None


class CreateGroupRequestTypeDef(BaseValidatorModel):
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


class LoggerTypeDef(BaseValidatorModel):
    pass


class CreateLoggerDefinitionVersionRequestTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    AmznClientToken: Optional[str] = None
    Loggers: Optional[Sequence[LoggerTypeDef]] = None


class LoggerDefinitionVersionOutputTypeDef(BaseValidatorModel):
    Loggers: Optional[List[LoggerTypeDef]] = None


class LoggerDefinitionVersionTypeDef(BaseValidatorModel):
    Loggers: Optional[Sequence[LoggerTypeDef]] = None


class CreateSubscriptionDefinitionVersionRequestTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    AmznClientToken: Optional[str] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None


class SubscriptionDefinitionVersionOutputTypeDef(BaseValidatorModel):
    Subscriptions: Optional[List[SubscriptionTypeDef]] = None


class SubscriptionDefinitionVersionTypeDef(BaseValidatorModel):
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None


class ListConnectorDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCoreDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDeviceDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFunctionDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLoggerDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionsResponseTypeDef(BaseValidatorModel):
    Definitions: List[DefinitionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDeploymentsResponseTypeDef(BaseValidatorModel):
    Deployments: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class LocalDeviceResourceDataTypeDef(BaseValidatorModel):
    GroupOwnerSetting: Optional[GroupOwnerSettingTypeDef] = None
    SourcePath: Optional[str] = None


class LocalVolumeResourceDataTypeDef(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    GroupOwnerSetting: Optional[GroupOwnerSettingTypeDef] = None
    SourcePath: Optional[str] = None


class ListBulkDeploymentDetailedReportsRequestPaginateTypeDef(BaseValidatorModel):
    BulkDeploymentId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBulkDeploymentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCoreDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    CoreDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCoreDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeploymentsRequestPaginateTypeDef(BaseValidatorModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeviceDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    DeviceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeviceDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFunctionDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupVersionsRequestPaginateTypeDef(BaseValidatorModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLoggerDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    LoggerDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLoggerDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionDefinitionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    SubscriptionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCoreDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDeviceDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListFunctionDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListLoggerDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListResourceDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[VersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class UpdateThingRuntimeConfigurationRequestTypeDef(BaseValidatorModel):
    ThingName: str
    TelemetryConfiguration: Optional[TelemetryConfigurationUpdateTypeDef] = None


class ListBulkDeploymentDetailedReportsResponseTypeDef(BaseValidatorModel):
    Deployments: List[BulkDeploymentResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetConnectorDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: ConnectorDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConnectorUnionTypeDef(BaseValidatorModel):
    pass


class CreateConnectorDefinitionVersionRequestTypeDef(BaseValidatorModel):
    ConnectorDefinitionId: str
    AmznClientToken: Optional[str] = None
    Connectors: Optional[Sequence[ConnectorUnionTypeDef]] = None


class GetCoreDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: CoreDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDeviceDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: DeviceDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetLoggerDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: LoggerDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSubscriptionDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: SubscriptionDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FunctionDefaultConfigTypeDef(BaseValidatorModel):
    Execution: Optional[FunctionDefaultExecutionConfigTypeDef] = None


class FunctionConfigurationEnvironmentOutputTypeDef(BaseValidatorModel):
    AccessSysfs: Optional[bool] = None
    Execution: Optional[FunctionExecutionConfigTypeDef] = None
    ResourceAccessPolicies: Optional[List[ResourceAccessPolicyTypeDef]] = None
    Variables: Optional[Dict[str, str]] = None


class FunctionConfigurationEnvironmentTypeDef(BaseValidatorModel):
    AccessSysfs: Optional[bool] = None
    Execution: Optional[FunctionExecutionConfigTypeDef] = None
    ResourceAccessPolicies: Optional[Sequence[ResourceAccessPolicyTypeDef]] = None
    Variables: Optional[Mapping[str, str]] = None


class ResourceDataContainerOutputTypeDef(BaseValidatorModel):
    LocalDeviceResourceData: Optional[LocalDeviceResourceDataTypeDef] = None
    LocalVolumeResourceData: Optional[LocalVolumeResourceDataTypeDef] = None
    S3MachineLearningModelResourceData: Optional[S3MachineLearningModelResourceDataTypeDef] = None
    SageMakerMachineLearningModelResourceData: Optional[ SageMakerMachineLearningModelResourceDataTypeDef ] = None
    SecretsManagerSecretResourceData: Optional[SecretsManagerSecretResourceDataOutputTypeDef] = None


class GetThingRuntimeConfigurationResponseTypeDef(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SecretsManagerSecretResourceDataUnionTypeDef(BaseValidatorModel):
    pass


class ResourceDataContainerTypeDef(BaseValidatorModel):
    LocalDeviceResourceData: Optional[LocalDeviceResourceDataTypeDef] = None
    LocalVolumeResourceData: Optional[LocalVolumeResourceDataTypeDef] = None
    S3MachineLearningModelResourceData: Optional[S3MachineLearningModelResourceDataTypeDef] = None
    SageMakerMachineLearningModelResourceData: Optional[ SageMakerMachineLearningModelResourceDataTypeDef ] = None
    SecretsManagerSecretResourceData: Optional[SecretsManagerSecretResourceDataUnionTypeDef] = None


class ConnectorDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateConnectorDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ConnectorDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CoreDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateCoreDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[CoreDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DeviceDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateDeviceDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[DeviceDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LoggerDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateLoggerDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[LoggerDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class SubscriptionDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateSubscriptionDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[SubscriptionDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class FunctionConfigurationOutputTypeDef(BaseValidatorModel):
    EncodingType: Optional[EncodingTypeType] = None
    Environment: Optional[FunctionConfigurationEnvironmentOutputTypeDef] = None
    ExecArgs: Optional[str] = None
    Executable: Optional[str] = None
    MemorySize: Optional[int] = None
    Pinned: Optional[bool] = None
    Timeout: Optional[int] = None
    FunctionRuntimeOverride: Optional[str] = None


class ResourceOutputTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerOutputTypeDef


class FunctionOutputTypeDef(BaseValidatorModel):
    Id: str
    FunctionArn: Optional[str] = None
    FunctionConfiguration: Optional[FunctionConfigurationOutputTypeDef] = None


class FunctionConfigurationEnvironmentUnionTypeDef(BaseValidatorModel):
    pass


class FunctionConfigurationTypeDef(BaseValidatorModel):
    EncodingType: Optional[EncodingTypeType] = None
    Environment: Optional[FunctionConfigurationEnvironmentUnionTypeDef] = None
    ExecArgs: Optional[str] = None
    Executable: Optional[str] = None
    MemorySize: Optional[int] = None
    Pinned: Optional[bool] = None
    Timeout: Optional[int] = None
    FunctionRuntimeOverride: Optional[str] = None


class ResourceDefinitionVersionOutputTypeDef(BaseValidatorModel):
    Resources: Optional[List[ResourceOutputTypeDef]] = None


class ResourceDataContainerUnionTypeDef(BaseValidatorModel):
    pass


class ResourceTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerUnionTypeDef


class FunctionDefinitionVersionOutputTypeDef(BaseValidatorModel):
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[List[FunctionOutputTypeDef]] = None


class GetResourceDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: ResourceDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceDefinitionVersionTypeDef(BaseValidatorModel):
    Resources: Optional[Sequence[ResourceTypeDef]] = None


class GetFunctionDefinitionVersionResponseTypeDef(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: FunctionDefinitionVersionOutputTypeDef
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FunctionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class FunctionTypeDef(BaseValidatorModel):
    Id: str
    FunctionArn: Optional[str] = None
    FunctionConfiguration: Optional[FunctionConfigurationUnionTypeDef] = None


class ResourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateResourceDefinitionVersionRequestTypeDef(BaseValidatorModel):
    ResourceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Resources: Optional[Sequence[ResourceUnionTypeDef]] = None


class FunctionDefinitionVersionTypeDef(BaseValidatorModel):
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[Sequence[FunctionTypeDef]] = None


class ResourceDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateResourceDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ResourceDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class FunctionUnionTypeDef(BaseValidatorModel):
    pass


class CreateFunctionDefinitionVersionRequestTypeDef(BaseValidatorModel):
    FunctionDefinitionId: str
    AmznClientToken: Optional[str] = None
    DefaultConfig: Optional[FunctionDefaultConfigTypeDef] = None
    Functions: Optional[Sequence[FunctionUnionTypeDef]] = None


class FunctionDefinitionVersionUnionTypeDef(BaseValidatorModel):
    pass


class CreateFunctionDefinitionRequestTypeDef(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[FunctionDefinitionVersionUnionTypeDef] = None
    Name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


