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
from aws_resource_validator.pydantic_models.iot1click_projects_constants import *

class AssociateDeviceWithPlacementRequestRequestTypeDef(BaseValidatorModel):
    projectName: str
    placementName: str
    deviceId: str
    deviceTemplateName: str

class CreatePlacementRequestRequestTypeDef(BaseValidatorModel):
    placementName: str
    projectName: str
    attributes: Optional[Mapping[str, str]] = None

class DeletePlacementRequestRequestTypeDef(BaseValidatorModel):
    placementName: str
    projectName: str

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    projectName: str

class DescribePlacementRequestRequestTypeDef(BaseValidatorModel):
    placementName: str
    projectName: str

class PlacementDescriptionTypeDef(BaseValidatorModel):
    projectName: str
    placementName: str
    attributes: Dict[str, str]
    createdDate: datetime
    updatedDate: datetime

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeProjectRequestRequestTypeDef(BaseValidatorModel):
    projectName: str

class DeviceTemplateTypeDef(BaseValidatorModel):
    deviceType: Optional[str] = None
    callbackOverrides: Optional[Mapping[str, str]] = None

class DisassociateDeviceFromPlacementRequestRequestTypeDef(BaseValidatorModel):
    projectName: str
    placementName: str
    deviceTemplateName: str

class GetDevicesInPlacementRequestRequestTypeDef(BaseValidatorModel):
    projectName: str
    placementName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPlacementsRequestRequestTypeDef(BaseValidatorModel):
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PlacementSummaryTypeDef(BaseValidatorModel):
    projectName: str
    placementName: str
    createdDate: datetime
    updatedDate: datetime

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummaryTypeDef(BaseValidatorModel):
    projectName: str
    createdDate: datetime
    updatedDate: datetime
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePlacementRequestRequestTypeDef(BaseValidatorModel):
    placementName: str
    projectName: str
    attributes: Optional[Mapping[str, str]] = None

class DescribePlacementResponseTypeDef(BaseValidatorModel):
    placement: PlacementDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicesInPlacementResponseTypeDef(BaseValidatorModel):
    devices: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PlacementTemplateTypeDef(BaseValidatorModel):
    defaultAttributes: Optional[Mapping[str, str]] = None
    deviceTemplates: Optional[Mapping[str, DeviceTemplateTypeDef]] = None

class ListPlacementsRequestListPlacementsPaginateTypeDef(BaseValidatorModel):
    projectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlacementsResponseTypeDef(BaseValidatorModel):
    placements: List[PlacementSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(BaseValidatorModel):
    projects: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
    projectName: str
    description: Optional[str] = None
    placementTemplate: Optional[PlacementTemplateTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ProjectDescriptionTypeDef(BaseValidatorModel):
    projectName: str
    createdDate: datetime
    updatedDate: datetime
    arn: Optional[str] = None
    description: Optional[str] = None
    placementTemplate: Optional[PlacementTemplateTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    projectName: str
    description: Optional[str] = None
    placementTemplate: Optional[PlacementTemplateTypeDef] = None

class DescribeProjectResponseTypeDef(BaseValidatorModel):
    project: ProjectDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

