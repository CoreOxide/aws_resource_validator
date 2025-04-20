from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.braket.braket_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ContainerImage(BaseValidatorModel):
    uri: str


class ScriptModeConfig(BaseValidatorModel):
    entryPoint: str
    s3Uri: str
    compressionType: Optional[CompressionTypeType] = None


class Association(BaseValidatorModel):
    arn: str
    type: Literal['RESERVATION_TIME_WINDOW_ARN']


class CancelJobRequest(BaseValidatorModel):
    jobArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelQuantumTaskRequest(BaseValidatorModel):
    clientToken: str
    quantumTaskArn: str


class DeviceConfig(BaseValidatorModel):
    device: str


class InstanceConfig(BaseValidatorModel):
    instanceType: InstanceTypeType
    volumeSizeInGb: int
    instanceCount: Optional[int] = None


class JobCheckpointConfig(BaseValidatorModel):
    s3Uri: str
    localPath: Optional[str] = None


class JobOutputDataConfig(BaseValidatorModel):
    s3Path: str
    kmsKeyId: Optional[str] = None


class JobStoppingCondition(BaseValidatorModel):
    maxRuntimeInSeconds: Optional[int] = None


class S3DataSource(BaseValidatorModel):
    s3Uri: str


class DeviceQueueInfo(BaseValidatorModel):
    queue: QueueNameType
    queueSize: str
    queuePriority: Optional[QueuePriorityType] = None


class DeviceSummary(BaseValidatorModel):
    deviceArn: str
    deviceName: str
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str


class GetDeviceRequest(BaseValidatorModel):
    deviceArn: str


class GetJobRequest(BaseValidatorModel):
    jobArn: str
    additionalAttributeNames: Optional[List[Literal['QueueInfo']]] = None


class HybridJobQueueInfo(BaseValidatorModel):
    position: str
    queue: QueueNameType
    message: Optional[str] = None


class JobEventDetails(BaseValidatorModel):
    eventType: Optional[JobEventTypeType] = None
    message: Optional[str] = None
    timeOfEvent: Optional[datetime] = None


class GetQuantumTaskRequest(BaseValidatorModel):
    quantumTaskArn: str
    additionalAttributeNames: Optional[List[Literal['QueueInfo']]] = None


class QuantumTaskQueueInfo(BaseValidatorModel):
    position: str
    queue: QueueNameType
    message: Optional[str] = None
    queuePriority: Optional[QueuePriorityType] = None


class JobSummary(BaseValidatorModel):
    createdAt: datetime
    device: str
    jobArn: str
    jobName: str
    status: JobPrimaryStatusType
    endedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class QuantumTaskSummary(BaseValidatorModel):
    createdAt: datetime
    deviceArn: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    shots: int
    status: QuantumTaskStatusType
    endedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class SearchDevicesFilter(BaseValidatorModel):
    name: str
    values: List[str]


class SearchJobsFilter(BaseValidatorModel):
    name: str
    operator: SearchJobsFilterOperatorType
    values: List[str]


class SearchQuantumTasksFilter(BaseValidatorModel):
    name: str
    operator: SearchQuantumTasksFilterOperatorType
    values: List[str]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AlgorithmSpecification(BaseValidatorModel):
    containerImage: Optional[ContainerImage] = None
    scriptModeConfig: Optional[ScriptModeConfig] = None


class CreateQuantumTaskRequest(BaseValidatorModel):
    action: str
    clientToken: str
    deviceArn: str
    outputS3Bucket: str
    outputS3KeyPrefix: str
    shots: int
    associations: Optional[List[Association]] = None
    deviceParameters: Optional[str] = None
    jobToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CancelJobResponse(BaseValidatorModel):
    cancellationStatus: CancellationStatusType
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CancelQuantumTaskResponse(BaseValidatorModel):
    cancellationStatus: CancellationStatusType
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadata


class CreateJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CreateQuantumTaskResponse(BaseValidatorModel):
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DataSource(BaseValidatorModel):
    s3DataSource: S3DataSource


class GetDeviceResponse(BaseValidatorModel):
    deviceArn: str
    deviceCapabilities: str
    deviceName: str
    deviceQueueInfo: List[DeviceQueueInfo]
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str
    ResponseMetadata: ResponseMetadata


class SearchDevicesResponse(BaseValidatorModel):
    devices: List[DeviceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetQuantumTaskResponse(BaseValidatorModel):
    associations: List[Association]
    createdAt: datetime
    deviceArn: str
    deviceParameters: str
    endedAt: datetime
    failureReason: str
    jobArn: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    queueInfo: QuantumTaskQueueInfo
    shots: int
    status: QuantumTaskStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SearchJobsResponse(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchQuantumTasksResponse(BaseValidatorModel):
    quantumTasks: List[QuantumTaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchDevicesRequestPaginate(BaseValidatorModel):
    filters: List[SearchDevicesFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchDevicesRequest(BaseValidatorModel):
    filters: List[SearchDevicesFilter]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchJobsRequestPaginate(BaseValidatorModel):
    filters: List[SearchJobsFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchJobsRequest(BaseValidatorModel):
    filters: List[SearchJobsFilter]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchQuantumTasksRequestPaginate(BaseValidatorModel):
    filters: List[SearchQuantumTasksFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchQuantumTasksRequest(BaseValidatorModel):
    filters: List[SearchQuantumTasksFilter]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class InputFileConfig(BaseValidatorModel):
    channelName: str
    dataSource: DataSource
    contentType: Optional[str] = None


class CreateJobRequest(BaseValidatorModel):
    algorithmSpecification: AlgorithmSpecification
    clientToken: str
    deviceConfig: DeviceConfig
    instanceConfig: InstanceConfig
    jobName: str
    outputDataConfig: JobOutputDataConfig
    roleArn: str
    associations: Optional[List[Association]] = None
    checkpointConfig: Optional[JobCheckpointConfig] = None
    hyperParameters: Optional[Dict[str, str]] = None
    inputDataConfig: Optional[List[InputFileConfig]] = None
    stoppingCondition: Optional[JobStoppingCondition] = None
    tags: Optional[Dict[str, str]] = None


class GetJobResponse(BaseValidatorModel):
    algorithmSpecification: AlgorithmSpecification
    associations: List[Association]
    billableDuration: int
    checkpointConfig: JobCheckpointConfig
    createdAt: datetime
    deviceConfig: DeviceConfig
    endedAt: datetime
    events: List[JobEventDetails]
    failureReason: str
    hyperParameters: Dict[str, str]
    inputDataConfig: List[InputFileConfig]
    instanceConfig: InstanceConfig
    jobArn: str
    jobName: str
    outputDataConfig: JobOutputDataConfig
    queueInfo: HybridJobQueueInfo
    roleArn: str
    startedAt: datetime
    status: JobPrimaryStatusType
    stoppingCondition: JobStoppingCondition
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata