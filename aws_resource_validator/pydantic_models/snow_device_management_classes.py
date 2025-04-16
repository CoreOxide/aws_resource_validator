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
from aws_resource_validator.pydantic_models.snow_device_management_constants import *

class CancelTaskInput(BaseValidatorModel):
    taskId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Capacity(BaseValidatorModel):
    available: Optional[int] = None
    name: Optional[str] = None
    total: Optional[int] = None
    unit: Optional[str] = None
    used: Optional[int] = None


class Command(BaseValidatorModel):
    reboot: Optional[Mapping[str, Any]] = None
    unlock: Optional[Mapping[str, Any]] = None


class CpuOptions(BaseValidatorModel):
    coreCount: Optional[int] = None
    threadsPerCore: Optional[int] = None


class DescribeDeviceEc2Input(BaseValidatorModel):
    instanceIds: Sequence[str]
    managedDeviceId: str


class DescribeDeviceInput(BaseValidatorModel):
    managedDeviceId: str


class PhysicalNetworkInterface(BaseValidatorModel):
    defaultGateway: Optional[str] = None
    ipAddress: Optional[str] = None
    ipAddressAssignment: Optional[IpAddressAssignmentType] = None
    macAddress: Optional[str] = None
    netmask: Optional[str] = None
    physicalConnectorType: Optional[PhysicalConnectorTypeType] = None
    physicalNetworkInterfaceId: Optional[str] = None


class SoftwareInformation(BaseValidatorModel):
    installState: Optional[str] = None
    installedVersion: Optional[str] = None
    installingVersion: Optional[str] = None


class DescribeExecutionInput(BaseValidatorModel):
    managedDeviceId: str
    taskId: str


class DescribeTaskInput(BaseValidatorModel):
    taskId: str


class DeviceSummary(BaseValidatorModel):
    associatedWithJob: Optional[str] = None
    managedDeviceArn: Optional[str] = None
    managedDeviceId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class EbsInstanceBlockDevice(BaseValidatorModel):
    attachTime: Optional[datetime] = None
    deleteOnTermination: Optional[bool] = None
    status: Optional[AttachmentStatusType] = None
    volumeId: Optional[str] = None


class ExecutionSummary(BaseValidatorModel):
    executionId: Optional[str] = None
    managedDeviceId: Optional[str] = None
    state: Optional[ExecutionStateType] = None
    taskId: Optional[str] = None


class InstanceState(BaseValidatorModel):
    code: Optional[int] = None
    name: Optional[InstanceStateNameType] = None


class SecurityGroupIdentifier(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDevicesInput(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExecutionsInput(BaseValidatorModel):
    taskId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    state: Optional[ExecutionStateType] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class ListTasksInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    state: Optional[TaskStateType] = None


class TaskSummary(BaseValidatorModel):
    taskId: str
    state: Optional[TaskStateType] = None
    tags: Optional[Dict[str, str]] = None
    taskArn: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class CancelTaskOutput(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


class CreateTaskOutput(BaseValidatorModel):
    taskArn: str
    taskId: str
    ResponseMetadata: ResponseMetadata


class DescribeExecutionOutput(BaseValidatorModel):
    executionId: str
    lastUpdatedAt: datetime
    managedDeviceId: str
    startedAt: datetime
    state: ExecutionStateType
    taskId: str
    ResponseMetadata: ResponseMetadata


class DescribeTaskOutput(BaseValidatorModel):
    completedAt: datetime
    createdAt: datetime
    description: str
    lastUpdatedAt: datetime
    state: TaskStateType
    tags: Dict[str, str]
    targets: List[str]
    taskArn: str
    taskId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateTaskInput(BaseValidatorModel):
    command: Command
    targets: Sequence[str]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeDeviceOutput(BaseValidatorModel):
    associatedWithJob: str
    deviceCapacities: List[Capacity]
    deviceState: UnlockStateType
    deviceType: str
    lastReachedOutAt: datetime
    lastUpdatedAt: datetime
    managedDeviceArn: str
    managedDeviceId: str
    physicalNetworkInterfaces: List[PhysicalNetworkInterface]
    software: SoftwareInformation
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListDevicesOutput(BaseValidatorModel):
    devices: List[DeviceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InstanceBlockDeviceMapping(BaseValidatorModel):
    deviceName: Optional[str] = None
    ebs: Optional[EbsInstanceBlockDevice] = None


class ListExecutionsOutput(BaseValidatorModel):
    executions: List[ExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDevicesInputPaginate(BaseValidatorModel):
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExecutionsInputPaginate(BaseValidatorModel):
    taskId: str
    state: Optional[ExecutionStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTasksInputPaginate(BaseValidatorModel):
    state: Optional[TaskStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ResourceSummary(BaseValidatorModel):
    pass


class ListDeviceResourcesOutput(BaseValidatorModel):
    resources: List[ResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTasksOutput(BaseValidatorModel):
    tasks: List[TaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Instance(BaseValidatorModel):
    amiLaunchIndex: Optional[int] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMapping]] = None
    cpuOptions: Optional[CpuOptions] = None
    createdAt: Optional[datetime] = None
    imageId: Optional[str] = None
    instanceId: Optional[str] = None
    instanceType: Optional[str] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None
    rootDeviceName: Optional[str] = None
    securityGroups: Optional[List[SecurityGroupIdentifier]] = None
    state: Optional[InstanceState] = None
    updatedAt: Optional[datetime] = None


class InstanceSummary(BaseValidatorModel):
    instance: Optional[Instance] = None
    lastUpdatedAt: Optional[datetime] = None


class DescribeDeviceEc2Output(BaseValidatorModel):
    instances: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata


