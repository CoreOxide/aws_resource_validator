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
from aws_resource_validator.pydantic_models.mobile_constants import *

class BundleDetailsTypeDef(BaseValidatorModel):
    bundleId: Optional[str] = None
    title: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    iconUrl: Optional[str] = None
    availablePlatforms: Optional[List[PlatformType]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str

class ResourceTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    feature: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None

class DescribeBundleRequestRequestTypeDef(BaseValidatorModel):
    bundleId: str

class DescribeProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    syncFromResources: Optional[bool] = None

class ExportBundleRequestRequestTypeDef(BaseValidatorModel):
    bundleId: str
    projectId: Optional[str] = None
    platform: Optional[PlatformType] = None

class ExportProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBundlesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProjectSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    projectId: Optional[str] = None

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    region: Optional[str] = None
    contents: Optional[BlobTypeDef] = None
    snapshotId: Optional[str] = None

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    projectId: str
    contents: Optional[BlobTypeDef] = None

class DescribeBundleResultTypeDef(BaseValidatorModel):
    details: BundleDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportBundleResultTypeDef(BaseValidatorModel):
    downloadUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportProjectResultTypeDef(BaseValidatorModel):
    downloadUrl: str
    shareUrl: str
    snapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBundlesResultTypeDef(BaseValidatorModel):
    bundleList: List[BundleDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResultTypeDef(BaseValidatorModel):
    deletedResources: List[ResourceTypeDef]
    orphanedResources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectDetailsTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    projectId: Optional[str] = None
    region: Optional[str] = None
    state: Optional[ProjectStateType] = None
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None
    consoleUrl: Optional[str] = None
    resources: Optional[List[ResourceTypeDef]] = None

class ListBundlesRequestListBundlesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsResultTypeDef(BaseValidatorModel):
    projects: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResultTypeDef(BaseValidatorModel):
    details: ProjectDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProjectResultTypeDef(BaseValidatorModel):
    details: ProjectDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResultTypeDef(BaseValidatorModel):
    details: ProjectDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

