from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.robomaker.robomaker_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'batch_delete_worlds' function.
class BatchDeleteWorldsRequest(BaseValidatorModel):
    worlds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'batch_describe_simulation_job' function.
class BatchDescribeSimulationJobRequest(BaseValidatorModel):
    jobs: List[str]


class BatchPolicy(BaseValidatorModel):
    timeoutInSeconds: Optional[int] = None
    maxConcurrency: Optional[int] = None


class CancelDeploymentJobRequest(BaseValidatorModel):
    job: str


class CancelSimulationJobBatchRequest(BaseValidatorModel):
    batch: str


class CancelSimulationJobRequest(BaseValidatorModel):
    job: str


class CancelWorldExportJobRequest(BaseValidatorModel):
    job: str


class CancelWorldGenerationJobRequest(BaseValidatorModel):
    job: str


class ComputeResponse(BaseValidatorModel):
    simulationUnitLimit: Optional[int] = None
    computeType: Optional[ComputeTypeType] = None
    gpuUnitLimit: Optional[int] = None


class Compute(BaseValidatorModel):
    simulationUnitLimit: Optional[int] = None
    computeType: Optional[ComputeTypeType] = None
    gpuUnitLimit: Optional[int] = None


# This class is the input for the 'create_fleet' function.
class CreateFleetRequest(BaseValidatorModel):
    name: str
    tags: Optional[Dict[str, str]] = None


class Environment(BaseValidatorModel):
    uri: Optional[str] = None


class RobotSoftwareSuite(BaseValidatorModel):
    name: Optional[RobotSoftwareSuiteTypeType] = None
    version: Optional[RobotSoftwareSuiteVersionTypeType] = None


