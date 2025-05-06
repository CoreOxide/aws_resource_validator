from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.sms.sms_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class LaunchDetails(BaseValidatorModel):
    latestLaunchTime: Optional[datetime] = None
    stackName: Optional[str] = None
    stackId: Optional[str] = None


class Connector(BaseValidatorModel):
    connectorId: Optional[str] = None
    version: Optional[str] = None
    status: Optional[ConnectorStatusType] = None
    capabilityList: Optional[List[ConnectorCapabilityType]] = None
    vmManagerName: Optional[str] = None
    vmManagerType: Optional[VmManagerTypeType] = None
    vmManagerId: Optional[str] = None
    ipAddress: Optional[str] = None
    macAddress: Optional[str] = None
    associatedOn: Optional[datetime] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

Timestamp = Union[datetime, str]


class DeleteAppLaunchConfigurationRequest(BaseValidatorModel):
    appId: Optional[str] = None


class DeleteAppReplicationConfigurationRequest(BaseValidatorModel):
    appId: Optional[str] = None


class DeleteAppRequest(BaseValidatorModel):
    appId: Optional[str] = None
    forceStopAppReplication: Optional[bool] = None
    forceTerminateApp: Optional[bool] = None


class DeleteAppValidationConfigurationRequest(BaseValidatorModel):
    appId: str


class DeleteReplicationJobRequest(BaseValidatorModel):
    replicationJobId: str


class DisassociateConnectorRequest(BaseValidatorModel):
    connectorId: str


class GenerateChangeSetRequest(BaseValidatorModel):
    appId: Optional[str] = None
    changesetFormat: Optional[OutputFormatType] = None


