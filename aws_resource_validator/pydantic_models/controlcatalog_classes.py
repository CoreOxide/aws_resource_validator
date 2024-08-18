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
from aws_resource_validator.pydantic_models.controlcatalog_constants import *

class AssociatedDomainSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AssociatedObjectiveSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ObjectiveResourceFilterTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class DomainResourceFilterTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class DomainSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreateTime: datetime
    Description: str
    LastUpdateTime: datetime
    Name: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ObjectiveSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreateTime: datetime
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    LastUpdateTime: datetime
    Name: str

class CommonControlSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreateTime: datetime
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    LastUpdateTime: datetime
    Name: str
    Objective: AssociatedObjectiveSummaryTypeDef

class CommonControlFilterTypeDef(BaseValidatorModel):
    Objectives: Optional[Sequence[ObjectiveResourceFilterTypeDef]] = None

class ObjectiveFilterTypeDef(BaseValidatorModel):
    Domains: Optional[Sequence[DomainResourceFilterTypeDef]] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsResponseTypeDef(BaseValidatorModel):
    Domains: List[DomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListObjectivesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Objectives: List[ObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommonControlsResponseTypeDef(BaseValidatorModel):
    CommonControls: List[CommonControlSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCommonControlsRequestListCommonControlsPaginateTypeDef(BaseValidatorModel):
    CommonControlFilter: Optional[CommonControlFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCommonControlsRequestRequestTypeDef(BaseValidatorModel):
    CommonControlFilter: Optional[CommonControlFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListObjectivesRequestListObjectivesPaginateTypeDef(BaseValidatorModel):
    ObjectiveFilter: Optional[ObjectiveFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListObjectivesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ObjectiveFilter: Optional[ObjectiveFilterTypeDef] = None

