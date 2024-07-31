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
from aws_resource_validator.pydantic_models.sms_constants import *

class LaunchDetailsTypeDef(BaseModel):
    latestLaunchTime: Optional[datetime] = None
    stackName: Optional[str] = None
    stackId: Optional[str] = None

class ConnectorTypeDef(BaseModel):
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

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteAppLaunchConfigurationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class DeleteAppReplicationConfigurationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class DeleteAppRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None
    forceStopAppReplication: Optional[bool] = None
    forceTerminateApp: Optional[bool] = None

class DeleteAppValidationConfigurationRequestRequestTypeDef(BaseModel):
    appId: str

class DeleteReplicationJobRequestRequestTypeDef(BaseModel):
    replicationJobId: str

class DisassociateConnectorRequestRequestTypeDef(BaseModel):
    connectorId: str

class GenerateChangeSetRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None
    changesetFormat: Optional[OutputFormatType] = None

class S3LocationTypeDef(BaseModel):
    bucket: Optional[str] = None
    key: Optional[str] = None

class GenerateTemplateRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None
    templateFormat: Optional[OutputFormatType] = None

class GetAppLaunchConfigurationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class GetAppReplicationConfigurationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class GetAppRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class GetAppValidationConfigurationRequestRequestTypeDef(BaseModel):
    appId: str

class GetAppValidationOutputRequestRequestTypeDef(BaseModel):
    appId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetConnectorsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetReplicationJobsRequestRequestTypeDef(BaseModel):
    replicationJobId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetReplicationRunsRequestRequestTypeDef(BaseModel):
    replicationJobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VmServerAddressTypeDef(BaseModel):
    vmManagerId: Optional[str] = None
    vmId: Optional[str] = None

class ImportAppCatalogRequestRequestTypeDef(BaseModel):
    roleName: Optional[str] = None

class LaunchAppRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class ListAppsRequestRequestTypeDef(BaseModel):
    appIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class NotificationContextTypeDef(BaseModel):
    validationId: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None

class ReplicationRunStageDetailsTypeDef(BaseModel):
    stage: Optional[str] = None
    stageProgress: Optional[str] = None

class ServerReplicationParametersTypeDef(BaseModel):
    seedTime: Optional[datetime] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None

class StartAppReplicationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class StartOnDemandAppReplicationRequestRequestTypeDef(BaseModel):
    appId: str
    description: Optional[str] = None

class StartOnDemandReplicationRunRequestRequestTypeDef(BaseModel):
    replicationJobId: str
    description: Optional[str] = None

class StopAppReplicationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class TerminateAppRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None

class AppSummaryTypeDef(BaseModel):
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
    launchDetails: Optional[LaunchDetailsTypeDef] = None
    creationTime: Optional[datetime] = None
    lastModified: Optional[datetime] = None
    roleName: Optional[str] = None
    totalServerGroups: Optional[int] = None
    totalServers: Optional[int] = None

