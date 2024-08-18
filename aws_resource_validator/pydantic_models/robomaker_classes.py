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
from aws_resource_validator.pydantic_models.robomaker_constants import *

class BatchDeleteWorldsRequestRequestTypeDef(BaseValidatorModel):
    worlds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchDescribeSimulationJobRequestRequestTypeDef(BaseValidatorModel):
    jobs: Sequence[str]

class BatchPolicyTypeDef(BaseValidatorModel):
    timeoutInSeconds: Optional[int] = None
    maxConcurrency: Optional[int] = None

class CancelDeploymentJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class CancelSimulationJobBatchRequestRequestTypeDef(BaseValidatorModel):
    batch: str

class CancelSimulationJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class CancelWorldExportJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class CancelWorldGenerationJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class ComputeResponseTypeDef(BaseValidatorModel):
    simulationUnitLimit: Optional[int] = None
    computeType: Optional[ComputeTypeType] = None
    gpuUnitLimit: Optional[int] = None

class ComputeTypeDef(BaseValidatorModel):
    simulationUnitLimit: Optional[int] = None
    computeType: Optional[ComputeTypeType] = None
    gpuUnitLimit: Optional[int] = None

class CreateFleetRequestRequestTypeDef(BaseValidatorModel):
    name: str
    tags: Optional[Mapping[str, str]] = None

class EnvironmentTypeDef(BaseValidatorModel):
    uri: Optional[str] = None

class RobotSoftwareSuiteTypeDef(BaseValidatorModel):
    name: Optional[RobotSoftwareSuiteTypeType] = None
    version: Optional[RobotSoftwareSuiteVersionTypeType] = None

