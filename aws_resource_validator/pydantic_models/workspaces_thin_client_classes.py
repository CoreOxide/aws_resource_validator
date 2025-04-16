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
from aws_resource_validator.pydantic_models.workspaces_thin_client_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Software(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DeviceSummary(BaseValidatorModel):
    pass


class ListDevicesResponse(BaseValidatorModel):
    devices: List[DeviceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDeviceResponse(BaseValidatorModel):
    device: DeviceSummary
    ResponseMetadata: ResponseMetadata


class Device(BaseValidatorModel):
    pass


class GetDeviceResponse(BaseValidatorModel):
    device: Device
    ResponseMetadata: ResponseMetadata


class ListDevicesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSoftwareSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class SoftwareSetSummary(BaseValidatorModel):
    pass


class ListSoftwareSetsResponse(BaseValidatorModel):
    softwareSets: List[SoftwareSetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EnvironmentSummary(BaseValidatorModel):
    pass


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


class Environment(BaseValidatorModel):
    pass


class GetEnvironmentResponse(BaseValidatorModel):
    environment: Environment
    ResponseMetadata: ResponseMetadata


class MaintenanceWindowUnion(BaseValidatorModel):
    pass


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
    tags: Optional[Mapping[str, str]] = None
    deviceCreationTags: Optional[Mapping[str, str]] = None


class SoftwareSet(BaseValidatorModel):
    pass


class GetSoftwareSetResponse(BaseValidatorModel):
    softwareSet: SoftwareSet
    ResponseMetadata: ResponseMetadata


