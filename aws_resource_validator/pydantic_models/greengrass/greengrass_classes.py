from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.greengrass.greengrass_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateRoleToGroupRequest(BaseValidatorModel):
    GroupId: str
    RoleArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateServiceRoleToAccountRequest(BaseValidatorModel):
    RoleArn: str


class BulkDeploymentMetrics(BaseValidatorModel):
    InvalidInputRecords: Optional[int] = None
    RecordsProcessed: Optional[int] = None
    RetryAttempts: Optional[int] = None


class ErrorDetail(BaseValidatorModel):
    DetailedErrorCode: Optional[str] = None
    DetailedErrorMessage: Optional[str] = None


class BulkDeployment(BaseValidatorModel):
    BulkDeploymentArn: Optional[str] = None
    BulkDeploymentId: Optional[str] = None
    CreatedAt: Optional[str] = None


class ConnectivityInfo(BaseValidatorModel):
    HostAddress: Optional[str] = None
    Id: Optional[str] = None
    Metadata: Optional[str] = None
    PortNumber: Optional[int] = None


class ConnectorOutput(BaseValidatorModel):
    ConnectorArn: str
    Id: str
    Parameters: Optional[Dict[str, str]] = None


class Connector(BaseValidatorModel):
    ConnectorArn: str
    Id: str
    Parameters: Optional[Dict[str, str]] = None


