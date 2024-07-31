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
from aws_resource_validator.pydantic_models.mobile_constants import *

class BundleDetailsTypeDef(BaseModel):
    bundleId: Optional[str] = None
    title: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    iconUrl: Optional[str] = None
    availablePlatforms: Optional[List[PlatformType]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteProjectRequestRequestTypeDef(BaseModel):
    projectId: str

class ResourceTypeDef(BaseModel):
    type: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    feature: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None

class DescribeBundleRequestRequestTypeDef(BaseModel):
    bundleId: str

class DescribeProjectRequestRequestTypeDef(BaseModel):
    projectId: str
    syncFromResources: Optional[bool] = None

class ExportBundleRequestRequestTypeDef(BaseModel):
    bundleId: str
    projectId: Optional[str] = None
    platform: Optional[PlatformType] = None

class ExportProjectRequestRequestTypeDef(BaseModel):
    projectId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBundlesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProjectSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    projectId: Optional[str] = None

class CreateProjectRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    region: Optional[str] = None
    contents: Optional[BlobTypeDef] = None
    snapshotId: Optional[str] = None

class UpdateProjectRequestRequestTypeDef(BaseModel):
    projectId: str
    contents: Optional[BlobTypeDef] = None

class DescribeBundleResultTypeDef(BaseModel):
    details: BundleDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportBundleResultTypeDef(BaseModel):
    downloadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportProjectResultTypeDef(BaseModel):
    downloadUrl: str
    shareUrl: str
    snapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBundlesResultTypeDef(BaseModel):
    bundleList: List[BundleDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResultTypeDef(BaseModel):
    deletedResources: List[ResourceTypeDef]
    orphanedResources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectDetailsTypeDef(BaseModel):
    name: Optional[str] = None
    projectId: Optional[str] = None
    region: Optional[str] = None
    state: Optional[ProjectStateType] = None
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None
    consoleUrl: Optional[str] = None
    resources: Optional[List[ResourceTypeDef]] = None

class ListBundlesRequestListBundlesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsResultTypeDef(BaseModel):
    projects: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResultTypeDef(BaseModel):
    details: ProjectDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProjectResultTypeDef(BaseModel):
    details: ProjectDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResultTypeDef(BaseModel):
    details: ProjectDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

