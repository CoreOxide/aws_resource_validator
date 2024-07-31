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
from aws_resource_validator.pydantic_models.robomaker_constants import *

class BatchDeleteWorldsRequestRequestTypeDef(BaseModel):
    worlds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDescribeSimulationJobRequestRequestTypeDef(BaseModel):
    jobs: Sequence[str]

class BatchPolicyTypeDef(BaseModel):
    timeoutInSeconds: Optional[int] = None
    maxConcurrency: Optional[int] = None

class CancelDeploymentJobRequestRequestTypeDef(BaseModel):
    job: str

class CancelSimulationJobBatchRequestRequestTypeDef(BaseModel):
    batch: str

class CancelSimulationJobRequestRequestTypeDef(BaseModel):
    job: str

class CancelWorldExportJobRequestRequestTypeDef(BaseModel):
    job: str

class CancelWorldGenerationJobRequestRequestTypeDef(BaseModel):
    job: str

class ComputeResponseTypeDef(BaseModel):
    simulationUnitLimit: Optional[int] = None
    computeType: Optional[ComputeTypeType] = None
    gpuUnitLimit: Optional[int] = None

class ComputeTypeDef(BaseModel):
    simulationUnitLimit: Optional[int] = None
    computeType: Optional[ComputeTypeType] = None
    gpuUnitLimit: Optional[int] = None

class CreateFleetRequestRequestTypeDef(BaseModel):
    name: str
    tags: Optional[Mapping[str, str]] = None

class EnvironmentTypeDef(BaseModel):
    uri: Optional[str] = None

class RobotSoftwareSuiteTypeDef(BaseModel):
    name: Optional[RobotSoftwareSuiteTypeType] = None
    version: Optional[RobotSoftwareSuiteVersionTypeType] = None

