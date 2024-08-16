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
from aws_resource_validator.pydantic_models.workspaces_thin_client_constants import *

class MaintenanceWindowTypeDef(BaseValidatorModel):
    type: Optional[MaintenanceWindowTypeType] = None
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[Sequence[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteDeviceRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None

class DeleteEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None

class DeregisterDeviceRequestRequestTypeDef(BaseValidatorModel):
    id: str
    targetDeviceStatus: Optional[TargetDeviceStatusType] = None
    clientToken: Optional[str] = None

class DeviceSummaryTypeDef(BaseValidatorModel):
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

class DeviceTypeDef(BaseValidatorModel):
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

class MaintenanceWindowOutputTypeDef(BaseValidatorModel):
    type: Optional[MaintenanceWindowTypeType] = None
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[List[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None

class GetDeviceRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetSoftwareSetRequestRequestTypeDef(BaseValidatorModel):
    id: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEnvironmentsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSoftwareSetsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SoftwareSetSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    version: Optional[str] = None
    releasedAt: Optional[datetime] = None
    supportedUntil: Optional[datetime] = None
    validationStatus: Optional[SoftwareSetValidationStatusType] = None
    arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MaintenanceWindowExtraOutputTypeDef(BaseValidatorModel):
    type: Optional[MaintenanceWindowTypeType] = None
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[List[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None

class SoftwareTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDeviceRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    desiredSoftwareSetId: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None

class UpdateSoftwareSetRequestRequestTypeDef(BaseValidatorModel):
    id: str
    validationStatus: SoftwareSetValidationStatusType

class CreateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateEnvironmentRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowTypeDef] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    deviceCreationTags: Optional[Mapping[str, str]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicesResponseTypeDef(BaseValidatorModel):
    devices: List[DeviceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceResponseTypeDef(BaseValidatorModel):
    device: DeviceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceResponseTypeDef(BaseValidatorModel):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentSummaryTypeDef(BaseValidatorModel):
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

class EnvironmentTypeDef(BaseValidatorModel):
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

class ListDevicesRequestListDevicesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsRequestListEnvironmentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSoftwareSetsRequestListSoftwareSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSoftwareSetsResponseTypeDef(BaseValidatorModel):
    softwareSets: List[SoftwareSetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SoftwareSetTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    version: Optional[str] = None
    releasedAt: Optional[datetime] = None
    supportedUntil: Optional[datetime] = None
    validationStatus: Optional[SoftwareSetValidationStatusType] = None
    software: Optional[List[SoftwareTypeDef]] = None
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSoftwareSetResponseTypeDef(BaseValidatorModel):
    softwareSet: SoftwareSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

