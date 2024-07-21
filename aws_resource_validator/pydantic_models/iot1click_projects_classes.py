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
from aws_resource_validator.pydantic_models.iot1click_projects_constants import *

class AssociateDeviceWithPlacementRequestRequestTypeDef(BaseModel):
    projectName: str
    placementName: str
    deviceId: str
    deviceTemplateName: str

class CreatePlacementRequestRequestTypeDef(BaseModel):
    placementName: str
    projectName: str
    attributes: Optional[Mapping[str, str]] = None

class DeletePlacementRequestRequestTypeDef(BaseModel):
    placementName: str
    projectName: str

class DeleteProjectRequestRequestTypeDef(BaseModel):
    projectName: str

class DescribePlacementRequestRequestTypeDef(BaseModel):
    placementName: str
    projectName: str

class PlacementDescriptionTypeDef(BaseModel):
    projectName: str
    placementName: str
    attributes: Dict[str, str]
    createdDate: datetime
    updatedDate: datetime

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeProjectRequestRequestTypeDef(BaseModel):
    projectName: str

class DeviceTemplateTypeDef(BaseModel):
    deviceType: Optional[str] = None
    callbackOverrides: Optional[Mapping[str, str]] = None

class DisassociateDeviceFromPlacementRequestRequestTypeDef(BaseModel):
    projectName: str
    placementName: str
    deviceTemplateName: str

class GetDevicesInPlacementRequestRequestTypeDef(BaseModel):
    projectName: str
    placementName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPlacementsRequestRequestTypeDef(BaseModel):
    projectName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PlacementSummaryTypeDef(BaseModel):
    projectName: str
    placementName: str
    createdDate: datetime
    updatedDate: datetime

class ListProjectsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProjectSummaryTypeDef(BaseModel):
    projectName: str
    createdDate: datetime
    updatedDate: datetime
    arn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePlacementRequestRequestTypeDef(BaseModel):
    placementName: str
    projectName: str
    attributes: Optional[Mapping[str, str]] = None

class DescribePlacementResponseTypeDef(BaseModel):
    placement: PlacementDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicesInPlacementResponseTypeDef(BaseModel):
    devices: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PlacementTemplateTypeDef(BaseModel):
    defaultAttributes: Optional[Mapping[str, str]] = None
    deviceTemplates: Optional[Mapping[str, DeviceTemplateTypeDef]] = None

class ListPlacementsRequestListPlacementsPaginateTypeDef(BaseModel):
    projectName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlacementsResponseTypeDef(BaseModel):
    placements: List[PlacementSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(BaseModel):
    projects: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectRequestRequestTypeDef(BaseModel):
    projectName: str
    description: Optional[str] = None
    placementTemplate: Optional[PlacementTemplateTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ProjectDescriptionTypeDef(BaseModel):
    projectName: str
    createdDate: datetime
    updatedDate: datetime
    arn: Optional[str] = None
    description: Optional[str] = None
    placementTemplate: Optional[PlacementTemplateTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class UpdateProjectRequestRequestTypeDef(BaseModel):
    projectName: str
    description: Optional[str] = None
    placementTemplate: Optional[PlacementTemplateTypeDef] = None

class DescribeProjectResponseTypeDef(BaseModel):
    project: ProjectDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

