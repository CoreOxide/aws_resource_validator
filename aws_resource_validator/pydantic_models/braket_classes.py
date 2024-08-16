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
from aws_resource_validator.pydantic_models.braket_constants import *

class ContainerImageTypeDef(BaseValidatorModel):
    uri: str

class ScriptModeConfigTypeDef(BaseValidatorModel):
    entryPoint: str
    s3Uri: str
    compressionType: Optional[CompressionTypeType] = None

class AssociationTypeDef(BaseValidatorModel):
    arn: str
    type: Literal["RESERVATION_TIME_WINDOW_ARN"]

class CancelJobRequestRequestTypeDef(BaseValidatorModel):
    jobArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CancelQuantumTaskRequestRequestTypeDef(BaseValidatorModel):
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

class GetDeviceRequestRequestTypeDef(BaseValidatorModel):
    deviceArn: str

class GetJobRequestRequestTypeDef(BaseValidatorModel):
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

class GetQuantumTaskRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class SearchJobsFilterTypeDef(BaseValidatorModel):
    name: str
    operator: SearchJobsFilterOperatorType
    values: Sequence[str]

class SearchQuantumTasksFilterTypeDef(BaseValidatorModel):
    name: str
    operator: SearchQuantumTasksFilterOperatorType
    values: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AlgorithmSpecificationTypeDef(BaseValidatorModel):
    containerImage: Optional[ContainerImageTypeDef] = None
    scriptModeConfig: Optional[ScriptModeConfigTypeDef] = None

class CreateQuantumTaskRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuantumTasksResponseTypeDef(BaseValidatorModel):
    nextToken: str
    quantumTasks: List[QuantumTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchDevicesRequestRequestTypeDef(BaseValidatorModel):
    filters: Sequence[SearchDevicesFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchDevicesRequestSearchDevicesPaginateTypeDef(BaseValidatorModel):
    filters: Sequence[SearchDevicesFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchJobsRequestRequestTypeDef(BaseValidatorModel):
    filters: Sequence[SearchJobsFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchJobsRequestSearchJobsPaginateTypeDef(BaseValidatorModel):
    filters: Sequence[SearchJobsFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchQuantumTasksRequestRequestTypeDef(BaseValidatorModel):
    filters: Sequence[SearchQuantumTasksFilterTypeDef]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef(BaseValidatorModel):
    filters: Sequence[SearchQuantumTasksFilterTypeDef]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class InputFileConfigTypeDef(BaseValidatorModel):
    channelName: str
    dataSource: DataSourceTypeDef
    contentType: Optional[str] = None

class CreateJobRequestRequestTypeDef(BaseValidatorModel):
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