class SourceConfig(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    architecture: Optional[ArchitectureType] = None


class Source(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Key: Optional[str] = None
    etag: Optional[str] = None
    architecture: Optional[ArchitectureType] = None


# This class is the input for the 'create_robot_application_version' function.
class CreateRobotApplicationVersionRequest(BaseValidatorModel):
    application: str
    currentRevisionId: Optional[str] = None
    s3Etags: Optional[List[str]] = None
    imageDigest: Optional[str] = None


# This class is the input for the 'create_robot' function.
class CreateRobotRequest(BaseValidatorModel):
    name: str
    architecture: ArchitectureType
    greengrassGroupId: str
    tags: Optional[Dict[str, str]] = None


class RenderingEngine(BaseValidatorModel):
    name: Optional[Literal['OGRE']] = None
    version: Optional[str] = None


class SimulationSoftwareSuite(BaseValidatorModel):
    name: Optional[SimulationSoftwareSuiteTypeType] = None
    version: Optional[str] = None


# This class is the input for the 'create_simulation_application_version' function.
class CreateSimulationApplicationVersionRequest(BaseValidatorModel):
    application: str
    currentRevisionId: Optional[str] = None
    s3Etags: Optional[List[str]] = None
    imageDigest: Optional[str] = None


class LoggingConfig(BaseValidatorModel):
    recordAllRosTopics: Optional[bool] = None


class OutputLocation(BaseValidatorModel):
    s3Bucket: Optional[str] = None
    s3Prefix: Optional[str] = None


class VPCConfigResponse(BaseValidatorModel):
    subnets: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    assignPublicIp: Optional[bool] = None


class WorldCount(BaseValidatorModel):
    floorplanCount: Optional[int] = None
    interiorCountPerFloorplan: Optional[int] = None


class TemplateLocation(BaseValidatorModel):
    s3Bucket: str
    s3Key: str


class DataSourceConfigOutput(BaseValidatorModel):
    name: str
    s3Bucket: str
    s3Keys: List[str]
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None


class DataSourceConfig(BaseValidatorModel):
    name: str
    s3Bucket: str
    s3Keys: List[str]
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None


class S3KeyOutput(BaseValidatorModel):
    s3Key: Optional[str] = None
    etag: Optional[str] = None


class DeleteFleetRequest(BaseValidatorModel):
    fleet: str


class DeleteRobotApplicationRequest(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None


class DeleteRobotRequest(BaseValidatorModel):
    robot: str


class DeleteSimulationApplicationRequest(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None


class DeleteWorldTemplateRequest(BaseValidatorModel):
    template: str


class DeploymentLaunchConfigOutput(BaseValidatorModel):
    packageName: str
    launchFile: str
    preLaunchFile: Optional[str] = None
    postLaunchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None


class S3Object(BaseValidatorModel):
    bucket: str
    key: str
    etag: Optional[str] = None


class DeploymentLaunchConfig(BaseValidatorModel):
    packageName: str
    launchFile: str
    preLaunchFile: Optional[str] = None
    postLaunchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None


# This class is the input for the 'deregister_robot' function.
class DeregisterRobotRequest(BaseValidatorModel):
    fleet: str
    robot: str


# This class is the input for the 'describe_deployment_job' function.
class DescribeDeploymentJobRequest(BaseValidatorModel):
    job: str


# This class is the input for the 'describe_fleet' function.
class DescribeFleetRequest(BaseValidatorModel):
    fleet: str


class Robot(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    fleetArn: Optional[str] = None
    status: Optional[RobotStatusType] = None
    greenGrassGroupId: Optional[str] = None
    createdAt: Optional[datetime] = None
    architecture: Optional[ArchitectureType] = None
    lastDeploymentJob: Optional[str] = None
    lastDeploymentTime: Optional[datetime] = None


# This class is the input for the 'describe_robot_application' function.
class DescribeRobotApplicationRequest(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None


# This class is the input for the 'describe_robot' function.
class DescribeRobotRequest(BaseValidatorModel):
    robot: str


# This class is the input for the 'describe_simulation_application' function.
class DescribeSimulationApplicationRequest(BaseValidatorModel):
    application: str
    applicationVersion: Optional[str] = None


# This class is the input for the 'describe_simulation_job_batch' function.
class DescribeSimulationJobBatchRequest(BaseValidatorModel):
    batch: str


class SimulationJobSummary(BaseValidatorModel):
    arn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[SimulationJobStatusType] = None
    simulationApplicationNames: Optional[List[str]] = None
    robotApplicationNames: Optional[List[str]] = None
    dataSourceNames: Optional[List[str]] = None
    computeType: Optional[ComputeTypeType] = None


# This class is the input for the 'describe_simulation_job' function.
class DescribeSimulationJobRequest(BaseValidatorModel):
    job: str


class NetworkInterface(BaseValidatorModel):
    networkInterfaceId: Optional[str] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None


# This class is the input for the 'describe_world_export_job' function.
class DescribeWorldExportJobRequest(BaseValidatorModel):
    job: str


# This class is the input for the 'describe_world_generation_job' function.
class DescribeWorldGenerationJobRequest(BaseValidatorModel):
    job: str


# This class is the input for the 'describe_world' function.
class DescribeWorldRequest(BaseValidatorModel):
    world: str


# This class is the input for the 'describe_world_template' function.
class DescribeWorldTemplateRequest(BaseValidatorModel):
    template: str


class WorldFailure(BaseValidatorModel):
    failureCode: Optional[WorldGenerationJobErrorCodeType] = None
    sampleFailureReason: Optional[str] = None
    failureCount: Optional[int] = None


class Filter(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class Fleet(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastDeploymentStatus: Optional[DeploymentStatusType] = None
    lastDeploymentJob: Optional[str] = None
    lastDeploymentTime: Optional[datetime] = None


# This class is the input for the 'get_world_template_body' function.
class GetWorldTemplateBodyRequest(BaseValidatorModel):
    template: Optional[str] = None
    generationJob: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class SimulationJobBatchSummary(BaseValidatorModel):
    arn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    status: Optional[SimulationJobBatchStatusType] = None
    failedRequestCount: Optional[int] = None
    pendingRequestCount: Optional[int] = None
    createdRequestCount: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_world_templates' function.
class ListWorldTemplatesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TemplateSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    version: Optional[str] = None


class WorldSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    generationJob: Optional[str] = None
    template: Optional[str] = None


class PortMapping(BaseValidatorModel):
    jobPort: int
    applicationPort: int
    enableOnPublicIp: Optional[bool] = None


class ProgressDetail(BaseValidatorModel):
    currentProgress: Optional[RobotDeploymentStepType] = None
    percentDone: Optional[float] = None
    estimatedTimeRemainingSeconds: Optional[int] = None
    targetResource: Optional[str] = None


# This class is the input for the 'register_robot' function.
class RegisterRobotRequest(BaseValidatorModel):
    fleet: str
    robot: str


class RestartSimulationJobRequest(BaseValidatorModel):
    job: str


class Tool(BaseValidatorModel):
    name: str
    command: str
    streamUI: Optional[bool] = None
    streamOutputToCloudWatch: Optional[bool] = None
    exitBehavior: Optional[ExitBehaviorType] = None


class UploadConfiguration(BaseValidatorModel):
    name: str
    path: str
    uploadBehavior: UploadBehaviorType


class WorldConfig(BaseValidatorModel):
    world: Optional[str] = None


class VPCConfigOutput(BaseValidatorModel):
    subnets: List[str]
    securityGroups: Optional[List[str]] = None
    assignPublicIp: Optional[bool] = None


# This class is the input for the 'sync_deployment_job' function.
class SyncDeploymentJobRequest(BaseValidatorModel):
    clientRequestToken: str
    fleet: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class VPCConfig(BaseValidatorModel):
    subnets: List[str]
    securityGroups: Optional[List[str]] = None
    assignPublicIp: Optional[bool] = None


# This class is the output for the 'batch_delete_worlds' function.
class BatchDeleteWorldsResponse(BaseValidatorModel):
    unprocessedWorlds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_fleet' function.
class CreateFleetResponse(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_robot' function.
class CreateRobotResponse(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    greengrassGroupId: str
    architecture: ArchitectureType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_world_template' function.
class CreateWorldTemplateResponse(BaseValidatorModel):
    arn: str
    clientRequestToken: str
    createdAt: datetime
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_robot' function.
class DeregisterRobotResponse(BaseValidatorModel):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_robot' function.
class DescribeRobotResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_world' function.
class DescribeWorldResponse(BaseValidatorModel):
    arn: str
    generationJob: str
    template: str
    createdAt: datetime
    tags: Dict[str, str]
    worldDescriptionBody: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_world_template' function.
class DescribeWorldTemplateResponse(BaseValidatorModel):
    arn: str
    clientRequestToken: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    version: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_world_template_body' function.
class GetWorldTemplateBodyResponse(BaseValidatorModel):
    templateBody: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_robot' function.
class RegisterRobotResponse(BaseValidatorModel):
    fleet: str
    robot: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_world_template' function.
class UpdateWorldTemplateResponse(BaseValidatorModel):
    arn: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class RobotApplicationSummary(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    version: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    robotSoftwareSuite: Optional[RobotSoftwareSuite] = None


# This class is the input for the 'create_robot_application' function.
class CreateRobotApplicationRequest(BaseValidatorModel):
    name: str
    robotSoftwareSuite: RobotSoftwareSuite
    sources: Optional[List[SourceConfig]] = None
    tags: Optional[Dict[str, str]] = None
    environment: Optional[Environment] = None


# This class is the input for the 'update_robot_application' function.
class UpdateRobotApplicationRequest(BaseValidatorModel):
    application: str
    robotSoftwareSuite: RobotSoftwareSuite
    sources: Optional[List[SourceConfig]] = None
    currentRevisionId: Optional[str] = None
    environment: Optional[Environment] = None


# This class is the output for the 'create_robot_application' function.
class CreateRobotApplicationResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    robotSoftwareSuite: RobotSoftwareSuite
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_robot_application_version' function.
class CreateRobotApplicationVersionResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    robotSoftwareSuite: RobotSoftwareSuite
    lastUpdatedAt: datetime
    revisionId: str
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_robot_application' function.
class DescribeRobotApplicationResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    robotSoftwareSuite: RobotSoftwareSuite
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    environment: Environment
    imageDigest: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_robot_application' function.
class UpdateRobotApplicationResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    robotSoftwareSuite: RobotSoftwareSuite
    lastUpdatedAt: datetime
    revisionId: str
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_simulation_application' function.
class CreateSimulationApplicationRequest(BaseValidatorModel):
    name: str
    simulationSoftwareSuite: SimulationSoftwareSuite
    robotSoftwareSuite: RobotSoftwareSuite
    sources: Optional[List[SourceConfig]] = None
    renderingEngine: Optional[RenderingEngine] = None
    tags: Optional[Dict[str, str]] = None
    environment: Optional[Environment] = None


# This class is the output for the 'create_simulation_application' function.
class CreateSimulationApplicationResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    simulationSoftwareSuite: SimulationSoftwareSuite
    robotSoftwareSuite: RobotSoftwareSuite
    renderingEngine: RenderingEngine
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_simulation_application_version' function.
class CreateSimulationApplicationVersionResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    simulationSoftwareSuite: SimulationSoftwareSuite
    robotSoftwareSuite: RobotSoftwareSuite
    renderingEngine: RenderingEngine
    lastUpdatedAt: datetime
    revisionId: str
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_simulation_application' function.
class DescribeSimulationApplicationResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    simulationSoftwareSuite: SimulationSoftwareSuite
    robotSoftwareSuite: RobotSoftwareSuite
    renderingEngine: RenderingEngine
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]
    environment: Environment
    imageDigest: str
    ResponseMetadata: ResponseMetadata


class SimulationApplicationSummary(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    version: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    robotSoftwareSuite: Optional[RobotSoftwareSuite] = None
    simulationSoftwareSuite: Optional[SimulationSoftwareSuite] = None


# This class is the input for the 'update_simulation_application' function.
class UpdateSimulationApplicationRequest(BaseValidatorModel):
    application: str
    simulationSoftwareSuite: SimulationSoftwareSuite
    robotSoftwareSuite: RobotSoftwareSuite
    sources: Optional[List[SourceConfig]] = None
    renderingEngine: Optional[RenderingEngine] = None
    currentRevisionId: Optional[str] = None
    environment: Optional[Environment] = None


# This class is the output for the 'update_simulation_application' function.
class UpdateSimulationApplicationResponse(BaseValidatorModel):
    arn: str
    name: str
    version: str
    sources: List[Source]
    simulationSoftwareSuite: SimulationSoftwareSuite
    robotSoftwareSuite: RobotSoftwareSuite
    renderingEngine: RenderingEngine
    lastUpdatedAt: datetime
    revisionId: str
    environment: Environment
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_world_export_job' function.
class CreateWorldExportJobRequest(BaseValidatorModel):
    worlds: List[str]
    outputLocation: OutputLocation
    iamRole: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_world_export_job' function.
class CreateWorldExportJobResponse(BaseValidatorModel):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocation
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_world_export_job' function.
class DescribeWorldExportJobResponse(BaseValidatorModel):
    arn: str
    status: WorldExportJobStatusType
    createdAt: datetime
    failureCode: WorldExportJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    worlds: List[str]
    outputLocation: OutputLocation
    iamRole: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class WorldExportJobSummary(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[WorldExportJobStatusType] = None
    createdAt: Optional[datetime] = None
    worlds: Optional[List[str]] = None
    outputLocation: Optional[OutputLocation] = None


# This class is the input for the 'create_world_generation_job' function.
class CreateWorldGenerationJobRequest(BaseValidatorModel):
    template: str
    worldCount: WorldCount
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    worldTags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_world_generation_job' function.
class CreateWorldGenerationJobResponse(BaseValidatorModel):
    arn: str
    status: WorldGenerationJobStatusType
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCodeType
    clientRequestToken: str
    template: str
    worldCount: WorldCount
    tags: Dict[str, str]
    worldTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class WorldGenerationJobSummary(BaseValidatorModel):
    arn: Optional[str] = None
    template: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[WorldGenerationJobStatusType] = None
    worldCount: Optional[WorldCount] = None
    succeededWorldCount: Optional[int] = None
    failedWorldCount: Optional[int] = None


# This class is the input for the 'create_world_template' function.
class CreateWorldTemplateRequest(BaseValidatorModel):
    clientRequestToken: Optional[str] = None
    name: Optional[str] = None
    templateBody: Optional[str] = None
    templateLocation: Optional[TemplateLocation] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_world_template' function.
class UpdateWorldTemplateRequest(BaseValidatorModel):
    template: str
    name: Optional[str] = None
    templateBody: Optional[str] = None
    templateLocation: Optional[TemplateLocation] = None

DataSourceConfigUnion = Union[DataSourceConfig, DataSourceConfigOutput]


class DataSource(BaseValidatorModel):
    name: Optional[str] = None
    s3Bucket: Optional[str] = None
    s3Keys: Optional[List[S3KeyOutput]] = None
    type: Optional[DataSourceTypeType] = None
    destination: Optional[str] = None


class DeploymentApplicationConfigOutput(BaseValidatorModel):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigOutput


class DeploymentConfig(BaseValidatorModel):
    concurrentDeploymentPercentage: Optional[int] = None
    failureThresholdPercentage: Optional[int] = None
    robotDeploymentTimeoutInSeconds: Optional[int] = None
    downloadConditionFile: Optional[S3Object] = None

DeploymentLaunchConfigUnion = Union[DeploymentLaunchConfig, DeploymentLaunchConfigOutput]


# This class is the output for the 'describe_fleet' function.
class DescribeFleetResponse(BaseValidatorModel):
    name: str
    arn: str
    robots: List[Robot]
    createdAt: datetime
    lastDeploymentStatus: DeploymentStatusType
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_robots' function.
class ListRobotsResponse(BaseValidatorModel):
    robots: List[Robot]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_simulation_jobs' function.
class ListSimulationJobsResponse(BaseValidatorModel):
    simulationJobSummaries: List[SimulationJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FailureSummary(BaseValidatorModel):
    totalFailureCount: Optional[int] = None
    failures: Optional[List[WorldFailure]] = None


# This class is the input for the 'list_deployment_jobs' function.
class ListDeploymentJobsRequest(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_fleets' function.
class ListFleetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_robot_applications' function.
class ListRobotApplicationsRequest(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_robots' function.
class ListRobotsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_simulation_applications' function.
class ListSimulationApplicationsRequest(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_simulation_job_batches' function.
class ListSimulationJobBatchesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_simulation_jobs' function.
class ListSimulationJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_world_export_jobs' function.
class ListWorldExportJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_world_generation_jobs' function.
class ListWorldGenerationJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the input for the 'list_worlds' function.
class ListWorldsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[Filter]] = None


# This class is the output for the 'list_fleets' function.
class ListFleetsResponse(BaseValidatorModel):
    fleetDetails: List[Fleet]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentJobsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRobotApplicationsRequestPaginate(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRobotsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSimulationApplicationsRequestPaginate(BaseValidatorModel):
    versionQualifier: Optional[str] = None
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSimulationJobBatchesRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSimulationJobsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorldExportJobsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorldGenerationJobsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorldTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorldsRequestPaginate(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_simulation_job_batches' function.
class ListSimulationJobBatchesResponse(BaseValidatorModel):
    simulationJobBatchSummaries: List[SimulationJobBatchSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_world_templates' function.
class ListWorldTemplatesResponse(BaseValidatorModel):
    templateSummaries: List[TemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_worlds' function.
class ListWorldsResponse(BaseValidatorModel):
    worldSummaries: List[WorldSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PortForwardingConfigOutput(BaseValidatorModel):
    portMappings: Optional[List[PortMapping]] = None


class PortForwardingConfig(BaseValidatorModel):
    portMappings: Optional[List[PortMapping]] = None


class RobotDeployment(BaseValidatorModel):
    arn: Optional[str] = None
    deploymentStartTime: Optional[datetime] = None
    deploymentFinishTime: Optional[datetime] = None
    status: Optional[RobotStatusType] = None
    progressDetail: Optional[ProgressDetail] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None

VPCConfigUnion = Union[VPCConfig, VPCConfigOutput]


# This class is the output for the 'list_robot_applications' function.
class ListRobotApplicationsResponse(BaseValidatorModel):
    robotApplicationSummaries: List[RobotApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_simulation_applications' function.
class ListSimulationApplicationsResponse(BaseValidatorModel):
    simulationApplicationSummaries: List[SimulationApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_world_export_jobs' function.
class ListWorldExportJobsResponse(BaseValidatorModel):
    worldExportJobSummaries: List[WorldExportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_world_generation_jobs' function.
class ListWorldGenerationJobsResponse(BaseValidatorModel):
    worldGenerationJobSummaries: List[WorldGenerationJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_deployment_job' function.
class CreateDeploymentJobResponse(BaseValidatorModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentApplicationConfigs: List[DeploymentApplicationConfigOutput]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    deploymentConfig: DeploymentConfig
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeploymentJob(BaseValidatorModel):
    arn: Optional[str] = None
    fleet: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    deploymentApplicationConfigs: Optional[List[DeploymentApplicationConfigOutput]] = None
    deploymentConfig: Optional[DeploymentConfig] = None
    failureReason: Optional[str] = None
    failureCode: Optional[DeploymentJobErrorCodeType] = None
    createdAt: Optional[datetime] = None


# This class is the output for the 'sync_deployment_job' function.
class SyncDeploymentJobResponse(BaseValidatorModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfig
    deploymentApplicationConfigs: List[DeploymentApplicationConfigOutput]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class DeploymentApplicationConfig(BaseValidatorModel):
    application: str
    applicationVersion: str
    launchConfig: DeploymentLaunchConfigUnion


class FinishedWorldsSummary(BaseValidatorModel):
    finishedCount: Optional[int] = None
    succeededWorlds: Optional[List[str]] = None
    failureSummary: Optional[FailureSummary] = None


class LaunchConfigOutput(BaseValidatorModel):
    packageName: Optional[str] = None
    launchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None
    portForwardingConfig: Optional[PortForwardingConfigOutput] = None
    streamUI: Optional[bool] = None
    command: Optional[List[str]] = None

PortForwardingConfigUnion = Union[PortForwardingConfig, PortForwardingConfigOutput]


# This class is the output for the 'describe_deployment_job' function.
class DescribeDeploymentJobResponse(BaseValidatorModel):
    arn: str
    fleet: str
    status: DeploymentStatusType
    deploymentConfig: DeploymentConfig
    deploymentApplicationConfigs: List[DeploymentApplicationConfigOutput]
    failureReason: str
    failureCode: DeploymentJobErrorCodeType
    createdAt: datetime
    robotDeploymentSummary: List[RobotDeployment]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_deployment_jobs' function.
class ListDeploymentJobsResponse(BaseValidatorModel):
    deploymentJobs: List[DeploymentJob]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

DeploymentApplicationConfigUnion = Union[DeploymentApplicationConfig, DeploymentApplicationConfigOutput]


# This class is the output for the 'describe_world_generation_job' function.
class DescribeWorldGenerationJobResponse(BaseValidatorModel):
    arn: str
    status: WorldGenerationJobStatusType
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    template: str
    worldCount: WorldCount
    finishedWorldsSummary: FinishedWorldsSummary
    tags: Dict[str, str]
    worldTags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RobotApplicationConfigOutput(BaseValidatorModel):
    application: str
    launchConfig: LaunchConfigOutput
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfiguration]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[Tool]] = None
    useDefaultTools: Optional[bool] = None


class SimulationApplicationConfigOutput(BaseValidatorModel):
    application: str
    launchConfig: LaunchConfigOutput
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfiguration]] = None
    worldConfigs: Optional[List[WorldConfig]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[Tool]] = None
    useDefaultTools: Optional[bool] = None


class LaunchConfig(BaseValidatorModel):
    packageName: Optional[str] = None
    launchFile: Optional[str] = None
    environmentVariables: Optional[Dict[str, str]] = None
    portForwardingConfig: Optional[PortForwardingConfigUnion] = None
    streamUI: Optional[bool] = None
    command: Optional[List[str]] = None


# This class is the input for the 'create_deployment_job' function.
class CreateDeploymentJobRequest(BaseValidatorModel):
    clientRequestToken: str
    fleet: str
    deploymentApplicationConfigs: List[DeploymentApplicationConfigUnion]
    deploymentConfig: Optional[DeploymentConfig] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_simulation_job' function.
class CreateSimulationJobResponse(BaseValidatorModel):
    arn: str
    status: SimulationJobStatusType
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehaviorType
    failureCode: SimulationJobErrorCodeType
    clientRequestToken: str
    outputLocation: OutputLocation
    loggingConfig: LoggingConfig
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List[RobotApplicationConfigOutput]
    simulationApplications: List[SimulationApplicationConfigOutput]
    dataSources: List[DataSource]
    tags: Dict[str, str]
    vpcConfig: VPCConfigResponse
    compute: ComputeResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_simulation_job' function.
class DescribeSimulationJobResponse(BaseValidatorModel):
    arn: str
    name: str
    status: SimulationJobStatusType
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehaviorType
    failureCode: SimulationJobErrorCodeType
    failureReason: str
    clientRequestToken: str
    outputLocation: OutputLocation
    loggingConfig: LoggingConfig
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List[RobotApplicationConfigOutput]
    simulationApplications: List[SimulationApplicationConfigOutput]
    dataSources: List[DataSource]
    tags: Dict[str, str]
    vpcConfig: VPCConfigResponse
    networkInterface: NetworkInterface
    compute: ComputeResponse
    ResponseMetadata: ResponseMetadata


class SimulationJobRequestOutput(BaseValidatorModel):
    maxJobDurationInSeconds: int
    outputLocation: Optional[OutputLocation] = None
    loggingConfig: Optional[LoggingConfig] = None
    iamRole: Optional[str] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    useDefaultApplications: Optional[bool] = None
    robotApplications: Optional[List[RobotApplicationConfigOutput]] = None
    simulationApplications: Optional[List[SimulationApplicationConfigOutput]] = None
    dataSources: Optional[List[DataSourceConfigOutput]] = None
    vpcConfig: Optional[VPCConfigOutput] = None
    compute: Optional[Compute] = None
    tags: Optional[Dict[str, str]] = None


class SimulationJob(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    status: Optional[SimulationJobStatusType] = None
    lastStartedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    failureCode: Optional[SimulationJobErrorCodeType] = None
    failureReason: Optional[str] = None
    clientRequestToken: Optional[str] = None
    outputLocation: Optional[OutputLocation] = None
    loggingConfig: Optional[LoggingConfig] = None
    maxJobDurationInSeconds: Optional[int] = None
    simulationTimeMillis: Optional[int] = None
    iamRole: Optional[str] = None
    robotApplications: Optional[List[RobotApplicationConfigOutput]] = None
    simulationApplications: Optional[List[SimulationApplicationConfigOutput]] = None
    dataSources: Optional[List[DataSource]] = None
    tags: Optional[Dict[str, str]] = None
    vpcConfig: Optional[VPCConfigResponse] = None
    networkInterface: Optional[NetworkInterface] = None
    compute: Optional[ComputeResponse] = None

LaunchConfigUnion = Union[LaunchConfig, LaunchConfigOutput]


class FailedCreateSimulationJobRequest(BaseValidatorModel):
    request: Optional[SimulationJobRequestOutput] = None
    failureReason: Optional[str] = None
    failureCode: Optional[SimulationJobErrorCodeType] = None
    failedAt: Optional[datetime] = None


# This class is the output for the 'batch_describe_simulation_job' function.
class BatchDescribeSimulationJobResponse(BaseValidatorModel):
    jobs: List[SimulationJob]
    unprocessedJobs: List[str]
    ResponseMetadata: ResponseMetadata


class RobotApplicationConfig(BaseValidatorModel):
    application: str
    launchConfig: LaunchConfigUnion
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfiguration]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[Tool]] = None
    useDefaultTools: Optional[bool] = None


class SimulationApplicationConfig(BaseValidatorModel):
    application: str
    launchConfig: LaunchConfigUnion
    applicationVersion: Optional[str] = None
    uploadConfigurations: Optional[List[UploadConfiguration]] = None
    worldConfigs: Optional[List[WorldConfig]] = None
    useDefaultUploadConfigurations: Optional[bool] = None
    tools: Optional[List[Tool]] = None
    useDefaultTools: Optional[bool] = None


# This class is the output for the 'describe_simulation_job_batch' function.
class DescribeSimulationJobBatchResponse(BaseValidatorModel):
    arn: str
    status: SimulationJobBatchStatusType
    lastUpdatedAt: datetime
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: BatchPolicy
    failureCode: Literal['InternalServiceError']
    failureReason: str
    failedRequests: List[FailedCreateSimulationJobRequest]
    pendingRequests: List[SimulationJobRequestOutput]
    createdRequests: List[SimulationJobSummary]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_simulation_job_batch' function.
class StartSimulationJobBatchResponse(BaseValidatorModel):
    arn: str
    status: SimulationJobBatchStatusType
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: BatchPolicy
    failureCode: Literal['InternalServiceError']
    failureReason: str
    failedRequests: List[FailedCreateSimulationJobRequest]
    pendingRequests: List[SimulationJobRequestOutput]
    createdRequests: List[SimulationJobSummary]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

RobotApplicationConfigUnion = Union[RobotApplicationConfig, RobotApplicationConfigOutput]

SimulationApplicationConfigUnion = Union[SimulationApplicationConfig, SimulationApplicationConfigOutput]


# This class is the input for the 'create_simulation_job' function.
class CreateSimulationJobRequest(BaseValidatorModel):
    maxJobDurationInSeconds: int
    iamRole: str
    clientRequestToken: Optional[str] = None
    outputLocation: Optional[OutputLocation] = None
    loggingConfig: Optional[LoggingConfig] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    robotApplications: Optional[List[RobotApplicationConfigUnion]] = None
    simulationApplications: Optional[List[SimulationApplicationConfigUnion]] = None
    dataSources: Optional[List[DataSourceConfigUnion]] = None
    tags: Optional[Dict[str, str]] = None
    vpcConfig: Optional[VPCConfigUnion] = None
    compute: Optional[Compute] = None


class SimulationJobRequest(BaseValidatorModel):
    maxJobDurationInSeconds: int
    outputLocation: Optional[OutputLocation] = None
    loggingConfig: Optional[LoggingConfig] = None
    iamRole: Optional[str] = None
    failureBehavior: Optional[FailureBehaviorType] = None
    useDefaultApplications: Optional[bool] = None
    robotApplications: Optional[List[RobotApplicationConfigUnion]] = None
    simulationApplications: Optional[List[SimulationApplicationConfigUnion]] = None
    dataSources: Optional[List[DataSourceConfigUnion]] = None
    vpcConfig: Optional[VPCConfigUnion] = None
    compute: Optional[Compute] = None
    tags: Optional[Dict[str, str]] = None

SimulationJobRequestUnion = Union[SimulationJobRequest, SimulationJobRequestOutput]


# This class is the input for the 'start_simulation_job_batch' function.
class StartSimulationJobBatchRequest(BaseValidatorModel):
    createSimulationJobRequests: List[SimulationJobRequestUnion]
    clientRequestToken: Optional[str] = None
    batchPolicy: Optional[BatchPolicy] = None
    tags: Optional[Dict[str, str]] = None