class SourceConfigTypeDef(BaseModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    architecture: Optional[ArchitectureType] = None

class SourceTypeDef(BaseModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    etag: Optional[str] = None
    architecture: Optional[ArchitectureType] = None

class CreateRobotApplicationVersionRequestRequestTypeDef(BaseModel):
    application: str
    currentRevisionId: Optional[str] = None
    s3Etags: Optional[Sequence[str]] = None
    imageDigest: Optional[str] = None

class CreateRobotRequestRequestTypeDef(BaseModel):
    name: str
    architecture: ArchitectureType
    greengrassGroupId: str
    tags: Optional[Mapping[str, str]] = None

class RenderingEngineTypeDef(BaseModel):
    name: Optional[Literal["OGRE"]] = None
    version: Optional[str] = None

class SimulationSoftwareSuiteTypeDef(BaseModel):
    name: Optional[SimulationSoftwareSuiteTypeType] = None
    version: Optional[str] = None

class CreateSimulationApplicationVersionRequestRequestTypeDef(BaseModel):
    application: str
    currentRevisionId: Optional[str] = None
    s3Etags: Optional[Sequence[str]] = None
    imageDigest: Optional[str] = None

class DataSourceConfigTypeDef(BaseModel):
    name: str
    s3Bucket: str
    s3Keys: Sequence[str]
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None

class LoggingConfigTypeDef(BaseModel):
    recordAllRosTopics: Optional[bool] = None

class OutputLocationTypeDef(BaseModel):
    s3Bucket: Optional[str] = None
    s3Prefix: Optional[str] = None

class VPCConfigTypeDef(BaseModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None
    assignPublicIp: Optional[bool] = None

class VPCConfigResponseTypeDef(BaseModel):
    subnets: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    assignPublicIp: Optional[bool] = None

class WorldCountTypeDef(BaseModel):
    floorplanCount: Optional[int] = None
    interiorCountPerFloorplan: Optional[int] = None

class TemplateLocationTypeDef(BaseModel):
    s3Bucket: str
    s3Key: str

class S3KeyOutputTypeDef(BaseModel):
    s3Key: Optional[str] = None
    etag: Optional[str] = None

class DeleteFleetRequestRequestTypeDef(BaseModel):
    fleet: str

class DeleteRobotApplicationRequestRequestTypeDef(BaseModel):
    application: str
    applicationVersion: Optional[str] = None

class DeleteRobotRequestRequestTypeDef(BaseModel):
    robot: str

class DeleteSimulationApplicationRequestRequestTypeDef(BaseModel):
    application: str
    applicationVersion: Optional[str] = None

class DeleteWorldTemplateRequestRequestTypeDef(BaseModel):
    template: str

class DeploymentLaunchConfigPaginatorTypeDef(BaseModel):
    packageName: str
    launchFile: str
    preLaunchFile: Optional[str] = None
    postLaunchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None

class DeploymentLaunchConfigTypeDef(BaseModel):
    packageName: str
    launchFile: str
    preLaunchFile: Optional[str] = None
    postLaunchFile: Optional[str] = None
    environmentVariables: Optional[Mapping[str, str]] = None

class S3ObjectTypeDef(BaseModel):
    bucket: str
    key: str
    etag: Optional[str] = None

class DeregisterRobotRequestRequestTypeDef(BaseModel):
    fleet: str
    robot: str

class DescribeDeploymentJobRequestRequestTypeDef(BaseModel):
    job: str

class DescribeFleetRequestRequestTypeDef(BaseModel):
    fleet: str

class RobotTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    fleetArn: Optional[str] = None
    status: Optional[RobotStatusType] = None
    greenGrassGroupId: Optional[str] = None
    createdAt: Optional[datetime] = None
    architecture: Optional[ArchitectureType] = None
    lastDeploymentJob: Optional[str] = None
    lastDeploymentTime: Optional[datetime] = None

class DescribeRobotApplicationRequestRequestTypeDef(BaseModel):
    application: str
    applicationVersion: Optional[str] = None

class DescribeRobotRequestRequestTypeDef(BaseModel):
    robot: str

class DescribeSimulationApplicationRequestRequestTypeDef(BaseModel):
    application: str
    applicationVersion: Optional[str] = None

class DescribeSimulationJobBatchRequestRequestTypeDef(BaseModel):
    batch: str

class SimulationJobSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[SimulationJobStatusType] = None
    simulationApplicationNames: Optional[List[str]] = None
    robotApplicationNames: Optional[List[str]] = None
    dataSourceNames: Optional[List[str]] = None
    computeType: Optional[ComputeTypeType] = None

class DescribeSimulationJobRequestRequestTypeDef(BaseModel):
    job: str

class NetworkInterfaceTypeDef(BaseModel):
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None

class DescribeWorldExportJobRequestRequestTypeDef(BaseModel):
    job: str

class DescribeWorldGenerationJobRequestRequestTypeDef(BaseModel):
    job: str

class DescribeWorldRequestRequestTypeDef(BaseModel):
    world: str

class DescribeWorldTemplateRequestRequestTypeDef(BaseModel):
    template: str

class WorldFailureTypeDef(BaseModel):
    failureCode: Optional[WorldGenerationJobErrorCodeType] = None
    sampleFailureReason: Optional[str] = None
    failureCount: Optional[int] = None

class FilterTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class FleetTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastDeploymentStatus: Optional[DeploymentStatusType] = None
    lastDeploymentJob: Optional[str] = None
    lastDeploymentTime: Optional[datetime] = None

class GetWorldTemplateBodyRequestRequestTypeDef(BaseModel):
    template: Optional[str] = None
    generationJob: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SimulationJobBatchSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    status: Optional[SimulationJobBatchStatusType] = None
    failedRequestCount: Optional[int] = None
    pendingRequestCount: Optional[int] = None
    createdRequestCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListWorldTemplatesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TemplateSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    version: Optional[str] = None

class WorldSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    generationJob: Optional[str] = None
    template: Optional[str] = None

class PortMappingTypeDef(BaseModel):
    jobPort: int
    applicationPort: int
    enableOnPublicIp: Optional[bool] = None

class ProgressDetailTypeDef(BaseModel):
    currentProgress: Optional[RobotDeploymentStepType] = None
    percentDone: Optional[float] = None
    estimatedTimeRemainingSeconds: Optional[int] = None
    targetResource: Optional[str] = None

class RegisterRobotRequestRequestTypeDef(BaseModel):
    fleet: str
    robot: str

class RestartSimulationJobRequestRequestTypeDef(BaseModel):
    job: str

class ToolTypeDef(BaseModel):
    name: str
    command: str
    streamUI: Optional[bool] = None
    streamOutputToCloudWatch: Optional[bool] = None
    exitBehavior: Optional[ExitBehaviorType] = None

class UploadConfigurationTypeDef(BaseModel):
    name: str
    path: str
    uploadBehavior: UploadBehaviorType

class WorldConfigTypeDef(BaseModel):
    world: Optional[str] = None

class SyncDeploymentJobRequestRequestTypeDef(BaseModel):
    clientRequestToken: str
    fleet: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchDeleteWorldsResponseTypeDef(BaseModel):
    unprocessedWorlds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseModel):
    arn: str
    name: str
    createdAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRobotResponseTypeDef(BaseModel):
    arn: str
    name: str
    createdAt: datetime
    greengrassGroupId: str
    architecture: ArchitectureType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorldTemplateResponseTypeDef(BaseModel):
    arn: str
    clientRequestToken: str
    createdAt: datetime
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterRobotResponseTypeDef(BaseModel):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRobotResponseTypeDef(BaseModel):
    arn: str
    name: str
    fleetArn: str
    status: RobotStatusType
    greengrassGroupId: str
    createdAt: datetime
    architecture: ArchitectureType
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldResponseTypeDef(BaseModel):
    arn: str
    generationJob: str
    template: str
    createdAt: datetime
    tags: Dict[str, str]
    worldDescriptionBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldTemplateResponseTypeDef(BaseModel):
    arn: str
    clientRequestToken: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorldTemplateBodyResponseTypeDef(BaseModel):
    templateBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterRobotResponseTypeDef(BaseModel):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorldTemplateResponseTypeDef(BaseModel):
    arn: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RobotApplicationSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    version: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    robotSoftwareSuite: Optional[RobotSoftwareSuiteTypeDef] = None

class CreateRobotApplicationRequestRequestTypeDef(BaseModel):
    name: str
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    environment: Optional[EnvironmentTypeDef] = None

class UpdateRobotApplicationRequestRequestTypeDef(BaseModel):
    application: str
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    currentRevisionId: Optional[str] = None
    environment: Optional[EnvironmentTypeDef] = None

class CreateRobotApplicationResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRobotApplicationVersionResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRobotApplicationResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    imageDigest: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRobotApplicationResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSimulationApplicationRequestRequestTypeDef(BaseModel):
    name: str
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    renderingEngine: Optional[RenderingEngineTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    environment: Optional[EnvironmentTypeDef] = None

class CreateSimulationApplicationResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSimulationApplicationVersionResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationApplicationResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    environment: EnvironmentTypeDef
    imageDigest: str
    ResponseMetadata: ResponseMetadataTypeDef

class SimulationApplicationSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    version: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    robotSoftwareSuite: Optional[RobotSoftwareSuiteTypeDef] = None
    simulationSoftwareSuite: Optional[SimulationSoftwareSuiteTypeDef] = None

class UpdateSimulationApplicationRequestRequestTypeDef(BaseModel):
    application: str
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    renderingEngine: Optional[RenderingEngineTypeDef] = None
    currentRevisionId: Optional[str] = None
    environment: Optional[EnvironmentTypeDef] = None

class UpdateSimulationApplicationResponseTypeDef(BaseModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    renderingEngine: RenderingEngineTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorldExportJobRequestRequestTypeDef(BaseModel):
    worlds: Sequence[str]
    outputLocation: OutputLocationTypeDef
    iamRole: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateWorldExportJobResponseTypeDef(BaseModel):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldExportJobResponseTypeDef(BaseModel):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    worlds: List[str]
    outputLocation: OutputLocationTypeDef
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class WorldExportJobSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    status: Optional[WorldExportJobStatusType] = None
    createdAt: Optional[datetime] = None
    worlds: Optional[List[str]] = None
    outputLocation: Optional[OutputLocationTypeDef] = None

class CreateWorldGenerationJobRequestRequestTypeDef(BaseModel):
    template: str
    worldCount: WorldCountTypeDef
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    worldTags: Optional[Mapping[str, str]] = None

class CreateWorldGenerationJobResponseTypeDef(BaseModel):
    arn: str
    status: WorldGenerationJobStatusType
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCodeType
    clientRequestToken: str
    template: str
    worldCount: WorldCountTypeDef
    tags: Dict[str, str]
    worldTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class WorldGenerationJobSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    template: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[WorldGenerationJobStatusType] = None
    worldCount: Optional[WorldCountTypeDef] = None
    succeededWorldCount: Optional[int] = None
    failedWorldCount: Optional[int] = None

class CreateWorldTemplateRequestRequestTypeDef(BaseModel):
    clientRequestToken: Optional[str] = None
    name: Optional[str] = None
    templateBody: Optional[str] = None
    templateLocation: Optional[TemplateLocationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateWorldTemplateRequestRequestTypeDef(BaseModel):
    template: str
    name: Optional[str] = None
    templateBody: Optional[str] = None
    templateLocation: Optional[TemplateLocationTypeDef] = None

class DataSourceTypeDef(BaseModel):
    name: Optional[str] = None
    s3Bucket: Optional[str] = None
    s3Keys: Optional[List[S3KeyOutputTypeDef]] = None
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None

class DeploymentApplicationConfigPaginatorTypeDef(BaseModel):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigPaginatorTypeDef

class DeploymentApplicationConfigTypeDef(BaseModel):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigTypeDef

class DeploymentConfigTypeDef(BaseModel):
    concurrentDeploymentPercentage: Optional[int] = None
    failureThresholdPercentage: Optional[int] = None
    robotDeploymentTimeoutInSeconds: Optional[int] = None
    downloadConditionFile: Optional[S3ObjectTypeDef] = None

class DescribeFleetResponseTypeDef(BaseModel):
    name: str
    arn: str
    robots: List[RobotTypeDef]
    createdAt: datetime
    lastDeploymentStatus: DeploymentStatusType
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRobotsResponseTypeDef(BaseModel):
    robots: List[RobotTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSimulationJobsResponseTypeDef(BaseModel):
    simulationJobSummaries: List[SimulationJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FailureSummaryTypeDef(BaseModel):
    totalFailureCount: Optional[int] = None
    failures: Optional[List[WorldFailureTypeDef]] = None

class ListDeploymentJobsRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFleetsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListRobotApplicationsRequestRequestTypeDef(BaseModel):
    versionQualifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListRobotsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListSimulationApplicationsRequestRequestTypeDef(BaseModel):
    versionQualifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListSimulationJobBatchesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListSimulationJobsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListWorldExportJobsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListWorldGenerationJobsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListWorldsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListFleetsResponseTypeDef(BaseModel):
    fleetDetails: List[FleetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentJobsRequestListDeploymentJobsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsRequestListFleetsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRobotApplicationsRequestListRobotApplicationsPaginateTypeDef(BaseModel):
    versionQualifier: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRobotsRequestListRobotsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationApplicationsRequestListSimulationApplicationsPaginateTypeDef(BaseModel):
    versionQualifier: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationJobsRequestListSimulationJobsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldExportJobsRequestListWorldExportJobsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldTemplatesRequestListWorldTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldsRequestListWorldsPaginateTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationJobBatchesResponseTypeDef(BaseModel):
    simulationJobBatchSummaries: List[SimulationJobBatchSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldTemplatesResponseTypeDef(BaseModel):
    templateSummaries: List[TemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldsResponseTypeDef(BaseModel):
    worldSummaries: List[WorldSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PortForwardingConfigTypeDef(BaseModel):
    portMappings: Optional[List[PortMappingTypeDef]] = None

class RobotDeploymentTypeDef(BaseModel):
    arn: Optional[str] = None
    deploymentStartTime: Optional[datetime] = None
    deploymentFinishTime: Optional[datetime] = None
    status: Optional[RobotStatusType] = None
    progressDetail: Optional[ProgressDetailTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None

class ListRobotApplicationsResponseTypeDef(BaseModel):
    robotApplicationSummaries: List[RobotApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSimulationApplicationsResponseTypeDef(BaseModel):
    simulationApplicationSummaries: List[SimulationApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldExportJobsResponseTypeDef(BaseModel):
    worldExportJobSummaries: List[WorldExportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldGenerationJobsResponseTypeDef(BaseModel):
    worldGenerationJobSummaries: List[WorldGenerationJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentJobRequestRequestTypeDef(BaseModel):
    clientRequestToken: str
    fleet: str
    deploymentApplicationConfigs: Sequence[DeploymentApplicationConfigTypeDef]
    deploymentConfig: Optional[DeploymentConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDeploymentJobResponseTypeDef(BaseModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentApplicationConfigs: List[DeploymentApplicationConfigTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    deploymentConfig: DeploymentConfigTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentJobPaginatorTypeDef(BaseModel):
    arn: Optional[str] = None
    fleet: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    deploymentApplicationConfigs: Optional[       List[DeploymentApplicationConfigPaginatorTypeDef]     ] = None
    deploymentConfig: Optional[DeploymentConfigTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None
    createdAt: Optional[datetime] = None

class DeploymentJobTypeDef(BaseModel):
    arn: Optional[str] = None
    fleet: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    deploymentApplicationConfigs: Optional[List[DeploymentApplicationConfigTypeDef]] = None
    deploymentConfig: Optional[DeploymentConfigTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None
    createdAt: Optional[datetime] = None

class SyncDeploymentJobResponseTypeDef(BaseModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfigTypeDef
    deploymentApplicationConfigs: List[DeploymentApplicationConfigTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class FinishedWorldsSummaryTypeDef(BaseModel):
    finishedCount: Optional[int] = None
    succeededWorlds: Optional[List[str]] = None
    failureSummary: Optional[FailureSummaryTypeDef] = None

class LaunchConfigTypeDef(BaseModel):
    packageName: Optional[str] = None
    launchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None
    portForwardingConfig: Optional[PortForwardingConfigTypeDef] = None
    streamUI: Optional[bool] = None
    command: Optional[List[str]] = None

class DescribeDeploymentJobResponseTypeDef(BaseModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfigTypeDef
    deploymentApplicationConfigs: List[DeploymentApplicationConfigTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    robotDeploymentSummary: List[RobotDeploymentTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentJobsResponsePaginatorTypeDef(BaseModel):
    deploymentJobs: List[DeploymentJobPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentJobsResponseTypeDef(BaseModel):
    deploymentJobs: List[DeploymentJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldGenerationJobResponseTypeDef(BaseModel):
    arn: str
    status: WorldGenerationJobStatusType
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    template: str
    worldCount: WorldCountTypeDef
    finishedWorldsSummary: FinishedWorldsSummaryTypeDef
    tags: Dict[str, str]
    worldTags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RobotApplicationConfigTypeDef(BaseModel):
    application: str
    launchConfig: LaunchConfigTypeDef
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfigurationTypeDef]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[ToolTypeDef]] = None
    useDefaultTools: Optional[bool] = None

class SimulationApplicationConfigTypeDef(BaseModel):
    application: str
    launchConfig: LaunchConfigTypeDef
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfigurationTypeDef]] = None
    worldConfigs: Optional[List[WorldConfigTypeDef]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[ToolTypeDef]] = None
    useDefaultTools: Optional[bool] = None

class CreateSimulationJobRequestRequestTypeDef(BaseModel):
    maxJobDurationInSeconds: int
    iamRole: str
    clientRequestToken: Optional[str] = None
    outputLocation: Optional[OutputLocationTypeDef] = None
    loggingConfig: Optional[LoggingConfigTypeDef] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    robotApplications: Optional[Sequence[RobotApplicationConfigTypeDef]] = None
    simulationApplications: Optional[Sequence[SimulationApplicationConfigTypeDef]] = None
    dataSources: Optional[Sequence[DataSourceConfigTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    vpcConfig: Optional[VPCConfigTypeDef] = None
    compute: Optional[ComputeTypeDef] = None

class CreateSimulationJobResponseTypeDef(BaseModel):
    arn: str
    status: SimulationJobStatusType
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehaviorType
    failureCode: SimulationJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    loggingConfig: LoggingConfigTypeDef
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List[RobotApplicationConfigTypeDef]
    simulationApplications: List[SimulationApplicationConfigTypeDef]
    dataSources: List[DataSourceTypeDef]
    tags: Dict[str, str]
    vpcConfig: VPCConfigResponseTypeDef
    compute: ComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationJobResponseTypeDef(BaseModel):
    arn: str
    name: str
    status: SimulationJobStatusType
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehaviorType
    failureCode: SimulationJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    loggingConfig: LoggingConfigTypeDef
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List[RobotApplicationConfigTypeDef]
    simulationApplications: List[SimulationApplicationConfigTypeDef]
    dataSources: List[DataSourceTypeDef]
    tags: Dict[str, str]
    vpcConfig: VPCConfigResponseTypeDef
    networkInterface: NetworkInterfaceTypeDef
    compute: ComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SimulationJobRequestTypeDef(BaseModel):
    maxJobDurationInSeconds: int
    outputLocation: Optional[OutputLocationTypeDef] = None
    loggingConfig: Optional[LoggingConfigTypeDef] = None
    iamRole: Optional[str] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    useDefaultApplications: Optional[bool] = None
    robotApplications: Optional[List[RobotApplicationConfigTypeDef]] = None
    simulationApplications: Optional[List[SimulationApplicationConfigTypeDef]] = None
    dataSources: Optional[List[DataSourceConfigTypeDef]] = None
    vpcConfig: Optional[VPCConfigTypeDef] = None
    compute: Optional[ComputeTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class SimulationJobTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    status: Optional[SimulationJobStatusType] = None
    lastStartedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    failureCode: Optional[SimulationJobErrorCodeType] = None
    failureReason: Optional[str] = None
    clientRequestToken: Optional[str] = None
    outputLocation: Optional[OutputLocationTypeDef] = None
    loggingConfig: Optional[LoggingConfigTypeDef] = None
    maxJobDurationInSeconds: Optional[int] = None
    simulationTimeMillis: Optional[int] = None
    iamRole: Optional[str] = None
    robotApplications: Optional[List[RobotApplicationConfigTypeDef]] = None
    simulationApplications: Optional[List[SimulationApplicationConfigTypeDef]] = None
    dataSources: Optional[List[DataSourceTypeDef]] = None
    tags: Optional[Dict[str, str]] = None
    vpcConfig: Optional[VPCConfigResponseTypeDef] = None
    networkInterface: Optional[NetworkInterfaceTypeDef] = None
    compute: Optional[ComputeResponseTypeDef] = None

class FailedCreateSimulationJobRequestTypeDef(BaseModel):
    request: Optional[SimulationJobRequestTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[SimulationJobErrorCodeType] = None
    failedAt: Optional[datetime] = None

class StartSimulationJobBatchRequestRequestTypeDef(BaseModel):
    createSimulationJobRequests: Sequence[SimulationJobRequestTypeDef]
    clientRequestToken: Optional[str] = None
    batchPolicy: Optional[BatchPolicyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class BatchDescribeSimulationJobResponseTypeDef(BaseModel):
    jobs: List[SimulationJobTypeDef]
    unprocessedJobs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationJobBatchResponseTypeDef(BaseModel):
    arn: str
    status: SimulationJobBatchStatusType
    lastUpdatedAt: datetime
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: BatchPolicyTypeDef
    failureCode: Literal["InternalServiceError"]
    failureReason: str
    failedRequests: List[FailedCreateSimulationJobRequestTypeDef]
    pendingRequests: List[SimulationJobRequestTypeDef]
    createdRequests: List[SimulationJobSummaryTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSimulationJobBatchResponseTypeDef(BaseModel):
    arn: str
    status: SimulationJobBatchStatusType
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: BatchPolicyTypeDef
    failureCode: Literal["InternalServiceError"]
    failureReason: str
    failedRequests: List[FailedCreateSimulationJobRequestTypeDef]
    pendingRequests: List[SimulationJobRequestTypeDef]
    createdRequests: List[SimulationJobSummaryTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

