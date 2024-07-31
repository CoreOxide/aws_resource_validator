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
from aws_resource_validator.pydantic_models.braket_constants import *

class ContainerImageTypeDef(BaseModel):
    uri: str

class ScriptModeConfigTypeDef(BaseModel):
    entryPoint: str
    s3Uri: str
    compressionType: Optional[CompressionTypeType] = None

class AssociationTypeDef(BaseModel):
    arn: str
    type: Literal["RESERVATION_TIME_WINDOW_ARN"]

class CancelJobRequestRequestTypeDef(BaseModel):
    jobArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelQuantumTaskRequestRequestTypeDef(BaseModel):
    clientToken: str
    quantumTaskArn: str

class DeviceConfigTypeDef(BaseModel):
    device: str

class InstanceConfigTypeDef(BaseModel):
    instanceType: InstanceTypeType
    volumeSizeInGb: int
    instanceCount: Optional[int] = None

class JobCheckpointConfigTypeDef(BaseModel):
    s3Uri: str
    localPath: Optional[str] = None

class JobOutputDataConfigTypeDef(BaseModel):
    s3Path: str
    kmsKeyId: Optional[str] = None

class JobStoppingConditionTypeDef(BaseModel):
    maxRuntimeInSeconds: Optional[int] = None

class S3DataSourceTypeDef(BaseModel):
    s3Uri: str

class DeviceQueueInfoTypeDef(BaseModel):
    queue: QueueNameType
    queueSize: str
    queuePriority: Optional[QueuePriorityType] = None

class DeviceSummaryTypeDef(BaseModel):
    deviceArn: str
    deviceName: str
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str

class GetDeviceRequestRequestTypeDef(BaseModel):
    deviceArn: str

class GetJobRequestRequestTypeDef(BaseModel):
    jobArn: str
    additionalAttributeNames: Optional[Sequence[Literal["QueueInfo"]]] = None

class HybridJobQueueInfoTypeDef(BaseModel):
    position: str
    queue: QueueNameType
    message: Optional[str] = None

class JobEventDetailsTypeDef(BaseModel):
    eventType: Optional[JobEventTypeType] = None
    message: Optional[str] = None
    timeOfEvent: Optional[datetime] = None

class GetQuantumTaskRequestRequestTypeDef(BaseModel):
    quantumTaskArn: str
    additionalAttributeNames: Optional[Sequence[Literal["QueueInfo"]]] = None

class QuantumTaskQueueInfoTypeDef(BaseModel):
    position: str
    queue: QueueNameType
    message: Optional[str] = None
    queuePriority: Optional[QueuePriorityType] = None

class JobSummaryTypeDef(BaseModel):
    createdAt: datetime
    device: str
    jobArn: str
    jobName: str
    status: JobPrimaryStatusType
    endedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class QuantumTaskSummaryTypeDef(BaseModel):
    createdAt: datetime
    deviceArn: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    shots: int
    status: QuantumTaskStatusType
    endedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class SearchDevicesFilterTypeDef(BaseModel):
    name: str
    values: Sequence[str]

class SearchJobsFilterTypeDef(BaseModel):
    name: str
    operator: SearchJobsFilterOperatorType
    values: Sequence[str]

class SearchQuantumTasksFilterTypeDef(BaseModel):
    name: str
    operator: SearchQuantumTasksFilterOperatorType
    values: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AlgorithmSpecificationTypeDef(BaseModel):
    containerImage: Optional[ContainerImageTypeDef] = None
    scriptModeConfig: Optional[ScriptModeConfigTypeDef] = None

class CreateQuantumTaskRequestRequestTypeDef(BaseModel):
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

class CancelJobResponseTypeDef(BaseModel):
    cancellationStatus: CancellationStatusType
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelQuantumTaskResponseTypeDef(BaseModel):
    cancellationStatus: CancellationStatusType
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResponseTypeDef(BaseModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuantumTaskResponseTypeDef(BaseModel):
    quantumTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceTypeDef(BaseModel):
    s3DataSource: S3DataSourceTypeDef

class GetDeviceResponseTypeDef(BaseModel):
    deviceArn: str
    deviceCapabilities: str
    deviceName: str
    deviceQueueInfo: List[DeviceQueueInfoTypeDef]
    deviceStatus: DeviceStatusType
    deviceType: DeviceTypeType
    providerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchDevicesResponseTypeDef(BaseModel):
    devices: List[DeviceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQuantumTaskResponseTypeDef(BaseModel):
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

class SearchJobsResponseTypeDef(BaseModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuantumTasksResponseTypeDef(BaseModel):
    nextToken: str
    quantumTasks: List[QuantumTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchDevicesRequestRequestTypeDef(BaseModel):
    filters: Sequence[SearchDevicesFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchDevicesRequestSearchDevicesPaginateTypeDef(BaseModel):
    filters: Sequence[SearchDevicesFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchJobsRequestRequestTypeDef(BaseModel):
    filters: Sequence[SearchJobsFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchJobsRequestSearchJobsPaginateTypeDef(BaseModel):
    filters: Sequence[SearchJobsFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchQuantumTasksRequestRequestTypeDef(BaseModel):
    filters: Sequence[SearchQuantumTasksFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef(BaseModel):
    filters: Sequence[SearchQuantumTasksFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class InputFileConfigTypeDef(BaseModel):
    channelName: str
    dataSource: DataSourceTypeDef
    contentType: Optional[str] = None

class CreateJobRequestRequestTypeDef(BaseModel):
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

class GetJobResponseTypeDef(BaseModel):
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