class CreateReplicationJobResponseTypeDef(BaseModel):
    replicationJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorsResponseTypeDef(BaseModel):
    connectorList: List[ConnectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOnDemandReplicationRunResponseTypeDef(BaseModel):
    replicationRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationJobRequestRequestTypeDef(BaseModel):
    serverId: str
    seedReplicationTime: TimestampTypeDef
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    roleName: Optional[str] = None
    description: Optional[str] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None

class UpdateReplicationJobRequestRequestTypeDef(BaseModel):
    replicationJobId: str
    frequency: Optional[int] = None
    nextReplicationRunStartTime: Optional[TimestampTypeDef] = None
    licenseType: Optional[LicenseTypeType] = None
    roleName: Optional[str] = None
    description: Optional[str] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None

class GenerateChangeSetResponseTypeDef(BaseModel):
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateTemplateResponseTypeDef(BaseModel):
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SSMOutputTypeDef(BaseModel):
    s3Location: Optional[S3LocationTypeDef] = None

class SourceTypeDef(BaseModel):
    s3Location: Optional[S3LocationTypeDef] = None

class UserDataTypeDef(BaseModel):
    s3Location: Optional[S3LocationTypeDef] = None

class GetConnectorsRequestGetConnectorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef(BaseModel):
    replicationJobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef(BaseModel):
    replicationJobId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppsRequestListAppsPaginateTypeDef(BaseModel):
    appIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetServersRequestGetServersPaginateTypeDef(BaseModel):
    vmServerAddressList: Optional[Sequence[VmServerAddressTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetServersRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    vmServerAddressList: Optional[Sequence[VmServerAddressTypeDef]] = None

class VmServerTypeDef(BaseModel):
    vmServerAddress: Optional[VmServerAddressTypeDef] = None
    vmName: Optional[str] = None
    vmManagerName: Optional[str] = None
    vmManagerType: Optional[VmManagerTypeType] = None
    vmPath: Optional[str] = None

class NotifyAppValidationOutputRequestRequestTypeDef(BaseModel):
    appId: str
    notificationContext: Optional[NotificationContextTypeDef] = None

class ReplicationRunTypeDef(BaseModel):
    replicationRunId: Optional[str] = None
    state: Optional[ReplicationRunStateType] = None
    type: Optional[ReplicationRunTypeType] = None
    stageDetails: Optional[ReplicationRunStageDetailsTypeDef] = None
    statusMessage: Optional[str] = None
    amiId: Optional[str] = None
    scheduledStartTime: Optional[datetime] = None
    completedTime: Optional[datetime] = None
    description: Optional[str] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None

class ListAppsResponseTypeDef(BaseModel):
    apps: List[AppSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppValidationOutputTypeDef(BaseModel):
    ssmOutput: Optional[SSMOutputTypeDef] = None

class SSMValidationParametersTypeDef(BaseModel):
    source: Optional[SourceTypeDef] = None
    instanceId: Optional[str] = None
    scriptType: Optional[ScriptTypeType] = None
    command: Optional[str] = None
    executionTimeoutSeconds: Optional[int] = None
    outputS3BucketName: Optional[str] = None

class UserDataValidationParametersTypeDef(BaseModel):
    source: Optional[SourceTypeDef] = None
    scriptType: Optional[ScriptTypeType] = None

class ServerTypeDef(BaseModel):
    serverId: Optional[str] = None
    serverType: Optional[Literal["VIRTUAL_MACHINE"]] = None
    vmServer: Optional[VmServerTypeDef] = None
    replicationJobId: Optional[str] = None
    replicationJobTerminated: Optional[bool] = None

class ReplicationJobTypeDef(BaseModel):
    replicationJobId: Optional[str] = None
    serverId: Optional[str] = None
    serverType: Optional[Literal["VIRTUAL_MACHINE"]] = None
    vmServer: Optional[VmServerTypeDef] = None
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
    replicationRunList: Optional[List[ReplicationRunTypeDef]] = None

class AppValidationConfigurationTypeDef(BaseModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    appValidationStrategy: Optional[Literal["SSM"]] = None
    ssmValidationParameters: Optional[SSMValidationParametersTypeDef] = None

class GetServersResponseTypeDef(BaseModel):
    lastModifiedOn: datetime
    serverCatalogStatus: ServerCatalogStatusType
    serverList: List[ServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerGroupTypeDef(BaseModel):
    serverGroupId: Optional[str] = None
    name: Optional[str] = None
    serverList: Optional[Sequence[ServerTypeDef]] = None

class ServerLaunchConfigurationTypeDef(BaseModel):
    server: Optional[ServerTypeDef] = None
    logicalId: Optional[str] = None
    vpc: Optional[str] = None
    subnet: Optional[str] = None
    securityGroup: Optional[str] = None
    ec2KeyName: Optional[str] = None
    userData: Optional[UserDataTypeDef] = None
    instanceType: Optional[str] = None
    associatePublicIpAddress: Optional[bool] = None
    iamInstanceProfileName: Optional[str] = None
    configureScript: Optional[S3LocationTypeDef] = None
    configureScriptType: Optional[ScriptTypeType] = None

class ServerReplicationConfigurationTypeDef(BaseModel):
    server: Optional[ServerTypeDef] = None
    serverReplicationParameters: Optional[ServerReplicationParametersTypeDef] = None

class ServerValidationConfigurationTypeDef(BaseModel):
    server: Optional[ServerTypeDef] = None
    validationId: Optional[str] = None
    name: Optional[str] = None
    serverValidationStrategy: Optional[Literal["USERDATA"]] = None
    userDataValidationParameters: Optional[UserDataValidationParametersTypeDef] = None

class ServerValidationOutputTypeDef(BaseModel):
    server: Optional[ServerTypeDef] = None

class GetReplicationJobsResponseTypeDef(BaseModel):
    replicationJobList: List[ReplicationJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReplicationRunsResponseTypeDef(BaseModel):
    replicationJob: ReplicationJobTypeDef
    replicationRunList: List[ReplicationRunTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    clientToken: Optional[str] = None
    serverGroups: Optional[Sequence[ServerGroupTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateAppResponseTypeDef(BaseModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppResponseTypeDef(BaseModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    serverGroups: Optional[Sequence[ServerGroupTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateAppResponseTypeDef(BaseModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServerGroupLaunchConfigurationTypeDef(BaseModel):
    serverGroupId: Optional[str] = None
    launchOrder: Optional[int] = None
    serverLaunchConfigurations: Optional[List[ServerLaunchConfigurationTypeDef]] = None

class ServerGroupReplicationConfigurationTypeDef(BaseModel):
    serverGroupId: Optional[str] = None
    serverReplicationConfigurations: Optional[List[ServerReplicationConfigurationTypeDef]] = None

class ServerGroupValidationConfigurationTypeDef(BaseModel):
    serverGroupId: Optional[str] = None
    serverValidationConfigurations: Optional[List[ServerValidationConfigurationTypeDef]] = None

class ValidationOutputTypeDef(BaseModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None
    latestValidationTime: Optional[datetime] = None
    appValidationOutput: Optional[AppValidationOutputTypeDef] = None
    serverValidationOutput: Optional[ServerValidationOutputTypeDef] = None

class GetAppLaunchConfigurationResponseTypeDef(BaseModel):
    appId: str
    roleName: str
    autoLaunch: bool
    serverGroupLaunchConfigurations: List[ServerGroupLaunchConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppLaunchConfigurationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None
    roleName: Optional[str] = None
    autoLaunch: Optional[bool] = None
    serverGroupLaunchConfigurations: Optional[       Sequence[ServerGroupLaunchConfigurationTypeDef]     ] = None

class GetAppReplicationConfigurationResponseTypeDef(BaseModel):
    serverGroupReplicationConfigurations: List[ServerGroupReplicationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppReplicationConfigurationRequestRequestTypeDef(BaseModel):
    appId: Optional[str] = None
    serverGroupReplicationConfigurations: Optional[       Sequence[ServerGroupReplicationConfigurationTypeDef]     ] = None

class GetAppValidationConfigurationResponseTypeDef(BaseModel):
    appValidationConfigurations: List[AppValidationConfigurationTypeDef]
    serverGroupValidationConfigurations: List[ServerGroupValidationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppValidationConfigurationRequestRequestTypeDef(BaseModel):
    appId: str
    appValidationConfigurations: Optional[Sequence[AppValidationConfigurationTypeDef]] = None
    serverGroupValidationConfigurations: Optional[       Sequence[ServerGroupValidationConfigurationTypeDef]     ] = None

class GetAppValidationOutputResponseTypeDef(BaseModel):
    validationOutputList: List[ValidationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

