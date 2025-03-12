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
from aws_resource_validator.pydantic_models.braket_constants import *

class ContainerImageTypeDef(BaseValidatorModel):
    uri: str


class ScriptModeConfigTypeDef(BaseValidatorModel):
    entryPoint: str
    s3Uri: str
    compressionType: Optional[CompressionTypeType] = None


class CancelJobRequestTypeDef(BaseValidatorModel):
    jobArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelQuantumTaskRequestTypeDef(BaseValidatorModel):
    clientToken: str
    quantumTaskArn: str


class DeviceConfigTypeDef(BaseValidatorModel):
    device: str


class InstanceConfigTypeDef(BaseValidatorModel):
    instanceType: InstanceTypeType
    volumeSizeInGb: int
    instanceCount: Optional[int] = None


class JobCheckpointConfigTypeDef(BaseValidatorModel):
    s3Uri: str
    localPath: Optional[str] = None


class JobOutputDataConfigTypeDef(BaseValidatorModel):
    s3Path: str
    kmsKeyId: Optional[str] = None


class JobStoppingConditionTypeDef(BaseValidatorModel):
    maxRuntimeInSeconds: Optional[int] = None


class S3DataSourceTypeDef(BaseValidatorModel):
    s3Uri: str


class DeviceQueueInfoTypeDef(BaseValidatorModel):
    queue: QueueNameType
    queueSize: str
    queuePriority: Optional[QueuePriorityType] = None


class DeviceSummaryTypeDef(BaseValidatorModel):
    deviceArn: str
    deviceName: str
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str


class GetDeviceRequestTypeDef(BaseValidatorModel):
    deviceArn: str


class GetJobRequestTypeDef(BaseValidatorModel):
    jobArn: str
    additionalAttributeNames: Optional[Sequence[Literal["QueueInfo"]]] = None


class HybridJobQueueInfoTypeDef(BaseValidatorModel):
    position: str
    queue: QueueNameType
    message: Optional[str] = None


class JobEventDetailsTypeDef(BaseValidatorModel):
    eventType: Optional[JobEventTypeType] = None
    message: Optional[str] = None
    timeOfEvent: Optional[datetime] = None


class GetQuantumTaskRequestTypeDef(BaseValidatorModel):
    quantumTaskArn: str
    additionalAttributeNames: Optional[Sequence[Literal["QueueInfo"]]] = None


class QuantumTaskQueueInfoTypeDef(BaseValidatorModel):
    position: str
    queue: QueueNameType
    message: Optional[str] = None
    queuePriority: Optional[QueuePriorityType] = None


class JobSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    device: str
    jobArn: str
    jobName: str
    status: JobPrimaryStatusType
    endedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class QuantumTaskSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    deviceArn: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    shots: int
    status: QuantumTaskStatusType
    endedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class SearchDevicesFilterTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AlgorithmSpecificationTypeDef(BaseValidatorModel):
    containerImage: Optional[ContainerImageTypeDef] = None
    scriptModeConfig: Optional[ScriptModeConfigTypeDef] = None


class AssociationTypeDef(BaseValidatorModel):
    pass


class CreateQuantumTaskRequestTypeDef(BaseValidatorModel):
    action: str
    clientToken: str
    deviceArn: str
    outputS3Bucket: str
    outputS3KeyPrefix: str
    shots: int
    associations: Optional[Sequence[AssociationTypeDef]] = None
    deviceParameters: Optional[str] = None
    jobToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CancelJobResponseTypeDef(BaseValidatorModel):
    cancellationStatus: CancellationStatusType
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelQuantumTaskResponseTypeDef(BaseValidatorModel):
    cancellationStatus: CancellationStatusType
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateQuantumTaskResponseTypeDef(BaseValidatorModel):
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DataSourceTypeDef(BaseValidatorModel):
    s3DataSource: S3DataSourceTypeDef


class GetDeviceResponseTypeDef(BaseValidatorModel):
    deviceArn: str
    deviceCapabilities: str
    deviceName: str
    deviceQueueInfo: List[DeviceQueueInfoTypeDef]
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchDevicesResponseTypeDef(BaseValidatorModel):
    devices: List[DeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetQuantumTaskResponseTypeDef(BaseValidatorModel):
    associations: List[AssociationTypeDef]
    createdAt: datetime
    deviceArn: str
    deviceParameters: str
    endedAt: datetime
    failureReason: str
    jobArn: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    queueInfo: QuantumTaskQueueInfoTypeDef
    shots: int
    status: QuantumTaskStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchQuantumTasksResponseTypeDef(BaseValidatorModel):
    quantumTasks: List[QuantumTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchDevicesRequestPaginateTypeDef(BaseValidatorModel):
    filters: Sequence[SearchDevicesFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchDevicesRequestTypeDef(BaseValidatorModel):
    filters: Sequence[SearchDevicesFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchJobsFilterTypeDef(BaseValidatorModel):
    pass


class SearchJobsRequestPaginateTypeDef(BaseValidatorModel):
    filters: Sequence[SearchJobsFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchJobsRequestTypeDef(BaseValidatorModel):
    filters: Sequence[SearchJobsFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchQuantumTasksFilterTypeDef(BaseValidatorModel):
    pass


class SearchQuantumTasksRequestPaginateTypeDef(BaseValidatorModel):
    filters: Sequence[SearchQuantumTasksFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchQuantumTasksRequestTypeDef(BaseValidatorModel):
    filters: Sequence[SearchQuantumTasksFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class InputFileConfigTypeDef(BaseValidatorModel):
    channelName: str
    dataSource: DataSourceTypeDef
    contentType: Optional[str] = None


class CreateJobRequestTypeDef(BaseValidatorModel):
    algorithmSpecification: AlgorithmSpecificationTypeDef
    clientToken: str
    deviceConfig: DeviceConfigTypeDef
    instanceConfig: InstanceConfigTypeDef
    jobName: str
    outputDataConfig: JobOutputDataConfigTypeDef
    roleArn: str
    associations: Optional[Sequence[AssociationTypeDef]] = None
    checkpointConfig: Optional[JobCheckpointConfigTypeDef] = None
    hyperParameters: Optional[Mapping[str, str]] = None
    inputDataConfig: Optional[Sequence[InputFileConfigTypeDef]] = None
    stoppingCondition: Optional[JobStoppingConditionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class GetJobResponseTypeDef(BaseValidatorModel):
    algorithmSpecification: AlgorithmSpecificationTypeDef
    associations: List[AssociationTypeDef]
    billableDuration: int
    checkpointConfig: JobCheckpointConfigTypeDef
    createdAt: datetime
    deviceConfig: DeviceConfigTypeDef
    endedAt: datetime
    events: List[JobEventDetailsTypeDef]
    failureReason: str
    hyperParameters: Dict[str, str]
    inputDataConfig: List[InputFileConfigTypeDef]
    instanceConfig: InstanceConfigTypeDef
    jobArn: str
    jobName: str
    outputDataConfig: JobOutputDataConfigTypeDef
    queueInfo: HybridJobQueueInfoTypeDef
    roleArn: str
    startedAt: datetime
    status: JobPrimaryStatusType
    stoppingCondition: JobStoppingConditionTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