class S3Location(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None


class GenerateTemplateRequest(BaseValidatorModel):
    appId: Optional[str] = None
    templateFormat: Optional[OutputFormatType] = None


class GetAppLaunchConfigurationRequest(BaseValidatorModel):
    appId: Optional[str] = None


class GetAppReplicationConfigurationRequest(BaseValidatorModel):
    appId: Optional[str] = None


class GetAppRequest(BaseValidatorModel):
    appId: Optional[str] = None


class GetAppValidationConfigurationRequest(BaseValidatorModel):
    appId: str


class GetAppValidationOutputRequest(BaseValidatorModel):
    appId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetConnectorsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetReplicationJobsRequest(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetReplicationRunsRequest(BaseValidatorModel):
    replicationJobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VmServerAddress(BaseValidatorModel):
    vmManagerId: Optional[str] = None
    vmId: Optional[str] = None


class ImportAppCatalogRequest(BaseValidatorModel):
    roleName: Optional[str] = None


class LaunchAppRequest(BaseValidatorModel):
    appId: Optional[str] = None


class ListAppsRequest(BaseValidatorModel):
    appIds: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class NotificationContext(BaseValidatorModel):
    validationId: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None


class ReplicationRunStageDetails(BaseValidatorModel):
    stage: Optional[str] = None
    stageProgress: Optional[str] = None


class ServerReplicationParametersOutput(BaseValidatorModel):
    seedTime: Optional[datetime] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class StartAppReplicationRequest(BaseValidatorModel):
    appId: Optional[str] = None


class StartOnDemandAppReplicationRequest(BaseValidatorModel):
    appId: str
    description: Optional[str] = None


class StartOnDemandReplicationRunRequest(BaseValidatorModel):
    replicationJobId: str
    description: Optional[str] = None


class StopAppReplicationRequest(BaseValidatorModel):
    appId: Optional[str] = None


class TerminateAppRequest(BaseValidatorModel):
    appId: Optional[str] = None


class AppSummary(BaseValidatorModel):
    appId: Optional[str] = None
    importedAppId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[AppStatusType] = None
    statusMessage: Optional[str] = None
    replicationConfigurationStatus: Optional[AppReplicationConfigurationStatusType] = None
    replicationStatus: Optional[AppReplicationStatusType] = None
    replicationStatusMessage: Optional[str] = None
    latestReplicationTime: Optional[datetime] = None
    launchConfigurationStatus: Optional[AppLaunchConfigurationStatusType] = None
    launchStatus: Optional[AppLaunchStatusType] = None
    launchStatusMessage: Optional[str] = None
    launchDetails: Optional[LaunchDetails] = None
    creationTime: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    roleName: Optional[str] = None
    totalServerGroups: Optional[int] = None
    totalServers: Optional[int] = None


class CreateReplicationJobResponse(BaseValidatorModel):
    replicationJobId: str
    ResponseMetadata: ResponseMetadata


class GetConnectorsResponse(BaseValidatorModel):
    connectorList: List[Connector]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartOnDemandReplicationRunResponse(BaseValidatorModel):
    replicationRunId: str
    ResponseMetadata: ResponseMetadata


class CreateReplicationJobRequest(BaseValidatorModel):
    serverId: str
    seedReplicationTime: Timestamp
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    roleName: Optional[str] = None
    description: Optional[str] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class ServerReplicationParameters(BaseValidatorModel):
    seedTime: Optional[Timestamp] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class UpdateReplicationJobRequest(BaseValidatorModel):
    replicationJobId: str
    frequency: Optional[int] = None
    nextReplicationRunStartTime: Optional[Timestamp] = None
    licenseType: Optional[LicenseTypeType] = None
    roleName: Optional[str] = None
    description: Optional[str] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class GenerateChangeSetResponse(BaseValidatorModel):
    s3Location: S3Location
    ResponseMetadata: ResponseMetadata


class GenerateTemplateResponse(BaseValidatorModel):
    s3Location: S3Location
    ResponseMetadata: ResponseMetadata


class SSMOutput(BaseValidatorModel):
    s3Location: Optional[S3Location] = None


class Source(BaseValidatorModel):
    s3Location: Optional[S3Location] = None


class UserData(BaseValidatorModel):
    s3Location: Optional[S3Location] = None


class GetConnectorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReplicationJobsRequestPaginate(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReplicationRunsRequestPaginate(BaseValidatorModel):
    replicationJobId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAppsRequestPaginate(BaseValidatorModel):
    appIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetServersRequestPaginate(BaseValidatorModel):
    vmServerAddressList: Optional[List[VmServerAddress]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetServersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    vmServerAddressList: Optional[List[VmServerAddress]] = None


class VmServer(BaseValidatorModel):
    vmServerAddress: Optional[VmServerAddress] = None
    vmName: Optional[str] = None
    vmManagerName: Optional[str] = None
    vmManagerType: Optional[VmManagerTypeType] = None
    vmPath: Optional[str] = None


class NotifyAppValidationOutputRequest(BaseValidatorModel):
    appId: str
    notificationContext: Optional[NotificationContext] = None


class ReplicationRun(BaseValidatorModel):
    replicationRunId: Optional[str] = None
    state: Optional[ReplicationRunStateType] = None
    type: Optional[ReplicationRunTypeType] = None
    stageDetails: Optional[ReplicationRunStageDetails] = None
    statusMessage: Optional[str] = None
    amiId: Optional[str] = None
    scheduledStartTime: Optional[datetime] = None
    completedTime: Optional[datetime] = None
    description: Optional[str] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class ListAppsResponse(BaseValidatorModel):
    apps: List[AppSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ServerReplicationParametersUnion = Union[ServerReplicationParameters, ServerReplicationParametersOutput]


class AppValidationOutput(BaseValidatorModel):
    ssmOutput: Optional[SSMOutput] = None


class SSMValidationParameters(BaseValidatorModel):
    source: Optional[Source] = None
    instanceId: Optional[str] = None
    scriptType: Optional[ScriptTypeType] = None
    command: Optional[str] = None
    executionTimeoutSeconds: Optional[int] = None
    outputS3BucketName: Optional[str] = None


class UserDataValidationParameters(BaseValidatorModel):
    source: Optional[Source] = None
    scriptType: Optional[ScriptTypeType] = None


class Server(BaseValidatorModel):
    serverId: Optional[str] = None
    serverType: Optional[Literal['VIRTUAL_MACHINE']] = None
    vmServer: Optional[VmServer] = None
    replicationJobId: Optional[str] = None
    replicationJobTerminated: Optional[bool] = None


class ReplicationJob(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    serverId: Optional[str] = None
    serverType: Optional[Literal['VIRTUAL_MACHINE']] = None
    vmServer: Optional[VmServer] = None
    seedReplicationTime: Optional[datetime] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    nextReplicationRunStartTime: Optional[datetime] = None
    licenseType: Optional[LicenseTypeType] = None
    roleName: Optional[str] = None
    latestAmiId: Optional[str] = None
    state: Optional[ReplicationJobStateType] = None
    statusMessage: Optional[str] = None
    description: Optional[str] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    replicationRunList: Optional[List[ReplicationRun]] = None


class AppValidationConfiguration(BaseValidatorModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    appValidationStrategy: Optional[Literal['SSM']] = None
    ssmValidationParameters: Optional[SSMValidationParameters] = None


class GetServersResponse(BaseValidatorModel):
    lastModifiedOn: datetime
    serverCatalogStatus: ServerCatalogStatusType
    serverList: List[Server]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServerGroupOutput(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    name: Optional[str] = None
    serverList: Optional[List[Server]] = None


class ServerGroup(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    name: Optional[str] = None
    serverList: Optional[List[Server]] = None


class ServerLaunchConfiguration(BaseValidatorModel):
    server: Optional[Server] = None
    logicalId: Optional[str] = None
    vpc: Optional[str] = None
    subnet: Optional[str] = None
    securityGroup: Optional[str] = None
    ec2KeyName: Optional[str] = None
    userData: Optional[UserData] = None
    instanceType: Optional[str] = None
    associatePublicIpAddress: Optional[bool] = None
    iamInstanceProfileName: Optional[str] = None
    configureScript: Optional[S3Location] = None
    configureScriptType: Optional[ScriptTypeType] = None


class ServerReplicationConfigurationOutput(BaseValidatorModel):
    server: Optional[Server] = None
    serverReplicationParameters: Optional[ServerReplicationParametersOutput] = None


class ServerReplicationConfiguration(BaseValidatorModel):
    server: Optional[Server] = None
    serverReplicationParameters: Optional[ServerReplicationParametersUnion] = None


class ServerValidationConfiguration(BaseValidatorModel):
    server: Optional[Server] = None
    validationId: Optional[str] = None
    name: Optional[str] = None
    serverValidationStrategy: Optional[Literal['USERDATA']] = None
    userDataValidationParameters: Optional[UserDataValidationParameters] = None


class ServerValidationOutput(BaseValidatorModel):
    server: Optional[Server] = None


class GetReplicationJobsResponse(BaseValidatorModel):
    replicationJobList: List[ReplicationJob]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetReplicationRunsResponse(BaseValidatorModel):
    replicationJob: ReplicationJob
    replicationRunList: List[ReplicationRun]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAppResponse(BaseValidatorModel):
    appSummary: AppSummary
    serverGroups: List[ServerGroupOutput]
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class GetAppResponse(BaseValidatorModel):
    appSummary: AppSummary
    serverGroups: List[ServerGroupOutput]
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateAppResponse(BaseValidatorModel):
    appSummary: AppSummary
    serverGroups: List[ServerGroupOutput]
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata

ServerGroupUnion = Union[ServerGroup, ServerGroupOutput]


class ServerGroupLaunchConfigurationOutput(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    launchOrder: Optional[int] = None
    serverLaunchConfigurations: Optional[List[ServerLaunchConfiguration]] = None


class ServerGroupLaunchConfiguration(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    launchOrder: Optional[int] = None
    serverLaunchConfigurations: Optional[List[ServerLaunchConfiguration]] = None


class ServerGroupReplicationConfigurationOutput(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverReplicationConfigurations: Optional[List[ServerReplicationConfigurationOutput]] = None

ServerReplicationConfigurationUnion = Union[ServerReplicationConfiguration, ServerReplicationConfigurationOutput]


class ServerGroupValidationConfigurationOutput(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverValidationConfigurations: Optional[List[ServerValidationConfiguration]] = None


class ServerGroupValidationConfiguration(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverValidationConfigurations: Optional[List[ServerValidationConfiguration]] = None


class ValidationOutput(BaseValidatorModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None
    latestValidationTime: Optional[datetime] = None
    appValidationOutput: Optional[AppValidationOutput] = None
    serverValidationOutput: Optional[ServerValidationOutput] = None


class CreateAppRequest(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    clientToken: Optional[str] = None
    serverGroups: Optional[List[ServerGroupUnion]] = None
    tags: Optional[List[Tag]] = None


class UpdateAppRequest(BaseValidatorModel):
    appId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    serverGroups: Optional[List[ServerGroupUnion]] = None
    tags: Optional[List[Tag]] = None


class GetAppLaunchConfigurationResponse(BaseValidatorModel):
    appId: str
    roleName: str
    autoLaunch: bool
    serverGroupLaunchConfigurations: List[ServerGroupLaunchConfigurationOutput]
    ResponseMetadata: ResponseMetadata

ServerGroupLaunchConfigurationUnion = Union[ServerGroupLaunchConfiguration, ServerGroupLaunchConfigurationOutput]


class GetAppReplicationConfigurationResponse(BaseValidatorModel):
    serverGroupReplicationConfigurations: List[ServerGroupReplicationConfigurationOutput]
    ResponseMetadata: ResponseMetadata


class ServerGroupReplicationConfiguration(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverReplicationConfigurations: Optional[List[ServerReplicationConfigurationUnion]] = None


class GetAppValidationConfigurationResponse(BaseValidatorModel):
    appValidationConfigurations: List[AppValidationConfiguration]
    serverGroupValidationConfigurations: List[ServerGroupValidationConfigurationOutput]
    ResponseMetadata: ResponseMetadata

ServerGroupValidationConfigurationUnion = Union[ServerGroupValidationConfiguration, ServerGroupValidationConfigurationOutput]


class GetAppValidationOutputResponse(BaseValidatorModel):
    validationOutputList: List[ValidationOutput]
    ResponseMetadata: ResponseMetadata


class PutAppLaunchConfigurationRequest(BaseValidatorModel):
    appId: Optional[str] = None
    roleName: Optional[str] = None
    autoLaunch: Optional[bool] = None
    serverGroupLaunchConfigurations: Optional[List[ServerGroupLaunchConfigurationUnion]] = None

ServerGroupReplicationConfigurationUnion = Union[ServerGroupReplicationConfiguration, ServerGroupReplicationConfigurationOutput]


class PutAppValidationConfigurationRequest(BaseValidatorModel):
    appId: str
    appValidationConfigurations: Optional[List[AppValidationConfiguration]] = None
    serverGroupValidationConfigurations: Optional[List[ServerGroupValidationConfigurationUnion]] = None


class PutAppReplicationConfigurationRequest(BaseValidatorModel):
    appId: Optional[str] = None
    serverGroupReplicationConfigurations: Optional[List[ServerGroupReplicationConfigurationUnion]] = None