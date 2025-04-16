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
from aws_resource_validator.pydantic_models.controlcatalog_constants import *

class AssociatedDomainSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class AssociatedObjectiveSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ObjectiveResourceFilter(BaseValidatorModel):
    Arn: Optional[str] = None


class ControlParameter(BaseValidatorModel):
    Name: str


class ControlSummary(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str


class DomainResourceFilter(BaseValidatorModel):
    Arn: Optional[str] = None


class DomainSummary(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    CreateTime: datetime
    LastUpdateTime: datetime


class GetControlRequest(BaseValidatorModel):
    ControlArn: str


class RegionConfiguration(BaseValidatorModel):
    Scope: ControlScopeType
    DeployableRegions: Optional[List[str]] = None


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


class ListControlsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDomainsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ObjectiveSummary(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Domain: AssociatedDomainSummary
    CreateTime: datetime
    LastUpdateTime: datetime


class CommonControlSummary(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Domain: AssociatedDomainSummary
    Objective: AssociatedObjectiveSummary
    CreateTime: datetime
    LastUpdateTime: datetime


class CommonControlFilter(BaseValidatorModel):
    Objectives: Optional[Sequence[ObjectiveResourceFilter]] = None


class ObjectiveFilter(BaseValidatorModel):
    Domains: Optional[Sequence[DomainResourceFilter]] = None


class ImplementationDetails(BaseValidatorModel):
    pass


class GetControlResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Behavior: ControlBehaviorType
    RegionConfiguration: RegionConfiguration
    Implementation: ImplementationDetails
    Parameters: List[ControlParameter]
    ResponseMetadata: ResponseMetadata


class ListControlsResponse(BaseValidatorModel):
    Controls: List[ControlSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDomainsResponse(BaseValidatorModel):
    Domains: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListControlsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectivesResponse(BaseValidatorModel):
    Objectives: List[ObjectiveSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCommonControlsResponse(BaseValidatorModel):
    CommonControls: List[CommonControlSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCommonControlsRequestPaginate(BaseValidatorModel):
    CommonControlFilter: Optional[CommonControlFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCommonControlsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CommonControlFilter: Optional[CommonControlFilter] = None


class ListObjectivesRequestPaginate(BaseValidatorModel):
    ObjectiveFilter: Optional[ObjectiveFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectivesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ObjectiveFilter: Optional[ObjectiveFilter] = None


