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
from aws_resource_validator.pydantic_models.kendra_ranking_constants import *

class CapacityUnitsConfigurationTypeDef(BaseValidatorModel):
    RescoreCapacityUnits: int


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteRescoreExecutionPlanRequestTypeDef(BaseValidatorModel):
    Id: str


class DescribeRescoreExecutionPlanRequestTypeDef(BaseValidatorModel):
    Id: str


class DocumentTypeDef(BaseValidatorModel):
    Id: str
    OriginalScore: float
    GroupId: Optional[str] = None
    Title: Optional[str] = None
    Body: Optional[str] = None
    TokenizedTitle: Optional[Sequence[str]] = None
    TokenizedBody: Optional[Sequence[str]] = None


class ListRescoreExecutionPlansRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RescoreExecutionPlanSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[RescoreExecutionPlanStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class RescoreResultItemTypeDef(BaseValidatorModel):
    DocumentId: Optional[str] = None
    Score: Optional[float] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateRescoreExecutionPlanRequestTypeDef(BaseValidatorModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None


class CreateRescoreExecutionPlanRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateRescoreExecutionPlanResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRescoreExecutionPlanResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    Name: str
    Description: str
    CapacityUnits: CapacityUnitsConfigurationTypeDef
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: RescoreExecutionPlanStatusType
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RescoreRequestTypeDef(BaseValidatorModel):
    RescoreExecutionPlanId: str
    SearchQuery: str
    Documents: Sequence[DocumentTypeDef]


class ListRescoreExecutionPlansResponseTypeDef(BaseValidatorModel):
    SummaryItems: List[RescoreExecutionPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RescoreResultTypeDef(BaseValidatorModel):
    RescoreId: str
    ResultItems: List[RescoreResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


