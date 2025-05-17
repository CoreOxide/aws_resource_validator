from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.controlcatalog.controlcatalog_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'get_control' function.
class GetControlRequest(BaseValidatorModel):
    ControlArn: str


class ImplementationDetails(BaseValidatorModel):
    Type: str


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


# This class is the input for the 'list_controls' function.
class ListControlsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_domains' function.
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
    Objectives: Optional[List[ObjectiveResourceFilter]] = None


class ObjectiveFilter(BaseValidatorModel):
    Domains: Optional[List[DomainResourceFilter]] = None


# This class is the output for the 'get_control' function.
class GetControlResponse(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Behavior: ControlBehaviorType
    RegionConfiguration: RegionConfiguration
    Implementation: ImplementationDetails
    Parameters: List[ControlParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_controls' function.
class ListControlsResponse(BaseValidatorModel):
    Controls: List[ControlSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_domains' function.
class ListDomainsResponse(BaseValidatorModel):
    Domains: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListControlsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_objectives' function.
class ListObjectivesResponse(BaseValidatorModel):
    Objectives: List[ObjectiveSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_common_controls' function.
class ListCommonControlsResponse(BaseValidatorModel):
    CommonControls: List[CommonControlSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCommonControlsRequestPaginate(BaseValidatorModel):
    CommonControlFilter: Optional[CommonControlFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_common_controls' function.
class ListCommonControlsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CommonControlFilter: Optional[CommonControlFilter] = None


class ListObjectivesRequestPaginate(BaseValidatorModel):
    ObjectiveFilter: Optional[ObjectiveFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_objectives' function.
class ListObjectivesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ObjectiveFilter: Optional[ObjectiveFilter] = None