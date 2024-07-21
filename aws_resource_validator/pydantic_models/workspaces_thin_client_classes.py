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
from aws_resource_validator.pydantic_models.workspaces_thin_client_constants import *

class MaintenanceWindowTypeDef(BaseModel):
    type: Optional[MaintenanceWindowTypeType] = None
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[Sequence[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteDeviceRequestRequestTypeDef(BaseModel):
    id: str
    clientToken: Optional[str] = None

class DeleteEnvironmentRequestRequestTypeDef(BaseModel):
    id: str
    clientToken: Optional[str] = None

class DeregisterDeviceRequestRequestTypeDef(BaseModel):
    id: str
    targetDeviceStatus: Optional[TargetDeviceStatusType] = None
    clientToken: Optional[str] = None

class DeviceSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    serialNumber: Optional[str] = None
    name: Optional[str] = None
    model: Optional[str] = None
    environmentId: Optional[str] = None
    status: Optional[DeviceStatusType] = None
    currentSoftwareSetId: Optional[str] = None
    desiredSoftwareSetId: Optional[str] = None
    pendingSoftwareSetId: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    lastConnectedAt: Optional[datetime] = None
    lastPostureAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    arn: Optional[str] = None

class DeviceTypeDef(BaseModel):
    id: Optional[str] = None
    serialNumber: Optional[str] = None
    name: Optional[str] = None
    model: Optional[str] = None
    environmentId: Optional[str] = None
    status: Optional[DeviceStatusType] = None
    currentSoftwareSetId: Optional[str] = None
    currentSoftwareSetVersion: Optional[str] = None
    desiredSoftwareSetId: Optional[str] = None
    pendingSoftwareSetId: Optional[str] = None
    pendingSoftwareSetVersion: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    softwareSetComplianceStatus: Optional[DeviceSoftwareSetComplianceStatusType] = None
    softwareSetUpdateStatus: Optional[SoftwareSetUpdateStatusType] = None
    lastConnectedAt: Optional[datetime] = None
    lastPostureAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    arn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class MaintenanceWindowOutputTypeDef(BaseModel):
    type: Optional[MaintenanceWindowTypeType] = None
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[List[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None

class GetDeviceRequestRequestTypeDef(BaseModel):
    id: str

class GetEnvironmentRequestRequestTypeDef(BaseModel):
    id: str

class GetSoftwareSetRequestRequestTypeDef(BaseModel):
    id: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDevicesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEnvironmentsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSoftwareSetsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SoftwareSetSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    version: Optional[str] = None
    releasedAt: Optional[datetime] = None
    supportedUntil: Optional[datetime] = None
    validationStatus: Optional[SoftwareSetValidationStatusType] = None
    arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MaintenanceWindowExtraOutputTypeDef(BaseModel):
    type: Optional[MaintenanceWindowTypeType] = None
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[List[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None

class SoftwareTypeDef(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDeviceRequestRequestTypeDef(BaseModel):
    id: str
    name: Optional[str] = None
    desiredSoftwareSetId: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None

class UpdateSoftwareSetRequestRequestTypeDef(BaseModel):
    id: str
    validationStatus: SoftwareSetValidationStatusType

class CreateEnvironmentRequestRequestTypeDef(BaseModel):
    desktopArn: str
    name: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowTypeDef] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    deviceCreationTags: Optional[Mapping[str, str]] = None

class UpdateEnvironmentRequestRequestTypeDef(BaseModel):
    id: str
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowTypeDef] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    deviceCreationTags: Optional[Mapping[str, str]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseModel):
    devices: List[DeviceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceResponseTypeDef(BaseModel):
    device: DeviceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceResponseTypeDef(BaseModel):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    desktopType: Optional[DesktopTypeType] = None
    activationCode: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowOutputTypeDef] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    pendingSoftwareSetId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    arn: Optional[str] = None

class EnvironmentTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    desktopType: Optional[DesktopTypeType] = None
    activationCode: Optional[str] = None
    registeredDevicesCount: Optional[int] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowOutputTypeDef] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    pendingSoftwareSetId: Optional[str] = None
    pendingSoftwareSetVersion: Optional[str] = None
    softwareSetComplianceStatus: Optional[EnvironmentSoftwareSetComplianceStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    arn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    deviceCreationTags: Optional[Dict[str, str]] = None

class ListDevicesRequestListDevicesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSoftwareSetsRequestListSoftwareSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSoftwareSetsResponseTypeDef(BaseModel):
    softwareSets: List[SoftwareSetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SoftwareSetTypeDef(BaseModel):
    id: Optional[str] = None
    version: Optional[str] = None
    releasedAt: Optional[datetime] = None
    supportedUntil: Optional[datetime] = None
    validationStatus: Optional[SoftwareSetValidationStatusType] = None
    software: Optional[List[SoftwareTypeDef]] = None
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateEnvironmentResponseTypeDef(BaseModel):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(BaseModel):
    environments: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(BaseModel):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentResponseTypeDef(BaseModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSoftwareSetResponseTypeDef(BaseModel):
    softwareSet: SoftwareSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