class Core(BaseValidatorModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None


class CreateDeploymentRequest(BaseValidatorModel):
    DeploymentType: DeploymentTypeType
    GroupId: str
    AmznClientToken: Optional[str] = None
    DeploymentId: Optional[str] = None
    GroupVersionId: Optional[str] = None


class Device(BaseValidatorModel):
    CertificateArn: str
    Id: str
    ThingArn: str
    SyncShadow: Optional[bool] = None


class CreateGroupCertificateAuthorityRequest(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None


class GroupVersion(BaseValidatorModel):
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None


class CreateGroupVersionRequest(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    ConnectorDefinitionVersionArn: Optional[str] = None
    CoreDefinitionVersionArn: Optional[str] = None
    DeviceDefinitionVersionArn: Optional[str] = None
    FunctionDefinitionVersionArn: Optional[str] = None
    LoggerDefinitionVersionArn: Optional[str] = None
    ResourceDefinitionVersionArn: Optional[str] = None
    SubscriptionDefinitionVersionArn: Optional[str] = None


class Logger(BaseValidatorModel):
    Component: LoggerComponentType
    Id: str
    Level: LoggerLevelType
    Type: LoggerTypeType
    Space: Optional[int] = None


class CreateSoftwareUpdateJobRequest(BaseValidatorModel):
    S3UrlSignerRole: str
    SoftwareToUpdate: SoftwareToUpdateType
    UpdateTargets: List[str]
    UpdateTargetsArchitecture: UpdateTargetsArchitectureType
    UpdateTargetsOperatingSystem: UpdateTargetsOperatingSystemType
    AmznClientToken: Optional[str] = None
    UpdateAgentLogLevel: Optional[UpdateAgentLogLevelType] = None


class Subscription(BaseValidatorModel):
    Id: str
    Source: str
    Subject: str
    Target: str


class DefinitionInformation(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedTimestamp: Optional[str] = None
    LatestVersion: Optional[str] = None
    LatestVersionArn: Optional[str] = None
    Name: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class DeleteConnectorDefinitionRequest(BaseValidatorModel):
    ConnectorDefinitionId: str


class DeleteCoreDefinitionRequest(BaseValidatorModel):
    CoreDefinitionId: str


class DeleteDeviceDefinitionRequest(BaseValidatorModel):
    DeviceDefinitionId: str


class DeleteFunctionDefinitionRequest(BaseValidatorModel):
    FunctionDefinitionId: str


class DeleteGroupRequest(BaseValidatorModel):
    GroupId: str


class DeleteLoggerDefinitionRequest(BaseValidatorModel):
    LoggerDefinitionId: str


class DeleteResourceDefinitionRequest(BaseValidatorModel):
    ResourceDefinitionId: str


class DeleteSubscriptionDefinitionRequest(BaseValidatorModel):
    SubscriptionDefinitionId: str


class Deployment(BaseValidatorModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    GroupArn: Optional[str] = None


class DisassociateRoleFromGroupRequest(BaseValidatorModel):
    GroupId: str


class ResourceAccessPolicy(BaseValidatorModel):
    ResourceId: str
    Permission: Optional[PermissionType] = None


class FunctionRunAsConfig(BaseValidatorModel):
    Gid: Optional[int] = None
    Uid: Optional[int] = None


class GetAssociatedRoleRequest(BaseValidatorModel):
    GroupId: str


class GetBulkDeploymentStatusRequest(BaseValidatorModel):
    BulkDeploymentId: str


class GetConnectivityInfoRequest(BaseValidatorModel):
    ThingName: str


class GetConnectorDefinitionRequest(BaseValidatorModel):
    ConnectorDefinitionId: str


class GetConnectorDefinitionVersionRequest(BaseValidatorModel):
    ConnectorDefinitionId: str
    ConnectorDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetCoreDefinitionRequest(BaseValidatorModel):
    CoreDefinitionId: str


class GetCoreDefinitionVersionRequest(BaseValidatorModel):
    CoreDefinitionId: str
    CoreDefinitionVersionId: str


class GetDeploymentStatusRequest(BaseValidatorModel):
    DeploymentId: str
    GroupId: str


class GetDeviceDefinitionRequest(BaseValidatorModel):
    DeviceDefinitionId: str


class GetDeviceDefinitionVersionRequest(BaseValidatorModel):
    DeviceDefinitionId: str
    DeviceDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetFunctionDefinitionRequest(BaseValidatorModel):
    FunctionDefinitionId: str


class GetFunctionDefinitionVersionRequest(BaseValidatorModel):
    FunctionDefinitionId: str
    FunctionDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetGroupCertificateAuthorityRequest(BaseValidatorModel):
    CertificateAuthorityId: str
    GroupId: str


class GetGroupCertificateConfigurationRequest(BaseValidatorModel):
    GroupId: str


class GetGroupRequest(BaseValidatorModel):
    GroupId: str


class GetGroupVersionRequest(BaseValidatorModel):
    GroupId: str
    GroupVersionId: str


class GetLoggerDefinitionRequest(BaseValidatorModel):
    LoggerDefinitionId: str


class GetLoggerDefinitionVersionRequest(BaseValidatorModel):
    LoggerDefinitionId: str
    LoggerDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetResourceDefinitionRequest(BaseValidatorModel):
    ResourceDefinitionId: str


class GetResourceDefinitionVersionRequest(BaseValidatorModel):
    ResourceDefinitionId: str
    ResourceDefinitionVersionId: str


class GetSubscriptionDefinitionRequest(BaseValidatorModel):
    SubscriptionDefinitionId: str


class GetSubscriptionDefinitionVersionRequest(BaseValidatorModel):
    SubscriptionDefinitionId: str
    SubscriptionDefinitionVersionId: str
    NextToken: Optional[str] = None


class GetThingRuntimeConfigurationRequest(BaseValidatorModel):
    ThingName: str


class GroupCertificateAuthorityProperties(BaseValidatorModel):
    GroupCertificateAuthorityArn: Optional[str] = None
    GroupCertificateAuthorityId: Optional[str] = None


class GroupInformation(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedTimestamp: Optional[str] = None
    LatestVersion: Optional[str] = None
    LatestVersionArn: Optional[str] = None
    Name: Optional[str] = None


class GroupOwnerSetting(BaseValidatorModel):
    AutoAddGroupOwner: Optional[bool] = None
    GroupOwner: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBulkDeploymentDetailedReportsRequest(BaseValidatorModel):
    BulkDeploymentId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListBulkDeploymentsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListConnectorDefinitionVersionsRequest(BaseValidatorModel):
    ConnectorDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class VersionInformation(BaseValidatorModel):
    Arn: Optional[str] = None
    CreationTimestamp: Optional[str] = None
    Id: Optional[str] = None
    Version: Optional[str] = None


class ListConnectorDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListCoreDefinitionVersionsRequest(BaseValidatorModel):
    CoreDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListCoreDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListDeploymentsRequest(BaseValidatorModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListDeviceDefinitionVersionsRequest(BaseValidatorModel):
    DeviceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListDeviceDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListFunctionDefinitionVersionsRequest(BaseValidatorModel):
    FunctionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListFunctionDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListGroupCertificateAuthoritiesRequest(BaseValidatorModel):
    GroupId: str


class ListGroupVersionsRequest(BaseValidatorModel):
    GroupId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListLoggerDefinitionVersionsRequest(BaseValidatorModel):
    LoggerDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListLoggerDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListResourceDefinitionVersionsRequest(BaseValidatorModel):
    ResourceDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListResourceDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionVersionsRequest(BaseValidatorModel):
    SubscriptionDefinitionId: str
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[str] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ResetDeploymentsRequest(BaseValidatorModel):
    GroupId: str
    AmznClientToken: Optional[str] = None
    Force: Optional[bool] = None


class SecretsManagerSecretResourceDataOutput(BaseValidatorModel):
    ARN: Optional[str] = None
    AdditionalStagingLabelsToDownload: Optional[List[str]] = None


class ResourceDownloadOwnerSetting(BaseValidatorModel):
    GroupOwner: str
    GroupPermission: PermissionType


class TelemetryConfiguration(BaseValidatorModel):
    Telemetry: TelemetryType
    ConfigurationSyncStatus: Optional[ConfigurationSyncStatusType] = None


class SecretsManagerSecretResourceData(BaseValidatorModel):
    ARN: Optional[str] = None
    AdditionalStagingLabelsToDownload: Optional[List[str]] = None


class StartBulkDeploymentRequest(BaseValidatorModel):
    ExecutionRoleArn: str
    InputFileUri: str
    AmznClientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class StopBulkDeploymentRequest(BaseValidatorModel):
    BulkDeploymentId: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    tags: Optional[Dict[str, str]] = None


class TelemetryConfigurationUpdate(BaseValidatorModel):
    Telemetry: TelemetryType


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateConnectorDefinitionRequest(BaseValidatorModel):
    ConnectorDefinitionId: str
    Name: Optional[str] = None


class UpdateCoreDefinitionRequest(BaseValidatorModel):
    CoreDefinitionId: str
    Name: Optional[str] = None


class UpdateDeviceDefinitionRequest(BaseValidatorModel):
    DeviceDefinitionId: str
    Name: Optional[str] = None


class UpdateFunctionDefinitionRequest(BaseValidatorModel):
    FunctionDefinitionId: str
    Name: Optional[str] = None


class UpdateGroupCertificateConfigurationRequest(BaseValidatorModel):
    GroupId: str
    CertificateExpiryInMilliseconds: Optional[str] = None


class UpdateGroupRequest(BaseValidatorModel):
    GroupId: str
    Name: Optional[str] = None


class UpdateLoggerDefinitionRequest(BaseValidatorModel):
    LoggerDefinitionId: str
    Name: Optional[str] = None


class UpdateResourceDefinitionRequest(BaseValidatorModel):
    ResourceDefinitionId: str
    Name: Optional[str] = None


class UpdateSubscriptionDefinitionRequest(BaseValidatorModel):
    SubscriptionDefinitionId: str
    Name: Optional[str] = None


class AssociateRoleToGroupResponse(BaseValidatorModel):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadata


class AssociateServiceRoleToAccountResponse(BaseValidatorModel):
    AssociatedAt: str
    ResponseMetadata: ResponseMetadata


class CreateConnectorDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateConnectorDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateCoreDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateCoreDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateDeploymentResponse(BaseValidatorModel):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadata


class CreateDeviceDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateDeviceDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateFunctionDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateFunctionDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateGroupCertificateAuthorityResponse(BaseValidatorModel):
    GroupCertificateAuthorityArn: str
    ResponseMetadata: ResponseMetadata


class CreateGroupResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateGroupVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateLoggerDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateLoggerDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateResourceDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateResourceDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateSoftwareUpdateJobResponse(BaseValidatorModel):
    IotJobArn: str
    IotJobId: str
    PlatformSoftwareVersion: str
    ResponseMetadata: ResponseMetadata


class CreateSubscriptionDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateSubscriptionDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class DisassociateRoleFromGroupResponse(BaseValidatorModel):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadata


class DisassociateServiceRoleFromAccountResponse(BaseValidatorModel):
    DisassociatedAt: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAssociatedRoleResponse(BaseValidatorModel):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadata


class GetConnectorDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetCoreDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetDeviceDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetFunctionDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetGroupCertificateAuthorityResponse(BaseValidatorModel):
    GroupCertificateAuthorityArn: str
    GroupCertificateAuthorityId: str
    PemEncodedCertificate: str
    ResponseMetadata: ResponseMetadata


class GetGroupCertificateConfigurationResponse(BaseValidatorModel):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadata


class GetGroupResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetLoggerDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetResourceDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetServiceRoleForAccountResponse(BaseValidatorModel):
    AssociatedAt: str
    RoleArn: str
    ResponseMetadata: ResponseMetadata


class GetSubscriptionDefinitionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ResetDeploymentsResponse(BaseValidatorModel):
    DeploymentArn: str
    DeploymentId: str
    ResponseMetadata: ResponseMetadata


class StartBulkDeploymentResponse(BaseValidatorModel):
    BulkDeploymentArn: str
    BulkDeploymentId: str
    ResponseMetadata: ResponseMetadata


class UpdateConnectivityInfoResponse(BaseValidatorModel):
    Message: str
    Version: str
    ResponseMetadata: ResponseMetadata


class UpdateGroupCertificateConfigurationResponse(BaseValidatorModel):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str
    ResponseMetadata: ResponseMetadata


class BulkDeploymentResult(BaseValidatorModel):
    CreatedAt: Optional[str] = None
    DeploymentArn: Optional[str] = None
    DeploymentId: Optional[str] = None
    DeploymentStatus: Optional[str] = None
    DeploymentType: Optional[DeploymentTypeType] = None
    ErrorDetails: Optional[List[ErrorDetail]] = None
    ErrorMessage: Optional[str] = None
    GroupArn: Optional[str] = None


class GetBulkDeploymentStatusResponse(BaseValidatorModel):
    BulkDeploymentMetrics: BulkDeploymentMetrics
    BulkDeploymentStatus: BulkDeploymentStatusType
    CreatedAt: str
    ErrorDetails: List[ErrorDetail]
    ErrorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetDeploymentStatusResponse(BaseValidatorModel):
    DeploymentStatus: str
    DeploymentType: DeploymentTypeType
    ErrorDetails: List[ErrorDetail]
    ErrorMessage: str
    UpdatedAt: str
    ResponseMetadata: ResponseMetadata


class ListBulkDeploymentsResponse(BaseValidatorModel):
    BulkDeployments: List[BulkDeployment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetConnectivityInfoResponse(BaseValidatorModel):
    ConnectivityInfo: List[ConnectivityInfo]
    Message: str
    ResponseMetadata: ResponseMetadata


class UpdateConnectivityInfoRequest(BaseValidatorModel):
    ThingName: str
    ConnectivityInfo: Optional[List[ConnectivityInfo]] = None


class ConnectorDefinitionVersionOutput(BaseValidatorModel):
    Connectors: Optional[List[ConnectorOutput]] = None


class ConnectorDefinitionVersion(BaseValidatorModel):
    Connectors: Optional[List[Connector]] = None

ConnectorUnion = Union[Connector, ConnectorOutput]


class CoreDefinitionVersionOutput(BaseValidatorModel):
    Cores: Optional[List[Core]] = None


class CoreDefinitionVersion(BaseValidatorModel):
    Cores: Optional[List[Core]] = None


class CreateCoreDefinitionVersionRequest(BaseValidatorModel):
    CoreDefinitionId: str
    AmznClientToken: Optional[str] = None
    Cores: Optional[List[Core]] = None


class CreateDeviceDefinitionVersionRequest(BaseValidatorModel):
    DeviceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Devices: Optional[List[Device]] = None


class DeviceDefinitionVersionOutput(BaseValidatorModel):
    Devices: Optional[List[Device]] = None


class DeviceDefinitionVersion(BaseValidatorModel):
    Devices: Optional[List[Device]] = None


class CreateGroupRequest(BaseValidatorModel):
    Name: str
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[GroupVersion] = None
    tags: Optional[Dict[str, str]] = None


class GetGroupVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: GroupVersion
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class CreateLoggerDefinitionVersionRequest(BaseValidatorModel):
    LoggerDefinitionId: str
    AmznClientToken: Optional[str] = None
    Loggers: Optional[List[Logger]] = None


class LoggerDefinitionVersionOutput(BaseValidatorModel):
    Loggers: Optional[List[Logger]] = None


class LoggerDefinitionVersion(BaseValidatorModel):
    Loggers: Optional[List[Logger]] = None


class CreateSubscriptionDefinitionVersionRequest(BaseValidatorModel):
    SubscriptionDefinitionId: str
    AmznClientToken: Optional[str] = None
    Subscriptions: Optional[List[Subscription]] = None


class SubscriptionDefinitionVersionOutput(BaseValidatorModel):
    Subscriptions: Optional[List[Subscription]] = None


class SubscriptionDefinitionVersion(BaseValidatorModel):
    Subscriptions: Optional[List[Subscription]] = None


class ListConnectorDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCoreDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDeviceDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFunctionDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLoggerDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionsResponse(BaseValidatorModel):
    Definitions: List[DefinitionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDeploymentsResponse(BaseValidatorModel):
    Deployments: List[Deployment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FunctionDefaultExecutionConfig(BaseValidatorModel):
    IsolationMode: Optional[FunctionIsolationModeType] = None
    RunAs: Optional[FunctionRunAsConfig] = None


class FunctionExecutionConfig(BaseValidatorModel):
    IsolationMode: Optional[FunctionIsolationModeType] = None
    RunAs: Optional[FunctionRunAsConfig] = None


class ListGroupCertificateAuthoritiesResponse(BaseValidatorModel):
    GroupCertificateAuthorities: List[GroupCertificateAuthorityProperties]
    ResponseMetadata: ResponseMetadata


class ListGroupsResponse(BaseValidatorModel):
    Groups: List[GroupInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LocalDeviceResourceData(BaseValidatorModel):
    GroupOwnerSetting: Optional[GroupOwnerSetting] = None
    SourcePath: Optional[str] = None


class LocalVolumeResourceData(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    GroupOwnerSetting: Optional[GroupOwnerSetting] = None
    SourcePath: Optional[str] = None


class ListBulkDeploymentDetailedReportsRequestPaginate(BaseValidatorModel):
    BulkDeploymentId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBulkDeploymentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectorDefinitionVersionsRequestPaginate(BaseValidatorModel):
    ConnectorDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectorDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoreDefinitionVersionsRequestPaginate(BaseValidatorModel):
    CoreDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoreDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsRequestPaginate(BaseValidatorModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeviceDefinitionVersionsRequestPaginate(BaseValidatorModel):
    DeviceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeviceDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionDefinitionVersionsRequestPaginate(BaseValidatorModel):
    FunctionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFunctionDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupVersionsRequestPaginate(BaseValidatorModel):
    GroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLoggerDefinitionVersionsRequestPaginate(BaseValidatorModel):
    LoggerDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLoggerDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceDefinitionVersionsRequestPaginate(BaseValidatorModel):
    ResourceDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionDefinitionVersionsRequestPaginate(BaseValidatorModel):
    SubscriptionDefinitionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectorDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCoreDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDeviceDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListFunctionDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLoggerDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListResourceDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSubscriptionDefinitionVersionsResponse(BaseValidatorModel):
    Versions: List[VersionInformation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class S3MachineLearningModelResourceData(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    OwnerSetting: Optional[ResourceDownloadOwnerSetting] = None
    S3Uri: Optional[str] = None


class SageMakerMachineLearningModelResourceData(BaseValidatorModel):
    DestinationPath: Optional[str] = None
    OwnerSetting: Optional[ResourceDownloadOwnerSetting] = None
    SageMakerJobArn: Optional[str] = None


class RuntimeConfiguration(BaseValidatorModel):
    TelemetryConfiguration: Optional[TelemetryConfiguration] = None

SecretsManagerSecretResourceDataUnion = Union[SecretsManagerSecretResourceData, SecretsManagerSecretResourceDataOutput]


class UpdateThingRuntimeConfigurationRequest(BaseValidatorModel):
    ThingName: str
    TelemetryConfiguration: Optional[TelemetryConfigurationUpdate] = None


class ListBulkDeploymentDetailedReportsResponse(BaseValidatorModel):
    Deployments: List[BulkDeploymentResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetConnectorDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: ConnectorDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ConnectorDefinitionVersionUnion = Union[ConnectorDefinitionVersion, ConnectorDefinitionVersionOutput]


class CreateConnectorDefinitionVersionRequest(BaseValidatorModel):
    ConnectorDefinitionId: str
    AmznClientToken: Optional[str] = None
    Connectors: Optional[List[ConnectorUnion]] = None


class GetCoreDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: CoreDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

CoreDefinitionVersionUnion = Union[CoreDefinitionVersion, CoreDefinitionVersionOutput]


class GetDeviceDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: DeviceDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

DeviceDefinitionVersionUnion = Union[DeviceDefinitionVersion, DeviceDefinitionVersionOutput]


class GetLoggerDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: LoggerDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata

LoggerDefinitionVersionUnion = Union[LoggerDefinitionVersion, LoggerDefinitionVersionOutput]


class GetSubscriptionDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: SubscriptionDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

SubscriptionDefinitionVersionUnion = Union[SubscriptionDefinitionVersion, SubscriptionDefinitionVersionOutput]


class FunctionDefaultConfig(BaseValidatorModel):
    Execution: Optional[FunctionDefaultExecutionConfig] = None


class FunctionConfigurationEnvironmentOutput(BaseValidatorModel):
    AccessSysfs: Optional[bool] = None
    Execution: Optional[FunctionExecutionConfig] = None
    ResourceAccessPolicies: Optional[List[ResourceAccessPolicy]] = None
    Variables: Optional[Dict[str, str]] = None


class FunctionConfigurationEnvironment(BaseValidatorModel):
    AccessSysfs: Optional[bool] = None
    Execution: Optional[FunctionExecutionConfig] = None
    ResourceAccessPolicies: Optional[List[ResourceAccessPolicy]] = None
    Variables: Optional[Dict[str, str]] = None


class ResourceDataContainerOutput(BaseValidatorModel):
    LocalDeviceResourceData: Optional[LocalDeviceResourceData] = None
    LocalVolumeResourceData: Optional[LocalVolumeResourceData] = None
    S3MachineLearningModelResourceData: Optional[S3MachineLearningModelResourceData] = None
    SageMakerMachineLearningModelResourceData: Optional[SageMakerMachineLearningModelResourceData] = None
    SecretsManagerSecretResourceData: Optional[SecretsManagerSecretResourceDataOutput] = None


class GetThingRuntimeConfigurationResponse(BaseValidatorModel):
    RuntimeConfiguration: RuntimeConfiguration
    ResponseMetadata: ResponseMetadata


class ResourceDataContainer(BaseValidatorModel):
    LocalDeviceResourceData: Optional[LocalDeviceResourceData] = None
    LocalVolumeResourceData: Optional[LocalVolumeResourceData] = None
    S3MachineLearningModelResourceData: Optional[S3MachineLearningModelResourceData] = None
    SageMakerMachineLearningModelResourceData: Optional[SageMakerMachineLearningModelResourceData] = None
    SecretsManagerSecretResourceData: Optional[SecretsManagerSecretResourceDataUnion] = None


class CreateConnectorDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ConnectorDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateCoreDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[CoreDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateDeviceDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[DeviceDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateLoggerDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[LoggerDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateSubscriptionDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[SubscriptionDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class FunctionConfigurationOutput(BaseValidatorModel):
    EncodingType: Optional[EncodingTypeType] = None
    Environment: Optional[FunctionConfigurationEnvironmentOutput] = None
    ExecArgs: Optional[str] = None
    Executable: Optional[str] = None
    MemorySize: Optional[int] = None
    Pinned: Optional[bool] = None
    Timeout: Optional[int] = None
    FunctionRuntimeOverride: Optional[str] = None

FunctionConfigurationEnvironmentUnion = Union[FunctionConfigurationEnvironment, FunctionConfigurationEnvironmentOutput]


class ResourceOutput(BaseValidatorModel):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerOutput

ResourceDataContainerUnion = Union[ResourceDataContainer, ResourceDataContainerOutput]


class FunctionOutput(BaseValidatorModel):
    Id: str
    FunctionArn: Optional[str] = None
    FunctionConfiguration: Optional[FunctionConfigurationOutput] = None


class FunctionConfiguration(BaseValidatorModel):
    EncodingType: Optional[EncodingTypeType] = None
    Environment: Optional[FunctionConfigurationEnvironmentUnion] = None
    ExecArgs: Optional[str] = None
    Executable: Optional[str] = None
    MemorySize: Optional[int] = None
    Pinned: Optional[bool] = None
    Timeout: Optional[int] = None
    FunctionRuntimeOverride: Optional[str] = None


class ResourceDefinitionVersionOutput(BaseValidatorModel):
    Resources: Optional[List[ResourceOutput]] = None


class Resource(BaseValidatorModel):
    Id: str
    Name: str
    ResourceDataContainer: ResourceDataContainerUnion


class FunctionDefinitionVersionOutput(BaseValidatorModel):
    DefaultConfig: Optional[FunctionDefaultConfig] = None
    Functions: Optional[List[FunctionOutput]] = None

FunctionConfigurationUnion = Union[FunctionConfiguration, FunctionConfigurationOutput]


class GetResourceDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: ResourceDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata


class ResourceDefinitionVersion(BaseValidatorModel):
    Resources: Optional[List[Resource]] = None

ResourceUnion = Union[Resource, ResourceOutput]


class GetFunctionDefinitionVersionResponse(BaseValidatorModel):
    Arn: str
    CreationTimestamp: str
    Definition: FunctionDefinitionVersionOutput
    Id: str
    Version: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Function(BaseValidatorModel):
    Id: str
    FunctionArn: Optional[str] = None
    FunctionConfiguration: Optional[FunctionConfigurationUnion] = None

ResourceDefinitionVersionUnion = Union[ResourceDefinitionVersion, ResourceDefinitionVersionOutput]


class CreateResourceDefinitionVersionRequest(BaseValidatorModel):
    ResourceDefinitionId: str
    AmznClientToken: Optional[str] = None
    Resources: Optional[List[ResourceUnion]] = None


class FunctionDefinitionVersion(BaseValidatorModel):
    DefaultConfig: Optional[FunctionDefaultConfig] = None
    Functions: Optional[List[Function]] = None

FunctionUnion = Union[Function, FunctionOutput]


class CreateResourceDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[ResourceDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

FunctionDefinitionVersionUnion = Union[FunctionDefinitionVersion, FunctionDefinitionVersionOutput]


class CreateFunctionDefinitionVersionRequest(BaseValidatorModel):
    FunctionDefinitionId: str
    AmznClientToken: Optional[str] = None
    DefaultConfig: Optional[FunctionDefaultConfig] = None
    Functions: Optional[List[FunctionUnion]] = None


class CreateFunctionDefinitionRequest(BaseValidatorModel):
    AmznClientToken: Optional[str] = None
    InitialVersion: Optional[FunctionDefinitionVersionUnion] = None
    Name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None