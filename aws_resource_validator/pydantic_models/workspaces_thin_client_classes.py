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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDevicesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEnvironmentsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSoftwareSetsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class SoftwareTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DeviceSummaryTypeDef(BaseValidatorModel):
    pass


class ListDevicesResponseTypeDef(BaseValidatorModel):
    devices: List[DeviceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDeviceResponseTypeDef(BaseValidatorModel):
    device: DeviceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeviceTypeDef(BaseValidatorModel):
    pass


class GetDeviceResponseTypeDef(BaseValidatorModel):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDevicesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSoftwareSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SoftwareSetSummaryTypeDef(BaseValidatorModel):
    pass


class ListSoftwareSetsResponseTypeDef(BaseValidatorModel):
    softwareSets: List[SoftwareSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EnvironmentSummaryTypeDef(BaseValidatorModel):
    pass


class CreateEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEnvironmentsResponseTypeDef(BaseValidatorModel):
    environments: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnvironmentTypeDef(BaseValidatorModel):
    pass


class GetEnvironmentResponseTypeDef(BaseValidatorModel):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MaintenanceWindowUnionTypeDef(BaseValidatorModel):
    pass


class CreateEnvironmentRequestTypeDef(BaseValidatorModel):
    desktopArn: str
    name: Optional[str] = None
    desktopEndpoint: Optional[str] = None
    softwareSetUpdateSchedule: Optional[SoftwareSetUpdateScheduleType] = None
    maintenanceWindow: Optional[MaintenanceWindowUnionTypeDef] = None
    softwareSetUpdateMode: Optional[SoftwareSetUpdateModeType] = None
    desiredSoftwareSetId: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    deviceCreationTags: Optional[Mapping[str, str]] = None


class SoftwareSetTypeDef(BaseValidatorModel):
    pass


class GetSoftwareSetResponseTypeDef(BaseValidatorModel):
    softwareSet: SoftwareSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