class SourceConfigTypeDef(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    architecture: Optional[ArchitectureType] = None

class SourceTypeDef(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    etag: Optional[str] = None
    architecture: Optional[ArchitectureType] = None

class CreateRobotApplicationVersionRequestRequestTypeDef(BaseValidatorModel):
    application: str
    currentRevisionId: Optional[str] = None
    s3Etags: Optional[Sequence[str]] = None
    imageDigest: Optional[str] = None

class CreateRobotRequestRequestTypeDef(BaseValidatorModel):
    name: str
    architecture: ArchitectureType
    greengrassGroupId: str
    tags: Optional[Mapping[str, str]] = None

class RenderingEngineTypeDef(BaseValidatorModel):
    name: Optional[Literal["OGRE"]] = None
    version: Optional[str] = None

class SimulationSoftwareSuiteTypeDef(BaseValidatorModel):
    name: Optional[SimulationSoftwareSuiteTypeType] = None
    version: Optional[str] = None

class CreateSimulationApplicationVersionRequestRequestTypeDef(BaseValidatorModel):
    application: str
    currentRevisionId: Optional[str] = None
    s3Etags: Optional[Sequence[str]] = None
    imageDigest: Optional[str] = None

class DataSourceConfigTypeDef(BaseValidatorModel):
    name: str
    s3Bucket: str
    s3Keys: Sequence[str]
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None

class LoggingConfigTypeDef(BaseValidatorModel):
    recordAllRosTopics: Optional[bool] = None

class OutputLocationTypeDef(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Prefix: Optional[str] = None

class VPCConfigTypeDef(BaseValidatorModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None
    assignPublicIp: Optional[bool] = None

class VPCConfigResponseTypeDef(BaseValidatorModel):
    subnets: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    assignPublicIp: Optional[bool] = None

class WorldCountTypeDef(BaseValidatorModel):
    floorplanCount: Optional[int] = None
    interiorCountPerFloorplan: Optional[int] = None

class TemplateLocationTypeDef(BaseValidatorModel):
    s3Bucket: str
    s3Key: str

class S3KeyOutputTypeDef(BaseValidatorModel):
    s3Key: Optional[str] = None
    etag: Optional[str] = None

class DeleteFleetRequestRequestTypeDef(BaseValidatorModel):
    fleet: str

class DeleteRobotApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None

class DeleteRobotRequestRequestTypeDef(BaseValidatorModel):
    robot: str

class DeleteSimulationApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None

class DeleteWorldTemplateRequestRequestTypeDef(BaseValidatorModel):
    template: str

class DeploymentLaunchConfigPaginatorTypeDef(BaseValidatorModel):
    packageName: str
    launchFile: str
    preLaunchFile: Optional[str] = None
    postLaunchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None

class DeploymentLaunchConfigTypeDef(BaseValidatorModel):
    packageName: str
    launchFile: str
    preLaunchFile: Optional[str] = None
    postLaunchFile: Optional[str] = None
    environmentVariables: Optional[Mapping[str, str]] = None

class S3ObjectTypeDef(BaseValidatorModel):
    bucket: str
    key: str
    etag: Optional[str] = None

class DeregisterRobotRequestRequestTypeDef(BaseValidatorModel):
    fleet: str
    robot: str

class DescribeDeploymentJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class DescribeFleetRequestRequestTypeDef(BaseValidatorModel):
    fleet: str

class RobotTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    fleetArn: Optional[str] = None
    status: Optional[RobotStatusType] = None
    greenGrassGroupId: Optional[str] = None
    createdAt: Optional[datetime] = None
    architecture: Optional[ArchitectureType] = None
    lastDeploymentJob: Optional[str] = None
    lastDeploymentTime: Optional[datetime] = None

class DescribeRobotApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None

class DescribeRobotRequestRequestTypeDef(BaseValidatorModel):
    robot: str

class DescribeSimulationApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None

class DescribeSimulationJobBatchRequestRequestTypeDef(BaseValidatorModel):
    batch: str

class SimulationJobSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[SimulationJobStatusType] = None
    simulationApplicationNames: Optional[List[str]] = None
    robotApplicationNames: Optional[List[str]] = None
    dataSourceNames: Optional[List[str]] = None
    computeType: Optional[ComputeTypeType] = None

class DescribeSimulationJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class NetworkInterfaceTypeDef(BaseValidatorModel):
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None

class DescribeWorldExportJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class DescribeWorldGenerationJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class DescribeWorldRequestRequestTypeDef(BaseValidatorModel):
    world: str

class DescribeWorldTemplateRequestRequestTypeDef(BaseValidatorModel):
    template: str

class WorldFailureTypeDef(BaseValidatorModel):
    failureCode: Optional[WorldGenerationJobErrorCodeType] = None
    sampleFailureReason: Optional[str] = None
    failureCount: Optional[int] = None

class FilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class FleetTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastDeploymentStatus: Optional[DeploymentStatusType] = None
    lastDeploymentJob: Optional[str] = None
    lastDeploymentTime: Optional[datetime] = None

class GetWorldTemplateBodyRequestRequestTypeDef(BaseValidatorModel):
    template: Optional[str] = None
    generationJob: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class SimulationJobBatchSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    status: Optional[SimulationJobBatchStatusType] = None
    failedRequestCount: Optional[int] = None
    pendingRequestCount: Optional[int] = None
    createdRequestCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListWorldTemplatesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TemplateSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    version: Optional[str] = None

class WorldSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    generationJob: Optional[str] = None
    template: Optional[str] = None

class PortMappingTypeDef(BaseValidatorModel):
    jobPort: int
    applicationPort: int
    enableOnPublicIp: Optional[bool] = None

class ProgressDetailTypeDef(BaseValidatorModel):
    currentProgress: Optional[RobotDeploymentStepType] = None
    percentDone: Optional[float] = None
    estimatedTimeRemainingSeconds: Optional[int] = None
    targetResource: Optional[str] = None

class RegisterRobotRequestRequestTypeDef(BaseValidatorModel):
    fleet: str
    robot: str

class RestartSimulationJobRequestRequestTypeDef(BaseValidatorModel):
    job: str

class ToolTypeDef(BaseValidatorModel):
    name: str
    command: str
    streamUI: Optional[bool] = None
    streamOutputToCloudWatch: Optional[bool] = None
    exitBehavior: Optional[ExitBehaviorType] = None

class UploadConfigurationTypeDef(BaseValidatorModel):
    name: str
    path: str
    uploadBehavior: UploadBehaviorType

class WorldConfigTypeDef(BaseValidatorModel):
    world: Optional[str] = None

class SyncDeploymentJobRequestRequestTypeDef(BaseValidatorModel):
    clientRequestToken: str
    fleet: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchDeleteWorldsResponseTypeDef(BaseValidatorModel):
    unprocessedWorlds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRobotResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    greengrassGroupId: str
    architecture: ArchitectureType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorldTemplateResponseTypeDef(BaseValidatorModel):
    arn: str
    clientRequestToken: str
    createdAt: datetime
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterRobotResponseTypeDef(BaseValidatorModel):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRobotResponseTypeDef(BaseValidatorModel):
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

class DescribeWorldResponseTypeDef(BaseValidatorModel):
    arn: str
    generationJob: str
    template: str
    createdAt: datetime
    tags: Dict[str, str]
    worldDescriptionBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldTemplateResponseTypeDef(BaseValidatorModel):
    arn: str
    clientRequestToken: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorldTemplateBodyResponseTypeDef(BaseValidatorModel):
    templateBody: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterRobotResponseTypeDef(BaseValidatorModel):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorldTemplateResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RobotApplicationSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    version: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    robotSoftwareSuite: Optional[RobotSoftwareSuiteTypeDef] = None

class CreateRobotApplicationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    environment: Optional[EnvironmentTypeDef] = None

class UpdateRobotApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    currentRevisionId: Optional[str] = None
    environment: Optional[EnvironmentTypeDef] = None

class CreateRobotApplicationResponseTypeDef(BaseValidatorModel):
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

class CreateRobotApplicationVersionResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRobotApplicationResponseTypeDef(BaseValidatorModel):
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

class UpdateRobotApplicationResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[SourceTypeDef]
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    lastUpdatedAt: datetime
    revisionId: str
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSimulationApplicationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    renderingEngine: Optional[RenderingEngineTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    environment: Optional[EnvironmentTypeDef] = None

class CreateSimulationApplicationResponseTypeDef(BaseValidatorModel):
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

class CreateSimulationApplicationVersionResponseTypeDef(BaseValidatorModel):
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

class DescribeSimulationApplicationResponseTypeDef(BaseValidatorModel):
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

class SimulationApplicationSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    version: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    robotSoftwareSuite: Optional[RobotSoftwareSuiteTypeDef] = None
    simulationSoftwareSuite: Optional[SimulationSoftwareSuiteTypeDef] = None

class UpdateSimulationApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    simulationSoftwareSuite: SimulationSoftwareSuiteTypeDef
    robotSoftwareSuite: RobotSoftwareSuiteTypeDef
    sources: Optional[Sequence[SourceConfigTypeDef]] = None
    renderingEngine: Optional[RenderingEngineTypeDef] = None
    currentRevisionId: Optional[str] = None
    environment: Optional[EnvironmentTypeDef] = None

class UpdateSimulationApplicationResponseTypeDef(BaseValidatorModel):
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

class CreateWorldExportJobRequestRequestTypeDef(BaseValidatorModel):
    worlds: Sequence[str]
    outputLocation: OutputLocationTypeDef
    iamRole: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateWorldExportJobResponseTypeDef(BaseValidatorModel):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocationTypeDef
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldExportJobResponseTypeDef(BaseValidatorModel):
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

class WorldExportJobSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[WorldExportJobStatusType] = None
    createdAt: Optional[datetime] = None
    worlds: Optional[List[str]] = None
    outputLocation: Optional[OutputLocationTypeDef] = None

class CreateWorldGenerationJobRequestRequestTypeDef(BaseValidatorModel):
    template: str
    worldCount: WorldCountTypeDef
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    worldTags: Optional[Mapping[str, str]] = None

class CreateWorldGenerationJobResponseTypeDef(BaseValidatorModel):
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

class WorldGenerationJobSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    template: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[WorldGenerationJobStatusType] = None
    worldCount: Optional[WorldCountTypeDef] = None
    succeededWorldCount: Optional[int] = None
    failedWorldCount: Optional[int] = None

class CreateWorldTemplateRequestRequestTypeDef(BaseValidatorModel):
    clientRequestToken: Optional[str] = None
    name: Optional[str] = None
    templateBody: Optional[str] = None
    templateLocation: Optional[TemplateLocationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateWorldTemplateRequestRequestTypeDef(BaseValidatorModel):
    template: str
    name: Optional[str] = None
    templateBody: Optional[str] = None
    templateLocation: Optional[TemplateLocationTypeDef] = None

class DataSourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    s3Bucket: Optional[str] = None
    s3Keys: Optional[List[S3KeyOutputTypeDef]] = None
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None

class DeploymentApplicationConfigPaginatorTypeDef(BaseValidatorModel):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigPaginatorTypeDef

class DeploymentApplicationConfigTypeDef(BaseValidatorModel):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigTypeDef

class DeploymentConfigTypeDef(BaseValidatorModel):
    concurrentDeploymentPercentage: Optional[int] = None
    failureThresholdPercentage: Optional[int] = None
    robotDeploymentTimeoutInSeconds: Optional[int] = None
    downloadConditionFile: Optional[S3ObjectTypeDef] = None

class DescribeFleetResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    robots: List[RobotTypeDef]
    createdAt: datetime
    lastDeploymentStatus: DeploymentStatusType
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRobotsResponseTypeDef(BaseValidatorModel):
    robots: List[RobotTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSimulationJobsResponseTypeDef(BaseValidatorModel):
    simulationJobSummaries: List[SimulationJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FailureSummaryTypeDef(BaseValidatorModel):
    totalFailureCount: Optional[int] = None
    failures: Optional[List[WorldFailureTypeDef]] = None

class ListDeploymentJobsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFleetsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListRobotApplicationsRequestRequestTypeDef(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListRobotsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListSimulationApplicationsRequestRequestTypeDef(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListSimulationJobBatchesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListSimulationJobsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListWorldExportJobsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListWorldGenerationJobsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListWorldsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[FilterTypeDef]] = None

class ListFleetsResponseTypeDef(BaseValidatorModel):
    fleetDetails: List[FleetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentJobsRequestListDeploymentJobsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsRequestListFleetsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRobotApplicationsRequestListRobotApplicationsPaginateTypeDef(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRobotsRequestListRobotsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationApplicationsRequestListSimulationApplicationsPaginateTypeDef(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationJobBatchesRequestListSimulationJobBatchesPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationJobsRequestListSimulationJobsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldExportJobsRequestListWorldExportJobsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldGenerationJobsRequestListWorldGenerationJobsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldTemplatesRequestListWorldTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorldsRequestListWorldsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSimulationJobBatchesResponseTypeDef(BaseValidatorModel):
    simulationJobBatchSummaries: List[SimulationJobBatchSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldTemplatesResponseTypeDef(BaseValidatorModel):
    templateSummaries: List[TemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldsResponseTypeDef(BaseValidatorModel):
    worldSummaries: List[WorldSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PortForwardingConfigTypeDef(BaseValidatorModel):
    portMappings: Optional[List[PortMappingTypeDef]] = None

class RobotDeploymentTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    deploymentStartTime: Optional[datetime] = None
    deploymentFinishTime: Optional[datetime] = None
    status: Optional[RobotStatusType] = None
    progressDetail: Optional[ProgressDetailTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None

class ListRobotApplicationsResponseTypeDef(BaseValidatorModel):
    robotApplicationSummaries: List[RobotApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSimulationApplicationsResponseTypeDef(BaseValidatorModel):
    simulationApplicationSummaries: List[SimulationApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldExportJobsResponseTypeDef(BaseValidatorModel):
    worldExportJobSummaries: List[WorldExportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorldGenerationJobsResponseTypeDef(BaseValidatorModel):
    worldGenerationJobSummaries: List[WorldGenerationJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentJobRequestRequestTypeDef(BaseValidatorModel):
    clientRequestToken: str
    fleet: str
    deploymentApplicationConfigs: Sequence[DeploymentApplicationConfigTypeDef]
    deploymentConfig: Optional[DeploymentConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDeploymentJobResponseTypeDef(BaseValidatorModel):
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

class DeploymentJobPaginatorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    fleet: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    deploymentApplicationConfigs: Optional[       List[DeploymentApplicationConfigPaginatorTypeDef]     ] = None
    deploymentConfig: Optional[DeploymentConfigTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None
    createdAt: Optional[datetime] = None

class DeploymentJobTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    fleet: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    deploymentApplicationConfigs: Optional[List[DeploymentApplicationConfigTypeDef]] = None
    deploymentConfig: Optional[DeploymentConfigTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None
    createdAt: Optional[datetime] = None

class SyncDeploymentJobResponseTypeDef(BaseValidatorModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfigTypeDef
    deploymentApplicationConfigs: List[DeploymentApplicationConfigTypeDef]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class FinishedWorldsSummaryTypeDef(BaseValidatorModel):
    finishedCount: Optional[int] = None
    succeededWorlds: Optional[List[str]] = None
    failureSummary: Optional[FailureSummaryTypeDef] = None

class LaunchConfigTypeDef(BaseValidatorModel):
    packageName: Optional[str] = None
    launchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None
    portForwardingConfig: Optional[PortForwardingConfigTypeDef] = None
    streamUI: Optional[bool] = None
    command: Optional[List[str]] = None

class DescribeDeploymentJobResponseTypeDef(BaseValidatorModel):
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

class ListDeploymentJobsResponsePaginatorTypeDef(BaseValidatorModel):
    deploymentJobs: List[DeploymentJobPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentJobsResponseTypeDef(BaseValidatorModel):
    deploymentJobs: List[DeploymentJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorldGenerationJobResponseTypeDef(BaseValidatorModel):
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

class RobotApplicationConfigTypeDef(BaseValidatorModel):
    application: str
    launchConfig: LaunchConfigTypeDef
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfigurationTypeDef]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[ToolTypeDef]] = None
    useDefaultTools: Optional[bool] = None

class SimulationApplicationConfigTypeDef(BaseValidatorModel):
    application: str
    launchConfig: LaunchConfigTypeDef
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfigurationTypeDef]] = None
    worldConfigs: Optional[List[WorldConfigTypeDef]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[ToolTypeDef]] = None
    useDefaultTools: Optional[bool] = None

class CreateSimulationJobRequestRequestTypeDef(BaseValidatorModel):
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

class CreateSimulationJobResponseTypeDef(BaseValidatorModel):
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

class DescribeSimulationJobResponseTypeDef(BaseValidatorModel):
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

class SimulationJobRequestTypeDef(BaseValidatorModel):
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

class SimulationJobTypeDef(BaseValidatorModel):
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

class FailedCreateSimulationJobRequestTypeDef(BaseValidatorModel):
    request: Optional[SimulationJobRequestTypeDef] = None
    failureReason: Optional[str] = None
    failureCode: Optional[SimulationJobErrorCodeType] = None
    failedAt: Optional[datetime] = None

class StartSimulationJobBatchRequestRequestTypeDef(BaseValidatorModel):
    createSimulationJobRequests: Sequence[SimulationJobRequestTypeDef]
    clientRequestToken: Optional[str] = None
    batchPolicy: Optional[BatchPolicyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class BatchDescribeSimulationJobResponseTypeDef(BaseValidatorModel):
    jobs: List[SimulationJobTypeDef]
    unprocessedJobs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSimulationJobBatchResponseTypeDef(BaseValidatorModel):
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

class StartSimulationJobBatchResponseTypeDef(BaseValidatorModel):
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

