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

class AssociatedDomainSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class AssociatedObjectiveSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ObjectiveResourceFilterTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class ControlParameterTypeDef(BaseValidatorModel):
    Name: str


class ControlSummaryTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str


class DomainResourceFilterTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class DomainSummaryTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    CreateTime: datetime
    LastUpdateTime: datetime


class GetControlRequestTypeDef(BaseValidatorModel):
    ControlArn: str


class RegionConfigurationTypeDef(BaseValidatorModel):
    Scope: ControlScopeType
    DeployableRegions: Optional[List[str]] = None


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


class ListControlsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDomainsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ObjectiveSummaryTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    CreateTime: datetime
    LastUpdateTime: datetime


class CommonControlSummaryTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Domain: AssociatedDomainSummaryTypeDef
    Objective: AssociatedObjectiveSummaryTypeDef
    CreateTime: datetime
    LastUpdateTime: datetime


class CommonControlFilterTypeDef(BaseValidatorModel):
    Objectives: Optional[Sequence[ObjectiveResourceFilterTypeDef]] = None


class ObjectiveFilterTypeDef(BaseValidatorModel):
    Domains: Optional[Sequence[DomainResourceFilterTypeDef]] = None


class ImplementationDetailsTypeDef(BaseValidatorModel):
    pass


class GetControlResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Description: str
    Behavior: ControlBehaviorType
    RegionConfiguration: RegionConfigurationTypeDef
    Implementation: ImplementationDetailsTypeDef
    Parameters: List[ControlParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListControlsResponseTypeDef(BaseValidatorModel):
    Controls: List[ControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDomainsResponseTypeDef(BaseValidatorModel):
    Domains: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListControlsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectivesResponseTypeDef(BaseValidatorModel):
    Objectives: List[ObjectiveSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCommonControlsResponseTypeDef(BaseValidatorModel):
    CommonControls: List[CommonControlSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCommonControlsRequestPaginateTypeDef(BaseValidatorModel):
    CommonControlFilter: Optional[CommonControlFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCommonControlsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    CommonControlFilter: Optional[CommonControlFilterTypeDef] = None


class ListObjectivesRequestPaginateTypeDef(BaseValidatorModel):
    ObjectiveFilter: Optional[ObjectiveFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectivesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ObjectiveFilter: Optional[ObjectiveFilterTypeDef] = None


