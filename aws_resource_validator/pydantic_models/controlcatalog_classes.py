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
from aws_resource_validator.pydantic_models.controlcatalog_constants import *

class AssociatedDomainSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AssociatedObjectiveSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ObjectiveResourceFilterTypeDef(BaseModel):
    Arn: Optional[str] = None

class DomainResourceFilterTypeDef(BaseModel):
    Arn: Optional[str] = None

class DomainSummaryTypeDef(BaseModel):
    Arn: str
    CreateTime: datetime
    Description: str
    LastUpdateTime: datetime
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ObjectiveSummaryTypeDef(BaseModel):
    Arn: str
    CreateTime: datetime
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    LastUpdateTime: datetime
    Name: str

class CommonControlSummaryTypeDef(BaseModel):
    Arn: str
    CreateTime: datetime
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    LastUpdateTime: datetime
    Name: str
    Objective: AssociatedObjectiveSummaryTypeDef

class CommonControlFilterTypeDef(BaseModel):
    Objectives: Optional[Sequence[ObjectiveResourceFilterTypeDef]] = None

class ObjectiveFilterTypeDef(BaseModel):
    Domains: Optional[Sequence[DomainResourceFilterTypeDef]] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsResponseTypeDef(BaseModel):
    Domains: List[DomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListObjectivesResponseTypeDef(BaseModel):
    NextToken: str
    Objectives: List[ObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommonControlsResponseTypeDef(BaseModel):
    CommonControls: List[CommonControlSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommonControlsRequestListCommonControlsPaginateTypeDef(BaseModel):
    CommonControlFilter: Optional[CommonControlFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCommonControlsRequestRequestTypeDef(BaseModel):
    CommonControlFilter: Optional[CommonControlFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListObjectivesRequestListObjectivesPaginateTypeDef(BaseModel):
    ObjectiveFilter: Optional[ObjectiveFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectivesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ObjectiveFilter: Optional[ObjectiveFilterTypeDef] = None

