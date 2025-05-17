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


# This class is the input for the 'cancel_job' function.
class CancelJobRequest(BaseValidatorModel):
    jobArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'cancel_quantum_task' function.
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


# This class is the input for the 'get_device' function.
class GetDeviceRequest(BaseValidatorModel):
    deviceArn: str


# This class is the input for the 'get_job' function.
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


# This class is the input for the 'get_quantum_task' function.
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


# This class is the input for the 'list_tags_for_resource' function.
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


# This class is the input for the 'create_quantum_task' function.
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


# This class is the output for the 'cancel_job' function.
class CancelJobResponse(BaseValidatorModel):
    cancellationStatus: CancellationStatusType
    jobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_quantum_task' function.
class CancelQuantumTaskResponse(BaseValidatorModel):
    cancellationStatus: CancellationStatusType
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_job' function.
class CreateJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_quantum_task' function.
class CreateQuantumTaskResponse(BaseValidatorModel):
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DataSource(BaseValidatorModel):
    s3DataSource: S3DataSource


# This class is the output for the 'get_device' function.
class GetDeviceResponse(BaseValidatorModel):
    deviceArn: str
    deviceCapabilities: str
    deviceName: str
    deviceQueueInfo: List[DeviceQueueInfo]
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_devices' function.
class SearchDevicesResponse(BaseValidatorModel):
    devices: List[DeviceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_quantum_task' function.
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


# This class is the output for the 'search_jobs' function.
class SearchJobsResponse(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'search_quantum_tasks' function.
class SearchQuantumTasksResponse(BaseValidatorModel):
    quantumTasks: List[QuantumTaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchDevicesRequestPaginate(BaseValidatorModel):
    filters: List[SearchDevicesFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_devices' function.
class SearchDevicesRequest(BaseValidatorModel):
    filters: List[SearchDevicesFilter]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchJobsRequestPaginate(BaseValidatorModel):
    filters: List[SearchJobsFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_jobs' function.
class SearchJobsRequest(BaseValidatorModel):
    filters: List[SearchJobsFilter]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchQuantumTasksRequestPaginate(BaseValidatorModel):
    filters: List[SearchQuantumTasksFilter]
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_quantum_tasks' function.
class SearchQuantumTasksRequest(BaseValidatorModel):
    filters: List[SearchQuantumTasksFilter]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class InputFileConfig(BaseValidatorModel):
    channelName: str
    dataSource: DataSource
    contentType: Optional[str] = None


# This class is the input for the 'create_job' function.
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


# This class is the output for the 'get_job' function.
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