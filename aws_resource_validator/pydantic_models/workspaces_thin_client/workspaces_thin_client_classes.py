from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workspaces_thin_client.workspaces_thin_client_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteDeviceRequest(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None


class DeleteEnvironmentRequest(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None


class DeregisterDeviceRequest(BaseValidatorModel):
    id: str
    targetDeviceStatus: Optional[TargetDeviceStatusType] = None
    clientToken: Optional[str] = None


class DeviceSummary(BaseValidatorModel):
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


class Device(BaseValidatorModel):
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


class MaintenanceWindowOutput(BaseValidatorModel):
    type: MaintenanceWindowTypeType
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[List[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None


class GetDeviceRequest(BaseValidatorModel):
    id: str


class GetEnvironmentRequest(BaseValidatorModel):
    id: str


class GetSoftwareSetRequest(BaseValidatorModel):
    id: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDevicesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEnvironmentsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSoftwareSetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SoftwareSetSummary(BaseValidatorModel):
    id: Optional[str] = None
    version: Optional[str] = None
    releasedAt: Optional[datetime] = None
    supportedUntil: Optional[datetime] = None
    validationStatus: Optional[SoftwareSetValidationStatusType] = None
    arn: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class MaintenanceWindow(BaseValidatorModel):
    type: MaintenanceWindowTypeType
    startTimeHour: Optional[int] = None
    startTimeMinute: Optional[int] = None
    endTimeHour: Optional[int] = None
    endTimeMinute: Optional[int] = None
    daysOfTheWeek: Optional[List[DayOfWeekType]] = None
    applyTimeOf: Optional[ApplyTimeOfType] = None


class Software(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateDeviceRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    desiredSoftwareSetId: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None


class UpdateSoftwareSetRequest(BaseValidatorModel):
    id: str
    validationStatus: SoftwareSetValidationStatusType


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListDevicesResponse(BaseValidatorModel):
    devices: List[DeviceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDeviceResponse(BaseValidatorModel):
    device: DeviceSummary
    ResponseMetadata: ResponseMetadata


class GetDeviceResponse(BaseValidatorModel):
    device: Device
    ResponseMetadata: ResponseMetadata


class EnvironmentSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    desktopType: Optional[DesktopTypeType] = None
    activationCode: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowOutput] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    pendingSoftwareSetId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    arn: Optional[str] = None


class Environment(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    desktopType: Optional[DesktopTypeType] = None
    activationCode: Optional[str] = None
    registeredDevicesCount: Optional[int] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowOutput] = None
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


class ListDevicesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSoftwareSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSoftwareSetsResponse(BaseValidatorModel):
    softwareSets: List[SoftwareSetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

MaintenanceWindowUnion = Union[MaintenanceWindow, MaintenanceWindowOutput]


class SoftwareSet(BaseValidatorModel):
    id: Optional[str] = None
    version: Optional[str] = None
    releasedAt: Optional[datetime] = None
    supportedUntil: Optional[datetime] = None
    validationStatus: Optional[SoftwareSetValidationStatusType] = None
    software: Optional[List[Software]] = None
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateEnvironmentResponse(BaseValidatorModel):
    environment: EnvironmentSummary
    ResponseMetadata: ResponseMetadata


class ListEnvironmentsResponse(BaseValidatorModel):
    environments: List[EnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateEnvironmentResponse(BaseValidatorModel):
    environment: EnvironmentSummary
    ResponseMetadata: ResponseMetadata


class GetEnvironmentResponse(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class CreateEnvironmentRequest(BaseValidatorModel):
    desktopArn: str
    name: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowUnion] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    deviceCreationTags: Optional[Dict[str, str]] = None


class UpdateEnvironmentRequest(BaseValidatorModel):
    id: str
    name: Optional[str] = None
    desktopArn: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowUnion] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    deviceCreationTags: Optional[Dict[str, str]] = None


class GetSoftwareSetResponse(BaseValidatorModel):
    softwareSet: SoftwareSet
    ResponseMetadata: ResponseMetadata