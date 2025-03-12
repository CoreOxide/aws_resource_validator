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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteAppLaunchConfigurationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class DeleteAppReplicationConfigurationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class DeleteAppRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    forceStopAppReplication: Optional[bool] = None
    forceTerminateApp: Optional[bool] = None


class DeleteAppValidationConfigurationRequestTypeDef(BaseValidatorModel):
    appId: str


class DeleteReplicationJobRequestTypeDef(BaseValidatorModel):
    replicationJobId: str


class DisassociateConnectorRequestTypeDef(BaseValidatorModel):
    connectorId: str


class GenerateChangeSetRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    changesetFormat: Optional[OutputFormatType] = None


class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None


class GenerateTemplateRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    templateFormat: Optional[OutputFormatType] = None


class GetAppLaunchConfigurationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class GetAppReplicationConfigurationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class GetAppRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class GetAppValidationConfigurationRequestTypeDef(BaseValidatorModel):
    appId: str


class GetAppValidationOutputRequestTypeDef(BaseValidatorModel):
    appId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetConnectorsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetReplicationJobsRequestTypeDef(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetReplicationRunsRequestTypeDef(BaseValidatorModel):
    replicationJobId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VmServerAddressTypeDef(BaseValidatorModel):
    vmManagerId: Optional[str] = None
    vmId: Optional[str] = None


class ImportAppCatalogRequestTypeDef(BaseValidatorModel):
    roleName: Optional[str] = None


class LaunchAppRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class ListAppsRequestTypeDef(BaseValidatorModel):
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


class ServerReplicationParametersOutputTypeDef(BaseValidatorModel):
    seedTime: Optional[datetime] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class StartAppReplicationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class StartOnDemandAppReplicationRequestTypeDef(BaseValidatorModel):
    appId: str
    description: Optional[str] = None


class StartOnDemandReplicationRunRequestTypeDef(BaseValidatorModel):
    replicationJobId: str
    description: Optional[str] = None


class StopAppReplicationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None


class TerminateAppRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartOnDemandReplicationRunResponseTypeDef(BaseValidatorModel):
    replicationRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateReplicationJobRequestTypeDef(BaseValidatorModel):
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


class ServerReplicationParametersTypeDef(BaseValidatorModel):
    seedTime: Optional[TimestampTypeDef] = None
    frequency: Optional[int] = None
    runOnce: Optional[bool] = None
    licenseType: Optional[LicenseTypeType] = None
    numberOfRecentAmisToKeep: Optional[int] = None
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None


class UpdateReplicationJobRequestTypeDef(BaseValidatorModel):
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


class GetConnectorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetReplicationJobsRequestPaginateTypeDef(BaseValidatorModel):
    replicationJobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetReplicationRunsRequestPaginateTypeDef(BaseValidatorModel):
    replicationJobId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAppsRequestPaginateTypeDef(BaseValidatorModel):
    appIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetServersRequestPaginateTypeDef(BaseValidatorModel):
    vmServerAddressList: Optional[Sequence[VmServerAddressTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetServersRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    vmServerAddressList: Optional[Sequence[VmServerAddressTypeDef]] = None


class VmServerTypeDef(BaseValidatorModel):
    vmServerAddress: Optional[VmServerAddressTypeDef] = None
    vmName: Optional[str] = None
    vmManagerName: Optional[str] = None
    vmManagerType: Optional[VmManagerTypeType] = None
    vmPath: Optional[str] = None


class NotifyAppValidationOutputRequestTypeDef(BaseValidatorModel):
    appId: str
    notificationContext: Optional[NotificationContextTypeDef] = None


class ListAppsResponseTypeDef(BaseValidatorModel):
    apps: List[AppSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class ReplicationRunTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServerGroupOutputTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    name: Optional[str] = None
    serverList: Optional[List[ServerTypeDef]] = None


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


class ServerReplicationConfigurationOutputTypeDef(BaseValidatorModel):
    server: Optional[ServerTypeDef] = None
    serverReplicationParameters: Optional[ServerReplicationParametersOutputTypeDef] = None


class ServerReplicationParametersUnionTypeDef(BaseValidatorModel):
    pass


class ServerReplicationConfigurationTypeDef(BaseValidatorModel):
    server: Optional[ServerTypeDef] = None
    serverReplicationParameters: Optional[ServerReplicationParametersUnionTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetReplicationRunsResponseTypeDef(BaseValidatorModel):
    replicationJob: ReplicationJobTypeDef
    replicationRunList: List[ReplicationRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateAppResponseTypeDef(BaseValidatorModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupOutputTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppResponseTypeDef(BaseValidatorModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupOutputTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAppResponseTypeDef(BaseValidatorModel):
    appSummary: AppSummaryTypeDef
    serverGroups: List[ServerGroupOutputTypeDef]
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ServerGroupLaunchConfigurationOutputTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    launchOrder: Optional[int] = None
    serverLaunchConfigurations: Optional[List[ServerLaunchConfigurationTypeDef]] = None


class ServerGroupLaunchConfigurationTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    launchOrder: Optional[int] = None
    serverLaunchConfigurations: Optional[Sequence[ServerLaunchConfigurationTypeDef]] = None


class ServerGroupReplicationConfigurationOutputTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverReplicationConfigurations: Optional[List[ServerReplicationConfigurationOutputTypeDef]] = None


class ServerGroupValidationConfigurationOutputTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverValidationConfigurations: Optional[List[ServerValidationConfigurationTypeDef]] = None


class ServerGroupValidationConfigurationTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverValidationConfigurations: Optional[Sequence[ServerValidationConfigurationTypeDef]] = None


class ValidationOutputTypeDef(BaseValidatorModel):
    validationId: Optional[str] = None
    name: Optional[str] = None
    status: Optional[ValidationStatusType] = None
    statusMessage: Optional[str] = None
    latestValidationTime: Optional[datetime] = None
    appValidationOutput: Optional[AppValidationOutputTypeDef] = None
    serverValidationOutput: Optional[ServerValidationOutputTypeDef] = None


class ServerGroupUnionTypeDef(BaseValidatorModel):
    pass


class CreateAppRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    clientToken: Optional[str] = None
    serverGroups: Optional[Sequence[ServerGroupUnionTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateAppRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    roleName: Optional[str] = None
    serverGroups: Optional[Sequence[ServerGroupUnionTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class GetAppLaunchConfigurationResponseTypeDef(BaseValidatorModel):
    appId: str
    roleName: str
    autoLaunch: bool
    serverGroupLaunchConfigurations: List[ServerGroupLaunchConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppReplicationConfigurationResponseTypeDef(BaseValidatorModel):
    serverGroupReplicationConfigurations: List[ServerGroupReplicationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ServerReplicationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ServerGroupReplicationConfigurationTypeDef(BaseValidatorModel):
    serverGroupId: Optional[str] = None
    serverReplicationConfigurations: Optional[ Sequence[ServerReplicationConfigurationUnionTypeDef] ] = None


class GetAppValidationConfigurationResponseTypeDef(BaseValidatorModel):
    appValidationConfigurations: List[AppValidationConfigurationTypeDef]
    serverGroupValidationConfigurations: List[ServerGroupValidationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetAppValidationOutputResponseTypeDef(BaseValidatorModel):
    validationOutputList: List[ValidationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ServerGroupLaunchConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutAppLaunchConfigurationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    roleName: Optional[str] = None
    autoLaunch: Optional[bool] = None
    serverGroupLaunchConfigurations: Optional[ Sequence[ServerGroupLaunchConfigurationUnionTypeDef] ] = None


class ServerGroupValidationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutAppValidationConfigurationRequestTypeDef(BaseValidatorModel):
    appId: str
    appValidationConfigurations: Optional[Sequence[AppValidationConfigurationTypeDef]] = None
    serverGroupValidationConfigurations: Optional[ Sequence[ServerGroupValidationConfigurationUnionTypeDef] ] = None


class ServerGroupReplicationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutAppReplicationConfigurationRequestTypeDef(BaseValidatorModel):
    appId: Optional[str] = None
    serverGroupReplicationConfigurations: Optional[ Sequence[ServerGroupReplicationConfigurationUnionTypeDef] ] = None


