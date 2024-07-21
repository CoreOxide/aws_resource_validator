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
from aws_resource_validator.pydantic_models.snow_device_management_constants import *

class CancelTaskInputRequestTypeDef(BaseModel):
    taskId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CapacityTypeDef(BaseModel):
    available: Optional[int] = None
    name: Optional[str] = None
    total: Optional[int] = None
    unit: Optional[str] = None
    used: Optional[int] = None

class CommandTypeDef(BaseModel):
    reboot: Optional[Mapping[str, Any]] = None
    unlock: Optional[Mapping[str, Any]] = None

class CpuOptionsTypeDef(BaseModel):
    coreCount: Optional[int] = None
    threadsPerCore: Optional[int] = None

class DescribeDeviceEc2InputRequestTypeDef(BaseModel):
    instanceIds: Sequence[str]
    managedDeviceId: str

class DescribeDeviceInputRequestTypeDef(BaseModel):
    managedDeviceId: str

class PhysicalNetworkInterfaceTypeDef(BaseModel):
    defaultGateway: Optional[str] = None
    ipAddress: Optional[str] = None
    ipAddressAssignment: Optional[IpAddressAssignmentType] = None
    macAddress: Optional[str] = None
    netmask: Optional[str] = None
    physicalConnectorType: Optional[PhysicalConnectorTypeType] = None
    physicalNetworkInterfaceId: Optional[str] = None

class SoftwareInformationTypeDef(BaseModel):
    installState: Optional[str] = None
    installedVersion: Optional[str] = None
    installingVersion: Optional[str] = None

class DescribeExecutionInputRequestTypeDef(BaseModel):
    managedDeviceId: str
    taskId: str

class DescribeTaskInputRequestTypeDef(BaseModel):
    taskId: str

class DeviceSummaryTypeDef(BaseModel):
    associatedWithJob: Optional[str] = None
    managedDeviceArn: Optional[str] = None
    managedDeviceId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class EbsInstanceBlockDeviceTypeDef(BaseModel):
    attachTime: Optional[datetime] = None
    deleteOnTermination: Optional[bool] = None
    status: Optional[AttachmentStatusType] = None
    volumeId: Optional[str] = None

class ExecutionSummaryTypeDef(BaseModel):
    executionId: Optional[str] = None
    managedDeviceId: Optional[str] = None
    state: Optional[ExecutionStateType] = None
    taskId: Optional[str] = None

class InstanceStateTypeDef(BaseModel):
    code: Optional[int] = None
    name: Optional[InstanceStateNameType] = None

class SecurityGroupIdentifierTypeDef(BaseModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeviceResourcesInputRequestTypeDef(BaseModel):
    managedDeviceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    type: Optional[str] = None

class ResourceSummaryTypeDef(BaseModel):
    resourceType: str
    arn: Optional[str] = None
    id: Optional[str] = None

class ListDevicesInputRequestTypeDef(BaseModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExecutionsInputRequestTypeDef(BaseModel):
    taskId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    state: Optional[ExecutionStateType] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class ListTasksInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    state: Optional[TaskStateType] = None

class TaskSummaryTypeDef(BaseModel):
    taskId: str
    state: Optional[TaskStateType] = None
    tags: Optional[Dict[str, str]] = None
    taskArn: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CancelTaskOutputTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskOutputTypeDef(BaseModel):
    taskArn: str
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExecutionOutputTypeDef(BaseModel):
    executionId: str
    lastUpdatedAt: datetime
    managedDeviceId: str
    startedAt: datetime
    state: ExecutionStateType
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskOutputTypeDef(BaseModel):
    completedAt: datetime
    createdAt: datetime
    description: str
    lastUpdatedAt: datetime
    state: TaskStateType
    tags: Dict[str, str]
    targets: List[str]
    taskArn: str
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskInputRequestTypeDef(BaseModel):
    command: CommandTypeDef
    targets: Sequence[str]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DescribeDeviceOutputTypeDef(BaseModel):
    associatedWithJob: str
    deviceCapacities: List[CapacityTypeDef]
    deviceState: UnlockStateType
    deviceType: str
    lastReachedOutAt: datetime
    lastUpdatedAt: datetime
    managedDeviceArn: str
    managedDeviceId: str
    physicalNetworkInterfaces: List[PhysicalNetworkInterfaceTypeDef]
    software: SoftwareInformationTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesOutputTypeDef(BaseModel):
    devices: List[DeviceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceBlockDeviceMappingTypeDef(BaseModel):
    deviceName: Optional[str] = None
    ebs: Optional[EbsInstanceBlockDeviceTypeDef] = None

class ListExecutionsOutputTypeDef(BaseModel):
    executions: List[ExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceResourcesInputListDeviceResourcesPaginateTypeDef(BaseModel):
    managedDeviceId: str
    type: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicesInputListDevicesPaginateTypeDef(BaseModel):
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExecutionsInputListExecutionsPaginateTypeDef(BaseModel):
    taskId: str
    state: Optional[ExecutionStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksInputListTasksPaginateTypeDef(BaseModel):
    state: Optional[TaskStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceResourcesOutputTypeDef(BaseModel):
    nextToken: str
    resources: List[ResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTasksOutputTypeDef(BaseModel):
    nextToken: str
    tasks: List[TaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceTypeDef(BaseModel):
    amiLaunchIndex: Optional[int] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMappingTypeDef]] = None
    cpuOptions: Optional[CpuOptionsTypeDef] = None
    createdAt: Optional[datetime] = None
    imageId: Optional[str] = None
    instanceId: Optional[str] = None
    instanceType: Optional[str] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None
    rootDeviceName: Optional[str] = None
    securityGroups: Optional[List[SecurityGroupIdentifierTypeDef]] = None
    state: Optional[InstanceStateTypeDef] = None
    updatedAt: Optional[datetime] = None

class InstanceSummaryTypeDef(BaseModel):
    instance: Optional[InstanceTypeDef] = None
    lastUpdatedAt: Optional[datetime] = None

class DescribeDeviceEc2OutputTypeDef(BaseModel):
    instances: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

