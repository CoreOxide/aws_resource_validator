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
from aws_resource_validator.pydantic_models.snow_device_management_constants import *

class CancelTaskInputRequestTypeDef(BaseValidatorModel):
    taskId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CapacityTypeDef(BaseValidatorModel):
    available: Optional[int] = None
    name: Optional[str] = None
    total: Optional[int] = None
    unit: Optional[str] = None
    used: Optional[int] = None

class CommandTypeDef(BaseValidatorModel):
    reboot: Optional[Mapping[str, Any]] = None
    unlock: Optional[Mapping[str, Any]] = None

class CpuOptionsTypeDef(BaseValidatorModel):
    coreCount: Optional[int] = None
    threadsPerCore: Optional[int] = None

class DescribeDeviceEc2InputRequestTypeDef(BaseValidatorModel):
    instanceIds: Sequence[str]
    managedDeviceId: str

class DescribeDeviceInputRequestTypeDef(BaseValidatorModel):
    managedDeviceId: str

class PhysicalNetworkInterfaceTypeDef(BaseValidatorModel):
    defaultGateway: Optional[str] = None
    ipAddress: Optional[str] = None
    ipAddressAssignment: Optional[IpAddressAssignmentType] = None
    macAddress: Optional[str] = None
    netmask: Optional[str] = None
    physicalConnectorType: Optional[PhysicalConnectorTypeType] = None
    physicalNetworkInterfaceId: Optional[str] = None

class SoftwareInformationTypeDef(BaseValidatorModel):
    installState: Optional[str] = None
    installedVersion: Optional[str] = None
    installingVersion: Optional[str] = None

class DescribeExecutionInputRequestTypeDef(BaseValidatorModel):
    managedDeviceId: str
    taskId: str

class DescribeTaskInputRequestTypeDef(BaseValidatorModel):
    taskId: str

class DeviceSummaryTypeDef(BaseValidatorModel):
    associatedWithJob: Optional[str] = None
    managedDeviceArn: Optional[str] = None
    managedDeviceId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class EbsInstanceBlockDeviceTypeDef(BaseValidatorModel):
    attachTime: Optional[datetime] = None
    deleteOnTermination: Optional[bool] = None
    status: Optional[AttachmentStatusType] = None
    volumeId: Optional[str] = None

class ExecutionSummaryTypeDef(BaseValidatorModel):
    executionId: Optional[str] = None
    managedDeviceId: Optional[str] = None
    state: Optional[ExecutionStateType] = None
    taskId: Optional[str] = None

class InstanceStateTypeDef(BaseValidatorModel):
    code: Optional[int] = None
    name: Optional[InstanceStateNameType] = None

class SecurityGroupIdentifierTypeDef(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDeviceResourcesInputRequestTypeDef(BaseValidatorModel):
    managedDeviceId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    type: Optional[str] = None

class ResourceSummaryTypeDef(BaseValidatorModel):
    resourceType: str
    arn: Optional[str] = None
    id: Optional[str] = None

class ListDevicesInputRequestTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExecutionsInputRequestTypeDef(BaseValidatorModel):
    taskId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    state: Optional[ExecutionStateType] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTasksInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    state: Optional[TaskStateType] = None

class TaskSummaryTypeDef(BaseValidatorModel):
    taskId: str
    state: Optional[TaskStateType] = None
    tags: Optional[Dict[str, str]] = None
    taskArn: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CancelTaskOutputTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskOutputTypeDef(BaseValidatorModel):
    taskArn: str
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExecutionOutputTypeDef(BaseValidatorModel):
    executionId: str
    lastUpdatedAt: datetime
    managedDeviceId: str
    startedAt: datetime
    state: ExecutionStateType
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskOutputTypeDef(BaseValidatorModel):
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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskInputRequestTypeDef(BaseValidatorModel):
    command: CommandTypeDef
    targets: Sequence[str]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DescribeDeviceOutputTypeDef(BaseValidatorModel):
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

class ListDevicesOutputTypeDef(BaseValidatorModel):
    devices: List[DeviceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceBlockDeviceMappingTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    ebs: Optional[EbsInstanceBlockDeviceTypeDef] = None

class ListExecutionsOutputTypeDef(BaseValidatorModel):
    executions: List[ExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceResourcesInputListDeviceResourcesPaginateTypeDef(BaseValidatorModel):
    managedDeviceId: str
    type: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicesInputListDevicesPaginateTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExecutionsInputListExecutionsPaginateTypeDef(BaseValidatorModel):
    taskId: str
    state: Optional[ExecutionStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksInputListTasksPaginateTypeDef(BaseValidatorModel):
    state: Optional[TaskStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceResourcesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    resources: List[ResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTasksOutputTypeDef(BaseValidatorModel):
    nextToken: str
    tasks: List[TaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceTypeDef(BaseValidatorModel):
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

class InstanceSummaryTypeDef(BaseValidatorModel):
    instance: Optional[InstanceTypeDef] = None
    lastUpdatedAt: Optional[datetime] = None

class DescribeDeviceEc2OutputTypeDef(BaseValidatorModel):
    instances: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

