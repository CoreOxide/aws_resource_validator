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
from aws_resource_validator.pydantic_models.sms_constants import *

class LaunchDetailsTypeDef(BaseValidatorModel):
    latestLaunchTime: Optional[datetime] = None
    stackName: Optional[str] = None
    stackId: Optional[str] = None

class ConnectorTypeDef(BaseValidatorModel):
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

class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteAppLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class DeleteAppReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class DeleteAppRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    forceStopAppReplication: Optional[bool] = None
    forceTerminateApp: Optional[bool] = None

class DeleteAppValidationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: str

class DeleteReplicationJobRequestRequestTypeDef(BaseValidatorModel):
    replicationJobId: str

class DisassociateConnectorRequestRequestTypeDef(BaseValidatorModel):
    connectorId: str

class GenerateChangeSetRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    changesetFormat: Optional[OutputFormatType] = None

class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None

class GenerateTemplateRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    templateFormat: Optional[OutputFormatType] = None

class GetAppLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class GetAppReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class GetAppRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class GetAppValidationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: str

class GetAppValidationOutputRequestRequestTypeDef(BaseValidatorModel):
    appId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetConnectorsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetReplicationJobsRequestRequestTypeDef(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetReplicationRunsRequestRequestTypeDef(BaseValidatorModel):
    replicationJobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VmServerAddressTypeDef(BaseValidatorModel):
    vmManagerId: Optional[str] = None
    vmId: Optional[str] = None

class ImportAppCatalogRequestRequestTypeDef(BaseValidatorModel):
    roleName: Optional[str] = None

class LaunchAppRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class ListAppsRequestRequestTypeDef(BaseValidatorModel):
    appIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class NotificationContextTypeDef(BaseValidatorModel):
    validationId: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None

class ReplicationRunStageDetailsTypeDef(BaseValidatorModel):
    stage: Optional[str] = None
    stageProgress: Optional[str] = None

class ServerReplicationParametersTypeDef(BaseValidatorModel):
    seedTime: Optional[datetime] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None

class StartAppReplicationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class StartOnDemandAppReplicationRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    description: Optional[str] = None

class StartOnDemandReplicationRunRequestRequestTypeDef(BaseValidatorModel):
    replicationJobId: str
    description: Optional[str] = None

class StopAppReplicationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class TerminateAppRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None

class AppSummaryTypeDef(BaseValidatorModel):
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

class CreateReplicationJobResponseTypeDef(BaseValidatorModel):
    replicationJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectorsResponseTypeDef(BaseValidatorModel):
    connectorList: List[ConnectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOnDemandReplicationRunResponseTypeDef(BaseValidatorModel):
    replicationRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationJobRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateReplicationJobRequestRequestTypeDef(BaseValidatorModel):
    replicationJobId: str
    frequency: Optional[int] = None
    nextReplicationRunStartTime: Optional[TimestampTypeDef] = None
    licenseType: Optional[LicenseTypeType] = None
    roleName: Optional[str] = None
    description: Optional[str] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None

class GenerateChangeSetResponseTypeDef(BaseValidatorModel):
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateTemplateResponseTypeDef(BaseValidatorModel):
    s3Location: S3LocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SSMOutputTypeDef(BaseValidatorModel):
    s3Location: Optional[S3LocationTypeDef] = None

class SourceTypeDef(BaseValidatorModel):
    s3Location: Optional[S3LocationTypeDef] = None

class UserDataTypeDef(BaseValidatorModel):
    s3Location: Optional[S3LocationTypeDef] = None

class GetConnectorsRequestGetConnectorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReplicationJobsRequestGetReplicationJobsPaginateTypeDef(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReplicationRunsRequestGetReplicationRunsPaginateTypeDef(BaseValidatorModel):
    replicationJobId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAppsRequestListAppsPaginateTypeDef(BaseValidatorModel):
    appIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetServersRequestGetServersPaginateTypeDef(BaseValidatorModel):
    vmServerAddressList: Optional[Sequence[VmServerAddressTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetServersRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    vmServerAddressList: Optional[Sequence[VmServerAddressTypeDef]] = None

class VmServerTypeDef(BaseValidatorModel):
    vmServerAddress: Optional[VmServerAddressTypeDef] = None
    vmName: Optional[str] = None
    vmManagerName: Optional[str] = None
    vmManagerType: Optional[VmManagerTypeType] = None
    vmPath: Optional[str] = None

class NotifyAppValidationOutputRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    notificationContext: Optional[NotificationContextTypeDef] = None

class ReplicationRunTypeDef(BaseValidatorModel):
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

class ListAppsResponseTypeDef(BaseValidatorModel):
    apps: List[AppSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppValidationOutputTypeDef(BaseValidatorModel):
    ssmOutput: Optional[SSMOutputTypeDef] = None

class SSMValidationParametersTypeDef(BaseValidatorModel):
    source: Optional[SourceTypeDef] = None
    instanceId: Optional[str] = None
    scriptType: Optional[ScriptTypeType] = None
    command: Optional[str] = None
    executionTimeoutSeconds: Optional[int] = None
    outputS3BucketName: Optional[str] = None

class UserDataValidationParametersTypeDef(BaseValidatorModel):
    source: Optional[SourceTypeDef] = None
    scriptType: Optional[ScriptTypeType] = None

class ServerTypeDef(BaseValidatorModel):
    serverId: Optional[str] = None
    serverType: Optional[Literal["VIRTUAL_MACHINE"]] = None
    vmServer: Optional[VmServerTypeDef] = None
    replicationJobId: Optional[str] = None
    replicationJobTerminated: Optional[bool] = None

class ReplicationJobTypeDef(BaseValidatorModel):
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

class AppValidationConfigurationTypeDef(BaseValidatorModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    appValidationStrategy: Optional[Literal["SSM"]] = None
    ssmValidationParameters: Optional[SSMValidationParametersTypeDef] = None

class GetServersResponseTypeDef(BaseValidatorModel):
    lastModifiedOn: datetime
    serverCatalogStatus: ServerCatalogStatusType
    serverList: List[ServerTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ServerGroupTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    name: Optional[str] = None
    serverList: Optional[Sequence[ServerTypeDef]] = None

class ServerLaunchConfigurationTypeDef(BaseValidatorModel):
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

class ServerReplicationConfigurationTypeDef(BaseValidatorModel):
    server: Optional[ServerTypeDef] = None
    serverReplicationParameters: Optional[ServerReplicationParametersTypeDef] = None

class ServerValidationConfigurationTypeDef(BaseValidatorModel):
    server: Optional[ServerTypeDef] = None
    validationId: Optional[str] = None
    name: Optional[str] = None
    serverValidationStrategy: Optional[Literal["USERDATA"]] = None
    userDataValidationParameters: Optional[UserDataValidationParametersTypeDef] = None

class ServerValidationOutputTypeDef(BaseValidatorModel):
    server: Optional[ServerTypeDef] = None

class GetReplicationJobsResponseTypeDef(BaseValidatorModel):
    replicationJobList: List[ReplicationJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReplicationRunsResponseTypeDef(BaseValidatorModel):
    replicationJob: ReplicationJobTypeDef
    replicationRunList: List[ReplicationRunTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    clientToken: Optional[str] = None
    serverGroups: Optional[Sequence[ServerGroupTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateAppResponseTypeDef(BaseValidatorModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppResponseTypeDef(BaseValidatorModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    serverGroups: Optional[Sequence[ServerGroupTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateAppResponseTypeDef(BaseValidatorModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServerGroupLaunchConfigurationTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    launchOrder: Optional[int] = None
    serverLaunchConfigurations: Optional[List[ServerLaunchConfigurationTypeDef]] = None

class ServerGroupReplicationConfigurationTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverReplicationConfigurations: Optional[List[ServerReplicationConfigurationTypeDef]] = None

class ServerGroupValidationConfigurationTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverValidationConfigurations: Optional[List[ServerValidationConfigurationTypeDef]] = None

class ValidationOutputTypeDef(BaseValidatorModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None
    latestValidationTime: Optional[datetime] = None
    appValidationOutput: Optional[AppValidationOutputTypeDef] = None
    serverValidationOutput: Optional[ServerValidationOutputTypeDef] = None

class GetAppLaunchConfigurationResponseTypeDef(BaseValidatorModel):
    appId: str
    roleName: str
    autoLaunch: bool
    serverGroupLaunchConfigurations: List[ServerGroupLaunchConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppLaunchConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    roleName: Optional[str] = None
    autoLaunch: Optional[bool] = None
    serverGroupLaunchConfigurations: Optional[       Sequence[ServerGroupLaunchConfigurationTypeDef]     ] = None

class GetAppReplicationConfigurationResponseTypeDef(BaseValidatorModel):
    serverGroupReplicationConfigurations: List[ServerGroupReplicationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    serverGroupReplicationConfigurations: Optional[       Sequence[ServerGroupReplicationConfigurationTypeDef]     ] = None

class GetAppValidationConfigurationResponseTypeDef(BaseValidatorModel):
    appValidationConfigurations: List[AppValidationConfigurationTypeDef]
    serverGroupValidationConfigurations: List[ServerGroupValidationConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppValidationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    appValidationConfigurations: Optional[Sequence[AppValidationConfigurationTypeDef]] = None
    serverGroupValidationConfigurations: Optional[       Sequence[ServerGroupValidationConfigurationTypeDef]     ] = None

class GetAppValidationOutputResponseTypeDef(BaseValidatorModel):
    validationOutputList: List[ValidationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

