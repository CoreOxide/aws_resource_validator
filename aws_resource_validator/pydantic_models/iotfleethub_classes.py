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
from aws_resource_validator.pydantic_models.iotfleethub_constants import *

class ApplicationSummaryTypeDef(BaseModel):
    applicationId: str
    applicationName: str
    applicationUrl: str
    applicationDescription: Optional[str] = None
    applicationCreationDate: Optional[int] = None
    applicationLastUpdateDate: Optional[int] = None
    applicationState: Optional[ApplicationStateType] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    applicationName: str
    roleArn: str
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str
    clientToken: Optional[str] = None

class DescribeApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    clientToken: Optional[str] = None

class CreateApplicationResponseTypeDef(BaseModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationResponseTypeDef(BaseModel):
    applicationId: str
    applicationArn: str
    applicationName: str
    applicationDescription: str
    applicationUrl: str
    applicationState: ApplicationStateType
    applicationCreationDate: int
    applicationLastUpdateDate: int
    roleArn: str
    ssoClientId: str
    errorMessage: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    applicationSummaries: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

